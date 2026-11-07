# BÁO CÁO KHAI BÁO SỬ DỤNG CÔNG CỤ TRÍ TUỆ NHÂN TẠO (AI_USAGE.MD)
## DỰ ÁN: BOT CỜ VUA CHESSLAB (CHESS960) — MÔN HỌC: BIỂU DIỄN TRI THỨC VÀ TÌM KIẾM NÂNG CAO
### NHÓM THỰC HIỆN: NHÓM 12 

---

## LỜI MỞ ĐẦU

Tài liệu này được lập nhằm mục đích minh bạch hóa toàn bộ quá trình sử dụng các công cụ Trí tuệ Nhân tạo trong quá trình nghiên cứu, thiết kế thuật toán, hiện thực mã nguồn và kiểm thử sản phẩm bot cờ vua ChessLab, tuân thủ các quy định tại:
**Quy chế Bài tập lớn trong `README.md`**: Cho phép sử dụng công cụ AI hỗ trợ lập trình nhưng nghiêm cấm tuyệt đối việc sử dụng Machine Learning / Deep Learning, mô hình đã huấn luyện sẵn, sách khai cuộc (opening book), cơ sở dữ liệu tàn cuộc (endgame tablebases) hoặc gọi engine cờ vua bên ngoài (như Stockfish). Toàn bộ mã nguồn phải được xây dựng dựa trên thuật toán tìm kiếm và hàm đánh giá heuristic truyền thống; sinh viên phải hiểu, giải thích và bảo vệ được từng dòng mã nguồn trước giảng viên.

> **Nguyên tắc phân định kiểm toán:** Tài liệu này phân biệt rạch ròi giữa **nhiệm vụ được giao theo kế hoạch**, **mã nguồn thực tế trong repository**, **phần việc AI hỗ trợ** và **phần sinh viên tự nghiên cứu, kiểm chứng**. Các nội dung chưa có dữ liệu lịch sử xác minh từ từng thành viên sẽ được gắn nhãn trạng thái minh bạch để thành viên bổ sung trước khi nộp bài chính thức.

---

## PHẦN I. KHAI BÁO SỬ DỤNG AI THEO TỪNG THÀNH VIÊN

---

### 1. THÀNH VIÊN 1
- **Họ và tên / MSSV:** *Vũ Hoàng Long / 25022922*
- **Tài khoản Git ghi nhận:** *long8807*

#### 1.1. Vai trò trong dự án
- **Theo kế hoạch nhóm:** Chịu trách nhiệm trụ cột *Duyệt không gian trạng thái trò chơi đối kháng & Cắt tỉa toán học*. Phụ trách khối lõi thuật toán trong `student/search.py`: Negamax, Alpha-Beta Pruning, Đào sâu lặp (Iterative Deepening Search - IDS), Cửa sổ kỳ vọng (Aspiration Windows), Principal Variation Search (PVS), chuẩn hóa điểm chiếu hết theo độ sâu, an toàn bàn cờ `board.push()` / `board.pop()`.

#### 1.2. Công cụ AI sử dụng
| Công cụ AI | Mục đích sử dụng |
|---|---|
| **Gemini** | Giải thích nguyên lý các thuật toán tìm kiếm; gợi ý cách kiểm tra thao tác `board.push()` / `board.pop()` và cách sử dụng Transposition Table; rà soát điều kiện cắt tỉa trong Negamax và gợi ý lựa chọn độ sâu cho LMR. |
#### 1.3. Nội dung AI hỗ trợ
| Nhóm công việc | Nội dung AI hỗ trợ | Cách thành viên sử dụng kết quả |
|---|---|---|
| **Giải thích thuật toán tìm kiếm** | Giải thích cách Negamax kết hợp Alpha-Beta, cách nhận diện trạng thái thắng/thua/hòa và cách các thuật toán tìm kiếm nước đi trong giới hạn thời gian. | Tự đọc, chọn lọc và áp dụng phần phù hợp khi hiện thực, sau đó chạy thử để kiểm tra thuật toán và hành vi của bot. |
| **Rà soát trạng thái bàn cờ và cắt tỉa** | Gợi ý kiểm tra việc hoàn tác trạng thái sau `push()` bằng `pop()` và rà soát điều kiện cắt tỉa trong Negamax; trao đổi về việc dùng Transposition Table để tra cứu kết quả/nước đi đã lưu. | Tự đối chiếu với luồng tìm kiếm trong mã nguồn và kiểm tra lại các hàm sau khi chỉnh sửa. |
| **Tham khảo tham số LMR** | Hướng dẫn các yếu tố cần cân nhắc khi chọn độ sâu giảm cho Late Move Reductions (LMR). | Tự đánh giá và thử nghiệm trên bot; không áp dụng máy móc gợi ý của AI. |

