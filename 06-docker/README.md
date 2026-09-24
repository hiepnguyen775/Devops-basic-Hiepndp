# 06 — Docker & Container

> Đóng gói — nền của Kubernetes và CI/CD hiện đại.

---

## 🎯 Học xong bạn làm được gì

- Container khác VM ở điểm cốt lõi nào
- Dockerfile multi-stage, image dưới 200 MB, không chạy bằng root
- Volume, mạng, và dữ liệu sống sót khi container chết
- Compose: nhiều dịch vụ, thứ tự khởi động, healthcheck

## 📋 Cần biết trước

Hoàn thành [`05-web-server/`](../05-web-server/)

## 📖 Bài học

| Ngày | Chủ đề |
|---|---|
| 16 | [Ngày 16 — Docker: Khái niệm & container đầu tiên](../Giai-doan-2-Git-Docker-Cloud.md#ngày-16--docker-khái-niệm--container-đầu-tiên) |
| 17 | [Ngày 17 — Docker: Dockerfile & Build Image](../Giai-doan-2-Git-Docker-Cloud.md#ngày-17--docker-dockerfile--build-image) |
| 18 | [Ngày 18 — Docker: Image tối ưu & Multi-stage Build](../Giai-doan-2-Git-Docker-Cloud.md#ngày-18--docker-image-tối-ưu--multi-stage-build) |
| 19 | [Ngày 19 — Docker: Volume, Network & dữ liệu bền vững](../Giai-doan-2-Git-Docker-Cloud.md#ngày-19--docker-volume-network--dữ-liệu-bền-vững) |
| 20 | [Ngày 20 — Docker Compose: Quản lý multi-container](../Giai-doan-2-Git-Docker-Cloud.md#ngày-20--docker-compose-quản-lý-multi-container) |
| 22 | [Ngày 22 — YAML, JSON & định dạng cấu hình](../Giai-doan-2-Git-Docker-Cloud.md#ngày-22--yaml-json--định-dạng-cấu-hình) |
| 24 | [Ngày 24 — Cơ sở dữ liệu cho DevOps](../Giai-doan-2-Git-Docker-Cloud.md#ngày-24--cơ-sở-dữ-liệu-cho-devops) |

### 🏁 LAB Final

[Ngày 21 — MILESTONE: Đóng gói ứng dụng full-stack](../Giai-doan-2-Git-Docker-Cloud.md#ngày-21--milestone-đóng-gói-ứng-dụng-full-stack) — đề bài + rubric 100 điểm, **không hướng dẫn từng bước**

---

## 📁 Thư mục làm việc của bạn

```text
06-docker/
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
| ⬅️ Trước | [`05-web-server/`](../05-web-server/) |
| ➡️ Tiếp theo | [`07-ansible/`](../07-ansible/) |
| 🗺️ Toàn cảnh | [ROADMAP.md](../ROADMAP.md) |
| ✅ Tiến độ | [PROGRESS.md](../PROGRESS.md) |
| 🐛 Khi kẹt | [TROUBLESHOOTING.md](../TROUBLESHOOTING.md) |
