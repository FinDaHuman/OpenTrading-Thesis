# 05. Bằng chứng

**Mỗi con số trong bài phải truy được về một file ở một commit.** Chưa truy được thì không viết.
PR thêm số mới phải thêm dòng vào bảng dưới. Ghi "đo" khi tự đếm lại được, "báo cáo" khi lấy từ tài liệu của nhóm.

## Sổ số liệu

| ID | Phát biểu được phép | Nguồn | Loại | Giới hạn bắt buộc ghi kèm |
|---|---|---|---|---|
| E01 | or16: OpenTrading 385/400 (96.25%), DSH 362/400 (90.50%), OpenCode 352/400 (88.00%) | benchmark `3be3e1b`, or16 MAIN-REPORT.md | báo cáo, đã đối chiếu JSONL | Bản OT đo là `38f8adb` (v0.4.0 + 36 commit), **không phải** bản hiện tại |
| E02 | Chênh lệch so với OT: OpenCode −8.25 pp [−12.75, −4.25]; DSH −5.75 pp [−9.25, −2.75] | như trên | báo cáo | Bootstrap ghép cặp theo bài, 2000 lần, CI 95% |
| E03 | Core 272/271/271 trên 280 (OT/OpenCode/DSH) | như trên | báo cáo | Ba harness **ngang nhau** ở phần core |
| E04 | Compute 53/54/43 trên 60 (OT/OpenCode/DSH) | như trên | báo cáo | OT còn `calculate`/`compute`; shell của hai đối thủ tắt |
| E05 | Memory 60/27/48 trên 60 (OT/OpenCode/DSH) | như trên | báo cáo | Tầng được thiết kế quanh khả năng của OT; OpenCode không có công cụ nhớ |
| E06 | Không tính Memory: 325/340, 325/340, 314/340 (OT/OpenCode/DSH) | như trên | đo | Phải nêu cùng E01 |
| E07 | Chi phí 1.498 / 0.972 / 0.944 USD (OT/OpenCode/DSH) | như trên, summary.json | báo cáo | OT có một lần thử không rõ chi phí: là chặn dưới |
| E08 | Judge LLM khớp **người duyệt là agent LLM** κ = 0.8498 (n = 71) | or16-main-kappa.json | đo | **Không** viết "khớp người chấm" |
| E09 | v4.7 chưa có kết quả; holdout chưa chạy | benchmark `3be3e1b` | đo | Chỉ nêu như thiết kế hoặc hướng phát triển |
| E10 | OpenTrading v0.5.1: 297 file TS trong `src`, 51,362 dòng; 23 tool có sẵn; 43 skill; 17 agent | OpenTrading `7319264` | đo | Dòng thô, gồm chú thích |
| E11 | OpenTrading: 2,253 test trên Ubuntu, 0 lỗi | CI run 45617110999 | đo | Tại `7319264` |
| E12 | opentrading-mcp: 175 tool đăng ký (174 khác nhau) | mcp `de956f8`, đếm bằng `list_tools` | đo | 176 khi có khóa web_search |
| E13 | opentrading-mcp: 1,338 test qua, độ phủ 71.69% | CI run 45325615006 | đo | Tại `de956f8` |
| E36 | Mốc theo tuần trong `tab:milestones`: chọn đề tài tuần 0, khảo sát harness tuần 2, demo I tuần 4, demo II tuần 7, or16 xong tuần 10, Review 1.1 tuần 13 | thesis `26226bb`, `admin/time-plan/2026FALL_G11.tex`, `admin/minutes/minutes.toml` | báo cáo | Ngày của tuần suy từ tuần 13 = Review 1.1, chưa đối chiếu FAP |
| E37 | Phát hành: 0.2.1 ngày 23/10/2026 (bản công khai đầu tiên), 0.5.0 ngày 24/11/2026, 0.5.1 ngày 25/11/2026 | GitHub releases của FinDaHuman/OpenTrading; `CHANGELOG.md` tại `7319264` | đo | 0.2.0 chưa từng phát hành |
| E38 | 0.2.0 không phát hành vì npm từ chối tên gói; gói đổi thành `@findahuman/opentrading` | OpenTrading `7319264`, `CHANGELOG.md:794-798` | báo cáo | |
| E39 | vnstock 6.0.0rc5 bị tắt từ 11/11/2026; 6.0.0 dùng được tới 10/11/2027 | opentrading-mcp `de956f8`, `README.md:43-44` | báo cáo | |
| E40 | Gói miễn phí Gemini: model Flash ngoài Flash-Lite chỉ 20 request/ngày | OpenTrading `7319264`, `docs/gemini-limits.md:12` | báo cáo | Theo trang Google ngày 25/11/2026 |
| E41 | or16: 132 lượt OT hỏng trước khi gọi model do symlink `node_modules` gãy khi dọn đĩa, đã chạy lại | benchmark `3be3e1b`, or16 MAIN-REPORT.md:50 | báo cáo | Lỗi hạ tầng, 0 request tới model |
| E42 | Token npm hết hạn muộn nhất 21/01/2027 | OpenTrading `7319264`, `docs/release.md:20` | báo cáo | |
| E43 | opentrading-benchmark: 1,199 test bộ v4.7 qua | CI run 45415688103 | đo | Tại commit của run đó |
| E44 | Server dữ liệu chạy gói miễn phí của Render | opentrading-mcp `de956f8`, `render.yaml:16` | đo | Không có chi phí hosting được ghi |
| E45 | Dự trù key OpenCode Go 10–15 USD | thesis `26226bb`, `admin/minutes/minutes.toml` tuần 8 | báo cáo | Dự trù, không phải chi thật; biên bản tuần 10 ghi 8 USD, chưa khớp E07 |
| E46 | Issue đầu tiên của repo OpenTrading (#268) mở ngày 13/11/2026, tức tuần 10 | GitHub issues của FinDaHuman/OpenTrading | đo | Trước tuần 10 không có issue; việc chỉ nằm trong pull request |
| E47 | Luật "thay đổi prompt/tool phải có số đo cặp nhỏ trước khi merge" có từ issue #354, ngày 16/11/2026, tức tuần 11 | GitHub issue FinDaHuman/OpenTrading#354 | báo cáo | Không áp dụng cho các thay đổi trước tuần 11 |

## Luật riêng

- Ghi phiên bản được đo ngay cạnh kết quả. Không gán kết quả v0.4.0 cho v0.5.x.
- Nêu cả kết quả kém và hòa, không chỉ chỗ thắng.
- Phân biệt: đăng ký trước, sửa đổi sau khi thấy kết quả, và phân tích thăm dò.
- So sánh phải có khoảng tin cậy hoặc kiểm định; không viết "significant" nếu chưa kiểm định.
- Không dùng số dòng commit để đo đóng góp của thành viên.
- Bài báo cáo tuần 10 không phải nguồn; một số câu chữ trong đó đã lỗi thời (E08).