#### 1.4. Ví dụ tương tác AI tiêu biểu
- **Vấn đề kỹ thuật:** Cách dùng Transposition Table để tham khảo nước đi tốt nhất, điều kiện cắt tỉa trong Negamax và độ sâu phù hợp cho LMR.
- **Yêu cầu đặt ra cho AI:** Giải thích cách kiểm tra nước đi tốt nhất trong Transposition Table, rà soát điều kiện cắt tỉa trong Negamax và hướng dẫn các yếu tố để lựa chọn độ sâu giảm cho LMR.
- **Kết quả nhận được:** Gemini giải thích cách tham khảo thông tin đã lưu trong Transposition Table, các điều kiện cắt tỉa cần xem xét và cách cân nhắc độ sâu giảm cho LMR.
- **Đánh giá và áp dụng:** Thành viên tự đối chiếu các gợi ý với mã nguồn, thử chạy các hàm để phát hiện lỗi và quan sát lựa chọn nước đi, gồm việc ưu tiên ăn quân có giá trị cao hoặc tìm cơ hội chiếu hết sớm. Các gợi ý được dùng để tham khảo, không thay thế việc tự quyết định và kiểm chứng.

#### 1.5. Phân định phạm vi đóng góp
- **Phần AI đóng góp:** Giải thích thuật toán và gợi ý rà soát Negamax, Transposition Table, thao tác `push()` / `pop()` và tham số LMR; không trực tiếp quyết định hay xác nhận tính đúng đắn của mã nguồn.
- **Phần thành viên tự thực hiện:** Tự hiện thực và điều chỉnh Negamax, kiểm tra trạng thái kết thúc ván, tìm kiếm nước đi trong giới hạn thời gian và các kỹ thuật tìm kiếm thuộc phần được phân công; tự kiểm tra mã nguồn và quyết định có áp dụng từng gợi ý hay không.
#### 1.6. Phương pháp kiểm chứng đã thực hiện
- Tự chạy thử các hàm tìm kiếm để kiểm tra lỗi khi thực thi và kiểm tra việc xử lý các trạng thái thắng, thua, hòa.
- Quan sát lựa chọn nước đi trong các tình huống thử, kiểm tra bot có cân nhắc ăn quân giá trị cao và cơ hội chiếu hết sớm hay không.
- Đối chiếu luồng cập nhật/hoàn tác trạng thái bàn cờ và các điều kiện cắt tỉa trong mã nguồn sau khi nhận gợi ý.

---


### 2. THÀNH VIÊN 2
- **Họ và tên / MSSV:** *Lê Văn Việt / 25023069*
- **Tài khoản Git ghi nhận:** *thocuong354-cloud*

#### 2.1. Vai trò trong dự án
- **Theo kế hoạch nhóm:** Chịu trách nhiệm trụ cột *Biểu diễn tri thức chuyên gia & Hàm lượng giá trạng thái (Heuristic Evaluation)*. Xây dựng toàn bộ module `student/evaluation.py`: hệ thống PeSTO Piece-Square Tables (trung cuộc và tàn cuộc), cơ chế Tapered Evaluation theo Game Phase (0..24), cấu trúc Tốt (tốt thông, tốt thông liên kết, tốt cô lập, tốt chồng), hoạt động quân (cặp tượng, xe cột mở/nửa mở/hàng 7, mã tiền đồn), an toàn Vua (Pawn Shield) và nhịp đi (Tempo Bonus).

#### 2.2. Công cụ AI sử dụng
| Công cụ AI | Mục đích sử dụng |
|---|---|
| **ChatGPT (OpenAI)** | Hỗ trợ đọc và đối chiếu yêu cầu thành viên B với module `evaluation.py`, rà soát mã nguồn và xác định các tiêu chí cần kiểm chứng. |
| **ChatGPT (OpenAI)** | Hỗ trợ xây dựng bộ kiểm thử độc lập `test_evaluation.py` cho tính đối xứng Chess960, ưu thế vật chất, quy ước dấu Negamax và hiệu năng. |
| **ChatGPT (OpenAI)** | Hướng dẫn khắc phục lỗi môi trường Python, cài đặt thư viện `python-chess`, thực thi kiểm thử và hoàn thiện tài liệu khai báo AI. |

