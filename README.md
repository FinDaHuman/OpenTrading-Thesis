# OpenTrading Thesis

LaTeX source của đồ án tốt nghiệp AIP491, Đại học FPT (FA26, nhóm G11):
**OpenTrading: An Agentic AI Harness for Financial Analysis and Market Research.**

Mã nguồn sản phẩm: [OpenTrading](https://github.com/FinDaHuman/OpenTrading) ·
[opentrading-mcp](https://github.com/DoanDuyLong212/opentrading-mcp) ·
[opentrading-benchmark](https://github.com/DoanDuyLong212/opentrading-benchmark)

## Cài trình biên dịch LaTeX

Cần **TeX Live 2026** (XeLaTeX, biber, latexmk) và **Python 3.11+**. Bản nộp luôn build trên Windows để có đúng font
Times New Roman, Arial, Courier New, Calibri, Cambria.

### Windows

**Cách 1, giao diện:** tải `install-tl-windows.exe` ở <https://tug.org/texlive/windows.html>, chạy, giữ `scheme-full`
(khoảng 8 GB), bấm Install, chờ 30 đến 90 phút.

**Cách 2, PowerShell, bản gọn (khoảng 3.600 gói, cỡ 10 phút):** đổi `D:/texlive` nếu muốn cài nơi khác.

```powershell
cd $env:TEMP
curl.exe -LO https://mirror.ctan.org/systems/texlive/tlnet/install-tl.zip
curl.exe -LO https://mirror.ctan.org/systems/texlive/tlnet/install-tl.zip.sha512
(Get-FileHash install-tl.zip -Algorithm SHA512).Hash -eq (Get-Content install-tl.zip.sha512).Split()[0]   # phải in True
Expand-Archive install-tl.zip -DestinationPath texlive-installer -Force
$repo = "D:/VsCode/OpenTrading-Thesis"        # thư mục repo trên máy bạn
& (Get-ChildItem texlive-installer\install-tl-*\install-tl-windows.bat).FullName -no-gui -non-admin -no-interaction -profile "$repo/tools/texlive.profile"
```

Mở PowerShell **mới** (để nhận PATH) rồi:

```powershell
tlmgr install carlito caladea
```

### macOS, Linux

macOS: `brew install --cask mactex-no-gui`. Ubuntu/Debian: dùng trình cài của TeX Live
(<https://tug.org/texlive/quickinstall.html>), vì gói `texlive` của hệ điều hành thường cũ. Không có font Microsoft thì class tự dùng font thay thế;
bản đó chỉ để xem, không nộp.

### Overleaf

Tải repo lên, Menu, Compiler: XeLaTeX, Main document: `main.tex`. Chỉ để xem nhanh.

### Kiểm tra

```
xelatex --version      # XeTeX ... (TeX Live 2026)
biber --version        # 2.22 hoặc mới hơn
latexmk --version
pip install -r requirements.txt
python tools/thesis.py test      # phải in "all tests passed"
```

VS Code: mở thư mục repo, cài extension được gợi ý **LaTeX Workshop**; `Ctrl+Alt+B` build, `Ctrl+Alt+V` xem PDF.

| Lỗi | Cách sửa |
|---|---|
| `xelatex` / `latexmk` not found | Mở terminal mới; hoặc thêm `D:\texlive\2026\bin\windows` vào PATH, hoặc đặt biến `TEXLIVE_BIN` |
| `File 'xxx.sty' not found` | `tlmgr install xxx` |
| Log ghi `fontset=fallback` | Máy thiếu font Microsoft; không dùng để nộp |
| `Unconfirmed value` khi build final | Điền thông tin trong `config/metadata.tex` |

## Viết bài

Đọc [rules/README.md](rules/README.md) trước. Đây là luật bắt buộc, CI kiểm tra phần lớn.

```
python tools/thesis.py draft              # build/main.pdf, còn hướng dẫn màu xanh và dấu DRAFT
python tools/thesis.py test               # mọi kiểm tra, chạy trước khi mở PR
python tools/thesis.py snapshot "ghi chú" # lưu một bản PDF có tên và phiên bản vào dist/
python tools/thesis.py admin              # Time plan (PDF) và Biên bản làm việc (Excel)
```

## Tài liệu trường yêu cầu nộp kèm

| Tài liệu | Nguồn | File sinh ra |
|---|---|---|
| Thesis | `main.tex` | `2026FALL_G11_Thesis.pdf` |
| Time plan, tối đa 2 trang A4 | `admin/time-plan/2026FALL_G11.tex` | `2026FALL_G11.pdf` |
| Biên bản làm việc GVHD và nhóm, mỗi tuần một sheet | `admin/minutes/minutes.toml` | `2026FALL_G11_Bien-ban-lam-viec.xlsx` |

Hai tài liệu sau đang là **bản nháp**: chữ đỏ là chỗ nhóm phải xác nhận. Slide không nằm trong repo này.

## Cấu trúc

| Đường dẫn | Nội dung |
|---|---|
| `main.tex` | Khung tài liệu, thứ tự các phần |
| `config/metadata.tex` | Tên đề tài, thành viên, GVHD, ngày; chỉ sửa ở đây |
| `frontmatter/` | Project Specification, Abstract, Acknowledgement, Definition and Acronyms |
| `chapters/` | Phần I đến VII |
| `appendices/` | Phần IX |
| `references/references.bib` | Phần VIII, tài liệu tham khảo |
| `figures/` | Hình; `figures/src` chứa nguồn và script tạo hình |
| `tex/` | Class `fptthesis` và style Harvard `fptharvard`; không sửa khi viết bài |
| `admin/` | Time plan và biên bản làm việc |
| `rules/` | Luật của nhóm |
| `tests/` | Bản sao hai template, bộ ví dụ Harvard, trang mẫu mọi thành phần |
| `tools/` | Build, kiểm tra, quản lý phiên bản PDF |
| `dist/` | PDF local, không commit |
| `local/` | File riêng trên máy mỗi người, không đẩy lên GitHub |

Trang mẫu để chép cú pháp hình, bảng, thuật toán, code, công thức, trích dẫn:
[tests/sample/sample.tex](tests/sample/sample.tex).

Bản quyền nội dung thuộc nhóm tác giả. Logo thuộc Đại học FPT.
