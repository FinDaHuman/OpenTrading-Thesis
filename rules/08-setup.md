# 08. Cài đặt

## Windows (máy chuẩn để build bản nộp)

1. TeX Live 2026: tải `install-tl-windows.exe` từ <https://tug.org/texlive/windows.html>, chọn `scheme-full`
   (khoảng 8 GB), hoặc cài nhẹ với các collection: basic, bibtexextra, binextra, fontsrecommended, fontutils, langenglish,
   langother, latex, latexextra, latexrecommended, luatex, mathscience, pictures, plaingeneric, wintools, xetex,
   rồi `tlmgr install carlito caladea`.
2. Python 3.11 trở lên, rồi `pip install -r requirements.txt`.
3. Mở terminal **mới**, kiểm tra: `xelatex --version`, `biber --version`, `latexmk --version`.
4. `python tools/thesis.py test` phải in `all tests passed`.

## VS Code

Mở thư mục repo, cài extension được gợi ý (LaTeX Workshop). `Ctrl+Alt+B` build, `Ctrl+Alt+V` xem PDF.

## macOS, Linux, Overleaf

Build được. Không có font Microsoft thì class tự dùng TeX Gyre, Carlito, Caladea (log ghi `fontset=fallback`);
dàn trang có thể lệch nhẹ và **không dùng để nộp**. Overleaf: chọn compiler XeLaTeX.

## Cập nhật

`tlmgr update --self --all` chỉ khi cả nhóm thống nhất; chạy lại `thesis.py test` sau khi cập nhật.
