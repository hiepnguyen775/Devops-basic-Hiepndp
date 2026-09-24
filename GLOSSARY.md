# 📚 GLOSSARY — Từ điển thuật ngữ DevOps

> Toàn bộ thuật ngữ xuất hiện trong khoá học, kèm **ngày học nó**. Bấm vào số ngày để nhảy tới bài giảng đầy đủ.

**364 thuật ngữ** · Trích tự động từ mục 📚 Thuật ngữ của các ngày học.

## Mục lục nhanh

[A](#a) · [B](#b) · [C](#c) · [D](#d) · [E](#e) · [F](#f) · [G](#g) · [H](#h) · [I](#i) · [J](#j) · [K](#k) · [#](#ký-hiệu) · [L](#l) · [M](#m) · [N](#n) · [O](#o) · [P](#p) · [Q](#q) · [R](#r) · [S](#s) · [T](#t) · [U](#u) · [V](#v) · [W](#w) · [Y](#y)

---

## A

| Thuật ngữ | Nghĩa | Học ở |
|---|---|---|
| **ACID** | Đảm bảo giao dịch chính xác | [Ngày 24](./Giai-doan-2-Git-Docker-Cloud.md#ngày-24-cơ-sở-dữ-liệu-cho-devops) |
| **Action (`uses:`)** | Khối dựng sẵn người khác viết, dùng lại bằng một dòng | [Ngày 31](./Giai-doan-3-CICD-K8s-Monitoring.md#ngày-31-cicd-khái-niệm-github-actions-cơ-bản) |
| **Agentless** | Không cần cài gì lên máy đích — chỉ cần SSH + Python | [Ngày 47](./Giai-doan-3-CICD-K8s-Monitoring.md#ngày-47-configuration-management-ansible) |
| **Alert fatigue** | Báo nhiều quá hoá nhờn, đến lúc có sự cố thật thì không ai nhìn | [Ngày 45](./Giai-doan-3-CICD-K8s-Monitoring.md#ngày-45-monitoring-grafana-dashboard) |
| **Alpine** | Bản Linux siêu nhỏ hay dùng làm base | [Ngày 18](./Giai-doan-2-Git-Docker-Cloud.md#ngày-18-docker-image-tối-ưu-multi-stage-build) |
| **AMI / Image** | Ảnh hệ điều hành dùng để tạo máy ảo | [Ngày 27](./Giai-doan-2-Git-Docker-Cloud.md#ngày-27-máy-chủ-cloud-tạo-quản-lý-vm) |
| **Anchor & alias** (`&`, `*`)** | Định nghĩa 1 lần, tái dùng nhiều nơi | [Ngày 22](./Giai-doan-2-Git-Docker-Cloud.md#ngày-22-yaml-json-định-dạng-cấu-hình) |
| **Ansible Vault** | Mã hoá **AES256 thật** — khác hẳn base64 của K8s Secret | [Ngày 47](./Giai-doan-3-CICD-K8s-Monitoring.md#ngày-47-configuration-management-ansible) |
| **App-of-Apps** | Một Application trỏ tới thư mục chứa các Application khác | [Ngày 43](./Giai-doan-3-CICD-K8s-Monitoring.md#ngày-43-gitops-argocd-triển-khai-khai-báo) |
| **Application (CRD)** | Object khai báo: theo dõi repo nào, nhánh nào, thư mục nào, deploy vào đâu | [Ngày 43](./Giai-doan-3-CICD-K8s-Monitoring.md#ngày-43-gitops-argocd-triển-khai-khai-báo) |
| **ArgoCD** | Công cụ GitOps phổ biến nhất cho Kubernetes | [Ngày 43](./Giai-doan-3-CICD-K8s-Monitoring.md#ngày-43-gitops-argocd-triển-khai-khai-báo) |
| **Argument / Parameter** | Tham số truyền vào script (`$1`, `$2`) | [Ngày 5](./Giai-doan-1-Linux-SysOps.md#ngày-5-bash-scripting-cơ-bản) |
| **Array** | Mảng — danh sách nhiều giá trị | [Ngày 6](./Giai-doan-1-Linux-SysOps.md#ngày-6-bash-scripting-nâng-cao-tự-động-hóa) |
| **Artifact** | Gói file lưu lại sau khi job xong — cách duy nhất chuyển đồ giữa các job | [Ngày 31](./Giai-doan-3-CICD-K8s-Monitoring.md#ngày-31-cicd-khái-niệm-github-actions-cơ-bản) |
| **authorized_keys** | File chứa các public key được phép vào server | [Ngày 8](./Giai-doan-1-Linux-SysOps.md#ngày-8-ssh-kết-nối-quản-lý-server-từ-xa) |
| **Automation** | Tự động hoá — để máy làm việc lặp lại thay người | [Ngày 1](./Giai-doan-1-Linux-SysOps.md#ngày-1-devops-sysops-là-gì-tổng-quan-toàn-ngành) |
| **Availability Zone (AZ)** | Một trung tâm dữ liệu riêng biệt bên trong một region | [Ngày 26](./Giai-doan-2-Git-Docker-Cloud.md#ngày-26-làm-quen-cloud-khái-niệm-free-tier) |

## B

| Thuật ngữ | Nghĩa | Học ở |
|---|---|---|
| **Backup / Restore** | Sao lưu / khôi phục | [Ngày 11](./Giai-doan-1-Linux-SysOps.md#ngày-11-lưu-trữ-backup-khôi-phục) |
| **Base image** | Image nền (alpine/slim/distroless) | [Ngày 18](./Giai-doan-2-Git-Docker-Cloud.md#ngày-18-docker-image-tối-ưu-multi-stage-build) |
| **Bastion / Jump host** | Máy trung gian để vào mạng nội bộ | [Ngày 8](./Giai-doan-1-Linux-SysOps.md#ngày-8-ssh-kết-nối-quản-lý-server-từ-xa) |
| **Bind mount** | Gắn thẳng thư mục host vào container | [Ngày 19](./Giai-doan-2-Git-Docker-Cloud.md#ngày-19-docker-volume-network-dữ-liệu-bền-vững) |
| **bisect** | Tìm commit gây bug bằng nhị phân | [Ngày 25](./Giai-doan-2-Git-Docker-Cloud.md#ngày-25-git-nâng-cao-rebase-tag-workflow) |
| **Blackbox probe** | Đo dịch vụ **từ bên ngoài** — đúng góc nhìn người dùng | [Ngày 51](./Giai-doan-4-SRE-Capstone.md#ngày-51-site-reliability-engineering-sre-nguyên-lý) |
| **Brace expansion** `{a,b,c}** | Shell bung thành nhiều tên trước khi chạy lệnh | [Ngày 2](./Giai-doan-1-Linux-SysOps.md#ngày-2-linux-cơ-bản-điều-hướng-quản-lý-file) |
| **Branch** | Nhánh — dòng phát triển song song | [Ngày 14](./Giai-doan-2-Git-Docker-Cloud.md#ngày-14-git-branch-merge-xử-lý-conflict) |
| **Branch protection** | Luật chặn merge vào nhánh chính khi CI chưa xanh | [Ngày 15](./Giai-doan-2-Git-Docker-Cloud.md#ngày-15-github-remote-collaboration-pull-request) · [Ngày 32](./Giai-doan-3-CICD-K8s-Monitoring.md#ngày-32-ci-pipeline-build-test-lint-tự-động) |
| **Build context** | Thư mục gửi cho Docker khi build (dấu `.`) | [Ngày 17](./Giai-doan-2-Git-Docker-Cloud.md#ngày-17-docker-dockerfile-build-image) |
| **Bulkhead** | Chia tách tài nguyên để một phần hỏng không kéo theo phần khác | [Ngày 54](./Giai-doan-4-SRE-Capstone.md#ngày-54-service-mesh-microservices-nâng-cao) |
| **Burn rate** | Tốc độ tiêu ngân sách lỗi = tỉ lệ lỗi hiện tại / tỉ lệ cho phép | [Ngày 51](./Giai-doan-4-SRE-Capstone.md#ngày-51-site-reliability-engineering-sre-nguyên-lý) |

## C

| Thuật ngữ | Nghĩa | Học ở |
|---|---|---|
| **Cache** | Lưu lại thư viện đã tải để lần sau không tải lại — tiết kiệm phút runner | [Ngày 17](./Giai-doan-2-Git-Docker-Cloud.md#ngày-17-docker-dockerfile-build-image) · [Ngày 32](./Giai-doan-3-CICD-K8s-Monitoring.md#ngày-32-ci-pipeline-build-test-lint-tự-động) |
| **Cardinality explosion** | Nhãn động làm số chuỗi bùng nổ và giết Prometheus | [Ngày 44](./Giai-doan-3-CICD-K8s-Monitoring.md#ngày-44-monitoring-prometheus-metrics) |
| **Cascading failure** | Sập dây chuyền — một dịch vụ chậm kéo sập mọi thứ phía trước | [Ngày 54](./Giai-doan-4-SRE-Capstone.md#ngày-54-service-mesh-microservices-nâng-cao) |
| **Cattle, not pets** | Coi máy chủ là đồ dùng một lần — hỏng thì xoá dựng lại, không ngồi chữa | [Ngày 27](./Giai-doan-2-Git-Docker-Cloud.md#ngày-27-máy-chủ-cloud-tạo-quản-lý-vm) |
| **Change failure rate** | % lần deploy gây sự cố — nhóm dẫn đầu: dưới 5% | [Ngày 55](./Giai-doan-4-SRE-Capstone.md#ngày-55-platform-engineering-developer-experience) |
| **Chaos engineering** | Chủ động phá hệ thống trong giờ làm việc để kiểm chứng khả năng chịu lỗi | [Ngày 52](./Giai-doan-4-SRE-Capstone.md#ngày-52-high-availability-scaling-disaster-recovery) |
| **Chart** | Gói khuôn mẫu Kubernetes (templates + values mặc định) | [Ngày 42](./Giai-doan-3-CICD-K8s-Monitoring.md#ngày-42-helm-package-manager-cho-kubernetes) |
| **Checkov** | Quét cấu hình hạ tầng dạng code (Terraform, K8s) | [Ngày 49](./Giai-doan-3-CICD-K8s-Monitoring.md#ngày-49-bảo-mật-devsecops-best-practices) |
| **Checksum** (`sha256sum`)** | Chữ ký kiểm tra toàn vẹn file | [Ngày 11](./Giai-doan-1-Linux-SysOps.md#ngày-11-lưu-trữ-backup-khôi-phục) |
| **cherry-pick** | Lấy 1 commit cụ thể sang nhánh khác | [Ngày 25](./Giai-doan-2-Git-Docker-Cloud.md#ngày-25-git-nâng-cao-rebase-tag-workflow) |
| **CI/CD** | Tích hợp liên tục / Chuyển giao–Triển khai liên tục (tự build-test-deploy) | [Ngày 1](./Giai-doan-1-Linux-SysOps.md#ngày-1-devops-sysops-là-gì-tổng-quan-toàn-ngành) |
| **CIA** | Confidentiality/Integrity/Availability | [Ngày 9](./Giai-doan-1-Linux-SysOps.md#ngày-9-tường-lửa-bảo-mật-hardening) |
| **CIDR** (`/24`)** | Cách viết dải mạng | [Ngày 7](./Giai-doan-1-Linux-SysOps.md#ngày-7-mạng-máy-tính-cho-devops-cơ-bản) |
| **Circuit breaker** | Đóng → Mở (từ chối ngay) → Nửa mở (thử dè dặt) | [Ngày 54](./Giai-doan-4-SRE-Capstone.md#ngày-54-service-mesh-microservices-nâng-cao) |
| **clone** | Sao chép repo về máy | [Ngày 15](./Giai-doan-2-Git-Docker-Cloud.md#ngày-15-github-remote-collaboration-pull-request) |
| **cloud-init** | Cơ chế máy tự cấu hình ở lần khởi động đầu tiên (AWS gọi là *user data*) | [Ngày 27](./Giai-doan-2-Git-Docker-Cloud.md#ngày-27-máy-chủ-cloud-tạo-quản-lý-vm) |
| **Cluster Autoscaler** | Tự thêm **node** khi pod không còn chỗ — tầng khác với HPA | [Ngày 41](./Giai-doan-3-CICD-K8s-Monitoring.md#ngày-41-kubernetes-health-check-resource-autoscaling) |
| **ClusterIP** | Loại Service mặc định — chỉ gọi được từ trong cluster (90% trường hợp) | [Ngày 38](./Giai-doan-3-CICD-K8s-Monitoring.md#ngày-38-kubernetes-service-networking) |
| **CMD / ENTRYPOINT** | Lệnh mặc định / lệnh chính cố định | [Ngày 17](./Giai-doan-2-Git-Docker-Cloud.md#ngày-17-docker-dockerfile-build-image) |
| **Code review** | Đọc & góp ý code trước khi merge | [Ngày 15](./Giai-doan-2-Git-Docker-Cloud.md#ngày-15-github-remote-collaboration-pull-request) |
| **Command substitution** `$( )** | Chạy lệnh rồi thay bằng kết quả | [Ngày 6](./Giai-doan-1-Linux-SysOps.md#ngày-6-bash-scripting-nâng-cao-tự-động-hóa) |
| **Commit** | Một ảnh chụp trạng thái được lưu | [Ngày 13](./Giai-doan-2-Git-Docker-Cloud.md#ngày-13-git-cơ-bản-quản-lý-phiên-bản) |
| **concurrency** | Huỷ các lần chạy cũ khi push liên tiếp, chỉ giữ lần mới nhất | [Ngày 32](./Giai-doan-3-CICD-K8s-Monitoring.md#ngày-32-ci-pipeline-build-test-lint-tự-động) |
| **condition: service_healthy** | Chờ service kia khoẻ mới start | [Ngày 20](./Giai-doan-2-Git-Docker-Cloud.md#ngày-20-docker-compose-quản-lý-multi-container) |
| **ConfigMap** | Nơi chứa cấu hình thường: URL, cổng, tên miền | [Ngày 39](./Giai-doan-3-CICD-K8s-Monitoring.md#ngày-39-kubernetes-configmap-secret-storage) |
| **Configuration drift** | Thực tế trôi khỏi file khai báo, thường do ai đó sửa tay | [Ngày 36](./Giai-doan-3-CICD-K8s-Monitoring.md#ngày-36-kubernetes-khái-niệm-kiến-trúc) |
| **Conflict** | Xung đột khi 2 nhánh sửa cùng dòng | [Ngày 14](./Giai-doan-2-Git-Docker-Cloud.md#ngày-14-git-branch-merge-xử-lý-conflict) |
| **Connection pooling** | Tái dùng kết nối DB (PgBouncer) | [Ngày 24](./Giai-doan-2-Git-Docker-Cloud.md#ngày-24-cơ-sở-dữ-liệu-cho-devops) |
| **Container** | Bản đang chạy của một image | [Ngày 16](./Giai-doan-2-Git-Docker-Cloud.md#ngày-16-docker-khái-niệm-container-đầu-tiên) |
| **Control Plane** | Ban giám đốc cluster: API Server, etcd, Scheduler, Controller Manager | [Ngày 36](./Giai-doan-3-CICD-K8s-Monitoring.md#ngày-36-kubernetes-khái-niệm-kiến-trúc) |
| **Conventional Commits** | Chuẩn message (`feat:`/`fix:`) | [Ngày 25](./Giai-doan-2-Git-Docker-Cloud.md#ngày-25-git-nâng-cao-rebase-tag-workflow) |
| **COPY --from** | Chép file từ stage khác | [Ngày 18](./Giai-doan-2-Git-Docker-Cloud.md#ngày-18-docker-image-tối-ưu-multi-stage-build) |
| **Counter** | Chỉ tăng — **bắt buộc bọc `rate()`** | [Ngày 44](./Giai-doan-3-CICD-K8s-Monitoring.md#ngày-44-monitoring-prometheus-metrics) |
| **Cron / crontab** | Trình hẹn giờ chạy lệnh theo lịch / bảng lịch | [Ngày 6](./Giai-doan-1-Linux-SysOps.md#ngày-6-bash-scripting-nâng-cao-tự-động-hóa) |
| **CVE** | Lỗ hổng bảo mật đã được ghi nhận | [Ngày 18](./Giai-doan-2-Git-Docker-Cloud.md#ngày-18-docker-image-tối-ưu-multi-stage-build) |
| **CVE / CVSS** | Mã định danh lỗ hổng công bố / điểm nghiêm trọng 0–10 | [Ngày 49](./Giai-doan-3-CICD-K8s-Monitoring.md#ngày-49-bảo-mật-devsecops-best-practices) |

## D

| Thuật ngữ | Nghĩa | Học ở |
|---|---|---|
| **Daemon** (dockerd)** | Tiến trình nền chạy Docker | [Ngày 16](./Giai-doan-2-Git-Docker-Cloud.md#ngày-16-docker-khái-niệm-container-đầu-tiên) |
| **Declarative** | Khai báo trạng thái mong muốn, không ra lệnh từng bước | [Ngày 36](./Giai-doan-3-CICD-K8s-Monitoring.md#ngày-36-kubernetes-khái-niệm-kiến-trúc) · [Ngày 37](./Giai-doan-3-CICD-K8s-Monitoring.md#ngày-37-kubernetes-pod-deployment-replicaset) |
| **Defense in depth** | Phòng thủ nhiều lớp | [Ngày 9](./Giai-doan-1-Linux-SysOps.md#ngày-9-tường-lửa-bảo-mật-hardening) |
| **Deny-by-default** | Chặn hết, chỉ mở cái cần | [Ngày 9](./Giai-doan-1-Linux-SysOps.md#ngày-9-tường-lửa-bảo-mật-hardening) |
| **Dependabot / Renovate** | Tự mở PR nâng phiên bản thư viện có lỗ hổng | [Ngày 49](./Giai-doan-3-CICD-K8s-Monitoring.md#ngày-49-bảo-mật-devsecops-best-practices) |
| **depends_on** | Khai báo thứ tự khởi động | [Ngày 20](./Giai-doan-2-Git-Docker-Cloud.md#ngày-20-docker-compose-quản-lý-multi-container) |
| **Deployment frequency** | Bao lâu deploy một lần — nhóm dẫn đầu: nhiều lần mỗi ngày | [Ngày 55](./Giai-doan-4-SRE-Capstone.md#ngày-55-platform-engineering-developer-experience) |
| **Detached HEAD** | Đang ở 1 commit, không trên nhánh nào | [Ngày 14](./Giai-doan-2-Git-Docker-Cloud.md#ngày-14-git-branch-merge-xử-lý-conflict) |
| **detached** (`-d`)** | Chạy container ở chế độ nền | [Ngày 16](./Giai-doan-2-Git-Docker-Cloud.md#ngày-16-docker-khái-niệm-container-đầu-tiên) |
| **Developer Experience** | Đo bằng **ma sát**: bao lâu deploy được lần đầu, bao nhiêu việc phải đi hỏi | [Ngày 55](./Giai-doan-4-SRE-Capstone.md#ngày-55-platform-engineering-developer-experience) |
| **DevOps** | Văn hoá + thực hành tự động hoá toàn bộ vòng đời phần mềm | [Ngày 1](./Giai-doan-1-Linux-SysOps.md#ngày-1-devops-sysops-là-gì-tổng-quan-toàn-ngành) |
| **Directory** | Thư mục | [Ngày 2](./Giai-doan-1-Linux-SysOps.md#ngày-2-linux-cơ-bản-điều-hướng-quản-lý-file) |
| **Distroless** | Image không có shell/OS thừa — an toàn nhất | [Ngày 18](./Giai-doan-2-Git-Docker-Cloud.md#ngày-18-docker-image-tối-ưu-multi-stage-build) |
| **DNS** | Hệ phân giải tên miền → IP | [Ngày 7](./Giai-doan-1-Linux-SysOps.md#ngày-7-mạng-máy-tính-cho-devops-cơ-bản) |
| **DNS nội bộ** | `web-svc.default.svc.cluster.local` — gọi dịch vụ bằng tên, không IP | [Ngày 19](./Giai-doan-2-Git-Docker-Cloud.md#ngày-19-docker-volume-network-dữ-liệu-bền-vững) · [Ngày 38](./Giai-doan-3-CICD-K8s-Monitoring.md#ngày-38-kubernetes-service-networking) |
| **Docker Compose** | Công cụ mô tả & chạy nhiều container bằng 1 file | [Ngày 20](./Giai-doan-2-Git-Docker-Cloud.md#ngày-20-docker-compose-quản-lý-multi-container) |
| **Dockerfile** | Công thức để build image | [Ngày 17](./Giai-doan-2-Git-Docker-Cloud.md#ngày-17-docker-dockerfile-build-image) |
| **DORA metrics** | 4 chỉ số: tần suất deploy, lead time, tỉ lệ gây lỗi, thời gian khôi phục | [Ngày 55](./Giai-doan-4-SRE-Capstone.md#ngày-55-platform-engineering-developer-experience) |
| **DR** | Khôi phục sau thảm hoạ — sao lưu, dựng lại | [Ngày 52](./Giai-doan-4-SRE-Capstone.md#ngày-52-high-availability-scaling-disaster-recovery) |
| **Drift** | Thực tế trôi khỏi state, thường do ai đó sửa tay trên console | [Ngày 29](./Giai-doan-2-Git-Docker-Cloud.md#ngày-29-infrastructure-as-code-giới-thiệu-terraform) · [Ngày 48](./Giai-doan-3-CICD-K8s-Monitoring.md#ngày-48-terraform-nâng-cao-module-remote-state-workspace) |

## E

| Thuật ngữ | Nghĩa | Học ở |
|---|---|---|
| **Egress cost** | Chi phí truyền dữ liệu **ra ngoài** và **giữa các vùng** — hay gây bất ngờ | [Ngày 53](./Giai-doan-4-SRE-Capstone.md#ngày-53-cost-optimization-finops) |
| **Elastic IP / IP tĩnh** | Địa chỉ IP cố định; không gắn với máy nào thì vẫn bị tính tiền | [Ngày 27](./Giai-doan-2-Git-Docker-Cloud.md#ngày-27-máy-chủ-cloud-tạo-quản-lý-vm) |
| **Endpoints** | Danh sách IP pod mà Service tìm thấy — lệnh chẩn đoán số một | [Ngày 38](./Giai-doan-3-CICD-K8s-Monitoring.md#ngày-38-kubernetes-service-networking) |
| **envFrom` vs `volumeMount** | Tiêm thành biến môi trường (cố định) vs thành file (tự cập nhật) | [Ngày 39](./Giai-doan-3-CICD-K8s-Monitoring.md#ngày-39-kubernetes-configmap-secret-storage) |
| **Environment** | Cổng có người gác trong GitHub Actions — chờ duyệt mới deploy | [Ngày 34](./Giai-doan-3-CICD-K8s-Monitoring.md#ngày-34-cd-pipeline-tự-động-deploy-lên-server) |
| **Environment variable** | Biến môi trường (vd `$PATH`) | [Ngày 3](./Giai-doan-1-Linux-SysOps.md#ngày-3-linux-quản-lý-tiến-trình-phần-mềm) |
| **Ephemeral** | Tạm thời — xoá là mất | [Ngày 19](./Giai-doan-2-Git-Docker-Cloud.md#ngày-19-docker-volume-network-dữ-liệu-bền-vững) |
| **Error budget** | Phần được phép sai = 100% − SLO; SLO 99,9% → 43 phút chết/tháng | [Ngày 51](./Giai-doan-4-SRE-Capstone.md#ngày-51-site-reliability-engineering-sre-nguyên-lý) |
| **etcd** | Sổ cái lưu toàn bộ trạng thái cluster — mất etcd là cluster mất trí nhớ | [Ngày 36](./Giai-doan-3-CICD-K8s-Monitoring.md#ngày-36-kubernetes-khái-niệm-kiến-trúc) |
| **Exit code** (`$?`)** | Mã kết thúc: 0 = ok, khác 0 = lỗi | [Ngày 5](./Giai-doan-1-Linux-SysOps.md#ngày-5-bash-scripting-cơ-bản) |
| **Exponential backoff + jitter** | Chờ tăng dần + ngẫu nhiên để các client không thử lại cùng lúc | [Ngày 54](./Giai-doan-4-SRE-Capstone.md#ngày-54-service-mesh-microservices-nâng-cao) |
| **Exporter** | Chương trình nhỏ bày thông tin hệ thống ra dạng metric (node-exporter, cAdvisor) | [Ngày 44](./Giai-doan-3-CICD-K8s-Monitoring.md#ngày-44-monitoring-prometheus-metrics) |
| **expose vs ports** | Chỉ cho container nội bộ thấy vs mở cổng ra ngoài máy chủ | [Ngày 28](./Giai-doan-2-Git-Docker-Cloud.md#ngày-28-triển-khai-app-lên-cloud-docker-trên-vm) |

## F

| Thuật ngữ | Nghĩa | Học ở |
|---|---|---|
| **Facts** | Thông tin Ansible tự thu thập về máy (OS, CPU, IP...) | [Ngày 47](./Giai-doan-3-CICD-K8s-Monitoring.md#ngày-47-configuration-management-ansible) |
| **fail-fast: false** | Một bản matrix hỏng vẫn chạy nốt các bản còn lại để thấy toàn cảnh | [Ngày 32](./Giai-doan-3-CICD-K8s-Monitoring.md#ngày-32-ci-pipeline-build-test-lint-tự-động) |
| **fail2ban** | Tự chặn IP dò mật khẩu | [Ngày 9](./Giai-doan-1-Linux-SysOps.md#ngày-9-tường-lửa-bảo-mật-hardening) |
| **Fast-forward** | Merge chỉ dời con trỏ (lịch sử thẳng) | [Ngày 14](./Giai-doan-2-Git-Docker-Cloud.md#ngày-14-git-branch-merge-xử-lý-conflict) |
| **Feature branch** | Nhánh riêng cho mỗi tính năng | [Ngày 14](./Giai-doan-2-Git-Docker-Cloud.md#ngày-14-git-branch-merge-xử-lý-conflict) |
| **FHS** | Filesystem Hierarchy Standard — chuẩn bố trí thư mục Linux | [Ngày 2](./Giai-doan-1-Linux-SysOps.md#ngày-2-linux-cơ-bản-điều-hướng-quản-lý-file) |
| **FinOps** | Đưa thông tin chi phí tới tận tay người ra quyết định kỹ thuật | [Ngày 53](./Giai-doan-4-SRE-Capstone.md#ngày-53-cost-optimization-finops) |
| **Firewall** | Tường lửa — kiểm soát cổng vào/ra | [Ngày 9](./Giai-doan-1-Linux-SysOps.md#ngày-9-tường-lửa-bảo-mật-hardening) |
| **for:** | Điều kiện phải duy trì bao lâu mới báo động — lọc bỏ nhấp nháy ngắn | [Ngày 44](./Giai-doan-3-CICD-K8s-Monitoring.md#ngày-44-monitoring-prometheus-metrics) |
| **Foreground / Background** | Tiền cảnh / chạy nền (`&`) | [Ngày 3](./Giai-doan-1-Linux-SysOps.md#ngày-3-linux-quản-lý-tiến-trình-phần-mềm) |
| **Fork** | Sao chép repo người khác về tài khoản mình | [Ngày 15](./Giai-doan-2-Git-Docker-Cloud.md#ngày-15-github-remote-collaboration-pull-request) |
| **Free tier** | Hạn mức dùng miễn phí; **vượt hạn mức vẫn tính tiền bình thường** | [Ngày 26](./Giai-doan-2-Git-Docker-Cloud.md#ngày-26-làm-quen-cloud-khái-niệm-free-tier) |
| **Function** | Hàm — nhóm lệnh gọi lại được | [Ngày 5](./Giai-doan-1-Linux-SysOps.md#ngày-5-bash-scripting-cơ-bản) |

## G

| Thuật ngữ | Nghĩa | Học ở |
|---|---|---|
| **Gauge** | Lên xuống tự do — đọc thẳng, không bọc `rate()` | [Ngày 44](./Giai-doan-3-CICD-K8s-Monitoring.md#ngày-44-monitoring-prometheus-metrics) |
| **GHCR** | GitHub Container Registry — đăng nhập bằng `GITHUB_TOKEN` có sẵn | [Ngày 33](./Giai-doan-3-CICD-K8s-Monitoring.md#ngày-33-cd-pipeline-build-push-docker-image) |
| **Ghim phiên bản action** | Dùng `@v4` thay `@main` để pipeline không gãy khi tác giả sửa | [Ngày 31](./Giai-doan-3-CICD-K8s-Monitoring.md#ngày-31-cicd-khái-niệm-github-actions-cơ-bản) |
| **GitHub Secrets** | Nơi cất token/mật khẩu; đọc bằng `${{ secrets.TÊN }}`, che `***` trong log | [Ngày 31](./Giai-doan-3-CICD-K8s-Monitoring.md#ngày-31-cicd-khái-niệm-github-actions-cơ-bản) |
| **Gitleaks** | Quét bí mật lỡ commit — quét **cả lịch sử**, cần `fetch-depth: 0` | [Ngày 49](./Giai-doan-3-CICD-K8s-Monitoring.md#ngày-49-bảo-mật-devsecops-best-practices) |
| **GitOps** | Git là nguồn sự thật; tác nhân trong cluster tự kéo về và sửa cho khớp | [Ngày 43](./Giai-doan-3-CICD-K8s-Monitoring.md#ngày-43-gitops-argocd-triển-khai-khai-báo) |
| **Golden image** | Ảnh hệ điều hành nướng sẵn mọi thứ; máy lên là dùng được ngay (Packer) | [Ngày 27](./Giai-doan-2-Git-Docker-Cloud.md#ngày-27-máy-chủ-cloud-tạo-quản-lý-vm) |
| **Golden path** | Con đường mặc định đã lát sẵn, đúng chuẩn, dễ đi hơn mọi cách khác | [Ngày 55](./Giai-doan-4-SRE-Capstone.md#ngày-55-platform-engineering-developer-experience) |
| **Graceful degradation** | Suy giảm có kiểm soát — mất bớt chức năng nhưng vẫn phục vụ được | [Ngày 28](./Giai-doan-2-Git-Docker-Cloud.md#ngày-28-triển-khai-app-lên-cloud-docker-trên-vm) · [Ngày 54](./Giai-doan-4-SRE-Capstone.md#ngày-54-service-mesh-microservices-nâng-cao) |

## H

| Thuật ngữ | Nghĩa | Học ở |
|---|---|---|
| **HA** | Chịu được hỏng hóc một thành phần — nhiều bản sao, tự chuyển đổi | [Ngày 52](./Giai-doan-4-SRE-Capstone.md#ngày-52-high-availability-scaling-disaster-recovery) |
| **Hadolint** | Kiểm tra cách viết Dockerfile | [Ngày 49](./Giai-doan-3-CICD-K8s-Monitoring.md#ngày-49-bảo-mật-devsecops-best-practices) |
| **Handler** | Task chỉ chạy khi có thay đổi thật sự (qua `notify`) | [Ngày 47](./Giai-doan-3-CICD-K8s-Monitoring.md#ngày-47-configuration-management-ansible) |
| **Hardening** | Làm cứng — siết cấu hình cho an toàn | [Ngày 9](./Giai-doan-1-Linux-SysOps.md#ngày-9-tường-lửa-bảo-mật-hardening) |
| **HEAD** | Con trỏ "đang ở commit nào" | [Ngày 13](./Giai-doan-2-Git-Docker-Cloud.md#ngày-13-git-cơ-bản-quản-lý-phiên-bản) |
| **Health check sau deploy** | Gọi `/health` có thử lại; thất bại thì báo đỏ, chặn bản hỏng | [Ngày 34](./Giai-doan-3-CICD-K8s-Monitoring.md#ngày-34-cd-pipeline-tự-động-deploy-lên-server) |
| **healthcheck** | Kiểm tra dịch vụ đã sẵn sàng chưa | [Ngày 20](./Giai-doan-2-Git-Docker-Cloud.md#ngày-20-docker-compose-quản-lý-multi-container) |
| **HEALTHCHECK** | Lệnh Docker tự chạy để biết container còn khoẻ không | [Ngày 33](./Giai-doan-3-CICD-K8s-Monitoring.md#ngày-33-cd-pipeline-build-push-docker-image) |
| **Healthy / Degraded** | Ứng dụng có chạy được không — **trục khác** với Synced | [Ngày 43](./Giai-doan-3-CICD-K8s-Monitoring.md#ngày-43-gitops-argocd-triển-khai-khai-báo) |
| **helm lint** | Kiểm tra chart hợp lệ trước khi cài | [Ngày 42](./Giai-doan-3-CICD-K8s-Monitoring.md#ngày-42-helm-package-manager-cho-kubernetes) |
| **helm template** | Render YAML ngoại tuyến, không đụng cluster — công cụ gỡ lỗi số một | [Ngày 42](./Giai-doan-3-CICD-K8s-Monitoring.md#ngày-42-helm-package-manager-cho-kubernetes) |
| **Hidden file** | File ẩn (tên bắt đầu bằng `.`) | [Ngày 2](./Giai-doan-1-Linux-SysOps.md#ngày-2-linux-cơ-bản-điều-hướng-quản-lý-file) |
| **Histogram** | Chia giá trị vào các 'xô' — dùng `histogram_quantile()` tính p95/p99 | [Ngày 44](./Giai-doan-3-CICD-K8s-Monitoring.md#ngày-44-monitoring-prometheus-metrics) |
| **HPA** | Tự tăng giảm **số pod** theo tải; cần metrics-server và requests | [Ngày 41](./Giai-doan-3-CICD-K8s-Monitoring.md#ngày-41-kubernetes-health-check-resource-autoscaling) |
| **HTTP status code** | Mã kết quả HTTP (2xx/4xx/5xx) | [Ngày 7](./Giai-doan-1-Linux-SysOps.md#ngày-7-mạng-máy-tính-cho-devops-cơ-bản) |

## I

| Thuật ngữ | Nghĩa | Học ở |
|---|---|---|
| **IaaS / PaaS / SaaS** | Ba mức 'ăn sẵn' — càng lên cao bạn càng lo ít, càng mất quyền kiểm soát | [Ngày 26](./Giai-doan-2-Git-Docker-Cloud.md#ngày-26-làm-quen-cloud-khái-niệm-free-tier) |
| **IaC** | Hạ tầng dưới dạng code | [Ngày 29](./Giai-doan-2-Git-Docker-Cloud.md#ngày-29-infrastructure-as-code-giới-thiệu-terraform) |
| **IAM** | Hệ quản lý người dùng và quyền trên cloud | [Ngày 26](./Giai-doan-2-Git-Docker-Cloud.md#ngày-26-làm-quen-cloud-khái-niệm-free-tier) |
| **Idempotent** | Chạy bao nhiêu lần cũng cho cùng kết quả — khái niệm quan trọng nhất | [Ngày 29](./Giai-doan-2-Git-Docker-Cloud.md#ngày-29-infrastructure-as-code-giới-thiệu-terraform) · [Ngày 47](./Giai-doan-3-CICD-K8s-Monitoring.md#ngày-47-configuration-management-ansible) |
| **IDP** | Internal Developer Platform — nền tảng nội bộ cho lập trình viên tự phục vụ | [Ngày 55](./Giai-doan-4-SRE-Capstone.md#ngày-55-platform-engineering-developer-experience) |
| **ignore-unfixed** | Bỏ qua lỗ hổng chưa có bản vá — thực dụng, tránh chặn vô ích | [Ngày 49](./Giai-doan-3-CICD-K8s-Monitoring.md#ngày-49-bảo-mật-devsecops-best-practices) |
| **Image** | Khuôn mẫu chỉ đọc để tạo container | [Ngày 16](./Giai-doan-2-Git-Docker-Cloud.md#ngày-16-docker-khái-niệm-container-đầu-tiên) |
| **Incremental backup** | Backup gia tăng (chỉ phần thay đổi) | [Ngày 11](./Giai-doan-1-Linux-SysOps.md#ngày-11-lưu-trữ-backup-khôi-phục) |
| **Indentation** | Thụt lề (thể hiện cấp bậc trong YAML) | [Ngày 22](./Giai-doan-2-Git-Docker-Cloud.md#ngày-22-yaml-json-định-dạng-cấu-hình) |
| **infracost** | Ước tính chi phí ngay trên Pull Request Terraform | [Ngày 53](./Giai-doan-4-SRE-Capstone.md#ngày-53-cost-optimization-finops) |
| **Ingress** | Tờ khai luật định tuyến theo tên miền/đường dẫn | [Ngày 38](./Giai-doan-3-CICD-K8s-Monitoring.md#ngày-38-kubernetes-service-networking) |
| **Ingress Controller** | Phần mềm thực thi các luật Ingress — **phải cài riêng** | [Ngày 23](./Giai-doan-2-Git-Docker-Cloud.md#ngày-23-reverse-proxy-web-server-nginx-chuyên-sâu) · [Ngày 38](./Giai-doan-3-CICD-K8s-Monitoring.md#ngày-38-kubernetes-service-networking) |
| **Inventory** | Danh sách máy cần quản lý, chia theo nhóm | [Ngày 47](./Giai-doan-3-CICD-K8s-Monitoring.md#ngày-47-configuration-management-ansible) |
| **IP address** | Địa chỉ máy trên mạng | [Ngày 7](./Giai-doan-1-Linux-SysOps.md#ngày-7-mạng-máy-tính-cho-devops-cơ-bản) |

## J

| Thuật ngữ | Nghĩa | Học ở |
|---|---|---|
| **journald / journalctl** | Hệ log của systemd / lệnh đọc nó | [Ngày 10](./Giai-doan-1-Linux-SysOps.md#ngày-10-quản-lý-log-giám-sát-hệ-thống) |
| **jq / yq** | Công cụ lọc/xử lý JSON / YAML | [Ngày 22](./Giai-doan-2-Git-Docker-Cloud.md#ngày-22-yaml-json-định-dạng-cấu-hình) |
| **JSON** | Định dạng dữ liệu ngoặc nhọn (API/CLI output) | [Ngày 22](./Giai-doan-2-Git-Docker-Cloud.md#ngày-22-yaml-json-định-dạng-cấu-hình) |

## K

| Thuật ngữ | Nghĩa | Học ở |
|---|---|---|
| **Key pair** | Cặp khoá SSH — phần công khai nạp vào máy, phần riêng bạn giữ | [Ngày 27](./Giai-doan-2-Git-Docker-Cloud.md#ngày-27-máy-chủ-cloud-tạo-quản-lý-vm) |
| **known_hosts** | Danh sách host key đã tin tưởng | [Ngày 8](./Giai-doan-1-Linux-SysOps.md#ngày-8-ssh-kết-nối-quản-lý-server-từ-xa) |
| **kubectl rollout restart** | Khởi động lại pod cuốn chiếu, không gián đoạn dịch vụ | [Ngày 39](./Giai-doan-3-CICD-K8s-Monitoring.md#ngày-39-kubernetes-configmap-secret-storage) |
| **kubelet** | Tổ trưởng trên mỗi node: nhận lệnh từ API Server, bảo runtime chạy container | [Ngày 36](./Giai-doan-3-CICD-K8s-Monitoring.md#ngày-36-kubernetes-khái-niệm-kiến-trúc) |

## Ký hiệu

| Thuật ngữ | Nghĩa | Học ở |
|---|---|---|
| **$__rate_interval** | Biến Grafana tự tính khoảng thời gian, thay cho `[5m]` cố định | [Ngày 45](./Giai-doan-3-CICD-K8s-Monitoring.md#ngày-45-monitoring-grafana-dashboard) |
| **--atomic** | Upgrade thất bại thì tự động quay lui về bản cũ | [Ngày 42](./Giai-doan-3-CICD-K8s-Monitoring.md#ngày-42-helm-package-manager-cho-kubernetes) |
| **--check --diff** | Chạy khô: báo sẽ đổi gì mà không đổi thật | [Ngày 47](./Giai-doan-3-CICD-K8s-Monitoring.md#ngày-47-configuration-management-ansible) |
| **.dockerignore** | Danh sách file không gửi vào trình build — build nhanh hơn, image sạch hơn | [Ngày 17](./Giai-doan-2-Git-Docker-Cloud.md#ngày-17-docker-dockerfile-build-image) · [Ngày 33](./Giai-doan-3-CICD-K8s-Monitoring.md#ngày-33-cd-pipeline-build-push-docker-image) |
| **.env** | File biến môi trường Compose tự đọc | [Ngày 20](./Giai-doan-2-Git-Docker-Cloud.md#ngày-20-docker-compose-quản-lý-multi-container) |
| **.gitignore** | Danh sách file Git bỏ qua | [Ngày 13](./Giai-doan-2-Git-Docker-Cloud.md#ngày-13-git-cơ-bản-quản-lý-phiên-bản) |
| **3 trụ cột observability** | Metrics (có sai không) → Logs (sai gì) → Traces (sai ở đâu) | [Ngày 46](./Giai-doan-3-CICD-K8s-Monitoring.md#ngày-46-logging-tập-trung-loki) |
| **3-2-1 rule** | 3 bản, 2 loại lưu trữ, 1 off-site | [Ngày 11](./Giai-doan-1-Linux-SysOps.md#ngày-11-lưu-trữ-backup-khôi-phục) |
| **4 tín hiệu vàng** | Traffic · Errors · Latency · Saturation — bộ lọc để biết nhìn gì | [Ngày 45](./Giai-doan-3-CICD-K8s-Monitoring.md#ngày-45-monitoring-grafana-dashboard) |
| **{{ .Values.x }}** | Cú pháp lấy giá trị từ values.yaml trong template | [Ngày 42](./Giai-doan-3-CICD-K8s-Monitoring.md#ngày-42-helm-package-manager-cho-kubernetes) |
| **{{-** | Nuốt khoảng trắng phía trước — thiếu nó là sai thụt lề YAML | [Ngày 42](./Giai-doan-3-CICD-K8s-Monitoring.md#ngày-42-helm-package-manager-cho-kubernetes) |

## L

| Thuật ngữ | Nghĩa | Học ở |
|---|---|---|
| **latest** | Nhãn dán di động trỏ tới bản mới nhất — **không dùng để deploy** | [Ngày 33](./Giai-doan-3-CICD-K8s-Monitoring.md#ngày-33-cd-pipeline-build-push-docker-image) |
| **Layer** | Một tầng của image (mỗi chỉ thị tạo 1 layer) | [Ngày 17](./Giai-doan-2-Git-Docker-Cloud.md#ngày-17-docker-dockerfile-build-image) |
| **Lead time for changes** | Từ commit tới production — nhóm dẫn đầu: dưới 1 giờ | [Ngày 55](./Giai-doan-4-SRE-Capstone.md#ngày-55-platform-engineering-developer-experience) |
| **Least privilege** | Đặc quyền tối thiểu — cho đúng quyền cần thiết, không hơn | [Ngày 4](./Giai-doan-1-Linux-SysOps.md#ngày-4-linux-người-dùng-nhóm-phân-quyền) · [Ngày 26](./Giai-doan-2-Git-Docker-Cloud.md#ngày-26-làm-quen-cloud-khái-niệm-free-tier) |
| **limits** | Trần cứng; vượt RAM → OOMKilled, vượt CPU → bị bóp chậm | [Ngày 41](./Giai-doan-3-CICD-K8s-Monitoring.md#ngày-41-kubernetes-health-check-resource-autoscaling) |
| **Lint** | Kiểm tra cú pháp tự động (`yamllint`) | [Ngày 22](./Giai-doan-2-Git-Docker-Cloud.md#ngày-22-yaml-json-định-dạng-cấu-hình) |
| **Listening port** | Cổng đang mở chờ kết nối | [Ngày 7](./Giai-doan-1-Linux-SysOps.md#ngày-7-mạng-máy-tính-cho-devops-cơ-bản) |
| **livenessProbe** | Hỏi 'còn cứu được không?' — trượt thì **giết và tạo lại container** | [Ngày 41](./Giai-doan-3-CICD-K8s-Monitoring.md#ngày-41-kubernetes-health-check-resource-autoscaling) |
| **Load average** | Tải trung bình 1/5/15 phút | [Ngày 10](./Giai-doan-1-Linux-SysOps.md#ngày-10-quản-lý-log-giám-sát-hệ-thống) |
| **Load balancing** | Chia tải giữa nhiều backend | [Ngày 23](./Giai-doan-2-Git-Docker-Cloud.md#ngày-23-reverse-proxy-web-server-nginx-chuyên-sâu) |
| **LoadBalancer** | Cloud cấp bộ cân bằng tải riêng — mỗi cái là một hoá đơn | [Ngày 38](./Giai-doan-3-CICD-K8s-Monitoring.md#ngày-38-kubernetes-service-networking) |
| **LocalStack** | Công cụ giả lập dịch vụ AWS trên máy — học và test không tốn chi phí | [Ngày 26](./Giai-doan-2-Git-Docker-Cloud.md#ngày-26-làm-quen-cloud-khái-niệm-free-tier) |
| **Log** | Nhật ký sự kiện của chương trình/hệ thống | [Ngày 10](./Giai-doan-1-Linux-SysOps.md#ngày-10-quản-lý-log-giám-sát-hệ-thống) |
| **Log rotation** | Giới hạn dung lượng log (`max-size`, `max-file`) để không làm đầy ổ đĩa | [Ngày 28](./Giai-doan-2-Git-Docker-Cloud.md#ngày-28-triển-khai-app-lên-cloud-docker-trên-vm) |
| **logrotate** | Tự xoay/nén/xoá log cũ | [Ngày 10](./Giai-doan-1-Linux-SysOps.md#ngày-10-quản-lý-log-giám-sát-hệ-thống) |
| **Loki** | Hệ gom log 'như Prometheus' — chỉ đánh chỉ mục nhãn, không đánh chỉ mục nội dung | [Ngày 46](./Giai-doan-3-CICD-K8s-Monitoring.md#ngày-46-logging-tập-trung-loki) |
| **Loop / Condition** | Vòng lặp (`for`/`while`) / điều kiện (`if`) | [Ngày 5](./Giai-doan-1-Linux-SysOps.md#ngày-5-bash-scripting-cơ-bản) |

## M

| Thuật ngữ | Nghĩa | Học ở |
|---|---|---|
| **Managed DB** | DB do cloud vận hành (RDS/Cloud SQL) | [Ngày 24](./Giai-doan-2-Git-Docker-Cloud.md#ngày-24-cơ-sở-dữ-liệu-cho-devops) |
| **Manifest** | File YAML mô tả đối tượng K8s (trạng thái mong muốn) | [Ngày 37](./Giai-doan-3-CICD-K8s-Monitoring.md#ngày-37-kubernetes-pod-deployment-replicaset) |
| **Matrix** | Chạy cùng một job trên nhiều phiên bản/OS song song | [Ngày 32](./Giai-doan-3-CICD-K8s-Monitoring.md#ngày-32-ci-pipeline-build-test-lint-tự-động) |
| **Merge** | Hợp nhất nhánh này vào nhánh kia | [Ngày 14](./Giai-doan-2-Git-Docker-Cloud.md#ngày-14-git-branch-merge-xử-lý-conflict) |
| **Metric** | Một con số + nhãn + mốc thời gian, expose ở trang `/metrics` | [Ngày 44](./Giai-doan-3-CICD-K8s-Monitoring.md#ngày-44-monitoring-prometheus-metrics) |
| **Metric / Trace** | Số đo theo thời gian / dấu vết một request | [Ngày 10](./Giai-doan-1-Linux-SysOps.md#ngày-10-quản-lý-log-giám-sát-hệ-thống) |
| **Migration** | Thay đổi schema có version, rollback được | [Ngày 24](./Giai-doan-2-Git-Docker-Cloud.md#ngày-24-cơ-sở-dữ-liệu-cho-devops) |
| **Migration tương thích ngược** | Thêm cột trước, bỏ cột ở lần sau — để code cũ vẫn chạy được | [Ngày 34](./Giai-doan-3-CICD-K8s-Monitoring.md#ngày-34-cd-pipeline-tự-động-deploy-lên-server) |
| **Module** | Đơn vị việc dựng sẵn (`apt`, `copy`, `service`) — hơn 3000 cái | [Ngày 47](./Giai-doan-3-CICD-K8s-Monitoring.md#ngày-47-configuration-management-ansible) · [Ngày 48](./Giai-doan-3-CICD-K8s-Monitoring.md#ngày-48-terraform-nâng-cao-module-remote-state-workspace) |
| **mTLS** | Mã hoá hai chiều giữa các dịch vụ — mesh bật tự động | [Ngày 54](./Giai-doan-4-SRE-Capstone.md#ngày-54-service-mesh-microservices-nâng-cao) |
| **MTTR** | Thời gian trung bình khôi phục — nhóm dẫn đầu: dưới 1 giờ | [Ngày 55](./Giai-doan-4-SRE-Capstone.md#ngày-55-platform-engineering-developer-experience) |
| **Multi-stage build** | Tầng đầu cài/biên dịch, tầng cuối chỉ chép phần cần chạy → image nhỏ | [Ngày 18](./Giai-doan-2-Git-Docker-Cloud.md#ngày-18-docker-image-tối-ưu-multi-stage-build) · [Ngày 33](./Giai-doan-3-CICD-K8s-Monitoring.md#ngày-33-cd-pipeline-build-push-docker-image) |

## N

| Thuật ngữ | Nghĩa | Học ở |
|---|---|---|
| **Namespace** | Ranh giới chia ngăn cluster — dùng cho quota và phân quyền RBAC | [Ngày 36](./Giai-doan-3-CICD-K8s-Monitoring.md#ngày-36-kubernetes-khái-niệm-kiến-trúc) |
| **needs:** | Khai báo job này chờ job kia xong mới chạy; job trước đỏ thì job sau bị skip | [Ngày 32](./Giai-doan-3-CICD-K8s-Monitoring.md#ngày-32-ci-pipeline-build-test-lint-tự-động) |
| **Network (bridge/host/none)** | Mạng của container | [Ngày 19](./Giai-doan-2-Git-Docker-Cloud.md#ngày-19-docker-volume-network-dữ-liệu-bền-vững) |
| **NetworkPolicy** | Luật giới hạn pod nào gọi được pod nào; **mặc định KHÔNG bật** | [Ngày 38](./Giai-doan-3-CICD-K8s-Monitoring.md#ngày-38-kubernetes-service-networking) |
| **nginx -t** | Test cú pháp config | [Ngày 23](./Giai-doan-2-Git-Docker-Cloud.md#ngày-23-reverse-proxy-web-server-nginx-chuyên-sâu) |
| **NodePort** | Mở cổng 30000–32767 trên mọi node; tiện cho lab, không dùng production | [Ngày 38](./Giai-doan-3-CICD-K8s-Monitoring.md#ngày-38-kubernetes-service-networking) |
| **Norway problem** | Bẫy `NO` → `false` khi không quote | [Ngày 22](./Giai-doan-2-Git-Docker-Cloud.md#ngày-22-yaml-json-định-dạng-cấu-hình) |
| **npm ci** | Cài đúng theo lock file, không sửa lock — bắt buộc dùng trong CI | [Ngày 32](./Giai-doan-3-CICD-K8s-Monitoring.md#ngày-32-ci-pipeline-build-test-lint-tự-động) |

## O

| Thuật ngữ | Nghĩa | Học ở |
|---|---|---|
| **Observability** | Khả năng quan sát hệ thống (metric+log+trace) | [Ngày 10](./Giai-doan-1-Linux-SysOps.md#ngày-10-quản-lý-log-giám-sát-hệ-thống) |
| **Off-site** | Bản lưu ở địa điểm khác | [Ngày 11](./Giai-doan-1-Linux-SysOps.md#ngày-11-lưu-trữ-backup-khôi-phục) |
| **OOM** | Out Of Memory — hết RAM, tiến trình bị kill | [Ngày 10](./Giai-doan-1-Linux-SysOps.md#ngày-10-quản-lý-log-giám-sát-hệ-thống) |
| **OOMKilled / Exit 137** | Container bị kernel giết vì vượt limits RAM | [Ngày 41](./Giai-doan-3-CICD-K8s-Monitoring.md#ngày-41-kubernetes-health-check-resource-autoscaling) |
| **Over-provisioning** | Xin nhiều hơn mức dùng — nguồn lãng phí lớn nhất | [Ngày 53](./Giai-doan-4-SRE-Capstone.md#ngày-53-cost-optimization-finops) |
| **Owner / Group / Other** | Chủ / nhóm / người khác (3 nhóm quyền) | [Ngày 4](./Giai-doan-1-Linux-SysOps.md#ngày-4-linux-người-dùng-nhóm-phân-quyền) |

## P

| Thuật ngữ | Nghĩa | Học ở |
|---|---|---|
| **p95 / p99** | Phân vị — 95%/99% số request nhanh hơn con số này | [Ngày 45](./Giai-doan-3-CICD-K8s-Monitoring.md#ngày-45-monitoring-grafana-dashboard) |
| **Package manager** | Trình quản lý gói phần mềm (`apt`, `dnf`) | [Ngày 3](./Giai-doan-1-Linux-SysOps.md#ngày-3-linux-quản-lý-tiến-trình-phần-mềm) |
| **Path** (absolute/relative)** | Đường dẫn (tuyệt đối/tương đối) | [Ngày 2](./Giai-doan-1-Linux-SysOps.md#ngày-2-linux-cơ-bản-điều-hướng-quản-lý-file) |
| **Permission** (rwx)** | Quyền đọc/ghi/chạy | [Ngày 4](./Giai-doan-1-Linux-SysOps.md#ngày-4-linux-người-dùng-nhóm-phân-quyền) |
| **Persistent data** | Dữ liệu bền vững (giữ qua restart) | [Ngày 19](./Giai-doan-2-Git-Docker-Cloud.md#ngày-19-docker-volume-network-dữ-liệu-bền-vững) |
| **pg_dump` / `mysqldump** | Công cụ backup DB nhất quán | [Ngày 24](./Giai-doan-2-Git-Docker-Cloud.md#ngày-24-cơ-sở-dữ-liệu-cho-devops) |
| **Pipeline** | Dây chuyền tự động chạy các bước build/test/deploy | [Ngày 1](./Giai-doan-1-Linux-SysOps.md#ngày-1-devops-sysops-là-gì-tổng-quan-toàn-ngành) |
| **plan / apply / destroy** | Xem trước / thực thi / xoá | [Ngày 29](./Giai-doan-2-Git-Docker-Cloud.md#ngày-29-infrastructure-as-code-giới-thiệu-terraform) |
| **Platform Engineering** | Xây nền tảng nội bộ như một **sản phẩm**, lập trình viên là khách hàng | [Ngày 55](./Giai-doan-4-SRE-Capstone.md#ngày-55-platform-engineering-developer-experience) |
| **Playbook** | File YAML mô tả trạng thái mong muốn của các máy | [Ngày 47](./Giai-doan-3-CICD-K8s-Monitoring.md#ngày-47-configuration-management-ansible) |
| **Pod** | Đơn vị nhỏ nhất K8s quản lý; **đồ dùng một lần**, chết là thay cái mới | [Ngày 36](./Giai-doan-3-CICD-K8s-Monitoring.md#ngày-36-kubernetes-khái-niệm-kiến-trúc) |
| **PodDisruptionBudget** | Đảm bảo tối thiểu N pod sống khi node được bảo trì | [Ngày 41](./Giai-doan-3-CICD-K8s-Monitoring.md#ngày-41-kubernetes-health-check-resource-autoscaling) |
| **Port** | Cổng — điểm vào của một dịch vụ trên máy | [Ngày 7](./Giai-doan-1-Linux-SysOps.md#ngày-7-mạng-máy-tính-cho-devops-cơ-bản) |
| **Port mapping** (`-p`)** | Ánh xạ cổng host ↔ container | [Ngày 16](./Giai-doan-2-Git-Docker-Cloud.md#ngày-16-docker-khái-niệm-container-đầu-tiên) |
| **Postmortem không đổ lỗi** | Mổ xẻ sự cố hỏi 'hệ thống nào cho phép sai sót gây hậu quả', không hỏi 'ai sai' | [Ngày 51](./Giai-doan-4-SRE-Capstone.md#ngày-51-site-reliability-engineering-sre-nguyên-lý) |
| **prevent_destroy** | Chặn xoá nhầm tài nguyên quan trọng | [Ngày 48](./Giai-doan-3-CICD-K8s-Monitoring.md#ngày-48-terraform-nâng-cao-module-remote-state-workspace) |
| **Process / PID** | Tiến trình / số định danh tiến trình | [Ngày 3](./Giai-doan-1-Linux-SysOps.md#ngày-3-linux-quản-lý-tiến-trình-phần-mềm) |
| **profiles** | Bật/tắt nhóm service theo môi trường | [Ngày 20](./Giai-doan-2-Git-Docker-Cloud.md#ngày-20-docker-compose-quản-lý-multi-container) |
| **PromQL** | Ngôn ngữ truy vấn metric của Prometheus | [Ngày 44](./Giai-doan-3-CICD-K8s-Monitoring.md#ngày-44-monitoring-prometheus-metrics) |
| **Promtail / Alloy** | Tác nhân đọc log container, gắn nhãn, đẩy về Loki | [Ngày 46](./Giai-doan-3-CICD-K8s-Monitoring.md#ngày-46-logging-tập-trung-loki) |
| **provider / resource** | Nhà cung cấp / tài nguyên cần tạo | [Ngày 29](./Giai-doan-2-Git-Docker-Cloud.md#ngày-29-infrastructure-as-code-giới-thiệu-terraform) |
| **Provisioning** | Khai báo datasource và dashboard bằng file để Grafana tự nạp | [Ngày 45](./Giai-doan-3-CICD-K8s-Monitoring.md#ngày-45-monitoring-grafana-dashboard) |
| **proxy_pass** | Chuyển tiếp request tới backend | [Ngày 23](./Giai-doan-2-Git-Docker-Cloud.md#ngày-23-reverse-proxy-web-server-nginx-chuyên-sâu) |
| **prune** | Xoá file trong Git thì xoá luôn tài nguyên trong cluster — con dao hai lưỡi | [Ngày 43](./Giai-doan-3-CICD-K8s-Monitoring.md#ngày-43-gitops-argocd-triển-khai-khai-báo) |
| **Public / Private key** | Khoá công khai (chia sẻ) / khoá bí mật (giữ kín) | [Ngày 8](./Giai-doan-1-Linux-SysOps.md#ngày-8-ssh-kết-nối-quản-lý-server-từ-xa) |
| **Pull Request (PR)** | Đề nghị gộp nhánh + để review | [Ngày 15](./Giai-doan-2-Git-Docker-Cloud.md#ngày-15-github-remote-collaboration-pull-request) |
| **Pull vs Push** | Prometheus tự đi lấy (biết ngay khi target chết) vs dịch vụ tự gửi | [Ngày 44](./Giai-doan-3-CICD-K8s-Monitoring.md#ngày-44-monitoring-prometheus-metrics) |
| **push / pull / fetch** | Đẩy lên / kéo về (fetch+merge) / chỉ tải về | [Ngày 15](./Giai-doan-2-Git-Docker-Cloud.md#ngày-15-github-remote-collaboration-pull-request) |
| **Push vs Pull deployment** | CI đẩy vào hạ tầng vs tác nhân trong hạ tầng tự kéo về | [Ngày 34](./Giai-doan-3-CICD-K8s-Monitoring.md#ngày-34-cd-pipeline-tự-động-deploy-lên-server) |
| **PV / PVC** | Ổ đĩa thật / yêu cầu xin ổ đĩa; bạn chỉ viết PVC, cluster lo phần còn lại | [Ngày 39](./Giai-doan-3-CICD-K8s-Monitoring.md#ngày-39-kubernetes-configmap-secret-storage) |

## Q

| Thuật ngữ | Nghĩa | Học ở |
|---|---|---|
| **QoS class** | Guaranteed / Burstable / BestEffort — quyết định ai bị giết trước khi cạn RAM | [Ngày 41](./Giai-doan-3-CICD-K8s-Monitoring.md#ngày-41-kubernetes-health-check-resource-autoscaling) |
| **Quy tắc 3-2-1** | 3 bản sao · 2 loại phương tiện · 1 bản ở nơi khác về địa lý | [Ngày 52](./Giai-doan-4-SRE-Capstone.md#ngày-52-high-availability-scaling-disaster-recovery) |

## R

| Thuật ngữ | Nghĩa | Học ở |
|---|---|---|
| **Rate limiting** | Giới hạn số request mỗi giây từ một nguồn, chống làm ngộp máy chủ | [Ngày 28](./Giai-doan-2-Git-Docker-Cloud.md#ngày-28-triển-khai-app-lên-cloud-docker-trên-vm) |
| **readinessProbe** | Hỏi 'nhận khách được chưa?' — trượt thì **rút khỏi Service**, pod vẫn sống | [Ngày 41](./Giai-doan-3-CICD-K8s-Monitoring.md#ngày-41-kubernetes-health-check-resource-autoscaling) |
| **Rebase** | Viết lại lịch sử thành tuyến tính | [Ngày 25](./Giai-doan-2-Git-Docker-Cloud.md#ngày-25-git-nâng-cao-rebase-tag-workflow) |
| **Recording rule** | Tính sẵn truy vấn nặng theo chu kỳ, lưu thành metric mới | [Ngày 44](./Giai-doan-3-CICD-K8s-Monitoring.md#ngày-44-monitoring-prometheus-metrics) |
| **Recursive** (`-r`, `-R`)** | Đệ quy — áp dụng cho cả thư mục con | [Ngày 2](./Giai-doan-1-Linux-SysOps.md#ngày-2-linux-cơ-bản-điều-hướng-quản-lý-file) |
| **RED / USE** | Rate-Errors-Duration (dịch vụ) / Utilization-Saturation-Errors (tài nguyên) | [Ngày 45](./Giai-doan-3-CICD-K8s-Monitoring.md#ngày-45-monitoring-grafana-dashboard) |
| **Redirect** (`>`, `>>`)** | Chuyển hướng output ra file (ghi đè/nối) | [Ngày 6](./Giai-doan-1-Linux-SysOps.md#ngày-6-bash-scripting-nâng-cao-tự-động-hóa) |
| **reflog** | Sổ ghi mọi thao tác — nơi cứu commit mất | [Ngày 13](./Giai-doan-2-Git-Docker-Cloud.md#ngày-13-git-cơ-bản-quản-lý-phiên-bản) |
| **Region** | Khu vực địa lý đặt trung tâm dữ liệu; ảnh hưởng độ trễ, giá, tuân thủ pháp lý | [Ngày 26](./Giai-doan-2-Git-Docker-Cloud.md#ngày-26-làm-quen-cloud-khái-niệm-free-tier) |
| **Registry** | Kho chứa image (GHCR, Docker Hub, ECR); nơi image sống sau khi runner bị xoá | [Ngày 33](./Giai-doan-3-CICD-K8s-Monitoring.md#ngày-33-cd-pipeline-build-push-docker-image) |
| **Registry / Docker Hub** | Kho chứa image | [Ngày 16](./Giai-doan-2-Git-Docker-Cloud.md#ngày-16-docker-khái-niệm-container-đầu-tiên) |
| **Release** | Một lần cài chart vào cluster, có tên riêng | [Ngày 42](./Giai-doan-3-CICD-K8s-Monitoring.md#ngày-42-helm-package-manager-cho-kubernetes) |
| **Remote / origin** | Repo trên server / tên mặc định của remote | [Ngày 15](./Giai-doan-2-Git-Docker-Cloud.md#ngày-15-github-remote-collaboration-pull-request) |
| **Remote state** | State lưu ở kho dùng chung (S3/GCS) thay vì trên máy cá nhân | [Ngày 48](./Giai-doan-3-CICD-K8s-Monitoring.md#ngày-48-terraform-nâng-cao-module-remote-state-workspace) |
| **Replica** | Bản sao của pod. `replicas: 3` = muốn 3 bản sao giống nhau | [Ngày 37](./Giai-doan-3-CICD-K8s-Monitoring.md#ngày-37-kubernetes-pod-deployment-replicaset) |
| **Replication** | Nhân bản DB để HA/đọc mở rộng | [Ngày 24](./Giai-doan-2-Git-Docker-Cloud.md#ngày-24-cơ-sở-dữ-liệu-cho-devops) |
| **Repo cấu hình** | Repo riêng chứa YAML/Helm values; tách khỏi repo mã nguồn | [Ngày 43](./Giai-doan-3-CICD-K8s-Monitoring.md#ngày-43-gitops-argocd-triển-khai-khai-báo) |
| **Repository (repo)** | Kho chứa mã nguồn (kèm lịch sử thay đổi) | [Ngày 1](./Giai-doan-1-Linux-SysOps.md#ngày-1-devops-sysops-là-gì-tổng-quan-toàn-ngành) · [Ngày 13](./Giai-doan-2-Git-Docker-Cloud.md#ngày-13-git-cơ-bản-quản-lý-phiên-bản) |
| **requests** | Tài nguyên đặt chỗ; Scheduler dùng để xếp node, HPA dùng làm mẫu số | [Ngày 41](./Giai-doan-3-CICD-K8s-Monitoring.md#ngày-41-kubernetes-health-check-resource-autoscaling) |
| **Reserved / Committed use** | Cam kết 1–3 năm để giảm 30–70%; chỉ dùng cho tải nền ổn định | [Ngày 53](./Giai-doan-4-SRE-Capstone.md#ngày-53-cost-optimization-finops) |
| **restart: unless-stopped** | Tự bật lại container sau khi máy khởi động lại, trừ khi bạn chủ động dừng | [Ngày 28](./Giai-doan-2-Git-Docker-Cloud.md#ngày-28-triển-khai-app-lên-cloud-docker-trên-vm) |
| **Retention** | Thời gian giữ log — quyết định về **tiền**, không phải kỹ thuật | [Ngày 46](./Giai-doan-3-CICD-K8s-Monitoring.md#ngày-46-logging-tập-trung-loki) |
| **Retention policy** | Chính sách giữ/xoá backup cũ | [Ngày 6](./Giai-doan-1-Linux-SysOps.md#ngày-6-bash-scripting-nâng-cao-tự-động-hóa) |
| **Retry storm** | Thử lại đồng loạt làm tăng tải đúng lúc dịch vụ đang yếu | [Ngày 54](./Giai-doan-4-SRE-Capstone.md#ngày-54-service-mesh-microservices-nâng-cao) |
| **Reverse proxy** | Máy chủ đứng trước ứng dụng, nhận request thay rồi chuyển vào trong | [Ngày 23](./Giai-doan-2-Git-Docker-Cloud.md#ngày-23-reverse-proxy-web-server-nginx-chuyên-sâu) · [Ngày 28](./Giai-doan-2-Git-Docker-Cloud.md#ngày-28-triển-khai-app-lên-cloud-docker-trên-vm) |
| **Revision** | Mỗi lần upgrade tạo một đời mới — `helm history` xem, `helm rollback` quay lui | [Ngày 42](./Giai-doan-3-CICD-K8s-Monitoring.md#ngày-42-helm-package-manager-cho-kubernetes) |
| **Right-sizing** | Điều chỉnh về mức dùng thật + 20–30% dự phòng | [Ngày 53](./Giai-doan-4-SRE-Capstone.md#ngày-53-cost-optimization-finops) |
| **Role** | Cách đóng gói playbook để dùng lại — như thư viện | [Ngày 47](./Giai-doan-3-CICD-K8s-Monitoring.md#ngày-47-configuration-management-ansible) |
| **Rollback** | Quay về bản trước bằng cách deploy lại tag SHA cũ | [Ngày 34](./Giai-doan-3-CICD-K8s-Monitoring.md#ngày-34-cd-pipeline-tự-động-deploy-lên-server) · [Ngày 37](./Giai-doan-3-CICD-K8s-Monitoring.md#ngày-37-kubernetes-pod-deployment-replicaset) |
| **Rolling update** | Cập nhật cuốn chiếu, thay từng pod một để không downtime | [Ngày 37](./Giai-doan-3-CICD-K8s-Monitoring.md#ngày-37-kubernetes-pod-deployment-replicaset) |
| **root / superuser** | Tài khoản quyền tối cao | [Ngày 4](./Giai-doan-1-Linux-SysOps.md#ngày-4-linux-người-dùng-nhóm-phân-quyền) |
| **Root** (`/`)** | Gốc của cây thư mục Linux | [Ngày 2](./Giai-doan-1-Linux-SysOps.md#ngày-2-linux-cơ-bản-điều-hướng-quản-lý-file) |
| **RPO** | Lượng dữ liệu tối đa chấp nhận mất, tính bằng thời gian | [Ngày 52](./Giai-doan-4-SRE-Capstone.md#ngày-52-high-availability-scaling-disaster-recovery) |
| **RPO / RTO** | Mất tối đa bao nhiêu dữ liệu / khôi phục trong bao lâu | [Ngày 11](./Giai-doan-1-Linux-SysOps.md#ngày-11-lưu-trữ-backup-khôi-phục) |
| **RTO** | Thời gian tối đa để khôi phục | [Ngày 52](./Giai-doan-4-SRE-Capstone.md#ngày-52-high-availability-scaling-disaster-recovery) |
| **Runbook** | Hướng dẫn xử lý kèm theo cảnh báo — dấu hiệu của đội chuyên nghiệp | [Ngày 45](./Giai-doan-3-CICD-K8s-Monitoring.md#ngày-45-monitoring-grafana-dashboard) |
| **Runner** | Máy ảo chạy job — **sạch mỗi lần chạy** | [Ngày 31](./Giai-doan-3-CICD-K8s-Monitoring.md#ngày-31-cicd-khái-niệm-github-actions-cơ-bản) |
| **RWO / RWX** | ReadWriteOnce (một node ghi) / ReadWriteMany (nhiều node cùng ghi) | [Ngày 39](./Giai-doan-3-CICD-K8s-Monitoring.md#ngày-39-kubernetes-configmap-secret-storage) |

## S

| Thuật ngữ | Nghĩa | Học ở |
|---|---|---|
| **SBOM** | Danh mục thành phần phần mềm — trả lời 'ta có dùng thư viện dính CVE không?' | [Ngày 33](./Giai-doan-3-CICD-K8s-Monitoring.md#ngày-33-cd-pipeline-build-push-docker-image) · [Ngày 49](./Giai-doan-3-CICD-K8s-Monitoring.md#ngày-49-bảo-mật-devsecops-best-practices) |
| **Scaffolding** | Sinh project chuẩn từ khuôn mẫu bằng một lệnh | [Ngày 55](./Giai-doan-4-SRE-Capstone.md#ngày-55-platform-engineering-developer-experience) |
| **Scale up vs out** | Máy to hơn (không giúp HA) vs thêm nhiều máy (có giúp HA) | [Ngày 52](./Giai-doan-4-SRE-Capstone.md#ngày-52-high-availability-scaling-disaster-recovery) |
| **scp / rsync** | Copy file qua SSH / đồng bộ thư mục hiệu quả | [Ngày 8](./Giai-doan-1-Linux-SysOps.md#ngày-8-ssh-kết-nối-quản-lý-server-từ-xa) |
| **Scrape / Target** | Việc Prometheus đi hỏi / nơi bị hỏi | [Ngày 44](./Giai-doan-3-CICD-K8s-Monitoring.md#ngày-44-monitoring-prometheus-metrics) |
| **Script** | File chứa chuỗi lệnh để máy tự chạy | [Ngày 5](./Giai-doan-1-Linux-SysOps.md#ngày-5-bash-scripting-cơ-bản) |
| **Sealed Secrets / SOPS** | Mã hoá thật để commit bí mật vào Git an toàn | [Ngày 39](./Giai-doan-3-CICD-K8s-Monitoring.md#ngày-39-kubernetes-configmap-secret-storage) |
| **Secret** | Nơi chứa dữ liệu nhạy cảm — **chỉ base64, KHÔNG phải mã hoá** | [Ngày 9](./Giai-doan-1-Linux-SysOps.md#ngày-9-tường-lửa-bảo-mật-hardening) · [Ngày 39](./Giai-doan-3-CICD-K8s-Monitoring.md#ngày-39-kubernetes-configmap-secret-storage) |
| **Security Group** | Tường lửa ở tầng cloud, đứng trước máy; mặc định chặn hết chiều vào | [Ngày 27](./Giai-doan-2-Git-Docker-Cloud.md#ngày-27-máy-chủ-cloud-tạo-quản-lý-vm) |
| **Selector / Label** | Nhãn dán lên đối tượng + câu điều kiện chọn theo nhãn | [Ngày 37](./Giai-doan-3-CICD-K8s-Monitoring.md#ngày-37-kubernetes-pod-deployment-replicaset) · [Ngày 38](./Giai-doan-3-CICD-K8s-Monitoring.md#ngày-38-kubernetes-service-networking) |
| **Self-healing** | K8s tự tạo lại pod khi pod chết, để luôn đủ số mong muốn | [Ngày 37](./Giai-doan-3-CICD-K8s-Monitoring.md#ngày-37-kubernetes-pod-deployment-replicaset) |
| **Self-hosted runner** | Máy của bạn tự cắm vào GitHub nhận việc; không cần IP public | [Ngày 34](./Giai-doan-3-CICD-K8s-Monitoring.md#ngày-34-cd-pipeline-tự-động-deploy-lên-server) |
| **selfHeal** | Tự hoàn tác mọi thay đổi thủ công trên cluster | [Ngày 43](./Giai-doan-3-CICD-K8s-Monitoring.md#ngày-43-gitops-argocd-triển-khai-khai-báo) |
| **Semantic Versioning** | Đánh số MAJOR.MINOR.PATCH có quy tắc | [Ngày 25](./Giai-doan-2-Git-Docker-Cloud.md#ngày-25-git-nâng-cao-rebase-tag-workflow) |
| **serial** | Cập nhật lần lượt từng nhóm máy thay vì tất cả cùng lúc | [Ngày 47](./Giai-doan-3-CICD-K8s-Monitoring.md#ngày-47-configuration-management-ansible) |
| **Service** | Địa chỉ cố định đứng trước nhóm pod hay thay đổi; tự chia tải | [Ngày 20](./Giai-doan-2-Git-Docker-Cloud.md#ngày-20-docker-compose-quản-lý-multi-container) · [Ngày 38](./Giai-doan-3-CICD-K8s-Monitoring.md#ngày-38-kubernetes-service-networking) |
| **Service / daemon** | Dịch vụ chạy nền liên tục (nginx, database...) | [Ngày 3](./Giai-doan-1-Linux-SysOps.md#ngày-3-linux-quản-lý-tiến-trình-phần-mềm) |
| **Service mesh** | Proxy cạnh mỗi dịch vụ lo timeout/retry/mTLS/đo lường thay ứng dụng | [Ngày 54](./Giai-doan-4-SRE-Capstone.md#ngày-54-service-mesh-microservices-nâng-cao) |
| **Shared Responsibility** | Nhà cung cấp lo bảo mật *của* cloud, bạn lo bảo mật *trong* cloud | [Ngày 26](./Giai-doan-2-Git-Docker-Cloud.md#ngày-26-làm-quen-cloud-khái-niệm-free-tier) |
| **Shebang** (`#!/bin/bash`)** | Dòng đầu chỉ định trình thông dịch | [Ngày 5](./Giai-doan-1-Linux-SysOps.md#ngày-5-bash-scripting-cơ-bản) |
| **Shift-left** | Đẩy kiểm tra về sớm trong vòng đời — càng sớm càng rẻ | [Ngày 49](./Giai-doan-3-CICD-K8s-Monitoring.md#ngày-49-bảo-mật-devsecops-best-practices) |
| **Sidecar** | Container proxy chạy cạnh app trong cùng pod | [Ngày 54](./Giai-doan-4-SRE-Capstone.md#ngày-54-service-mesh-microservices-nâng-cao) |
| **Signal** (TERM/KILL)** | Tín hiệu gửi cho tiến trình (dừng lịch sự / ép tắt) | [Ngày 3](./Giai-doan-1-Linux-SysOps.md#ngày-3-linux-quản-lý-tiến-trình-phần-mềm) |
| **SLA** | Cam kết với khách hàng, vi phạm là đền tiền; luôn **lỏng hơn** SLO | [Ngày 51](./Giai-doan-4-SRE-Capstone.md#ngày-51-site-reliability-engineering-sre-nguyên-lý) |
| **SLI** | Chỉ số **đo được**: tỉ lệ request thành công, p95 độ trễ | [Ngày 51](./Giai-doan-4-SRE-Capstone.md#ngày-51-site-reliability-engineering-sre-nguyên-lý) |
| **SLO** | Mục tiêu **nội bộ** đặt cho SLI (ví dụ ≥ 99,9% trong 30 ngày) | [Ngày 51](./Giai-doan-4-SRE-Capstone.md#ngày-51-site-reliability-engineering-sre-nguyên-lý) |
| **Snapshot** | Ảnh chụp tức thời của dữ liệu/hệ thống | [Ngày 11](./Giai-doan-1-Linux-SysOps.md#ngày-11-lưu-trữ-backup-khôi-phục) |
| **SPOF** | Điểm chết đơn lẻ — thành phần mà nó chết là cả hệ thống chết | [Ngày 52](./Giai-doan-4-SRE-Capstone.md#ngày-52-high-availability-scaling-disaster-recovery) |
| **Spot instance** | Rẻ 60–90% nhưng **có thể bị thu hồi bất cứ lúc nào** | [Ngày 53](./Giai-doan-4-SRE-Capstone.md#ngày-53-cost-optimization-finops) |
| **SQL / NoSQL** | CSDL quan hệ / phi quan hệ | [Ngày 24](./Giai-doan-2-Git-Docker-Cloud.md#ngày-24-cơ-sở-dữ-liệu-cho-devops) |
| **Squash** | Gộp nhiều commit thành 1 | [Ngày 25](./Giai-doan-2-Git-Docker-Cloud.md#ngày-25-git-nâng-cao-rebase-tag-workflow) |
| **SSH** | Giao thức đăng nhập server từ xa an toàn (mã hoá) | [Ngày 8](./Giai-doan-1-Linux-SysOps.md#ngày-8-ssh-kết-nối-quản-lý-server-từ-xa) |
| **SSH key** | Cặp khoá (private + public) để xác thực an toàn không cần mật khẩu | [Ngày 1](./Giai-doan-1-Linux-SysOps.md#ngày-1-devops-sysops-là-gì-tổng-quan-toàn-ngành) |
| **SSH tunnel** (`-L`)** | Đường hầm mã hoá tới dịch vụ nội bộ | [Ngày 8](./Giai-doan-1-Linux-SysOps.md#ngày-8-ssh-kết-nối-quản-lý-server-từ-xa) |
| **ssh-keyscan** | Nạp host key trước khi SSH tự động, tránh treo chờ xác nhận | [Ngày 34](./Giai-doan-3-CICD-K8s-Monitoring.md#ngày-34-cd-pipeline-tự-động-deploy-lên-server) |
| **SSL/TLS termination** | nginx giải mã HTTPS thay backend | [Ngày 23](./Giai-doan-2-Git-Docker-Cloud.md#ngày-23-reverse-proxy-web-server-nginx-chuyên-sâu) |
| **Staging area** | Khu vực chuẩn bị file cho commit | [Ngày 13](./Giai-doan-2-Git-Docker-Cloud.md#ngày-13-git-cơ-bản-quản-lý-phiên-bản) |
| **startupProbe** | Hỏi 'khởi động xong chưa?' — tạm hoãn hai probe kia trong lúc app đang lên | [Ngày 41](./Giai-doan-3-CICD-K8s-Monitoring.md#ngày-41-kubernetes-health-check-resource-autoscaling) |
| **stash** | Cất tạm thay đổi chưa commit | [Ngày 14](./Giai-doan-2-Git-Docker-Cloud.md#ngày-14-git-branch-merge-xử-lý-conflict) |
| **State** | Sổ ghi ánh xạ code ↔ tài nguyên thật; mất nó là Terraform mù | [Ngày 48](./Giai-doan-3-CICD-K8s-Monitoring.md#ngày-48-terraform-nâng-cao-module-remote-state-workspace) |
| **state file** | Bản đồ trạng thái hạ tầng | [Ngày 29](./Giai-doan-2-Git-Docker-Cloud.md#ngày-29-infrastructure-as-code-giới-thiệu-terraform) |
| **State locking** | Khoá state khi đang apply, chặn người thứ hai ghi đè | [Ngày 48](./Giai-doan-3-CICD-K8s-Monitoring.md#ngày-48-terraform-nâng-cao-module-remote-state-workspace) |
| **Stateless** | Không giữ trạng thái trong bộ nhớ app — điều kiện để nhân bản thoải mái | [Ngày 52](./Giai-doan-4-SRE-Capstone.md#ngày-52-high-availability-scaling-disaster-recovery) |
| **stdout / stderr** | Luồng ra chuẩn / luồng lỗi chuẩn (`2>`) | [Ngày 6](./Giai-doan-1-Linux-SysOps.md#ngày-6-bash-scripting-nâng-cao-tự-động-hóa) |
| **stop vs terminate** | Tắt (giữ ổ đĩa, vẫn tính tiền) vs xoá hẳn (hết tính tiền) | [Ngày 27](./Giai-doan-2-Git-Docker-Cloud.md#ngày-27-máy-chủ-cloud-tạo-quản-lý-vm) |
| **StorageClass** | Nhà cung cấp ổ đĩa — tự tạo PV khi có PVC | [Ngày 39](./Giai-doan-3-CICD-K8s-Monitoring.md#ngày-39-kubernetes-configmap-secret-storage) |
| **strategy: Recreate** | Xoá pod cũ rồi mới tạo mới — bắt buộc cho database dùng ổ RWO | [Ngày 39](./Giai-doan-3-CICD-K8s-Monitoring.md#ngày-39-kubernetes-configmap-secret-storage) |
| **Structured logging** | Ghi log dạng JSON để lọc được theo trường, không phải khớp chuỗi | [Ngày 46](./Giai-doan-3-CICD-K8s-Monitoring.md#ngày-46-logging-tập-trung-loki) |
| **sudo** | Chạy 1 lệnh với quyền cao (mượn quyền admin) | [Ngày 4](./Giai-doan-1-Linux-SysOps.md#ngày-4-linux-người-dùng-nhóm-phân-quyền) |
| **SUID** | Cờ đặc biệt: file chạy với quyền của chủ file | [Ngày 4](./Giai-doan-1-Linux-SysOps.md#ngày-4-linux-người-dùng-nhóm-phân-quyền) |
| **Supply chain attack** | Tấn công qua thư viện/action/image bên thứ ba | [Ngày 49](./Giai-doan-3-CICD-K8s-Monitoring.md#ngày-49-bảo-mật-devsecops-best-practices) |
| **Synced / OutOfSync** | Cluster có khớp Git không | [Ngày 43](./Giai-doan-3-CICD-K8s-Monitoring.md#ngày-43-gitops-argocd-triển-khai-khai-báo) |
| **systemd / systemctl** | Hệ quản lý dịch vụ của Linux / lệnh điều khiển nó | [Ngày 3](./Giai-doan-1-Linux-SysOps.md#ngày-3-linux-quản-lý-tiến-trình-phần-mềm) |

## T

| Thuật ngữ | Nghĩa | Học ở |
|---|---|---|
| **Tag** | Nhãn phiên bản của image (`:1.0`) | [Ngày 17](./Giai-doan-2-Git-Docker-Cloud.md#ngày-17-docker-dockerfile-build-image) · [Ngày 25](./Giai-doan-2-Git-Docker-Cloud.md#ngày-25-git-nâng-cao-rebase-tag-workflow) |
| **Tag bất biến** | Tag không bao giờ bị ghi đè (thường là SHA commit) — điều kiện để rollback | [Ngày 33](./Giai-doan-3-CICD-K8s-Monitoring.md#ngày-33-cd-pipeline-build-push-docker-image) |
| **Tagging** | Gắn thẻ để quy trách nhiệm chi phí — nền móng của mọi việc còn lại | [Ngày 53](./Giai-doan-4-SRE-Capstone.md#ngày-53-cost-optimization-finops) |
| **Tài nguyên mồ côi** | Ổ đĩa, IP, snapshot không ai dùng nhưng vẫn tính tiền | [Ngày 53](./Giai-doan-4-SRE-Capstone.md#ngày-53-cost-optimization-finops) |
| **TCP / UDP** | Hai giao thức giao vận (tin cậy / nhanh) | [Ngày 7](./Giai-doan-1-Linux-SysOps.md#ngày-7-mạng-máy-tính-cho-devops-cơ-bản) |
| **Terraform / HCL** | Công cụ IaC / ngôn ngữ của nó | [Ngày 29](./Giai-doan-2-Git-Docker-Cloud.md#ngày-29-infrastructure-as-code-giới-thiệu-terraform) |
| **terraform import** | Đưa hạ tầng đã có sẵn vào quản lý của Terraform | [Ngày 48](./Giai-doan-3-CICD-K8s-Monitoring.md#ngày-48-terraform-nâng-cao-module-remote-state-workspace) |
| **terraform plan** | Xem trước thay đổi; chú ý dòng `-/+` = **huỷ rồi tạo lại** | [Ngày 48](./Giai-doan-3-CICD-K8s-Monitoring.md#ngày-48-terraform-nâng-cao-module-remote-state-workspace) |
| **Test coverage** | Tỉ lệ code được test chạy qua; cao **không** chứng minh chất lượng | [Ngày 32](./Giai-doan-3-CICD-K8s-Monitoring.md#ngày-32-ci-pipeline-build-test-lint-tự-động) |
| **Threshold** | Ngưỡng màu trên panel — để liếc 2 giây là biết có chuyện | [Ngày 45](./Giai-doan-3-CICD-K8s-Monitoring.md#ngày-45-monitoring-grafana-dashboard) |
| **Timeout** | Chờ tối đa bao lâu rồi bỏ — **tấm khiên quan trọng nhất** | [Ngày 54](./Giai-doan-4-SRE-Capstone.md#ngày-54-service-mesh-microservices-nâng-cao) |
| **tmpfs** | Lưu trong RAM, không bền vững | [Ngày 19](./Giai-doan-2-Git-Docker-Cloud.md#ngày-19-docker-volume-network-dữ-liệu-bền-vững) |
| **Toil** | Việc thủ công lặp lại không sinh giá trị; SRE giới hạn ở 50% thời gian | [Ngày 51](./Giai-doan-4-SRE-Capstone.md#ngày-51-site-reliability-engineering-sre-nguyên-lý) |
| **trace_id** | Mã định danh chung cho một request qua nhiều dịch vụ — cầu nối sang tracing | [Ngày 46](./Giai-doan-3-CICD-K8s-Monitoring.md#ngày-46-logging-tập-trung-loki) |
| **Trigger (`on:`)** | Sự kiện kích hoạt workflow: push, pull_request, schedule... | [Ngày 31](./Giai-doan-3-CICD-K8s-Monitoring.md#ngày-31-cicd-khái-niệm-github-actions-cơ-bản) |
| **Trivy** | Quét lỗ hổng trong thư viện và image | [Ngày 49](./Giai-doan-3-CICD-K8s-Monitoring.md#ngày-49-bảo-mật-devsecops-best-practices) |

## U

| Thuật ngữ | Nghĩa | Học ở |
|---|---|---|
| **up** | Metric Prometheus tự sinh: 1 = scrape thành công, 0 = thất bại | [Ngày 44](./Giai-doan-3-CICD-K8s-Monitoring.md#ngày-44-monitoring-prometheus-metrics) |
| **upstream** | Nhóm backend để load balance | [Ngày 23](./Giai-doan-2-Git-Docker-Cloud.md#ngày-23-reverse-proxy-web-server-nginx-chuyên-sâu) |
| **USER** | Chỉ thị chạy container bằng user không-root | [Ngày 18](./Giai-doan-2-Git-Docker-Cloud.md#ngày-18-docker-image-tối-ưu-multi-stage-build) |
| **User / Group** | Người dùng / nhóm người dùng | [Ngày 4](./Giai-doan-1-Linux-SysOps.md#ngày-4-linux-người-dùng-nhóm-phân-quyền) |

## V

| Thuật ngữ | Nghĩa | Học ở |
|---|---|---|
| **Values** | Giá trị truyền vào chart để điền chỗ trống | [Ngày 42](./Giai-doan-3-CICD-K8s-Monitoring.md#ngày-42-helm-package-manager-cho-kubernetes) |
| **Variable** | Biến — hộp đựng giá trị | [Ngày 5](./Giai-doan-1-Linux-SysOps.md#ngày-5-bash-scripting-cơ-bản) |
| **version` vs `appVersion** | Phiên bản của *chart* vs phiên bản của *ứng dụng* | [Ngày 42](./Giai-doan-3-CICD-K8s-Monitoring.md#ngày-42-helm-package-manager-cho-kubernetes) |
| **Volume** | Ổ lưu dữ liệu bền vững do Docker quản lý | [Ngày 16](./Giai-doan-2-Git-Docker-Cloud.md#ngày-16-docker-khái-niệm-container-đầu-tiên) · [Ngày 19](./Giai-doan-2-Git-Docker-Cloud.md#ngày-19-docker-volume-network-dữ-liệu-bền-vững) |
| **Vòng điều hoà (reconciliation loop)** | So mong muốn với thực tế rồi sửa cho khớp — gốc của mọi tính năng K8s | [Ngày 36](./Giai-doan-3-CICD-K8s-Monitoring.md#ngày-36-kubernetes-khái-niệm-kiến-trúc) |

## W

| Thuật ngữ | Nghĩa | Học ở |
|---|---|---|
| **Workflow / Job / Step** | Cả quy trình (1 file YAML) / nhóm việc trên 1 máy / từng bước trong job | [Ngày 31](./Giai-doan-3-CICD-K8s-Monitoring.md#ngày-31-cicd-khái-niệm-github-actions-cơ-bản) |
| **workflow_run** | Trigger chạy workflow này sau khi workflow kia kết thúc | [Ngày 34](./Giai-doan-3-CICD-K8s-Monitoring.md#ngày-34-cd-pipeline-tự-động-deploy-lên-server) |
| **Working directory** | Thư mục làm việc — nơi sửa file | [Ngày 13](./Giai-doan-2-Git-Docker-Cloud.md#ngày-13-git-cơ-bản-quản-lý-phiên-bản) |
| **Works on my machine** | Câu nói kinh điển khi code chạy ở máy Dev nhưng lỗi trên server | [Ngày 1](./Giai-doan-1-Linux-SysOps.md#ngày-1-devops-sysops-là-gì-tổng-quan-toàn-ngành) |
| **Workspace** | Nhiều file state cho cùng một bộ code | [Ngày 48](./Giai-doan-3-CICD-K8s-Monitoring.md#ngày-48-terraform-nâng-cao-module-remote-state-workspace) |

## Y

| Thuật ngữ | Nghĩa | Học ở |
|---|---|---|
| **YAML** | Định dạng cấu hình dựa trên thụt lề | [Ngày 22](./Giai-doan-2-Git-Docker-Cloud.md#ngày-22-yaml-json-định-dạng-cấu-hình) |

---

## Cách dùng file này

| Tình huống | Làm gì |
|---|---|
| Gặp thuật ngữ lạ khi đọc bài | `Ctrl+F` tìm ở đây trước, chưa rõ thì bấm link sang bài gốc |
| Ôn trước phỏng vấn | Đọc lướt cột *Thuật ngữ*, cái nào không tự giải thích được thì quay lại bài đó |
| Tự kiểm tra | Che cột *Nghĩa*, đọc tên thuật ngữ và tự nói lại định nghĩa |

> 💡 **Mẹo ôn tập:** thuật ngữ bạn *đọc hiểu* khác với thuật ngữ bạn *giải thích được cho người khác*. Chỉ cái thứ hai mới dùng được lúc phỏng vấn.
