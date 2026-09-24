# 🏗️ PROJECTS — Hệ thống dự án thực hành

> Tài liệu dạy bạn **từng mảnh**. Dự án bắt bạn **ghép chúng lại** — và đó mới là lúc bạn biết mình thật sự hiểu hay chỉ đang chép lệnh.
>
> Mỗi dự án đều có: 📋 đề bài · ✅ yêu cầu · 📐 rubric chấm điểm · 🔥 phép thử · 🎓 bài tập 4 mức. **Không có hướng dẫn từng bước.**

---

## Vì sao phải làm dự án, không chỉ làm LAB

| | LAB trong bài học | Dự án |
|---|---|---|
| Phạm vi | Một chủ đề | **Ghép 2–5 chủ đề** |
| Hướng dẫn | Từng bước, có output mẫu | Chỉ có đề bài và tiêu chí |
| Khi kẹt | Đọc bước tiếp theo | **Tự tìm cách** |
| Kết quả | Hiểu một công cụ | **Một thứ đem đi khoe được** |

> 🔑 Người phỏng vấn không hỏi *"bạn đã làm bao nhiêu lab?"*. Họ hỏi *"kể về một hệ thống bạn đã xây"*. Dự án chính là câu trả lời đó.

---

## Bản đồ 5 dự án