#### 2.3. Nội dung AI hỗ trợ
| Nhóm công việc | Nội dung AI hỗ trợ | Cách thành viên sử dụng kết quả |
|---|---|---|
| **Rà soát hàm lượng giá** | Đối chiếu các thành phần PeSTO PST, Tapered Evaluation, Game Phase, cấu trúc Tốt, hoạt động quân, an toàn Vua và Tempo Bonus với kế hoạch nhóm. | Tham khảo nhận xét để kiểm tra mức độ hoàn thiện của module và xác định các tiêu chí cần kiểm thử thực tế. |
| **Thiết kế bộ kiểm thử** | Hỗ trợ xây dựng file kiểm thử riêng để kiểm tra 960 thế xuất phát Chess960, tính đối xứng, ưu thế vật chất, quy ước dấu Negamax và tốc độ đánh giá. | Sử dụng file test để chuẩn bị kiểm chứng module `evaluation.py`, chạy thử và theo dõi các lỗi phát sinh. |
| **Phân tích lỗi và hỗ trợ tài liệu** | Giải thích các lỗi `ModuleNotFoundError`, hướng dẫn kiểm tra đường dẫn, tên module và môi trường Python; hỗ trợ trình bày báo cáo khai báo AI. | Đối chiếu hướng dẫn với môi trường VS Code, điều chỉnh cách thực thi và rà soát nội dung báo cáo trước khi nộp. |

#### 2.4. Ví dụ tương tác AI tiêu biểu
- **Vấn đề kỹ thuật:** Cần xác định module `evaluation.py` có đáp ứng đầy đủ các yêu cầu về hàm lượng giá Chess960, tính đối xứng, ưu thế vật chất và hiệu năng hay không.
- **Yêu cầu đặt ra cho AI:** Đối chiếu file `evaluation.py` với kế hoạch phân công của nhóm, đánh giá mức độ hoàn thiện, tạo bộ kiểm thử độc lập và hướng dẫn thực thi trong VS Code.
- **Kết quả nhận được:** ChatGPT hỗ trợ rà soát các chức năng của module, xây dựng file `test_evaluation.py`, hướng dẫn cài đặt thư viện `python-chess` và giải thích nguyên nhân lỗi khi chạy kiểm thử.
- **Đánh giá và áp dụng:** Thành viên tham khảo các nhận xét, thử thực thi chương trình và xác định những vấn đề liên quan đến môi trường Python. Quá trình kiểm thử chưa hoàn tất do lỗi không tìm thấy module `test_evaluation`, vì vậy chưa thể xác nhận toàn bộ tiêu chí đều đạt yêu cầu.

#### 2.5. Phân định phạm vi đóng góp
- **Phần AI đóng góp:** Hỗ trợ phân tích yêu cầu kỹ thuật, rà soát module `evaluation.py`, xây dựng bộ kiểm thử độc lập, giải thích lỗi môi trường và hỗ trợ biên soạn tài liệu. Các nội dung AI hỗ trợ sinh hoặc chỉnh sửa mã nguồn trực tiếp trong những lần làm việc khác cần được khai báo bổ sung nếu có.
- **Phần thành viên tự thực hiện:** Chịu trách nhiệm về module `student/evaluation.py`, lựa chọn và kiểm tra mã nguồn đưa vào repository, thực hiện kiểm thử, đánh giá kết quả và giải thích các thuật toán PeSTO, Tapered Evaluation, Game Phase, Bitboard, cấu trúc Tốt và quy ước dấu Negamax.

#### 2.6. Phương pháp kiểm chứng đã thực hiện
- Đối chiếu cấu trúc và các thành phần của `evaluation.py` với yêu cầu kỹ thuật được phân công trong kế hoạch nhóm.
- Kiểm tra cú pháp Python và rà soát các chức năng đánh giá vị trí, cấu trúc Tốt, hoạt động quân và an toàn Vua.
- Thử thực thi chương trình và xử lý vấn đề thiếu thư viện `python-chess` trong môi trường Python.
- Thử chạy bộ kiểm thử độc lập bằng `unittest`, phát hiện lỗi không tìm thấy module `test_evaluation`.
- **Chưa xác nhận:** Kết quả kiểm thử toàn bộ 960 thế Chess960, ưu thế vật chất tối thiểu 800 centipawn và tốc độ tối thiểu 40.000 evaluations/giây. Các kết quả này cần được bổ sung sau khi kiểm thử thành công.

