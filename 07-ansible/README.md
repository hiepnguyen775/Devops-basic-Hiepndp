# 07 — Ansible / Configuration Management

> Cầu nối từ làm tay sang hạ tầng bằng code.

---

## 🎯 Học xong bạn làm được gì

- Idempotent — và vì sao Bash script thiếu nó lại nguy hiểm
- Inventory, playbook, module, handler
- `--check --diff` xem trước khi làm thật

## 📋 Cần biết trước

Hoàn thành [`06-docker/`](../06-docker/)

## 📖 Bài học

| Ngày | Chủ đề |
|---|---|
| 47 | [Ngày 47 — Configuration Management: Ansible](../Giai-doan-3-CICD-K8s-Monitoring.md#ngày-47--configuration-management-ansible) |

### 📚 Đào sâu thêm

| Bài | Nội dung |
|---|---|
| [NT3 — Ansible nâng cao](../Module-Nen-Tang-Mo-Rong.md) | Role · Vault đúng cách · `serial` · inventory động |

---

## 🧪 File LAB có sẵn

Các file trong bài học đã được **trích ra thành file thật** — `cd` vào là chạy được ngay.

| Thư mục | File | Chạy thử |
|---|---|---|
| [`labs/ngay-47/`](./labs/ngay-47/) | `Dockerfile.server` · `docker-compose.yml` · `inventory.ini` · `playbook.yml` · `templates/trang-chu.html.j2` | `docker compose up -d` |
| [`labs/nt3-ansible-nang-cao/`](./labs/nt3-ansible-nang-cao/) | `ansible.cfg` · `inventory-tu-terraform.py` · `roles/web/defaults/main.yml` · `roles/web/handlers/main.yml` · `roles/web/tasks/main.yml` · +2 | `ansible-playbook site.yml` |

> ⚠️ **Hãy tự gõ tay khi làm bài lần đầu** — đó là cách kiến thức đọng lại. Thư mục này để **đối chiếu khi kẹt** và để chạy nhanh khi ôn lại.

---

## 📁 Thư mục làm việc của bạn

```text
07-ansible/
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
| ⬅️ Trước | [`06-docker/`](../06-docker/) |
| ➡️ Tiếp theo | [`08-terraform/`](../08-terraform/) |
| 🗺️ Toàn cảnh | [ROADMAP.md](../ROADMAP.md) |
| ✅ Tiến độ | [PROGRESS.md](../PROGRESS.md) |
| 🐛 Khi kẹt | [TROUBLESHOOTING.md](../TROUBLESHOOTING.md) |
