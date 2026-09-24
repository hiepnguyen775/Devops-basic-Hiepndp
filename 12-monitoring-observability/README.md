# 12 — Monitoring & Observability

> Có hệ thống chạy rồi mới giám sát được.

---

## 🎯 Học xong bạn làm được gì

- Pull model, 4 loại metric, vì sao counter cần `rate()`
- Bốn tín hiệu vàng và vì sao p95 thay vì trung bình
- Log tập trung với Loki, và quy trình metric → log → trace

## 📋 Cần biết trước

Hoàn thành [`11-kubernetes/`](../11-kubernetes/)

## 📖 Bài học

| Ngày | Chủ đề |
|---|---|
| 44 | [Ngày 44 — Monitoring: Prometheus & Metrics](../Giai-doan-3-CICD-K8s-Monitoring.md#ngày-44--monitoring-prometheus--metrics) |
| 45 | [Ngày 45 — Monitoring: Grafana Dashboard](../Giai-doan-3-CICD-K8s-Monitoring.md#ngày-45--monitoring-grafana-dashboard) |
| 46 | [Ngày 46 — Logging tập trung: Loki](../Giai-doan-3-CICD-K8s-Monitoring.md#ngày-46--logging-tập-trung-loki) |

---

## 🧪 File LAB có sẵn

Các file trong bài học đã được **trích ra thành file thật** — `cd` vào là chạy được ngay.

| Thư mục | File | Chạy thử |
|---|---|---|
| [`labs/ngay-44/`](./labs/ngay-44/) | `alert.rules.yml` · `alertmanager.yml` · `docker-compose.yml` · `prometheus.yml` | `docker compose up -d` |
| [`labs/ngay-45/`](./labs/ngay-45/) | `grafana/provisioning/dashboards/dashboard.yml` · `grafana/provisioning/dashboards/he-thong.json` · `grafana/provisioning/datasources/prometheus.yml` | — |
| [`labs/ngay-46/`](./labs/ngay-46/) | `grafana/provisioning/datasources/loki.yml` · `loki-config.yaml` · `promtail-config.yaml` | — |

> ⚠️ **Hãy tự gõ tay khi làm bài lần đầu** — đó là cách kiến thức đọng lại. Thư mục này để **đối chiếu khi kẹt** và để chạy nhanh khi ôn lại.

---

## 📁 Thư mục làm việc của bạn

```text
12-monitoring-observability/
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
| ⬅️ Trước | [`11-kubernetes/`](../11-kubernetes/) |
| ➡️ Tiếp theo | [`13-devsecops/`](../13-devsecops/) |
| 🗺️ Toàn cảnh | [ROADMAP.md](../ROADMAP.md) |
| ✅ Tiến độ | [PROGRESS.md](../PROGRESS.md) |
| 🐛 Khi kẹt | [TROUBLESHOOTING.md](../TROUBLESHOOTING.md) |
