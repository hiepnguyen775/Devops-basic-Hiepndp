# 14 — GitOps

> Git là nguồn sự thật; tác nhân trong cluster tự kéo về.

---

## 🎯 Học xong bạn làm được gì

- Push vs pull — ai giữ chìa khoá cluster
- Trôi cấu hình và cơ chế tự hoàn tác
- Rollback bằng `git revert`

## 📋 Cần biết trước

Hoàn thành [`13-devsecops/`](../13-devsecops/)

## 📖 Bài học

| Ngày | Chủ đề |
|---|---|
| 43 | [Ngày 43 — GitOps: ArgoCD & Triển khai khai báo](../Giai-doan-3-CICD-K8s-Monitoring.md#ngày-43--gitops-argocd--triển-khai-khai-báo) |

### 🏁 LAB Final

[Ngày 50 — MILESTONE: LAB tổng hợp Giai đoạn 3](../Giai-doan-3-CICD-K8s-Monitoring.md#ngày-50--milestone-lab-tổng-hợp-giai-đoạn-3) — đề bài + rubric 100 điểm, **không hướng dẫn từng bước**

---

## 🧪 File LAB có sẵn

Các file trong bài học đã được **trích ra thành file thật** — `cd` vào là chạy được ngay.

| Thư mục | File | Chạy thử |
|---|---|---|
| [`labs/ngay-43/`](./labs/ngay-43/) | `application.yaml` · `ung-dung/deployment.yaml` · `ung-dung/service.yaml` | `kubectl apply -f .` |

> ⚠️ **Hãy tự gõ tay khi làm bài lần đầu** — đó là cách kiến thức đọng lại. Thư mục này để **đối chiếu khi kẹt** và để chạy nhanh khi ôn lại.

---

## 📁 Thư mục làm việc của bạn

```text
14-gitops/
├── labs/        ← code và file cấu hình bạn viết khi làm LAB
├── exercises/   ← bài tập tự làm thêm
└── notes/       ← ghi chép của riêng bạn
```

> 💡 **Đây là nơi bạn làm việc.** Nội dung giảng dạy nằm trong các file giai đoạn ở thư mục gốc (đọc liền mạch dễ hơn); còn thư mục này để bạn **lưu thành quả** — commit nó lên GitHub, đó là bằng chứng bạn đã làm thật.

### Gợi ý ghi chép

Tạo `notes/nhat-ky.md` theo khuôn:

```markdown
## Ngày ___

**Hiểu được gì:**
**Bất ngờ nhất:**
**Lệnh mới học:**
**Kẹt ở đâu, gỡ thế nào:**
**Còn chưa rõ:**
```

---

## 🧭 Điều hướng

| | |
|---|---|
| ⬅️ Trước | [`13-devsecops/`](../13-devsecops/) |
| ➡️ Tiếp theo | [`15-advanced/`](../15-advanced/) |
| 🗺️ Toàn cảnh | [ROADMAP.md](../ROADMAP.md) |
| ✅ Tiến độ | [PROGRESS.md](../PROGRESS.md) |
| 🐛 Khi kẹt | [TROUBLESHOOTING.md](../TROUBLESHOOTING.md) |
