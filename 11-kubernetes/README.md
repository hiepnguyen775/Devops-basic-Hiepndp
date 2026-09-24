# 11 — Kubernetes

> Điều phối container ở quy mô lớn.

---

## 🎯 Học xong bạn làm được gì

- Vòng điều hoà — gốc của mọi tính năng K8s
- Deployment, Service, Ingress, ConfigMap, Secret, PVC
- Probe, requests/limits, HPA
- Helm: một chart, nhiều môi trường

## 📋 Cần biết trước

Hoàn thành [`10-cloud/`](../10-cloud/)

## 📖 Bài học

| Ngày | Chủ đề |
|---|---|
| 36 | [Ngày 36 — Kubernetes: Khái niệm & Kiến trúc](../Giai-doan-3-CICD-K8s-Monitoring.md#ngày-36--kubernetes-khái-niệm--kiến-trúc) |
| 37 | [Ngày 37 — Kubernetes: Pod, Deployment & ReplicaSet](../Giai-doan-3-CICD-K8s-Monitoring.md#ngày-37--kubernetes-pod-deployment--replicaset) |
| 38 | [Ngày 38 — Kubernetes: Service & Networking](../Giai-doan-3-CICD-K8s-Monitoring.md#ngày-38--kubernetes-service--networking) |
| 39 | [Ngày 39 — Kubernetes: ConfigMap, Secret & Storage](../Giai-doan-3-CICD-K8s-Monitoring.md#ngày-39--kubernetes-configmap-secret--storage) |
| 41 | [Ngày 41 — Kubernetes: Health Check, Resource & Autoscaling](../Giai-doan-3-CICD-K8s-Monitoring.md#ngày-41--kubernetes-health-check-resource--autoscaling) |
| 42 | [Ngày 42 — Helm: Package Manager cho Kubernetes](../Giai-doan-3-CICD-K8s-Monitoring.md#ngày-42--helm-package-manager-cho-kubernetes) |

### 🏁 LAB Final

[Ngày 40 — MILESTONE: Deploy Full-stack lên Kubernetes](../Giai-doan-3-CICD-K8s-Monitoring.md#ngày-40--milestone-deploy-full-stack-lên-kubernetes) — đề bài + rubric 100 điểm, **không hướng dẫn từng bước**

---

## 🧪 File LAB có sẵn

Các file trong bài học đã được **trích ra thành file thật** — `cd` vào là chạy được ngay.

| Thư mục | File | Chạy thử |
|---|---|---|
| [`labs/ngay-36/`](./labs/ngay-36/) | `deployment-web.yaml` · `pod-tran.yaml` | `kubectl apply -f .` |
| [`labs/ngay-37/`](./labs/ngay-37/) | `deployment-prod.yaml` | `kubectl apply -f .` |
| [`labs/ngay-38/`](./labs/ngay-38/) | `app-api.yaml` · `app-web.yaml` · `ingress.yaml` | `kubectl apply -f .` |
| [`labs/ngay-39/`](./labs/ngay-39/) | `app.yaml` · `bi-mat.yaml` · `cau-hinh.yaml` · `postgres.yaml` | — |
| [`labs/ngay-41/`](./labs/ngay-41/) | `app-probe.yaml` · `hpa-demo.yaml` | `kubectl apply -f .` |

> ⚠️ **Hãy tự gõ tay khi làm bài lần đầu** — đó là cách kiến thức đọng lại. Thư mục này để **đối chiếu khi kẹt** và để chạy nhanh khi ôn lại.

---

## 📁 Thư mục làm việc của bạn

```text
11-kubernetes/
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
| ⬅️ Trước | [`10-cloud/`](../10-cloud/) |
| ➡️ Tiếp theo | [`12-monitoring-observability/`](../12-monitoring-observability/) |
| 🗺️ Toàn cảnh | [ROADMAP.md](../ROADMAP.md) |
| ✅ Tiến độ | [PROGRESS.md](../PROGRESS.md) |
| 🐛 Khi kẹt | [TROUBLESHOOTING.md](../TROUBLESHOOTING.md) |
