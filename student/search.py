from __future__ import annotations

from typing import Any, NamedTuple
import chess

from .time_manager import TimeManager

# =========================================================================
# 1. HẰNG SỐ VÀ CÁC CỜ CỦA TRANSPOSITION TABLE
# =========================================================================
TT_SIZE = 1 << 18       # 262,144 mục (vừa vặn RAM, tốc độ O(1))
MATE_SCORE = 30_000     # Điểm quy ước khi chiếu hết
MATE_THRESHOLD = 29_000 # Ngưỡng nhận diện điểm chiếu hết

# 3 loại cận (bound) trong thuật toán Alpha-Beta
TT_EXACT = 0  # Điểm chính xác (alpha < score < beta)
TT_LOWER = 1  # Cận dưới / Fail-high (score >= beta)
TT_UPPER = 2  # Cận trên / Fail-low  (score <= alpha)


def score_to_tt(score: int, ply: int) -> int:
    """Chuẩn hóa điểm chiếu hết theo độ sâu (ply) trước khi lưu vào TT."""
    if score >= MATE_THRESHOLD:
        return score + ply
    elif score <= -MATE_THRESHOLD:
        return score - ply
    return score


def score_from_tt(score: int, ply: int) -> int:
    """Khôi phục lại điểm chiếu hết theo đúng khoảng cách ply khi lấy từ TT ra."""
    if score >= MATE_THRESHOLD:
        return score - ply
    elif score <= -MATE_THRESHOLD:
        return score + ply
    return score


# =========================================================================
# 2. CẤU TRÚC DỮ LIỆU TRANSPOSITION TABLE
# =========================================================================
class TTEntry(NamedTuple):
    key: Any                     # Khóa băm Zobrist của bàn cờ
    depth: int                   # Độ sâu đã duyệt
    score: int                   # Điểm đánh giá (đã qua score_to_tt)
    flag: int                    # TT_EXACT, TT_LOWER, hoặc TT_UPPER
    best_move: chess.Move | None # Nước đi tốt nhất tìm thấy tại vị trí này
    age: int                     # Số thứ tự lượt đi của ván cờ


class TranspositionTable:
    """Bảng băm kích thước cố định với cơ chế băm bitmask O(1) và thay thế tối ưu."""

    def __init__(self, size: int = TT_SIZE) -> None:
        self.size = size
        self._table: dict[int, TTEntry] = {}

    def probe(self, key: Any) -> TTEntry | None:
        """Tra cứu trạng thái bàn cờ trong bảng băm."""
        idx = hash(key) & (self.size - 1)
        entry = self._table.get(idx)
        if entry is not None and entry.key == key:
            return entry
        return None

    def store(
        self,
        key: Any,
        depth: int,
        score: int,
        flag: int,
        best_move: chess.Move | None,
        age: int,
    ) -> None:
        """
        Lưu hoặc ghi đè trạng thái:
        - Ghi đè nếu ô còn trống.
        - Ghi đè nếu ô chứa dữ liệu của lượt đi cũ (age != existing.age).
        - Ghi đè nếu lượt tìm kiếm mới sâu hơn hoặc bằng (depth >= existing.depth).
        """
        idx = hash(key) & (self.size - 1)
        existing = self._table.get(idx)
        if (
            existing is None
            or existing.age != age
            or depth >= existing.depth
        ):
            self._table[idx] = TTEntry(key, depth, score, flag, best_move, age)

    def clear(self) -> None:
        """Xóa sạch bảng băm khi bắt đầu trận đấu mới."""
        self._table.clear()


