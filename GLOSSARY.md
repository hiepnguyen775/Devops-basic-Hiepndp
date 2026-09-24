# 📚 GLOSSARY — Từ điển thuật ngữ DevOps

> Toàn bộ thuật ngữ xuất hiện trong khoá học, kèm **ngày học nó**. Bấm vào số ngày để nhảy tới bài giảng đầy đủ.

**171 thuật ngữ** · Trích tự động từ mục 📚 Thuật ngữ của các ngày học.

## Mục lục nhanh

[A](#a) · [B](#b) · [C](#c) · [D](#d) · [E](#e) · [F](#f) · [H](#h) · [I](#i) · [J](#j) · [K](#k) · [#](#ký-hiệu) · [L](#l) · [M](#m) · [N](#n) · [O](#o) · [P](#p) · [R](#r) · [S](#s) · [T](#t) · [U](#u) · [V](#v) · [W](#w) · [Y](#y)

---

## A

| Thuật ngữ | Nghĩa | Học ở |
|---|---|---|
| **ACID** | Đảm bảo giao dịch chính xác | [Ngày 24](./Giai-doan-2-Git-Docker-Cloud.md#ngày-24-cơ-sở-dữ-liệu-cho-devops) |
| **Alpine** | Bản Linux siêu nhỏ hay dùng làm base | [Ngày 18](./Giai-doan-2-Git-Docker-Cloud.md#ngày-18-docker-image-tối-ưu-multi-stage-build) |
| **Anchor & alias** (`&`, `*`)** | Định nghĩa 1 lần, tái dùng nhiều nơi | [Ngày 22](./Giai-doan-2-Git-Docker-Cloud.md#ngày-22-yaml-json-định-dạng-cấu-hình) |
| **Argument / Parameter** | Tham số truyền vào script (`$1`, `$2`) | [Ngày 5](./Giai-doan-1-Linux-SysOps.md#ngày-5-bash-scripting-cơ-bản) |
| **Array** | Mảng — danh sách nhiều giá trị | [Ngày 6](./Giai-doan-1-Linux-SysOps.md#ngày-6-bash-scripting-nâng-cao-tự-động-hóa) |
| **authorized_keys** | File chứa các public key được phép vào server | [Ngày 8](./Giai-doan-1-Linux-SysOps.md#ngày-8-ssh-kết-nối-quản-lý-server-từ-xa) |
| **Automation** | Tự động hoá — để máy làm việc lặp lại thay người | [Ngày 1](./Giai-doan-1-Linux-SysOps.md#ngày-1-devops-sysops-là-gì-tổng-quan-toàn-ngành) |

## B

| Thuật ngữ | Nghĩa | Học ở |
|---|---|---|
| **Backup / Restore** | Sao lưu / khôi phục | [Ngày 11](./Giai-doan-1-Linux-SysOps.md#ngày-11-lưu-trữ-backup-khôi-phục) |
| **Base image** | Image nền (alpine/slim/distroless) | [Ngày 18](./Giai-doan-2-Git-Docker-Cloud.md#ngày-18-docker-image-tối-ưu-multi-stage-build) |
| **Bastion / Jump host** | Máy trung gian để vào mạng nội bộ | [Ngày 8](./Giai-doan-1-Linux-SysOps.md#ngày-8-ssh-kết-nối-quản-lý-server-từ-xa) |
| **Bind mount** | Gắn thẳng thư mục host vào container | [Ngày 19](./Giai-doan-2-Git-Docker-Cloud.md#ngày-19-docker-volume-network-dữ-liệu-bền-vững) |
| **bisect** | Tìm commit gây bug bằng nhị phân | [Ngày 25](./Giai-doan-2-Git-Docker-Cloud.md#ngày-25-git-nâng-cao-rebase-tag-workflow) |
| **Brace expansion** `{a,b,c}** | Shell bung thành nhiều tên trước khi chạy lệnh | [Ngày 2](./Giai-doan-1-Linux-SysOps.md#ngày-2-linux-cơ-bản-điều-hướng-quản-lý-file) |
| **Branch** | Nhánh — dòng phát triển song song | [Ngày 14](./Giai-doan-2-Git-Docker-Cloud.md#ngày-14-git-branch-merge-xử-lý-conflict) |
| **Branch protection** | Quy tắc bảo vệ nhánh chính | [Ngày 15](./Giai-doan-2-Git-Docker-Cloud.md#ngày-15-github-remote-collaboration-pull-request) |
| **Build context** | Thư mục gửi cho Docker khi build (dấu `.`) | [Ngày 17](./Giai-doan-2-Git-Docker-Cloud.md#ngày-17-docker-dockerfile-build-image) |

## C

| Thuật ngữ | Nghĩa | Học ở |
|---|---|---|
| **Cache** | Docker tái dùng layer không đổi để build nhanh | [Ngày 17](./Giai-doan-2-Git-Docker-Cloud.md#ngày-17-docker-dockerfile-build-image) |
| **Checksum** (`sha256sum`)** | Chữ ký kiểm tra toàn vẹn file | [Ngày 11](./Giai-doan-1-Linux-SysOps.md#ngày-11-lưu-trữ-backup-khôi-phục) |
| **cherry-pick** | Lấy 1 commit cụ thể sang nhánh khác | [Ngày 25](./Giai-doan-2-Git-Docker-Cloud.md#ngày-25-git-nâng-cao-rebase-tag-workflow) |
| **CI/CD** | Tích hợp liên tục / Chuyển giao–Triển khai liên tục (tự build-test-deploy) | [Ngày 1](./Giai-doan-1-Linux-SysOps.md#ngày-1-devops-sysops-là-gì-tổng-quan-toàn-ngành) |
| **CIA** | Confidentiality/Integrity/Availability | [Ngày 9](./Giai-doan-1-Linux-SysOps.md#ngày-9-tường-lửa-bảo-mật-hardening) |
| **CIDR** (`/24`)** | Cách viết dải mạng | [Ngày 7](./Giai-doan-1-Linux-SysOps.md#ngày-7-mạng-máy-tính-cho-devops-cơ-bản) |
| **clone** | Sao chép repo về máy | [Ngày 15](./Giai-doan-2-Git-Docker-Cloud.md#ngày-15-github-remote-collaboration-pull-request) |
| **CMD / ENTRYPOINT** | Lệnh mặc định / lệnh chính cố định | [Ngày 17](./Giai-doan-2-Git-Docker-Cloud.md#ngày-17-docker-dockerfile-build-image) |
| **Code review** | Đọc & góp ý code trước khi merge | [Ngày 15](./Giai-doan-2-Git-Docker-Cloud.md#ngày-15-github-remote-collaboration-pull-request) |
| **Command substitution** `$( )** | Chạy lệnh rồi thay bằng kết quả | [Ngày 6](./Giai-doan-1-Linux-SysOps.md#ngày-6-bash-scripting-nâng-cao-tự-động-hóa) |
| **Commit** | Một ảnh chụp trạng thái được lưu | [Ngày 13](./Giai-doan-2-Git-Docker-Cloud.md#ngày-13-git-cơ-bản-quản-lý-phiên-bản) |
| **condition: service_healthy** | Chờ service kia khoẻ mới start | [Ngày 20](./Giai-doan-2-Git-Docker-Cloud.md#ngày-20-docker-compose-quản-lý-multi-container) |
| **Conflict** | Xung đột khi 2 nhánh sửa cùng dòng | [Ngày 14](./Giai-doan-2-Git-Docker-Cloud.md#ngày-14-git-branch-merge-xử-lý-conflict) |
| **Connection pooling** | Tái dùng kết nối DB (PgBouncer) | [Ngày 24](./Giai-doan-2-Git-Docker-Cloud.md#ngày-24-cơ-sở-dữ-liệu-cho-devops) |
| **Container** | Bản đang chạy của một image | [Ngày 16](./Giai-doan-2-Git-Docker-Cloud.md#ngày-16-docker-khái-niệm-container-đầu-tiên) |
| **Conventional Commits** | Chuẩn message (`feat:`/`fix:`) | [Ngày 25](./Giai-doan-2-Git-Docker-Cloud.md#ngày-25-git-nâng-cao-rebase-tag-workflow) |
| **COPY --from** | Chép file từ stage khác | [Ngày 18](./Giai-doan-2-Git-Docker-Cloud.md#ngày-18-docker-image-tối-ưu-multi-stage-build) |
| **Cron / crontab** | Trình hẹn giờ chạy lệnh theo lịch / bảng lịch | [Ngày 6](./Giai-doan-1-Linux-SysOps.md#ngày-6-bash-scripting-nâng-cao-tự-động-hóa) |
| **CVE** | Lỗ hổng bảo mật đã được ghi nhận | [Ngày 18](./Giai-doan-2-Git-Docker-Cloud.md#ngày-18-docker-image-tối-ưu-multi-stage-build) |

## D

| Thuật ngữ | Nghĩa | Học ở |
|---|---|---|
| **Daemon** (dockerd)** | Tiến trình nền chạy Docker | [Ngày 16](./Giai-doan-2-Git-Docker-Cloud.md#ngày-16-docker-khái-niệm-container-đầu-tiên) |
| **Declarative** | Khai báo *cái muốn* (YAML), K8s tự lo *cách đạt* | [Ngày 37](./Giai-doan-3-CICD-K8s-Monitoring.md#ngày-37-kubernetes-pod-deployment-replicaset) |
| **Defense in depth** | Phòng thủ nhiều lớp | [Ngày 9](./Giai-doan-1-Linux-SysOps.md#ngày-9-tường-lửa-bảo-mật-hardening) |
| **Deny-by-default** | Chặn hết, chỉ mở cái cần | [Ngày 9](./Giai-doan-1-Linux-SysOps.md#ngày-9-tường-lửa-bảo-mật-hardening) |
| **depends_on** | Khai báo thứ tự khởi động | [Ngày 20](./Giai-doan-2-Git-Docker-Cloud.md#ngày-20-docker-compose-quản-lý-multi-container) |
| **Detached HEAD** | Đang ở 1 commit, không trên nhánh nào | [Ngày 14](./Giai-doan-2-Git-Docker-Cloud.md#ngày-14-git-branch-merge-xử-lý-conflict) |
| **detached** (`-d`)** | Chạy container ở chế độ nền | [Ngày 16](./Giai-doan-2-Git-Docker-Cloud.md#ngày-16-docker-khái-niệm-container-đầu-tiên) |
| **DevOps** | Văn hoá + thực hành tự động hoá toàn bộ vòng đời phần mềm | [Ngày 1](./Giai-doan-1-Linux-SysOps.md#ngày-1-devops-sysops-là-gì-tổng-quan-toàn-ngành) |
| **Directory** | Thư mục | [Ngày 2](./Giai-doan-1-Linux-SysOps.md#ngày-2-linux-cơ-bản-điều-hướng-quản-lý-file) |
| **Distroless** | Image không có shell/OS thừa — an toàn nhất | [Ngày 18](./Giai-doan-2-Git-Docker-Cloud.md#ngày-18-docker-image-tối-ưu-multi-stage-build) |
| **DNS** | Hệ phân giải tên miền → IP | [Ngày 7](./Giai-doan-1-Linux-SysOps.md#ngày-7-mạng-máy-tính-cho-devops-cơ-bản) |
| **DNS nội bộ** | Gọi container bằng tên trong cùng network | [Ngày 19](./Giai-doan-2-Git-Docker-Cloud.md#ngày-19-docker-volume-network-dữ-liệu-bền-vững) |
| **Docker Compose** | Công cụ mô tả & chạy nhiều container bằng 1 file | [Ngày 20](./Giai-doan-2-Git-Docker-Cloud.md#ngày-20-docker-compose-quản-lý-multi-container) |
| **Dockerfile** | Công thức để build image | [Ngày 17](./Giai-doan-2-Git-Docker-Cloud.md#ngày-17-docker-dockerfile-build-image) |
| **Drift** | Thực tế lệch khỏi code (do sửa tay) | [Ngày 29](./Giai-doan-2-Git-Docker-Cloud.md#ngày-29-infrastructure-as-code-giới-thiệu-terraform) |

## E

| Thuật ngữ | Nghĩa | Học ở |
|---|---|---|
| **Environment variable** | Biến môi trường (vd `$PATH`) | [Ngày 3](./Giai-doan-1-Linux-SysOps.md#ngày-3-linux-quản-lý-tiến-trình-phần-mềm) |
| **Ephemeral** | Tạm thời — xoá là mất | [Ngày 19](./Giai-doan-2-Git-Docker-Cloud.md#ngày-19-docker-volume-network-dữ-liệu-bền-vững) |
| **Exit code** (`$?`)** | Mã kết thúc: 0 = ok, khác 0 = lỗi | [Ngày 5](./Giai-doan-1-Linux-SysOps.md#ngày-5-bash-scripting-cơ-bản) |

## F

| Thuật ngữ | Nghĩa | Học ở |
|---|---|---|
| **fail2ban** | Tự chặn IP dò mật khẩu | [Ngày 9](./Giai-doan-1-Linux-SysOps.md#ngày-9-tường-lửa-bảo-mật-hardening) |
| **Fast-forward** | Merge chỉ dời con trỏ (lịch sử thẳng) | [Ngày 14](./Giai-doan-2-Git-Docker-Cloud.md#ngày-14-git-branch-merge-xử-lý-conflict) |
| **Feature branch** | Nhánh riêng cho mỗi tính năng | [Ngày 14](./Giai-doan-2-Git-Docker-Cloud.md#ngày-14-git-branch-merge-xử-lý-conflict) |
| **FHS** | Filesystem Hierarchy Standard — chuẩn bố trí thư mục Linux | [Ngày 2](./Giai-doan-1-Linux-SysOps.md#ngày-2-linux-cơ-bản-điều-hướng-quản-lý-file) |
| **Firewall** | Tường lửa — kiểm soát cổng vào/ra | [Ngày 9](./Giai-doan-1-Linux-SysOps.md#ngày-9-tường-lửa-bảo-mật-hardening) |
| **Foreground / Background** | Tiền cảnh / chạy nền (`&`) | [Ngày 3](./Giai-doan-1-Linux-SysOps.md#ngày-3-linux-quản-lý-tiến-trình-phần-mềm) |
| **Fork** | Sao chép repo người khác về tài khoản mình | [Ngày 15](./Giai-doan-2-Git-Docker-Cloud.md#ngày-15-github-remote-collaboration-pull-request) |
| **Function** | Hàm — nhóm lệnh gọi lại được | [Ngày 5](./Giai-doan-1-Linux-SysOps.md#ngày-5-bash-scripting-cơ-bản) |

## H

| Thuật ngữ | Nghĩa | Học ở |
|---|---|---|
| **Hardening** | Làm cứng — siết cấu hình cho an toàn | [Ngày 9](./Giai-doan-1-Linux-SysOps.md#ngày-9-tường-lửa-bảo-mật-hardening) |
| **HEAD** | Con trỏ "đang ở commit nào" | [Ngày 13](./Giai-doan-2-Git-Docker-Cloud.md#ngày-13-git-cơ-bản-quản-lý-phiên-bản) |
| **healthcheck** | Kiểm tra dịch vụ đã sẵn sàng chưa | [Ngày 20](./Giai-doan-2-Git-Docker-Cloud.md#ngày-20-docker-compose-quản-lý-multi-container) |
| **Hidden file** | File ẩn (tên bắt đầu bằng `.`) | [Ngày 2](./Giai-doan-1-Linux-SysOps.md#ngày-2-linux-cơ-bản-điều-hướng-quản-lý-file) |
| **HTTP status code** | Mã kết quả HTTP (2xx/4xx/5xx) | [Ngày 7](./Giai-doan-1-Linux-SysOps.md#ngày-7-mạng-máy-tính-cho-devops-cơ-bản) |

## I

| Thuật ngữ | Nghĩa | Học ở |
|---|---|---|
| **IaC** | Hạ tầng dưới dạng code | [Ngày 29](./Giai-doan-2-Git-Docker-Cloud.md#ngày-29-infrastructure-as-code-giới-thiệu-terraform) |
| **Idempotent** | Chạy lại ra cùng kết quả | [Ngày 29](./Giai-doan-2-Git-Docker-Cloud.md#ngày-29-infrastructure-as-code-giới-thiệu-terraform) |
| **Image** | Khuôn mẫu chỉ đọc để tạo container | [Ngày 16](./Giai-doan-2-Git-Docker-Cloud.md#ngày-16-docker-khái-niệm-container-đầu-tiên) |
| **Incremental backup** | Backup gia tăng (chỉ phần thay đổi) | [Ngày 11](./Giai-doan-1-Linux-SysOps.md#ngày-11-lưu-trữ-backup-khôi-phục) |
| **Indentation** | Thụt lề (thể hiện cấp bậc trong YAML) | [Ngày 22](./Giai-doan-2-Git-Docker-Cloud.md#ngày-22-yaml-json-định-dạng-cấu-hình) |
| **Ingress Controller** | "nginx của Kubernetes" (GĐ3) | [Ngày 23](./Giai-doan-2-Git-Docker-Cloud.md#ngày-23-reverse-proxy-web-server-nginx-chuyên-sâu) |
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
| **known_hosts** | Danh sách host key đã tin tưởng | [Ngày 8](./Giai-doan-1-Linux-SysOps.md#ngày-8-ssh-kết-nối-quản-lý-server-từ-xa) |

## Ký hiệu

| Thuật ngữ | Nghĩa | Học ở |
|---|---|---|
| **.dockerignore** | Danh sách file bỏ khỏi build context | [Ngày 17](./Giai-doan-2-Git-Docker-Cloud.md#ngày-17-docker-dockerfile-build-image) |
| **.env** | File biến môi trường Compose tự đọc | [Ngày 20](./Giai-doan-2-Git-Docker-Cloud.md#ngày-20-docker-compose-quản-lý-multi-container) |
| **.gitignore** | Danh sách file Git bỏ qua | [Ngày 13](./Giai-doan-2-Git-Docker-Cloud.md#ngày-13-git-cơ-bản-quản-lý-phiên-bản) |
| **3-2-1 rule** | 3 bản, 2 loại lưu trữ, 1 off-site | [Ngày 11](./Giai-doan-1-Linux-SysOps.md#ngày-11-lưu-trữ-backup-khôi-phục) |

## L

| Thuật ngữ | Nghĩa | Học ở |
|---|---|---|
| **Layer** | Một tầng của image (mỗi chỉ thị tạo 1 layer) | [Ngày 17](./Giai-doan-2-Git-Docker-Cloud.md#ngày-17-docker-dockerfile-build-image) |
| **Least privilege** | Nguyên tắc cấp quyền tối thiểu đủ dùng | [Ngày 4](./Giai-doan-1-Linux-SysOps.md#ngày-4-linux-người-dùng-nhóm-phân-quyền) |
| **Lint** | Kiểm tra cú pháp tự động (`yamllint`) | [Ngày 22](./Giai-doan-2-Git-Docker-Cloud.md#ngày-22-yaml-json-định-dạng-cấu-hình) |
| **Listening port** | Cổng đang mở chờ kết nối | [Ngày 7](./Giai-doan-1-Linux-SysOps.md#ngày-7-mạng-máy-tính-cho-devops-cơ-bản) |
| **Load average** | Tải trung bình 1/5/15 phút | [Ngày 10](./Giai-doan-1-Linux-SysOps.md#ngày-10-quản-lý-log-giám-sát-hệ-thống) |
| **Load balancing** | Chia tải giữa nhiều backend | [Ngày 23](./Giai-doan-2-Git-Docker-Cloud.md#ngày-23-reverse-proxy-web-server-nginx-chuyên-sâu) |
| **Log** | Nhật ký sự kiện của chương trình/hệ thống | [Ngày 10](./Giai-doan-1-Linux-SysOps.md#ngày-10-quản-lý-log-giám-sát-hệ-thống) |
| **logrotate** | Tự xoay/nén/xoá log cũ | [Ngày 10](./Giai-doan-1-Linux-SysOps.md#ngày-10-quản-lý-log-giám-sát-hệ-thống) |
| **Loop / Condition** | Vòng lặp (`for`/`while`) / điều kiện (`if`) | [Ngày 5](./Giai-doan-1-Linux-SysOps.md#ngày-5-bash-scripting-cơ-bản) |

## M

| Thuật ngữ | Nghĩa | Học ở |
|---|---|---|
| **Managed DB** | DB do cloud vận hành (RDS/Cloud SQL) | [Ngày 24](./Giai-doan-2-Git-Docker-Cloud.md#ngày-24-cơ-sở-dữ-liệu-cho-devops) |
| **Manifest** | File YAML mô tả đối tượng K8s (trạng thái mong muốn) | [Ngày 37](./Giai-doan-3-CICD-K8s-Monitoring.md#ngày-37-kubernetes-pod-deployment-replicaset) |
| **Merge** | Hợp nhất nhánh này vào nhánh kia | [Ngày 14](./Giai-doan-2-Git-Docker-Cloud.md#ngày-14-git-branch-merge-xử-lý-conflict) |
| **Metric / Trace** | Số đo theo thời gian / dấu vết một request | [Ngày 10](./Giai-doan-1-Linux-SysOps.md#ngày-10-quản-lý-log-giám-sát-hệ-thống) |
| **Migration** | Thay đổi schema có version, rollback được | [Ngày 24](./Giai-doan-2-Git-Docker-Cloud.md#ngày-24-cơ-sở-dữ-liệu-cho-devops) |
| **Multi-stage build** | Build nhiều tầng, tầng cuối chỉ lấy artifact | [Ngày 18](./Giai-doan-2-Git-Docker-Cloud.md#ngày-18-docker-image-tối-ưu-multi-stage-build) |

## N

| Thuật ngữ | Nghĩa | Học ở |
|---|---|---|
| **Network (bridge/host/none)** | Mạng của container | [Ngày 19](./Giai-doan-2-Git-Docker-Cloud.md#ngày-19-docker-volume-network-dữ-liệu-bền-vững) |
| **nginx -t** | Test cú pháp config | [Ngày 23](./Giai-doan-2-Git-Docker-Cloud.md#ngày-23-reverse-proxy-web-server-nginx-chuyên-sâu) |
| **Norway problem** | Bẫy `NO` → `false` khi không quote | [Ngày 22](./Giai-doan-2-Git-Docker-Cloud.md#ngày-22-yaml-json-định-dạng-cấu-hình) |

## O

| Thuật ngữ | Nghĩa | Học ở |
|---|---|---|
| **Observability** | Khả năng quan sát hệ thống (metric+log+trace) | [Ngày 10](./Giai-doan-1-Linux-SysOps.md#ngày-10-quản-lý-log-giám-sát-hệ-thống) |
| **Off-site** | Bản lưu ở địa điểm khác | [Ngày 11](./Giai-doan-1-Linux-SysOps.md#ngày-11-lưu-trữ-backup-khôi-phục) |
| **OOM** | Out Of Memory — hết RAM, tiến trình bị kill | [Ngày 10](./Giai-doan-1-Linux-SysOps.md#ngày-10-quản-lý-log-giám-sát-hệ-thống) |
| **Owner / Group / Other** | Chủ / nhóm / người khác (3 nhóm quyền) | [Ngày 4](./Giai-doan-1-Linux-SysOps.md#ngày-4-linux-người-dùng-nhóm-phân-quyền) |

## P

| Thuật ngữ | Nghĩa | Học ở |
|---|---|---|
| **Package manager** | Trình quản lý gói phần mềm (`apt`, `dnf`) | [Ngày 3](./Giai-doan-1-Linux-SysOps.md#ngày-3-linux-quản-lý-tiến-trình-phần-mềm) |
| **Path** (absolute/relative)** | Đường dẫn (tuyệt đối/tương đối) | [Ngày 2](./Giai-doan-1-Linux-SysOps.md#ngày-2-linux-cơ-bản-điều-hướng-quản-lý-file) |
| **Permission** (rwx)** | Quyền đọc/ghi/chạy | [Ngày 4](./Giai-doan-1-Linux-SysOps.md#ngày-4-linux-người-dùng-nhóm-phân-quyền) |
| **Persistent data** | Dữ liệu bền vững (giữ qua restart) | [Ngày 19](./Giai-doan-2-Git-Docker-Cloud.md#ngày-19-docker-volume-network-dữ-liệu-bền-vững) |
| **pg_dump` / `mysqldump** | Công cụ backup DB nhất quán | [Ngày 24](./Giai-doan-2-Git-Docker-Cloud.md#ngày-24-cơ-sở-dữ-liệu-cho-devops) |
| **Pipeline** | Dây chuyền tự động chạy các bước build/test/deploy | [Ngày 1](./Giai-doan-1-Linux-SysOps.md#ngày-1-devops-sysops-là-gì-tổng-quan-toàn-ngành) |
| **plan / apply / destroy** | Xem trước / thực thi / xoá | [Ngày 29](./Giai-doan-2-Git-Docker-Cloud.md#ngày-29-infrastructure-as-code-giới-thiệu-terraform) |
| **Port** | Cổng — điểm vào của một dịch vụ trên máy | [Ngày 7](./Giai-doan-1-Linux-SysOps.md#ngày-7-mạng-máy-tính-cho-devops-cơ-bản) |
| **Port mapping** (`-p`)** | Ánh xạ cổng host ↔ container | [Ngày 16](./Giai-doan-2-Git-Docker-Cloud.md#ngày-16-docker-khái-niệm-container-đầu-tiên) |
| **Process / PID** | Tiến trình / số định danh tiến trình | [Ngày 3](./Giai-doan-1-Linux-SysOps.md#ngày-3-linux-quản-lý-tiến-trình-phần-mềm) |
| **profiles** | Bật/tắt nhóm service theo môi trường | [Ngày 20](./Giai-doan-2-Git-Docker-Cloud.md#ngày-20-docker-compose-quản-lý-multi-container) |
| **provider / resource** | Nhà cung cấp / tài nguyên cần tạo | [Ngày 29](./Giai-doan-2-Git-Docker-Cloud.md#ngày-29-infrastructure-as-code-giới-thiệu-terraform) |
| **proxy_pass** | Chuyển tiếp request tới backend | [Ngày 23](./Giai-doan-2-Git-Docker-Cloud.md#ngày-23-reverse-proxy-web-server-nginx-chuyên-sâu) |
| **Public / Private key** | Khoá công khai (chia sẻ) / khoá bí mật (giữ kín) | [Ngày 8](./Giai-doan-1-Linux-SysOps.md#ngày-8-ssh-kết-nối-quản-lý-server-từ-xa) |
| **Pull Request (PR)** | Đề nghị gộp nhánh + để review | [Ngày 15](./Giai-doan-2-Git-Docker-Cloud.md#ngày-15-github-remote-collaboration-pull-request) |
| **push / pull / fetch** | Đẩy lên / kéo về (fetch+merge) / chỉ tải về | [Ngày 15](./Giai-doan-2-Git-Docker-Cloud.md#ngày-15-github-remote-collaboration-pull-request) |

## R

| Thuật ngữ | Nghĩa | Học ở |
|---|---|---|
| **Rebase** | Viết lại lịch sử thành tuyến tính | [Ngày 25](./Giai-doan-2-Git-Docker-Cloud.md#ngày-25-git-nâng-cao-rebase-tag-workflow) |
| **Recursive** (`-r`, `-R`)** | Đệ quy — áp dụng cho cả thư mục con | [Ngày 2](./Giai-doan-1-Linux-SysOps.md#ngày-2-linux-cơ-bản-điều-hướng-quản-lý-file) |
| **Redirect** (`>`, `>>`)** | Chuyển hướng output ra file (ghi đè/nối) | [Ngày 6](./Giai-doan-1-Linux-SysOps.md#ngày-6-bash-scripting-nâng-cao-tự-động-hóa) |
| **reflog** | Sổ ghi mọi thao tác — nơi cứu commit mất | [Ngày 13](./Giai-doan-2-Git-Docker-Cloud.md#ngày-13-git-cơ-bản-quản-lý-phiên-bản) |
| **Registry / Docker Hub** | Kho chứa image | [Ngày 16](./Giai-doan-2-Git-Docker-Cloud.md#ngày-16-docker-khái-niệm-container-đầu-tiên) |
| **Remote / origin** | Repo trên server / tên mặc định của remote | [Ngày 15](./Giai-doan-2-Git-Docker-Cloud.md#ngày-15-github-remote-collaboration-pull-request) |
| **Replica** | Bản sao của pod. `replicas: 3` = muốn 3 bản sao giống nhau | [Ngày 37](./Giai-doan-3-CICD-K8s-Monitoring.md#ngày-37-kubernetes-pod-deployment-replicaset) |
| **Replication** | Nhân bản DB để HA/đọc mở rộng | [Ngày 24](./Giai-doan-2-Git-Docker-Cloud.md#ngày-24-cơ-sở-dữ-liệu-cho-devops) |
| **Repository (repo)** | Kho chứa mã nguồn (kèm lịch sử thay đổi) | [Ngày 1](./Giai-doan-1-Linux-SysOps.md#ngày-1-devops-sysops-là-gì-tổng-quan-toàn-ngành) · [Ngày 13](./Giai-doan-2-Git-Docker-Cloud.md#ngày-13-git-cơ-bản-quản-lý-phiên-bản) |
| **Retention policy** | Chính sách giữ/xoá backup cũ | [Ngày 6](./Giai-doan-1-Linux-SysOps.md#ngày-6-bash-scripting-nâng-cao-tự-động-hóa) |
| **Reverse proxy** | Proxy đứng trước server | [Ngày 23](./Giai-doan-2-Git-Docker-Cloud.md#ngày-23-reverse-proxy-web-server-nginx-chuyên-sâu) |
| **Rollback** | Quay về phiên bản trước khi bản mới lỗi | [Ngày 37](./Giai-doan-3-CICD-K8s-Monitoring.md#ngày-37-kubernetes-pod-deployment-replicaset) |
| **Rolling update** | Cập nhật cuốn chiếu, thay từng pod một để không downtime | [Ngày 37](./Giai-doan-3-CICD-K8s-Monitoring.md#ngày-37-kubernetes-pod-deployment-replicaset) |
| **root / superuser** | Tài khoản quyền tối cao | [Ngày 4](./Giai-doan-1-Linux-SysOps.md#ngày-4-linux-người-dùng-nhóm-phân-quyền) |
| **Root** (`/`)** | Gốc của cây thư mục Linux | [Ngày 2](./Giai-doan-1-Linux-SysOps.md#ngày-2-linux-cơ-bản-điều-hướng-quản-lý-file) |
| **RPO / RTO** | Mất tối đa bao nhiêu dữ liệu / khôi phục trong bao lâu | [Ngày 11](./Giai-doan-1-Linux-SysOps.md#ngày-11-lưu-trữ-backup-khôi-phục) |

## S

| Thuật ngữ | Nghĩa | Học ở |
|---|---|---|
| **scp / rsync** | Copy file qua SSH / đồng bộ thư mục hiệu quả | [Ngày 8](./Giai-doan-1-Linux-SysOps.md#ngày-8-ssh-kết-nối-quản-lý-server-từ-xa) |
| **Script** | File chứa chuỗi lệnh để máy tự chạy | [Ngày 5](./Giai-doan-1-Linux-SysOps.md#ngày-5-bash-scripting-cơ-bản) |
| **Secret** | Bí mật (mật khẩu, API key, token) | [Ngày 9](./Giai-doan-1-Linux-SysOps.md#ngày-9-tường-lửa-bảo-mật-hardening) |
| **Selector / Label** | Nhãn dán lên đối tượng + câu điều kiện chọn theo nhãn | [Ngày 37](./Giai-doan-3-CICD-K8s-Monitoring.md#ngày-37-kubernetes-pod-deployment-replicaset) |
| **Self-healing** | K8s tự tạo lại pod khi pod chết, để luôn đủ số mong muốn | [Ngày 37](./Giai-doan-3-CICD-K8s-Monitoring.md#ngày-37-kubernetes-pod-deployment-replicaset) |
| **Semantic Versioning** | Đánh số MAJOR.MINOR.PATCH có quy tắc | [Ngày 25](./Giai-doan-2-Git-Docker-Cloud.md#ngày-25-git-nâng-cao-rebase-tag-workflow) |
| **Service** | Một dịch vụ (container) trong compose | [Ngày 20](./Giai-doan-2-Git-Docker-Cloud.md#ngày-20-docker-compose-quản-lý-multi-container) |
| **Service / daemon** | Dịch vụ chạy nền liên tục (nginx, database...) | [Ngày 3](./Giai-doan-1-Linux-SysOps.md#ngày-3-linux-quản-lý-tiến-trình-phần-mềm) |
| **Shebang** (`#!/bin/bash`)** | Dòng đầu chỉ định trình thông dịch | [Ngày 5](./Giai-doan-1-Linux-SysOps.md#ngày-5-bash-scripting-cơ-bản) |
| **Signal** (TERM/KILL)** | Tín hiệu gửi cho tiến trình (dừng lịch sự / ép tắt) | [Ngày 3](./Giai-doan-1-Linux-SysOps.md#ngày-3-linux-quản-lý-tiến-trình-phần-mềm) |
| **Snapshot** | Ảnh chụp tức thời của dữ liệu/hệ thống | [Ngày 11](./Giai-doan-1-Linux-SysOps.md#ngày-11-lưu-trữ-backup-khôi-phục) |
| **SQL / NoSQL** | CSDL quan hệ / phi quan hệ | [Ngày 24](./Giai-doan-2-Git-Docker-Cloud.md#ngày-24-cơ-sở-dữ-liệu-cho-devops) |
| **Squash** | Gộp nhiều commit thành 1 | [Ngày 25](./Giai-doan-2-Git-Docker-Cloud.md#ngày-25-git-nâng-cao-rebase-tag-workflow) |
| **SSH** | Giao thức đăng nhập server từ xa an toàn (mã hoá) | [Ngày 8](./Giai-doan-1-Linux-SysOps.md#ngày-8-ssh-kết-nối-quản-lý-server-từ-xa) |
| **SSH key** | Cặp khoá (private + public) để xác thực an toàn không cần mật khẩu | [Ngày 1](./Giai-doan-1-Linux-SysOps.md#ngày-1-devops-sysops-là-gì-tổng-quan-toàn-ngành) |
| **SSH tunnel** (`-L`)** | Đường hầm mã hoá tới dịch vụ nội bộ | [Ngày 8](./Giai-doan-1-Linux-SysOps.md#ngày-8-ssh-kết-nối-quản-lý-server-từ-xa) |
| **SSL/TLS termination** | nginx giải mã HTTPS thay backend | [Ngày 23](./Giai-doan-2-Git-Docker-Cloud.md#ngày-23-reverse-proxy-web-server-nginx-chuyên-sâu) |
| **Staging area** | Khu vực chuẩn bị file cho commit | [Ngày 13](./Giai-doan-2-Git-Docker-Cloud.md#ngày-13-git-cơ-bản-quản-lý-phiên-bản) |
| **stash** | Cất tạm thay đổi chưa commit | [Ngày 14](./Giai-doan-2-Git-Docker-Cloud.md#ngày-14-git-branch-merge-xử-lý-conflict) |
| **state file** | Bản đồ trạng thái hạ tầng | [Ngày 29](./Giai-doan-2-Git-Docker-Cloud.md#ngày-29-infrastructure-as-code-giới-thiệu-terraform) |
| **stdout / stderr** | Luồng ra chuẩn / luồng lỗi chuẩn (`2>`) | [Ngày 6](./Giai-doan-1-Linux-SysOps.md#ngày-6-bash-scripting-nâng-cao-tự-động-hóa) |
| **sudo** | Chạy 1 lệnh với quyền cao (mượn quyền admin) | [Ngày 4](./Giai-doan-1-Linux-SysOps.md#ngày-4-linux-người-dùng-nhóm-phân-quyền) |
| **SUID** | Cờ đặc biệt: file chạy với quyền của chủ file | [Ngày 4](./Giai-doan-1-Linux-SysOps.md#ngày-4-linux-người-dùng-nhóm-phân-quyền) |
| **systemd / systemctl** | Hệ quản lý dịch vụ của Linux / lệnh điều khiển nó | [Ngày 3](./Giai-doan-1-Linux-SysOps.md#ngày-3-linux-quản-lý-tiến-trình-phần-mềm) |

## T

| Thuật ngữ | Nghĩa | Học ở |
|---|---|---|
| **Tag** | Nhãn phiên bản của image (`:1.0`) | [Ngày 17](./Giai-doan-2-Git-Docker-Cloud.md#ngày-17-docker-dockerfile-build-image) · [Ngày 25](./Giai-doan-2-Git-Docker-Cloud.md#ngày-25-git-nâng-cao-rebase-tag-workflow) |
| **TCP / UDP** | Hai giao thức giao vận (tin cậy / nhanh) | [Ngày 7](./Giai-doan-1-Linux-SysOps.md#ngày-7-mạng-máy-tính-cho-devops-cơ-bản) |
| **Terraform / HCL** | Công cụ IaC / ngôn ngữ của nó | [Ngày 29](./Giai-doan-2-Git-Docker-Cloud.md#ngày-29-infrastructure-as-code-giới-thiệu-terraform) |
| **tmpfs** | Lưu trong RAM, không bền vững | [Ngày 19](./Giai-doan-2-Git-Docker-Cloud.md#ngày-19-docker-volume-network-dữ-liệu-bền-vững) |

## U

| Thuật ngữ | Nghĩa | Học ở |
|---|---|---|
| **upstream** | Nhóm backend để load balance | [Ngày 23](./Giai-doan-2-Git-Docker-Cloud.md#ngày-23-reverse-proxy-web-server-nginx-chuyên-sâu) |
| **USER** | Chỉ thị chạy container bằng user không-root | [Ngày 18](./Giai-doan-2-Git-Docker-Cloud.md#ngày-18-docker-image-tối-ưu-multi-stage-build) |
| **User / Group** | Người dùng / nhóm người dùng | [Ngày 4](./Giai-doan-1-Linux-SysOps.md#ngày-4-linux-người-dùng-nhóm-phân-quyền) |

## V

| Thuật ngữ | Nghĩa | Học ở |
|---|---|---|
| **Variable** | Biến — hộp đựng giá trị | [Ngày 5](./Giai-doan-1-Linux-SysOps.md#ngày-5-bash-scripting-cơ-bản) |
| **Volume** | Ổ lưu dữ liệu bền vững do Docker quản lý | [Ngày 16](./Giai-doan-2-Git-Docker-Cloud.md#ngày-16-docker-khái-niệm-container-đầu-tiên) · [Ngày 19](./Giai-doan-2-Git-Docker-Cloud.md#ngày-19-docker-volume-network-dữ-liệu-bền-vững) |

## W

| Thuật ngữ | Nghĩa | Học ở |
|---|---|---|
| **Working directory** | Thư mục làm việc — nơi sửa file | [Ngày 13](./Giai-doan-2-Git-Docker-Cloud.md#ngày-13-git-cơ-bản-quản-lý-phiên-bản) |
| **Works on my machine** | Câu nói kinh điển khi code chạy ở máy Dev nhưng lỗi trên server | [Ngày 1](./Giai-doan-1-Linux-SysOps.md#ngày-1-devops-sysops-là-gì-tổng-quan-toàn-ngành) |

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
