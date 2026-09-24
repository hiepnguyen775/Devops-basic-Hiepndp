# 13 — Security / DevSecOps

> Gài bảo mật vào pipeline đã có, không phải bước cuối rời rạc.

---

## 🎯 Học xong bạn làm được gì

- Shift-left: phát hiện sớm rẻ hơn 50 lần
- Bốn lớp quét: bí mật, lỗ hổng, Dockerfile, hạ tầng
- `git rm` KHÔNG xoá bí mật khỏi lịch sử

## 📋 Cần biết trước

Hoàn thành [`12-monitoring-observability/`](../12-monitoring-observability/)

## 📖 Bài học

| Ngày | Chủ đề |
|---|---|
| 49 | [Ngày 49 — Bảo mật DevSecOps & Best Practices](../Giai-doan-3-CICD-K8s-Monitoring.md#ngày-49--bảo-mật-devsecops--best-practices) |

---

## 🧪 File LAB có sẵn

Các file trong bài học đã được **trích ra thành file thật** — `cd` vào là chạy được ngay.

| Thư mục | File | Chạy thử |
|---|---|---|
| [`labs/ngay-49/`](./labs/ngay-49/) | `.github/workflows/bao-mat.yml` · `.gitleaks.toml` · `.hadolint.yaml` | — |

> ⚠️ **Hãy tự gõ tay khi làm bài lần đầu** — đó là cách kiến thức đọng lại. Thư mục này để **đối chiếu khi kẹt** và để chạy nhanh khi ôn lại.

---

## 📁 Thư mục làm việc của bạn

```text
13-devsecops/
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
| ⬅️ Trước | [`12-monitoring-observability/`](../12-monitoring-observability/) |
| ➡️ Tiếp theo | [`14-gitops/`](../14-gitops/) |
| 🗺️ Toàn cảnh | [ROADMAP.md](../ROADMAP.md) |
| ✅ Tiến độ | [PROGRESS.md](../PROGRESS.md) |
| 🐛 Khi kẹt | [TROUBLESHOOTING.md](../TROUBLESHOOTING.md) |
