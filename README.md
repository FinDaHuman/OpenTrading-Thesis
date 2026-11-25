# OpenTrading Thesis

LaTeX source của đồ án tốt nghiệp AIP491, Đại học FPT (FA26, nhóm G11):
**OpenTrading: An Agentic AI Harness for Financial Analysis and Market Research.**

Mã nguồn sản phẩm: [OpenTrading](https://github.com/FinDaHuman/OpenTrading) ·
[opentrading-mcp](https://github.com/DoanDuyLong212/opentrading-mcp) ·
[opentrading-benchmark](https://github.com/DoanDuyLong212/opentrading-benchmark)

## Bắt đầu

1. Cài công cụ theo [rules/08-setup.md](rules/08-setup.md) (TeX Live 2026, Python 3.11 trở lên).
2. Đọc [rules/README.md](rules/README.md). Đây là luật bắt buộc, CI kiểm tra phần lớn.
3. Build và kiểm tra:

```
python tools/thesis.py draft              # build/main.pdf, còn hướng dẫn màu xanh và dấu DRAFT
python tools/thesis.py test               # mọi kiểm tra, chạy trước khi mở PR
python tools/thesis.py snapshot "ghi chú" # lưu một bản PDF có tên và phiên bản vào dist/
```

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
| `rules/` | Luật của nhóm |
| `tests/` | Bản sao hai template, bộ ví dụ Harvard, trang mẫu mọi thành phần |
| `tools/` | Build, kiểm tra, quản lý phiên bản PDF |
| `dist/` | PDF local, không commit |

Trang mẫu để chép cú pháp hình, bảng, thuật toán, code, công thức, trích dẫn:
[tests/sample/sample.tex](tests/sample/sample.tex).

Bản quyền nội dung thuộc nhóm tác giả. Logo thuộc Đại học FPT.
