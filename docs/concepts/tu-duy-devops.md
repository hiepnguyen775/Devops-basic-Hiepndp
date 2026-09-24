# 🧠 Tư duy DevOps — Bảy nguyên tắc lặp lại xuyên suốt

> Công cụ sẽ đổi. Bảy nguyên tắc dưới đây thì không — và chúng xuất hiện lại ở **mọi giai đoạn** của khoá học.
>
> Đọc file này sau Giai đoạn 1, rồi đọc lại sau Giai đoạn 3. Lần hai bạn sẽ thấy khác hẳn.

---

## 1. Khai báo, không ra lệnh

| | Ra lệnh | Khai báo |
|---|---|---|
| Bạn nói | *"Chạy các bước này"* | *"Hệ thống phải trông như thế này"* |
| Ai giữ đúng | Bạn | **Hệ thống** |
| Chạy lại lần hai | Có thể hỏng | An toàn |

**Gặp lại ở:** Kubernetes (Ngày 36) · Ansible (47) · Terraform (29, 48) · GitOps (43)

Điểm chung của cả bốn: một **vòng điều hoà** liên tục so *mong muốn* với *thực tế* rồi sửa cho khớp. Nắm được khuôn này thì học công cụ thứ hai trở đi nhanh hơn hẳn.

---

## 2. Đặc quyền tối thiểu

Cho đúng quyền cần thiết, không hơn. Khi có sự cố, đây là thứ quyết định thiệt hại dừng ở một container hay lan ra cả hệ thống.

**Gặp lại ở:**

| Ngày | Biểu hiện |
|---|---|
| 4, 9 | User riêng cho từng việc, không dùng root |
| 26 | IAM policy chỉ cho đúng hành động cần |
| 31, 33 | `permissions:` của `GITHUB_TOKEN` |
| 33 | Container chạy bằng user thường |
| 39 | RBAC giới hạn ai đọc được Secret |
| 43 | GitOps — **không ai bên ngoài** giữ chìa khoá cluster |

---

## 3. Bất biến và tái lập được

Thứ gì **dựng lại được từ số 0** mới đáng tin. Thứ gì chỉ tồn tại vì "ai đó đã cấu hình nó" là quả bom hẹn giờ.

**Gặp lại ở:** image tag theo SHA (33) · cloud-init (27) · Terraform (29) · Helm (42) · "máy chủ là đồ dùng một lần" (27, 36)

**Phép thử:** xoá sạch rồi dựng lại. Nếu kết quả không giống hệt, bạn chưa có Infrastructure as Code — bạn chỉ có tài liệu mô tả.

---

## 4. Thất bại nhanh, phục hồi nhanh

Không ngăn được mọi lỗi. Nhưng **giảm được thời gian phát hiện và thời gian sửa**.

| Biểu hiện | Ngày |
|---|---|
| `set -euo pipefail` — dừng ngay khi lỗi | 5 |
| Lint trước test, test trước build | 32 |
| Healthcheck chặn bản hỏng | 34 |
| Timeout — thất bại nhanh hơn treo | 54 |
| Rollback dễ quan trọng hơn deploy nhanh | 34, 43 |

---

## 5. Đo trước, tối ưu sau

Không đo được thì mọi cải thiện đều là phỏng đoán.

| Bạn muốn | Phải đo gì trước |
|---|---|
| Tăng độ tin cậy | SLI hiện tại là bao nhiêu (51) |
| Giảm chi phí | Đang dùng bao nhiêu so với đặt chỗ (53) |
| Pipeline nhanh hơn | Bước nào đang lâu nhất (32, 35) |
| Hệ thống nhanh hơn | `rt` vs `urt` — chậm ở đâu (NT2) |

---

## 6. Chỉ lộ ra thứ cần lộ

| Tầng | Biểu hiện |
|---|---|
| Linux | Tường lửa chặn mặc định, mở đúng cổng cần (9) |
| Docker | `expose` thay vì `ports` cho dịch vụ nội bộ (19, 28) |
| Kubernetes | ClusterIP mặc định, Ingress là cửa duy nhất (38) |
| Cloud | Security group chặn hết chiều vào (27) |

---

## 7. Tài liệu là một phần của hệ thống

Hệ thống không ai hiểu được thì với người khác, nó **không tồn tại**.

| Loại | Trả lời câu hỏi | Ngày |
|---|---|---|
| README | *Cái này là gì, chạy thế nào?* | 59 |
| ADR | *Vì sao chọn cái này, đánh đổi gì?* | 56 |
| Runbook | *Sự cố rồi làm gì ngay?* | 45, 59 |
| Postmortem | *Vì sao hỏng, làm sao không tái diễn?* | 51 |

---

## Bài kiểm tra: bạn đã ngấm chưa?

Với **mỗi** nguyên tắc, tự trả lời: *"tôi đã gặp nó ở những ngày nào, và nó biểu hiện khác nhau ra sao?"*

Nếu kể được từ 3 chỗ trở lên cho mỗi nguyên tắc, bạn đã có **mô hình tư duy** — thứ còn lại khi cú pháp đã quên.

---

[⬅️ docs](../README.md) · [🗺️ ROADMAP](../../ROADMAP.md)