---

### 3. THÀNH VIÊN 3
- **Họ và tên / MSSV:** đỗ thành vương/25023079
- **Tài khoản Git ghi nhận:** dovuong28122007-spec

#### 3.1. Vai trò trong dự án
- **Theo kế hoạch nhóm:** Chịu trách nhiệm trụ cột *Sắp xếp nước đi tối ưu (Move Ordering) & Triệt tiêu hiệu ứng chân trời*. Hiện thực các kỹ thuật nâng cao hiệu năng trong `student/search.py`: hàm sắp xếp nước đi `_order_moves`, thuật toán đánh giá đổi quân tĩnh 1-ply `see()`, Tìm kiếm tĩnh lặng `_quiescence()`, Delta Pruning, Null Move Pruning (NMP) và Late Move Reductions (LMR).

#### 3.2. Công cụ AI sử dụng
| Công cụ AI | Mục đích sử dụng |
|---|---|
|open AI|Hỗ trợ phân tích nguyên lý và đề xuất cách triển khai SEE, Quiescence Search|
|open AI|Hỗ trợ xây dựng điều kiện cắt tỉa trong Delta Pruning và Null Move Pruning|
|open AI|Hỗ trợ rà soát logic các thuật toán tối ưu tìm kiếm và những trường hợp đặc biệt|
#### 3.3. Nội dung AI hỗ trợ
| Nhóm công việc | Nội dung AI hỗ trợ | Cách thành viên sử dụng kết quả |
|Static Exchange Evaluation (SEE)|Gợi ý phương pháp đánh giá trao đổi quân dựa trên giá trị quân và khả năng bị ăn lại|Tham khảo và tích hợp phiên bản đánh giá trao đổi quân đơn giản vào see()|
|Quiescence Search và Delta Pruning|Phân tích Horizon Effect, điều kiện stand-pat và thời điểm áp dụng Delta Pruning|Sử dụng mã gợi ý để bổ sung _quiescence() và điều chỉnh thứ tự kiểm tra điều kiện cắt tỉa|
|Null Move Pruning và LMR|Giải thích điều kiện áp dụng cắt tỉa, giảm độ sâu và các trường hợp có thể gây sai lệch kết quả|Tham khảo logic để bổ sung NMP và rà soát các điều kiện tìm kiếm trong _negamax()|

#### 3.4. Ví dụ tương tác AI tiêu biểu
- **Vấn đề kỹ thuật:** Delta Pruning có thể không phát huy tác dụng nếu điều kiện cắt tỉa được kiểm tra sau khi cập nhật alpha bằng stand_pat
- **Yêu cầu đặt ra cho AI:** Phân tích logic của Delta Pruning trong Quiescence Search và đề xuất cách sắp xếp lại điều kiện để tránh phép kiểm tra không hiệu quả
- **Kết quả nhận được:** AI đề xuất kiểm tra điều kiện stand_pat + margin < alpha trước khi cập nhật alpha, đồng thời xem xét các trường hợp phong cấp
- **Đánh giá và áp dụng:** Sử dụng đề xuất để chỉnh sửa phần Delta Pruning trong _quiescence(). Việc kiểm thử toàn bộ hệ thống chưa được xác nhận hoàn tất

#### 3.5. Phân định phạm vi đóng góp
- **Phần AI đóng góp:** Giải thích nguyên lý các thuật toán tối ưu tìm kiếm, đề xuất mã nguồn và hỗ trợ phân tích những điều kiện logic phức tạp
- **Phần thành viên tự thực hiện:** Lựa chọn các đoạn mã phù hợp, đưa vào student/search.py, chỉnh sửa theo cấu trúc dự án và thực hiện các lệnh kiểm tra trong môi trường phát triển
#### 3.6. Phương pháp kiểm chứng đã thực hiện
Sử dụng python -m py_compile và compileall để kiểm tra cú pháp mã nguồn

Sử dụng pytest để kiểm tra khả năng tích hợp với các thành phần của dự án

Phân tích thông báo lỗi và traceback để xác định các vấn đề liên quan đến Search và các module phụ thuộc

Kết quả kiểm tra cú pháp đạt; các bài kiểm thử tích hợp vẫn còn trường hợp thất bại, chưa xác nhận toàn bộ thuật toán hoạt động chính xác

