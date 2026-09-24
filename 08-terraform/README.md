# 08 — Terraform / Infrastructure as Code

> Tạo hạ tầng bằng code, không bấm chuột.

---

## 🎯 Học xong bạn làm được gì

- State là gì và điều gì xảy ra khi mất nó
- Đọc `terraform plan`, nhận ra dấu hiệu huỷ-tạo-lại
- Module tái sử dụng, remote state có khoá, workspace

## 📋 Cần biết trước

Hoàn thành [`07-ansible/`](../07-ansible/)

## 📖 Bài học

| Ngày | Chủ đề |
|---|---|
| 29 | [Ngày 29 — Infrastructure as Code — Giới thiệu Terraform](../Giai-doan-2-Git-Docker-Cloud.md#ngày-29--infrastructure-as-code--giới-thiệu-terraform) |
| 48 | [Ngày 48 — Terraform nâng cao: Module, Remote State & Workspace](../Giai-doan-3-CICD-K8s-Monitoring.md#ngày-48--terraform-nâng-cao-module-remote-state--workspace) |

---

## 🧪 File LAB có sẵn

Các file trong bài học đã được **trích ra thành file thật** — `cd` vào là chạy được ngay.

| Thư mục | File | Chạy thử |
|---|---|---|
| [`labs/ngay-29/`](./labs/ngay-29/) | `main.tf` | `terraform init && terraform apply` |
| [`labs/ngay-48/`](./labs/ngay-48/) | `main.tf` · `minio-compose.yml` · `modules/ung-dung/main.tf` · `modules/ung-dung/outputs.tf` · `modules/ung-dung/variables.tf` · +1 | `terraform init && terraform apply` |

> ⚠️ **Hãy tự gõ tay khi làm bài lần đầu** — đó là cách kiến thức đọng lại. Thư mục này để **đối chiếu khi kẹt** và để chạy nhanh khi ôn lại.

---

## 📁 Thư mục làm việc của bạn

```text
08-terraform/
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
| ⬅️ Trước | [`07-ansible/`](../07-ansible/) |
| ➡️ Tiếp theo | [`09-ci-cd/`](../09-ci-cd/) |
| 🗺️ Toàn cảnh | [ROADMAP.md](../ROADMAP.md) |
| ✅ Tiến độ | [PROGRESS.md](../PROGRESS.md) |
| 🐛 Khi kẹt | [TROUBLESHOOTING.md](../TROUBLESHOOTING.md) |
