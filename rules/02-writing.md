# 02. Văn phong và số trang

## Số trang

GVHD (26/11/2026): 25–35 trang chỉ là khuyến khích; bài cần ngắn gọn, đơn giản, dễ hiểu.
Mục tiêu của nhóm: **khoảng 40 trang**, không tính phụ lục, mục lục, danh sách bảng và hình. Kiểm tra số trang chỉ cảnh báo, không chặn bản nộp.

Ngân sách dưới đây chia theo trọng số điểm. Cột Pages của GVHD chia theo nội dung: ba từ khóa 2-4, 2-3, 1-2;
ba mục tiêu 10-12, 8-10, 6-8; đánh giá 2-4; kết luận 1 (cộng 32 đến 44). Lệch nhau thì hỏi GVHD.

Bảng dưới là ngân sách gốc (tổng 35), chỉ để tham khảo tỉ lệ giữa các phần.

| Phần | Ngân sách (trang) | Trọng số hội đồng | Trọng số quá trình |
|---|---|---|---|
| I. Project Introduction | 3 | 5% | 10% |
| II. Project Management Plan | 3 | 5% | 10% |
| III. Existing Systems/State of the Art | 5 | 5% | 10% |
| IV. Methodology | 9 | 35% | 35% |
| V. System Design and Implementation | 6,5 | 20% | 20% |
| VI. Results and Discussion | 7 | 15% (cùng VII) | 15% (cùng VII) |
| VII. Conclusion | 1,5 | | |
| Tổng | 35 | | |

## Nội dung nằm ở phần nào

- **IV: thuật toán và lý do.** V: thành phần nằm ở đâu, dữ liệu chảy thế nào. **VI: benchmark** (thiết kế ở VI.1.1-VI.1.4, kết quả ở VI.1.5-VI.1.9).
- IV.4 và IV.5 giữ ngắn (cách kiểm chứng, công thức), chi tiết trỏ sang VI.1.
- Không tả một thứ hai lần; trỏ bằng `\cref`. Chỉ hai cấp tiêu đề (GVHD, 26/11/2026); tên mục cấp 1, 2 giữ theo trường. Mục cấp 2 có nhiều ý thì mở bằng một câu nêu các ý, và câu đầu mỗi đoạn nêu ý của đoạn.

## Văn phong

- Tiếng Anh học thuật, en-GB, câu ngắn, mỗi đoạn một ý. Viết ngôi thứ ba hoặc "the group"; tránh "I".
- Viết việc nhóm làm. Kiến thức của người khác thì trích dẫn, không kể lại.
- Thì quá khứ cho việc đã làm và kết quả; thì hiện tại cho mô tả hệ thống.
- Không quảng cáo: bỏ "revolutionary", "state-of-the-art" (trừ tên phần), "very", "significantly" khi không có kiểm định.
- Viết tắt: mở rộng ở lần đầu và có trong `frontmatter/acronyms.tex`.
- Một khái niệm một tên. Tên sản phẩm: OpenTrading, opentrading-mcp, opentrading-benchmark, OpenCode, DeepSeek Harness (DSH).
- Số: dấu chấm thập phân, dấu phẩy hàng nghìn, dùng `\num` và `\qty` của siunitx; phần trăm kèm mẫu số (385/400, 96.25%).
- Trích lời nguyên văn phải có ngoặc `\enquote{}` và số trang.
- Không chép văn bản từ README, AI hoặc nguồn khác vào bài. Người đứng tên phần chịu trách nhiệm hiểu và bảo vệ từng câu.

## File nguồn

- Mỗi câu một dòng, để diff dễ đọc.
- `\guide{...}` là hướng dẫn của template: xóa khi đã viết xong mục đó. `\todo{...}` cho việc còn mở. `\TBC{...}` cho dữ kiện chưa xác nhận.
- Bản `final` không build được nếu còn `\todo` hoặc `\TBC`; bản nộp còn yêu cầu hết `\guide`.