---

### 4. THÀNH VIÊN 4
- **Họ và tên / MSSV:** *Nông Văn Bách/ 25022782*
- **Tài khoản Git ghi nhận:** *nvb_07.wbai*

#### 4.1. Vai trò trong dự án
- **Theo kế hoạch phân công:** Chịu trách nhiệm trụ cột *Quản trị trạng thái (TT), Đồng hồ thi đấu thực tế & Kiến trúc hệ thống chống sập*. Hiện thực toàn bộ `student/time_manager.py`, hoàn thiện điểm vào `student/bot.py`, hiện thực khối Transposition Table trong `student/search.py`, điều phối tích hợp hệ thống, quản lý quy trình Git/QA, hoàn thiện `team.json`, `AI_USAGE.md` và gắn tag `submission-final`.

#### 4.2. Công cụ AI sử dụng
| Công cụ AI | Mục đích sử dụng |
|---|---|
| **Gemini / Google Antigravity** | Hỗ trợ phân tích lỗi kỹ thuật, giải thích nguyên lý quản lý thời gian tìm kiếm, thiết kế cơ chế bù trừ độ trễ hệ thống GameController, rà soát logic bitboard phong cấp trong Quiescence Search và chuẩn hóa tài liệu báo cáo. |
| **Gemini / Google Antigravity** | Hỗ trợ phân tích thuật toán dọn tàn cuộc Mop-Up Heuristic (ép Vua đối phương vào góc khi áp đảo vật chất), tối ưu sắp xếp nước chiếu hiểm hóc và xây dựng bộ kiểm thử 12 thế cờ chiến thuật. |

#### 4.3. Nội dung AI hỗ trợ
| Nhóm công việc | Nội dung AI hỗ trợ | Cách thành viên sử dụng kết quả |
|---|---|---|
| **Phân tích lỗi kỹ thuật & Bitboard** | Hỗ trợ phân tích lỗi bitboard has_promotion kiểm tra nhầm tốt cả hai bên trong Quiescence Search làm tê liệt Delta Pruning; giải thích nguyên nhân lỗi AttributeError: 'Board' object has no attribute 'zobrist_hash' và thay bằng oard._transposition_key(). | Tự chạy chương trình, đọc mã nguồn, đối chiếu tài liệu python-chess, sửa đổi bitboard kiểm tra tốt theo lượt đi thực tế (oard.pawns & board.occupied_co[board.turn]) và kiểm chứng tính đúng đắn. |
| **Hiệu chuẩn quản lý thời gian** | Phân tích cơ chế cộng dồn độ trễ 500ms - 1000ms của GameController, hướng dẫn cân bằng ngân sách tìm kiếm theo từng giai đoạn và thiết lập sàn khẩn cấp 20ms cho Panic Mode. | Tự xây dựng công thức compute_budget_ms(), điều chỉnh hệ số mở tầng can_start_next_depth(), bảo lưu quỹ trễ và kiểm thử đối kháng chống rụng kim trong các ván đấu 200+ ply. |
| **Nâng cấp chiến thuật & Tàn cuộc** | Hướng dẫn thuật toán Mop-Up Heuristic bảo toàn tính đối xứng gương .mirror() và sắp xếp nước chiếu gives_check (+600k điểm). | Tự tích hợp vào student/evaluation.py và student/search.py, kiểm chứng qua bộ 12 FEN chiến thuật đạt 100% độ chính xác. |
| **Hỗ trợ tài liệu** | Gợi ý cách diễn đạt, cấu trúc hóa báo cáo và minh bạch hóa trách nhiệm. | Tự đối chiếu nội dung với mã nguồn, kiểm tra Git an toàn và hoàn thiện hồ sơ dự án. |
#### 4.4. Ví dụ tương tác AI tiêu biểu
- **Vấn đề kỹ thuật:** Tại sao bot cờ vua luôn thực hiện nước đi `g1h3` trong thời gian 0.000s mặc dù đã được viết đầy đủ?
- **Yêu cầu đặt ra cho AI:** *"Hãy phân tích nguyên nhân có thể dẫn đến lỗi `AttributeError` khi sử dụng phương thức `zobrist_hash()` trong thư viện `python-chess`. Giải thích cách kiểm tra và đề xuất hướng khắc phục. Không viết lại toàn bộ module tìm kiếm, chỉ tập trung giải thích nguyên nhân và hướng xử lý."*
- **Kết quả nhận được:** Traceback chỉ ra lỗi `AttributeError: 'Board' object has no attribute 'zobrist_hash'` tại dòng gọi `self.tt.probe()`. Khối `except Exception` trong `bot.py` đã bắt ngoại lệ này và trả về `legal[0]`.
- **Đánh giá và áp dụng:** Nhận diện đây là lỗi nghiêm trọng nhất của hệ thống, ngay lập tức nghiên cứu tài liệu thư viện `chess` và thay thế bằng `board._transposition_key()`, khôi phục thành công khả năng tìm kiếm sâu của bot.

