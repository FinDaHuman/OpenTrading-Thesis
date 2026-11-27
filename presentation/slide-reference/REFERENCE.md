# Slide tham khảo

Các bộ slide và bài hướng dẫn trình bày nghiên cứu, chọn theo điều kiện gần với buổi bảo vệ của nhóm:
đề tài AI và agent, nói khoảng 15 đến 25 phút, chiếu trong phòng trước hội đồng.
File PDF tải ngày 27/11/2026, chỉ để tham khảo nội bộ. Bản quyền thuộc tác giả, không đưa lên GitHub
(đã thêm vào `.gitignore`).

## Danh sách

| File | Loại | Nguồn | Dùng để học gì |
|---|---|---|---|
| `01_sands-after-peyton-jones_good-research-talk.pdf` | Slide bài giảng, 80 trang, 4:3 | [Chalmers DAT147](https://www.cse.chalmers.se/edu/year/2015/course/DAT147/mtrl/L06%20DAT147%20Giving%20a%20talk.pdf), dựa trên [Peyton Jones, MSR](https://www.microsoft.com/en-us/research/academic-program/give-great-research-talk/) | Cấu trúc bài nói: động cơ 20%, ý chính 80%, ví dụ là vũ khí chính |
| `02_naegle-2021_ten-rules-presentation-slides.pdf` | Bài báo PLOS Comput Biol 17(12): e1009554 | [doi.org/10.1371/journal.pcbi.1009554](https://doi.org/10.1371/journal.pcbi.1009554) | 10 luật thiết kế từng slide: một ý, một phút, tiêu đề là câu kết luận, tương phản |
| `03_bourne-2007_ten-rules-oral-presentations.pdf` | Bài báo PLOS Comput Biol 3(4): e77 | [doi.org/10.1371/journal.pcbi.0030077](https://doi.org/10.1371/journal.pcbi.0030077) | 10 luật cho bài nói: ít là nhiều, thông điệp mang về, tập và bấm giờ |
| `04_webis-2025_bachelor-defense-llm.pdf` | Slide bảo vệ cử nhân về LLM, Bauhaus-Universität Weimar, 28 trang, 16:9 | [webis.de](https://downloads.webis.de/theses/slides/al-jasim_2025.pdf) | Cùng cấp độ với nhóm: thưa chữ, ảnh chụp sản phẩm lớn |
| `05_course_swe-agent.pdf` | Slide môn học về SWE-agent, 65 trang | [surrealyz.github.io](https://surrealyz.github.io/classes/llmsec-fall24/slides/05-SWE-agent.pdf) | Cùng chủ đề agent; **ví dụ cần tránh** vì dán nguyên bảng và hình từ bài báo |
| `06_neurips-2024_tool-augmented-llm-talk.pdf` | Slide trình bày NeurIPS 2024, 15 trang | [neurips.cc](https://neurips.cc/media/neurips-2024/Slides/94647_d04vZ2l.pdf) | Cùng chủ đề tool use; **ví dụ cần tránh** vì chữ nhỏ, nhiều màu nhấn |
| `07_iclr-2025_toolgen-talk.pdf` | Slide trình bày ICLR 2025, 21 trang, 16:9 | [iclr.cc](https://iclr.cc/media/iclr-2025/Slides/29311.pdf) | Nền trắng, một màu nhấn, sơ đồ khối đơn giản, font Aptos |

## Nhận xét từ các bộ slide

| Bộ | Làm tốt | Không nên học |
|---|---|---|
| 04 Webis | Nền trắng trơn, tiêu đề lớn, mỗi slide một ý, ảnh chụp giao diện chiếm nửa slide, slide cuối là Conclusion với Summary và Future work | Font serif (Times) cho nội dung; vài slide toàn chữ monospace nhỏ |
| 07 ToolGen | Nền trắng, chỉ một màu nhấn xanh đậm, sơ đồ khối và mũi tên gọn, tiêu đề cùng vị trí trên mọi slide | Chữ thân và nhãn sơ đồ quá nhỏ cho máy chiếu |
| 06 NeurIPS | Có trình tự Background, Motivation, Method, Experiments rõ | Chữ đỏ, xanh, gạch chân lẫn lộn; nhiều đoạn chữ dày; ảnh chụp bảng của bài báo |
| 05 SWE-agent | Tiêu đề rõ | Dán nguyên trang bài báo, bảng số liệu cỡ chữ 8, không đọc được từ cuối phòng |

## Quy tắc rút ra cho slide G11

### Bố cục
- Mỗi slide **một ý**; tiêu đề là **câu kết luận** của slide (Naegle, luật 3), ví dụ
  "OpenTrading answered 279 of 300 tasks" thay cho "Results".
- Khoảng **1 phút mỗi slide** (Naegle, luật 2): 20 đến 25 phút thì 18 đến 24 slide.
- Tiêu đề, nhãn phần (I đến VII) và chân trang ở **cùng vị trí** trên mọi slide.
- Lề rộng; nội dung chính nằm trong vùng giữa, không sát mép vì máy chiếu có thể cắt viền.
- Một người không tập trung vẫn phải nắm được ý chính trong 3 giây (Naegle, luật 8).

### Màu sắc
- **Nền trắng hoặc trắng ngà trơn**; chữ gần đen (#1A1A1A đến #222).
- **Một màu nhấn chính**, đậm (xanh đậm kiểu #1F4E9A), thêm tối đa một màu phụ để so sánh
  (xám đậm cho baseline). Không dùng đỏ và xanh lá làm cặp đối lập (mù màu).
- Không dùng xám nhạt cho chữ cần đọc; máy chiếu làm nhạt thêm. Xám tối thiểu khoảng #555.
- Không gradient, không ảnh nền, không bóng đổ.

### Phông chữ
- **Sans-serif**, một họ font cho cả bộ (Naegle, luật 7). Vì nộp `.pptx`, chọn font có sẵn trong Office:
  **Arial** hoặc **Calibri** (Aptos nếu máy phòng có Office 365).
- Đậm để nhấn mạnh; không gạch chân, không in nghiêng, không viết HOA cả câu.
- Cỡ chữ trên khung Canva 1920 × 1080 (≈ 0,5 pt/px khi xuất): tiêu đề ≥ 64 px, thân ≥ 36 px,
  nhãn biểu đồ, chú thích, chân trang ≥ 28 px.

### Hình ảnh, biểu đồ, sơ đồ
- Ảnh chụp sản phẩm thật (terminal OpenTrading) lớn, cắt đúng vùng cần nói, không thu nhỏ cả màn hình.
- Biểu đồ vẽ lại cho slide, không dán hình từ thesis: ít trục, nhãn ghi thẳng trên cột,
  màu nhấn cho OpenTrading, xám cho baseline.
- Bảng tối đa khoảng 5 hàng × 4 cột; tô một hàng cần nhìn (như hàng Memory).
- Sơ đồ khối và mũi tên như bộ 07, tối đa khoảng 6 khối.
- Icon đơn sắc, nét đồng nhất; không clipart, không ảnh minh họa trang trí.
- Không animation trừ khi cần lộ dần từng bước của sơ đồ.

### Nội dung và lời nói
- Mở đầu 2 phút trả lời "vấn đề là gì, vì sao đáng quan tâm" (Peyton Jones).
- Ví dụ cụ thể (câu hỏi về FPT, ví dụ P/E 12.34) có sức thuyết phục hơn định nghĩa.
- Kết bằng thông điệp mang về và giới hạn trung thực (Bourne, luật 4).
- Ghi chú người nói giữ số liệu và nguồn; slide chỉ giữ điều khán giả cần nhìn.
- Chuẩn bị cho sự cố (Naegle, luật 10): mang PDF dự phòng, video demo quay sẵn, không phụ thuộc mạng.
