# 02 — Networking

> Không hiểu mạng thì mọi lỗi kết nối đều trông như phép màu.

---

## 🎯 Học xong bạn làm được gì

- Debug theo tầng: ping IP → ping tên → nc → curl
- Phân biệt `refused` (dịch vụ chết) vs `timeout` (tường lửa chặn)
- SSH bằng khoá, siết cấu hình mà không tự khoá mình
- Tường lửa chặn mặc định, chỉ mở cổng cần

## 📋 Cần biết trước

Hoàn thành [`01-linux/`](../01-linux/)

## 📖 Bài học

| Ngày | Chủ đề |
|---|---|
| 7 | [Ngày 7 — Mạng máy tính cho DevOps: Cơ bản](../Giai-doan-1-Linux-SysOps.md#ngày-7--mạng-máy-tính-cho-devops-cơ-bản) |
| 8 | [Ngày 8 — SSH: Kết nối & quản lý server từ xa](../Giai-doan-1-Linux-SysOps.md#ngày-8--ssh-kết-nối--quản-lý-server-từ-xa) |
| 9 | [Ngày 9 — Tường lửa, bảo mật & hardening](../Giai-doan-1-Linux-SysOps.md#ngày-9--tường-lửa-bảo-mật--hardening) |

### 📚 Đào sâu thêm

| Bài | Nội dung |
|---|---|
| [NT1 — Mạng chuyên sâu](../Module-Nen-Tang-Mo-Rong.md) | Subnet · định tuyến · tcpdump · chẩn đoán TLS |

---

## 🧪 Về thư mục `labs/`

Module này **chủ yếu là lệnh chẩn đoán** (`ss`, `dig`, `nc`, `curl`). Dùng `notes/` để ghi lại output thật của máy bạn — rất hữu ích khi so sánh lúc có sự cố.

---

## 📁 Thư mục làm việc của bạn

```text
02-networking/
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
| ⬅️ Trước | [`01-linux/`](../01-linux/) |
| ➡️ Tiếp theo | [`03-bash-python/`](../03-bash-python/) |
| 🗺️ Toàn cảnh | [ROADMAP.md](../ROADMAP.md) |
| ✅ Tiến độ | [PROGRESS.md](../PROGRESS.md) |
| 🐛 Khi kẹt | [TROUBLESHOOTING.md](../TROUBLESHOOTING.md) |