# =========================================================================
# 3. LỚP SEARCHER ĐÃ ĐƯỢC TÍCH HỢP BẢNG CHUYỂN VỊ
# =========================================================================
class Searcher:
    """
    Yêu cầu dự kiến:
    - Thuật toán lõi: Negamax với Alpha-Beta Pruning (Thành viên 1).
    - Tìm kiếm sâu dần: Iterative Deepening Search (IDS) (Thành viên 1 & 2).
    - Mở rộng chống hiệu ứng đường chân trời: Quiescence Search (QS) (Thành viên 2).
    - Cấu trúc tăng tốc:
        + Transposition Table (TT) -> ĐÃ HOÀN THIỆN BỞI Văn Bách
        + Move Ordering (MVV-LVA, Killer, History) -> Chờ Thành viên 2.
    """

    def __init__(self) -> None:
        """
        Khởi tạo các cấu trúc dữ liệu dùng chung giữa các lượt đi.
        """
        # [ĐÃ LÀM XONG]: Bảng chuyển vị và quản lý tuổi ván cờ 
        self.tt = TranspositionTable(TT_SIZE)
        self._age: int = 0
        self._nodes: int = 0

        # TODO (Thành viên 2): Khởi tạo Killer Moves và History Heuristic tại đây nếu cần.

    def search(self, board: chess.Board, tm: TimeManager) -> chess.Move:
        """
        Tìm kiếm và trả về nước đi tối ưu nhất cho bên đi hiện tại.
        ----------------------------------------------------
        1. INPUT:
           - board (chess.Board): Trạng thái bàn cờ hiện tại (hỗ trợ cả chuẩn FEN lẫn Chess960).
           - tm (TimeManager): Bộ điều phối thời gian cho lượt đi này.
           
        2. OUTPUT:
           - Trả về một đối tượng `chess.Move` BẮT BUỘC nằm trong `list(board.legal_moves)`.
           
        3. RÀNG BUỘC THỜI GIAN (TIME INVARIANTS):
           - Bắt đầu tìm kiếm: gọi `tm.start()`.
           - Trước mỗi vòng lặp độ sâu mới (IDS): kiểm tra `if not tm.can_start_next_depth(): break`.
           - Trong các nút tìm kiếm đệ quy: định kỳ kiểm tra `if tm.should_stop(): break/return`.
           
        4. TÍNH BẤT BIẾN BÀN CỜ (BOARD IMMUTABILITY):
           - Tuyệt đối mọi lệnh `board.push(move)` trong lúc duyệt cây đều phải có `board.pop()` tương ứng.
           - Khi hàm này trả về (dù bình thường hay ngắt do hết giờ), `board.fen()` phải GIỮ NGUYÊN 100%
             như lúc nhận vào.
        """
        legal_moves = list(board.legal_moves)
        if not legal_moves:
            return chess.Move.null()

        if len(legal_moves) == 1:
            return legal_moves[0]

        # Bắt đầu tính giờ và tăng tuổi ván cờ
        tm.start()
        self._age += 1
        self._nodes = 0

        # Lấy khóa băm của thế cờ hiện tại (python-chess hỗ trợ hoàn hảo cả Chess960)
        board_key = board._transposition_key()

        # =========================================================================
        # [MẪU DÙNG TT 1]: Tra cứu TT ở gốc bàn cờ (Root Probe)
        # =========================================================================
        entry = self.tt.probe(board_key)
        if entry is not None and entry.best_move in legal_moves:
            best_move = entry.best_move
        else:
            best_move = legal_moves[0]

        # =========================================================================
        # MOCK IMPLEMENTATION (Dành cho việc chạy thử và test tích hợp bot.py)
        # TODO (Thành viên 1 & 2): Thay thế đoạn mock này bằng vòng lặp
        # Iterative Deepening và hàm đệ quy Negamax Alpha-Beta thật.
        # =========================================================================
        for move in legal_moves:
            if board.is_capture(move):
                best_move = move
                break

        # =========================================================================
        # [MẪU DÙNG TT 2]: Lưu nước đi tốt nhất tìm được vào TT (Root Store)
        # =========================================================================
        self.tt.store(
            key=board_key,
            depth=1,
            score=score_to_tt(0, ply=0),
            flag=TT_EXACT,
            best_move=best_move,
            age=self._age,
        )

        return best_move