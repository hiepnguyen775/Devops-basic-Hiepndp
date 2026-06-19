# Giai đoạn 3 — CI/CD, Kubernetes & Tự động hóa nâng cao

> **Ngày 31–50** · Trái tim của DevOps: pipeline tự động và điều phối container ở quy mô lớn.
>
> **Khuôn mỗi ngày:** 📘 Lý thuyết → 🧪 Lab cơ bản → 🚀 Lab nâng cao (best-practice) → 💡 Bổ sung thực tế → 📝 Bài ôn tập.
>
> ✅ Trung lập nền tảng: ví dụ CI dùng GitHub Actions, K8s dùng Minikube/local, cloud dùng ví dụ chung — đều có ghi chú công cụ tương đương (GitLab CI, EKS/GKE/AKS...).

---

## Mục lục

| Ngày | Chủ đề |
|------|--------|
| [31](#ngày-31--cicd-khái-niệm--github-actions-cơ-bản) | CI/CD — Khái niệm & GitHub Actions cơ bản |
| [32](#ngày-32--ci-pipeline--build-test--lint-tự-động) | CI Pipeline — Build, Test & Lint tự động |
| [33](#ngày-33--cd-pipeline--build--push-docker-image) | CD Pipeline — Build & Push Docker Image |
| [34](#ngày-34--cd-pipeline--tự-động-deploy-lên-server) | CD Pipeline — Tự động Deploy lên Server |
| [35](#ngày-35--milestone--pipeline-cicd-hoàn-chỉnh) | **Milestone — Pipeline CI/CD hoàn chỉnh** |
| [36](#ngày-36--kubernetes--khái-niệm--kiến-trúc) | Kubernetes — Khái niệm & Kiến trúc |
| [37](#ngày-37--kubernetes--pod-deployment--replicaset) | Kubernetes — Pod, Deployment & ReplicaSet |
| [38](#ngày-38--kubernetes--service--networking) | Kubernetes — Service & Networking |
| [39](#ngày-39--kubernetes--configmap-secret--storage) | Kubernetes — ConfigMap, Secret & Storage |
| [40](#ngày-40--milestone--deploy-full-stack-lên-kubernetes) | **Milestone — Deploy Full-stack lên Kubernetes** |
| [41](#ngày-41--kubernetes--health-check-resource--autoscaling) | Kubernetes — Health Check, Resource & Autoscaling |
| [42](#ngày-42--helm--package-manager-cho-kubernetes) | Helm — Package Manager cho Kubernetes |
| [43](#ngày-43--gitops--argocd--triển-khai-khai-báo) | GitOps — ArgoCD & Triển khai khai báo |
| [44](#ngày-44--monitoring--prometheus--metrics) | Monitoring — Prometheus & Metrics |
| [45](#ngày-45--monitoring--grafana-dashboard) | Monitoring — Grafana Dashboard |
| [46](#ngày-46--logging-tập-trung--loki) | Logging tập trung — Loki |
| [47](#ngày-47--configuration-management--ansible) | Configuration Management — Ansible |
| [48](#ngày-48--terraform-nâng-cao--module-remote-state--workspace) | Terraform nâng cao — Module, Remote State |
| [49](#ngày-49--bảo-mật-devsecops--best-practices) | Bảo mật DevSecOps & Best Practices |
| [50](#ngày-50--milestone--lab-tổng-hợp-giai-đoạn-3) | **Milestone — LAB tổng hợp Giai đoạn 3** |

---

## Ngày 31 — CI/CD: Khái niệm & GitHub Actions cơ bản

> ⏱️ ~90 phút · Loại: CI/CD
>
> 🔧 *Ví dụ dùng GitHub Actions; tương đương: **GitLab CI** (`.gitlab-ci.yml`), **Jenkins**, **CircleCI**.*

### 📘 Lý thuyết

- **CI (Continuous Integration):** mỗi lần push code → tự động build + test, phát hiện lỗi sớm.
- **CD (Continuous Delivery/Deployment):** tự động đưa code đã test lên staging/production.
- **Pipeline:** chuỗi bước tự động (lint → build → test → deploy).
- **GitHub Actions:** CI/CD tích hợp sẵn GitHub; cấu hình YAML trong `.github/workflows/`.
- **Khái niệm:** workflow, job, step, action, runner, trigger (`on: push`, `pull_request`).
- **Marketplace:** hàng nghìn action có sẵn (checkout, setup-node, docker build...).
- **Secret:** lưu thông tin nhạy cảm trong GitHub Secrets, không hard-code.

### 🧪 Lab cơ bản

1. Tạo `.github/workflows/ci.yml` chạy khi push: in `Hello CI`, chạy trên `ubuntu-latest`.
2. Push lên GitHub, vào tab Actions xem workflow chạy.
3. Thêm bước checkout code (`actions/checkout`) và setup môi trường (`setup-node`/`setup-python`).
4. Thêm bước chạy test đơn giản (echo hoặc lệnh test thật).
5. Tạo 1 GitHub Secret và in (che) nó trong workflow để hiểu cơ chế.

### 🚀 Lab nâng cao (best-practice)

> Mục tiêu: viết workflow chuẩn — có trigger đúng, tên rõ, dùng action ghim phiên bản.

1. **Workflow CI mẫu có cấu trúc:**
   ```yaml
   name: CI
   on:
     push: { branches: [main] }
     pull_request: { branches: [main] }
   jobs:
     test:
       runs-on: ubuntu-latest
       steps:
         - uses: actions/checkout@v4
         - uses: actions/setup-node@v4
           with: { node-version: '20', cache: 'npm' }
         - run: npm ci
         - run: npm test
   ```
2. **Ghim action theo phiên bản** (`@v4`, hoặc SHA cho bảo mật cao) — không dùng `@main` (thay đổi bất ngờ, rủi ro supply chain).
3. **Quyền tối thiểu cho token:** thêm `permissions: { contents: read }` ở đầu workflow.
4. **Trigger đúng:** PR chạy test, push main mới deploy — không deploy mỗi lần push nhánh.

### 💡 Bổ sung thực tế: vì sao CI/CD là kỹ năng "định danh" của DevOps

- **CI/CD trả lời 5 điểm yếu của deploy thủ công** (Ngày 28): lặp lại được, dấu vết đầy đủ (mỗi run có log), không phụ thuộc 1 người, rollback bằng re-run, ít sai vì máy làm.
- **Quan hệ workflow → job → step:**
  - **Workflow** = cả quy trình (1 file YAML).
  - **Job** = nhóm bước chạy trên 1 runner; các job **chạy song song** mặc định (dùng `needs:` để xếp thứ tự).
  - **Step** = 1 lệnh/action, chạy tuần tự trong job.
- **GitHub Secrets vs biến thường:** secret được **che trong log** (hiện `***`), không lộ ra. Token/key luôn dùng secret, không bao giờ viết thẳng YAML (commit = lộ vĩnh viễn).
- **Runner:** GitHub cấp runner sẵn (ubuntu/windows/macos) — sạch mỗi lần chạy. Khi cần môi trường riêng/mạnh hơn → self-hosted runner.

### 📝 Bài ôn tập & Demo đối chiếu

- **Bài ôn:** phân biệt CI và CD.
- workflow, job, step quan hệ với nhau thế nào?
- Vì sao dùng GitHub Secrets thay vì viết token trực tiếp trong YAML?

| Demo đối chiếu | Kết quả mong đợi |
|---|---|
| Tạo workflow đầu tiên | Tab Actions hiện job chạy với dấu ✓ xanh |
| Workflow tự kích hoạt khi push | Mỗi commit → 1 run mới |
| Đọc log của job | Xem được output từng step |

✅ **Kết quả đạt được:** Hiểu CI/CD, tạo được pipeline GitHub Actions đầu tiên.

---

## Ngày 32 — CI Pipeline: Build, Test & Lint tự động

> ⏱️ ~90 phút · Loại: CI/CD

### 📘 Lý thuyết

- **Các bước CI điển hình:** install dependencies → lint (kiểm tra style) → unit test → build.
- **Matrix build:** test trên nhiều phiên bản (Node 18, 20...) hoặc nhiều OS song song.
- **Caching:** cache dependencies (`node_modules`, pip) để pipeline chạy nhanh hơn.
- **Status check & badge:** hiển thị trạng thái build trên README.
- **Fail fast:** pipeline dừng ngay khi 1 bước lỗi.
- **Artifact:** lưu kết quả build (file, report) để dùng ở job sau hoặc tải về.
- **Bảo vệ nhánh:** yêu cầu CI pass trước khi merge PR (branch protection).

### 🧪 Lab cơ bản

1. Mở rộng pipeline: thêm bước lint, test, build cho app của bạn.
2. Cấu hình matrix build chạy test trên 2 phiên bản runtime.
3. Thêm caching dependencies để tăng tốc.
4. Upload 1 artifact (vd thư mục build) bằng `actions/upload-artifact`.
5. Bật branch protection: yêu cầu CI pass mới được merge vào main.

### 🚀 Lab nâng cao (best-practice)

> Mục tiêu: pipeline CI nhanh, đáng tin, chặn code lỗi trước khi vào main.

1. **Matrix + cache:**
   ```yaml
   strategy:
     matrix: { node: [18, 20] }
   steps:
     - uses: actions/setup-node@v4
       with: { node-version: '${{ matrix.node }}', cache: 'npm' }
   ```
2. **Tách job chạy song song** (lint, test, build độc lập) → pipeline nhanh hơn nhiều.
3. **Concurrency** — hủy run cũ khi push commit mới vào cùng PR (tiết kiệm runner):
   ```yaml
   concurrency: { group: '${{ github.ref }}', cancel-in-progress: true }
   ```
4. **Báo cáo coverage + chặn merge** nếu coverage giảm; thêm status badge vào README.

### 💡 Bổ sung thực tế: pipeline nhanh = team hạnh phúc

- **Pipeline chậm giết năng suất:** CI 30 phút = dev ngại push, batch nhiều thay đổi, khó tìm lỗi. Mục tiêu CI **dưới 10 phút**. Cách tăng tốc: cache, song song hóa job, chỉ test phần thay đổi.
- **Fail fast vs chạy hết:** mặc định 1 step lỗi → dừng job (tiết kiệm). Nhưng đôi khi muốn xem **tất cả** lỗi cùng lúc → `continue-on-error` hoặc `fail-fast: false` trong matrix.
- **Artifact dùng để:** chuyển file giữa job (build job → deploy job), lưu test report/screenshot khi fail để debug, phát hành binary.
- **Branch protection là "hàng rào chất lượng":** không có nó, CI chỉ là trang trí — người ta vẫn merge code lỗi. Bắt buộc: CI pass + ít nhất 1 review + nhánh up-to-date.

### 📝 Bài ôn tập & Demo đối chiếu

- **Bài ôn:** matrix build hữu ích trong trường hợp nào?
- Caching trong CI cải thiện điều gì?
- Artifact dùng để làm gì?

| Demo đối chiếu | Kết quả mong đợi |
|---|---|
| Pipeline tự chạy test | Job Test → passed (xanh) khi code đúng |
| Test fail | CI báo lỗi đỏ và chặn merge |
| Lint tự động | Step lint chạy, báo cảnh báo/lỗi format |

✅ **Kết quả đạt được:** Xây dựng CI pipeline hoàn chỉnh: lint + test + build + bảo vệ nhánh.

---

## Ngày 33 — CD Pipeline: Build & Push Docker Image

> ⏱️ ~90 phút · Loại: CI/CD

### 📘 Lý thuyết

- **Mục tiêu:** mỗi khi merge vào main → tự động build Docker image và push lên registry.
- **Docker trong Actions:** `docker/build-push-action`, `docker/login-action`.
- **Registry:** Docker Hub hoặc GitHub Container Registry (`ghcr.io`).
- **Đặt tag image theo commit SHA hoặc version** để truy vết.
- **Lưu credential registry trong GitHub Secrets.**
- **Conditional steps:** chỉ push khi ở nhánh main (`if: github.ref == ...`).
- **Multi-platform build (buildx)** cho amd64/arm64 (nâng cao).

### 🧪 Lab cơ bản

1. Tạo workflow build Docker image khi push lên main.
2. Cấu hình login vào Docker Hub/ghcr bằng Secrets.
3. Push image với 2 tag: `latest` và commit SHA.
4. Kiểm tra image xuất hiện trên registry sau khi pipeline chạy.
5. Thêm điều kiện chỉ build+push khi nhánh là main.

### 🚀 Lab nâng cao (best-practice)

> Mục tiêu: build image có tag truy vết được, dùng cache layer, đa nền tảng.

1. **Build + push chuẩn với tag tự động:**
   ```yaml
   - uses: docker/login-action@v3
     with: { registry: ghcr.io, username: ${{ github.actor }}, password: ${{ secrets.GITHUB_TOKEN }} }
   - uses: docker/metadata-action@v5
     id: meta
     with: { images: ghcr.io/${{ github.repository }} }
   - uses: docker/build-push-action@v6
     with:
       push: true
       tags: ${{ steps.meta.outputs.tags }}    # tự sinh tag từ branch/sha/version
       cache-from: type=gha
       cache-to: type=gha,mode=max               # cache layer giữa các run
   ```
2. **Dùng `ghcr.io` với `GITHUB_TOKEN`** — không cần tạo secret riêng, quyền theo repo.
3. **Tag theo SHA + semver** để mỗi deploy truy về đúng commit.
4. **Quét image bằng Trivy** ngay trong pipeline trước khi push (xem Ngày 49).

### 💡 Bổ sung thực tế: vì sao KHÔNG dùng `latest` để deploy

- **`latest` là cái bẫy ở production:** "máy nào pull lúc nào ra phiên bản đó" → không ai biết chính xác đang chạy gì, không rollback chính xác được. → Luôn deploy theo **tag bất biến** (SHA/semver).
- **Tag theo commit SHA = truy vết hoàn hảo:** thấy `myapp:a1b2c3d` → biết ngay commit nào, ai viết, PR nào. Khi sự cố, đây là vàng.
- **`GITHUB_TOKEN` vs Personal Access Token:** `GITHUB_TOKEN` tự sinh mỗi run, hết hạn sau run, quyền giới hạn theo repo — an toàn hơn PAT cá nhân nhiều. Ưu tiên dùng nó.
- **Cache layer trong CI** (`type=gha`) — không có cache, mỗi build cài lại từ đầu, rất chậm. Cache đúng = build vài giây thay vì vài phút.

### 📝 Bài ôn tập & Demo đối chiếu

- **Bài ôn:** vì sao nên tag image theo commit SHA thay vì chỉ `latest`?
- Credential registry nên lưu ở đâu trong GitHub Actions?
- Giải thích bước `login-action` làm gì.

| Demo đối chiếu | Kết quả mong đợi |
|---|---|
| CI tự build Docker image | Image được tạo trong runner |
| Push image lên registry | Docker Hub/GHCR hiện image với tag mới |
| Image gắn tag theo commit | Tag dạng sha hoặc version xuất hiện |

✅ **Kết quả đạt được:** Tự động build và đẩy Docker image lên registry mỗi lần merge.

---

## Ngày 34 — CD Pipeline: Tự động Deploy lên Server

> ⏱️ ~90 phút · Loại: CI/CD

### 📘 Lý thuyết

- **Deploy tự động:** sau khi push image, pipeline SSH vào server và cập nhật container.
- **SSH trong CI:** lưu private key trong Secrets, dùng action SSH (vd `appleboy/ssh-action`).
- **Chiến lược cập nhật:** pull image mới → `docker compose up -d` (recreate container).
- **Zero-downtime cơ bản:** health check trước khi chuyển traffic.
- **Rollback:** quay về image version trước nếu deploy lỗi.
- **Môi trường:** tách workflow deploy staging vs production (environments + approval).
- **Bảo mật pipeline:** least privilege cho deploy key.

### 🧪 Lab cơ bản

1. Thêm job deploy: SSH vào VM, pull image mới và chạy lại `docker compose`.
2. Lưu SSH private key và host vào GitHub Secrets.
3. Test pipeline end-to-end: sửa code → push → tự build → deploy → kiểm tra app cập nhật.
4. Cấu hình GitHub Environment cho production cần approval thủ công.
5. Thực hành rollback: deploy version cũ khi phát hiện lỗi.

### 🚀 Lab nâng cao (best-practice)

> Mục tiêu: deploy tự động an toàn — có approval cho production, có health check, rollback được.

1. **GitHub Environments + required reviewers:** production deploy phải có người duyệt → chặn deploy nhầm giữa đêm.
2. **Deploy có health check:** sau khi `up -d`, pipeline `curl /health` — fail thì rollback tự động:
   ```bash
   docker compose up -d
   for i in $(seq 1 10); do curl -fs localhost/health && exit 0; sleep 3; done
   echo "Health check failed, rolling back"; docker compose down; exit 1
   ```
3. **Deploy key least privilege:** SSH key riêng cho deploy, chỉ quyền cần thiết, không phải key cá nhân full quyền.
4. **Tách staging/production:** merge vào `develop` → deploy staging tự động; tag release → deploy production (có approval).

### 💡 Bổ sung thực tế: chiến lược deploy & vì sao cần approval

- **Luồng CD đầy đủ:** `git push → CI test → build image → push registry → deploy server → health check → (fail? rollback)`.
- **Vì sao production cần approval:** CD lên staging nên tự động hoàn toàn (nhanh, an toàn). Nhưng production ảnh hưởng người dùng thật → cần 1 người nhìn lại, đặc biệt giờ cao điểm. Đây là **Continuous Delivery** (sẵn sàng deploy, bấm nút) vs **Continuous Deployment** (tự động hoàn toàn).
- **Các chiến lược deploy nâng cao** (sẽ gặp lại ở K8s):
  | Chiến lược | Cách làm |
  |---|---|
  | **Rolling** | thay dần từng instance — mặc định, đơn giản |
  | **Blue-Green** | 2 môi trường, switch traffic tức thì, rollback nhanh |
  | **Canary** | đẩy cho % nhỏ user trước, theo dõi rồi mở rộng |
- **Rollback phải nhanh hơn fix:** khi production lỗi, **rollback trước, điều tra sau**. Deploy theo tag bất biến giúp rollback = chạy lại deploy với tag cũ.

### 📝 Bài ôn tập & Demo đối chiếu

- **Bài ôn:** mô tả luồng CD đầy đủ từ git push đến app chạy bản mới.
- Vì sao production deploy nên có bước approval?
- Rollback hoạt động thế nào trong chiến lược deploy của bạn?

| Demo đối chiếu | Kết quả mong đợi |
|---|---|
| Pipeline tự deploy lên server | Sau khi push, server tự cập nhật phiên bản mới |
| Dùng secrets an toàn | SSH key/token trong Secrets, không lộ trong log |
| Xác nhận deploy thành công | `curl` tới server trả về version mới |

✅ **Kết quả đạt được:** Hoàn chỉnh pipeline CI/CD end-to-end: push code là tự động lên production.

---

## Ngày 35 — MILESTONE: Pipeline CI/CD hoàn chỉnh

> ⏱️ ~120 phút · Loại: Milestone

### 📘 Lý thuyết — Tổng kết

- **Mạch CI/CD:** lint/test → build image → push registry → deploy server → rollback.
- **Đây là kỹ năng định danh của 1 DevOps Engineer.**
- **Best practices:** pipeline nhanh, fail fast, secret an toàn, deploy có thể đảo ngược.

### 🧪 Lab cơ bản (Milestone)

1. Xây pipeline hoàn chỉnh cho app full-stack — từ push code tới deploy tự động lên VM.
2. Pipeline gồm: lint → test → build Docker → push → deploy qua SSH → health check.
3. Thêm status badge vào README.
4. Demo: thực hiện 1 thay đổi nhỏ và quay video/screenshot toàn bộ pipeline chạy thành công.
5. Đẩy lên repo `cicd-pipeline-demo` với tài liệu đầy đủ.

### 🚀 Lab nâng cao (best-practice) — Mô hình hoàn chỉnh

**Mô hình pipeline CI/CD end-to-end:**
```
  Developer ──push──▶ GitHub
                        │
        ┌───────────────▼───────────────┐
        │   CI (mỗi PR/push)            │
        │   lint → test → scan (Trivy)  │  ◀── chặn merge nếu fail
        └───────────────┬───────────────┘
                        │ merge main
        ┌───────────────▼───────────────┐
        │   CD                          │
        │   build image (tag=SHA)       │
        │   push → registry             │
        │   deploy (SSH/compose)        │
        │   health check                │  ── fail? ──▶ rollback
        └───────────────┬───────────────┘
                        ▼
                  App live (vài phút từ commit)
```

**Yêu cầu best-practice:**
1. **CI và CD tách rõ:** CI chạy mọi PR; CD chỉ chạy khi merge main / tag.
2. **Image tag theo SHA**, cache layer, quét Trivy.
3. **Secret trong GitHub Secrets/Environments**, production có approval.
4. **Health check + rollback tự động.**
5. **Status badge** + README mô tả luồng + sơ đồ.

### 📝 Bài ôn tập & Demo đối chiếu

- **Tự chấm:** pipeline chạy từ commit tới production không cần thao tác tay không?
- **Mở rộng:** thêm thông báo Slack/Discord khi deploy xong.
- Vẽ sơ đồ toàn bộ pipeline.

| Demo đối chiếu | Kết quả mong đợi |
|---|---|
| Pipeline end-to-end | push → test → build → push → deploy, tất cả tự động |
| Thời gian commit → live | Đo được (vài phút), không thao tác tay |
| Repo có workflow đầy đủ | `.github/workflows/*.yml` có đủ các stage |

✅ **Kết quả đạt được — MỐC 4:** Làm chủ CI/CD end-to-end — năng lực cốt lõi nhất của DevOps.

---

## Ngày 36 — Kubernetes: Khái niệm & Kiến trúc

> ⏱️ ~90 phút · Loại: Kubernetes
>
> ☸️ *Học trên Minikube/kind/k3s (local); production dùng managed: **EKS** (AWS) / **GKE** (GCP) / **AKS** (Azure).*

### 📘 Lý thuyết

- **Vấn đề K8s giải quyết:** chạy/quản lý hàng trăm container, tự phục hồi, scale, không downtime.
- **Kiến trúc:**
  - **Control Plane:** API server, scheduler, etcd (database trạng thái), controller manager.
  - **Worker Node:** kubelet, kube-proxy, container runtime.
- **Đối tượng cơ bản:** Pod (đơn vị nhỏ nhất, chứa 1+ container), Node, Cluster.
- **Declarative:** bạn mô tả **trạng thái mong muốn** (YAML), K8s tự điều chỉnh để đạt được.
- **kubectl:** công cụ dòng lệnh điều khiển cluster.
- **Self-healing:** pod chết → K8s tự tạo lại; đây là sức mạnh chính.

### 🧪 Lab cơ bản

1. Cài Minikube (hoặc kind) và kubectl, khởi động: `minikube start`.
2. Kiểm tra: `kubectl get nodes`, `kubectl cluster-info`.
3. Chạy pod đầu tiên: `kubectl run nginx --image=nginx`, xem `kubectl get pods`.
4. Mô tả pod: `kubectl describe pod <tên>`, xem log: `kubectl logs <tên>`.
5. Xóa pod và quan sát (nếu là deployment thì K8s tạo lại).

### 🚀 Lab nâng cao (best-practice)

> Mục tiêu: làm quen kubectl đúng cách và hiểu mô hình declarative ngay từ đầu.

1. **Declarative ngay từ đầu — không dùng lệnh imperative:** thay vì `kubectl run`, viết YAML và `kubectl apply -f`. Mọi thứ trong file = version hóa được, review được.
2. **`kubectl` thiết yếu:**
   ```bash
   kubectl get all -A              # xem mọi thứ ở mọi namespace
   kubectl describe pod <name>     # điều tra: events, lý do crash
   kubectl logs -f <pod>           # theo dõi log
   kubectl get events --sort-by=.lastTimestamp   # chuyện gì vừa xảy ra
   ```
3. **Dùng `--dry-run=client -o yaml`** để sinh YAML mẫu nhanh:
   ```bash
   kubectl create deployment web --image=nginx --dry-run=client -o yaml > deploy.yaml
   ```
4. **Đặt alias `k=kubectl`** và bật autocomplete — bạn sẽ gõ nó hàng nghìn lần.

### 💡 Bổ sung thực tế: hiểu "vòng điều hòa" (reconciliation loop)

- **Linh hồn của K8s:** controller liên tục so sánh **trạng thái thực tế** với **trạng thái mong muốn** trong etcd, và hành động để khớp. Bạn nói "tôi muốn 3 pod" → 1 pod chết → controller thấy 2≠3 → tạo lại. Đây là **self-healing**.
- **Imperative vs Declarative:**
  | | Ví dụ | Vấn đề/Lợi ích |
  |---|---|---|
  | Imperative | `kubectl run`, `kubectl scale` | nhanh để thử, nhưng không lưu vết |
  | Declarative | `kubectl apply -f file.yaml` | nguồn sự thật trong Git → chuẩn production |
- **etcd là "bộ não":** lưu toàn bộ trạng thái cluster. Mất etcd = mất cluster → backup etcd là việc sống còn ở production (managed K8s lo hộ bạn việc này).
- **Học local trước:** Minikube/kind/k3s đủ để học mọi khái niệm. Đừng vội lên cloud K8s (tốn tiền + phức tạp) khi chưa vững cơ bản.

### 📝 Bài ôn tập & Demo đối chiếu

- **Bài ôn:** Pod là gì và khác container thế nào?
- Control Plane và Worker Node mỗi bên làm gì?
- Declarative nghĩa là gì trong K8s?

| Demo đối chiếu | Kết quả mong đợi |
|---|---|
| Cụm K8s hoạt động | `kubectl get nodes` → STATUS Ready |
| Xem thông tin cụm | `kubectl cluster-info` in control plane URL |
| Giải thích kiến trúc | Mô tả control plane, node, kubelet, etcd |

✅ **Kết quả đạt được:** Hiểu kiến trúc Kubernetes, chạy cluster local và pod đầu tiên.

---

## Ngày 37 — Kubernetes: Pod, Deployment & ReplicaSet

> ⏱️ ~90 phút · Loại: Kubernetes

### 📘 Lý thuyết

- **Pod YAML:** `apiVersion`, `kind`, `metadata`, `spec` (containers, image, ports).
- **Deployment:** quản lý ReplicaSet, đảm bảo số lượng pod mong muốn, hỗ trợ rolling update.
- **ReplicaSet:** duy trì số bản sao pod; thường không tạo trực tiếp mà qua Deployment.
- **Scaling:** `kubectl scale deployment <tên> --replicas=3`.
- **Rolling update & rollback:** cập nhật image không downtime; `kubectl rollout undo`.
- **Label & selector:** gắn nhãn để nhóm và chọn lọc đối tượng.
- **`kubectl apply -f file.yaml`:** áp dụng cấu hình declarative.

### 🧪 Lab cơ bản

1. Viết `deployment.yaml` chạy 3 replica của app bạn, `kubectl apply -f`.
2. Xem: `kubectl get deployments`, `kubectl get pods` (thấy 3 pod).
3. Scale lên 5 rồi xuống 2: `kubectl scale`.
4. Rolling update đổi image version, xem `kubectl rollout status`.
5. Rollback về version cũ: `kubectl rollout undo deployment/<tên>`.

### 🚀 Lab nâng cao (best-practice)

> Mục tiêu: viết Deployment chuẩn production — có label đúng, rolling update kiểm soát.

1. **Deployment với chiến lược rolling update kiểm soát:**
   ```yaml
   spec:
     replicas: 3
     strategy:
       type: RollingUpdate
       rollingUpdate: { maxSurge: 1, maxUnavailable: 0 }   # 0 downtime: tạo mới trước, xóa cũ sau
     selector: { matchLabels: { app: web } }
     template:
       metadata: { labels: { app: web } }
       spec:
         containers:
           - name: web
             image: ghcr.io/user/web:a1b2c3d   # tag bất biến, KHÔNG latest
   ```
2. **Luôn dùng tag bất biến** (SHA) trong image — `latest` làm rolling update không đoán được.
3. **Label chuẩn** (`app.kubernetes.io/name`, `version`) để Service/monitoring chọn đúng pod.
4. **`kubectl rollout`** kiểm soát triển khai:
   ```bash
   kubectl rollout status deployment/web   # theo dõi tiến trình
   kubectl rollout history deployment/web  # lịch sử các bản
   kubectl rollout undo deployment/web     # rollback
   ```

### 💡 Bổ sung thực tế: chuỗi Deployment → ReplicaSet → Pod & rolling update

- **Chuỗi quản lý:** **Deployment** (bạn khai báo) → tạo **ReplicaSet** (đảm bảo số lượng) → tạo **Pod** (chạy thật). Mỗi lần đổi image, Deployment tạo ReplicaSet mới, dịch dần pod từ cũ sang mới.
- **Rolling update tránh downtime:** thay vì tắt hết rồi bật lại (downtime), K8s thay **từng pod một**, luôn giữ đủ pod phục vụ. `maxUnavailable: 0` = không bao giờ thiếu pod.
- **Vì sao không tạo Pod trực tiếp:** Pod "trần" chết là mất luôn (không tự tạo lại). Luôn dùng Deployment để có self-healing + scaling + rolling update.
- **Rollback trong giây:** `kubectl rollout undo` quay về ReplicaSet cũ tức thì — đây là lý do K8s rollback nhanh hơn deploy thủ công rất nhiều.

### 📝 Bài ôn tập & Demo đối chiếu

- **Bài ôn:** Deployment quản lý ReplicaSet quản lý Pod — giải thích chuỗi này.
- Rolling update giúp tránh điều gì?
- Viết lệnh scale deployment lên 4 replica.

| Demo đối chiếu | Kết quả mong đợi |
|---|---|
| Tạo Deployment | `kubectl get deploy` → READY 3/3 |
| Xem các Pod | `kubectl get pods` → tất cả Running |
| Thử xóa 1 pod | K8s tự tạo lại pod mới (self-healing) |

✅ **Kết quả đạt được:** Triển khai và scale ứng dụng bằng Deployment, rolling update an toàn.

---

## Ngày 38 — Kubernetes: Service & Networking

> ⏱️ ~90 phút · Loại: Kubernetes

### 📘 Lý thuyết

- **Vấn đề:** pod có IP thay đổi liên tục → cần cách truy cập ổn định = **Service**.
- **Loại Service:** ClusterIP (nội bộ, mặc định), NodePort (mở cổng trên node), LoadBalancer (cloud), ExternalName.
- **Service dùng label selector** để định tuyến traffic tới đúng pod.
- **DNS nội bộ:** pod gọi service qua tên (`service-name.namespace.svc.cluster.local`).
- **Ingress:** định tuyến HTTP/HTTPS từ ngoài vào nhiều service (như reverse proxy cấp cluster).
- **Ingress Controller:** nginx-ingress, traefik — cần cài để Ingress hoạt động.
- **Port:** `port` (service), `targetPort` (container), `nodePort` (trên node).

### 🧪 Lab cơ bản

1. Tạo Service ClusterIP cho deployment, test truy cập nội bộ từ pod khác.
2. Tạo Service NodePort và truy cập app qua `minikube service <tên>`.
3. Bật ingress addon trong minikube và cài ingress controller.
4. Viết Ingress định tuyến theo path tới service của bạn.
5. Test truy cập app qua Ingress host/path.

### 🚀 Lab nâng cao (best-practice)

> Mục tiêu: hiểu khi nào dùng loại Service nào, expose app đúng chuẩn qua Ingress.

1. **ClusterIP + Ingress là chuẩn production** (không NodePort):
   ```yaml
   apiVersion: networking.k8s.io/v1
   kind: Ingress
   metadata: { name: web, annotations: { nginx.ingress.kubernetes.io/rewrite-target: / } }
   spec:
     rules:
       - host: app.example.com
         http:
           paths:
             - path: /api
               pathType: Prefix
               backend: { service: { name: api-svc, port: { number: 80 } } }
   ```
2. **Service nội bộ dùng ClusterIP** — DB/backend không bao giờ expose ra ngoài.
3. **TLS qua Ingress + cert-manager** — tự động cấp/gia hạn chứng chỉ Let's Encrypt.
4. **Đặt tên service rõ ràng** (`api-svc`, `db-svc`) vì pod gọi nhau qua tên này.

### 💡 Bổ sung thực tế: chọn loại Service & Ingress vs LoadBalancer

- **Khi nào dùng loại nào:**
  | Service | Dùng khi |
  |---|---|
  | **ClusterIP** | giao tiếp nội bộ trong cluster (mặc định, an toàn) — đa số trường hợp |
  | **NodePort** | test local/dev nhanh — không dùng production (port cao, xấu) |
  | **LoadBalancer** | expose 1 service ra ngoài qua LB của cloud — mỗi service 1 LB (tốn tiền) |
  | **Ingress** | 1 điểm vào cho **nhiều** service theo host/path — chuẩn production |
- **Ingress vs LoadBalancer:** LoadBalancer = mỗi service 1 IP/LB ngoài (tốn kém). Ingress = 1 LB + định tuyến thông minh cho hàng chục service (tiết kiệm, linh hoạt). → Production gần như luôn dùng Ingress.
- **DNS nội bộ là phép màu microservice:** backend gọi `http://db-svc:5432` — K8s tự phân giải tên → IP pod hiện tại, kể cả khi pod đổi IP liên tục. Đây là lý do Service tồn tại.
- **Ingress controller chính là nginx/traefik** — kiến thức nginx (Ngày 23) áp dụng thẳng vào đây.

### 📝 Bài ôn tập & Demo đối chiếu

- **Bài ôn:** phân biệt ClusterIP, NodePort, LoadBalancer.
- Service giải quyết vấn đề gì của IP pod?
- Ingress khác Service LoadBalancer thế nào?

| Demo đối chiếu | Kết quả mong đợi |
|---|---|
| Tạo Service expose app | `kubectl get svc` hiện ClusterIP/NodePort |
| Truy cập app qua Service | `curl`/port-forward trả về app |
| Load balancing giữa pod | Request phân phối tới các pod khác nhau |

✅ **Kết quả đạt được:** Kết nối và expose ứng dụng trong K8s qua Service và Ingress.

---

## Ngày 39 — Kubernetes: ConfigMap, Secret & Storage

> ⏱️ ~90 phút · Loại: Kubernetes

### 📘 Lý thuyết

- **ConfigMap:** lưu cấu hình **không nhạy cảm** (biến môi trường, file config) tách khỏi image.
- **Secret:** lưu thông tin **nhạy cảm** (mật khẩu, token) — mã hóa base64 (⚠️ base64 KHÔNG phải mã hóa, cần thêm biện pháp thật).
- **Inject vào pod:** qua biến môi trường (`env`/`envFrom`) hoặc mount thành file (volume).
- **Volume trong K8s:** `emptyDir`, `hostPath`; PersistentVolume (PV) + PersistentVolumeClaim (PVC) cho lưu trữ bền vững.
- **StorageClass:** cấp phát storage động.
- **StatefulSet:** cho ứng dụng có trạng thái (database) cần danh tính và storage ổn định.
- **Namespace:** phân vùng logic cluster (dev, prod) để tổ chức và phân quyền.

### 🧪 Lab cơ bản

1. Tạo ConfigMap chứa biến cấu hình, inject vào pod qua `env`.
2. Tạo Secret chứa mật khẩu DB, mount vào pod.
3. Tạo PersistentVolumeClaim và gắn vào pod để lưu dữ liệu bền vững.
4. Tạo namespace `dev` và deploy app vào đó: `kubectl apply -n dev`.
5. Xem tài nguyên theo namespace: `kubectl get all -n dev`.

### 🚀 Lab nâng cao (best-practice)

> Mục tiêu: quản lý cấu hình/secret đúng chuẩn, hiểu giới hạn của Secret base64.

1. **Tách config khỏi image hoàn toàn** — cùng 1 image chạy được mọi môi trường nhờ ConfigMap/Secret khác nhau.
2. **Secret KHÔNG dùng base64 thuần ở production** — dùng:
   - **Sealed Secrets / External Secrets Operator** — đồng bộ từ Vault/cloud secret manager.
   - Bật **encryption at rest** cho etcd.
3. **StatefulSet cho database** (không phải Deployment) — pod có danh tính ổn định (`db-0`, `db-1`), storage gắn cố định.
4. **Namespace tách môi trường + ResourceQuota** giới hạn tài nguyên mỗi namespace.

### 💡 Bổ sung thực tế: base64 ≠ mã hóa & ConfigMap vs Secret

- **CẢNH BÁO quan trọng:** K8s Secret chỉ **base64-encode**, ai có quyền đọc Secret là đọc được plaintext (`echo <value> | base64 -d`). Secret an toàn cần: RBAC chặt + encryption-at-rest cho etcd + công cụ ngoài (Vault). Đừng tưởng "đặt vào Secret là an toàn".
- **ConfigMap vs Secret:** dùng giống nhau, khác ở **ý định** — ConfigMap cho config thường (log level, URL), Secret cho nhạy cảm (mật khẩu, token). Secret được xử lý cẩn thận hơn (không hiện trong `describe`, có thể mã hóa).
- **Stateless vs Stateful:** app web (stateless) → Deployment. Database (stateful, cần lưu dữ liệu + danh tính) → StatefulSet + PVC. Nhầm lẫn = mất dữ liệu.
- **Namespace để làm gì:** cô lập logic (dev/staging/prod), phân quyền RBAC theo namespace, giới hạn tài nguyên — không phải bảo mật mạng (cần NetworkPolicy cho việc đó, Ngày 49).

### 📝 Bài ôn tập & Demo đối chiếu

- **Bài ôn:** khi nào dùng ConfigMap, khi nào dùng Secret?
- PVC và PV quan hệ thế nào?
- Namespace dùng để làm gì?

| Demo đối chiếu | Kết quả mong đợi |
|---|---|
| Tạo ConfigMap và Secret | `kubectl get configmap,secret` liệt kê đúng |
| Pod có config từ env | `kubectl exec` → biến môi trường có giá trị mong đợi |
| Gắn PersistentVolume | Dữ liệu còn sau khi pod bị xóa và tạo lại |

✅ **Kết quả đạt được:** Quản lý cấu hình, secret và lưu trữ bền vững trong Kubernetes.

---

## Ngày 40 — MILESTONE: Deploy Full-stack lên Kubernetes

> ⏱️ ~120 phút · Loại: Milestone

### 📘 Lý thuyết — Tổng kết

- **Mạch K8s:** Pod → Deployment → Service → Ingress → ConfigMap/Secret → PVC → Namespace.
- **Kiến trúc:** frontend Deployment + Service, backend Deployment + Service, database StatefulSet + PVC, Ingress định tuyến.

### 🧪 Lab cơ bản (Milestone)

1. Deploy app full-stack (web + backend + database) lên Minikube bằng manifest YAML.
2. Dùng ConfigMap/Secret cho cấu hình, PVC cho database, Service kết nối các tầng.
3. Cấu hình Ingress để truy cập app từ ngoài.
4. Tổ chức tất cả YAML trong thư mục `k8s/` của repo, có README.
5. Test: scale backend lên 3 replica và thực hiện rolling update.

### 🚀 Lab nâng cao (best-practice) — Mô hình hoàn chỉnh

**Mô hình full-stack trên K8s:**
```
            Internet
               │
        ┌──────▼───────┐
        │   Ingress    │  (nginx-ingress + cert-manager TLS)
        └──┬────────┬──┘
     /     │        │  /api
  ┌────────▼─┐   ┌──▼────────┐
  │ frontend │   │  backend  │   Deployment (3 replica) + Service ClusterIP
  │ Service  │   │  Service  │
  └──────────┘   └────┬──────┘
                      │
              ┌───────▼────────┐
              │   database     │   StatefulSet + PVC (lưu bền vững)
              │  (db-svc)      │   Secret: mật khẩu DB
              └────────────────┘
   ConfigMap: cấu hình app · Namespace: tách môi trường
```

**Yêu cầu best-practice:**
1. Frontend/backend dùng **Deployment + ClusterIP**, expose qua **Ingress**.
2. Database dùng **StatefulSet + PVC**, mật khẩu qua **Secret**.
3. Cấu hình qua **ConfigMap**, mọi thứ trong **namespace** riêng.
4. Có **liveness/readiness probe** + **resource requests/limits** (chuẩn bị Ngày 41).
5. Toàn bộ YAML trong `k8s/`, README có sơ đồ + lệnh `kubectl apply -k`.

### 📝 Bài ôn tập & Demo đối chiếu

- **Tự chấm:** bạn deploy được ứng dụng nhiều tầng lên K8s chưa?
- **Mở rộng:** thêm liveness/readiness probe cho các pod.
- Vẽ sơ đồ kiến trúc K8s của bạn.

| Demo đối chiếu | Kết quả mong đợi |
|---|---|
| App full-stack trên K8s | frontend + backend + db đều Running |
| Truy cập từ ngoài cụm | Mở qua Ingress/NodePort thấy giao diện app |
| Manifests trong repo | `k8s/` có deployment, service, configmap... |

✅ **Kết quả đạt được — MỐC 5:** Triển khai ứng dụng full-stack lên Kubernetes — kỹ năng cao cấp.

---

## Ngày 41 — Kubernetes: Health Check, Resource & Autoscaling

> ⏱️ ~90 phút · Loại: Kubernetes

### 📘 Lý thuyết

- **Probe:** liveness (pod còn sống?), readiness (sẵn sàng nhận traffic?), startup (khởi động xong chưa?).
- **Resource requests & limits:** requests (tối thiểu cần), limits (trần tối đa) cho CPU/RAM.
- **QoS class:** Guaranteed, Burstable, BestEffort — ảnh hưởng thứ tự bị evict khi thiếu tài nguyên.
- **Horizontal Pod Autoscaler (HPA):** tự scale số pod theo CPU/metric.
- **Metrics Server:** cần cài để HPA hoạt động.
- **Vertical vs Horizontal scaling.**
- **Node affinity, taints & tolerations** (giới thiệu): điều khiển pod chạy ở node nào.

### 🧪 Lab cơ bản

1. Thêm liveness & readiness probe vào deployment, test bằng cách làm pod fail.
2. Đặt resource requests/limits cho container.
3. Cài metrics-server trong minikube (`minikube addons enable metrics-server`).
4. Tạo HPA: `kubectl autoscale deployment <tên> --cpu-percent=50 --min=1 --max=5`.
5. Tạo tải giả để quan sát HPA tự scale pod lên.

### 🚀 Lab nâng cao (best-practice)

> Mục tiêu: cấu hình pod "khỏe mạnh" đúng chuẩn — probe đúng, tài nguyên hợp lý, tự scale.

1. **3 loại probe dùng đúng vai trò:**
   ```yaml
   startupProbe:   { httpGet: { path: /health, port: 8080 }, failureThreshold: 30, periodSeconds: 2 }
   readinessProbe: { httpGet: { path: /ready,  port: 8080 }, periodSeconds: 5 }
   livenessProbe:  { httpGet: { path: /health, port: 8080 }, periodSeconds: 10 }
   ```
2. **Luôn đặt requests/limits** — không có thì 1 pod ngốn RAM có thể làm chết cả node:
   ```yaml
   resources:
     requests: { cpu: 100m, memory: 128Mi }   # scheduler dùng để đặt pod
     limits:   { cpu: 500m, memory: 256Mi }   # trần, vượt RAM → OOMKilled
   ```
3. **HPA dựa trên metric thật** (CPU, hoặc custom metric như request/s).
4. **PodDisruptionBudget** để khi bảo trì node không tắt quá nhiều pod cùng lúc.

### 💡 Bổ sung thực tế: liveness vs readiness (lỗi cấu hình hay gặp)

- **Phân biệt sống còn:**
  | Probe | Hỏi gì | Fail thì sao |
  |---|---|---|
  | **readiness** | "sẵn sàng nhận traffic chưa?" | tạm gỡ pod khỏi Service (không nhận request), KHÔNG restart |
  | **liveness** | "còn sống không, hay treo?" | **restart pod** |
  | **startup** | "khởi động xong chưa?" | hoãn 2 probe kia cho app khởi động chậm |
- **Lỗi cấu hình kinh điển:** đặt liveness probe quá gắt → app đang bận xử lý bị tưởng "chết" → K8s restart → vòng lặp restart vô tận (CrashLoopBackOff). Readiness mới là cái dùng để "tạm ngừng nhận traffic".
- **requests vs limits:** **requests** = K8s dùng để **đặt chỗ** (scheduling). **limits** = trần cứng. Vượt limit RAM → pod bị **OOMKilled**; vượt limit CPU → bị **throttle** (chậm, không chết).
- **HPA cần Metrics Server** — không cài thì HPA hiện `<unknown>` và không scale. Đây là lỗi đầu tiên ai cũng gặp khi thử HPA.

### 📝 Bài ôn tập & Demo đối chiếu

- **Bài ôn:** phân biệt liveness và readiness probe.
- requests và limits khác nhau thế nào?
- HPA tự động làm gì khi CPU tăng cao?

| Demo đối chiếu | Kết quả mong đợi |
|---|---|
| Cấu hình probe | `kubectl describe pod` hiện probe, pod chỉ nhận traffic khi Ready |
| Đặt requests/limits | `kubectl describe` hiện CPU/Memory limits |
| Bật HPA | `kubectl get hpa`; tăng tải → số pod tự tăng |

✅ **Kết quả đạt được:** Cấu hình health check, giới hạn tài nguyên và autoscaling — vận hành K8s production.

---

## Ngày 42 — Helm: Package Manager cho Kubernetes

> ⏱️ ~90 phút · Loại: Kubernetes

### 📘 Lý thuyết

- **Vấn đề:** quản lý nhiều file YAML lặp lại, khó tái sử dụng giữa các môi trường.
- **Helm:** "apt cho Kubernetes" — đóng gói ứng dụng K8s thành **Chart**.
- **Cấu trúc Chart:** `Chart.yaml`, `values.yaml`, `templates/` (YAML có biến).
- **Templating:** dùng `{{ .Values.xxx }}` để tham số hóa.
- **Lệnh:** `helm install`, `helm upgrade`, `helm rollback`, `helm uninstall`, `helm list`.
- **Repository:** kho chart công khai (Artifact Hub); cài app phổ biến chỉ 1 lệnh.
- **values.yaml:** ghi đè cấu hình cho từng môi trường (dev/prod).

### 🧪 Lab cơ bản

1. Cài Helm, thêm repo: `helm repo add bitnami ...`.
2. Cài 1 app có sẵn (vd nginx hoặc postgresql) qua Helm chart.
3. Tạo Helm chart cho app của bạn: `helm create my-chart`.
4. Tham số hóa image và replica trong `values.yaml`, deploy bằng `helm install`.
5. Thực hành `helm upgrade` (đổi giá trị) và `helm rollback`.

### 🚀 Lab nâng cao (best-practice)

> Mục tiêu: dùng Helm để 1 chart deploy được nhiều môi trường, nâng cấp/rollback an toàn.

1. **1 chart + nhiều values file cho mỗi môi trường:**
   ```bash
   helm install web ./chart -f values-dev.yaml
   helm upgrade web ./chart -f values-prod.yaml   # cùng chart, config khác
   ```
2. **`helm diff` trước khi upgrade** (plugin) — xem chính xác sẽ đổi gì, như `terraform plan`.
3. **`helm lint` + `helm template`** để validate chart trước khi deploy.
4. **Versioning chart** (`Chart.yaml`) + đẩy lên chart repo riêng cho team.

### 💡 Bổ sung thực tế: Helm vs Kustomize & bẫy upgrade

- **Helm giải quyết:** YAML lặp lại + tham số hóa + đóng gói + version + rollback. 1 chart deploy được dev/staging/prod chỉ bằng values khác nhau.
- **Helm vs Kustomize** (2 cách quản YAML phổ biến):
  | | Cách tiếp cận | Phù hợp |
  |---|---|---|
  | **Helm** | template + biến | app phức tạp, đóng gói phân phối, nhiều môi trường |
  | **Kustomize** | overlay/patch YAML thuần | đơn giản hơn, tích hợp sẵn `kubectl -k` |
- **Bẫy `helm upgrade`:** nó áp dụng thay đổi ngay — luôn `helm diff upgrade` hoặc `--dry-run` trước. Và `helm rollback <release> <revision>` cứu bạn khi upgrade hỏng.
- **Cài app phổ biến trong 1 lệnh:** Prometheus, Grafana, PostgreSQL, ingress-nginx... đều có chart sẵn. Đây là cách bạn sẽ cài monitoring stack ở Ngày 44.

### 📝 Bài ôn tập & Demo đối chiếu

- **Bài ôn:** Helm giải quyết vấn đề gì so với `kubectl apply` nhiều file?
- `values.yaml` và `templates/` quan hệ thế nào?
- Viết lệnh cài 1 chart với tên release tùy chỉnh.

| Demo đối chiếu | Kết quả mong đợi |
|---|---|
| Cài app bằng Helm | `helm install` → STATUS: deployed |
| Liệt kê release | `helm list` hiện release của bạn |
| Nâng cấp & rollback | `helm upgrade` rồi `helm rollback` chạy thành công |

✅ **Kết quả đạt được:** Đóng gói và quản lý ứng dụng K8s bằng Helm — chuẩn công nghiệp.

---

## Ngày 43 — GitOps: ArgoCD & Triển khai khai báo

> ⏱️ ~90 phút · Loại: GitOps

### 📘 Lý thuyết

- **GitOps:** Git là **nguồn chân lý duy nhất**; trạng thái cluster luôn đồng bộ với repo.
- **Nguyên tắc:** mọi thay đổi qua Git (PR) → tool tự đồng bộ vào cluster.
- **ArgoCD:** công cụ GitOps phổ biến, liên tục so sánh repo với cluster và tự sync.
- **Lợi ích:** audit (lịch sử Git), rollback dễ, không cần cấp quyền cluster cho CI.
- **Pull-based vs push-based deployment.**
- **Application CRD trong ArgoCD:** trỏ tới repo + path + cluster đích.
- **Drift detection:** phát hiện khi cluster lệch khỏi Git và tự sửa.

### 🧪 Lab cơ bản

1. Cài ArgoCD vào cluster minikube, truy cập UI.
2. Tạo repo Git chứa manifest K8s của app.
3. Tạo ArgoCD Application trỏ tới repo, để nó tự sync.
4. Sửa manifest trong Git (đổi replica), commit, quan sát ArgoCD tự áp dụng.
5. Thử thay đổi trực tiếp trên cluster và xem ArgoCD phát hiện drift.

### 🚀 Lab nâng cao (best-practice)

> Mục tiêu: dựng luồng GitOps thật — Git là nguồn sự thật, ArgoCD tự đồng bộ.

1. **Repo cấu hình tách khỏi repo code** (chuẩn GitOps): repo `app` chứa code + CI build image; repo `config` chứa manifest/Helm → ArgoCD theo dõi repo config.
2. **Auto-sync + self-heal:**
   ```yaml
   syncPolicy:
     automated: { prune: true, selfHeal: true }   # tự đồng bộ + tự sửa drift
   ```
3. **App of Apps pattern** — 1 ArgoCD Application quản lý nhiều app con.
4. **Tách quyền:** CI chỉ build/push image + cập nhật tag trong repo config; **không** CI nào có quyền vào cluster → bảo mật tốt hơn push-based.

### 💡 Bổ sung thực tế: GitOps khác CI/CD truyền thống thế nào

- **Push vs Pull:**
  | | CI/CD truyền thống (push) | GitOps (pull) |
  |---|---|---|
  | Ai deploy | CI có credential vào cluster, đẩy lên | Agent (ArgoCD) **trong** cluster tự kéo từ Git |
  | Bảo mật | CI cần quyền cluster (rủi ro) | Cluster không lộ credential ra ngoài |
  | Drift | không tự phát hiện | tự phát hiện + sửa (self-heal) |
  | Rollback | re-run pipeline | `git revert` → tự sync về |
- **Git là nguồn chân lý:** trạng thái cluster = đúng những gì trong Git. Ai đó sửa tay trên cluster (`kubectl edit`) → ArgoCD phát hiện **drift** và kéo về đúng Git. → không còn "cấu hình bí ẩn không ai biết từ đâu".
- **Audit miễn phí:** mọi thay đổi production = 1 commit Git, có tác giả, thời gian, lý do (PR). Khi sự cố: `git log` trên repo config cho biết chính xác ai đổi gì lúc nào.
- **Rollback = git revert:** quay về trạng thái cũ chỉ là revert commit → ArgoCD tự sync. Đơn giản và an toàn nhất trong các phương pháp.

### 📝 Bài ôn tập & Demo đối chiếu

- **Bài ôn:** GitOps khác CI/CD truyền thống ở điểm nào?
- Vì sao Git là "nguồn chân lý" giúp rollback dễ?
- Drift detection làm gì?

| Demo đối chiếu | Kết quả mong đợi |
|---|---|
| ArgoCD đồng bộ từ Git | UI ArgoCD hiện app Synced + Healthy |
| Sửa manifest trên Git | ArgoCD tự phát hiện và đồng bộ thay đổi |
| Tự phục hồi khi lệch | Đổi thủ công trên cụm → ArgoCD kéo về đúng Git |

✅ **Kết quả đạt được:** Áp dụng GitOps với ArgoCD — phương pháp triển khai hiện đại nhất.

---

## Ngày 44 — Monitoring: Prometheus & Metrics

> ⏱️ ~90 phút · Loại: Monitoring

### 📘 Lý thuyết

- **3 trụ cột observability:** Metrics (số đo), Logs (nhật ký), Traces (dấu vết request).
- **Prometheus:** hệ thống thu thập & lưu metric dạng time-series, **kéo (pull)** metric từ target.
- **Exporter:** node-exporter (metric hệ thống), cAdvisor (container), app tự expose `/metrics`.
- **PromQL:** ngôn ngữ truy vấn metric (`rate`, `sum`, `avg`...).
- **Alerting:** Alertmanager gửi cảnh báo khi metric vượt ngưỡng.
- **Khái niệm:** counter, gauge, histogram, summary.
- **Service discovery:** Prometheus tự tìm target trong K8s.

### 🧪 Lab cơ bản

1. Chạy Prometheus + node-exporter bằng Docker Compose (hoặc Helm trên K8s).
2. Truy cập Prometheus UI, chạy vài truy vấn PromQL cơ bản (`up`, `node_memory...`).
3. Quan sát metric CPU/RAM của hệ thống.
4. Cấu hình 1 alert rule đơn giản (vd CPU > 80%).
5. (K8s) Cài `kube-prometheus-stack` bằng Helm để giám sát cluster.

### 🚀 Lab nâng cao (best-practice)

> Mục tiêu: dựng monitoring stack chuẩn cho cả hệ thống + hiểu PromQL đủ để điều tra.

1. **Cài cả stack bằng Helm** (Prometheus + Grafana + Alertmanager + exporters):
   ```bash
   helm install monitoring prometheus-community/kube-prometheus-stack
   ```
2. **App tự expose `/metrics`** (instrument bằng client library) — đo metric nghiệp vụ (request/s, latency, lỗi), không chỉ CPU/RAM.
3. **PromQL điều tra:**
   ```promql
   rate(http_requests_total[5m])                          # request/s
   histogram_quantile(0.95, rate(http_duration_bucket[5m]))  # p95 latency
   sum(rate(http_requests_total{status=~"5.."}[5m]))     # tỉ lệ lỗi 5xx
   ```
4. **Alert rule có ý nghĩa** (dựa trên triệu chứng người dùng thấy, không phải mọi dao động nhỏ).

### 💡 Bổ sung thực tế: pull model & loại metric

- **Vì sao Prometheus dùng pull (kéo):** Prometheus tự đi "hỏi" từng target qua HTTP `/metrics`. Lợi: tự biết target nào chết (scrape fail = down), không cần target biết địa chỉ Prometheus, dễ debug (mở `/metrics` xem trực tiếp). Push model (như StatsD) hợp cho job ngắn hạn → dùng Pushgateway.
- **4 loại metric:**
  | Loại | Ý nghĩa | Ví dụ |
  |---|---|---|
  | **Counter** | chỉ tăng | tổng số request, tổng lỗi |
  | **Gauge** | lên xuống | RAM dùng, số kết nối hiện tại, nhiệt độ |
  | **Histogram** | phân phối theo bucket | phân bố latency (tính p95, p99) |
  | **Summary** | tương tự histogram, tính quantile phía client | |
- **Counter dùng với `rate()`:** counter luôn tăng nên giá trị thô vô nghĩa; `rate(counter[5m])` = tốc độ tăng/giây = thứ bạn thực sự quan tâm.
- **Đừng alert mọi thứ:** alert quá nhiều = "alert fatigue", người ta tắt thông báo. Alert dựa trên **4 golden signals** (Ngày 45) và triệu chứng người dùng cảm nhận được.

### 📝 Bài ôn tập & Demo đối chiếu

- **Bài ôn:** 3 trụ cột observability là gì?
- Prometheus dùng cơ chế pull hay push?
- Phân biệt counter và gauge.

| Demo đối chiếu | Kết quả mong đợi |
|---|---|
| Prometheus thu thập metrics | UI, query `up` → giá trị 1 cho target |
| Xem targets | Status > Targets tất cả State UP |
| Truy vấn 1 metric | PromQL trả về biểu đồ/giá trị (vd node_cpu...) |

✅ **Kết quả đạt được:** Thu thập và truy vấn metric với Prometheus — nền tảng giám sát.

---

## Ngày 45 — Monitoring: Grafana Dashboard

> ⏱️ ~90 phút · Loại: Monitoring

### 📘 Lý thuyết

- **Grafana:** công cụ trực quan hóa, tạo dashboard từ nhiều nguồn dữ liệu (Prometheus, Loki...).
- **Data source:** kết nối Grafana với Prometheus.
- **Panel:** biểu đồ (graph, gauge, stat, table) hiển thị metric.
- **Dashboard có sẵn:** import từ Grafana.com bằng ID (vd Node Exporter Full).
- **Variable & template:** dashboard động chọn theo host/service.
- **Alerting trong Grafana:** cảnh báo trực quan, gửi qua nhiều kênh.
- **Best practice:** dashboard cho **4 golden signals** (latency, traffic, errors, saturation).

### 🧪 Lab cơ bản

1. Chạy Grafana (Docker/Helm), kết nối data source Prometheus.
2. Import dashboard Node Exporter Full (ID 1860) để xem metric hệ thống.
3. Tự tạo 1 dashboard với 3 panel: CPU, RAM, disk.
4. Cấu hình 1 alert trong Grafana khi RAM vượt ngưỡng.
5. Thêm variable để chọn server/instance trên dashboard.

### 🚀 Lab nâng cao (best-practice)

> Mục tiêu: dashboard có ý nghĩa vận hành (golden signals), alert gửi đến đúng kênh.

1. **Dashboard theo 4 golden signals** thay vì nhồi mọi metric:
   - **Latency** (p50/p95/p99) · **Traffic** (request/s) · **Errors** (tỉ lệ 5xx) · **Saturation** (CPU/RAM/disk %).
2. **Alert gửi đến kênh thật** (Slack/Telegram/email) qua contact point — alert không ai thấy = vô dụng.
3. **Dùng variable** (`$instance`, `$namespace`) để 1 dashboard xem được mọi service.
4. **Provisioning dashboard bằng code** (JSON trong Git) — dashboard cũng nên là IaC, không tạo tay.

### 💡 Bổ sung thực tế: 4 golden signals & dashboard cho người, không cho máy

- **4 Golden Signals (Google SRE)** — nếu chỉ theo dõi 4 thứ, hãy chọn 4 cái này:
  | Tín hiệu | Trả lời câu hỏi |
  |---|---|
  | **Latency** | request mất bao lâu? (tách thành công vs lỗi) |
  | **Traffic** | hệ thống đang chịu tải bao nhiêu? |
  | **Errors** | tỉ lệ request thất bại? |
  | **Saturation** | tài nguyên "đầy" đến đâu? (CPU/RAM/disk/queue) |
- **Grafana + Prometheus phối hợp:** Prometheus **lưu + truy vấn** số liệu; Grafana **vẽ + cảnh báo**. Grafana không lưu metric, nó hỏi Prometheus.
- **Dashboard tốt kể một câu chuyện:** nhìn vào là biết "hệ thống có khỏe không" trong 5 giây. Dashboard 50 panel lộn xộn = không ai nhìn. Bắt đầu từ golden signals, đào sâu khi cần.
- **Alert nên gắn với SLO** (Ngày 51): alert khi sắp vi phạm cam kết với người dùng, không phải khi CPU nhích lên 60%.

### 📝 Bài ôn tập & Demo đối chiếu

- **Bài ôn:** Grafana và Prometheus phối hợp thế nào?
- 4 golden signals là gì?
- Vì sao trực quan hóa metric quan trọng cho vận hành?

| Demo đối chiếu | Kết quả mong đợi |
|---|---|
| Grafana kết nối Prometheus | Data source: Test → working |
| Tạo dashboard | Panel hiển thị CPU/RAM theo thời gian thực |
| Import dashboard có sẵn | Nhập ID → biểu đồ hiện ngay |

✅ **Kết quả đạt được:** Xây dashboard giám sát trực quan với Grafana — kỹ năng SRE/DevOps.

---

## Ngày 46 — Logging tập trung: Loki

> ⏱️ ~90 phút · Loại: Monitoring

### 📘 Lý thuyết

- **Vấn đề:** log nằm rải rác trên nhiều container/server → cần tập trung.
- **Loki:** hệ thống tổng hợp log của Grafana, nhẹ, index theo **label** (như Prometheus cho log).
- **Promtail/agent:** thu thập log và đẩy về Loki.
- **ELK/EFK stack** (Elasticsearch + Logstash/Fluentd + Kibana): giải pháp truyền thống mạnh mẽ.
- **LogQL:** truy vấn log trong Loki.
- **Cấu trúc log:** nên log dạng JSON có cấu trúc để dễ query.
- **Tổng quan log + metric trong Grafana** để debug nhanh.

### 🧪 Lab cơ bản

1. Chạy Loki + Promtail + Grafana bằng Docker Compose.
2. Cấu hình Promtail thu thập log của các container.
3. Trong Grafana, thêm data source Loki và xem log.
4. Dùng LogQL lọc log theo label và tìm dòng `error`.
5. Tạo dashboard kết hợp metric (Prometheus) và log (Loki).

### 🚀 Lab nâng cao (best-practice)

> Mục tiêu: gom log toàn hệ thống về một nơi, query nhanh, gắn với metric để debug.

1. **Structured logging (JSON)** từ app — mỗi log là object có field (level, request_id, user...) → query chính xác:
   ```json
   {"level":"error","msg":"db timeout","request_id":"abc","duration_ms":5200}
   ```
2. **LogQL kết hợp lọc + đếm:**
   ```logql
   {app="api"} |= "error" | json | duration_ms > 1000   # log lỗi chậm > 1s
   sum(rate({app="api"} |= "error" [5m]))                # tốc độ lỗi
   ```
3. **Correlation:** thêm `request_id`/`trace_id` vào log → lần theo 1 request qua nhiều service.
4. **Retention + giới hạn dung lượng** — log vô hạn = đầy đĩa; đặt chính sách giữ log hợp lý.

### 💡 Bổ sung thực tế: Loki vs ELK & vì sao log có cấu trúc

- **Loki khác Elasticsearch ở triết lý index:** Loki **chỉ index label** (như Prometheus), nội dung log không index → nhẹ, rẻ, nhanh để vận hành. ELK index **toàn văn** → tìm kiếm mạnh hơn nhưng nặng, tốn tài nguyên. Loki hợp khi đã dùng Grafana/Prometheus; ELK hợp khi cần phân tích log sâu.
- **Vì sao log JSON có cấu trúc:** log text thô (`"Error: something at line 5"`) khó query. Log JSON cho phép lọc theo field chính xác (`level=error AND user_id=123`). → app production nên log JSON.
- **3 trụ cột phối hợp:** **Metric** cho biết *"có gì đó sai"* (alert), **Log** cho biết *"sai cái gì"* (chi tiết lỗi), **Trace** cho biết *"sai ở đâu trong chuỗi service"*. Gom cả 3 vào Grafana = debug nhanh.
- **Đừng log secret/PII:** log thường lưu lâu, ai cũng đọc được — không bao giờ log mật khẩu, token, thông tin cá nhân.

### 📝 Bài ôn tập & Demo đối chiếu

- **Bài ôn:** vì sao cần logging tập trung?
- Loki khác Elasticsearch ở cách index thế nào?
- Vì sao nên log dạng JSON có cấu trúc?

| Demo đối chiếu | Kết quả mong đợi |
|---|---|
| Loki nhận log | Trong Grafana Explore, chọn Loki thấy log chạy về |
| Truy vấn log theo nhãn | `{app="myapp"}` lọc đúng log của app |
| Gộp log nhiều service | Xem được log tập trung từ các container |

✅ **Kết quả đạt được:** Tập trung và truy vấn log toàn hệ thống — hoàn thiện observability.

---

## Ngày 47 — Configuration Management: Ansible

> ⏱️ ~90 phút · Loại: IaC

### 📘 Lý thuyết

- **Ansible:** tự động cấu hình server (cài phần mềm, sửa config) — **agentless**, dùng SSH.
- **Khác Terraform:** Terraform **tạo** hạ tầng, Ansible **cấu hình bên trong** server (bổ trợ nhau).
- **Inventory:** danh sách server cần quản lý (file INI/YAML).
- **Playbook:** file YAML mô tả các task cần thực hiện.
- **Module:** đơn vị tác vụ (`apt`, `copy`, `service`, `template`...).
- **Idempotent:** chạy lại không gây thay đổi nếu đã ở trạng thái mong muốn.
- **Role:** tổ chức playbook tái sử dụng; Ansible Galaxy chia sẻ role.

### 🧪 Lab cơ bản

1. Cài Ansible, tạo inventory trỏ tới VM (hoặc localhost).
2. Viết playbook cài nginx và khởi động dịch vụ.
3. Chạy playbook 2 lần, quan sát tính idempotent (lần 2 không thay đổi).
4. Dùng module `template` đẩy 1 file cấu hình có biến lên server.
5. Tổ chức playbook thành role đơn giản.

### 🚀 Lab nâng cao (best-practice)

> Mục tiêu: viết playbook idempotent, có cấu trúc role, dùng vault cho secret.

1. **Playbook idempotent đúng cách** — dùng module chuyên dụng, không `command`/`shell` bừa:
   ```yaml
   - name: Cài và chạy nginx
     hosts: web
     become: true
     tasks:
       - apt: { name: nginx, state: present, update_cache: true }
       - service: { name: nginx, state: started, enabled: true }
       - template: { src: nginx.conf.j2, dest: /etc/nginx/nginx.conf }
         notify: reload nginx
     handlers:
       - name: reload nginx
         service: { name: nginx, state: reloaded }
   ```
2. **Ansible Vault** mã hóa secret trong playbook: `ansible-vault encrypt secrets.yml`.
3. **Cấu trúc role chuẩn** (`roles/web/{tasks,templates,handlers,defaults}`) để tái dùng.
4. **`--check` (dry-run) + `--diff`** xem thay đổi trước khi áp dụng thật.

### 💡 Bổ sung thực tế: Terraform vs Ansible & "agentless"

- **Terraform và Ansible bổ trợ, không cạnh tranh:**
  | | Vai trò | Câu hỏi |
  |---|---|---|
  | **Terraform** | provisioning hạ tầng | "tạo 3 VM, 1 network, 1 load balancer" |
  | **Ansible** | configuration management | "cài nginx + cấu hình + chạy service trên 3 VM đó" |
  - Luồng thật: Terraform dựng máy → Ansible cấu hình bên trong. (Thời container/K8s, vai trò Ansible giảm cho app mới, nhưng vẫn rất mạnh cho cấu hình OS/server truyền thống.)
- **Agentless là lợi thế lớn:** Ansible chỉ cần SSH + Python trên target, **không cài agent**. Khác Puppet/Chef (cần agent + master). → dễ bắt đầu, dễ áp dụng cho server có sẵn.
- **Idempotent là cốt lõi:** chạy playbook 10 lần phải ra cùng kết quả, lần 2+ báo `changed=0`. Đây là lý do dùng module (`apt`, `service`) thay vì `shell` — module biết kiểm tra trạng thái trước khi hành động.
- **Khi nào dùng Ansible thời K8s:** cấu hình node OS, cài đặt bootstrap cluster, quản lý server không-container, chạy các tác vụ vận hành hàng loạt (patch 50 server).

### 📝 Bài ôn tập & Demo đối chiếu

- **Bài ôn:** Terraform và Ansible khác vai trò thế nào?
- Idempotent quan trọng vì sao trong cấu hình server?
- Inventory và Playbook là gì?

| Demo đối chiếu | Kết quả mong đợi |
|---|---|
| Ansible ping được host | `ansible all -m ping` → SUCCESS / pong |
| Chạy playbook | PLAY RECAP → ok=N changed=N failed=0 |
| Idempotent (chạy lại) | Lần 2: changed=0 |

✅ **Kết quả đạt được:** Tự động cấu hình server hàng loạt bằng Ansible — bổ trợ hoàn hảo cho Terraform.

---

## Ngày 48 — Terraform nâng cao: Module, Remote State & Workspace

> ⏱️ ~90 phút · Loại: IaC

### 📘 Lý thuyết

- **Module:** đóng gói tài nguyên tái sử dụng (như hàm); module riêng và từ registry.
- **Remote state:** lưu tfstate trên S3 (hoặc tương đương) + khóa bằng DynamoDB → làm việc nhóm an toàn.
- **State locking:** tránh 2 người apply cùng lúc gây hỏng state.
- **Workspace:** quản lý nhiều môi trường (dev/staging/prod) từ cùng code.
- **Variables nâng cao:** tfvars, biến nhạy cảm, validation.
- **Data source:** tham chiếu tài nguyên đã tồn tại.
- **`terraform fmt` & `validate`; tích hợp Terraform vào CI/CD.**

### 🧪 Lab cơ bản

1. Tách hạ tầng thành module (vd module mạng, module compute).
2. Cấu hình remote state trên S3 với DynamoDB lock.
3. Dùng workspace tạo môi trường dev và prod từ cùng code.
4. Dùng tfvars truyền biến khác nhau cho mỗi môi trường.
5. Thêm bước `terraform plan` vào pipeline CI để review thay đổi hạ tầng.

### 🚀 Lab nâng cao (best-practice)

> Mục tiêu: cấu trúc Terraform quy mô lớn — module tái dùng, state remote khóa, plan trong CI.

1. **Module tái dùng + tham số hóa:**
   ```hcl
   module "web_server" {
     source        = "./modules/compute"
     instance_type = var.instance_type
     environment   = terraform.workspace
   }
   ```
2. **Remote state + locking** (đã giới thiệu Ngày 29) — bắt buộc cho team.
3. **Tách môi trường:** mỗi env một state key/folder + tfvars riêng (nhiều team dùng folder thay vì workspace cho rõ ràng).
4. **Terraform trong CI/CD:** PR chạy `fmt` + `validate` + `plan` (comment plan vào PR); merge main chạy `apply` (có approval). Quét `tfsec`/`checkov` tìm cấu hình sai bảo mật.

### 💡 Bổ sung thực tế: tổ chức Terraform khi dự án lớn lên

- **Module = hàm cho hạ tầng:** thay vì copy-paste cấu hình VM 10 lần, viết 1 module `compute` rồi gọi với tham số khác nhau. DRY (Don't Repeat Yourself) cho hạ tầng.
- **Remote state giải quyết bài toán team:** state local = chỉ 1 người dùng được, dễ mất, dễ xung đột. Remote state (S3/GCS/Terraform Cloud) + **locking** = cả team làm chung an toàn, không ai apply đè ai.
- **Workspace vs thư mục riêng** (tranh luận thật trong ngành):
  - **Workspace:** nhẹ, cùng code khác state — dễ nhầm apply nhầm môi trường.
  - **Thư mục riêng** (`environments/dev`, `environments/prod`): rõ ràng hơn, khó nhầm, nhiều team production chọn cách này.
- **`plan` trong CI là "code review cho hạ tầng":** reviewer thấy chính xác PR sẽ tạo/xóa gì trên cloud trước khi merge — chặn được những `destroy` thảm họa.

### 📝 Bài ôn tập & Demo đối chiếu

- **Bài ôn:** vì sao cần remote state khi làm việc nhóm?
- Module giúp ích gì cho việc tái sử dụng?
- Workspace giải quyết bài toán nhiều môi trường thế nào?

| Demo đối chiếu | Kết quả mong đợi |
|---|---|
| Tách module Terraform | Module dùng lại được, `plan` sạch |
| Lưu state remote | State nằm trên backend, không phải local |
| Dùng workspace | `terraform workspace list` hiện dev/prod |

✅ **Kết quả đạt được:** Quản lý hạ tầng quy mô lớn với Terraform module, remote state, đa môi trường.

---

## Ngày 49 — Bảo mật DevSecOps & Best Practices

> ⏱️ ~90 phút · Loại: Security

### 📘 Lý thuyết

- **DevSecOps:** tích hợp bảo mật vào toàn bộ pipeline (**shift-left security**).
- **Quét lỗ hổng:** image scanning (Trivy), dependency scanning (SCA), SAST (quét code).
- **Secret management:** Vault, cloud Secrets Manager — không bao giờ hard-code secret.
- **Least privilege:** IAM role tối thiểu, RBAC trong K8s.
- **Supply chain security:** ký image (cosign), SBOM (danh mục thành phần).
- **Network policy trong K8s:** kiểm soát luồng traffic giữa pod.
- **Compliance & audit:** log mọi thay đổi, quét cấu hình sai (tfsec, kube-bench).

### 🧪 Lab cơ bản

1. Tích hợp Trivy vào pipeline CI để quét lỗ hổng image, fail nếu có lỗi nghiêm trọng.
2. Quét dependency của app tìm lỗ hổng đã biết.
3. Tạo K8s NetworkPolicy giới hạn pod backend chỉ nhận traffic từ frontend.
4. Cấu hình RBAC: tạo role chỉ đọc trong namespace.
5. Chạy tfsec quét cấu hình Terraform tìm vấn đề bảo mật.

### 🚀 Lab nâng cao (best-practice)

> Mục tiêu: nhúng bảo mật vào mọi tầng — code, image, hạ tầng, runtime.

1. **Quét nhiều tầng trong CI** (mỗi PR):
   ```yaml
   - run: trivy fs --severity HIGH,CRITICAL --exit-code 1 .   # dependency + secret
   - run: trivy image --severity CRITICAL --exit-code 1 myapp # lỗ hổng image
   - run: tfsec ./infra                                        # cấu hình IaC sai
   ```
2. **NetworkPolicy deny-by-default** trong K8s — pod chỉ nói chuyện với pod được phép.
3. **RBAC least privilege** — mỗi service account chỉ quyền tối thiểu; không dùng `cluster-admin` bừa.
4. **Ký image (cosign) + SBOM** — đảm bảo image chạy đúng là image bạn build, biết rõ thành phần bên trong.

### 💡 Bổ sung thực tế: shift-left & 4 loại quét

- **Shift-left nghĩa là gì:** đẩy bảo mật **sớm** về phía dev (trái của pipeline) thay vì kiểm tra cuối (phải). Phát hiện lỗ hổng lúc code/PR rẻ hơn nghìn lần so với lúc đã lên production. Lỗ hổng nằm càng lâu càng đắt để sửa.
- **4 loại quét trong pipeline:**
  | Loại | Quét gì | Công cụ |
  |---|---|---|
  | **SCA** | thư viện/dependency có CVE | Trivy, Dependabot, Snyk |
  | **SAST** | lỗ hổng trong code của bạn | Semgrep, CodeQL |
  | **Image scan** | lỗ hổng trong image OS/lib | Trivy, Grype |
  | **IaC scan** | cấu hình hạ tầng sai (S3 public...) | tfsec, checkov, kube-bench |
  | **Secret scan** | secret lỡ commit | gitleaks, trufflehog |
- **Defense in depth (phòng thủ nhiều lớp):** firewall (SG/UFW) → NetworkPolicy → RBAC → least privilege → image scan → secret management. Không lớp nào đủ một mình; nhiều lớp cộng lại mới an toàn.
- **Supply chain là mặt trận mới:** tấn công qua dependency/image bị nhiễm độc ngày càng nhiều. Ghim version, quét, ký image, dùng SBOM để biết chính xác bạn đang chạy gì.

### 📝 Bài ôn tập & Demo đối chiếu

- **Bài ôn:** "shift-left security" nghĩa là gì?
- Liệt kê 3 loại quét bảo mật trong pipeline.
- RBAC và NetworkPolicy bảo vệ cluster thế nào?

| Demo đối chiếu | Kết quả mong đợi |
|---|---|
| Quét lỗ hổng image | `trivy image myapp` → bảng CVE theo mức độ |
| Không hard-code secret | Secret trong vault/secret manager, không trong code |
| Quét secret trong repo | Công cụ scan báo sạch, không lộ key |

✅ **Kết quả đạt được:** Tích hợp bảo mật vào pipeline và hạ tầng — tư duy DevSecOps.

---

## Ngày 50 — MILESTONE: LAB tổng hợp Giai đoạn 3

> ⏱️ ~150 phút · Loại: Milestone

### 📘 Lý thuyết — Tổng kết

- **Mạch kiến thức:** CI/CD → Kubernetes → Helm → GitOps → Monitoring (Prometheus/Grafana/Loki) → Ansible → Terraform nâng cao → DevSecOps.
- **Bạn đã có toàn bộ kỹ năng của 1 DevOps Engineer hiện đại.**
- **Kiến trúc hoàn chỉnh:** Code → CI (test+scan) → build image → push → GitOps deploy K8s → monitor → alert.

### 🧪 Lab cơ bản (Milestone)

1. Ghép tất cả: pipeline CI build+scan image → push → ArgoCD deploy lên K8s → Prometheus/Grafana giám sát.
2. Dùng Helm chart cho app, Terraform tạo cluster/hạ tầng, Ansible cấu hình node (nếu cần).
3. Thiết lập dashboard giám sát và 1 alert hoạt động.
4. Toàn bộ trong monorepo có cấu trúc rõ ràng + README + sơ đồ kiến trúc.
5. Tự đánh giá theo checklist năng lực DevOps đầy đủ.

### 🚀 Lab nâng cao (best-practice) — Mô hình DevOps hoàn chỉnh

**Mô hình hệ thống DevOps end-to-end:**
```
  Dev ──push──▶ GitHub (app repo)
                  │
        ┌─────────▼──────────┐
        │ CI: lint→test→scan │  (Trivy, tfsec, SAST)
        │ build image (SHA)  │
        │ push → registry    │
        │ cập nhật tag →      │──▶ GitHub (config repo: Helm/manifests)
        └────────────────────┘             │
                                  ┌─────────▼─────────┐
                                  │  ArgoCD (GitOps)  │ tự sync
                                  └─────────┬─────────┘
                          ┌────────────────▼─────────────────┐
                          │       Kubernetes Cluster          │
                          │  (Terraform tạo, Helm deploy app) │
                          │  app + ingress + HPA + probe      │
                          └────────────────┬──────────────────┘
                                           │ scrape metrics + logs
                          ┌────────────────▼──────────────────┐
                          │  Prometheus + Grafana + Loki       │
                          │  dashboard (golden signals) + alert│
                          └────────────────────────────────────┘
```

**Yêu cầu best-practice:**
1. **CI có quét bảo mật** (shift-left), image tag bất biến.
2. **GitOps (ArgoCD)** — Git là nguồn sự thật, không CI nào có credential cluster.
3. **K8s có probe + resource limits + HPA.**
4. **Monitoring đủ 3 trụ cột** (metric/log + alert đến kênh thật).
5. **Hạ tầng bằng Terraform** (module + remote state), README có sơ đồ.

### 📝 Bài ôn tập & Demo đối chiếu

- **Tự chấm:** bạn vận hành được vòng đời DevOps hoàn chỉnh từ code đến giám sát chưa?
- **Mở rộng:** thêm logging Loki vào hệ thống giám sát.
- Chuẩn bị giai đoạn cuối: SRE, project tốt nghiệp và định hướng nghề.

| Demo đối chiếu | Kết quả mong đợi |
|---|---|
| Pipeline + K8s + Monitoring liên hoàn | push → CI/CD → deploy K8s → metrics/log lên Grafana |
| Thấy sức khỏe hệ thống | Dashboard phản ánh deploy mới theo thời gian thực |
| Toàn bộ khai báo trong Git | Hạ tầng + app + pipeline đều version-controlled |

✅ **Kết quả đạt được — MỐC 6:** Làm chủ toàn bộ stack DevOps hiện đại — sẵn sàng cho dự án tốt nghiệp.

---

# 📎 Phụ lục Giai đoạn 3 — Kiến thức sống còn

## Phụ lục A — Lỗi thường gặp (CI/CD · K8s · Monitoring)

| Lỗi kinh điển | Hậu quả | Cách làm đúng |
|---|---|---|
| Deploy bằng tag `latest` | Không biết đang chạy gì, rollback sai | Tag bất biến (SHA/semver) |
| Hard-code secret trong workflow YAML | Lộ secret vĩnh viễn | GitHub Secrets/Environments |
| Liveness probe quá gắt | CrashLoopBackOff (restart vô tận) | Readiness để ngừng traffic; liveness nới lỏng |
| Pod không có resource limits | 1 pod ngốn RAM giết cả node | Luôn đặt requests + limits |
| Tưởng K8s Secret là mã hóa | Lộ secret (chỉ base64) | RBAC + encryption-at-rest + Vault |
| Sửa tay trên cluster (`kubectl edit`) | Drift, mất đồng bộ với Git | Mọi thay đổi qua Git (GitOps) |
| HPA không scale | Quên cài Metrics Server | Cài metrics-server trước |
| Database dùng Deployment | Mất dữ liệu/danh tính | StatefulSet + PVC |
| Alert mọi dao động nhỏ | Alert fatigue → bỏ qua cả alert thật | Alert theo golden signals/SLO |
| NodePort/LoadBalancer cho mọi service | Tốn kém, khó quản | ClusterIP + Ingress |

## Phụ lục B — Playbook xử lý sự cố

**🔴 "Pod không lên / CrashLoopBackOff"**
```bash
kubectl get pods                       # trạng thái: Pending? CrashLoop? ImagePullBackOff?
kubectl describe pod <pod>             # Events ở cuối — lý do thật
kubectl logs <pod> --previous          # log của lần crash trước
# Pending → thiếu tài nguyên/không có node phù hợp
# ImagePullBackOff → sai tên image / thiếu credential registry
# CrashLoop → app lỗi khi khởi động hoặc liveness probe sai
```

**🔴 "Không truy cập được service"**
```bash
kubectl get svc,endpoints              # Service có endpoint không? (không = selector sai)
kubectl get pods --show-labels         # label pod khớp selector của Service?
kubectl port-forward svc/<name> 8080:80  # test trực tiếp, bỏ qua Ingress
kubectl describe ingress <name>        # Ingress route đúng chưa
```

**🔴 "Pipeline CI/CD fail"**
- Đọc log job — bước nào đỏ? (lint? test? build? deploy?)
- `ImagePullBackOff` khi deploy → registry credential / tag sai.
- Deploy SSH fail → kiểm tra Secret (key/host), quyền key.
- Build chậm/hết cache → kiểm tra cấu hình cache layer.

**🔴 "Metric/dashboard không có dữ liệu"**
- Prometheus: Status > Targets — target có UP không? (DOWN = scrape fail)
- App đã expose `/metrics` chưa? `curl pod:port/metrics`
- Grafana: data source Test có "working"? Time range đúng chưa?

**🔴 "ArgoCD OutOfSync / Degraded"**
- `OutOfSync` → có drift hoặc commit mới chưa sync → xem diff trong UI.
- `Degraded` → tài nguyên K8s lỗi (pod CrashLoop...) → đào vào pod.
- `Unknown` → ArgoCD không truy cập được repo/cluster.

## Phụ lục C — Cheat sheet

```text
# KUBECTL HÀNG NGÀY
kubectl get pods -A                    # mọi pod, mọi namespace
kubectl describe pod <p>               # điều tra (Events ở cuối)
kubectl logs -f <p> [--previous]       # log (lần crash trước)
kubectl exec -it <p> -- sh             # vào trong pod
kubectl apply -f . / -k ./overlay      # declarative apply
kubectl rollout undo deploy/<d>        # rollback
kubectl port-forward svc/<s> 8080:80   # test service nội bộ
kubectl get events --sort-by=.lastTimestamp

# HELM
helm install <name> <chart> -f values-prod.yaml
helm diff upgrade <name> <chart>       # xem trước (plugin)
helm rollback <name> <revision>

# CI/CD (GitHub Actions)
# - tag image theo SHA, KHÔNG latest
# - secret trong Secrets/Environments
# - CI mọi PR; CD khi merge main (production có approval)

# MONITORING (PromQL)
rate(http_requests_total[5m])          # request/s
histogram_quantile(0.95, rate(http_duration_bucket[5m]))  # p95
sum(rate(http_requests_total{status=~"5.."}[5m]))         # lỗi 5xx

# TERRAFORM (team)
terraform fmt && terraform validate
terraform plan -out=tfplan             # review trong CI/PR
# remote state + locking BẮT BUỘC khi làm nhóm

# BẢO MẬT (shift-left, chạy trong CI)
trivy image --severity CRITICAL --exit-code 1 <img>
tfsec ./infra ; gitleaks detect
```

> 💬 **Lời khuyên cuối Giai đoạn 3:** Bạn vừa lắp ráp toàn bộ "dây chuyền" DevOps hiện đại: code tự test → tự build → tự deploy → tự giám sát → tự phục hồi. Điểm mấu chốt không phải biết từng công cụ, mà hiểu **chúng ghép vào nhau như thế nào** để tạo một vòng đời khép kín. Giai đoạn 4 sẽ nâng tư duy lên mức **độ tin cậy** (SRE): không chỉ "chạy được" mà "chạy đáng tin ở quy mô lớn", tối ưu chi phí, và gói tất cả vào một dự án tốt nghiệp.

> ➡️ **Tiếp theo — Giai đoạn 4 (Ngày 51–60):** SRE, HA/DR, FinOps, Service Mesh & Dự án tốt nghiệp.
