# 04. Hình, bảng, thuật toán, code, công thức

Chép mẫu từ `tests/sample/sample.tex`.

- Mỗi hình, bảng, thuật toán, listing có `\caption`, `\label` ngay sau caption, và được nhắc trong bài bằng `\cref` **trước** khi xuất hiện.
- Nhãn: `fig:`, `tab:`, `alg:`, `lst:`, `eq:`, `sec:`, `ch:`, chữ thường nối bằng gạch ngang.
- Caption là một câu ngắn, tự hiểu được. Bảng: caption trên. Hình: caption dưới.
- Vị trí `[H]`, đặt ngay sau đoạn văn nhắc tới nó, có dòng trống trước và sau, để hình không cắt ngang đoạn văn.
  Khi ráp bài mà `[H]` để trống nhiều ở cuối trang thì đưa đoạn kế tiếp lên trước hình, hoặc dùng `[htb]`.
- Hình vẽ: vector (PDF) từ nguồn trong `figures/src`. Ảnh chụp màn hình: PNG, tối thiểu 150 dpi ở cỡ in, chỉ lấy vùng cần xem, không lộ khóa, token, email, đường dẫn cá nhân.
- Chữ trong hình tối thiểu 8 pt sau khi co, Arial hoặc Times New Roman. Phân biệt được khi in đen trắng.
- Biểu đồ số liệu: có script tạo lại từ dữ liệu đã commit, trục có tên và đơn vị, trục cột bắt đầu từ 0, có khoảng tin cậy khi so sánh.
- Bảng: `tabularx` + `booktabs`, không kẻ dọc, số canh theo dấu thập phân (cột `S`), đơn vị ở tiêu đề cột.
- `\fignote{Note: ... Source: ...}` dưới hình và bảng. Nguồn ghi theo Harvard: `Source: the group.`, `Source: OpenTrading version 0.5.1 \parencite{group2026opentrading}.`,
  hoặc trích dẫn nếu lấy của người khác. **Không ghi mã commit, đường dẫn file trong bài**; truy vết ở [05-evidence.md](05-evidence.md), gắn bằng chú thích `%% Evidence: Exx.`
- Code trong bài: tối đa 20 dòng, chỉ code của nhóm, `[float=htb]`; code dài để ở phụ lục.
- Thuật toán: `algorithm` + `algpseudocode`, có `\Require`/`\Ensure`.
- Công thức: giải thích mọi ký hiệu ngay sau công thức.
