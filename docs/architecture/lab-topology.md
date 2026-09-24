# 🖥️ LAB Topology — Thiết kế môi trường thực hành

> Hai phương án: **VMware đầy đủ** (giống production nhất) và **nhẹ** (Docker + Multipass, chạy được với 8 GB RAM).
>
> Chọn theo máy bạn có. Mọi bài học đều làm được bằng **cả hai**.

---

## Chọn phương án nào

| | Phương án A — VMware | Phương án B — Nhẹ |
|---|---|---|
| RAM tối thiểu | **16 GB** | **8 GB** |
| Đĩa trống | 150 GB | 60 GB |
| Giống production | ⭐⭐⭐⭐⭐ — máy thật, mạng thật | ⭐⭐⭐ — đủ để học mọi khái niệm |
| Dựng lại khi hỏng | 10–20 phút | **90 giây** |
| Học được gì thêm | Mạng nhiều máy, định tuyến, HA thật | — |
| Hợp với | Có máy khoẻ, muốn sát thực tế | Laptop thường, muốn nhanh |

> 🔑 **Nếu phân vân, chọn B.** Bạn học được **cùng một lượng khái niệm** và dựng lại nhanh hơn nhiều khi làm hỏng — mà làm hỏng là chuyện sẽ xảy ra liên tục, và đó là điều tốt.
>
> Chuyển từ B sang A lúc nào cũng được: cùng những lệnh đó, chỉ khác nơi chạy.

---

# Phương án A — VMware (16 GB RAM)

## Sơ đồ tổng thể

```text
                          Internet
                              │
                    ┌─────────┴─────────┐
                    │   VMware NAT       │  192.168.100.0/24
                    │   (vmnet8)         │  Gateway: 192.168.100.2
                    └─────────┬─────────┘
                              │
        ┌─────────────┬───────┴───────┬─────────────┐
        │             │               │             │
   ┌────┴────┐   ┌────┴────┐    ┌────┴────┐   ┌────┴────┐
   │  ctrl   │   │  node1  │    │  node2  │   │  node3  │
   │  .10    │   │  .11    │    │  .12    │   │  .13    │
   │ 2C/4G   │   │ 2C/4G   │    │ 2C/2G   │   │ 2C/2G   │
   └─────────┘   └─────────┘    └─────────┘   └─────────┘
   Điều khiển     Worker         Worker        Worker
   Ansible        K8s CP         K8s           K8s
   Terraform      App            App           Database
   Giám sát
```

## Bảng tài nguyên

| VM | Hostname | IP | CPU | RAM | Đĩa | Vai trò |
|---|---|---|---|---|---|---|
| 1 | `ctrl` | 192.168.100.10 | 2 | 4 GB | 40 GB | Ansible controller · Terraform · Prometheus/Grafana |
| 2 | `node1` | 192.168.100.11 | 2 | 4 GB | 40 GB | K8s control plane · web server |
| 3 | `node2` | 192.168.100.12 | 2 | 2 GB | 30 GB | K8s worker · ứng dụng |
| 4 | `node3` | 192.168.100.13 | 2 | 2 GB | 30 GB | K8s worker · database |
| | **Tổng** | | **8** | **12 GB** | **140 GB** | *(chừa 4 GB cho máy chủ)* |

> ⚠️ **Không bật cả 4 VM cùng lúc nếu chỉ có 16 GB.** Xem bảng "bật VM nào khi nào" ở dưới.

## Thông số chung mọi VM

| Mục | Giá trị |
|---|---|
| Hệ điều hành | **Ubuntu Server 24.04 LTS** (bản minimal, không GUI) |
| Mạng | NAT (`vmnet8`) — có Internet, và các VM thấy nhau |
| Đĩa | Thin provision, tách thành nhiều file |
| Ảo hoá lồng | **Bật** trên node1–3 (cần cho Docker/K8s chạy mượt) |
| User | `quantri` · sudo không mật khẩu · **chỉ đăng nhập bằng khoá** |
| Snapshot | Chụp một snapshot **"sạch"** ngay sau khi cài xong |

## Kế hoạch IP

| Dải | Dùng cho |
|---|---|
| `192.168.100.0/24` | Mạng VMware NAT |
| `192.168.100.1` | Máy chủ (máy thật của bạn) |
| `192.168.100.2` | Gateway NAT |
| `192.168.100.10–13` | Bốn VM (IP **tĩnh**) |
| `192.168.100.100–200` | DHCP — để trống cho VM tạm |
| `10.244.0.0/16` | Pod network của Kubernetes |
| `10.96.0.0/12` | Service network của Kubernetes |

> ⚠️ **Kiểm tra trùng dải trước khi bắt đầu.** Nếu mạng nhà/công ty bạn cũng dùng `192.168.100.x` thì đổi sang `192.168.56.x` hoặc `10.10.10.x`. Trùng dải gây lỗi định tuyến rất khó chẩn đoán.

