# 🧩 Module nâng cao bổ sung — Lấp lỗ hổng so với roadmap chuẩn

> Module này bổ sung các chủ đề mà lộ trình 60 ngày mới **nhắc tên nhưng chưa có lab thực hành đầy đủ**, để bộ kỹ năng của bạn trọn vẹn theo chuẩn ngành (roadmap.sh/devops + CNCF).
>
> **Học khi nào:** sau khi xong Giai đoạn 3 (Ngày 50) — vì các chủ đề này dựa trên K8s + observability + CI/CD. Không bắt buộc theo thứ tự; chọn cái bạn cần trước.
>
> **Cùng khuôn mỗi ngày như 60 ngày chính:** 📘 Lý thuyết sâu → 📖 Hiểu rõ hơn → 🧪 Lab cơ bản (file đầy đủ) → 🚀 Lab nâng cao → 💡 Bổ sung thực tế → 🧭 Hướng dẫn step-by-step (có checkpoint) → 🐛 Gỡ lỗi → 📝 Quiz → 📚 Thuật ngữ.
>
> ✅ **Trung lập nền tảng · Linux-first** — như toàn bộ khóa học.

---

## Mục lục

| Bài | Chủ đề | Lấp lỗ hổng |
|---|---|---|
| [NC1](#nc1--distributed-tracing-opentelemetry--jaeger) | Distributed Tracing (OpenTelemetry + Jaeger) | Trụ cột observability thứ 3 (Traces) — trước chỉ có Metrics + Logs |
| [NC2](#nc2--quản-lý-secret-với-hashicorp-vault) | Quản lý secret với HashiCorp Vault | Vault chỉ được nhắc, chưa có lab |
| [NC3](#nc3--message-queue-kafka--rabbitmq) | Message Queue (Kafka & RabbitMQ) | Kiến trúc bất đồng bộ — trước chỉ có Redis |
| [NC4](#nc4--managed-kubernetes-cert-manager--serverless) | Managed K8s (EKS/GKE) + cert-manager + Serverless | Cloud-native production sâu hơn |

---

## NC1 — Distributed Tracing (OpenTelemetry + Jaeger)

> ⏱️ ~90 phút · Loại: Observability
>
> 🧭 **Bạn đang ở đâu:** Ngày 44–46 (Metrics + Logs) → **NC1 (Traces — trụ cột observability thứ 3)** → NC2 (Vault). Metric báo *"có sự cố"*, Log cho biết *"lỗi gì"*, còn **Trace chỉ *"lỗi CHỖ NÀO trong chuỗi service"*** — mảnh còn thiếu.
>
> ✅ **Chuẩn bị:** đã có Grafana/Prometheus (Ngày 44–45). Docker/Compose hoặc cluster K8s để chạy Jaeger/Tempo. Một app nhiều service để tạo trace (dùng app capstone càng tốt).

### 📘 Lý thuyết

#### 1. Vì sao cần Tracing — vấn đề của microservice

1 request người dùng có thể đi qua 5–10 service (gateway → auth → order → payment → db...). Khi nó **chậm hoặc lỗi**, metric chỉ nói "chậm", log rải rác từng service. Câu hỏi *"nghẽn ở service nào, bước nào?"* → chỉ **trace** trả lời được.

#### 2. Trace, Span & Context propagation

| Khái niệm | Là gì |
|---|---|
| **Trace** | Hành trình đầy đủ của 1 request qua các service (1 cây) |
| **Span** | 1 công đoạn trong trace (vd "gọi DB", "xử lý payment") — có thời gian bắt đầu/kết thúc |
| **Trace ID** | Mã định danh chung, đi kèm request qua mọi service |
| **Context propagation** | Truyền Trace ID qua header (`traceparent`) giữa các service để "nối" các span |

Một trace = 1 cây span; nhìn cây là thấy ngay span nào ngốn thời gian.

#### 3. OpenTelemetry (OTel) — chuẩn chung

**OpenTelemetry** là chuẩn CNCF để *tạo & thu thập* telemetry (traces, metrics, logs) — không khoá vào 1 nhà cung cấp. Gồm:
- **SDK/instrumentation**: nhúng vào app để sinh span (nhiều ngôn ngữ có *auto-instrumentation* — gần như không sửa code).
- **OTel Collector**: nhận telemetry, xử lý, đẩy tới backend (Jaeger/Tempo/...).

#### 4. Backend hiển thị trace

| Backend | Đặc điểm |
|---|---|
| **Jaeger** | Phổ biến, UI xem trace tốt, dễ bắt đầu |
| **Grafana Tempo** | Nhẹ, hợp khi đã dùng Grafana (xem trace cạnh metric/log) |
| **Zipkin** | Lâu đời, đơn giản |

#### 5. Ba trụ cột nối lại

Cho `trace_id` vào **log** (Ngày 46) → từ 1 trace nhảy sang log đúng request; từ metric bất thường → nhảy sang trace. Đây là "observability đúng nghĩa": metric → trace → log liên thông.

> 🔑 Đừng trace 100% request ở production (tốn lưu trữ) — dùng **sampling** (vd giữ 10%, hoặc "tail sampling" giữ mọi trace lỗi/chậm). OpenTelemetry là chuẩn nên chọn — tránh khoá vào 1 vendor.

### 📖 Hiểu rõ hơn (giải thích cho người mới)

**Trace là gì — ví như bưu kiện có mã vận đơn.**
Hình dung request là 1 kiện hàng. Nó đi qua nhiều kho (service). **Trace ID** như mã vận đơn dán trên kiện — mỗi kho quét mã, ghi "nhận lúc X, gửi đi lúc Y" (1 **span**). Cuối cùng ghép lại: kiện đi mất tổng 3 giây, trong đó **nằm ở kho payment 2,8 giây** → biết ngay nghẽn ở đâu. Không có trace, bạn chỉ biết "giao hàng chậm" mà không biết kho nào.

**OpenTelemetry — vì sao là "chuẩn" quan trọng.**
Ngày xưa mỗi hãng (Jaeger, Datadog...) có cách nhúng riêng → đổi backend là viết lại. OTel thống nhất: bạn nhúng OTel **một lần**, muốn đổi từ Jaeger sang Tempo/Datadog chỉ đổi cấu hình Collector. Đây là lý do CNCF đẩy mạnh OTel.

**Auto-instrumentation — phép màu ít-sửa-code.**
Nhiều ngôn ngữ (Java, Python, Node, Go) có agent OTel tự động sinh span cho HTTP/DB call phổ biến mà **gần như không sửa code app**. Bắt đầu từ đây, sau đó thêm span thủ công cho phần nghiệp vụ quan trọng.

> 🧠 **Một câu để nhớ:** 3 trụ cột trả lời 3 câu khác nhau — **Metric: "có sai không?"** · **Log: "sai cái gì?"** · **Trace: "sai/chậm ở ĐÂU trong chuỗi service?"**. Thiếu trace = mù ở microservice.

### 🧪 Lab cơ bản

> Mục tiêu: chạy Jaeger, cho một app sinh trace, và xem cây span trên UI. File đầy đủ, copy-chạy được.

**Bước 1 — Chạy Jaeger all-in-one bằng Docker.**
```bash
docker run -d --name jaeger \
  -p 16686:16686 \
  -p 4318:4318 \
  jaegertracing/all-in-one:latest
```
Mở `http://localhost:16686` → thấy UI Jaeger (chưa có trace nào).

**Bước 2 — App Node tự sinh trace (auto-instrumentation).** Tạo thư mục, 3 file:

`package.json`:
```json
{ "name": "otel-demo", "version": "1.0.0", "main": "app.js" }
```
`app.js`:
```javascript
const http = require('http');
http.createServer(async (req, res) => {
  // giả lập gọi 1 "service" khác để tạo span con
  await fetch('https://api.github.com').catch(() => {});
  res.end('Hello Tracing');
}).listen(3000, () => console.log('cổng 3000'));
```

**Bước 3 — Cài OTel và chạy với auto-instrumentation.**
```bash
npm install @opentelemetry/api @opentelemetry/auto-instrumentations-node
export OTEL_TRACES_EXPORTER=otlp
export OTEL_EXPORTER_OTLP_ENDPOINT=http://localhost:4318
export OTEL_SERVICE_NAME=otel-demo
node --require @opentelemetry/auto-instrumentations-node/register app.js
```

**Bước 4 — Tạo request để sinh trace.**
```bash
curl localhost:3000        # gọi vài lần
```

**Bước 5 — Xem trace trên Jaeger.** Về UI `http://localhost:16686` → chọn Service `otel-demo` → **Find Traces**. Bạn sẽ thấy trace với các span (HTTP server → fetch ra ngoài), kèm thời gian từng span.

### 🚀 Lab nâng cao (best-practice)

> Mục tiêu: dựng luồng chuẩn production — OTel Collector ở giữa, sampling, và nối trace ↔ log.

1. **OTel Collector làm điểm gom** (thay vì app đẩy thẳng vào backend):
   ```yaml
   # otel-collector-config.yaml
   receivers:
     otlp: { protocols: { http: {}, grpc: {} } }
   processors:
     batch: {}
     tail_sampling:            # giữ MỌI trace lỗi/chậm, sample phần còn lại
       policies:
         - { name: errors, type: status_code, status_code: { status_codes: [ERROR] } }
         - { name: slow, type: latency, latency: { threshold_ms: 1000 } }
   exporters:
     otlp/jaeger: { endpoint: jaeger:4317, tls: { insecure: true } }
   service:
     pipelines:
       traces: { receivers: [otlp], processors: [batch, tail_sampling], exporters: [otlp/jaeger] }
   ```
   → App chỉ biết Collector; đổi backend không đụng app.
2. **Nối trace ↔ log:** in `trace_id` vào mỗi dòng log JSON → trên Grafana/Loki, từ 1 trace nhảy thẳng sang log đúng request đó.
3. **Span thủ công cho nghiệp vụ:** thêm span quanh đoạn code quan trọng (vd "tính tồn kho") để đo riêng.
4. **Grafana Tempo** thay Jaeger nếu đã dùng Grafana — xem trace cạnh metric/log trong 1 giao diện (correlation liền mạch).

### 💡 Bổ sung thực tế: sampling & khi nào cần trace

- **Sampling là bắt buộc ở quy mô lớn:** trace mọi request = bùng nổ dữ liệu. 2 chiến lược: **head sampling** (quyết ngay đầu, vd giữ 10%) — đơn giản nhưng có thể bỏ lỡ trace lỗi; **tail sampling** (quyết sau khi trace xong) — giữ *mọi* trace lỗi/chậm + sample phần bình thường — tốt hơn nhưng tốn tài nguyên Collector.
- **Context propagation là mấu chốt:** trace "gãy" (mỗi service 1 trace rời) thường do **không truyền header `traceparent`**. Auto-instrumentation lo phần này cho HTTP/gRPC phổ biến; gọi qua queue (Kafka) cần truyền context thủ công.
- **Đừng nhầm 3 trụ cột:** nhiều người đổ hết vào log rồi cố grep tìm request chậm — rất khổ. Trace sinh ra đúng cho việc đó. Metric để alert, log để chi tiết, trace để định vị.
- **OTel là tương lai:** metric + log của OTel đang trưởng thành dần — xu hướng là **1 SDK (OTel) cho cả 3 trụ cột**, đẩy qua 1 Collector tới backend tuỳ chọn.

### 🧭 Hướng dẫn làm lab & giải nghĩa lệnh (cho người tự học)

> Làm tuần tự, dừng ở mỗi ✅ **Checkpoint**.

**Bước 1 — Chạy Jaeger và mở UI.**
```bash
docker run -d --name jaeger -p 16686:16686 -p 4318:4318 jaegertracing/all-in-one:latest
```
✅ **Checkpoint:** mở `localhost:16686` thấy UI Jaeger.
💡 Cổng `16686` = UI; `4318` = nơi nhận telemetry OTLP/HTTP từ app.

**Bước 2 — Chạy app với OTel auto-instrumentation.**
```bash
OTEL_EXPORTER_OTLP_ENDPOINT=http://localhost:4318 OTEL_SERVICE_NAME=otel-demo \
  node --require @opentelemetry/auto-instrumentations-node/register app.js
```
✅ **Checkpoint:** app chạy, log "cổng 3000".
💡 `--require .../register` nhồi OTel vào *trước* khi app chạy → tự sinh span cho HTTP/fetch mà không sửa code.

**Bước 3 — Sinh trace và xem cây span.**
```bash
curl localhost:3000
```
✅ **Checkpoint:** Jaeger UI (Service `otel-demo` → Find Traces) hiện trace có ≥2 span (server + call ngoài), thấy thời gian từng span.
💡 Nhìn span dài nhất = biết chỗ nghẽn.

**Bước 4 — (Nâng cao) đặt sampling.**
```bash
export OTEL_TRACES_SAMPLER=parentbased_traceidratio
export OTEL_TRACES_SAMPLER_ARG=0.1     # giữ 10%
```
✅ **Checkpoint:** chỉ ~1/10 request tạo trace — hiểu cơ chế tiết kiệm ở production.

### 🐛 Gỡ lỗi nhanh

| Triệu chứng | Nguyên nhân | Cách sửa |
|---|---|---|
| Jaeger UI không có trace | App chưa đẩy được / sai endpoint | Đúng `OTEL_EXPORTER_OTLP_ENDPOINT` (cổng 4318 http); kiểm app log |
| Trace "gãy" (mỗi service 1 trace) | Không truyền `traceparent` | Bật propagation; auto-instrumentation cho HTTP; qua queue phải truyền thủ công |
| Quá nhiều trace, tốn đĩa | Trace 100% | Bật sampling (head 10% hoặc tail giữ lỗi/chậm) |
| Span thiếu thông tin nghiệp vụ | Chỉ có auto-instrumentation | Thêm span thủ công + attribute (user_id, order_id) |
| `connection refused` tới collector | Collector/Jaeger chưa chạy | Kiểm container; đúng service name trong cùng network |

### 📝 Bài ôn tập & Demo đối chiếu

**✍️ Tự kiểm tra:**

<details>
<summary>1. Trace, Span, Trace ID khác nhau thế nào?</summary>

> Trace = hành trình đầy đủ 1 request qua các service. Span = 1 công đoạn trong trace (có thời gian). Trace ID = mã chung nối mọi span của cùng request.
</details>

<details>
<summary>2. 3 trụ cột observability trả lời câu hỏi gì?</summary>

> Metric: "có sai không?". Log: "sai cái gì?". Trace: "sai/chậm ở đâu trong chuỗi service?".
</details>

<details>
<summary>3. Vì sao dùng OpenTelemetry thay vì SDK riêng của Jaeger/Datadog?</summary>

> OTel là chuẩn chung — nhúng 1 lần, đổi backend chỉ đổi cấu hình Collector, không khoá vào 1 vendor.
</details>

<details>
<summary>4. Vì sao cần sampling? head vs tail?</summary>

> Trace mọi request tốn lưu trữ khổng lồ. Head sampling quyết ngay đầu (đơn giản, có thể bỏ lỡ lỗi). Tail sampling quyết sau khi trace xong → giữ mọi trace lỗi/chậm (tốt hơn, tốn Collector).
</details>

**🔬 Demo đối chiếu:**

| Demo đối chiếu | Kết quả mong đợi |
|---|---|
| Chạy Jaeger | UI mở ở `localhost:16686` |
| App sinh trace | Service xuất hiện trong Jaeger, có trace |
| Xem cây span | Thấy span nào ngốn thời gian nhất |

### 📚 Thuật ngữ Anh–Việt (bài này)

| Thuật ngữ | Nghĩa |
|---|---|
| **Trace** | Hành trình đầy đủ của 1 request |
| **Span** | 1 công đoạn trong trace |
| **Trace ID** | Mã định danh nối các span |
| **Context propagation** | Truyền trace context qua header |
| **OpenTelemetry (OTel)** | Chuẩn CNCF tạo/thu telemetry |
| **Collector** | Bộ gom & đẩy telemetry tới backend |
| **Sampling** | Chỉ giữ 1 phần trace (tiết kiệm) |

✅ **Kết quả đạt được:** Hiểu & dựng được distributed tracing (OTel + Jaeger), đọc cây span để định vị nghẽn — hoàn thiện trụ cột thứ 3 của observability.

---

## NC2 — Quản lý secret với HashiCorp Vault

> ⏱️ ~90 phút · Loại: Security
>
> 🧭 **Bạn đang ở đâu:** Ngày 39 (K8s Secret — chỉ base64) & Ngày 49 (DevSecOps) → **NC2 (Vault — quản secret ĐÚNG chuẩn production)**. Đây là lab cho thứ trước đó chỉ được "nhắc tên".
>
> ✅ **Chuẩn bị:** Docker (chạy Vault dev). Ôn lại "K8s Secret chỉ base64, không phải mã hoá" (Ngày 39).

### 📘 Lý thuyết

#### 1. Vì sao K8s Secret / `.env` chưa đủ

- **K8s Secret** chỉ **base64** (`base64 -d` là ra plaintext) — ai đọc được Secret là đọc được mật khẩu.
- **`.env`** tiện cho lab nhưng dễ lộ, không xoay vòng, không phân quyền chi tiết, không audit.

Production cần: **mã hoá thật + phân quyền + audit + xoay vòng tự động + secret động**.

#### 2. Vault là gì

**HashiCorp Vault** = kho secret tập trung, mã hoá, có kiểm soát truy cập chặt. Chức năng chính:

| Chức năng | Ý nghĩa |
|---|---|
| **Secret tĩnh (KV)** | Lưu mật khẩu/API key mã hoá, cấp theo policy |
| **Secret động** | Tạo credential DB **tạm thời**, hết hạn tự thu hồi |
| **Encryption as a Service** | App gửi dữ liệu, Vault mã hoá/giải mã (không lộ khoá) |
| **Audit log** | Ghi lại ai đọc secret nào, lúc nào |

#### 3. Seal / Unseal & Token

- Vault khởi động ở trạng thái **sealed** (niêm phong) — dữ liệu mã hoá, không dùng được. Phải **unseal** bằng các "unseal key" (chia nhiều mảnh — Shamir) mới mở.
- Truy cập bằng **token**; token gắn với **policy** (quyền tối thiểu: chỉ đọc đúng path cần).

#### 4. Auth methods — cách app/người chứng minh danh tính

Vault không chỉ dùng token tĩnh. Có nhiều cách xác thực: **AppRole** (cho app/CI), **Kubernetes auth** (pod tự xác thực bằng service account), **cloud IAM**, OIDC (cho người). → app lấy secret mà không cần "secret để lấy secret" cứng.

#### 5. Secret động — điểm ăn tiền nhất

Thay vì 1 mật khẩu DB cố định (lộ là toang), Vault tạo **user DB tạm** mỗi lần app cần, **TTL ngắn** (vd 1 giờ) rồi tự xoá. Lộ credential → hết hạn ngay, thiệt hại tối thiểu.

> 🔑 Trong K8s, đừng nhồi secret cứng vào manifest — dùng **Vault + External Secrets Operator** (đồng bộ từ Vault vào K8s Secret) hoặc **Vault Agent Injector** (tiêm secret vào pod lúc chạy). Bật **audit log** để biết ai đọc gì.

### 📖 Hiểu rõ hơn (giải thích cho người mới)

**Vault như két sắt ngân hàng, không phải ngăn kéo có khoá.**
`.env`/K8s Secret giống ngăn kéo khoá tạm — ai có chìa (quyền đọc) là lấy hết, không ai biết. Vault là **két ngân hàng**: mã hoá thật, mỗi người chỉ mở được ô của mình (policy), có camera ghi lại (audit), và có thể phát "chìa dùng 1 lần rồi vứt" (secret động).

**Secret động — vì sao là bước nhảy tư duy.**
Bí mật lớn nhất về bảo mật: *secret sống lâu là secret nguy hiểm*. Mật khẩu DB cố định 3 năm — lộ lúc nào không biết. Vault lật ngược: mỗi lần app cần, cấp 1 credential **sống 1 giờ**. Kẻ trộm có lấy được cũng vô dụng sau 1 giờ. Đây là điều `.env` không bao giờ làm được.

**Seal/Unseal — vì sao Vault "tự khoá".**
Khi restart, Vault niêm phong lại — kể cả admin cũng không đọc được cho tới khi có đủ mảnh unseal key (chia cho nhiều người giữ). Ý nghĩa: **không một cá nhân nào** tự mở được kho — cần nhiều người phối hợp. (Production dùng auto-unseal qua cloud KMS.)

> 🧠 **Một câu để nhớ:** nguyên tắc vàng — *secret không bao giờ nằm plaintext trong code/log/image/env lộ ra `ps`*. Vault + secret động biến "quản lý mật khẩu" thành "quản lý quyền truy cập tạm thời".

### 🧪 Lab cơ bản

> Mục tiêu: chạy Vault dev, ghi/đọc secret, và hiểu policy. (Chế độ dev đã unseal sẵn — chỉ để học.)

**Bước 1 — Chạy Vault dev bằng Docker.**
```bash
docker run -d --name vault --cap-add=IPC_LOCK \
  -e VAULT_DEV_ROOT_TOKEN_ID=root \
  -p 8200:8200 hashicorp/vault:latest
```
Mở `http://localhost:8200` (UI) — đăng nhập token `root`.

**Bước 2 — Cấu hình CLI trỏ tới Vault.**
```bash
export VAULT_ADDR=http://localhost:8200
export VAULT_TOKEN=root
docker exec -e VAULT_ADDR=http://localhost:8200 -e VAULT_TOKEN=root vault vault status
```
Bạn sẽ thấy `Sealed  false` (dev mode đã mở sẵn).

**Bước 3 — Ghi & đọc secret (KV).**
```bash
alias v='docker exec -e VAULT_ADDR=http://localhost:8200 -e VAULT_TOKEN=root vault vault'
v kv put secret/myapp db_pass=SieuBiMat123 api_key=abc
v kv get secret/myapp
```
Bạn sẽ thấy `db_pass` và `api_key` in ra (vì bạn có quyền root).

**Bước 4 — Tạo policy quyền tối thiểu.**
```bash
docker exec -i -e VAULT_ADDR=http://localhost:8200 -e VAULT_TOKEN=root vault \
  sh -c 'echo "path \"secret/data/myapp\" { capabilities = [\"read\"] }" | vault policy write app-ro -'
v token create -policy=app-ro -ttl=1h
```
Token mới chỉ **đọc** được `secret/myapp`, hết hạn sau 1h.

**Bước 5 — Kiểm chứng phân quyền.**
```bash
APPTOKEN=<token vừa tạo>
docker exec -e VAULT_ADDR=http://localhost:8200 -e VAULT_TOKEN=$APPTOKEN vault \
  vault kv get secret/myapp        # đọc được
# thử ghi → bị từ chối (permission denied) vì policy chỉ read
```

### 🚀 Lab nâng cao (best-practice)

> Mục tiêu: dùng Vault như production — secret động cho DB + tích hợp K8s.

1. **Secret động cho database** — Vault tự tạo user DB tạm, TTL ngắn:
   ```bash
   v secrets enable database
   # cấu hình connection tới Postgres + role tạo user TTL=1h
   v read database/creds/my-role     # mỗi lần đọc → 1 user DB MỚI, hết hạn tự thu hồi
   ```
2. **Kubernetes auth + External Secrets Operator** — pod dùng service account xác thực với Vault, ESO đồng bộ secret vào K8s Secret tự động (không nhồi secret cứng vào manifest).
3. **Vault Agent Injector** — annotation trên pod → sidecar tự tiêm secret vào file trong pod lúc chạy, tự làm mới khi xoay vòng.
4. **Bật audit log** — `vault audit enable file file_path=/vault/logs/audit.log` → mọi truy cập secret đều được ghi.

### 💡 Bổ sung thực tế: secret động & "secret zero"

- **Secret động là siêu năng lực của Vault:** DB, cloud IAM, chứng chỉ — Vault cấp credential tạm, hết hạn tự thu hồi. Không còn "mật khẩu DB 3 năm không đổi ai cũng biết". Lộ = vô hại sau TTL.
- **Bài toán "secret zero" (chicken-and-egg):** để lấy secret từ Vault, app cần... 1 secret để xác thực Vault. Giải bằng danh tính *có sẵn*: **Kubernetes auth** (service account của pod), **cloud IAM** (IAM role của máy), **AppRole** (role-id + secret-id cấp qua CI). → không có "secret cứng" nào phải nhúng.
- **Vault không phải lựa chọn duy nhất:** cloud có sẵn **AWS Secrets Manager / GCP Secret Manager / Azure Key Vault** — đơn giản hơn Vault, tích hợp IAM sẵn. Vault mạnh khi multi-cloud/on-prem + cần secret động phức tạp. Với 1 cloud → dùng secret manager của cloud đó có khi đủ.
- **Đừng quên vận hành Vault:** Vault tự nó là hệ thống quan trọng (mất Vault = app mất secret). Cần HA, backup, auto-unseal (KMS), giám sát. Đây là lý do nhiều team nhỏ chọn managed secret manager.

### 🧭 Hướng dẫn làm lab & giải nghĩa lệnh (cho người tự học)

> Làm tuần tự, dừng ở mỗi ✅ **Checkpoint**.

**Bước 1 — Chạy Vault dev & kiểm tra.**
```bash
docker run -d --name vault --cap-add=IPC_LOCK -e VAULT_DEV_ROOT_TOKEN_ID=root -p 8200:8200 hashicorp/vault:latest
export VAULT_ADDR=http://localhost:8200 VAULT_TOKEN=root
```
✅ **Checkpoint:** UI `localhost:8200` đăng nhập bằng token `root`; `vault status` → `Sealed false`.
💡 Dev mode đã unseal sẵn cho tiện học; production KHÔNG như vậy (phải unseal).

**Bước 2 — Ghi/đọc secret.**
```bash
v kv put secret/myapp db_pass=x && v kv get secret/myapp
```
✅ **Checkpoint:** đọc lại đúng giá trị vừa ghi.

**Bước 3 — Policy quyền tối thiểu.**
✅ **Checkpoint:** token `app-ro` đọc được nhưng **ghi bị từ chối**.
💡 Đây là điểm hơn hẳn `.env`: phân quyền chi tiết theo path + audit ai đọc gì.

**Bước 4 — (Nâng cao) secret động.**
✅ **Checkpoint:** mỗi lần `vault read database/creds/...` ra 1 user DB **khác nhau**, có TTL.
💡 Lộ credential → hết hạn ngay, thiệt hại tối thiểu — đây là giá trị lớn nhất.

### 🐛 Gỡ lỗi nhanh

| Triệu chứng | Nguyên nhân | Cách sửa |
|---|---|---|
| `Vault is sealed` | Vault vừa restart (production) | Unseal bằng đủ mảnh unseal key; production dùng auto-unseal KMS |
| `permission denied` khi đọc secret | Token thiếu policy / sai path | Kiểm policy; nhớ KV v2 path là `secret/data/...` trong policy |
| App không lấy được secret | "Secret zero" / auth sai | Dùng K8s auth / AppRole thay vì token cứng |
| Secret vẫn lộ trong log | App in secret ra | Sửa app; bật audit để phát hiện; xoay secret |
| Mất Vault = app chết | Vault chưa HA/backup | Chạy HA + backup; hoặc dùng managed secret manager |

### 📝 Bài ôn tập & Demo đối chiếu

**✍️ Tự kiểm tra:**

<details>
<summary>1. Vì sao K8s Secret chưa đủ cho production?</summary>

> Nó chỉ base64 (không mã hoá thật), thiếu phân quyền chi tiết, audit, xoay vòng, secret động. Cần Vault/secret manager + RBAC + encryption-at-rest.
</details>

<details>
<summary>2. Secret động là gì và lợi ích?</summary>

> Vault cấp credential (vd user DB) tạm thời, TTL ngắn, tự thu hồi. Lộ ra cũng vô hại sau TTL — an toàn hơn secret cố định.
</details>

<details>
<summary>3. "Secret zero" là gì, giải quyết thế nào?</summary>

> Bài toán con-gà-quả-trứng: cần secret để lấy secret. Giải bằng danh tính có sẵn: K8s service account, cloud IAM, AppRole — không nhúng secret cứng.
</details>

<details>
<summary>4. Khi nào dùng cloud secret manager thay Vault?</summary>

> Khi chỉ dùng 1 cloud và nhu cầu không quá phức tạp — AWS/GCP/Azure secret manager đơn giản hơn, tích hợp IAM sẵn, khỏi tự vận hành Vault.
</details>

**🔬 Demo đối chiếu:**

| Demo đối chiếu | Kết quả mong đợi |
|---|---|
| Chạy Vault | `vault status` → Sealed false (dev) |
| Ghi/đọc secret | `kv get` trả đúng giá trị |
| Policy read-only | Đọc OK, ghi bị `permission denied` |

### 📚 Thuật ngữ Anh–Việt (bài này)

| Thuật ngữ | Nghĩa |
|---|---|
| **Vault** | Kho secret tập trung, mã hoá |
| **Seal / Unseal** | Niêm phong / mở kho |
| **Policy** | Quy tắc quyền truy cập secret |
| **Dynamic secret** | Credential tạm, tự hết hạn |
| **Auth method** | Cách xác thực (AppRole, K8s, IAM) |
| **Audit log** | Nhật ký ai đọc secret nào |
| **External Secrets Operator** | Đồng bộ secret từ Vault vào K8s |

✅ **Kết quả đạt được:** Quản lý secret đúng chuẩn production với Vault — policy, secret động, audit; hiểu khi nào dùng cloud secret manager.

---

## NC3 — Message Queue (Kafka & RabbitMQ)

> ⏱️ ~90 phút · Loại: Kiến trúc
>
> 🧭 **Bạn đang ở đâu:** Ngày 24 (Redis làm hàng đợi đơn giản) → **NC3 (message queue chuyên dụng: Kafka & RabbitMQ)**. Đây là mảnh kiến trúc bất đồng bộ (async) mà hệ thống thật hầu như đều có.
>
> ✅ **Chuẩn bị:** Docker/Compose. Hiểu client-server & container networking (Ngày 19).

### 📘 Lý thuyết

#### 1. Vấn đề: giao tiếp đồng bộ dễ "domino"

Nếu service A gọi thẳng service B (đồng bộ) và B chậm/chết → A cũng kẹt/chết → dây chuyền sập. Với tác vụ không cần trả lời ngay (gửi email, xử lý ảnh, ghi log), nên **tách rời (decouple)** qua **hàng đợi**.

#### 2. Message Queue giải quyết gì

| Lợi ích | Ý nghĩa |
|---|---|
| **Decoupling** | A gửi message rồi đi tiếp; B xử lý khi rảnh — A không phụ thuộc B |
| **Buffering** | Tải tăng đột biến → message xếp hàng, không làm sập B |
| **Resilience** | B chết → message còn trong queue, B sống lại xử lý tiếp (không mất) |
| **Scaling** | Nhiều consumer cùng rút message → xử lý song song |

#### 3. Hai mô hình & hai công cụ

| | **RabbitMQ** (message broker) | **Kafka** (event streaming) |
|---|---|---|
| Mô hình | Queue: message được **tiêu thụ rồi biến mất** | Log: event **được giữ lại**, nhiều consumer đọc lại |
| Hợp cho | Hàng đợi tác vụ (task queue), routing linh hoạt | Luồng sự kiện lớn, log, analytics, event sourcing |
| Ví như | Bưu điện chia thư tới đúng hộp | Sổ nhật ký ai cũng đọc lại từ đầu được |

#### 4. Khái niệm cốt lõi

- **RabbitMQ**: Producer → **Exchange** (định tuyến) → **Queue** → Consumer. Message **ack** (xác nhận đã xử lý) thì mới bị xoá.
- **Kafka**: Producer → **Topic** (chia **partition**) → Consumer **Group**. Mỗi consumer đọc theo **offset** (vị trí đã đọc); event giữ lại theo retention.

#### 5. Đảm bảo giao nhận

- **At-least-once** (phổ biến): message giao ít nhất 1 lần → consumer phải xử lý **idempotent** (xử lý trùng không sao).
- **At-most-once / Exactly-once**: đánh đổi phức tạp/hiệu năng. Đa số hệ thống chọn at-least-once + idempotent.

> 🔑 Chọn công cụ theo nhu cầu: **RabbitMQ** cho task queue truyền thống (đơn giản, routing mạnh); **Kafka** cho luồng sự kiện khối lượng lớn / cần đọc lại. Đừng dùng Kafka cho mọi thứ — nó phức tạp để vận hành.

### 📖 Hiểu rõ hơn (giải thích cho người mới)

**Message queue như "phiếu gọi món" ở quán ăn.**
Khách (producer) gọi món, ghi phiếu bỏ vào kẹp (queue) rồi đi ngồi — **không đứng chờ bếp**. Bếp (consumer) lấy phiếu xử lý khi rảnh. Đông khách → phiếu xếp hàng, bếp làm dần. Bếp nghỉ tay 5 phút → phiếu vẫn còn đó, không mất. Đây là **bất đồng bộ**: khách và bếp không phải chờ nhau.

**RabbitMQ vs Kafka — hai triết lý khác nhau.**
- **RabbitMQ** = kẹp phiếu: bếp lấy phiếu xong thì phiếu **bỏ đi** (message tiêu thụ là mất). Hợp cho "làm việc này 1 lần".
- **Kafka** = cuốn sổ nhật ký: mọi sự kiện **ghi vào sổ, giữ lại**. Nhiều bộ phận (consumer group) đọc cùng cuốn sổ theo tốc độ riêng, đọc lại từ đầu được. Hợp cho "nhiều nơi cùng quan tâm 1 luồng sự kiện" (vd 1 đơn hàng → kho, kế toán, email cùng xử lý).

**Idempotent — vì sao quan trọng với queue.**
Queue thường hứa "giao ít nhất 1 lần" → đôi khi giao **trùng**. Nếu consumer "trừ tiền" mà xử lý trùng → trừ 2 lần! Giải: thiết kế xử lý **idempotent** (kiểm tra "đã xử lý message này chưa" bằng ID) → chạy trùng vẫn đúng.

> 🧠 **Một câu để nhớ:** message queue = **tách rời + đệm + không mất việc**. Nhưng nó thêm 1 thành phần phải vận hành (broker) — chỉ dùng khi thật sự cần bất đồng bộ, đừng thêm cho "sang".

### 🧪 Lab cơ bản

> Mục tiêu: chạy RabbitMQ, gửi/nhận message, thấy UI. (RabbitMQ dễ bắt đầu hơn Kafka.)

**Bước 1 — Chạy RabbitMQ (có UI quản trị).**
```bash
docker run -d --name rabbit -p 5672:5672 -p 15672:15672 rabbitmq:3-management
```
Mở `http://localhost:15672` (user/pass mặc định: `guest`/`guest`) → UI quản trị.

**Bước 2 — Producer gửi message** (`send.py`):
```python
import pika
conn = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
ch = conn.channel()
ch.queue_declare(queue='tasks', durable=True)
ch.basic_publish(exchange='', routing_key='tasks', body='Xu ly anh #1')
print("Đã gửi"); conn.close()
```

**Bước 3 — Consumer nhận message** (`worker.py`):
```python
import pika
conn = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
ch = conn.channel()
ch.queue_declare(queue='tasks', durable=True)
def cb(ch, method, props, body):
    print("Nhận:", body.decode())
    ch.basic_ack(delivery_tag=method.delivery_tag)   # ack sau khi xử lý xong
ch.basic_consume(queue='tasks', on_message_callback=cb)
print("Đang chờ..."); ch.start_consuming()
```

**Bước 4 — Chạy thử.**
```bash
pip install pika
python worker.py &     # consumer chờ sẵn
python send.py         # gửi → worker in "Nhận: Xu ly anh #1"
```

**Bước 5 — Quan sát trên UI.** Vào tab **Queues** → thấy queue `tasks`, số message vào/ra. Dừng worker rồi `send.py` nhiều lần → thấy message **xếp hàng** (chưa bị tiêu thụ).

### 🚀 Lab nâng cao (best-practice)

> Mục tiêu: hiểu bền vững, ack, và khi nào cần Kafka.

1. **Durability + ack đúng cách** — queue `durable=True` + message `persistent` + `basic_ack` **sau khi xử lý xong** → broker chết hay worker chết, message không mất.
2. **Nhiều consumer song song** — chạy 2–3 `worker.py` → RabbitMQ chia message (round-robin) → xử lý song song, scale bằng cách thêm worker.
3. **Dead Letter Queue (DLQ)** — message xử lý lỗi nhiều lần → chuyển sang queue "chết" để điều tra, không kẹt queue chính.
4. **Kafka khi cần streaming** — chạy Kafka (KRaft mode), tạo topic có nhiều **partition**, nhiều consumer group đọc **cùng** luồng độc lập:
   ```bash
   docker run -d --name kafka -p 9092:9092 apache/kafka:latest
   # tạo topic, producer/consumer bằng kafka client — nhiều group đọc lại cùng event
   ```

### 💡 Bổ sung thực tế: chọn Kafka hay RabbitMQ & bẫy thường gặp

- **Quy tắc chọn nhanh:**
  | Nhu cầu | Chọn |
  |---|---|
  | Task queue (gửi email, xử lý ảnh, job nền) | **RabbitMQ** (hoặc Redis/SQS cho đơn giản) |
  | Luồng sự kiện lớn, nhiều consumer đọc lại, analytics, log | **Kafka** |
  | Chỉ cần đơn giản, đã có Redis | Redis Streams / list (Ngày 24) |
  | Trên cloud, ngại vận hành | Managed: **SQS/SNS** (AWS), **Pub/Sub** (GCP) |
- **Idempotent consumer là bắt buộc:** hầu hết queue giao "at-least-once" → có lúc trùng. Consumer phải chịu được xử lý trùng (lưu ID đã xử lý). Bỏ qua điều này = bug tài chính/dữ liệu kinh điển.
- **Kafka mạnh nhưng nặng vận hành:** partition, consumer group, offset, retention... nhiều khái niệm. Đừng chọn Kafka chỉ vì "nghe ngầu" — với task queue đơn giản, RabbitMQ/SQS gọn hơn nhiều.
- **Message queue không phải database:** đừng dùng queue để lưu trữ lâu dài. Nó để *chuyển việc*, không phải *lưu trạng thái*.

### 🧭 Hướng dẫn làm lab & giải nghĩa lệnh (cho người tự học)

> Làm tuần tự, dừng ở mỗi ✅ **Checkpoint**.

**Bước 1 — Chạy RabbitMQ + mở UI.**
```bash
docker run -d --name rabbit -p 5672:5672 -p 15672:15672 rabbitmq:3-management
```
✅ **Checkpoint:** UI `localhost:15672` đăng nhập `guest/guest`.
💡 Cổng `5672` = giao thức AMQP (app kết nối); `15672` = UI quản trị.

**Bước 2 — Gửi & nhận 1 message.**
✅ **Checkpoint:** chạy `worker.py` rồi `send.py` → worker in `Nhận: ...`.
💡 `basic_ack` báo broker "đã xử lý xong" → message mới bị xoá. Không ack → message quay lại queue.

**Bước 3 — Thấy message xếp hàng (đệm).**
```bash
# tắt worker, chạy send.py 5 lần
```
✅ **Checkpoint:** UI tab Queues → `tasks` có 5 message chờ. Bật worker → rút dần về 0.
💡 Đây là "buffering": producer nhanh, consumer xử lý dần, không sập.

**Bước 4 — Scale bằng nhiều consumer.**
```bash
python worker.py &   python worker.py &   # 2 worker
python send.py; python send.py; python send.py; python send.py
```
✅ **Checkpoint:** 2 worker chia nhau message (mỗi cái in ~2). Thêm worker = xử lý nhanh hơn.

### 🐛 Gỡ lỗi nhanh

| Triệu chứng | Nguyên nhân | Cách sửa |
|---|---|---|
| Message mất khi broker restart | Queue/message không durable | `durable=True` + delivery_mode persistent |
| Message xử lý 2 lần gây sai dữ liệu | At-least-once + consumer không idempotent | Lưu ID đã xử lý; thiết kế idempotent |
| Queue phình mãi không rút | Consumer chậm/chết, hoặc quên ack | Thêm consumer; kiểm ack; đặt DLQ |
| Consumer xử lý xong nhưng message quay lại | Không gọi `basic_ack` | Ack sau khi xử lý thành công |
| Kafka: consumer không nhận event cũ | Offset đã qua / sai group | Đặt `auto.offset.reset=earliest`; group mới đọc lại |

### 📝 Bài ôn tập & Demo đối chiếu

**✍️ Tự kiểm tra:**

<details>
<summary>1. Message queue giải quyết vấn đề gì?</summary>

> Tách rời (decouple) service, đệm tải đột biến, không mất việc khi consumer chết, scale bằng thêm consumer — cho các tác vụ không cần trả lời ngay.
</details>

<details>
<summary>2. RabbitMQ khác Kafka thế nào?</summary>

> RabbitMQ = queue, message tiêu thụ rồi mất (task queue). Kafka = log sự kiện giữ lại, nhiều consumer group đọc lại độc lập (streaming, analytics).
</details>

<details>
<summary>3. Vì sao consumer phải idempotent?</summary>

> Queue thường giao "at-least-once" → đôi khi trùng. Không idempotent → xử lý trùng gây sai (vd trừ tiền 2 lần).
</details>

<details>
<summary>4. Khi nào KHÔNG nên dùng Kafka?</summary>

> Khi chỉ cần task queue đơn giản — Kafka nặng vận hành (partition/offset/group). Dùng RabbitMQ/SQS/Redis gọn hơn.
</details>

**🔬 Demo đối chiếu:**

| Demo đối chiếu | Kết quả mong đợi |
|---|---|
| Chạy RabbitMQ | UI `localhost:15672` đăng nhập được |
| Gửi/nhận message | Worker in message đã gửi |
| Message xếp hàng | UI thấy số message chờ khi tắt worker |

### 📚 Thuật ngữ Anh–Việt (bài này)

| Thuật ngữ | Nghĩa |
|---|---|
| **Message Queue / Broker** | Hàng đợi / bộ trung chuyển message |
| **Producer / Consumer** | Bên gửi / bên xử lý message |
| **Decoupling** | Tách rời phụ thuộc giữa service |
| **Ack** | Xác nhận đã xử lý (mới xoá message) |
| **Topic / Partition / Offset** | Kênh / phân vùng / vị trí đọc (Kafka) |
| **At-least-once** | Giao ít nhất 1 lần (có thể trùng) |
| **Idempotent** | Xử lý trùng vẫn cho kết quả đúng |

✅ **Kết quả đạt được:** Hiểu & dùng được message queue (RabbitMQ) cho kiến trúc bất đồng bộ, biết khi nào cần Kafka, và vì sao consumer phải idempotent.

---

## NC4 — Managed Kubernetes, cert-manager & Serverless

> ⏱️ ~90 phút · Loại: Cloud-native
>
> 🧭 **Bạn đang ở đâu:** Ngày 36–43 (K8s tự dựng local) + Ngày 26–28 (cloud cơ bản) → **NC4 (K8s do cloud vận hành + HTTPS tự động + serverless)**. Đây là cách chạy K8s ở production thật và các lựa chọn "không cần quản server".
>
> ✅ **Chuẩn bị:** tài khoản cloud (⚠️ managed K8s **tốn tiền thật** — bật billing alert, `destroy` sau khi học). Đã nắm K8s cơ bản (GĐ3).

### 📘 Lý thuyết

#### 1. Managed Kubernetes — vì sao đừng tự dựng ở production

Tự vận hành control plane K8s (etcd, API server, upgrade, vá bảo mật, HA) rất khó và rủi ro. **Managed K8s** để cloud lo control plane, bạn chỉ quản worker node + app.

| Cloud | Managed K8s |
|---|---|
| AWS | **EKS** |
| GCP | **GKE** (có Autopilot — cloud quản cả node) |
| Azure | **AKS** |

Điểm chung: control plane do cloud lo; tích hợp sẵn IAM, load balancer, storage, autoscaler của cloud.

#### 2. Khác biệt so với Minikube (local)

| | Local (Minikube) | Managed (EKS/GKE) |
|---|---|---|
| Control plane | Bạn tự chạy | Cloud lo (có phí/giờ) |
| Node | 1 máy | Node group tự scale |
| LoadBalancer Service | Không thật | Tạo LB thật của cloud |
| Storage | hostPath | EBS/PD (PV động qua StorageClass) |
| IAM | Không | Tích hợp (IRSA/Workload Identity) |

#### 3. cert-manager — HTTPS tự động trong K8s

Nhớ Ngày 23 (`certbot` thủ công)? Trong K8s, **cert-manager** tự động **xin + gia hạn chứng chỉ TLS** (Let's Encrypt) cho Ingress:
- Khai báo `ClusterIssuer` (Let's Encrypt).
- Ingress thêm annotation → cert-manager tự xin cert, lưu vào Secret, gia hạn trước hạn. HTTPS "tự lành".

#### 4. Serverless — "không cần quản server"

| Loại | Là gì | Ví dụ |
|---|---|---|
| **FaaS** | Chạy 1 hàm khi có sự kiện, tự scale về 0 | AWS Lambda, Cloud Functions |
| **Container serverless** | Chạy container không quản node, scale-to-zero | Cloud Run, AWS Fargate |
| **K8s serverless** | Scale-to-zero trên K8s | Knative |

Ưu: không quản server, trả tiền theo dùng thật, tự scale. Nhược: **cold start** (khởi động lần đầu chậm), giới hạn thời gian chạy, dễ khoá vào vendor.

#### 5. Chọn cái nào

- App chạy liên tục, phức tạp, nhiều service → **Managed K8s**.
- Tác vụ theo sự kiện, lưu lượng thất thường, muốn đơn giản → **Serverless** (Lambda/Cloud Run).
- Nhiều hệ thống dùng **cả hai** (K8s cho core, serverless cho job phụ).

> 🔑 Managed K8s tính tiền **control plane theo giờ** + node + LB → **luôn `terraform destroy`/xoá cluster sau khi học**. Serverless rẻ khi tải thấp nhưng coi chừng chi phí bất ngờ khi traffic lớn.

### 📖 Hiểu rõ hơn (giải thích cho người mới)

**Managed K8s — thuê tài xế thay vì tự lái xe tải.**
Tự dựng K8s (kubeadm) giống tự lái + tự bảo dưỡng xe tải: làm được nhưng tốn công, dễ hỏng. EKS/GKE giống thuê hãng lo phần đầu máy (control plane) — bạn chỉ xếp hàng lên xe (deploy app). Ở production, gần như không ai tự vận hành control plane K8s nữa.

**cert-manager — "certbot tự động cho cả cluster".**
Ngày 23 bạn chạy certbot tay cho từng domain. Trong K8s có hàng chục service → cert-manager làm tự động: bạn chỉ dán 1 annotation lên Ingress, nó lo xin cert, cắm vào, và **tự gia hạn** trước khi hết hạn. Không còn cảnh "quên gia hạn, web báo lỗi HTTPS".

**Serverless — trả tiền cho việc chạy, không cho việc chờ.**
Server thường chạy 24/7 dù không ai dùng (vẫn trả tiền). Serverless (Lambda/Cloud Run) chỉ chạy — và tính tiền — **khi có request**, rảnh thì **scale về 0** (miễn phí). Cực hợp cho job thất thường (webhook, xử lý ảnh khi upload). Đánh đổi: request đầu tiên sau khi "ngủ" bị chậm (**cold start**).

> 🧠 **Một câu để nhớ:** production K8s → dùng **managed** (đừng tự dựng control plane). HTTPS trong K8s → **cert-manager** (đừng certbot tay). Job thất thường/đơn giản → cân nhắc **serverless** thay vì nuôi server 24/7.

### 🧪 Lab cơ bản

> Mục tiêu: hiểu quy trình tạo managed cluster + cài cert-manager. (Có thể đọc-hiểu nếu ngại tốn phí; phần cert-manager chạy được trên Minikube.)

**Bước 1 — Tạo managed cluster (ví dụ GKE — hoặc đọc hiểu).**
```bash
# GKE (cần gcloud đã cấu hình) — VÍ DỤ, sẽ tốn phí:
gcloud container clusters create-auto demo --region=asia-southeast1
gcloud container clusters get-credentials demo --region=asia-southeast1
kubectl get nodes        # node do GKE quản
```
> AWS tương đương: `eksctl create cluster --name demo ...`. ⚠️ Nhớ xoá sau khi học.

**Bước 2 — Cài cert-manager (chạy được cả trên Minikube).**
```bash
kubectl apply -f https://github.com/cert-manager/cert-manager/releases/latest/download/cert-manager.yaml
kubectl get pods -n cert-manager      # các pod cert-manager Running
```

**Bước 3 — Tạo `ClusterIssuer` Let's Encrypt** (`issuer.yaml`):
```yaml
apiVersion: cert-manager.io/v1
kind: ClusterIssuer
metadata: { name: letsencrypt }
spec:
  acme:
    server: https://acme-v02.api.letsencrypt.org/directory
    email: ban@example.com
    privateKeySecretRef: { name: letsencrypt-key }
    solvers:
      - http01: { ingress: { class: nginx } }
```
```bash
kubectl apply -f issuer.yaml
```

**Bước 4 — Ingress tự xin HTTPS** (annotation):
```yaml
metadata:
  annotations:
    cert-manager.io/cluster-issuer: letsencrypt
spec:
  tls:
    - hosts: [app.example.com]
      secretName: app-tls        # cert-manager tự tạo & đổ cert vào đây
```

**Bước 5 — Kiểm tra chứng chỉ.**
```bash
kubectl get certificate           # thấy READY=True khi cert đã cấp
kubectl describe certificate app-tls
```

### 🚀 Lab nâng cao (best-practice)

> Mục tiêu: hiểu tích hợp cloud của managed K8s và triển khai serverless.

1. **IAM cho pod (không nhúng key cloud):** EKS **IRSA** / GKE **Workload Identity** — pod nhận quyền cloud qua danh tính, không cần access key cứng (giống Vault K8s auth).
2. **Cluster Autoscaler + node group** — node tự thêm/bớt theo tải pod (khác HPA scale pod; đây scale *node*).
3. **Deploy 1 hàm serverless** — ví dụ Cloud Run (container serverless, scale-to-zero):
   ```bash
   gcloud run deploy hello --image=gcr.io/PROJECT/hello --allow-unauthenticated --region=asia-southeast1
   # trả về URL HTTPS; không request → scale về 0 (không tính tiền compute)
   ```
4. **cert-manager production-grade** — dùng DNS-01 solver (cấp cert wildcard `*.example.com`), staging issuer để test tránh rate-limit Let's Encrypt.

### 💡 Bổ sung thực tế: chi phí, khoá vendor & khi nào serverless

- **Managed K8s không miễn phí:** control plane EKS ~$0.10/giờ + node + LB + egress. GKE Autopilot tính theo pod. → cluster để quên = hoá đơn đau. **Luôn xoá sau khi học** (`eksctl delete cluster` / `gcloud container clusters delete`).
- **Rate limit Let's Encrypt:** production issuer có giới hạn số cert/tuần. Test bằng **staging issuer** (cert không được trình duyệt tin nhưng không tốn quota), khi ổn mới chuyển production.
- **Serverless — đọc kỹ đánh đổi:** cold start (request đầu chậm, tệ với latency-sensitive), giới hạn thời gian chạy (Lambda ~15 phút), khó debug/quan sát hơn, dễ **vendor lock-in** (viết cho Lambda khó chuyển sang chỗ khác). → hợp cho job ngắn, sự kiện, tải thất thường; không hợp cho service chạy dài, tải đều cao (K8s rẻ hơn ở tải đều).
- **Managed K8s vẫn cần bạn hiểu K8s:** cloud lo *control plane*, nhưng app, manifest, RBAC, network policy, cost vẫn là việc của bạn. Kiến thức GĐ3 không thừa — nó là nền để dùng managed đúng.

### 🧭 Hướng dẫn làm lab & giải nghĩa lệnh (cho người tự học)

> Làm tuần tự, dừng ở mỗi ✅ **Checkpoint**. Phần cert-manager làm được trên Minikube (miễn phí).

**Bước 1 — Cài cert-manager.**
```bash
kubectl apply -f https://github.com/cert-manager/cert-manager/releases/latest/download/cert-manager.yaml
kubectl get pods -n cert-manager
```
✅ **Checkpoint:** 3 pod cert-manager (`cert-manager`, `cainjector`, `webhook`) đều `Running`.

**Bước 2 — Tạo ClusterIssuer.**
```bash
kubectl apply -f issuer.yaml
kubectl get clusterissuer
```
✅ **Checkpoint:** `letsencrypt` hiện `READY=True`.
💡 Dùng **staging** issuer khi test để không tốn quota Let's Encrypt.

**Bước 3 — Gắn annotation vào Ingress & kiểm cert.**
```bash
kubectl get certificate
```
✅ **Checkpoint:** certificate `READY=True` (cert-manager đã xin & lưu vào Secret).
💡 Cert-manager tự **gia hạn** trước hạn — không còn quên gia hạn.

**Bước 4 — (Nếu dùng cloud) tạo & XOÁ managed cluster.**
✅ **Checkpoint:** `kubectl get nodes` thấy node cloud; **xoá cluster xong** để không tốn phí.
⚠️ Đây là bước dễ "cháy túi" nhất — đặt lịch nhắc xoá.

### 🐛 Gỡ lỗi nhanh

| Triệu chứng | Nguyên nhân | Cách sửa |
|---|---|---|
| Certificate kẹt `READY=False` | HTTP-01 challenge fail (domain chưa trỏ / cổng 80 chặn) | Domain trỏ đúng IP Ingress; mở 80; đọc `describe certificate`/`challenge` |
| Bị Let's Encrypt rate-limit | Xin cert production quá nhiều lần | Dùng **staging issuer** khi test |
| Hoá đơn cloud tăng sốc | Quên xoá cluster / LB | Xoá cluster + LB + volume; billing alert |
| Pod thiếu quyền cloud | Chưa cấu hình IRSA/Workload Identity | Gán IAM qua danh tính pod, không nhúng access key |
| Serverless request đầu chậm | Cold start | Min-instances > 0 cho latency-sensitive; chấp nhận cho job nền |

### 📝 Bài ôn tập & Demo đối chiếu

**✍️ Tự kiểm tra:**

<details>
<summary>1. Vì sao production nên dùng managed K8s thay vì tự dựng?</summary>

> Vận hành control plane (etcd, API server, upgrade, HA, vá bảo mật) rất khó/rủi ro. Managed để cloud lo phần đó; bạn tập trung app + node + cost.
</details>

<details>
<summary>2. cert-manager giải quyết gì?</summary>

> Tự động xin + gia hạn chứng chỉ TLS (Let's Encrypt) cho Ingress trong K8s — thay cho certbot thủ công; HTTPS "tự lành".
</details>

<details>
<summary>3. Ưu/nhược của serverless?</summary>

> Ưu: không quản server, scale-to-zero, trả theo dùng. Nhược: cold start, giới hạn thời gian chạy, khó quan sát, dễ vendor lock-in.
</details>

<details>
<summary>4. Vì sao phải nhớ xoá managed cluster sau khi học?</summary>

> Control plane + node + LB tính tiền theo giờ; để quên = hoá đơn lớn. Luôn `destroy`/delete cluster + đặt billing alert.
</details>

**🔬 Demo đối chiếu:**

| Demo đối chiếu | Kết quả mong đợi |
|---|---|
| Cài cert-manager | Pod cert-manager Running |
| ClusterIssuer | `READY=True` |
| Certificate cho Ingress | `READY=True`, HTTPS hoạt động |

### 📚 Thuật ngữ Anh–Việt (bài này)

| Thuật ngữ | Nghĩa |
|---|---|
| **Managed K8s (EKS/GKE/AKS)** | K8s do cloud vận hành control plane |
| **Control plane** | Bộ não cluster (cloud lo ở managed) |
| **cert-manager** | Tự cấp/gia hạn TLS trong K8s |
| **ClusterIssuer** | Nguồn cấp chứng chỉ (Let's Encrypt) |
| **Serverless / FaaS** | Chạy không quản server / hàm theo sự kiện |
| **Cold start** | Độ trễ request đầu sau khi scale-to-zero |
| **IRSA / Workload Identity** | Cấp quyền cloud cho pod không cần key cứng |

✅ **Kết quả đạt được:** Hiểu managed K8s (EKS/GKE), HTTPS tự động bằng cert-manager, và serverless — cùng chi phí & đánh đổi để chọn đúng ở production.

---

> 🎓 **Hoàn thành Module nâng cao!** Bộ kỹ năng của bạn giờ phủ trọn cả 4 chủ đề từng là "lỗ hổng": distributed tracing (đủ 3 trụ cột observability), quản secret production-grade (Vault), kiến trúc bất đồng bộ (message queue), và cloud-native production (managed K8s + cert-manager + serverless). Kết hợp với 60 ngày chính, đây là nền tảng DevOps rất đầy đủ theo chuẩn ngành.
