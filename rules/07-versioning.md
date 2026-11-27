# 07. Phiên bản và PDF

## Số phiên bản

| Tag | Ý nghĩa |
|---|---|
| `v0.Y.Z` | Bản nháp. Tăng Y khi xong một phần hoặc một vòng review, tăng Z khi sửa nhỏ |
| `v1.0.0` | Bản chính thức đầu tiên, nộp Review 1.1 (28/11/2026); `v1.0.Z` là sửa sau góp ý, bản bảo vệ cũng tăng từ đây |

Tag có chú thích, trên `main`, sau khi CI xanh: `git tag -a v0.2.0 -m "Review 1.1"`.
Đẩy tag thì GitHub tự build và tạo Release kèm PDF và SHA256.

## PDF local

- `build/main.pdf` là bản tạm, luôn bị ghi đè. **Không gửi file này cho ai.**
- `python tools/thesis.py snapshot "ghi chú"` lưu vào `dist/drafts/` với tên chứa phiên bản, commit và giờ:
  `OpenTrading-Thesis_v0.1.0-3-gabc1234_20261126-210501_draft.pdf`.
  Hậu tố `-dirty` nghĩa là còn thay đổi chưa commit.
- `python tools/thesis.py admin` lưu bản nháp time plan và biên bản theo cùng cách đặt tên.
- Mỗi file được ghi vào `dist/MANIFEST.csv` (thời gian, commit, số trang, SHA256). Không bao giờ ghi đè.
- Bản nháp có dấu "DRAFT <phiên bản>" giữa footer. Bản final không có gì thêm; phiên bản và commit nằm trong thuộc tính PDF.

## Nộp bài

1. Mọi PR đã merge, `config/metadata.tex` đúng ngày nộp, `python tools/check.py --strict` sạch.
2. Gắn tag trên commit đó, rồi `python tools/thesis.py submit review1.1 <slide.pdf>` (slide xuất từ Canva, không commit; bỏ trống thì gói không có slide).
   Lệnh dừng nếu còn thay đổi chưa commit, chưa có tag, còn `\guide`/`\todo`/`\TBC`/`[CẦN XÁC NHẬN]`, hoặc sai định dạng.
3. File nộp ở `dist/submissions/<sự kiện>_<tag>/`: `Thesis.pdf`, `Time_Plan.pdf`, `Bien_ban_lam_viec.xlsx`, `Slide.pdf` và gói `Review1_1.zip` chứa cả bốn. Edunext cấm mã nhóm, dấu cách và ký tự đặc biệt trong tên file, nên tên file không có `G11`; mã nhóm vẫn nằm trong nội dung time plan. Review 1.1: tải **gói zip** vào thư mục Progress Reports (mỗi lần một file nén, tối đa 500 MB), rồi tải về kiểm tra. Nộp **đúng** các file này.
4. Commit `SUBMISSIONS.csv` qua PR. Đây là sổ các bản đã nộp, không sửa dòng cũ.

Chỉ bản build trên Windows với font Microsoft (log ghi `fontset=MS`) được nộp.
