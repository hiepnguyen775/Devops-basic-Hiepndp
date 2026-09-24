# ⚡ Cheat Sheet — Tra nhanh

> Bảng tra lệnh dùng hằng ngày. **Chi tiết đầy đủ nằm ở phụ lục cuối mỗi file giai đoạn** — link ở cuối trang.

---

## 🐧 Linux

```bash
# Tiến trình & dịch vụ
systemctl status|start|stop|restart|enable <dv>
journalctl -u <dv> -n 50 --no-pager     # log dịch vụ
journalctl -p err -n 30                 # chỉ lỗi
ps aux --sort=-%mem | head              # ngốn RAM nhất

# Tài nguyên
df -h              # đĩa   |  df -i  → inode
free -h            # RAM
du -sh /var/* | sort -h | tail          # thư mục nào to
lsof +L1           # file đã xoá nhưng còn tiến trình giữ

# Quyền
chown -R user:group <duong-dan>
chmod 755 <thu-muc>  ·  chmod 644 <file>
```

## 🌐 Mạng

```bash
ss -tlnp                       # cổng nào đang nghe, tiến trình nào
ip route get 8.8.8.8           # gói này đi đường nào
dig +short <domain>            # phân giải DNS
nc -zv <host> <port>           # cổng có mở không
curl -o /dev/null -s -w "%{http_code} %{time_total}s\n" <url>
sudo tcpdump -i any -n 'host X and port Y' -c 10
```

| Tín hiệu | Nghĩa |
|---|---|
| `Connection refused` | Tới được máy, **không ai nghe** ở cổng đó |
| `Connection timed out` | Bị chặn im lặng — **tường lửa** |

## 🐳 Docker

```bash
docker ps -a                              # kể cả container đã chết
docker logs <c> --tail 50 -f
docker exec -it <c> sh
docker inspect <c> --format '{{.State.ExitCode}}'
docker compose up -d --build  ·  down -v  ·  ps  ·  logs -f
docker system df              # còn bao nhiêu có thể thu hồi
docker system prune -af --volumes         # ⚠️ XOÁ volume không dùng
```

| Mã thoát | Nghĩa |
|---|---|
| `0` | Thoát bình thường (thường là lệnh chạy xong, không phải dịch vụ nền) |
| `1` | Lỗi ứng dụng |
| `127` | Không tìm thấy lệnh (alpine không có `bash`) |
| `137` | **OOMKilled** — vượt limits RAM |

## ☸️ Kubernetes

```bash
kubectl get pods -o wide  ·  get all  ·  get events --sort-by=.lastTimestamp
kubectl describe pod <p>                  # Events ở CUỐI — quan trọng nhất
kubectl logs <p> --previous               # log LẦN CHẠY TRƯỚC
kubectl get endpoints <svc>               # Service có thấy pod không → <none> = sai selector
kubectl rollout status|undo|restart deploy/<d>
kubectl top nodes  ·  top pods
kubectl exec -it <p> -- sh
kubectl port-forward deploy/<d> 8080:80
```

**Thứ tự chẩn đoán:** `describe` (vì sao) → `logs --previous` (app nói gì) → `events` (cluster làm gì)

## 🔀 Git

```bash
git log --oneline --graph --all -10
git diff  ·  git diff --staged
git switch -c <nhanh>  ·  git switch <nhanh>
git rebase main  ·  git rebase -i HEAD~3
git revert <sha>                # AN TOÀN — tạo commit mới
git reset --hard <sha>          # ⚠️ MẤT thay đổi chưa commit
git stash  ·  git stash pop
```

## 🏗️ Terraform

```bash
terraform init  ·  validate  ·  fmt -recursive
terraform plan              # ĐỌC KỸ dòng -/+ = huỷ rồi tạo lại
terraform apply  ·  destroy
terraform state list  ·  state show <resource>
terraform workspace show    # ⚠️ chạy TRƯỚC mọi apply/destroy
terraform import <resource> <id>
```