#### 4.5. Phân định phạm vi đóng góp
- **Phần AI đóng góp:** 
    - Hỗ trợ giải thích và định hướng phân tích lỗi liên quan đến phương thức zobrist_hash().
    - Gợi ý một số nguyên tắc phân bổ ngân sách thời gian và kiểm soát quá trình tìm kiếm.
    - Đưa ra các trường hợp ngoại lệ cần được xem xét trong quá trình xây dựng bot.
    - Hỗ trợ rà soát cách trình bày tài liệu kỹ thuật và khai báo sử dụng AI.
- **Phần thành viên D tự thực hiện:**
  - Nghiên cứu và hoàn thiện toàn bộ tệp `student/time_manager.py`.
  - Xây dựng công thức compute_budget_ms() và các phương thức quản lý deadline.
  - Hiện thực lớp `StudentBot` trong `student/bot.py`, bao gồm cơ chế kiểm tra nước đi hợp lệ và fallback khi xảy ra ngoại lệ.
  - Xây dựng lớp `TranspositionTable` và các hàm chuẩn hóa điểm chiếu hết.
  - Tự kiểm thử, sửa lỗi, tích hợp mã nguồn của các thành viên và chịu trách nhiệm giải trình các nội dung kỹ thuật được phân công. 

#### 4.6. Phương pháp kiểm chứng đã thực hiện
- Kiểm thử quản lý thời gian: Thử nghiệm bot với các mức thời gian khác nhau, kiểm tra ngân sách tìm kiếm và khả năng dừng khi đạt deadline.
- Kiểm thử khả năng chịu lỗi: Kiểm tra các trường hợp thuật toán tìm kiếm gặp ngoại lệ, xác nhận bot có thể trả về nước đi hợp lệ dự phòng.
- Kiểm tra tính hợp lệ: Đối chiếu nước đi trả về với danh sách `board.legal_moves`.
- Kiểm tra tài nguyên: Kiểm tra dung lượng thư mục `student/` và đối chiếu với giới hạn của đề bài.

---

## PHẦN II. KHAI BÁO SỬ DỤNG AI CẤP NHÓM

### 2.1. Nguyên tắc sử dụng AI của nhóm
Toàn thể 4 thành viên Nhóm 12 thống nhất và tuân thủ nghiêm ngặt các nguyên tắc sau:
1. **AI là công cụ trợ lực, không thay thế tư duy học thuật:** Công cụ AI chỉ được sử dụng để hỗ trợ tra cứu tài liệu, giải thích lý thuyết, rà soát lỗi cú pháp và gợi ý hướng tối ưu. Toàn bộ quyết định kỹ thuật và mã nguồn đưa vào dự án đều do các thành viên tự đọc hiểu, đánh giá và kiểm chứng.
2. **Tuân thủ tuyệt đối quy định cấm của môn học:** Không sử dụng bất kỳ thư viện học máy (Machine Learning / Deep Learning), không sử dụng mô hình huấn luyện sẵn, không gọi API bên ngoài, không sử dụng sách khai cuộc hoặc cơ sở dữ liệu cờ tàn.
3. **Trách nhiệm giải trình cá nhân:** Mọi dòng mã nguồn trong thư mục `student/` đều có thành viên cụ thể chịu trách nhiệm giải thích chi tiết cơ chế hoạt động khi được giảng viên vấn đáp trực tiếp.

### 2.2. Bảng tổng hợp công cụ và phạm vi sử dụng toàn nhóm

