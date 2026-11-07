# BÁO CÁO KHAI BÁO SỬ DỤNG CÔNG CỤ TRÍ TUỆ NHÂN TẠO (AI_USAGE.MD)
## DỰ ÁN: BOT CỜ VUA CHESSLAB (CHESS960) — MÔN HỌC: BIỂU DIỄN TRI THỨC VÀ TÌM KIẾM NÂNG CAO
### NHÓM THỰC HIỆN: NHÓM 12

---

## LỜI MỞ ĐẦU

Tài liệu này được lập nhằm mục đích minh bạch hóa việc sử dụng các công cụ Trí tuệ Nhân tạo (AI) trong quá trình học tập, nghiên cứu và phát triển sản phẩm bot cờ vua ChessLab, tuân thủ nghiêm ngặt các quy định tại:
- **Quy chế Bài tập lớn trong `README.md`**: Cho phép sử dụng công cụ AI hỗ trợ tra cứu cú pháp và tài liệu nhưng nghiêm cấm tuyệt đối việc sử dụng Machine Learning / Deep Learning, mô hình đã huấn luyện sẵn, sách khai cuộc (opening book), cơ sở dữ liệu tàn cuộc (endgame tablebases) hoặc gọi engine cờ vua bên ngoài (như Stockfish). Toàn bộ mã nguồn phải được xây dựng dựa trên thuật toán tìm kiếm đối kháng và hàm đánh giá heuristic truyền thống; sinh viên phải tự hiểu, tự viết, giải thích và bảo vệ được từng dòng mã nguồn trước giảng viên.

> **Nguyên tắc phân định mức độ hỗ trợ:** 
> Trong toàn bộ dự án, các công cụ AI chỉ đóng vai trò trợ lý tra cứu phụ trợ mức độ thấp (**chiếm khoảng 10% – 15% khối lượng công việc**, chủ yếu hỗ trợ tra cứu cú pháp thư viện `python-chess`, giải thích các mã lỗi traceback và hỗ trợ định dạng bảng biểu). **Khoảng 85% – 90% khối lượng công việc cốt lõi** (thiết kế kiến trúc hệ thống, chứng minh và cài đặt thuật toán Negamax/PVS, xây dựng bảng lượng giá bitboard, quản lý đồng hồ thi đấu và giải quyết các bài toán biên Chess960) đều do 4 thành viên Nhóm 12 trực tiếp tự nghiên cứu tài liệu môn học, tự lập trình và kiểm nghiệm thực tế.

---

## PHẦN I. KHAI BÁO SỬ DỤNG AI THEO TỪNG THÀNH VIÊN

---

### 1. THÀNH VIÊN 1: VŨ HOÀNG LONG
- **Mã sinh viên:** 25022922
- **Tài khoản Git ghi nhận:** `long8807`

#### 1.1. Vai trò và nhiệm vụ phân công
- Phụ trách trụ cột *Duyệt không gian trạng thái trò chơi đối kháng & Cắt tỉa toán học*.
- Chịu trách nhiệm chính về khối lõi thuật toán trong `student/search.py`: Negamax, Alpha-Beta Pruning, Đào sâu lặp (Iterative Deepening Search - IDS), Cửa sổ kỳ vọng (Aspiration Windows), Principal Variation Search (PVS), chuẩn hóa điểm chiếu hết theo độ sâu (`score_to_tt`, `score_from_tt`), và đảm bảo an toàn trạng thái bàn cờ qua `board.push()` / `board.pop()`.

#### 1.2. Công cụ AI sử dụng
| Công cụ AI | Công đoạn sử dụng | Mục đích sử dụng |
|---|---|---|
| **Google Gemini** | Tra cứu cú pháp & Tài liệu tham khảo | Tra cứu nhanh tài liệu lý thuyết Minimax/Negamax từ giáo trình; hỏi nhanh cú pháp các hàm sao chép trạng thái của thư viện `python-chess`. |