## 🔧 Ansible

```bash
ansible all -m ping
ansible-playbook site.yml --check --diff       # chạy khô
ansible-playbook site.yml --tags cau-hinh
ansible-inventory --graph
ansible-vault encrypt_string 'bi-mat' --name 'ten_bien'
```

## 📊 PromQL & LogQL

```promql
up                                              # target sống (1) / chết (0)
rate(http_requests_total[5m])                   # request/giây
sum by (code) (rate(http_requests_total[5m]))
histogram_quantile(0.95, rate(http_duration_bucket[5m]))
100 - avg(rate(node_cpu_seconds_total{mode="idle"}[5m])) * 100
```

```logql
{container="api"}                    # chọn nhãn — BẮT BUỘC
{container="api"} |= "error"         # lọc chuỗi
{job="docker"} |~ "(?i)(error|fail)" # regex
sum(rate({job="docker"} |= "error" [5m]))   # log → metric
```

| Loại metric | Cách dùng |
|---|---|
| Counter (chỉ tăng) | **Bắt buộc** bọc `rate()` |
| Gauge (lên xuống) | Đọc thẳng |
| Histogram | `histogram_quantile()` |

## 🔒 Bảo mật

```bash
# Quét bí mật trong TOÀN BỘ lịch sử Git
docker run --rm -v "$PWD:/repo" zricethezav/gitleaks:latest detect --source=/repo

# Quét lỗ hổng image
docker run --rm -v /var/run/docker.sock:/var/run/docker.sock \
  aquasec/trivy:latest image --severity HIGH,CRITICAL --ignore-unfixed <image>

# Kiểm tra Dockerfile
docker run --rm -i hadolint/hadolint < Dockerfile

# Chứng chỉ TLS
echo | openssl s_client -connect <host>:443 -servername <host> 2>/dev/null \
  | openssl x509 -noout -subject -issuer -dates
```

---

## ⚠️ Lệnh cần dừng lại suy nghĩ trước khi gõ

| Lệnh | Hậu quả |
|---|---|
| `rm -rf` | Không hoàn tác được |
| `docker system prune -af --volumes` | **Xoá mọi volume** không gắn container đang chạy |
| `terraform destroy` | Xoá hạ tầng — **kiểm tra workspace trước** |
| `kubectl delete namespace` | Xoá mọi thứ bên trong |
| `git reset --hard` | Mất thay đổi chưa commit |
| `git push --force` | Ghi đè lịch sử của người khác |
| `> file` | Xoá sạch nội dung file |

> 🔑 Với mọi lệnh trên: chạy lệnh **xem trước** tương ứng (`ls`, `plan`, `--dry-run`, `get`) rồi mới thực thi.

---

## 📖 Cheat sheet đầy đủ theo giai đoạn

| Giai đoạn | Link |
|---|---|
| 1 — Linux & SysOps | [Phụ lục C](../../Giai-doan-1-Linux-SysOps.md#phụ-lục-c--cheat-sheet-lệnh-dùng-hàng-ngày) |
| 2 — Git, Docker & Cloud | [Phụ lục C](../../Giai-doan-2-Git-Docker-Cloud.md#phụ-lục-c--cheat-sheet) |
| 3 — CI/CD, K8s & Monitoring | [Phụ lục C](../../Giai-doan-3-CICD-K8s-Monitoring.md#phụ-lục-c--cheat-sheet) |
| 4 — SRE (tổng hợp cả 4 GĐ) | [Phụ lục A](../../Giai-doan-4-SRE-Capstone.md#phụ-lục-a--cheat-sheet-tổng-hợp-theo-giai-đoạn) |

---

[⬅️ docs](../README.md) · [📚 GLOSSARY](../../GLOSSARY.md) · [🐛 TROUBLESHOOTING](../../TROUBLESHOOTING.md)
