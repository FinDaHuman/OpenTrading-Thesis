# Slide thuyết trình

Yêu cầu cho slide bảo vệ AIP491 của nhóm G11. Slide làm trên Canva, không nằm trong repo; file này giữ yêu cầu
và cách đối chiếu slide với thesis.

| Mục | Giá trị |
|---|---|
| Bản làm việc | Canva: <https://canva.link/xarsjt6yd51or7b> |
| File nộp | `.pptx` xuất từ Canva (Share, Download, PowerPoint) |
| Thời lượng | 20 đến 25 phút |
| Thiết bị trình chiếu | Máy chiếu, không phải TV. Từ SPRING 2025 có phòng dùng TV, tùy phòng và tùy kỳ, nên thiết kế cho trường hợp xấu nhất là máy chiếu |
| Tỉ lệ | 16:9 (1920 × 1080 trên Canva) |

## Hình thức

Máy chiếu làm nhạt màu và giảm tương phản, nhất là trong phòng sáng.

- Nền trơn, sáng, một màu. Không ảnh nền, không gradient, không hoa văn.
- Chữ tối trên nền sáng. Không dùng chữ xám nhạt cho nội dung cần đọc.
- Font sans-serif đơn giản, một họ font cho cả bộ. Ưu tiên font có sẵn trong PowerPoint (Arial, Calibri) để
  file `.pptx` không bị thay font khi mở trên máy phòng bảo vệ.
- Cỡ chữ trên khung 1920 × 1080 của Canva (1 px ≈ 0,5 pt sau khi xuất):
  tiêu đề từ 64 px, nội dung từ 36 px (18 pt), chú thích, nguồn và chân trang từ 28 px (14 pt).
- Màu nhấn tối đa hai màu, đủ đậm để còn phân biệt khi máy chiếu nhạt màu. Không phân biệt ý chỉ bằng màu.
- Biểu đồ và sơ đồ: nét dày, nhãn ghi trực tiếp, ít chữ.
- Không hiệu ứng chuyển trang hay animation phức tạp.

## Nội dung

- Theo thứ tự các phần của thesis (I đến VII, VIII References) và cùng tên phần.
- Mọi con số trên slide phải khớp thesis bản nộp gần nhất và có trong `rules/05-evidence.md`.
- Chỉ dùng kết quả benchmark cuối cùng sau khi chấm, một bộ 300 task; không đưa số của bản nháp hay lần chạy trước.
- Link "Source" trỏ tới tag phát hành của thesis đang nộp (ví dụ `v0.3.0`), không trỏ tới commit cũ.
- Tham chiếu số bảng, số mục (Table 15, § IV.4) phải đúng với PDF đang nộp.
- Ghi chú người thuyết trình (presenter notes) cũng phải khớp thesis, vì hội đồng có thể đọc file `.pptx`.
- Nêu giới hạn đúng như thesis (Part VI, Discussion), không làm mạnh kết luận hơn bài viết.

## Phân bổ thời gian gợi ý (khoảng 24 phút)

| Phần | Slide | Phút |
|---|---|---|
| Mở đầu, I Introduction | 1 đến 2 | 2 |
| II Management | 3 | 1,5 |
| III Existing Systems | 4 | 1,5 |
| IV Methodology | 5 đến 8, 12 | 6 |
| V System Design | 9 đến 11 | 3,5 |
| VI Results and Discussion | 13 đến 16 | 5 |
| VII Conclusion, VIII References | 17 đến 18 | 1,5 |
| Demo trực tiếp (hoặc video dự phòng) | 19 | 3 |

## Trước khi nộp

1. Đối chiếu từng số trên slide và trong presenter notes với thesis bản nộp.
2. Cập nhật link Source về tag thesis đang nộp.
3. Xuất `.pptx`, mở bằng PowerPoint: kiểm tra font, xuống dòng, biểu đồ, link.
4. Chiếu thử trên máy chiếu hoặc xem ở độ sáng thấp; đứng cách màn hình 3 đến 4 m vẫn đọc được chân trang.
5. Tập trình bày, bấm giờ trong khoảng 20 đến 25 phút.

## Trạng thái bản Canva

Ngày 27/11/2026, bản Canva (19 slide) đã khớp thesis `v0.3.0`: số liệu, link Source, presenter notes, Table 15,
slide 12 ghi Haiku 5.5 chấm cả 900 trial.

Còn phải làm:

- [x] Chân trang, nhãn phần, số trang và chú thích xám lên 28 px, màu `#4b5665`; nhãn trục slide 13 lên 26 px,
  nhãn "$0", "0 s" slide 15 lên 24 px (27/11/2026).
- [x] Font: cả 19 slide dùng Arial (kiểm tra trong trình chỉnh sửa Canva ngày 27/11/2026).
- [x] Slide 19 "Live demo" ở cuối bộ: hỏi về FPT, lưu một quy tắc rồi mở phiên mới, hỏi dữ liệu không tồn tại.
- [ ] Quay video dự phòng cho ba bước demo (slide 19 ghi "Backup: a recorded video").
- [ ] Đổi "Review 1.1" ở tiêu đề và chân trang khi dùng cho buổi bảo vệ cuối.
- [ ] Xuất `.pptx` và làm checklist "Trước khi nộp".
