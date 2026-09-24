# 🚀 Lộ trình SysOps & DevOps 60 Ngày — Từ cơ bản đến nâng cao

> Tài liệu học **SysOps & DevOps** trong 60 ngày, dành cho người mới biết Linux căn bản.
> Mỗi ngày ~90 phút: **Lý thuyết → LAB (file đầy đủ) → Hướng dẫn step by step → Đúc kết**.
>
> 🎯 **Nguyên tắc biên soạn:** mọi LAB đều **chạy được thật**, mọi lệnh đều có **output mẫu** để bạn tự đối chiếu, và mỗi bài đều có ít nhất một lần **bạn tự gây sự cố** để thấy hệ thống phản ứng.
>
> 💻 **Chạy miễn phí 100%** trên máy bạn — không cần tài khoản cloud, không cần thẻ tín dụng.
>
> ✅ Trung lập nền tảng — học xong áp dụng được cho **server vật lý, máy ảo, hay cloud (AWS/GCP/Azure)**.

---

## 📚 Cấu trúc khóa học

| Giai đoạn | Ngày | Nội dung | Trạng thái |
|-----------|------|----------|------------|
| **GĐ 1** | 1–12 | Nền tảng Hệ thống & Linux (SysOps Foundation) | ✅ Hoàn thành |
| **GĐ 2** | 13–30 | Git, Docker & Container hóa | ✅ Hoàn thành |
| **GĐ 3** | 31–50 | CI/CD, Kubernetes & Tự động hóa nâng cao | ✅ Hoàn thành |
| **GĐ 4** | 51–60 | SRE, Chủ đề nâng cao & Dự án tốt nghiệp | ✅ Hoàn thành |

## 🧭 Bắt đầu từ đâu

**Lần đầu mở repo này?** Đọc theo đúng thứ tự sau:

| # | File | Mất bao lâu | Để làm gì |
|---|---|---|---|
| 1 | [**ROADMAP.md**](./ROADMAP.md) | 10 phút | Hiểu **học gì, thứ tự nào, vì sao thứ tự đó** + mental model DevOps |
| 2 | [**HOC-HANG-NGAY.md**](./HOC-HANG-NGAY.md) | 10 phút | Khuôn một buổi học · nhịp tuần · nhịp tháng — **thứ quyết định bạn có đi hết 60 ngày** |
| 3 | [Tài liệu tham khảo](./Tai-lieu-tham-khao.md) | 5 phút | Cách kết hợp tài liệu này với docs chính thức và cộng đồng |
| 4 | [**PROGRESS.md**](./PROGRESS.md) | 2 phút | Mở sẵn để tick từng ngày — đây là bảng theo dõi của bạn |
| 5 | Ngày 1 | 90 phút | Bắt đầu học |

**Sáu file tra cứu — mở khi cần, không đọc tuần tự:**

| File | Mở khi |
|---|---|
| 📚 [**GLOSSARY.md**](./GLOSSARY.md) | Gặp thuật ngữ lạ — 364 thuật ngữ, có link về bài gốc |
| 🐛 [**TROUBLESHOOTING.md**](./TROUBLESHOOTING.md) | **Đang kẹt vì một lỗi** — 118 lỗi gom theo chủ đề + quy trình chẩn đoán 9 bước |
| 🏗️ [**PROJECTS.md**](./PROJECTS.md) | Cuối mỗi tháng — 5 dự án + capstone, có rubric và bài tập 4 mức |
| 🧠 [**QUIZ-TONG-HOP.md**](./QUIZ-TONG-HOP.md) | Cuối mỗi giai đoạn — 4 bộ × 20 câu tự kiểm tra |
| 🎤 [**INTERVIEW.md**](./INTERVIEW.md) | Chuẩn bị phỏng vấn — 25 câu tình huống kèm đáp án tham khảo |
| ✅ [**PROGRESS.md**](./PROGRESS.md) | Sau mỗi ngày học, và khi muốn biết mình đang ở đâu |

---

## 🗂️ Cấu trúc repository