| Thành viên | Trụ cột phân công | Công cụ AI xác nhận | Mục đích chính |
|---|---|---|---|
| **Vũ Hoàng Long** | Duyệt không gian trạng thái và cắt tỉa toán học | Gemini | Giải thích thuật toán tìm kiếm; gợi ý rà soát Negamax, Transposition Table, thao tác `push()` / `pop()` và tham số LMR. Thành viên tự hiện thực, thử nghiệm và quyết định áp dụng. |
| **Lê Văn Việt** | Biểu diễn tri thức chuyên gia và hàm lượng giá trạng thái trong `student/evaluation.py` | Gemini / ChatGPT | Hỗ trợ rà soát PeSTO PST, Tapered Evaluation, Game Phase, cấu trúc Tốt, hoạt động quân, an toàn Vua và Tempo Bonus; hỗ trợ chuẩn hóa tài liệu. Thành viên tự lựa chọn, kiểm tra mã nguồn và xác minh kết quả. |
| **Đỗ Thành Vương** | Tối ưu hóa thuật toán tìm kiếm: Move Ordering, SEE, Quiescence Search, Delta Pruning, NMP và LMR | OpenAI | Hỗ trợ phân tích và đề xuất mã nguồn cho các thuật toán SEE, Quiescence Search, Delta Pruning, NMP và LMR; hỗ trợ rà soát các điều kiện cắt tỉa và logic tìm kiếm trong `student/search.py` |
| **Nông Văn Bách** | Quản trị trạng thái, quản lý thời gian & tích hợp hệ thống | Google Antigravity (Gemini / Claude) | Hỗ trợ phân tích lỗi kỹ thuật zobrist_hash, giải thích nguyên lý quản lý ngân sách thời gian tìm kiếm, tham khảo hướng xử lý ngoại lệ và rà soát tài liệu. Thành viên tự nghiên cứu, lựa chọn giải pháp, lập trình, tích hợp mã nguồn và hoàn thiện hồ sơ dự án|

### 2.3. Cam kết học thuật của nhóm
Nhóm 12 cam kết toàn bộ nội dung khai báo trong tài liệu này là hoàn toàn trung thực. Toàn bộ mã nguồn bot cờ vua ChessLab nộp trong thư mục `student/` phản ánh đúng năng lực, sự nỗ lực nghiên cứu và hiểu biết học thuật của 4 thành viên trong nhóm.

---


## PHẦN III. KHAI BÁO BỔ SUNG TRONG GIAI ĐOẠN ĐÁNH GIÁ THỰC NGHIỆM VÀ TỐI ƯU HÓA CUỐI CÙNG

Trong giai đoạn kiểm thử đối kháng và chuẩn bị nộp bài chính thức, nhóm đã sử dụng trợ lý AI (Google Antigravity / Gemini) nhằm hỗ trợ các nội dung sau:
1. **Thiết lập công cụ benchmark thực nghiệm độc lập:** Hỗ trợ xây dựng kịch bản kiểm thử không giao diện (headless tournament) song song dựa trên mã nguồn khung của ban tổ chức (`chesslab_sdk`), mô phỏng đúng độ trễ ngẫu nhiên 500–1000ms của GameController để phát hiện nguy cơ quá giờ trong các tình huống thực tế.
2. **Phân tích nguyên nhân thất bại của bản gốc (Root Cause Analysis):** Hỗ trợ chỉ ra hiện tượng tiêu hao thời gian quá mức ở giai đoạn khai cuộc khi bàn cờ chưa có biến động lớn, cùng với sự xung đột giữa điều kiện kiểm tra phong cấp trong Quiescence Search và độ trễ hệ thống dẫn đến cạn kiệt đồng hồ ở tàn cuộc.
3. **Đề xuất tinh chỉnh Heuristic và Kiểm soát Thời gian:**
   - Điều chỉnh công thức phân bổ thời gian động (`compute_budget_ms`), bổ sung quỹ dự trữ độ trễ hệ thống (`moves_left * 550ms`) và cơ chế hạ cánh khẩn cấp (Panic Mode floor) khi đồng hồ còn dưới 3.5s.
   - Chuẩn hóa điều kiện bắt quân phong cấp trong Quiescence Search theo đúng màu quân đang đi (`board.turn`).
   - Tăng cường trọng số phạt an toàn Vua khi đứng trên cột mở và bán mở trong `evaluation.py`.
4. **Cam kết kiểm chứng:** Mọi tinh chỉnh mã nguồn trong `student/` đều được nhóm tự biên dịch, kiểm tra thông qua `pytest` và kiểm chứng đối đầu thực tế 2 lượt đổi màu trước khi chấp nhận vào bản chính thức.
