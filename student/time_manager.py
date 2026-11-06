"""
Module time_manager.py – Quản trị ngân sách thời gian thực thi cho Chess Engine.

Đặc thù môi trường thi đấu ChessLab:
1. Mỗi bên có tổng thời gian ban đầu (thường là 180s - 360s, không có thời gian cộng thêm increment).
2. Hệ thống GameController áp đặt độ trễ tối thiểu ngẫu nhiên 500ms - 1000ms cho mỗi nước đi.
   Khoảng thời gian này trừ trực tiếp vào đồng hồ thi đấu của bot.
3. Bot bị xử thua ngay lập tức nếu đồng hồ về 0 (timeout / rụng kim).

Giải pháp thiết kế:
- Tính toán ngân sách linh hoạt theo từng giai đoạn ván đấu (khai cuộc, trung cuộc, tàn cuộc).
- Nhận thức độ trễ hệ thống (_AVG_SYSTEM_DELAY_MS = 700ms) để giới hạn số nước đi vật lý tối đa.
- Kích hoạt chế độ Kiếp Nạn Hoảng Loạn (Panic Mode: 40ms) khi thời gian còn dưới 3.5s.
- Sử dụng đồng hồ đơn điệu chuẩn xác time.monotonic() để tránh lỗi trôi thời gian hệ thống.
"""

from __future__ import annotations

import time

# ---------------------------------------------------------------------------
# CÁC HẰNG SỐ CẤU HÌNH THỜI GIAN
# ---------------------------------------------------------------------------

# Dự phòng an toàn (Safety buffer): trừ hao độ trễ overhead gọi hàm và trả kết quả
_OVERHEAT_MS = 60

# Ngưỡng thời gian nguy cấp (Critical threshold): dưới 8 giây còn lại
_CRITICAL_MS = 8_000

# Ngưỡng hoảng loạn (Panic threshold): dưới 3.5 giây còn lại
# Với độ trễ 500ms-1000ms của hệ thống, 3.5s chỉ còn đủ cho khoảng 3-4 nước đi
_PANIC_MS = 3_500

# Độ trễ trung bình do GameController áp đặt (500ms - 1000ms => trung bình ~700ms)
_AVG_SYSTEM_DELAY_MS = 700


