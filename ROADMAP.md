# 🗺️ ROADMAP — Lộ trình học DevOps

> Bản đồ toàn khoá: **học gì, theo thứ tự nào, và vì sao thứ tự đó**.
> Đọc file này trước khi bắt đầu, và mở lại mỗi khi thấy lạc.

---

## 1. Vì sao thứ tự này, không phải thứ tự khác

Sai lầm phổ biến nhất khi tự học DevOps là **học tool trước, học nền tảng sau**:

```text
❌ Docker → Kubernetes → Terraform → Jenkins
   (học được cú pháp, nhưng gặp lỗi lạ là bí hoàn toàn)
```

Lý do nó thất bại: mọi công cụ DevOps đều **chạy trên Linux, nói chuyện qua mạng, và lưu trạng thái ở đâu đó**. Không hiểu ba thứ đó thì bạn chỉ đang chép lệnh.

Khoá này đi theo **chuỗi phụ thuộc thật**:

```text
Linux  ──┐
Mạng   ──┼──>  Container  ──>  Điều phối (K8s)
Shell  ──┘         │
                   │
Git ───────────────┼──>  CI/CD  ──>  GitOps
                   │
IaC ───────────────┘
                   │
                   └──>  Giám sát  ──>  SRE
```

Mỗi tầng dùng lại tầng dưới. Bỏ qua một tầng là để lại một lỗ hổng mà bạn sẽ vấp phải ở tầng trên.

---

## 2. Mental model — DevOps là một vòng lặp, không phải danh sách tool

Giữ sơ đồ này trong đầu suốt khoá học. Mỗi ngày bạn học, hãy tự hỏi *"mình đang ở đoạn nào của vòng này?"*

```text
   Lập trình viên
        ↓
   Git (mã nguồn)
        ↓
   CI — build · test · quét bảo mật
        ↓
   Artifact / Container image
        ↓
   Registry (kho image)
        ↓
   Hạ tầng (Terraform) · Cấu hình (Ansible)
        ↓
   Triển khai (CD / GitOps)
        ↓
   Ứng dụng đang chạy
        ↓
   Giám sát · Log · Cảnh báo
        ↓
   Phản hồi ──────────> quay lại Lập trình viên
```

---

## 3. Bản đồ Phase → Ngày học

Cột **Ngày** bấm được — nhảy thẳng tới bài.