#### 1.3. Nội dung AI hỗ trợ và cách thành viên xử lý
| Nội dung AI hỗ trợ | Hình thức hỗ trợ | Cách thành viên tiếp nhận và kiểm chứng |
|---|---|---|
| **Cú pháp thư viện python-chess** | Tra cứu cách sử dụng `board.push()` và `board.pop()` an toàn trong khối `try...finally`. | Tự tay viết mã nguồn hàm `_negamax`, tự xây dựng cấu trúc đệ quy đối xứng toán học zero-sum và kiểm tra stack bàn cờ. |
| **Công thức chuẩn hóa điểm chiếu hết** | Nhắc lại quy tắc cộng/trừ ply kinh điển trong Chess Programming Wiki khi lưu vào Transposition Table. | Tự thiết kế và tự cài đặt 2 hàm `score_to_tt` và `score_from_tt`, kiểm chứng thực nghiệm qua các bài test Mate-in-1 và Mate-in-2. |
| **Rà soát điều kiện dừng IDS** | Gợi ý kiểm tra biến cờ `_timeout` khi vòng lặp đào sâu bị ngắt. | Tự phân tích logic, bổ sung điều kiện `if candidate is not None and (not self._timeout or depth == 1)` để bảo toàn nước đi tốt nhất của tầng đã hoàn chỉnh. |

#### 1.4. Phân định mức độ đóng góp (Ước lượng theo phạm vi công việc)
- **AI hỗ trợ tra cứu phụ trợ:** **~15%** (tra cứu cú pháp hàm và tài liệu tham khảo).
- **Thành viên tự nghiên cứu, lập trình và bảo vệ:** **~85%** (tự thiết kế cây tìm kiếm, tự code toán học Negamax/PVS, kiểm thử tính tất định và chịu trách nhiệm bảo vệ).

#### 1.5. Phương pháp kiểm chứng đã thực hiện
- Chạy kiểm thử đơn vị với các thế cờ chiếu hết bắt buộc để xác nhận bot luôn tìm ra chuỗi nước đi ngắn nhất.
- Kiểm tra tính an toàn của stack bàn cờ: xác nhận số lần `push()` luôn bằng số lần `pop()`.
- Chạy kiểm thử tính ổn định 10 lần liên tiếp trên cùng thế cờ FEN, xác nhận kết quả trả về là 100% tất định (deterministic).

---

### 2. THÀNH VIÊN 2: LÊ VĂN VIỆT
- **Mã sinh viên:** 25023069
- **Tài khoản Git ghi nhận:** `thocuong354-cloud`

#### 2.1. Vai trò và nhiệm vụ phân công
- Phụ trách trụ cột *Biểu diễn tri thức chuyên gia & Hàm lượng giá trạng thái (Heuristic Evaluation)*.
- Xây dựng toàn bộ module `student/evaluation.py`: hệ thống Piece-Square Tables theo PeSTO, cơ chế nội suy Tapered Evaluation theo giai đoạn trận đấu (Game Phase 0..24), đánh giá cấu trúc Tốt (tốt thông, tốt chồng, tốt cô lập), hoạt động quân (cặp Tượng, Xe cột mở/hàng 7, Mã tiền đồn) và thuật toán dồn Vua tàn cuộc Mop-Up Heuristic.

#### 2.2. Công cụ AI sử dụng
| Công cụ AI | Công đoạn sử dụng | Mục đích sử dụng |
|---|---|---|
| **ChatGPT (OpenAI)** | Thu thập dữ liệu bảng mẫu | Lấy dữ liệu mảng số nguyên chuẩn của bảng PeSTO công khai từ diễn đàn cờ vua quốc tế; kiểm tra định dạng mảng Python. |

#### 2.3. Nội dung AI hỗ trợ và cách thành viên xử lý
| Nội dung AI hỗ trợ | Hình thức hỗ trợ | Cách thành viên tiếp nhận và kiểm chứng |
|---|---|---|
| **Bảng số liệu PeSTO thô** | Trích xuất mảng 64 số nguyên tương ứng các ô cờ từ tài liệu mở. | Tự viết hàm `_orient_table` chuyển đổi tọa độ sang chỉ số ô chuẩn python-chess (0..63) và tự tối ưu hóa thành các tuple hằng số đóng gói. |
| **Gợi ý kỹ thuật bit-packing** | Gợi ý ý tưởng toán học gộp 2 giá trị trung cuộc (mg) và tàn cuộc (eg) vào một số nguyên 32-bit: `val = mg + (eg << 16)`. | Tự viết công thức giải nén có làm tròn có dấu: `eg = (val + 0x8000) >> 16`, tự viết script kiểm thử 1.000 số ngẫu nhiên sửa dứt điểm lỗi tràn số nguyên âm trong Python. |
| **Khoảng cách Chebyshev tàn cuộc** | Nhắc lại công thức khoảng cách tâm và khoảng cách Vua trong cờ tàn. | Tự tay tích hợp hàm `Mop-Up` với điều kiện kích hoạt an toàn (`phase <= 6` và `|score| >= 200`), đảm bảo 0% overhead ở trung cuộc và đạt đối xứng gương 100%. |

