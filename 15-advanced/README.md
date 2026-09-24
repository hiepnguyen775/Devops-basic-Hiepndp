# 15 — Advanced DevOps / SRE

> Nâng từ 'chạy được' lên 'tin cậy đo được'.

---

## 🎯 Học xong bạn làm được gì

- SLI/SLO/SLA, ngân sách lỗi, cảnh báo theo burn rate
- HA, DR, RTO/RPO — và sao lưu phải khôi phục thử
- FinOps: đo lãng phí, right-sizing, gắn thẻ
- Sập dây chuyền và bốn tấm khiên; DORA, golden path

## 📋 Cần biết trước

Hoàn thành [`14-gitops/`](../14-gitops/)

## 📖 Bài học

| Ngày | Chủ đề |
|---|---|
| 51 | [Ngày 51 — Site Reliability Engineering (SRE) — Nguyên lý](../Giai-doan-4-SRE-Capstone.md#ngày-51--site-reliability-engineering-sre--nguyên-lý) |
| 52 | [Ngày 52 — High Availability, Scaling & Disaster Recovery](../Giai-doan-4-SRE-Capstone.md#ngày-52--high-availability-scaling--disaster-recovery) |
| 53 | [Ngày 53 — Cost Optimization & FinOps](../Giai-doan-4-SRE-Capstone.md#ngày-53--cost-optimization--finops) |
| 54 | [Ngày 54 — Service Mesh & Microservices nâng cao](../Giai-doan-4-SRE-Capstone.md#ngày-54--service-mesh--microservices-nâng-cao) |
| 55 | [Ngày 55 — Platform Engineering & Developer Experience](../Giai-doan-4-SRE-Capstone.md#ngày-55--platform-engineering--developer-experience) |

### 📚 Đào sâu thêm

| Bài | Nội dung |
|---|---|
| [Module nâng cao bổ sung](../Module-Nang-Cao-Bo-Sung.md) | Tracing · Vault · Kafka · Managed K8s |

---

## 🧪 File LAB có sẵn

Các file trong bài học đã được **trích ra thành file thật** — `cd` vào là chạy được ngay.

| Thư mục | File | Chạy thử |
|---|---|---|
| [`labs/ngay-51/`](./labs/ngay-51/) | `blackbox.yml` · `slo.rules.yml` | — |
| [`labs/ngay-52/`](./labs/ngay-52/) | `docker-compose.yml` · `nginx-lb.conf` | `docker compose up -d` |
| [`labs/ngay-53/`](./labs/ngay-53/) | `bang-gia.json` · `tim-rac.sh` · `tinh-lang-phi.py` | `./tim-rac.sh` |
| [`labs/ngay-54/`](./labs/ngay-54/) | `docker-compose.yml` · `gateway-co-khien.conf` · `gateway-ngay-tho.conf` | `docker compose up -d` |
| [`labs/ngay-55/`](./labs/ngay-55/) | `do-dora.py` · `mau/Dockerfile` · `mau/Makefile` · `mau/ci.yml` · `tao-dich-vu.sh` | `./tao-dich-vu.sh` |

> ⚠️ **Hãy tự gõ tay khi làm bài lần đầu** — đó là cách kiến thức đọng lại. Thư mục này để **đối chiếu khi kẹt** và để chạy nhanh khi ôn lại.

---

## 📁 Thư mục làm việc của bạn

```text
15-advanced/
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
| ⬅️ Trước | [`14-gitops/`](../14-gitops/) |
| ➡️ Tiếp theo | [`capstone/`](../capstone/) |
| 🗺️ Toàn cảnh | [ROADMAP.md](../ROADMAP.md) |
| ✅ Tiến độ | [PROGRESS.md](../PROGRESS.md) |
| 🐛 Khi kẹt | [TROUBLESHOOTING.md](../TROUBLESHOOTING.md) |
