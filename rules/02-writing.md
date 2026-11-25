# 02. Văn phong và số trang

## Số trang

Mục tiêu: **25 đến 35 trang** ("25-35 pages hoàn chỉnh", GVHD). Nhóm tạm hiểu là phần I đến VII; chưa hỏi lại GVHD,
nên kiểm tra số trang chỉ cảnh báo, không chặn bản nộp.

Ngân sách dưới đây chia theo trọng số điểm. Cột Pages của GVHD chia theo nội dung: ba từ khóa 2-4, 2-3, 1-2;
ba mục tiêu 10-12, 8-10, 6-8; đánh giá 2-4; kết luận 1 (cộng 32 đến 44). Lệch nhau thì hỏi GVHD.

| Phần | Ngân sách (trang) | Trọng số hội đồng | Trọng số quá trình |
|---|---|---|---|
| I. Project Introduction | 3 | 5% | 10% |
| II. Project Management Plan | 3 | 5% | 10% |
| III. Existing Systems/State of the Art | 5 | 5% | 10% |
| IV. Methodology | 9 | 35% | 35% |
| V. System Design and Implementation | 7 | 20% | 20% |
| VI. Results and Discussion | 5 | 15% (cùng VII) | 15% (cùng VII) |
| VII. Conclusion | 2 | | |
| Tổng | 34 | | |

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