## Bật VM nào khi nào

Với 16 GB RAM, đừng bật hết cùng lúc:

| Giai đoạn | VM cần bật | RAM dùng |
|---|---|---|
| **GĐ1** — Linux (Ngày 1–12) | `node1` | 4 GB |
| **GĐ2** — Docker (13–25) | `node1` | 4 GB |
| **GĐ2** — Cloud/IaC (26–30) | `ctrl` + `node1` | 8 GB |
| **GĐ3** — CI/CD (31–35) | `ctrl` + `node1` | 8 GB |
| **GĐ3** — Kubernetes (36–43) | `node1` + `node2` + `node3` | 8 GB |
| **GĐ3** — Giám sát (44–50) | `ctrl` + `node1` + `node2` | 10 GB |
| **GĐ4** — SRE (51–60) | Tất cả | 12 GB |

## Dựng VM — hai cách

### Cách 1: Cài tay (lần đầu, hiểu rõ từng bước)

```text
1. Tải Ubuntu Server 24.04 LTS ISO
2. VMware → Create New VM → chọn ISO
3. Cấu hình CPU/RAM/đĩa theo bảng trên
4. Settings → Processors → tick "Virtualize Intel VT-x/EPT"
5. Cài đặt:
   - Hostname theo bảng
   - Chọn "Install OpenSSH server"
   - KHÔNG cài snap package nào thêm
6. Sau khi cài xong: đặt IP tĩnh, nạp khoá SSH, chụp snapshot "sach"
```

Đặt IP tĩnh bằng netplan (`/etc/netplan/01-static.yaml`):

```yaml
network:
  version: 2
  ethernets:
    ens33:
      dhcp4: false
      addresses: [192.168.100.11/24]
      routes:
        - to: default
          via: 192.168.100.2
      nameservers:
        addresses: [1.1.1.1, 8.8.8.8]
```

```bash
sudo netplan try      # tự rollback sau 120s nếu mất mạng — AN TOÀN
sudo netplan apply
```

### Cách 2: Tự động bằng Vagrant (khuyến nghị sau lần đầu)

```ruby
# Vagrantfile
MAY = {
  "ctrl"  => { ip: "192.168.100.10", ram: 4096, cpu: 2 },
  "node1" => { ip: "192.168.100.11", ram: 4096, cpu: 2 },
  "node2" => { ip: "192.168.100.12", ram: 2048, cpu: 2 },
  "node3" => { ip: "192.168.100.13", ram: 2048, cpu: 2 },
}

Vagrant.configure("2") do |config|
  config.vm.box = "bento/ubuntu-24.04"

  MAY.each do |ten, cfg|
    config.vm.define ten do |m|
      m.vm.hostname = ten
      m.vm.network "private_network", ip: cfg[:ip]
      m.vm.provider "vmware_desktop" do |v|
        v.memory = cfg[:ram]
        v.cpus   = cfg[:cpu]
        v.vmx["vhv.enable"] = "TRUE"      # ảo hoá lồng
      end
      m.vm.provision "shell", path: "cloud-init-chung.sh"
    end
  end
end
```

```bash
vagrant up              # dựng cả 4 VM
vagrant up node1        # chỉ bật một VM
vagrant halt            # tắt hết
vagrant destroy -f      # xoá sạch, dựng lại từ đầu
```

> 💡 **Vagrant đáng đầu tư 30 phút học.** Nó biến việc dựng lại 4 VM từ *"cả buổi cài đặt"* thành **một lệnh** — và bạn sẽ dựng lại nhiều lần hơn bạn nghĩ.

## Topology theo từng module

Cùng 4 VM đó, vai trò đổi theo bài học:

**Module 07 — Ansible**
```text
   ctrl (Ansible controller)
     │  SSH
     ├──> node1
     ├──> node2
     └──> node3
```

**Module 06 — Docker**
```text
   node1 (Docker host)
     ├── nginx (reverse proxy)
     ├── app
     └── postgres
```

**Module 11 — Kubernetes**
```text
   node1 (control plane)          node2, node3 (worker)
     ├── kube-apiserver             ├── kubelet
     ├── etcd                       ├── kube-proxy
     ├── scheduler                  └── pod
     └── controller-manager
```

**Module 12 — Giám sát**
```text
   ctrl                        node1, node2
     ├── Prometheus  <──scrape──── node-exporter
     ├── Grafana                   cAdvisor
     └── Loki        <──push────── Promtail
```

---

# Phương án B — Nhẹ (8 GB RAM)

## Sơ đồ