| # | Dự án | Ghép những gì | Làm sau | Thời lượng | Điểm |
|---|---|---|---|---|---|
| **01** | [Máy chủ Linux chuẩn production](#dự-án-01--máy-chủ-linux-chuẩn-production) | Linux · SSH · tường lửa · systemd · Bash · sao lưu | Ngày 12 | 3–5 giờ | 100 |
| **02** | [Ứng dụng container hoá](#dự-án-02--ứng-dụng-container-hoá) | Git · Docker · Compose · Nginx · Database | Ngày 21 | 4–6 giờ | 100 |
| **03** | [Tự động hoá hạ tầng](#dự-án-03--tự-động-hoá-hạ-tầng) | Terraform · Ansible · cloud-init · Docker | Ngày 48* | 5–7 giờ | 100 |
| **04** | [Dây chuyền CI/CD](#dự-án-04--dây-chuyền-cicd) | Git · CI · test · registry · deploy · rollback | Ngày 35 | 5–7 giờ | 100 |
| **05** | [Hệ thống quan sát được](#dự-án-05--hệ-thống-quan-sát-được) | Metrics · Logs · Dashboard · Alert · SLO | Ngày 51 | 5–7 giờ | 100 |
| 🎓 | [**CAPSTONE — CloudNote**](#-capstone--cloudnote) | **Tất cả** | Ngày 55 | 4 buổi | 100 |

\* Dự án 03 cần Terraform nâng cao (Ngày 48); nếu muốn làm sớm sau Ngày 29 thì bỏ phần module và remote state.

### Quan hệ với Milestone trong bài học

Sáu ngày Milestone (12, 21, 30, 35, 40, 50) **chính là bản rút gọn** của các dự án này, có sẵn rubric và script tự chấm. Dự án ở đây là **phiên bản mở rộng**: phạm vi lớn hơn, yêu cầu tài liệu đầy đủ hơn, và có bài tập 4 mức.

| Nếu bạn | Thì |
|---|---|
| Đang học đúng tiến độ | Làm Milestone trong bài là đủ; quay lại dự án khi ôn tập |
| Muốn portfolio mạnh | Làm dự án đầy đủ, đẩy lên GitHub riêng từng repo |
| Chuẩn bị phỏng vấn gấp | Làm **Dự án 04 + 05** — hai cái này gây ấn tượng nhất |

---

## Dự án 01 — Máy chủ Linux chuẩn production

> 📋 **Đề bài:** Bạn nhận một máy Linux trần và một yêu cầu: *"biến nó thành máy chủ web nội bộ, an toàn, có giám sát, và bàn giao được cho người khác."* Không ai hướng dẫn gì thêm.
>
> **Làm sau:** Ngày 12 · **Thời lượng:** 3–5 giờ · **Môi trường:** Multipass hoặc VirtualBox

### ✅ Yêu cầu

| # | Bắt buộc |
|---|---|
| 1 | User quản trị riêng có sudo; **root không đăng nhập được** |
| 2 | SSH chỉ dùng khoá, cấm mật khẩu, đổi cổng mặc định |
| 3 | Tường lửa chặn mặc định, chỉ mở cổng cần |
| 4 | Web server chạy, tự bật khi máy khởi động |
| 5 | User "ứng dụng" không có shell, sở hữu thư mục web |
| 6 | Script kiểm tra sức khoẻ có ngưỡng rõ ràng |
| 7 | Script sao lưu **có bước tự kiểm chứng**, chạy theo lịch |
| 8 | Xoay vòng log |
| 9 | Tài liệu bàn giao |

| # | Nâng cao |
|---|---|
| 10 | `fail2ban` chặn dò mật khẩu |
| 11 | Script sức khoẻ gửi cảnh báo khi vượt ngưỡng |
| 12 | **Toàn bộ máy dựng lại được từ một file `cloud-init.yaml`** |
| 13 | Systemd timer thay cron, có log qua journald |

### 📐 Rubric (100 điểm)

| Hạng mục | Điểm |
|---|---|
| Người dùng & phân quyền | 15 |
| Bảo mật SSH | 20 |
| Tường lửa | 10 |
| Web server | 10 |
| Script sức khoẻ | 15 |
| Sao lưu (có khôi phục thử) | 20 |
| Quản lý log | 5 |
| Tài liệu bàn giao | 5 |

### 🔥 Ba phép thử

1. **Khôi phục thật** — xoá sạch thư mục web, khôi phục từ bản sao lưu, trang web trở lại nguyên vẹn
2. **Không tự khoá mình** — siết SSH trong khi giữ một phiên dự phòng; nếu mất cả hai phiên là trượt
3. **Người lạ tiếp quản** — đưa tài liệu cho người khác, họ trả lời được: máy chạy gì? sao lưu ở đâu? dịch vụ chết thì kiểm tra gì?

### 🎓 Bài tập 4 mức

| Mức | Bài tập |
|---|---|
| **A — Cơ bản** | Thêm một user chỉ đọc log, không sudo, không sửa được file web |
| **B — Trung cấp** | Script sức khoẻ ghi kết quả vào file CSV để vẽ đồ thị theo thời gian |
| **C — Gỡ lỗi** | Nhờ người khác **phá máy của bạn** (đổi quyền, sửa cấu hình, làm đầy đĩa) rồi bạn tìm và sửa — chỉ dùng log |
| **D — Thực tế** | Máy chủ sắp hết đĩa lúc 2 giờ sáng. Viết runbook để người trực **chưa từng thấy máy này** vẫn xử lý được |

📖 Chi tiết đề bài và script tự chấm: [Ngày 12](./Giai-doan-1-Linux-SysOps.md#ngày-12--milestone-lab-tổng-hợp-giai-đoạn-1)

---

## Dự án 02 — Ứng dụng container hoá

> 📋 **Đề bài:** Đóng gói một hệ thống ba tầng sao cho **người lạ clone repo về, chạy một lệnh, là hệ thống lên** — không cài Node, không cài PostgreSQL, không đọc hướng dẫn dài.
>
> **Làm sau:** Ngày 21 · **Thời lượng:** 4–6 giờ

### ✅ Yêu cầu

| # | Bắt buộc |
|---|---|
| 1 | Ba dịch vụ chạy bằng **một lệnh** |
| 2 | Multi-stage build, image dưới 200 MB |
| 3 | Container không chạy bằng root |
| 4 | Dữ liệu database sống sót khi xoá và tạo lại container |
| 5 | Chỉ reverse proxy lộ cổng |
| 6 | Backend chờ database **sẵn sàng** rồi mới khởi động |
| 7 | `HEALTHCHECK` cho backend và database |
| 8 | `.env` + `.env.example`, không commit bí mật |
| 9 | `.dockerignore` đầy đủ |
| 10 | README: chạy, dừng, xoá sạch |

| # | Nâng cao |
|---|---|
| 11 | Profile `dev` (nạp lại code tự động) và `prod` |
| 12 | Giới hạn log và tài nguyên cho từng dịch vụ |
| 13 | Image dưới 100 MB (distroless) |
| 14 | Script `khoi-dong.sh`: dựng → chờ khoẻ → in địa chỉ |

### 📐 Rubric (100 điểm)

| Hạng mục | Điểm |
|---|---|
| Chạy bằng một lệnh | 15 |
| Chất lượng Dockerfile | 20 |
| Kích thước image | 10 |
| Dữ liệu bền | 15 |
| Mạng & bảo mật | 15 |
| Thứ tự khởi động & healthcheck | 10 |
| Quản lý cấu hình | 10 |
| Tài liệu | 5 |

### 🔥 Hai phép thử

1. **Dữ liệu bền** — ghi dữ liệu, `docker compose down`, `up` lại, dữ liệu còn nguyên
2. **Người lạ chạy được** — clone vào máy sạch, chỉ được phép làm `cp .env.example .env` rồi `docker compose up -d`

### 🎓 Bài tập 4 mức

| Mức | Bài tập |
|---|---|
| **A** | Thêm một dịch vụ Redis làm cache, backend gọi được |
| **B** | Giảm image backend xuống dưới 100 MB, ghi lại mỗi bước giảm được bao nhiêu |
| **C** | Cố ý đặt `depends_on` sai (không có `condition`), quan sát backend crash, rồi giải thích **vì sao** |
| **D** | Đội bạn than *"máy tôi chạy được, CI thì không"*. Nêu 3 nguyên nhân có thể và cách xác minh từng cái |

📖 Chi tiết: [Ngày 21](./Giai-doan-2-Git-Docker-Cloud.md#ngày-21--milestone-đóng-gói-ứng-dụng-full-stack)

---

## Dự án 03 — Tự động hoá hạ tầng

> 📋 **Đề bài:** **Xoá sạch mọi thứ, rồi dựng lại toàn bộ hệ thống từ số 0 chỉ bằng các lệnh có trong README** — hạ tầng lẫn ứng dụng. Không bấm chuột, không thao tác nhớ trong đầu.
>
> **Làm sau:** Ngày 48 · **Thời lượng:** 5–7 giờ

### ✅ Yêu cầu

| # | Bắt buộc |
|---|---|
| 1 | Terraform dựng hạ tầng, có biến và output |
| 2 | Máy tự cấu hình bằng cloud-init |
| 3 | Ansible role cấu hình dịch vụ |
| 4 | Remote state có khoá |
| 5 | Ứng dụng chạy sau reverse proxy |
| 6 | `terraform destroy` xoá sạch, không sót |
| 7 | Không bí mật nào trong Git |
| 8 | README: dựng từ số 0 và xoá |

| # | Nâng cao |
|---|---|
| 9 | Terraform tách module; hai môi trường dev/prod |
| 10 | **Inventory động** sinh từ `terraform output` |
| 11 | Ansible `serial` — cập nhật không gián đoạn |
| 12 | Checkov quét Terraform trong CI |

### 📐 Rubric (100 điểm)

| Hạng mục | Điểm |
|---|---|
| Hạ tầng bằng code | 25 |
| Cấu hình tự động (Ansible) | 25 |
| Remote state & bảo mật | 15 |
| Dựng lại được từ số 0 | 20 |
| Tài liệu | 15 |

### 🔥 Phép thử lớn

```bash
BAT_DAU=$(date +%s)
terraform destroy -auto-approve
terraform apply -auto-approve && ansible-playbook site.yml
curl http://<dia-chi>/
echo "Dựng lại từ số 0: $(( ($(date +%s)-BAT_DAU)/60 )) phút"
```

| Kết quả | Đánh giá |
|---|---|
| Dưới 10 phút, một mạch | 🟢 Đây là IaC thật |
| 10–20 phút | 🟡 Còn vài bước thủ công |
| Phải sửa gì đó giữa chừng | 🔴 Chưa phải IaC |

> Mỗi lần bạn phải gõ thêm một lệnh không có trong README — đó là một lỗi. Ghi lại, bổ sung vào script, lặp lại tới khi chạy trót lọt.

### 🎓 Bài tập 4 mức

| Mức | Bài tập |
|---|---|
| **A** | Thêm một biến `so_may` để tạo N máy thay vì 1 |
| **B** | Tách Terraform thành module, gọi 2 lần với tham số khác nhau |
| **C** | Xoá một tài nguyên bằng tay trên console, chạy `terraform plan` và giải thích Terraform đề nghị làm gì, vì sao |
| **D** | Đồng nghiệp chạy `apply` cùng lúc với bạn. Chuyện gì xảy ra nếu **không có** state locking? Mô tả cách khắc phục hậu quả |

📖 Nền tảng: [Ngày 29](./Giai-doan-2-Git-Docker-Cloud.md#ngày-29--infrastructure-as-code--giới-thiệu-terraform) · [Ngày 48](./Giai-doan-3-CICD-K8s-Monitoring.md#ngày-48--terraform-nâng-cao-module-remote-state--workspace) · [NT3 Ansible nâng cao](./Module-Nen-Tang-Mo-Rong.md#nt3--ansible-nâng-cao-role-vault-rolling-update--inventory-động)

---

## Dự án 04 — Dây chuyền CI/CD

> 📋 **Đề bài:** Từ `git push` tới ứng dụng đang phục vụ, **không ai chạm tay vào server**. Và bạn phải **chứng minh bằng số liệu** rằng nó hơn hẳn deploy thủ công.
>
> **Làm sau:** Ngày 35 · **Thời lượng:** 5–7 giờ

### ✅ Yêu cầu

| # | Bắt buộc |
|---|---|
| 1 | CI nhiều tầng: lint → test (matrix) → build, có cache |
| 2 | Ba lớp quét bảo mật, **thực sự chặn được** |
| 3 | Image tag theo SHA, đẩy lên registry |
| 4 | Deploy tự động sau khi image sẵn sàng |
| 5 | Kiểm tra sức khoẻ sau deploy, có thử lại |
| 6 | Quay lui một thao tác, dưới 2 phút |
| 7 | Branch protection: CI đỏ không merge được |
| 8 | **Bảng so sánh với deploy thủ công**, có số liệu thật |

| # | Nâng cao |
|---|---|
| 9 | Pipeline dưới 4 phút |
| 10 | CI tự cập nhật tag vào repo cấu hình (khép kín) |
| 11 | Environment có người duyệt |
| 12 | Triển khai canary |

### 📐 Rubric (100 điểm)

| Hạng mục | Điểm |
|---|---|
| Cấu trúc pipeline | 20 |
| Bảo mật trong pipeline | 20 |
| Đóng gói & gắn tag | 15 |
| Tự động deploy | 15 |
| Kiểm tra sau deploy | 10 |
| Quay lui | 10 |
| Đo đạc & so sánh | 10 |

### 🔥 Bốn phép thử

1. **Toàn bộ dây chuyền** — sửa code, push, bấm giờ tới khi bản mới phục vụ
2. **CI chặn code hỏng** — PR có lỗi test, nút Merge phải bị khoá
3. **Quét bảo mật chặn được** — commit chuỗi giống mật khẩu, job quét phải đỏ
4. **Quay lui** — deploy bản hỏng rồi lui về bản cũ, bấm giờ

### 🎓 Bài tập 4 mức

| Mức | Bài tập |
|---|---|
| **A** | Thêm một job chạy `hadolint` kiểm tra Dockerfile |
| **B** | Rút pipeline xuống dưới 4 phút. Ghi lại **trước/sau** từng tối ưu |
| **C** | Pipeline xanh nhưng bản mới không lên. Liệt kê 4 nguyên nhân có thể và cách xác minh từng cái |
| **D** | Đội deploy mỗi tháng một lần, 4 tiếng, hay hỏng. Đề xuất 3 việc làm trước tiên **kèm lý do** |

📖 Chi tiết: [Ngày 35](./Giai-doan-3-CICD-K8s-Monitoring.md#ngày-35--milestone-pipeline-cicd-hoàn-chỉnh)

---

## Dự án 05 — Hệ thống quan sát được

> 📋 **Đề bài:** Hệ thống phải trả lời được bốn câu hỏi **mà không cần bạn SSH vào đâu cả**: có khoẻ không? có vi phạm cam kết không? hỏng thì tôi có biết không? hỏng thì có tự chữa không?
>
> **Làm sau:** Ngày 51 · **Thời lượng:** 5–7 giờ

### ✅ Yêu cầu

| # | Bắt buộc |
|---|---|
| 1 | Ứng dụng tự expose **metric nghiệp vụ**, không chỉ CPU/RAM |
| 2 | Prometheus thu được metric của mọi thành phần |
| 3 | Dashboard đủ 4 tín hiệu vàng, **provisioning từ file** |
| 4 | Log tập trung, tra được theo dịch vụ |
| 5 | SLO + ngân sách lỗi hiển thị được |
| 6 | Ít nhất 3 cảnh báo **gửi tới kênh thật** |
| 7 | **Diễn tập sự cố** có ghi biên bản |

| # | Nâng cao |
|---|---|
| 8 | Cảnh báo theo tốc độ đốt ngân sách, hai khung thời gian |
| 9 | Mỗi cảnh báo kèm runbook |
| 10 | Distributed tracing |
| 11 | Sao lưu tự động có kiểm chứng + đo RTO thật |

### 📐 Rubric (100 điểm)

| Hạng mục | Điểm |
|---|---|
| Thu thập metric | 15 |
| Dashboard | 15 |
| Log tập trung | 15 |
| SLO & ngân sách lỗi | 20 |
| Cảnh báo | 15 |
| Diễn tập sự cố | 20 |

### 🔥 Sáu kịch bản diễn tập

Với **mỗi** kịch bản, ghi ba điều: hệ thống phản ứng thế nào · bạn có được báo không · mất bao lâu hồi phục.

| # | Kịch bản | Đáng lẽ phải xảy ra |
|---|---|---|
| 1 | Giết 1 pod/container backend | Không gián đoạn, bản mới lên trong vài giây |
| 2 | Giết **toàn bộ** backend | Gián đoạn ngắn rồi tự hồi phục |
| 3 | Làm readiness trượt ở 1 bản | Bị rút khỏi cụm, **không** bị restart |
| 4 | Dừng database | Cảnh báo bắn; app suy giảm có kiểm soát, không treo |
| 5 | Đổ tải cao | Tự mở rộng; độ trễ vẫn trong ngưỡng SLO |
| 6 | Xoá dữ liệu rồi khôi phục | Khôi phục được; **ghi lại RTO thật** |

### 🎓 Bài tập 4 mức

| Mức | Bài tập |
|---|---|
| **A** | Thêm một panel hiển thị số request theo mã HTTP |
| **B** | Đặt SLO dựa trên **số đo thật** của hệ thống bạn, giải thích vì sao chọn con số đó |
| **C** | Dashboard hiện p95 tăng vọt nhưng tỉ lệ lỗi vẫn 0%. Nêu 3 nguyên nhân và cách xác minh |
| **D** | Viết postmortem cho kịch bản 4, **không đổ lỗi**, có hành động khắc phục kèm người chịu trách nhiệm |

📖 Chi tiết: [Ngày 51](./Giai-doan-4-SRE-Capstone.md#ngày-51--site-reliability-engineering-sre--nguyên-lý) · [Ngày 58](./Giai-doan-4-SRE-Capstone.md#ngày-58--dự-án-tốt-nghiệp--phần-3-monitoring--reliability)

---

## 🎓 CAPSTONE — CloudNote

> Dự án tốt nghiệp: **ghép tất cả** thành một hệ thống duy nhất, đủ để đem đi phỏng vấn.

```text
   Người dùng
       │
   [Ingress] ──> [Frontend] ──> [API] ──> [PostgreSQL]
                                  │
                        [Prometheus · Grafana · Loki]

   Tạo bởi: Terraform (hạ tầng) + Helm (ứng dụng)
   Đi qua:  Git → CI → registry → GitOps → cluster
```

| Phần | Nội dung | Điểm | Chi tiết |
|---|---|---|---|
| 1 | Thiết kế & Hạ tầng | 25 | [Ngày 56](./Giai-doan-4-SRE-Capstone.md#ngày-56--dự-án-tốt-nghiệp--phần-1-thiết-kế--hạ-tầng) |
| 2 | Container & CI/CD | 30 | [Ngày 57](./Giai-doan-4-SRE-Capstone.md#ngày-57--dự-án-tốt-nghiệp--phần-2-container--cicd) |
| 3 | Giám sát & Độ tin cậy | 30 | [Ngày 58](./Giai-doan-4-SRE-Capstone.md#ngày-58--dự-án-tốt-nghiệp--phần-3-monitoring--reliability) |
| 4 | Tài liệu & Portfolio | 15 | [Ngày 59](./Giai-doan-4-SRE-Capstone.md#ngày-59--dự-án-tốt-nghiệp--phần-4-tài-liệu-demo--portfolio) |

🏗️ **Bộ khung code sẵn:** [`capstone-cloudnote/`](./capstone-cloudnote/) — 26 file chạy được, nhiều `# TODO` để bạn tự hoàn thiện.

**Đạt 80/100 trở lên** là một dự án portfolio mạnh.

---

## 📊 Bảng theo dõi dự án

| Dự án | Ngày bắt đầu | Ngày xong | Điểm tự chấm | Link repo | Ghi chú |
|---|---|---|---|---|---|
| 01 — Linux server | | | ___ /100 | | |
| 02 — Container app | | | ___ /100 | | |
| 03 — Tự động hoá | | | ___ /100 | | |
| 04 — CI/CD | | | ___ /100 | | |
| 05 — Observability | | | ___ /100 | | |
| 🎓 Capstone | | | ___ /100 | | |

---

## 💡 Bảy lời khuyên khi làm dự án

1. **Đẩy mỗi dự án lên một repo GitHub riêng.** Nhà tuyển dụng xem GitHub trước khi gọi phỏng vấn. Sáu repo có README tử tế nói nhiều hơn một dòng "biết Docker" trong CV.

2. **README quan trọng ngang code.** Người xem dành chưa tới 3 phút. Sơ đồ + ảnh chụp + **số liệu thật** phải nằm trong 60 giây đầu.

3. **Ghi lại số liệu khi làm, đừng để cuối mới nhớ.** Thời gian deploy, thời gian quay lui, kích thước image, tỉ lệ khả dụng — đó là thứ khiến bạn khác biệt lúc phỏng vấn.

4. **Nêu giới hạn của dự án.** *"Chạy trên một node nên chưa thể hiện HA ở tầng cluster — xem ADR-001"* khiến bạn đáng tin hơn, không phải yếu đi.

5. **Đừng ôm đồm tính năng ứng dụng.** Người phỏng vấn quan tâm **pipeline, hạ tầng, giám sát** — không quan tâm app của bạn có bao nhiêu màn hình.

6. **Làm xong thì phá thử.** Giết container, dừng database, đổ tải. Dự án bạn *dám phá trước mặt người khác* là dự án bạn thật sự hiểu.

7. **Viết ADR cho mỗi quyết định lớn.** Câu *"vì sao bạn chọn cái này?"* là câu hỏi phỏng vấn kinh điển. Có ADR sẵn nghĩa là bạn đã suy nghĩ thấu đáo, không chọn bừa.

---

## Liên kết

| File | Dùng khi |
|---|---|
| [ROADMAP.md](./ROADMAP.md) | Xem dự án này nằm ở đâu trong lộ trình |
| [PROGRESS.md](./PROGRESS.md) | Tick tiến độ và ghi điểm |
| [HOC-HANG-NGAY.md](./HOC-HANG-NGAY.md) | Nhịp học ngày/tuần/tháng |
| [INTERVIEW.md](./INTERVIEW.md) | Tập kể về dự án của bạn |
| [TROUBLESHOOTING.md](./TROUBLESHOOTING.md) | Khi kẹt giữa chừng |