```text
devops-60-ngay/
│
├── README.md · ROADMAP.md · PROGRESS.md      ← bắt đầu ở đây
├── GLOSSARY.md · TROUBLESHOOTING.md          ← tra cứu
├── PROJECTS.md · QUIZ-TONG-HOP.md            ← thực hành & tự kiểm tra
├── INTERVIEW.md · HOC-HANG-NGAY.md
│
├── Giai-doan-1..4-*.md                       ← NỘI DUNG 60 ngày (đọc liền mạch)
├── Module-*.md                               ← 3 module bổ sung
│
├── docs/
│   ├── architecture/lab-topology.md          ← dựng môi trường lab
│   ├── concepts/tu-duy-devops.md             ← 7 nguyên tắc xuyên suốt
│   └── references/cheat-sheet.md             ← tra lệnh nhanh
│
├── 00-devops-fundamentals/ … 15-advanced/    ← 16 module: cổng vào + nơi bạn làm việc
│   ├── README.md    (mục tiêu · bài học · điều hướng)
│   ├── labs/        (code bạn viết)
│   ├── exercises/   (bài tập tự làm)
│   └── notes/       (ghi chép của bạn)
│
├── projects/project-01..05/                  ← 5 dự án
├── capstone/                                 ← dự án tốt nghiệp của bạn
└── capstone-cloudnote/                       ← bộ khung code mẫu
```

> 💡 **Vì sao tách làm hai chỗ:** nội dung giảng dạy nằm trong các file giai đoạn (đọc liền mạch dễ hơn nhiều so với nhảy qua 60 file nhỏ). Các thư mục module là **cổng vào** — mỗi cái có README nêu mục tiêu, danh sách bài, và **thư mục trống để bạn lưu thành quả**.
>
> Bắt đầu một module: mở `README.md` của nó → bấm link sang bài học → làm LAB → lưu kết quả vào `labs/` của chính thư mục đó.

---

## 📂 Danh sách tài liệu

**Lộ trình chính (60 ngày):**
- [Giai đoạn 1 — Nền tảng Linux & SysOps (Ngày 1–12)](./Giai-doan-1-Linux-SysOps.md)
- [Giai đoạn 2 — Git, Docker & Cloud (Ngày 13–30)](./Giai-doan-2-Git-Docker-Cloud.md)
- [Giai đoạn 3 — CI/CD, Kubernetes & Monitoring (Ngày 31–50)](./Giai-doan-3-CICD-K8s-Monitoring.md)
- [Giai đoạn 4 — SRE & Dự án Tốt nghiệp (Ngày 51–60)](./Giai-doan-4-SRE-Capstone.md)

**Bổ sung (nên học kèm):**
- 🐍 [Module Python cho DevOps (3 ngày)](./Module-Python-cho-DevOps.md) — học sau Bash (Ngày 5–6); lấp khoảng trống so với roadmap chuẩn.
- 🧱 [**Module Nền tảng Mở rộng (3 bài)**](./Module-Nen-Tang-Mo-Rong.md) — đào sâu ba chỗ mà lộ trình chính chỉ kịp chạm bề mặt: **NT1 Mạng chuyên sâu** (subnet, định tuyến, `tcpdump`, chẩn đoán TLS — học sau Ngày 9) · **NT2 Web Server production** (HTTPS thật, 4 thuật toán cân bằng tải, tinh chỉnh — sau Ngày 23) · **NT3 Ansible nâng cao** (role, Vault đúng cách, cập nhật không gián đoạn, inventory động — sau Ngày 47).
- 🧩 [**Module nâng cao bổ sung (4 bài)**](./Module-Nang-Cao-Bo-Sung.md) — học **sau Giai đoạn 3**; lấp nốt các lỗ hổng so với roadmap chuẩn: **Distributed Tracing** (OpenTelemetry+Jaeger — trụ cột observability thứ 3), **HashiCorp Vault** (quản secret production), **Message Queue** (Kafka & RabbitMQ), **Managed K8s + cert-manager + Serverless**.
- 📚 [Tài liệu tham khảo & Cách học hiệu quả](./Tai-lieu-tham-khao.md) — docs chính thức, nền tảng lab tương tác, cộng đồng. **Đọc file này trước khi bắt đầu.**
- 🏗️ [**Bộ khung dự án tốt nghiệp — CloudNote**](./capstone-cloudnote/) — code thật sẵn sàng (FastAPI + Postgres + Docker + K8s + Terraform + CI/CD + Monitoring) kèm sơ đồ kiến trúc. Chạy local bằng 1 lệnh `docker compose up`, rồi tự hoàn thiện các `# TODO`.