```text
              Máy của bạn (Linux/WSL2)
                        │
     ┌──────────┬───────┴───────┬──────────┐
     │          │               │          │
  Docker     Multipass       minikube   LocalStack
     │          │               │          │
  container  VM Ubuntu       cluster    giả lập
  (GĐ2,3)    (GĐ2 cloud)     (GĐ3)      AWS (GĐ2)
```

## Công cụ thay thế tương ứng

| Cần gì | Phương án A | Phương án B | Giống nhau ở |
|---|---|---|---|
| Máy chủ Linux | VM VMware | **Multipass** | Dùng **chính cloud-init** như cloud thật |
| Nhiều máy (Ansible) | 3 VM | **3 container có sshd** | Với Ansible thì không khác gì |
| Kubernetes | 3 VM + kubeadm | **minikube** | Mọi khái niệm K8s giống hệt |
| Dịch vụ AWS | Tài khoản thật | **LocalStack** | Cùng lệnh `aws` CLI, chỉ đổi endpoint |
| Kho Terraform state | S3 | **MinIO** | Cùng giao thức S3 |
| Runner CI | VM | **GitHub Actions** | Runner miễn phí |

## Lệnh dựng nhanh

```bash
# Máy chủ Linux (thay VM)
multipass launch 24.04 --name may-web --cpus 1 --memory 1G --disk 5G \
  --cloud-init cloud-init.yaml

# Kubernetes
minikube start --driver=docker --memory=3072 --cpus=2
minikube addons enable ingress metrics-server

# Giả lập AWS
docker run -d -p 4566:4566 localstack/localstack:3.8

# Ba "server" cho Ansible
docker compose up -d      # 3 container Debian có sshd
```

## RAM dùng bao nhiêu

| Đang học | Chạy gì | RAM |
|---|---|---|
| GĐ1 Linux | 1 Multipass VM | ~1 GB |
| GĐ2 Docker | Docker + vài container | ~2 GB |
| GĐ2 Cloud | Multipass + LocalStack | ~2 GB |
| GĐ3 K8s | minikube | ~4 GB |
| GĐ3 Giám sát | Docker Compose 7 container | ~2 GB |

**Cao điểm khoảng 4 GB** — chạy tốt trên máy 8 GB.

---

## 🔧 Chuẩn bị chung (cả hai phương án)

### Phần mềm trên máy chủ

| Công cụ | Kiểm tra |
|---|---|
| Git | `git --version` |
| Docker | `docker --version` |
| Trình soạn thảo | VS Code hoặc vim |
| Terminal | Có SSH client |

### Khoá SSH cho lab

Tạo **khoá riêng cho lab**, không dùng khoá cá nhân:

```bash
ssh-keygen -t ed25519 -f ~/.ssh/khoa-lab -N "" -C "devops-lab"
```

### Kỷ luật snapshot

| Khi nào | Chụp snapshot tên |
|---|---|
| Cài xong OS, chưa đụng gì | `sach` |
| Trước mỗi bài có bước nguy hiểm | `truoc-ngay-XX` |
| Sau khi hoàn thành một giai đoạn | `xong-gd-X` |

> 💡 **Snapshot là lưới an toàn cho phép bạn dám phá.** Người học sợ làm hỏng sẽ không dám thử — mà thử và hỏng mới là lúc học được nhiều nhất. Có snapshot, hỏng thì quay lại trong 10 giây.

---

## ⚠️ Những vấn đề hay gặp

| Triệu chứng | Nguyên nhân | Cách sửa |
|---|---|---|
| VM không có mạng | Sai loại adapter | Dùng NAT (`vmnet8`), không dùng Host-only |
| Các VM không thấy nhau | Khác mạng ảo | Đảm bảo cùng `vmnet8` |
| Docker trong VM rất chậm | Chưa bật ảo hoá lồng | VMware → Processors → tick VT-x/EPT |
| minikube không khởi động | Thiếu RAM | `minikube start --memory=2048` |
| Máy chủ chậm khi bật nhiều VM | Quá tải RAM | Xem bảng "bật VM nào khi nào" |
| IP đổi sau khi reboot | Đang dùng DHCP | Đặt IP tĩnh bằng netplan |
| Không SSH vào VM được | Chưa cài OpenSSH server | `sudo apt install -y openssh-server` |

---

## Liên kết

| File | Dùng khi |
|---|---|
| [ROADMAP.md](../../ROADMAP.md) | Xem lộ trình tổng thể |
| [HOC-HANG-NGAY.md](../../HOC-HANG-NGAY.md) | Nhịp học ngày/tuần/tháng |
| [NT1 — Mạng chuyên sâu](../../Module-Nen-Tang-Mo-Rong.md) | Hiểu sâu về subnet và định tuyến |
| [TROUBLESHOOTING.md](../../TROUBLESHOOTING.md) | Khi môi trường lab có vấn đề |