#### 2.4. Phân định mức độ đóng góp (Ước lượng theo phạm vi công việc)
- **AI hỗ trợ tra cứu phụ trợ:** **~10%** (thu thập bảng số liệu PeSTO công khai và gợi ý ý tưởng toán học).
- **Thành viên tự nghiên cứu, lập trình và bảo vệ:** **~90%** (tự xây dựng toàn bộ logic bitboard, kiểm thử đối xứng gương trên 960 thế Chess960, đo đạc NPS đạt ~89,000 evals/s).

#### 2.5. Phương pháp kiểm chứng đã thực hiện
- Kiểm thử tính đối xứng gương tuyệt đối: `evaluate(b) == evaluate(b.mirror())` trên 960 thế cờ Chess960 và hơn 1.000 thế cờ ngẫu nhiên, đạt độ chính xác 100%.
- Kiểm tra tốc độ thực thi hàm đánh giá: đạt ~89,000 evaluations/giây trên môi trường Python 3.12 đơn luồng.
- Xác nhận điểm số ở trạng thái xuất phát cân bằng luôn đạt đúng điểm Tempo Bonus (+9 centipawns cho bên Trắng).

---

### 3. THÀNH VIÊN 3: ĐỖ THÀNH VƯƠNG
- **Mã sinh viên:** 25023079
- **Tài khoản Git ghi nhận:** `dovuong28122007-spec`

#### 3.1. Vai trò và nhiệm vụ phân công
- Phụ trách trụ cột *Sắp xếp nước đi tối ưu (Move Ordering) & Triệt tiêu hiệu ứng chân trời*.
- Hiện thực các kỹ thuật nâng cao hiệu năng trong `student/search.py`: hàm sắp xếp nước đi `_order_moves`, thuật toán đánh giá đổi quân tĩnh 1-ply `see()`, Tìm kiếm tĩnh lặng `_quiescence()`, Delta Pruning, Null Move Pruning (NMP), Reverse Futility Pruning (RFP) và Late Move Reductions (LMR).

#### 3.2. Công cụ AI sử dụng
| Công cụ AI | Công đoạn sử dụng | Mục đích sử dụng |
|---|---|---|
| **ChatGPT (OpenAI)** | Tra cứu thuật ngữ | Tra cứu định nghĩa giải thuật SEE (Static Exchange Evaluation) và kỹ thuật MVV-LVA (Most Valuable Victim - Least Valuable Attacker) trong tài liệu Chess Programming. |

#### 3.3. Nội dung AI hỗ trợ và cách thành viên xử lý
| Nội dung AI hỗ trợ | Hình thức hỗ trợ | Cách thành viên tiếp nhận và kiểm chứng |
|---|---|---|
| **Lý thuyết SEE 1-ply** | Tóm tắt nguyên lý so sánh giá trị quân tấn công và quân phòng thủ trên ô đích. | Tự thiết kế thuật toán `see()` tinh gọn 1-ply, bổ sung trường hợp đặc biệt cho đổi quân nhẹ ($B \times N = 0\text{ cp}$), giúp Quiescence Search không bỏ sót đòn chiến thuật. |
| **Kỹ thuật Delta Pruning** | Nhắc lại ngưỡng cắt tỉa tĩnh: nếu điểm tĩnh cộng giá trị Hậu vẫn nhỏ hơn alpha thì cắt tỉa. | Tự lập trình hàm `_quiescence()`, tự bổ sung kiểm tra bitboard Tốt ở hàng áp chót để vô hiệu hóa Delta Pruning khi có nguy cơ phong cấp. |
| **Thứ tự Move Ordering** | Liệt kê các tầng sắp xếp phổ biến trong cờ vua máy tính. | Tự lập trình hàm `_order_moves()` với 7 tầng ưu tiên (TT Move > Phong Hậu > Good SEE > Killers > History > Bad SEE > Quiet), đo đạc đạt tỷ lệ cắt tỉa beta > 85% ngay tại nước đầu tiên. |

#### 3.4. Phân định mức độ đóng góp (Ước lượng theo phạm vi công việc)
- **AI hỗ trợ tra cứu phụ trợ:** **~15%** (tra cứu lý thuyết thuật toán cắt tỉa).
- **Thành viên tự nghiên cứu, lập trình và bảo vệ:** **~85%** (tự viết code hàm, tinh chỉnh trọng số Move Ordering, kiểm tra các trường hợp ngoại lệ).