def compute_budget_ms(
    time_remaining_ms: int,
    ply: int,
    initial_time_ms: int,
) -> int:
    """
    Tính toán ngân sách thời gian tìm kiếm tối ưu (ms) cho lượt đi hiện tại.

    Thuật toán phân bổ thời gian thích ứng (Adaptive Time Allocation):
    1. Trừ hao an toàn (_OVERHEAT_MS) để tính thời gian khả dụng thực tế.
    2. Chế độ Hoảng loạn (Panic Mode - dưới 3.5s): Ép ngân sách xuống 40ms,
       nhường toàn bộ thời gian cho độ trễ 500ms của hệ thống, chống rụng kim.
    3. Chế độ Nguy cấp (Critical Mode - dưới 8s): Thu hẹp ngân sách trong khoảng 50ms - 150ms.
    4. Ước tính số nước đi còn lại (moves_left) theo số ply đã qua:
       - Khai cuộc (< 10 nước): 35 nước.
       - Trung cuộc sớm (< 30 nước): 30 nước.
       - Trung cuộc muộn (< 50 nước): 25 nước.
       - Tàn cuộc (>= 50 nước): 20 nước.
    5. Điều chỉnh theo số nước đi vật lý tối đa cho phép bởi độ trễ hệ thống:
       max_physical_moves = safe_remaining // 700ms.
    6. Áp trần ngân sách không vượt quá 12% quỹ thời gian còn lại và sàn tối thiểu 60ms.

    Args:
        time_remaining_ms: Tổng thời gian thi đấu còn lại của bot (ms).
        ply: Số nửa nước đi (half-moves) đã trôi qua kể từ đầu ván.
        initial_time_ms: Tổng thời gian ban đầu được cấp (ms).

    Returns:
        int: Ngân sách thời gian (ms) dành riêng cho lượt tìm kiếm này.
    """
    safe_remaining = max(0, time_remaining_ms - _OVERHEAT_MS)

    # 1. Chế độ Hoảng loạn (Panic Mode): còn dưới 3.5s
    # Phải đi cực nhanh (40ms) để nhường toàn bộ thời gian cho độ trễ 500ms của hệ thống
    if safe_remaining < _PANIC_MS:
        return 40

    # 2. Chế độ Nguy cấp (Critical Mode): còn dưới 8s
    if safe_remaining < _CRITICAL_MS:
        return max(50, min(150, safe_remaining // 15))

    # 3. Ước tính số nước đi còn lại theo tiến độ thực tế của ván cờ
    moves_played = ply // 2
    if moves_played < 10:
        moves_left = 35
    elif moves_played < 30:
        moves_left = 30
    elif moves_played < 50:
        moves_left = 25
    else:
        moves_left = 20

    # Giới hạn số nước đi thực tế tối đa mà đồng hồ cho phép với độ trễ ~700ms của GameController
    max_physical_moves = max(1, safe_remaining // _AVG_SYSTEM_DELAY_MS)
    moves_left = min(moves_left, max_physical_moves)

    # Ngân sách cơ sở phân bổ đều cho số nước dự kiến
    budget = safe_remaining // moves_left

    # Giới hạn trần tối đa không tiêu tốn quá 12% quỹ thời gian còn lại trong một nước
    max_allowed = max(100, safe_remaining * 12 // 100)
    budget = min(budget, max_allowed)

    # Đảm bảo ngân sách sàn tối thiểu từ 60ms trở lên
    return max(budget, 60)


class TimeManager:
    """
    Bộ quản lý đồng hồ đơn điệu và deadline cho từng lượt tìm kiếm của bot.

    Sử dụng time.monotonic() thay cho time.time() để đảm bảo tính đơn điệu tuyệt đối,
    không bao giờ bị lỗi thời gian âm do chỉnh giờ hệ thống hay đồng bộ mạng NTP.
    """

    def __init__(self, budget_ms: int) -> None:
        """
        Khởi tạo TimeManager với ngân sách thời gian cho trước.

        Args:
            budget_ms: Ngân sách thời gian (mili-giây) tối đa cho lượt tìm kiếm này.
        """
        self.budget_ms = budget_ms
        self._start_time: float = 0.0
        self._deadline: float = 0.0

    def start(self) -> None:
        """Bắt đầu bấm giờ và xác lập mốc thời gian hết hạn (deadline)."""
        self._start_time = time.monotonic()
        self._deadline = self._start_time + self.budget_ms / 1000.0

    def should_stop(self) -> bool:
        """
        Kiểm tra xem lượt tìm kiếm hiện tại đã chạm deadline hay chưa.

        Được gọi định kỳ trong các vòng lặp đệ quy của Negamax và Quiescence Search
        (thường sau mỗi 512 nodes để giảm thiểu chi phí gọi hàm hệ thống).

        Returns:
            bool: True nếu đã hết thời gian cho phép, ngược lại False.
        """
        return time.monotonic() >= self._deadline

    def elapsed_ms(self) -> int:
        """
        Tính số mili-giây đã trôi qua kể từ khi start().

        Returns:
            int: Thời gian đã sử dụng (ms).
        """
        return int((time.monotonic() - self._start_time) * 1000)

    def can_start_next_depth(self) -> bool:
        """
        Kiểm tra xem có đủ thời gian an toàn để mở thêm một tầng độ sâu mới hay không.

        Nguyên lý toán học: Hệ số rẽ nhánh hữu hiệu (Effective Branching Factor - EBF)
        của thuật toán Alpha-Beta trong cờ vua thường dao động từ 3 đến 5. Do đó,
        thời gian cần thiết cho độ sâu (d + 1) sẽ gấp khoảng 3 - 5 lần độ sâu d.
        Nếu thời gian đã trôi qua vượt quá 55% tổng ngân sách, việc mở thêm tầng mới
        sẽ không kịp hoàn thành và gây lãng phí tài nguyên tính toán.

        Returns:
            bool: True nếu thời gian đã dùng < 55% ngân sách, ngược lại False.
        """
        used = self.elapsed_ms()
        return used < int(self.budget_ms * 0.55)
