# 09 — CI/CD

> Lấy quy trình ra khỏi đầu bạn và viết thành file để máy chạy.

---

## 🎯 Học xong bạn làm được gì

- Pipeline nhiều tầng, cache, artifact, branch protection
- Image tag bất biến theo SHA — điều kiện để rollback
- Deploy tự động có kiểm tra sức khoẻ và đường lui

## 📋 Cần biết trước

Hoàn thành [`08-terraform/`](../08-terraform/)

## 📖 Bài học

| Ngày | Chủ đề |
|---|---|
| 31 | [Ngày 31 — CI/CD: Khái niệm & GitHub Actions cơ bản](../Giai-doan-3-CICD-K8s-Monitoring.md#ngày-31--cicd-khái-niệm--github-actions-cơ-bản) |
| 32 | [Ngày 32 — CI Pipeline: Build, Test & Lint tự động](../Giai-doan-3-CICD-K8s-Monitoring.md#ngày-32--ci-pipeline-build-test--lint-tự-động) |
| 33 | [Ngày 33 — CD Pipeline: Build & Push Docker Image](../Giai-doan-3-CICD-K8s-Monitoring.md#ngày-33--cd-pipeline-build--push-docker-image) |
| 34 | [Ngày 34 — CD Pipeline: Tự động Deploy lên Server](../Giai-doan-3-CICD-K8s-Monitoring.md#ngày-34--cd-pipeline-tự-động-deploy-lên-server) |

### 🏁 LAB Final

[Ngày 35 — MILESTONE: Pipeline CI/CD hoàn chỉnh](../Giai-doan-3-CICD-K8s-Monitoring.md#ngày-35--milestone-pipeline-cicd-hoàn-chỉnh) — đề bài + rubric 100 điểm, **không hướng dẫn từng bước**

---

## 🧪 File LAB có sẵn

Các file trong bài học đã được **trích ra thành file thật** — `cd` vào là chạy được ngay.

| Thư mục | File | Chạy thử |
|---|---|---|
| [`labs/ngay-31/`](./labs/ngay-31/) | `.github/workflows/ci.yml` · `app.js` · `package.json` · `src/tinh-tien.js` · `test/tinh-tien.test.js` | — |
| [`labs/ngay-32/`](./labs/ngay-32/) | `.github/workflows/ci.yml` · `eslint.config.js` · `package.json` | — |
| [`labs/ngay-33/`](./labs/ngay-33/) | `.dockerignore` · `.github/workflows/cd-image.yml` · `Dockerfile` | — |
| [`labs/ngay-34/`](./labs/ngay-34/) | `.github/workflows/deploy.yml` · `deploy/docker-compose.prod.yml` | — |

> ⚠️ **Hãy tự gõ tay khi làm bài lần đầu** — đó là cách kiến thức đọng lại. Thư mục này để **đối chiếu khi kẹt** và để chạy nhanh khi ôn lại.

---

## 📁 Thư mục làm việc của bạn

```text
09-ci-cd/
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
| ⬅️ Trước | [`08-terraform/`](../08-terraform/) |
| ➡️ Tiếp theo | [`10-cloud/`](../10-cloud/) |
| 🗺️ Toàn cảnh | [ROADMAP.md](../ROADMAP.md) |
| ✅ Tiến độ | [PROGRESS.md](../PROGRESS.md) |
| 🐛 Khi kẹt | [TROUBLESHOOTING.md](../TROUBLESHOOTING.md) |