#### 3.5. Phương pháp kiểm chứng đã thực hiện
- Kiểm thử Quiescence Search qua các thế cờ có chuỗi đổi quân phức tạp, xác nhận không bị hiện tượng mù chân trời.
- Kiểm thử các thế cờ chiến thuật (bắt Hậu treo, đòn fork/pin), xác nhận Move Ordering đưa nước đi chiến thuật lên vị trí duyệt đầu tiên.
- Chạy kiểm thử hồi quy hệ thống `pytest`, xác nhận 100% test cases đều vượt qua.

---

### 4. THÀNH VIÊN 4: NÔNG VĂN BÁCH
- **Mã sinh viên:** 25022782
- **Tài khoản Git ghi nhận:** `nvb-07-wbai`

#### 4.1. Vai trò và nhiệm vụ phân công
- Phụ trách trụ cột *Quản trị trạng thái (TT), Quản lý đồng hồ thi đấu & Kiến trúc phòng thủ hệ thống*.
- Hiện thực toàn bộ `student/time_manager.py`, điểm vào bắt buộc `student/bot.py`, cấu trúc bảng chuyển vị `TranspositionTable` trong `student/search.py`, điều phối tích hợp hệ thống, quản lý quy trình QA/Git, hoàn thiện `team.json`, `AI_USAGE.md` và gắn thẻ nộp bài `submission-final`.

#### 4.2. Công cụ AI sử dụng
| Công cụ AI | Công đoạn sử dụng | Mục đích sử dụng |
|---|---|---|
| **Google Gemini** | Tra cứu lỗi Traceback & Định dạng văn bản | Hỗ trợ phân tích nhanh nguyên nhân lỗi `AttributeError` khi gọi sai tên hàm băm của thư viện `python-chess`; hỗ trợ định dạng bảng biểu Markdown trong báo cáo. |

#### 4.3. Nội dung AI hỗ trợ và cách thành viên xử lý
| Nội dung AI hỗ trợ | Hình thức hỗ trợ | Cách thành viên tiếp nhận và kiểm chứng |
|---|---|---|
| **Phân tích lỗi hàm băm Zobrist** | Giải thích rằng `python-chess` đã tích hợp sẵn phương thức băm `board._transposition_key()`. | Tự đọc tài liệu chính thức của `python-chess`, cấu hình lại lớp `TranspositionTable` với kích thước $2^{19}$ mục, bổ sung `last_iteration_ms` vào `__slots__` để tối ưu bộ nhớ. |
| **Phân tích độ trễ GameController** | Thảo luận công thức tính thời gian của hệ thống: $\text{elapsed} = \max(\text{search\_ms}, \text{delay\_ms})$. | Tự tay xây dựng mô hình quản lý thời gian đa tầng trong `compute_budget_ms()`: phân bổ $150\text{ms}$ ở trung cuộc để độ trễ $500\text{ms}$ hấp thụ hoàn toàn, và sàn $35\text{ms}$ ở tàn cuộc để hoàn tất Depth 3-4. |
| **Xây dựng kịch bản kiểm thử** | Gợi ý các tiêu chí phân loại nước đi (Excellent, Good, Inaccuracy, Mistake, Blunder). | Trực tiếp lập trình script kiểm định không giao diện, tổ chức thi đấu đối kháng thực tế 16 ván, phân tích biên bản PGN và đo đạc tỷ lệ 0 blunder. |

#### 4.4. Phân định mức độ đóng góp (Ước lượng theo phạm vi công việc)
- **AI hỗ trợ tra cứu phụ trợ:** **~15%** (hỗ trợ phân tích mã lỗi traceback và hỗ trợ định dạng văn bản).
- **Thành viên tự nghiên cứu, lập trình và bảo vệ:** **~85%** (tự lập trình `time_manager.py`, `bot.py`, thiết kế Transposition Table, điều phối kiểm thử toàn diện và bảo vệ dự án).

#### 4.5. Phương pháp kiểm chứng đã thực hiện
- Kiểm thử khả năng chịu lỗi (Fault Tolerance): Khối try...except trong `choose_move()` luôn trả về nước đi hợp lệ dự phòng ngay cả khi thuật toán bị gián đoạn.
- Kiểm thử đồng hồ thi đấu trên nhiều mức thời gian: Blitz 45s, Standard 180s, kiểm tra cơ chế dừng `should_stop()` và dự đoán `can_start_next_depth()`.
- Kiểm tra tài nguyên hệ thống: Xác nhận tổng dung lượng thư mục `student/` đạt ~154 KiB (thỏa mãn tiêu chuẩn nghiêm ngặt $< 1\text{ MiB}$).

---

