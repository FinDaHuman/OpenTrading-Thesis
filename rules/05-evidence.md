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
| E14 | v4.7 main: DeepSeek V4.1 Flash `deepseek-v4.1-flash-1017`, temperature 0, reasoning off; 3 arm; 2 lần chạy mỗi task (1,200 trial); trần 24 request (48 memory), 4.6M token, 1,800 s mỗi trial | benchmark `3be3e1b` `tools/bench_config.json`; run `main-20261124` `seal.json`, `run-entry.json` | đo | Cấu hình, không phải kết quả. Từ 25/11 chạy hai luồng (amendment) |
| E15 | Bộ đề v4.7: main 200 (L 30, C 69, M 51, I 20, R 16, S 14), holdout 70, pilot 57 | benchmark `3be3e1b` `experiments/finance-v47-study/tasks/` | đo | Holdout chưa chạy, gold public: không gọi là unseen |
| E16 | Arm được so: OpenTrading 0.5.0 + PR #437 (`ae7ec48`), OpenCode 2.4.1, DSH 0.2.2-rc.5 | benchmark `3be3e1b` `opentrading-runtime.SHA`, PR #36 | đo | **Không** phải v0.5.1; không ghép với E10, E11 |
| E17 | Judge Claude Haiku 5.5: 200/200 câu kiểm soát đúng, κ = 1.0 | benchmark `3be3e1b` `audits/judge-calibration-2026-11-24/haiku-5.5-kappa.json` | đo | Câu kiểm soát, không đo ca ranh giới |
| E18 | Nhóm R main: luôn trả lời BÁN đạt 11/16 | benchmark `3be3e1b` `audits/methodology-2026-11-16/DECISIONS.json` | đo | Mức nền khi đọc kết quả nhóm R |

## Luật riêng

- Ghi phiên bản được đo ngay cạnh kết quả. Không gán kết quả v0.4.0 cho v0.5.x.
- Nêu cả kết quả kém và hòa, không chỉ chỗ thắng.
- Phân biệt: đăng ký trước, sửa đổi sau khi thấy kết quả, và phân tích thăm dò.
- So sánh phải có khoảng tin cậy hoặc kiểm định; không viết "significant" nếu chưa kiểm định.
- Không dùng số dòng commit để đo đóng góp của thành viên.
- Bài báo cáo tuần 10 không phải nguồn; một số câu chữ trong đó đã lỗi thời (E08).