| Phase | Nội dung | Ngày học | Vì sao ở vị trí này |
|---|---|---|---|
| **Phase 0** | DevOps Fundamentals | [1](./Giai-doan-1-Linux-SysOps.md#ngày-1--devops--sysops-là-gì-tổng-quan-toàn-ngành) | Hiểu bài toán trước khi học công cụ |
| **Phase 1** | Linux | [2](./Giai-doan-1-Linux-SysOps.md#ngày-2--linux-cơ-bản-điều-hướng--quản-lý-file) · [3](./Giai-doan-1-Linux-SysOps.md#ngày-3--linux-quản-lý-tiến-trình--phần-mềm) · [4](./Giai-doan-1-Linux-SysOps.md#ngày-4--linux-người-dùng-nhóm--phân-quyền) · [10](./Giai-doan-1-Linux-SysOps.md#ngày-10--quản-lý-log--giám-sát-hệ-thống) · [11](./Giai-doan-1-Linux-SysOps.md#ngày-11--lưu-trữ-backup--khôi-phục) | Mọi thứ phía sau đều chạy trên Linux |
| **Phase 2** | Networking | [7](./Giai-doan-1-Linux-SysOps.md#ngày-7--mạng-máy-tính-cho-devops-cơ-bản) · [8](./Giai-doan-1-Linux-SysOps.md#ngày-8--ssh-kết-nối--quản-lý-server-từ-xa) · [9](./Giai-doan-1-Linux-SysOps.md#ngày-9--tường-lửa-bảo-mật--hardening) | Không hiểu mạng thì mọi lỗi kết nối đều là phép màu |
| **Phase 3** | Bash & Python | [5](./Giai-doan-1-Linux-SysOps.md#ngày-5--bash-scripting-cơ-bản) · [6](./Giai-doan-1-Linux-SysOps.md#ngày-6--bash-scripting-nâng-cao--tự-động-hóa) | Tự động hoá bắt đầu từ script, trước khi tới công cụ |
| **Phase 4** | Git & GitHub | [13](./Giai-doan-2-Git-Docker-Cloud.md#ngày-13--git-cơ-bản--quản-lý-phiên-bản) · [14](./Giai-doan-2-Git-Docker-Cloud.md#ngày-14--git-branch-merge--xử-lý-conflict) · [15](./Giai-doan-2-Git-Docker-Cloud.md#ngày-15--github-remote-collaboration--pull-request) · [25](./Giai-doan-2-Git-Docker-Cloud.md#ngày-25--git-nâng-cao--rebase-tag-workflow) | Điều kiện tiên quyết của CI/CD và GitOps |
| **Phase 5** | Web Server / Reverse Proxy | [23](./Giai-doan-2-Git-Docker-Cloud.md#ngày-23--reverse-proxy--web-server-nginx-chuyên-sâu) | Hiểu cách request tới được app, trước khi đóng gói app |
| **Phase 6** | Docker | [16](./Giai-doan-2-Git-Docker-Cloud.md#ngày-16--docker-khái-niệm--container-đầu-tiên) · [17](./Giai-doan-2-Git-Docker-Cloud.md#ngày-17--docker-dockerfile--build-image) · [18](./Giai-doan-2-Git-Docker-Cloud.md#ngày-18--docker-image-tối-ưu--multi-stage-build) · [19](./Giai-doan-2-Git-Docker-Cloud.md#ngày-19--docker-volume-network--dữ-liệu-bền-vững) · [20](./Giai-doan-2-Git-Docker-Cloud.md#ngày-20--docker-compose-quản-lý-multi-container) · [22](./Giai-doan-2-Git-Docker-Cloud.md#ngày-22--yaml-json--định-dạng-cấu-hình) · [24](./Giai-doan-2-Git-Docker-Cloud.md#ngày-24--cơ-sở-dữ-liệu-cho-devops) | Đóng gói — nền của K8s và CI/CD hiện đại |
| **Phase 7** | Ansible | [47](./Giai-doan-3-CICD-K8s-Monitoring.md#ngày-47--configuration-management-ansible) | Tự động hoá cấu hình máy; cầu nối từ làm tay sang IaC |
| **Phase 8** | Terraform / IaC | [29](./Giai-doan-2-Git-Docker-Cloud.md#ngày-29--infrastructure-as-code--giới-thiệu-terraform) · [48](./Giai-doan-3-CICD-K8s-Monitoring.md#ngày-48--terraform-nâng-cao-module-remote-state--workspace) | Tạo hạ tầng bằng code, không bấm chuột |
| **Phase 9** | CI/CD | [31](./Giai-doan-3-CICD-K8s-Monitoring.md#ngày-31--cicd-khái-niệm--github-actions-cơ-bản) · [32](./Giai-doan-3-CICD-K8s-Monitoring.md#ngày-32--ci-pipeline-build-test--lint-tự-động) · [33](./Giai-doan-3-CICD-K8s-Monitoring.md#ngày-33--cd-pipeline-build--push-docker-image) · [34](./Giai-doan-3-CICD-K8s-Monitoring.md#ngày-34--cd-pipeline-tự-động-deploy-lên-server) | Cần Git + Docker trước mới xây được pipeline |
| **Phase 10** | Cloud | [26](./Giai-doan-2-Git-Docker-Cloud.md#ngày-26--làm-quen-cloud--khái-niệm--free-tier) · [27](./Giai-doan-2-Git-Docker-Cloud.md#ngày-27--máy-chủ-cloud--tạo--quản-lý-vm) · [28](./Giai-doan-2-Git-Docker-Cloud.md#ngày-28--triển-khai-app-lên-cloud-docker-trên-vm) | Nơi để triển khai; học sau khi biết đóng gói |
| **Phase 11** | Kubernetes | [36](./Giai-doan-3-CICD-K8s-Monitoring.md#ngày-36--kubernetes-khái-niệm--kiến-trúc) · [37](./Giai-doan-3-CICD-K8s-Monitoring.md#ngày-37--kubernetes-pod-deployment--replicaset) · [38](./Giai-doan-3-CICD-K8s-Monitoring.md#ngày-38--kubernetes-service--networking) · [39](./Giai-doan-3-CICD-K8s-Monitoring.md#ngày-39--kubernetes-configmap-secret--storage) · [41](./Giai-doan-3-CICD-K8s-Monitoring.md#ngày-41--kubernetes-health-check-resource--autoscaling) · [42](./Giai-doan-3-CICD-K8s-Monitoring.md#ngày-42--helm-package-manager-cho-kubernetes) | Điều phối container ở quy mô lớn — cần Docker + mạng vững |
| **Phase 12** | Monitoring & Observability | [44](./Giai-doan-3-CICD-K8s-Monitoring.md#ngày-44--monitoring-prometheus--metrics) · [45](./Giai-doan-3-CICD-K8s-Monitoring.md#ngày-45--monitoring-grafana-dashboard) · [46](./Giai-doan-3-CICD-K8s-Monitoring.md#ngày-46--logging-tập-trung-loki) | Có hệ thống chạy rồi mới giám sát được |
| **Phase 13** | Security / DevSecOps | [49](./Giai-doan-3-CICD-K8s-Monitoring.md#ngày-49--bảo-mật-devsecops--best-practices) | Gài vào pipeline đã có, không phải bước cuối rời rạc |
| **Phase 14** | GitOps | [43](./Giai-doan-3-CICD-K8s-Monitoring.md#ngày-43--gitops-argocd--triển-khai-khai-báo) | Cần Git + K8s + CD trước |
| **Phase 15** | Advanced / SRE | [51](./Giai-doan-4-SRE-Capstone.md#ngày-51--site-reliability-engineering-sre--nguyên-lý) · [52](./Giai-doan-4-SRE-Capstone.md#ngày-52--high-availability-scaling--disaster-recovery) · [53](./Giai-doan-4-SRE-Capstone.md#ngày-53--cost-optimization--finops) · [54](./Giai-doan-4-SRE-Capstone.md#ngày-54--service-mesh--microservices-nâng-cao) · [55](./Giai-doan-4-SRE-Capstone.md#ngày-55--platform-engineering--developer-experience) | Nâng từ 'chạy được' lên 'tin cậy đo được' |

### Module bổ sung — đào sâu khi cần

| Module | Nội dung | Học sau |
|---|---|---|
| [🐍 Python cho DevOps](./Module-Python-cho-DevOps.md) | Script Python thay Bash khi việc phức tạp hơn | Ngày 6 |
| [🧱 **Nền tảng Mở rộng**](./Module-Nen-Tang-Mo-Rong.md) — NT1 | Subnet · định tuyến · `tcpdump` · TLS | Ngày 9 |
| [🧱 Nền tảng Mở rộng](./Module-Nen-Tang-Mo-Rong.md) — NT2 | HTTPS production · cân bằng tải · tinh chỉnh | Ngày 23 |
| [🧱 Nền tảng Mở rộng](./Module-Nen-Tang-Mo-Rong.md) — NT3 | Role · Vault · rolling update · inventory động | Ngày 47 |
| [🧩 Nâng cao bổ sung](./Module-Nang-Cao-Bo-Sung.md) | Tracing · Vault · Kafka · Managed K8s | Giai đoạn 3 |

### Ngày Milestone — LAB Final

| Ngày | Chủ đề tổng hợp | Chấm điểm |
|---|---|---|
| [Ngày 12](./Giai-doan-1-Linux-SysOps.md#ngày-12--milestone-lab-tổng-hợp-giai-đoạn-1) | MILESTONE: LAB tổng hợp Giai đoạn 1 | 100 điểm, tự chấm |
| [Ngày 21](./Giai-doan-2-Git-Docker-Cloud.md#ngày-21--milestone-đóng-gói-ứng-dụng-full-stack) | MILESTONE: Đóng gói ứng dụng full-stack | 100 điểm, tự chấm |
| [Ngày 30](./Giai-doan-2-Git-Docker-Cloud.md#ngày-30--milestone-lab-tổng-hợp-giai-đoạn-2) | MILESTONE: LAB tổng hợp Giai đoạn 2 | 100 điểm, tự chấm |
| [Ngày 35](./Giai-doan-3-CICD-K8s-Monitoring.md#ngày-35--milestone-pipeline-cicd-hoàn-chỉnh) | MILESTONE: Pipeline CI/CD hoàn chỉnh | 100 điểm, tự chấm |
| [Ngày 40](./Giai-doan-3-CICD-K8s-Monitoring.md#ngày-40--milestone-deploy-full-stack-lên-kubernetes) | MILESTONE: Deploy Full-stack lên Kubernetes | 100 điểm, tự chấm |
| [Ngày 50](./Giai-doan-3-CICD-K8s-Monitoring.md#ngày-50--milestone-lab-tổng-hợp-giai-đoạn-3) | MILESTONE: LAB tổng hợp Giai đoạn 3 | 100 điểm, tự chấm |

### Dự án tốt nghiệp

| Ngày | Phần | Điểm |
|---|---|---|
| [Ngày 56](./Giai-doan-4-SRE-Capstone.md#ngày-56--dự-án-tốt-nghiệp--phần-1-thiết-kế--hạ-tầng) | Thiết kế & Hạ tầng | 25 |
| [Ngày 57](./Giai-doan-4-SRE-Capstone.md#ngày-57--dự-án-tốt-nghiệp--phần-2-container--cicd) | Container & CI/CD | 30 |
| [Ngày 58](./Giai-doan-4-SRE-Capstone.md#ngày-58--dự-án-tốt-nghiệp--phần-3-monitoring--reliability) | Giám sát & Độ tin cậy | 30 |
| [Ngày 59](./Giai-doan-4-SRE-Capstone.md#ngày-59--dự-án-tốt-nghiệp--phần-4-tài-liệu-demo--portfolio) | Tài liệu & Portfolio | 15 |
| [Ngày 60](./Giai-doan-4-SRE-Capstone.md#ngày-60--tốt-nghiệp--tổng-kết-chứng-chỉ--định-hướng-sự-nghiệp) | **LAB FINAL toàn khoá** + định hướng nghề | 100 |

---

## 4. Thứ tự học đề xuất

Khoá được đánh số 1→60 theo **thứ tự tuyến tính** — cứ đi từ Ngày 1 là đúng. Bảng Phase ở trên dành cho hai việc:

- **Tra cứu:** cần ôn Kubernetes thì biết ngay là Ngày 36–43
- **Nhảy cóc có kiểm soát:** đã vững Linux rồi thì bắt đầu từ Ngày 13, nhưng **phải làm được LAB Final Ngày 12** trước đã

> ⚠️ **Kiểm tra trước khi nhảy cóc:** mở LAB Final của giai đoạn bạn định bỏ qua, chạy bộ script tự chấm. Trên 75 điểm thì được bỏ; dưới thì đừng.

---

## 5. Mốc thời gian tham khảo

| Nhịp học | Thời gian hoàn thành | Phù hợp với |
|---|---|---|
| 1 ngày/ngày, 90 phút | ~2 tháng | Đang thất nghiệp hoặc học toàn thời gian |
| 5 ngày/tuần | ~3 tháng | Đi làm, học buổi tối |
| 3 ngày/tuần | ~5 tháng | Bận, nhưng đều đặn |

> 🧠 **Đều quan trọng hơn nhiều.** 3 ngày mỗi tuần trong 5 tháng thắng 7 ngày mỗi tuần trong 2 tuần rồi bỏ. Kỹ năng vận hành là thứ tích luỹ.

---

## 6. Môi trường thực hành

Toàn bộ khoá chạy **miễn phí trên máy bạn** — không cần tài khoản cloud:

| Cần gì | Dùng gì | RAM tối thiểu |
|---|---|---|
| Máy chủ Linux | Multipass (dùng chính cloud-init như AWS/GCP) | 2 GB |
| Dịch vụ AWS | LocalStack (cùng lệnh `aws` CLI) | 1 GB |
| Kubernetes | minikube | 4 GB |
| CI/CD | GitHub Actions (runner miễn phí) | — |
| Giám sát | Docker Compose (Prometheus/Grafana/Loki) | 2 GB |

**Máy 8 GB RAM là đủ** cho toàn khoá, miễn là không chạy mọi thứ cùng lúc.

---

## 7. Liên kết nhanh

| File | Dùng khi |
|---|---|
| [HOC-HANG-NGAY.md](./HOC-HANG-NGAY.md) | Nhịp học ngày · tuần · tháng |
| [PROGRESS.md](./PROGRESS.md) | Theo dõi mình đã học tới đâu |
| [PROJECTS.md](./PROJECTS.md) | Làm dự án cuối mỗi tháng |
| [QUIZ-TONG-HOP.md](./QUIZ-TONG-HOP.md) | Tự kiểm tra cuối mỗi giai đoạn |
| [Module Nền tảng Mở rộng](./Module-Nen-Tang-Mo-Rong.md) | Cần đào sâu mạng, web server hoặc Ansible |
| [GLOSSARY.md](./GLOSSARY.md) | Gặp thuật ngữ lạ |
| [TROUBLESHOOTING.md](./TROUBLESHOOTING.md) | Đang kẹt vì một lỗi |
| [INTERVIEW.md](./INTERVIEW.md) | Chuẩn bị phỏng vấn |
| [Tài liệu tham khảo](./Tai-lieu-tham-khao.md) | Muốn đọc sâu hơn |