## PHẦN II. KHAI BÁO SỬ DỤNG AI CẤP NHÓM

### 2.1. Nguyên tắc sử dụng AI của Nhóm 12
1. **AI là công cụ tra cứu phụ trợ, sinh viên làm chủ 100% mã nguồn:** Công cụ AI chỉ được dùng như một cuốn từ điển tra cứu nhanh cú pháp hoặc giải thích thông báo lỗi. Mọi logic thuật toán, mô hình hóa toán học và mã nguồn trong `student/` đều do sinh viên tự nghiên cứu, tự gõ từng dòng lệnh và chịu trách nhiệm giải trình.
2. **Tuân thủ tuyệt đối quy chế môn học:** Không sử dụng Machine Learning, không sử dụng mô hình học sâu, không dùng thư viện ngoài bị cấm, không dùng sách khai cuộc hoặc dữ liệu cờ tàn.
3. **Trách nhiệm bảo vệ học thuật:** Từng thành viên hiểu rõ vai trò của từng hàm, từng biến và sẵn sàng trả lời trực tiếp mọi câu hỏi chất vấn của giảng viên trong buổi vấn đáp.

### 2.2. Bảng tổng hợp mức độ đóng góp toàn dự án
| Thành viên | Trụ cột đảm nhiệm | Tỷ lệ AI hỗ trợ phụ trợ | Tỷ lệ Sinh viên tự làm & Bảo vệ |
|---|---|:---:|:---:|
| **Vũ Hoàng Long** | Duyệt cây trò chơi (Search Engine) trong `student/search.py` | **15%** | **85%** |
| **Lê Văn Việt** | Hàm lượng giá trạng thái (Evaluation) trong `student/evaluation.py` | **10%** | **90%** |
| **Đỗ Thành Vương** | Sắp xếp nước đi & Quiescence Search trong `student/search.py` | **15%** | **85%** |
| **Nông Văn Bách** | Quản lý thời gian, Bảng băm & Điểm vào `student/bot.py` | **15%** | **85%** |
| **TRUNG BÌNH TOÀN NHÓM** | **DỰ ÁN BOT CỜ VUA CHESSLAB NHÓM 12** | **~13.75% (Dưới 15%)** | **~86.25% (Chủ đạo)** |

---

## PHẦN III. KHAI BÁO VỀ CÁC VẤN ĐỀ TỐI ƯU HÓA CUỐI CÙNG

Trong đợt rà soát và kiểm định độc lập cuối cùng trước khi đóng gói nộp bài, nhóm đã tự giải quyết 4 bài toán kỹ thuật thực tế:

1. **Khắc phục lỗi tràn số nguyên âm trong đóng gói PST:**
   - *Vấn đề:* Phép toán bitmask `& 0xFFFF` trên số âm trong Python làm biến đổi số âm thành số dương lớn, gây sai lệch điểm số cờ tàn.
   - *Sinh viên tự giải quyết:* Chuyển sang đóng gói tuyến tính `mg + (eg << 16)` và giải nén có làm tròn có dấu `eg = (val + 0x8000) >> 16`, sửa triệt để lỗi phong cấp.
2. **Khắc phục lỗi ngắt vòng lặp tìm kiếm sâu:**
   - *Sinh viên tự giải quyết:* Bổ sung điều kiện kiểm tra `not self._timeout or depth == 1` trước khi cập nhật `best_move` để tránh lưu kết quả của tầng bị gián đoạn.
3. **Phân tầng thời gian sinh tồn trong `time_manager.py`:**
   - *Sinh viên tự giải quyết:* Thiết lập phân tầng $25\text{--}40\text{ms}$ cho các nước sau 55 và phân tầng khẩn cấp cực hạn $8\text{--}15\text{ms}$ khi còn dưới 1.5s để loại trừ 100% rủi ro rụng cờ.
4. **Kiểm định chất lượng qua giải đấu đối kháng thực nghiệm:**
   - Nhóm đã tự lập trình runner kiểm thử headless và chạy đối đầu 16 ván thực tế giữa các phiên bản (đạt 12 thắng, 1 hòa, 3 thua, 0 blunder), chứng minh bot có năng lực suy luận đối kháng chiều sâu trước khi bước vào giải đấu chính thức.

### Cam kết học thuật
Toàn bộ 4 thành viên Nhóm 12 khẳng định nội dung khai báo trên là hoàn toàn trung thực, phản ánh chính xác thực tế quá trình nghiên cứu và làm việc của nhóm, cam kết chịu mọi trách nhiệm trước hội đồng chấm thi môn học.
