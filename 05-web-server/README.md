# 05 — Web Server / Reverse Proxy

> Hiểu cách một request tới được ứng dụng, trước khi đóng gói ứng dụng.

---

## 🎯 Học xong bạn làm được gì

- Reverse proxy làm gì và vì sao cần nó
- Cấu hình nginx: server block, location, upstream
- Kỷ luật `nginx -t` trước mọi lần reload

## 📋 Cần biết trước

Hoàn thành [`04-git/`](../04-git/)

## 📖 Bài học

| Ngày | Chủ đề |
|---|---|
| 23 | [Ngày 23 — Reverse Proxy & Web Server (Nginx chuyên sâu)](../Giai-doan-2-Git-Docker-Cloud.md#ngày-23--reverse-proxy--web-server-nginx-chuyên-sâu) |

### 📚 Đào sâu thêm

| Bài | Nội dung |
|---|---|
| [NT2 — Web Server production](../Module-Nen-Tang-Mo-Rong.md) | HTTPS thật · 4 thuật toán cân bằng tải · tinh chỉnh · log điều tra |

---

## 📁 Thư mục làm việc của bạn

```text
05-web-server/
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
| ⬅️ Trước | [`04-git/`](../04-git/) |
| ➡️ Tiếp theo | [`06-docker/`](../06-docker/) |
| 🗺️ Toàn cảnh | [ROADMAP.md](../ROADMAP.md) |
| ✅ Tiến độ | [PROGRESS.md](../PROGRESS.md) |
| 🐛 Khi kẹt | [TROUBLESHOOTING.md](../TROUBLESHOOTING.md) |