> ⚠️ **Quan trọng — tài liệu này không thay thế thực hành:** lộ trình giúp bạn biết *học gì, thứ tự nào, tại sao*. Nhưng phải **gõ tay làm lab trên môi trường thật** + **đối chiếu docs chính thức** + **hỏi cộng đồng khi kẹt** mới thật sự học được. Xem [Tài liệu tham khảo](./Tai-lieu-tham-khao.md) để biết cách kết hợp.

---

## 🎯 Cách dùng tài liệu hiệu quả

1. **Mỗi ngày dành 60–90 phút**, không vội.
2. **Gõ tay tất cả lệnh** — không copy-paste, để cơ tay và đầu cùng nhớ.
3. Làm đủ **3 tầng**: Lab cơ bản (hiểu) → Lab nâng cao (làm như production) → Bài ôn tập (tự kiểm tra).
4. **Đẩy mọi sản phẩm lên GitHub** — cuối khóa bạn có một portfolio thực chiến.
5. Chưa hiểu ngày nào thì **học lại trước khi đi tiếp** — DevOps là kiến thức tích lũy.

## 🧩 Mỗi ngày gồm

| Phần | Nội dung |
|---|---|
| 📘 **Lý thuyết** | Mở bằng **một vấn đề có thật**, rồi mới tới khái niệm. Có bảng so sánh và ẩn dụ để nhớ lâu |
| 🧪 **LAB** | **File đầy đủ, copy là chạy** — không cắt khúc, không "bạn tự điền phần còn lại" |
| 🧭 **Hướng dẫn step by step** | Mỗi bước: gõ gì → **khối output mẫu bạn sẽ thấy** → ✅ Checkpoint → ⚠️ lỗi cụ thể và cách sửa → 💡 vì sao |
| 💡 **Đi làm mới thấm** | Kiến thức production mà giáo trình cơ bản hay bỏ quên |
| 🎯 **Đúc kết + Tự chấm** | 3 điều phải mang theo + checklist tự đánh giá |

### 🏁 Ngày Milestone = LAB Final

**Ngày 12, 21, 30, 35, 40, 50** và **dự án tốt nghiệp (56–59)** theo khuôn khác hẳn — **không có hướng dẫn từng bước**:

📋 Đề bài → ✅ Yêu cầu (bắt buộc + nâng cao) → 📐 **Tiêu chí chấm điểm 100 điểm** → 🔥 Phép thử khắc nghiệt → 🧪 Script tự chấm → ⚠️ Bẫy thường gặp → 💬 Gợi ý khi bí (giấu trong `<details>`)

**Ngày 60** là **LAB FINAL toàn khoá**: bài kiểm tra 100 điểm (chẩn đoán sự cố / thiết kế / thực hành) + bảng tự đánh giá năng lực 48 điểm + 5 câu phỏng vấn kèm đáp án mẫu.

### 💻 Mọi LAB chạy miễn phí trên máy bạn

Không bắt buộc tài khoản cloud, không cần thẻ tín dụng:

| Cần gì | Dùng gì |
|---|---|
| Máy chủ Linux | **Multipass** (dùng chính cloud-init như AWS/GCP) |
| Dịch vụ AWS | **LocalStack** (cùng lệnh `aws` CLI, chỉ đổi endpoint) |
| Kubernetes | **minikube** |
| CI/CD | **GitHub Actions** (runner miễn phí) + self-hosted runner trên máy bạn |
| Giám sát | **Docker Compose** (Prometheus, Grafana, Loki, Alertmanager) |
| Kho lưu Terraform state | **MinIO** (tương thích S3) |

Mỗi bài đều kèm cách làm **trên cloud thật** khi bạn đã sẵn sàng — cùng khái niệm, chỉ khác endpoint.

Mỗi giai đoạn kết thúc bằng **LAB Final (Milestone)** + **Phụ lục** (lỗi thường gặp, playbook xử lý sự cố, cheat sheet).

> 🖼️ **Sơ đồ:** các bài LAB/Milestone quan trọng có sơ đồ kiến trúc vẽ bằng **Mermaid** — GitHub tự render thành hình đồ họa (mở file `.md` trên GitHub để xem). Tổng cộng 18 sơ đồ: SSH bastion, Git states, Container vs VM, pipeline CI/CD, kiến trúc K8s, Service/Ingress, GitOps, observability, SLO/error budget, HA/DR, sidecar mesh, và sơ đồ dự án tốt nghiệp.

---

*Tài liệu được biên soạn và mở rộng để bám sát thực tế vận hành hệ thống.*
