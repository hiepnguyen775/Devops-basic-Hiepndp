# 10 — Cloud Fundamentals

> Nơi để triển khai. Học **miễn phí** bằng LocalStack và Multipass.

---

## 🎯 Học xong bạn làm được gì

- Trách nhiệm chia sẻ — 'lên cloud' không tự động an toàn
- cloud-init: máy tự cấu hình lúc sinh ra
- `stop` vs `terminate` và các khoản tiền âm thầm

## 📋 Cần biết trước

Hoàn thành [`09-ci-cd/`](../09-ci-cd/)

## 📖 Bài học

| Ngày | Chủ đề |
|---|---|
| 26 | [Ngày 26 — Làm quen Cloud — Khái niệm & Free Tier](../Giai-doan-2-Git-Docker-Cloud.md#ngày-26--làm-quen-cloud--khái-niệm--free-tier) |
| 27 | [Ngày 27 — Máy chủ Cloud — Tạo & quản lý VM](../Giai-doan-2-Git-Docker-Cloud.md#ngày-27--máy-chủ-cloud--tạo--quản-lý-vm) |
| 28 | [Ngày 28 — Triển khai App lên Cloud (Docker trên VM)](../Giai-doan-2-Git-Docker-Cloud.md#ngày-28--triển-khai-app-lên-cloud-docker-trên-vm) |

### 🏁 LAB Final

[Ngày 30 — MILESTONE: LAB tổng hợp Giai đoạn 2](../Giai-doan-2-Git-Docker-Cloud.md#ngày-30--milestone-lab-tổng-hợp-giai-đoạn-2) — đề bài + rubric 100 điểm, **không hướng dẫn từng bước**

---

## 🧪 File LAB có sẵn

Các file trong bài học đã được **trích ra thành file thật** — `cd` vào là chạy được ngay.

| Thư mục | File | Chạy thử |
|---|---|---|
| [`labs/ngay-26/`](./labs/ngay-26/) | `chinh-sach-doc.json` · `docker-compose.yml` | `docker compose up -d` |
| [`labs/ngay-27/`](./labs/ngay-27/) | `cloud-init.yaml` · `kiem-tra.sh` | `./kiem-tra.sh` |
| [`labs/ngay-28/`](./labs/ngay-28/) | `app/Dockerfile` · `app/app.js` · `app/package.json` · `docker-compose.yml` · `nginx.conf` | `docker compose up -d` |

> ⚠️ **Hãy tự gõ tay khi làm bài lần đầu** — đó là cách kiến thức đọng lại. Thư mục này để **đối chiếu khi kẹt** và để chạy nhanh khi ôn lại.

---

## 📁 Thư mục làm việc của bạn

```text
10-cloud/
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
| ⬅️ Trước | [`09-ci-cd/`](../09-ci-cd/) |
| ➡️ Tiếp theo | [`11-kubernetes/`](../11-kubernetes/) |
| 🗺️ Toàn cảnh | [ROADMAP.md](../ROADMAP.md) |
| ✅ Tiến độ | [PROGRESS.md](../PROGRESS.md) |
| 🐛 Khi kẹt | [TROUBLESHOOTING.md](../TROUBLESHOOTING.md) |
