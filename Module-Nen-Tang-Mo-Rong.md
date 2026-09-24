# 🧱 Module Nền tảng Mở rộng — Mạng, Web Server & Ansible chuyên sâu

> **3 bài bổ sung** cho những chỗ mà lộ trình 60 ngày chỉ kịp chạm tới bề mặt.
>
> Mỗi bài ~120 phút, theo đúng khuôn: 📘 Lý thuyết → 🧪 LAB (file đầy đủ) → 🧭 Step by step → 💡 Đi làm mới thấm → 📝 Tự kiểm tra → 🎯 Đúc kết.
>
> 💻 **Chạy miễn phí trên máy bạn** — không cần cloud, không cần tên miền thật.

---

## Học bài nào, khi nào

| Bài | Nội dung | Học sau | Vì sao cần |
|---|---|---|---|
| **[NT1](#nt1--mạng-chuyên-sâu-subnet-định-tuyến-bắt-gói--tls)** | Subnet · Định tuyến · tcpdump · TLS | Ngày 9 | Ngày 7 cho bạn phản xạ debug; bài này cho bạn **bằng chứng** thay vì phỏng đoán |
| **[NT2](#nt2--web-server-production-https-load-balancing--tinh-chỉnh)** | HTTPS thật · Cân bằng tải · Tinh chỉnh | Ngày 23 | Ngày 23 dạy reverse proxy cơ bản; production cần thêm TLS, keepalive, log đúng |
| **[NT3](#nt3--ansible-nâng-cao-role-vault-rolling-update--inventory-động)** | Role · Vault · `serial` · Inventory động | Ngày 47 | Ngày 47 cho playbook chạy được; bài này cho playbook **dùng được trong đội** |

> 📌 **Ba bài độc lập nhau** — học theo nhu cầu, không bắt buộc tuần tự. Nhưng mỗi bài đều cần kiến thức của ngày tương ứng trong cột *"Học sau"*.

### Ba bài này lấp chỗ nào

| Lĩnh vực | Lộ trình 60 ngày | Sau module này |
|---|---|---|
| **Mạng** | IP, port, DNS, debug theo tầng *(Ngày 7)* | + subnetting, định tuyến, bắt gói, chẩn đoán TLS |
| **Web server** | Reverse proxy, upstream cơ bản *(Ngày 23)* | + HTTPS production, 4 thuật toán cân bằng tải, tinh chỉnh, log điều tra |
| **Ansible** | Playbook, idempotent, handler *(Ngày 47)* | + role, Vault đúng cách, cập nhật không gián đoạn, inventory động |

---

## NT1 — Mạng chuyên sâu: Subnet, Định tuyến, Bắt gói & TLS

> ⏱️ ~120 phút · Loại: Networking · **Học sau Ngày 9**
>
> 🧭 **Vì sao có bài này:** Ngày 7 cho bạn IP, port, DNS và phản xạ debug theo tầng — đủ để làm việc. Nhưng ba tình huống sau sẽ chặn bạn lại nếu không học sâu thêm:
> - *"Chia dải mạng cho VPC thế nào để sau này không đụng nhau?"* → cần **subnetting**
> - *"Gói tin đi đâu mất?"* → cần đọc được **bảng định tuyến** và **bắt gói**
> - *"HTTPS lỗi chứng chỉ"* → cần hiểu **bắt tay TLS**
>
> ✅ **Chuẩn bị:** máy Linux. Cài: `sudo apt install -y iproute2 tcpdump dnsutils openssl ipcalc`
>
> 🎁 **Cuối bài bạn có gì:** tự chia được dải mạng cho một hệ thống nhiều tầng, đọc được bảng định tuyến, **bắt gói tin tận mắt** để thấy TCP bắt tay ba bước, và chẩn đoán được lỗi chứng chỉ TLS.

### 📘 Lý thuyết

#### 1. CIDR — đọc `/24` không phải học thuộc, mà là đếm bit

Một địa chỉ IPv4 có **32 bit**. Dấu `/24` nghĩa là **24 bit đầu là phần mạng**, 8 bit còn lại là phần máy.

```text
192.168.1.0/24
────────┬─── ──┬
   phần mạng   phần máy (8 bit → 2^8 = 256 địa chỉ)
   (24 bit)
```

Bảng cần thuộc — chỉ 5 dòng, dùng suốt đời:

| CIDR | Số địa chỉ | Dùng được* | Hay dùng cho |
|---|---|---|---|
| `/24` | 256 | 254 | Một subnet thông thường |
| `/25` | 128 | 126 | Chia đôi một `/24` |
| `/26` | 64 | 62 | Subnet nhỏ |
| `/28` | 16 | 14 | Dải nhỏ cho vài máy |
| `/16` | 65.536 | 65.534 | Cả một VPC |

*Trừ 2: địa chỉ đầu là **địa chỉ mạng**, địa chỉ cuối là **broadcast**.

**Mẹo tính nhanh:** số địa chỉ = `2^(32 - số bit)`. `/26` → `2^6` = 64.

> ⚠️ **Trên cloud còn mất thêm địa chỉ.** AWS giữ riêng **5 địa chỉ** mỗi subnet (mạng, gateway, DNS, dự phòng, broadcast). Một `/28` trên AWS chỉ còn **11 địa chỉ dùng được**, không phải 14. Đây là chỗ hay tính hụt khi chia VPC.

#### 2. Dải IP riêng — ba khối phải nhớ

| Khối | Dải | Kích thước |
|---|---|---|
| `10.0.0.0/8` | 10.0.0.0 – 10.255.255.255 | ~16,7 triệu |
| `172.16.0.0/12` | 172.16.0.0 – 172.31.255.255 | ~1 triệu |
| `192.168.0.0/16` | 192.168.0.0 – 192.168.255.255 | 65.536 |

> 🔑 **Vì sao phải nhớ:** khi thiết kế VPC, nếu chọn dải trùng với mạng văn phòng hoặc trùng với đối tác, thì **VPN sẽ không kết nối được** — và sửa lúc đó nghĩa là đánh số lại toàn bộ hệ thống. Chọn dải là quyết định khó đảo ngược nhất trong thiết kế mạng.

Một cái bẫy rất hay gặp: **Docker mặc định dùng `172.17.0.0/16`**. Nếu mạng công ty bạn cũng dùng dải đó thì container sẽ không gọi ra được — và triệu chứng rất khó hiểu.

#### 3. Bảng định tuyến — máy quyết định gửi gói đi đâu

Mỗi khi gửi một gói tin, kernel tra bảng định tuyến theo nguyên tắc: **dòng nào khớp cụ thể nhất thì thắng**.

```text
đích 10.0.5.20  →  có dòng nào khớp 10.0.5.20/32 không?  (cụ thể nhất)
                →  có dòng nào khớp 10.0.5.0/24 không?
                →  có dòng nào khớp 10.0.0.0/8 không?
                →  dùng default (0.0.0.0/0) — "không biết thì gửi ra đây"
```

`default` chính là **gateway** — cửa ra mặc định khi máy không biết đích nằm ở đâu.

#### 4. Bắt tay TCP ba bước — nhìn tận mắt mới nhớ

```text
Client                          Server
  │                                │
  │──────── SYN ──────────────────>│   "Tôi muốn kết nối"
  │<─────── SYN-ACK ───────────────│   "Được, tôi cũng sẵn sàng"
  │──────── ACK ──────────────────>│   "Xác nhận"
  │                                │
  │═══════ dữ liệu đi lại ═════════│
  │                                │
  │──────── FIN ──────────────────>│   "Tôi đóng"
```

Hiểu điều này giúp bạn **đọc được lỗi**:

| Bạn thấy | Nghĩa là | Thường do |
|---|---|---|
| `Connection refused` | Server trả về **RST** ngay | Không có ai nghe ở cổng đó |
| `Connection timed out` | SYN gửi đi, **không có hồi âm** | Tường lửa chặn im lặng |
| Kết nối được rồi treo | Bắt tay xong nhưng không có dữ liệu | Ứng dụng treo, không phải lỗi mạng |

#### 5. Bắt tay TLS — vì sao HTTPS lại hay lỗi chứng chỉ

```text
1. Client Hello    →  "tôi hỗ trợ các bộ mã hoá này"
2. Server Hello    ←  "dùng bộ này" + GỬI CHUỖI CHỨNG CHỈ
3. Client kiểm tra chứng chỉ:
      ├─ Có do một CA mà tôi tin ký không?
      ├─ Tên miền có khớp không?          ← lỗi hay gặp nhất
      ├─ Còn hạn không?
      └─ Chuỗi có đủ không?               ← lỗi hay gặp thứ hai
4. Trao khoá phiên →  từ đây mã hoá đối xứng (nhanh hơn nhiều)
```

Bốn lỗi TLS phổ biến và cách đọc:

| Thông báo | Nguyên nhân |
|---|---|
| `certificate has expired` | Hết hạn — chứng chỉ Let's Encrypt chỉ sống 90 ngày |
| `Hostname mismatch` | Tên miền truy cập không nằm trong chứng chỉ (thiếu SAN) |
| `unable to get local issuer certificate` | **Thiếu chứng chỉ trung gian** — server chỉ gửi chứng chỉ lá |
| `self signed certificate` | Chứng chỉ tự ký, không có CA nào tin |

> 🔑 Lỗi *thiếu chứng chỉ trung gian* rất ranh ma: **trình duyệt thường vẫn vào được** (vì nó tự tải chứng chỉ thiếu), nhưng `curl` và các ứng dụng khác thì **lỗi**. Kết quả: "trên trình duyệt em thấy bình thường mà" — và mất nửa ngày để tìm ra.

### 🧪 LAB — Ba phần độc lập

**Phần A:** chia mạng cho một hệ thống thật · **Phần B:** đọc route và bắt gói · **Phần C:** chẩn đoán TLS

### 🧭 Hướng dẫn làm LAB — step by step

#### Bước 1 — Tự tính subnet trước, rồi mới dùng công cụ

Đề bài: bạn có `10.20.0.0/16` cho một VPC, cần chia thành:
- 3 subnet **công khai** (load balancer), mỗi cái ~250 địa chỉ
- 3 subnet **riêng tư** (ứng dụng), mỗi cái ~1000 địa chỉ
- 3 subnet **database**, mỗi cái ~60 địa chỉ

**Tự tính trước khi đọc tiếp:** 250 địa chỉ cần `/24`; 1000 địa chỉ cần `/22`; 60 địa chỉ cần `/26`.

```bash
# Kiểm chứng bằng ipcalc
ipcalc 10.20.0.0/24 | head -8
```

**Bạn sẽ thấy:**
```text
Address:   10.20.0.0
Netmask:   255.255.255.0 = 24
Network:   10.20.0.0/24
HostMin:   10.20.0.1
HostMax:   10.20.0.254
Hosts/Net: 254
```

✅ **Checkpoint:** `Hosts/Net` là 254 — khớp với tính tay.

Một cách chia gọn gàng, **chừa chỗ để mở rộng**:

| Loại | Dải | CIDR | Số địa chỉ |
|---|---|---|---|
| Công khai A/B/C | `10.20.0.0` · `10.20.1.0` · `10.20.2.0` | `/24` | 254 mỗi cái |
| *(dự phòng)* | `10.20.3.0` – `10.20.15.0` | | *để trống* |
| Riêng tư A/B/C | `10.20.16.0` · `10.20.20.0` · `10.20.24.0` | `/22` | 1022 mỗi cái |
| *(dự phòng)* | `10.20.28.0` – `10.20.31.0` | | *để trống* |
| Database A/B/C | `10.20.32.0` · `10.20.32.64` · `10.20.32.128` | `/26` | 62 mỗi cái |

💡 **Hai bài học thiết kế quan trọng hơn phép tính:**
1. **Luôn chừa khoảng trống giữa các nhóm.** Ba tháng nữa cần thêm một subnet riêng tư — có chỗ trống thì thêm được ngay, không thì phải đánh số lại.
2. **Nhóm theo chức năng, không theo thứ tự.** Mọi subnet công khai nằm trong `10.20.0.0/20`, mọi subnet riêng tư trong `10.20.16.0/20` — nhờ vậy viết được **một luật tường lửa cho cả nhóm** thay vì ba luật riêng lẻ.

Kiểm tra hai dải có chồng nhau không:
```bash
python3 -c "
import ipaddress as ip
a = ip.ip_network('10.20.16.0/22')
b = ip.ip_network('10.20.20.0/22')
print('Chồng nhau?' , a.overlaps(b))
print('10.20.17.5 thuộc A?', ip.ip_address('10.20.17.5') in a)
"
```

**Bạn sẽ thấy:**
```text
Chồng nhau? False
10.20.17.5 thuộc A? True
```

✅ **Checkpoint:** biết kiểm tra chồng dải bằng lệnh, không phải nhẩm.

#### Bước 2 — Đọc bảng định tuyến của máy bạn

```bash
ip route show
```

**Bạn sẽ thấy:**
```text
default via 192.168.1.1 dev eth0 proto dhcp metric 100
172.17.0.0/16 dev docker0 proto kernel scope link src 172.17.0.1
192.168.1.0/24 dev eth0 proto kernel scope link src 192.168.1.50
```

Đọc từng dòng:
| Dòng | Nghĩa |
|---|---|
| `default via 192.168.1.1` | Không biết đích ở đâu thì gửi tới gateway này |
| `172.17.0.0/16 dev docker0` | Mọi địa chỉ Docker đi thẳng qua cầu `docker0`, **không qua gateway** |
| `192.168.1.0/24 dev eth0` | Mạng LAN — cùng đoạn mạng, gửi trực tiếp |

✅ **Checkpoint:** giải thích được vì sao có dòng `docker0`.

Giờ hỏi kernel: **gói tin này sẽ đi đường nào?**

```bash
ip route get 8.8.8.8
ip route get 172.17.0.5
```

**Bạn sẽ thấy:**
```text
8.8.8.8 via 192.168.1.1 dev eth0 src 192.168.1.50 uid 1000
172.17.0.5 dev docker0 src 172.17.0.1 uid 1000
```

✅ **Checkpoint:** hai đích đi hai đường khác nhau — một qua gateway, một đi thẳng.

💡 **`ip route get` là lệnh chẩn đoán vàng.** Thay vì đoán *"gói tin có ra được không?"*, bạn hỏi thẳng kernel. Cực kỳ hữu ích khi có VPN, nhiều card mạng, hoặc container — những lúc đường đi không hiển nhiên.

#### Bước 3 — Bắt gói và nhìn thấy bắt tay TCP

Đây là bước biến lý thuyết thành thứ bạn *nhìn thấy*. Mở **hai terminal**.

**Terminal 1** — bắt gói:
```bash
sudo tcpdump -i any -n 'host example.com and tcp port 80' -c 10
```

**Terminal 2** — tạo một kết nối:
```bash
curl -s -o /dev/null http://example.com
```

**Bạn sẽ thấy ở Terminal 1:**
```text
10:15:32.101 IP 192.168.1.50.54321 > 93.184.216.34.80: Flags [S], seq 1234567
10:15:32.145 IP 93.184.216.34.80 > 192.168.1.50.54321: Flags [S.], seq 987654, ack 1234568
10:15:32.145 IP 192.168.1.50.54321 > 93.184.216.34.80: Flags [.], ack 1
10:15:32.146 IP 192.168.1.50.54321 > 93.184.216.34.80: Flags [P.], length 76: HTTP: GET / HTTP/1.1
10:15:32.190 IP 93.184.216.34.80 > 192.168.1.50.54321: Flags [P.], length 1440: HTTP: HTTP/1.1 200 OK
```

✅ **Checkpoint:** nhận ra đúng ba dòng đầu là **bắt tay ba bước**.

Đọc cột `Flags`:
| Ký hiệu | Nghĩa |
|---|---|
| `[S]` | SYN — xin kết nối |
| `[S.]` | SYN-ACK — đồng ý (dấu `.` là ACK) |
| `[.]` | ACK — xác nhận |
| `[P.]` | PUSH — có dữ liệu |
| `[F.]` | FIN — đóng kết nối |
| `[R]` | **RST — từ chối thẳng** |

💡 Để ý khoảng cách thời gian giữa dòng 1 và dòng 2: **44 mili giây**. Đó là độ trễ mạng thật tới server — đo được, không phải đoán.

Giờ xem **kết nối bị từ chối** trông thế nào:

```bash
# Terminal 1
sudo tcpdump -i lo -n 'tcp port 9999' -c 4
# Terminal 2
curl -s --max-time 3 http://localhost:9999
```

**Bạn sẽ thấy:**
```text
IP 127.0.0.1.55555 > 127.0.0.1.9999: Flags [S], seq ...
IP 127.0.0.1.9999 > 127.0.0.1.55555: Flags [R.], seq 1, ack 1
```

✅ **Checkpoint:** thấy `[R]` (RST) — đây chính là `Connection refused`.

💡 **So sánh hai tín hiệu bạn đã học ở Ngày 7, giờ thấy tận gói tin:**
- **RST trả về** → `Connection refused` → không có ai nghe
- **SYN gửi đi, im lặng** → `timeout` → tường lửa nuốt gói

Giờ bạn không chỉ *nhớ* quy tắc — bạn *thấy* nó.

#### Bước 4 — Chẩn đoán chứng chỉ TLS

```bash
echo | openssl s_client -connect github.com:443 -servername github.com 2>/dev/null \
  | openssl x509 -noout -subject -issuer -dates
```

**Bạn sẽ thấy:**
```text
subject=CN=github.com
issuer=C=US, O=Sectigo Limited, CN=Sectigo ECC Domain Validation Secure Server CA
notBefore=Feb 5 00:00:00 2026 GMT
notAfter=Mar 6 23:59:59 2027 GMT
```

✅ **Checkpoint:** đọc được chủ thể, đơn vị cấp và hạn của chứng chỉ.

Xem **chuỗi chứng chỉ** — đây là chỗ hay hỏng:

```bash
echo | openssl s_client -connect github.com:443 -servername github.com 2>/dev/null \
  | grep -E "^ *[0-9]+ s:|^ *i:"
```

**Bạn sẽ thấy:**
```text
 0 s:CN=github.com
   i:C=US, O=Sectigo Limited, CN=Sectigo ECC Domain Validation Secure Server CA
 1 s:C=US, O=Sectigo Limited, CN=Sectigo ECC Domain Validation Secure Server CA
   i:C=GB, O=Sectigo Limited, CN=Sectigo ECC Certification Authority
```

✅ **Checkpoint:** thấy **chuỗi** — chứng chỉ lá (0) được ký bởi chứng chỉ trung gian (1).

💡 **Đây chính là chỗ lỗi `unable to get local issuer certificate` xảy ra:** nếu server chỉ gửi chứng chỉ lá mà **quên gửi chứng chỉ trung gian**, client không nối được chuỗi lên tới CA gốc. Trình duyệt tự tải bù nên vẫn vào được, nhưng `curl` thì lỗi — dẫn tới cuộc tranh luận *"trên máy em thấy bình thường mà"*.

Kiểm tra số ngày còn lại (dùng cho cảnh báo tự động):

```bash
for host in github.com google.com; do
  het_han=$(echo | openssl s_client -connect $host:443 -servername $host 2>/dev/null \
    | openssl x509 -noout -enddate | cut -d= -f2)
  con_lai=$(( ($(date -d "$het_han" +%s) - $(date +%s)) / 86400 ))
  printf "%-15s còn %3d ngày\n" "$host" "$con_lai"
done
```

**Bạn sẽ thấy:**
```text
github.com      còn 164 ngày
google.com      còn  72 ngày
```

✅ **Checkpoint:** tính được số ngày còn lại bằng script.

💡 **Chứng chỉ hết hạn là một trong những sự cố ngớ ngẩn và phổ biến nhất** — cả hệ thống chết vì một thứ ai cũng biết trước ngày nó xảy ra. Script trên đưa vào cron + cảnh báo trước 30 ngày là đủ phòng.

#### Bước 5 — Tự tạo lỗi TLS để nhận diện

```bash
# Tạo chứng chỉ tự ký cho tên miền "shop.local"
openssl req -x509 -newkey rsa:2048 -nodes -days 365 \
  -keyout /tmp/khoa.pem -out /tmp/chung-chi.pem \
  -subj "/CN=shop.local" 2>/dev/null

# Dựng server HTTPS bằng chứng chỉ đó
openssl s_server -accept 8443 -cert /tmp/chung-chi.pem -key /tmp/khoa.pem -quiet &
sleep 1

echo "--- Lỗi 1: chứng chỉ tự ký ---"
curl -s https://localhost:8443 2>&1 | head -2

echo "--- Lỗi 2: tên miền không khớp (bỏ qua lỗi tự ký) ---"
curl -sk --resolve shop.local:8443:127.0.0.1 https://localhost:8443 2>&1 | head -2

echo "--- Bỏ qua kiểm tra (CHỈ dùng khi debug) ---"
curl -sk https://localhost:8443 2>&1 | head -2

kill %1 2>/dev/null
```

**Bạn sẽ thấy:**
```text
--- Lỗi 1: chứng chỉ tự ký ---
curl: (60) SSL certificate problem: self-signed certificate
```

✅ **Checkpoint:** nhận ra thông báo lỗi ứng với từng nguyên nhân.

⚠️ **Về cờ `-k`:** nó bỏ qua **toàn bộ** kiểm tra chứng chỉ. Dùng để debug thì được; đưa vào script production là **tự tay tắt lớp bảo vệ chống tấn công xen giữa**. Nếu thấy `-k` hoặc `verify=False` trong code production, đó là một lỗ hổng cần sửa, không phải một tuỳ chọn.

#### Bước 6 — MTU và một lỗi mạng rất khó chẩn đoán

Đây là lỗi khiến nhiều người mất cả ngày: **kết nối mở được, gói nhỏ đi qua bình thường, nhưng gói lớn thì treo**.

```bash
ip link show | grep -E "^[0-9]+: (eth|ens|enp)" -A1 | grep mtu
```

**Bạn sẽ thấy:** `mtu 1500` (giá trị chuẩn Ethernet).

Thử tìm MTU thật của đường truyền:

```bash
ping -c1 -M do -s 1472 8.8.8.8 | tail -2     # 1472 + 28 header = 1500
ping -c1 -M do -s 1500 8.8.8.8 | tail -2     # vượt MTU
```

**Bạn sẽ thấy:**
```text
1 packets transmitted, 1 received, 0% packet loss

ping: local error: message too long, mtu=1500
```

✅ **Checkpoint:** thấy ranh giới MTU.

💡 **Vì sao điều này quan trọng với DevOps:** VPN, tunnel và một số mạng overlay của Kubernetes **giảm MTU** (ví dụ xuống 1450) vì phải thêm header riêng. Nếu MTU không được điều chỉnh đúng, triệu chứng sẽ là: *SSH kết nối được nhưng treo khi chạy lệnh có output dài*, hoặc *API trả về được response nhỏ nhưng treo với response lớn*.

Đây là loại lỗi gần như không ai nghĩ tới, nên biết trước là tiết kiệm được rất nhiều giờ.

### 💡 Đi làm mới thấm

- **Chọn dải IP là quyết định khó đảo ngược nhất.** Trùng dải với mạng văn phòng hoặc với đối tác thì VPN không kết nối được, và sửa nghĩa là đánh số lại toàn bộ. Trước khi chọn, hãy hỏi: *"tổ chức này đang dùng những dải nào?"* và ghi lại vào một bảng chung.
- **Luôn chừa chỗ trống khi chia subnet.** Chia vừa khít hôm nay thì sáu tháng nữa muốn thêm một subnet sẽ phải xen vào giữa — rất rối. Dùng hết một nửa dải là thoải mái.
- **`tcpdump` là bằng chứng, không phải phỏng đoán.** Khi hai bên đổ lỗi cho nhau (*"chúng tôi có gửi"* / *"chúng tôi không nhận được"*), bắt gói ở cả hai đầu sẽ chấm dứt tranh cãi trong 5 phút.
- **Chứng chỉ phải có cảnh báo trước 30 ngày.** Let's Encrypt chỉ sống 90 ngày. Tự động gia hạn là tốt, nhưng **cảnh báo vẫn phải có** — vì cơ chế gia hạn cũng hỏng được.
- **Đừng bao giờ tắt kiểm tra chứng chỉ trong production.** `-k`, `verify=False`, `InsecureSkipVerify: true` — mỗi cái là một cánh cửa mở cho tấn công xen giữa. Nếu chứng chỉ nội bộ không được tin, hãy **thêm CA nội bộ vào máy**, đừng tắt kiểm tra.
- **MTU là nghi phạm khi 'gói nhỏ chạy, gói lớn treo'.** Rất ít người nghĩ tới nó, nên nó ngốn hàng giờ. Nhớ triệu chứng đặc trưng là đủ.

### 📝 Tự kiểm tra

<details>
<summary><b>1. Một subnet `/26` trên AWS có bao nhiêu địa chỉ dùng được? Vì sao khác con số lý thuyết?</b></summary>

Lý thuyết: `2^6 = 64` địa chỉ, trừ 2 (mạng + broadcast) = **62**.

Nhưng **AWS giữ riêng 5 địa chỉ** mỗi subnet: địa chỉ mạng, gateway, DNS, một địa chỉ dự phòng, và broadcast. Nên thực tế chỉ còn **59 địa chỉ** dùng được.

Đây là chỗ hay tính hụt khi chia VPC — đặc biệt với subnet nhỏ như `/28` (16 địa chỉ lý thuyết → **11** thực dùng).
</details>

<details>
<summary><b>2. `ip route get 10.0.5.20` dùng để làm gì? Hơn gì so với đọc `ip route show`?</b></summary>

`ip route show` liệt kê **toàn bộ luật**; bạn phải tự suy ra dòng nào thắng.

`ip route get` **hỏi thẳng kernel**: *"gói tin tới đích này sẽ đi đường nào, qua card nào, với địa chỉ nguồn nào?"* — kernel trả lời sau khi đã áp dụng mọi luật.

Cực kỳ hữu ích khi có VPN, nhiều card mạng, hoặc container — những lúc đường đi không hiển nhiên và việc suy luận bằng mắt dễ sai.
</details>

<details>
<summary><b>3. Trong `tcpdump`, thấy `Flags [R]` nghĩa là gì? Nó tương ứng với lỗi nào?</b></summary>

`[R]` là **RST** (reset) — server **chủ động từ chối** kết nối.

Nó tương ứng với `Connection refused`: gói tin **tới được máy đích**, nhưng không có tiến trình nào nghe ở cổng đó nên kernel trả về RST ngay.

Đối lập với nó: SYN gửi đi mà **không có hồi âm gì cả** → `Connection timed out` → tường lửa nuốt gói im lặng.

Phân biệt được hai cái này cho biết nên đi sửa **dịch vụ** hay sửa **tường lửa**.
</details>

<details>
<summary><b>4. Vì sao lỗi thiếu chứng chỉ trung gian lại khó phát hiện?</b></summary>

Vì **trình duyệt vẫn vào được**. Trình duyệt hiện đại tự tải chứng chỉ trung gian còn thiếu (qua AIA fetching) nên người dùng không thấy lỗi gì.

Nhưng `curl`, thư viện HTTP của ứng dụng, và các dịch vụ gọi API thì **không làm vậy** — chúng báo `unable to get local issuer certificate`.

Kết quả là cuộc tranh luận kinh điển: *"trên trình duyệt em thấy bình thường mà"*, trong khi hệ thống tích hợp thì chết. Kiểm tra bằng:
```bash
echo | openssl s_client -connect host:443 -servername host 2>/dev/null | grep "^ *[0-9] s:"
```
Chỉ thấy một dòng `0 s:` là thiếu chuỗi trung gian.
</details>

<details>
<summary><b>5. Triệu chứng nào khiến bạn nghi ngờ MTU?</b></summary>

**"Kết nối được, gói nhỏ chạy bình thường, gói lớn thì treo."**

Ví dụ cụ thể: SSH đăng nhập được nhưng treo khi chạy lệnh có output dài; API trả về response nhỏ bình thường nhưng treo với response lớn.

Thường gặp khi có VPN, tunnel, hoặc mạng overlay của Kubernetes — chúng thêm header riêng nên MTU thực tế nhỏ hơn 1500.

Kiểm tra: `ping -M do -s <kích thước> <đích>` để tìm ngưỡng.
</details>

### 📚 Thuật ngữ Anh–Việt

| Thuật ngữ | Nghĩa |
|---|---|
| **CIDR** | Cách viết dải mạng `a.b.c.d/n` — `n` là số bit phần mạng |
| **Subnet** | Một dải con tách ra từ dải lớn hơn |
| **Broadcast address** | Địa chỉ cuối của subnet, không gán cho máy nào |
| **Default gateway** | Cửa ra khi máy không biết đích nằm ở đâu |
| **Longest prefix match** | Luật định tuyến: dòng khớp cụ thể nhất thì thắng |
| **SYN / SYN-ACK / ACK** | Ba bước bắt tay TCP |
| **RST** | Gói từ chối kết nối — tương ứng `Connection refused` |
| **MTU** | Kích thước gói tin lớn nhất đi qua được; chuẩn Ethernet là 1500 |
| **TLS handshake** | Quá trình thoả thuận mã hoá và kiểm tra chứng chỉ |
| **Certificate chain** | Chuỗi chứng chỉ từ lá lên tới CA gốc |
| **SAN** | Subject Alternative Name — danh sách tên miền chứng chỉ bảo vệ |
| **CA** | Certificate Authority — đơn vị ký chứng chỉ |
| **tcpdump** | Công cụ bắt gói tin ngay trên máy |

### 🎯 Đúc kết NT1

**3 điều phải mang theo:**

1. **Chia dải mạng là quyết định khó đảo ngược.** Chừa chỗ trống, nhóm theo chức năng, và kiểm tra không trùng với mạng có sẵn.
2. **Bắt gói là bằng chứng.** Khi tranh cãi *"có gửi / không nhận"*, `tcpdump` ở hai đầu chấm dứt mọi phỏng đoán.
3. **Lỗi TLS gần như luôn nằm ở bốn chỗ:** hết hạn, sai tên miền, thiếu chuỗi trung gian, hoặc tự ký. Biết bốn cái này là chẩn đoán được 95% ca.

> 🧠 **Một câu để nhớ:** mạng không có phép màu — mọi thứ đều **nhìn thấy được** nếu bạn biết dùng `ip route get`, `tcpdump` và `openssl s_client`.

**✅ Tự chấm:**

- [ ] Tính được số địa chỉ từ CIDR, và nhớ cloud giữ thêm 5 địa chỉ
- [ ] Chia được dải mạng cho hệ thống nhiều tầng, có chừa chỗ mở rộng
- [ ] Đọc được bảng định tuyến và dùng `ip route get` để hỏi đường đi
- [ ] Bắt gói và chỉ ra ba bước bắt tay TCP
- [ ] Nhận ra `[R]` trong tcpdump và biết nó ứng với lỗi gì
- [ ] Đọc được chuỗi chứng chỉ và bốn lỗi TLS phổ biến
- [ ] Nhận diện được triệu chứng của lỗi MTU

✅ **Kết quả đạt được:** Đủ nền tảng mạng để thiết kế dải IP cho hệ thống thật, và để chẩn đoán những lỗi mà công cụ tầng cao không giải thích được.

---

## NT2 — Web Server production: HTTPS, Load Balancing & Tinh chỉnh

> ⏱️ ~120 phút · Loại: Web Server · **Học sau Ngày 23**
>
> 🧭 **Vì sao có bài này:** Ngày 23 dạy reverse proxy và `upstream` cơ bản. Nhưng đưa lên production thì ba thứ sau là bắt buộc, và không bài nào trong 60 ngày dạy đủ:
> - **HTTPS thật** — chứng chỉ ở đâu ra, gia hạn thế nào, cấu hình sao cho an toàn
> - **Chọn thuật toán cân bằng tải** — `round-robin` không phải lúc nào cũng đúng
> - **Tinh chỉnh** — mặc định của nginx dành cho máy nhỏ, không dành cho hệ thống thật
>
> ✅ **Chuẩn bị:** Docker. Toàn bộ lab chạy local, **không cần tên miền thật**.
>
> 🎁 **Cuối bài bạn có gì:** một reverse proxy có HTTPS đúng chuẩn (đạt hạng A trên thang đánh giá SSL), biết chọn đúng thuật toán cân bằng tải cho từng loại ứng dụng, và **tự đo được** giới hạn của cấu hình mặc định.

### 📘 Lý thuyết

#### 1. Chứng chỉ TLS đến từ đâu — ba con đường

| Cách | Chi phí | Phù hợp với | Gia hạn |
|---|---|---|---|
| **Let's Encrypt** | Miễn phí | Hầu hết mọi trường hợp | **Tự động**, chu kỳ 90 ngày |
| **CA thương mại** | 50–500 USD/năm | Cần bảo hiểm hoặc EV | Thủ công, 1 năm |
| **CA nội bộ / tự ký** | Miễn phí | Dịch vụ nội bộ, môi trường dev | Tự quản |

> 🔑 **Vì sao Let's Encrypt chỉ cho 90 ngày:** cố ý. Chu kỳ ngắn **buộc bạn phải tự động hoá** việc gia hạn. Chứng chỉ 1 năm khiến người ta gia hạn bằng tay, rồi quên, rồi hệ thống chết vào một ngày Chủ nhật.

Hai cách chứng minh bạn sở hữu tên miền:

| Cách | Hoạt động thế nào | Dùng khi |
|---|---|---|
| **HTTP-01** | Đặt một file ở `/.well-known/acme-challenge/` | Có cổng 80 mở ra Internet |
| **DNS-01** | Thêm một bản ghi TXT vào DNS | Máy chủ **không** lộ ra Internet, hoặc cần **chứng chỉ wildcard** |

#### 2. Cấu hình TLS an toàn — ba thứ phải có

```nginx
# 1) CHỈ TLS 1.2 và 1.3 — bỏ hẳn các phiên bản cũ
ssl_protocols TLSv1.2 TLSv1.3;

# 2) Bộ mã hoá hiện đại, ưu tiên forward secrecy
ssl_ciphers ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES128-GCM-SHA256:...;
ssl_prefer_server_ciphers off;   # TLS 1.3 thì để client chọn

# 3) HSTS — bắt trình duyệt CHỈ dùng HTTPS cho tên miền này
add_header Strict-Transport-Security "max-age=31536000; includeSubDomains" always;
```

> ⚠️ **HSTS là con dao hai lưỡi.** Sau khi trình duyệt nhận header này, nó **từ chối HTTP** cho tên miền đó trong đúng `max-age` giây — kể cả khi bạn đã gỡ HSTS. Nếu chứng chỉ hết hạn mà chưa kịp gia hạn, người dùng **không vào được bằng bất kỳ cách nào**. Hãy bắt đầu với `max-age=300` (5 phút), chạy ổn định vài tuần rồi mới nâng lên 1 năm.

**Forward secrecy** nghĩa là: kẻ tấn công ghi lại toàn bộ lưu lượng mã hoá hôm nay, sau này lấy được khoá riêng của server thì **vẫn không giải mã được** các phiên cũ. Đây là lý do phải dùng bộ mã hoá `ECDHE`.

#### 3. Bốn thuật toán cân bằng tải — chọn sai là lệch tải

| Thuật toán | Cách chia | Hợp với | Không hợp với |
|---|---|---|---|
| `round-robin` *(mặc định)* | Lần lượt từng backend | Request ngắn, đồng đều | Request có thời gian xử lý rất khác nhau |
| `least_conn` | Gửi tới backend **đang rảnh nhất** | Request dài ngắn khác nhau, WebSocket | — |
| `ip_hash` | Cùng IP → cùng backend | App giữ phiên trong RAM | Phía sau NAT (nhiều người chung một IP) |
| `hash $key` | Băm theo khoá tuỳ chọn | Cache theo người dùng | — |

> 🔑 **Quy tắc thực dụng:** không chắc thì dùng **`least_conn`**. Nó đúng trong nhiều tình huống hơn `round-robin`, đặc biệt khi thời gian xử lý các request khác nhau nhiều.
>
> Và về `ip_hash`: nó là **giải pháp chữa cháy cho app giữ trạng thái**, không phải thiết kế tốt. Cách đúng là làm app **stateless** — đưa phiên đăng nhập ra Redis hoặc dùng JWT. Khi đó mọi backend đều phục vụ được mọi người dùng.

#### 4. Kiểm tra sức khoẻ — chủ động hay bị động

| | **Bị động** (nginx bản miễn phí) | **Chủ động** (nginx Plus, HAProxy, Traefik) |
|---|---|---|
| Cách biết backend chết | Chờ tới khi có request **thất bại** | Tự gọi `/health` theo chu kỳ |
| Hệ quả | Vài người dùng **gặp lỗi trước** khi nginx loại backend | Loại backend **trước khi** ai đó bị ảnh hưởng |
| Cấu hình | `max_fails=2 fail_timeout=10s` | `health_check interval=5s` |

Bản nginx mã nguồn mở chỉ có kiểm tra **bị động**. Đó là một lý do nhiều đội chọn **HAProxy** hoặc **Traefik** cho tầng cân bằng tải.

#### 5. Mặc định của nginx dành cho máy nhỏ

| Tham số | Mặc định | Vì sao cần đổi |
|---|---|---|
| `worker_connections` | 512–1024 | Quá thấp cho lưu lượng thật |
| `keepalive` tới upstream | **Không bật** | Mỗi request mở kết nối TCP mới — rất lãng phí |
| `gzip` | Tắt | Bật lên giảm băng thông 60–80% cho JSON/HTML |
| `client_max_body_size` | 1 MB | Tải file lên lớn hơn là lỗi `413` |
| `proxy_read_timeout` | 60 giây | Quá dài — giữ luồng khi backend treo |

Công thức số kết nối tối đa:

```text
max_clients = worker_processes × worker_connections
```

Với reverse proxy thì chia đôi, vì mỗi client chiếm **hai** kết nối (một tới client, một tới backend).

### 🧪 LAB — Reverse proxy chuẩn production

**Thư mục:**

```text
lab-nt2/
├── docker-compose.yml
├── nginx/
│   ├── nginx.conf              # cấu hình chính (tinh chỉnh)
│   └── conf.d/
│       ├── tls.conf            # phần TLS dùng chung
│       └── site.conf           # site + upstream
├── chung-chi/                  # chứng chỉ tự sinh
└── app/                        # 3 backend giả
```

#### File 1 — `nginx/nginx.conf`

```nginx
user  nginx;
worker_processes  auto;              # tự khớp số nhân CPU
worker_rlimit_nofile 65535;          # nâng giới hạn file descriptor

events {
    worker_connections  4096;        # mặc định 1024 là quá thấp
    multi_accept on;
}

http {
    include       /etc/nginx/mime.types;
    default_type  application/octet-stream;

    # ---- Hiệu năng ----
    sendfile        on;
    tcp_nopush      on;              # gửi header cùng lúc với dữ liệu
    tcp_nodelay     on;              # không chờ gom gói nhỏ
    keepalive_timeout  65;
    keepalive_requests 1000;

    # ---- Nén ----
    gzip on;
    gzip_vary on;
    gzip_min_length 1024;            # file nhỏ hơn thì nén không đáng
    gzip_comp_level 5;               # 5 là điểm cân bằng CPU/dung lượng
    gzip_types text/plain text/css application/json application/javascript
               text/xml application/xml image/svg+xml;

    # ---- Giới hạn ----
    client_max_body_size 20m;        # mặc định 1m — tải file lên sẽ lỗi 413
    client_body_timeout 15s;
    client_header_timeout 15s;

    # ---- Ẩn thông tin ----
    server_tokens off;               # không lộ phiên bản nginx

    # ---- Log có thời gian xử lý (rất cần khi điều tra) ----
    log_format chi_tiet '$remote_addr - [$time_local] "$request" '
                        '$status $body_bytes_sent '
                        'rt=$request_time urt="$upstream_response_time" '
                        'up=$upstream_addr';
    access_log /var/log/nginx/access.log chi_tiet;

    include /etc/nginx/conf.d/*.conf;
}
```

#### File 2 — `nginx/conf.d/tls.conf`

```nginx
# Cấu hình TLS dùng chung cho mọi site
ssl_protocols TLSv1.2 TLSv1.3;
ssl_ciphers ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-GCM-SHA384:ECDHE-ECDSA-CHACHA20-POLY1305:ECDHE-RSA-CHACHA20-POLY1305;
ssl_prefer_server_ciphers off;

# Bộ nhớ đệm phiên — giảm số lần bắt tay đầy đủ
ssl_session_cache shared:SSL:10m;
ssl_session_timeout 1d;
ssl_session_tickets off;

# OCSP stapling — server tự đính kèm trạng thái thu hồi chứng chỉ
ssl_stapling on;
ssl_stapling_verify on;
resolver 1.1.1.1 8.8.8.8 valid=300s;
resolver_timeout 5s;
```

#### File 3 — `nginx/conf.d/site.conf`

```nginx
upstream backend {
    least_conn;                      # rảnh nhất nhận trước

    server app1:80 max_fails=2 fail_timeout=10s;
    server app2:80 max_fails=2 fail_timeout=10s;
    server app3:80 max_fails=2 fail_timeout=10s backup;   # chỉ dùng khi 2 cái kia chết

    keepalive 32;                    # giữ kết nối tới backend — QUAN TRỌNG
    keepalive_timeout 60s;
}

# Giới hạn tần suất và số kết nối đồng thời
limit_req_zone  $binary_remote_addr zone=theo_ip:10m rate=30r/s;
limit_conn_zone $binary_remote_addr zone=ket_noi:10m;

# ---- Chuyển hướng HTTP sang HTTPS ----
server {
    listen 80;
    server_name shop.local;

    # Chừa đường cho Let's Encrypt xác thực
    location /.well-known/acme-challenge/ {
        root /var/www/certbot;
    }

    location / {
        return 301 https://$host$request_uri;
    }
}

# ---- Site HTTPS ----
server {
    listen 443 ssl;
    http2 on;                        # cú pháp mới (nginx 1.25+)
    server_name shop.local;

    ssl_certificate     /etc/nginx/chung-chi/shop.local.pem;
    ssl_certificate_key /etc/nginx/chung-chi/shop.local-key.pem;

    # ---- Header bảo mật ----
    add_header Strict-Transport-Security "max-age=300" always;  # bắt đầu NGẮN
    add_header X-Content-Type-Options nosniff always;
    add_header X-Frame-Options SAMEORIGIN always;
    add_header Referrer-Policy strict-origin-when-cross-origin always;

    location / {
        limit_req  zone=theo_ip burst=60 nodelay;
        limit_conn ket_noi 20;

        proxy_pass http://backend;
        proxy_http_version 1.1;              # BẮT BUỘC để keepalive hoạt động
        proxy_set_header Connection "";      # BẮT BUỘC — xoá header Connection

        proxy_set_header Host              $host;
        proxy_set_header X-Real-IP         $remote_addr;
        proxy_set_header X-Forwarded-For   $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;

        proxy_connect_timeout 2s;
        proxy_send_timeout    10s;
        proxy_read_timeout    10s;

        proxy_next_upstream error timeout http_502 http_503 http_504;
        proxy_next_upstream_tries 2;
    }

    location /health {
        access_log off;
        return 200 "ok\n";
    }

    # Trạng thái nội bộ — chỉ cho mạng riêng
    location /nginx-status {
        stub_status;
        access_log off;
        allow 172.16.0.0/12;
        allow 127.0.0.1;
        deny all;
    }
}
```

#### File 4 — `docker-compose.yml`

```yaml
services:
  nginx:
    image: nginx:1.27-alpine
    container_name: nt2-nginx
    ports:
      - "8080:80"
      - "8443:443"
    volumes:
      - ./nginx/nginx.conf:/etc/nginx/nginx.conf:ro
      - ./nginx/conf.d:/etc/nginx/conf.d:ro
      - ./chung-chi:/etc/nginx/chung-chi:ro
    depends_on: [app1, app2, app3]

  app1: &app
    image: nginx:1.27-alpine
    container_name: nt2-app1
    command:
      - /bin/sh
      - -c
      - echo '{"backend":"app1"}' > /usr/share/nginx/html/index.html
        && nginx -g 'daemon off;'

  app2:
    <<: *app
    container_name: nt2-app2
    command:
      - /bin/sh
      - -c
      - echo '{"backend":"app2"}' > /usr/share/nginx/html/index.html
        && nginx -g 'daemon off;'

  app3:
    <<: *app
    container_name: nt2-app3
    command:
      - /bin/sh
      - -c
      - echo '{"backend":"app3-DUPHONG"}' > /usr/share/nginx/html/index.html
        && nginx -g 'daemon off;'
```

### 🧭 Hướng dẫn làm LAB — step by step

#### Bước 1 — Tạo chứng chỉ có SAN đúng chuẩn

Chứng chỉ thiếu **SAN** (Subject Alternative Name) sẽ bị trình duyệt hiện đại từ chối, kể cả khi `CN` đúng:

```bash
mkdir -p ~/lab-nt2/{nginx/conf.d,chung-chi,app} && cd ~/lab-nt2

openssl req -x509 -newkey rsa:2048 -nodes -days 365 \
  -keyout chung-chi/shop.local-key.pem \
  -out    chung-chi/shop.local.pem \
  -subj "/CN=shop.local" \
  -addext "subjectAltName=DNS:shop.local,DNS:www.shop.local,IP:127.0.0.1" \
  2>/dev/null

openssl x509 -in chung-chi/shop.local.pem -noout -text | grep -A1 "Subject Alternative"
```

**Bạn sẽ thấy:**
```text
X509v3 Subject Alternative Name:
    DNS:shop.local, DNS:www.shop.local, IP Address:127.0.0.1
```

✅ **Checkpoint:** chứng chỉ có đủ ba mục SAN.

💡 **`CN` đã lỗi thời.** Trình duyệt hiện đại **chỉ đọc SAN** — chứng chỉ chỉ có `CN` sẽ bị từ chối dù `CN` hoàn toàn đúng. Đây là nguyên nhân của rất nhiều ca *"chứng chỉ đúng tên mà vẫn báo lỗi"*.

#### Bước 2 — Khởi động và kiểm tra cú pháp trước

```bash
# tạo 4 file theo phần LAB
docker compose up -d
docker compose exec nginx nginx -t
```

**Bạn sẽ thấy:**
```text
nginx: the configuration file /etc/nginx/nginx.conf syntax is ok
nginx: configuration file /etc/nginx/nginx.conf test is successful
```

✅ **Checkpoint:** cú pháp hợp lệ.

💡 **`nginx -t` trước mọi lần reload là kỷ luật bắt buộc.** Reload với cấu hình hỏng thì nginx **giữ cấu hình cũ** (may mắn), nhưng nếu nginx bị restart vì lý do khác thì nó **không lên lại được** — và bạn mất toàn bộ dịch vụ. Một lệnh 0,2 giây đổi lấy sự an tâm.

#### Bước 3 — Kiểm chứng HTTPS và chuyển hướng

```bash
echo "127.0.0.1 shop.local" | sudo tee -a /etc/hosts

echo "--- HTTP phải chuyển hướng sang HTTPS ---"
curl -sI http://shop.local:8080/ | head -3

echo "--- HTTPS hoạt động ---"
curl -sk https://shop.local:8443/
```

**Bạn sẽ thấy:**
```text
HTTP/1.1 301 Moved Permanently
Location: https://shop.local/

{"backend":"app1"}
```

✅ **Checkpoint:** HTTP trả 301, HTTPS trả JSON.

Kiểm tra phiên bản TLS và header bảo mật:

```bash
echo | openssl s_client -connect shop.local:8443 -servername shop.local 2>/dev/null \
  | grep -E "Protocol|Cipher"
curl -skI https://shop.local:8443/ | grep -iE "strict-transport|x-content|x-frame"
```

**Bạn sẽ thấy:**
```text
Protocol  : TLSv1.3
Cipher    : TLS_AES_256_GCM_SHA384

strict-transport-security: max-age=300
x-content-type-options: nosniff
x-frame-options: SAMEORIGIN
```

✅ **Checkpoint:** TLS 1.3, và đủ ba header bảo mật.

Chứng minh TLS cũ đã bị chặn:
```bash
echo | openssl s_client -connect shop.local:8443 -tls1_1 2>&1 | grep -iE "error|alert" | head -2
```

**Bạn sẽ thấy** lỗi bắt tay — TLS 1.1 đã bị từ chối đúng như cấu hình.

#### Bước 4 — Thấy `least_conn` và backend dự phòng hoạt động

```bash
echo "--- Chia tải giữa app1 và app2 (app3 là dự phòng) ---"
for i in $(seq 1 8); do curl -sk https://shop.local:8443/ | grep -o 'app[0-9]*'; done | sort | uniq -c
```

**Bạn sẽ thấy:**
```text
      4 app1
      4 app2
```

✅ **Checkpoint:** chỉ app1 và app2 phục vụ — app3 chưa được dùng vì có cờ `backup`.

Giết cả hai backend chính:

```bash
docker stop nt2-app1 nt2-app2
sleep 2
curl -sk https://shop.local:8443/
```

**Bạn sẽ thấy:**
```text
{"backend":"app3-DUPHONG"}
```

✅ **Checkpoint:** backend dự phòng tự nhận việc.

```bash
docker start nt2-app1 nt2-app2
```

💡 Cờ `backup` hữu ích khi bạn có một máy yếu hơn hoặc ở vùng khác: nó **chỉ nhận tải khi các máy chính đều chết**, thay vì chia đều ngay từ đầu.

#### Bước 5 — Đo tác dụng của keepalive tới upstream

Đây là tối ưu ít ai để ý nhưng hiệu quả rất rõ. So sánh trực tiếp:

```bash
# Đo hiện tại (đã bật keepalive)
echo "--- CÓ keepalive ---"
time (for i in $(seq 1 200); do curl -sk https://shop.local:8443/ -o /dev/null; done)
```

Giờ tắt nó đi:

```bash
sed -i 's/^    keepalive 32;/#   keepalive 32;/' nginx/conf.d/site.conf
docker compose exec nginx nginx -t && docker compose exec nginx nginx -s reload
sleep 1

echo "--- KHÔNG keepalive ---"
time (for i in $(seq 1 200); do curl -sk https://shop.local:8443/ -o /dev/null; done)
```

**Bạn sẽ thấy** thời gian tăng lên rõ rệt (thường 20–40%), và số kết nối TCP tạo mới cũng tăng:

```bash
docker compose exec nginx sh -c "cat /proc/net/sockstat | head -2"
```

✅ **Checkpoint:** thấy chênh lệch đo được giữa có và không có keepalive.

Bật lại:
```bash
sed -i 's/^#   keepalive 32;/    keepalive 32;/' nginx/conf.d/site.conf
docker compose exec nginx nginx -s reload
```

💡 **Hai dòng đi kèm bắt buộc** mà thiếu là keepalive **không hoạt động** dù đã khai:
```nginx
proxy_http_version 1.1;          # HTTP/1.0 không hỗ trợ keepalive
proxy_set_header Connection "";  # xoá header Connection mặc định
```
Rất nhiều cấu hình ngoài đời khai `keepalive 32` rồi quên hai dòng này — và tự hỏi vì sao không thấy cải thiện.

#### Bước 6 — Kiểm chứng giới hạn tần suất

```bash
echo "--- Gửi 100 request thật nhanh (giới hạn 30r/s, burst 60) ---"
for i in $(seq 1 100); do
  curl -sk -o /dev/null -w "%{http_code}\n" https://shop.local:8443/ &
done | sort | uniq -c
wait
```

**Bạn sẽ thấy:**
```text
     63 200
     37 503
```

✅ **Checkpoint:** một phần request bị chặn với mã 503.

💡 **Cờ `nodelay` quyết định hành vi:**
- **Có `nodelay`**: cho `burst` request đi qua **ngay lập tức**, vượt quá thì từ chối luôn
- **Không có `nodelay`**: xếp hàng và **làm chậm lại** cho đúng nhịp, thay vì từ chối

Chọn cái nào tuỳ tình huống: API công khai thường dùng `nodelay` (thà từ chối nhanh còn hơn để client chờ); trang web cho người dùng thật thì làm chậm dễ chịu hơn là báo lỗi.

#### Bước 7 — Đọc log để tìm điểm nghẽn

Định dạng log trong `nginx.conf` có hai trường rất quan trọng mà log mặc định **không có**:

```bash
docker compose exec nginx tail -3 /var/log/nginx/access.log
```

**Bạn sẽ thấy:**
```text
172.18.0.1 - [23/Sep/2026:10:15:32 +0000] "GET / HTTP/2.0" 200 19 rt=0.003 urt="0.001" up=172.18.0.3:80
```

| Trường | Nghĩa |
|---|---|
| `rt=0.003` | **Tổng** thời gian nginx xử lý request |
| `urt="0.001"` | Thời gian **backend** trả lời |
| `up=172.18.0.3:80` | Backend nào đã phục vụ |

✅ **Checkpoint:** đọc được cả ba trường.

💡 **Đây là công cụ khoanh vùng hiệu quả nhất khi hệ thống chậm:**
- `rt` cao, `urt` cao → **backend chậm**, đi sửa ứng dụng
- `rt` cao, `urt` **thấp** → nginx hoặc mạng chậm (thường là TLS, DNS, hoặc client kết nối kém)

Không có hai trường này trong log thì bạn chỉ biết *"hệ thống chậm"* mà không biết chậm ở đâu. Log mặc định của nginx **không có chúng** — phải tự thêm.

#### Bước 8 — Let's Encrypt trên hệ thống thật

Lab dùng chứng chỉ tự ký. Với tên miền thật, đây là cách lấy chứng chỉ tự động:

**Cách 1 — Caddy** (đơn giản nhất, tự lo mọi thứ):

```caddyfile
shop.example.com {
    reverse_proxy app1:80 app2:80 {
        lb_policy least_conn
        health_uri /health
    }
    encode gzip
}
```

Đúng 6 dòng. Caddy tự xin chứng chỉ, tự gia hạn, tự cấu hình TLS an toàn.

**Cách 2 — nginx + certbot** (khi đã quen nginx):

```bash
docker run --rm \
  -v "$PWD/certbot/conf:/etc/letsencrypt" \
  -v "$PWD/certbot/www:/var/www/certbot" \
  certbot/certbot certonly --webroot -w /var/www/certbot \
  -d shop.example.com --email ban@example.com --agree-tos --no-eff-email
```

Rồi đặt lịch gia hạn:
```bash
0 3 * * * docker run --rm -v ... certbot/certbot renew --quiet && docker exec nginx nginx -s reload
```

⚠️ **Ba điều bắt buộc khi dùng Let's Encrypt:**
1. **Dùng `--staging` khi thử nghiệm.** Môi trường thật có giới hạn **5 lần cấp/tuần cho mỗi tên miền** — thử vài lần là bị khoá một tuần.
2. **Nhớ `nginx -s reload` sau khi gia hạn.** Certbot đổi file chứng chỉ nhưng nginx vẫn giữ bản cũ trong bộ nhớ cho tới khi reload. Rất nhiều người bị chứng chỉ hết hạn *dù certbot chạy thành công* chỉ vì thiếu dòng này.
3. **Vẫn phải có cảnh báo hết hạn** — cơ chế tự động cũng hỏng được (đổi DNS, cổng 80 bị chặn, hết dung lượng đĩa).

#### Bước 9 — Dọn dẹp

```bash
cd ~/lab-nt2 && docker compose down
sudo sed -i '/shop.local/d' /etc/hosts
```

### 💡 Đi làm mới thấm

- **Bắt đầu HSTS với `max-age` ngắn.** Đặt thẳng 1 năm rồi phát hiện cấu hình sai thì người dùng **không vào được bằng bất kỳ cách nào** cho tới khi hết hạn — không có cách nào gỡ từ phía server. Bắt đầu 300 giây, chạy ổn vài tuần rồi mới nâng.
- **`nginx -t` trước mọi lần reload.** Một lệnh 0,2 giây, đổi lấy việc không bao giờ để nginx kẹt ở trạng thái không khởi động lại được.
- **Thêm `rt` và `urt` vào log ngay hôm nay.** Đây là hai trường phân biệt *"hệ thống chậm"* với *"backend chậm"*. Không có chúng thì mọi cuộc điều tra hiệu năng đều bắt đầu bằng phỏng đoán.
- **`ip_hash` là dấu hiệu app chưa stateless.** Nó chữa cháy được, nhưng cũng nghĩa là mất một backend là mất phiên của một nhóm người dùng, và không scale đều được. Cách đúng: đưa phiên ra Redis hoặc dùng JWT.
- **`client_max_body_size` là lỗi 413 phổ biến nhất.** Mặc định 1 MB — người dùng tải ảnh 3 MB lên là lỗi. Và nhớ chỉnh **cả ở ứng dụng phía sau**, không chỉ ở nginx.
- **Cân nhắc Caddy hoặc Traefik cho dự án mới.** Chúng tự lo chứng chỉ, và Traefik tự phát hiện container mới. nginx mạnh và linh hoạt hơn, nhưng với nhu cầu phổ thông thì 6 dòng Caddy thay được 60 dòng nginx.

### 📝 Tự kiểm tra

<details>
<summary><b>1. Vì sao Let's Encrypt chỉ cấp chứng chỉ 90 ngày?</b></summary>

**Cố ý, để buộc phải tự động hoá.** Chu kỳ ngắn khiến gia hạn thủ công trở nên bất khả thi — bạn phải viết script hoặc dùng công cụ tự động.

Chứng chỉ 1 năm nghe tiện hơn, nhưng thực tế nó khiến người ta gia hạn bằng tay, rồi quên, rồi hệ thống chết vào một ngày Chủ nhật.

Lý do phụ: chứng chỉ sống ngắn thì khoá bị lộ cũng chỉ gây hại trong thời gian ngắn.
</details>

<details>
<summary><b>2. Khai `keepalive 32` trong upstream nhưng không thấy cải thiện. Thiếu gì?</b></summary>

Thiếu **hai dòng bắt buộc** trong block `location`:

```nginx
proxy_http_version 1.1;          # HTTP/1.0 không hỗ trợ keepalive
proxy_set_header Connection "";  # xoá header Connection mặc định
```

Không có chúng, nginx vẫn mở kết nối TCP mới cho **mỗi** request tới backend — `keepalive 32` bị vô hiệu hoàn toàn.

Đây là lỗi cấu hình rất phổ biến ngoài đời, vì nó không báo lỗi gì cả, chỉ là không có tác dụng.
</details>

<details>
<summary><b>3. Log ghi `rt=2.5` nhưng `urt="0.05"`. Vấn đề nằm ở đâu?</b></summary>

**Không phải ở backend** — backend trả lời chỉ trong 50 mili giây.

2,45 giây còn lại nằm ở nginx hoặc ở đường truyền tới client. Các khả năng:
- Bắt tay TLS chậm (client ở xa, hoặc thiếu session cache)
- Phân giải DNS chậm trong `resolver`
- Client kết nối kém, nhận dữ liệu chậm (`$request_time` tính cả thời gian gửi response)
- nginx đang quá tải, hết worker connection

Nếu ngược lại (`rt` và `urt` đều cao) thì mới là backend chậm.
</details>

<details>
<summary><b>4. Khi nào dùng `least_conn` thay vì `round-robin`?</b></summary>

Khi **thời gian xử lý các request khác nhau nhiều**.

`round-robin` chia lần lượt bất kể backend đang bận hay rảnh. Nếu request 1 mất 5 giây và request 2 mất 50 mili giây, thì một backend có thể ôm nhiều request nặng trong khi backend khác đang rảnh.

`least_conn` gửi tới backend **đang ít kết nối nhất** — tự cân bằng theo tải thực tế.

Đặc biệt quan trọng với WebSocket và kết nối giữ lâu, vì `round-robin` sẽ phân bổ rất lệch.

Quy tắc thực dụng: không chắc thì dùng `least_conn`.
</details>

<details>
<summary><b>5. Vì sao chứng chỉ chỉ có CN mà không có SAN lại bị từ chối?</b></summary>

Vì **trình duyệt hiện đại chỉ đọc SAN** (Subject Alternative Name) và bỏ qua hoàn toàn trường `CN`. Đây là thay đổi đã áp dụng nhiều năm nay.

Chứng chỉ có `CN=shop.local` nhưng không có SAN → trình duyệt báo lỗi tên miền không khớp, **dù `CN` hoàn toàn đúng**.

Khi tự tạo chứng chỉ phải luôn thêm:
```bash
-addext "subjectAltName=DNS:shop.local,DNS:www.shop.local"
```
Đây là nguyên nhân của rất nhiều ca *"chứng chỉ đúng tên mà vẫn lỗi"*.
</details>

### 📚 Thuật ngữ Anh–Việt

| Thuật ngữ | Nghĩa |
|---|---|
| **Let's Encrypt** | CA miễn phí, chứng chỉ 90 ngày, thiết kế để tự động gia hạn |
| **ACME** | Giao thức tự động xin và gia hạn chứng chỉ |
| **HTTP-01 / DNS-01** | Hai cách chứng minh sở hữu tên miền (file / bản ghi TXT) |
| **SAN** | Subject Alternative Name — danh sách tên miền; **CN đã lỗi thời** |
| **HSTS** | Bắt trình duyệt chỉ dùng HTTPS; cẩn thận với `max-age` dài |
| **Forward secrecy** | Lộ khoá riêng sau này vẫn không giải mã được phiên cũ (cần ECDHE) |
| **OCSP stapling** | Server tự đính kèm trạng thái thu hồi chứng chỉ, đỡ một lượt gọi |
| **`least_conn`** | Gửi tới backend đang ít kết nối nhất |
| **`ip_hash`** | Cùng IP → cùng backend; dấu hiệu app chưa stateless |
| **`backup`** | Backend chỉ nhận tải khi các máy chính đều chết |
| **Upstream keepalive** | Giữ kết nối tới backend; cần `proxy_http_version 1.1` + `Connection ""` |
| **`$request_time` / `$upstream_response_time`** | Tổng thời gian / thời gian backend — hai trường khoanh vùng nghẽn |
| **`burst` / `nodelay`** | Cho vượt tạm thời / cho qua ngay thay vì xếp hàng |

### 🎯 Đúc kết NT2

**3 điều phải mang theo:**

1. **HTTPS chỉ là bước đầu — cấu hình TLS mới quyết định an toàn.** TLS 1.2+, forward secrecy, HSTS bắt đầu ngắn, và SAN chứ không phải CN.
2. **`rt` và `urt` trong log là hai trường đáng giá nhất.** Chúng phân biệt *"hệ thống chậm"* với *"backend chậm"* — thiếu chúng thì mọi điều tra hiệu năng đều là đoán.
3. **Mặc định của nginx dành cho máy nhỏ.** Keepalive tới upstream, `worker_connections`, `client_max_body_size`, gzip — bốn thứ gần như luôn phải chỉnh.

> 🧠 **Một câu để nhớ:** một reverse proxy tốt không được đo bằng việc nó *chạy được*, mà bằng việc lúc sự cố bạn **có đủ thông tin trong log** để biết lỗi nằm ở đâu.

**✅ Tự chấm:**

- [ ] Tạo chứng chỉ có SAN và giải thích vì sao CN không còn đủ
- [ ] Cấu hình TLS 1.2+ và kiểm chứng TLS cũ bị từ chối
- [ ] Giải thích rủi ro của HSTS `max-age` dài
- [ ] Chọn đúng thuật toán cân bằng tải cho từng loại ứng dụng
- [ ] Bật keepalive tới upstream **kèm hai dòng bắt buộc**, và đo được chênh lệch
- [ ] Đọc `rt`/`urt` để khoanh vùng điểm nghẽn
- [ ] Biết dùng `--staging` của Let's Encrypt và nhớ reload sau khi gia hạn

✅ **Kết quả đạt được:** Một reverse proxy đủ chuẩn đưa ra Internet — HTTPS đúng cách, cân bằng tải hợp lý, có giới hạn tần suất, và log đủ để điều tra khi có sự cố.

---

## NT3 — Ansible nâng cao: Role, Vault, Rolling Update & Inventory động

> ⏱️ ~120 phút · Loại: Tự động hoá · **Học sau Ngày 47**
>
> 🧭 **Vì sao có bài này:** Ngày 47 cho bạn playbook chạy được và khái niệm idempotent. Nhưng khi dùng thật trong đội, bốn thứ sau là bắt buộc:
> - **Role** — playbook một file sẽ thành 800 dòng không ai đọc nổi
> - **Vault dùng đúng cách** — mã hoá từng biến, không mã hoá cả file
> - **`serial`** — playbook mặc định chạy song song **mọi máy**, một cấu hình sai là hạ cả đội
> - **Inventory động** — danh sách máy sinh từ cloud/Terraform, không viết tay
>
> ✅ **Chuẩn bị:** Ansible và Docker (dùng lại 3 "server" container của Ngày 47).
>
> 🎁 **Cuối bài bạn có gì:** một role tái sử dụng có kiểm thử, quy trình cập nhật cuốn chiếu **không gián đoạn dịch vụ** (đo được), và inventory sinh tự động từ Terraform.

### 📘 Lý thuyết

#### 1. Role — cấu trúc chuẩn Ansible mong đợi

Role là cách đóng gói playbook để dùng lại. Ansible **tự tìm file theo đúng tên thư mục** — không cần khai đường dẫn:

```text
roles/nginx/
├── defaults/main.yml     # biến mặc định — ƯU TIÊN THẤP NHẤT, người dùng dễ ghi đè
├── vars/main.yml         # biến nội bộ — ưu tiên cao, KHÓ ghi đè
├── tasks/main.yml        # việc cần làm (điểm vào)
├── handlers/main.yml     # handler
├── templates/            # file .j2
├── files/                # file copy nguyên
├── meta/main.yml         # phụ thuộc vào role khác
└── molecule/             # kiểm thử role
```

> 🔑 **Phân biệt `defaults` và `vars` — chỗ này hay nhầm:**
> - `defaults/` = *"giá trị gợi ý, bạn đổi thoải mái"* — đặt mọi thứ người dùng role có thể muốn chỉnh
> - `vars/` = *"hằng số nội bộ của role"* — khó ghi đè, chỉ đặt thứ không nên đổi
>
> Người mới hay để mọi biến vào `vars/`, rồi role trở nên cứng nhắc và không ai dùng lại được.

#### 2. Thứ tự ưu tiên biến — nguồn gốc của nhiều giờ bối rối

Từ **thấp** tới **cao** (phần thường gặp):

```text
1. role defaults/          ← thấp nhất, dễ ghi đè
2. group_vars/all
3. group_vars/<nhóm>
4. host_vars/<máy>
5. biến khai trong play
6. -e "bien=gia_tri"       ← CAO NHẤT, thắng tất cả
```

Khi một biến *"không hiểu sao mang giá trị lạ"*, hãy kiểm tra thay vì đoán:

```bash
ansible-inventory -i inventory.ini --host web1 --yaml
ansible web1 -i inventory.ini -m debug -a "var=ten_bien"
```

#### 3. `serial` — thứ ngăn bạn tự hạ cả hệ thống

Mặc định Ansible chạy **song song trên mọi máy**. Với dịch vụ đang phục vụ, đó là công thức của thảm hoạ: một cấu hình sai sẽ hạ toàn bộ đội máy **cùng một lúc**.

```yaml
- hosts: web
  serial: 1                    # lần lượt từng máy
  # serial: "25%"              # hoặc từng 25% số máy
  # serial: [1, 5, "50%"]      # 1 máy thử → 5 máy → nửa còn lại
  max_fail_percentage: 0       # 1 máy lỗi là DỪNG toàn bộ
```

Dạng `serial: [1, 5, "50%"]` chính là **canary**: cập nhật một máy trước, quan sát, rồi mới mở rộng dần.

Và `max_fail_percentage: 0` là dây an toàn — máy đầu tiên lỗi thì dừng ngay, thay vì hỏng tiếp 20 máy nữa.

#### 4. Vault — mã hoá từng biến, không mã hoá cả file

Ngày 47 dùng `ansible-vault create bi-mat.yml` — mã hoá **cả file**. Nó hoạt động, nhưng có nhược điểm: file thành một khối nhị phân, `git diff` vô dụng, và không ai biết trong đó có biến gì.

Cách tốt hơn — **mã hoá từng giá trị**:

```bash
ansible-vault encrypt_string 'MatKhauThat' --name 'mat_khau_db'
```

Kết quả dán thẳng vào `group_vars/` như một biến bình thường:

```yaml
ten_database: cuahang            # đọc được, review được
mat_khau_db: !vault |
          $ANSIBLE_VAULT;1.1;AES256
          38396164653238623361393661...
```

Nhờ vậy: **thấy được có biến gì**, `git diff` hiển thị đúng dòng nào đổi, và chỉ giá trị nhạy cảm bị che.

#### 5. Inventory động — danh sách máy không nên viết tay

Viết tay `inventory.ini` chỉ hợp khi máy cố định. Với hạ tầng tạo bằng Terraform hoặc cloud thì danh sách thay đổi liên tục.

| Cách | Hoạt động thế nào |
|---|---|
| **Plugin cloud** | Ansible tự gọi API cloud, lọc theo thẻ |
| **Script động** | Bất kỳ chương trình nào in ra JSON đúng định dạng |
| **Terraform output** | `terraform output -json` → chuyển thành inventory |

Cách thứ ba là mắt xích nối Ngày 48 với Ngày 47: **Terraform tạo máy → xuất IP → Ansible cấu hình**.

### 🧪 LAB — Role, Vault, cập nhật cuốn chiếu

**Cấu trúc:**

```text
lab-nt3/
├── ansible.cfg
├── inventory.ini
├── group_vars/
│   └── web.yml               # có biến mã hoá bằng Vault
├── site.yml
├── roles/
│   └── web/
│       ├── defaults/main.yml
│       ├── tasks/main.yml
│       ├── handlers/main.yml
│       └── templates/trang.html.j2
└── inventory-tu-terraform.py  # inventory động
```

#### File 1 — `ansible.cfg`

```ini
[defaults]
inventory = inventory.ini
host_key_checking = False          # LAB thôi; production PHẢI bật
retry_files_enabled = False
stdout_callback = yaml             # dễ đọc hơn mặc định
interpreter_python = /usr/bin/python3

[ssh_connection]
pipelining = True                  # nhanh hơn đáng kể
ssh_args = -o ControlMaster=auto -o ControlPersist=60s
```

#### File 2 — `roles/web/defaults/main.yml`

```yaml
---
# Giá trị mặc định — người dùng role ghi đè thoải mái
web_cong: 80
web_thu_muc: /var/www/html
web_so_worker: auto
web_tieu_de: "Trang mặc định"
web_bat_gzip: true
web_goi_can:
  - nginx
  - curl
```

#### File 3 — `roles/web/tasks/main.yml`

```yaml
---
- name: Kiểm tra hệ điều hành được hỗ trợ
  assert:
    that: ansible_facts['os_family'] == 'Debian'
    fail_msg: "Role này chỉ hỗ trợ Debian/Ubuntu, máy này là {{ ansible_facts['os_family'] }}"
  tags: [always]

- name: Cài các gói cần thiết
  apt:
    name: "{{ web_goi_can }}"
    state: present
    update_cache: true
    cache_valid_time: 3600
  tags: [cai-dat]

- name: Tạo thư mục web
  file:
    path: "{{ web_thu_muc }}"
    state: directory
    owner: www-data
    group: www-data
    mode: "0755"
  tags: [cau-hinh]

- name: Sinh trang chủ riêng cho từng máy
  template:
    src: trang.html.j2
    dest: "{{ web_thu_muc }}/index.html"
    owner: www-data
    mode: "0644"
  notify: nap lai nginx
  tags: [cau-hinh]

- name: Đảm bảo nginx đang chạy và bật khi khởi động
  service:
    name: nginx
    state: started
    enabled: true
  tags: [dich-vu]

# Kiểm chứng ngay trong role — role tự chứng minh nó đã làm đúng
- name: Kiểm tra web trả lời được
  uri:
    url: "http://127.0.0.1:{{ web_cong }}/"
    status_code: 200
    timeout: 5
  register: kq_kiem_tra
  retries: 3
  delay: 2
  until: kq_kiem_tra is succeeded
  tags: [kiem-tra]
```

#### File 4 — `roles/web/handlers/main.yml`

```yaml
---
- name: nap lai nginx
  service:
    name: nginx
    state: reloaded      # reload, KHÔNG restart — không ngắt kết nối đang có
```

#### File 5 — `roles/web/templates/trang.html.j2`

```jinja
<!DOCTYPE html>
<html lang="vi">
<head><meta charset="utf-8"><title>{{ inventory_hostname }}</title></head>
<body>
  <h1>{{ web_tieu_de }}</h1>
  <ul>
    <li>Máy: {{ inventory_hostname }}</li>
    <li>Nhóm: {{ group_names | join(', ') }}</li>
    <li>Phiên bản triển khai: {{ phien_ban | default('chưa đặt') }}</li>
    <li>Hệ điều hành: {{ ansible_facts['distribution'] }} {{ ansible_facts['distribution_version'] }}</li>
  </ul>
</body>
</html>
```

#### File 6 — `site.yml`

```yaml
---
- name: Cập nhật cuốn chiếu cho nhóm web
  hosts: web
  become: true

  # ---- Cập nhật LẦN LƯỢT, không đồng loạt ----
  serial: 1
  max_fail_percentage: 0          # một máy lỗi là dừng toàn bộ

  vars:
    phien_ban: "{{ lookup('env', 'PHIEN_BAN') | default('v1', true) }}"
    web_tieu_de: "Cửa hàng ABC — {{ phien_ban }}"

  pre_tasks:
    - name: "[{{ inventory_hostname }}] Rút khỏi cụm trước khi sửa"
      debug:
        msg: "Thực tế: gọi API load balancer để ngừng gửi tải vào máy này"
      tags: [always]

  roles:
    - role: web

  post_tasks:
    - name: "[{{ inventory_hostname }}] Xác nhận khoẻ rồi mới đưa lại vào cụm"
      uri:
        url: "http://127.0.0.1/"
        return_content: true
      register: kq
      failed_when: phien_ban not in kq.content

    - name: "[{{ inventory_hostname }}] Đã cập nhật xong"
      debug:
        msg: "✅ {{ inventory_hostname }} đang chạy {{ phien_ban }}"
```

#### File 7 — `inventory-tu-terraform.py`

```python
#!/usr/bin/env python3
"""Sinh inventory Ansible từ output của Terraform.
Dùng: ansible-playbook -i inventory-tu-terraform.py site.yml"""

import json
import subprocess
import sys


def lay_output_terraform():
    """Đọc terraform output. Nếu không có Terraform thì dùng dữ liệu mẫu."""
    try:
        r = subprocess.run(
            ["terraform", "output", "-json"],
            capture_output=True, text=True, timeout=10,
        )
        if r.returncode == 0 and r.stdout.strip():
            return json.loads(r.stdout)
    except Exception:
        pass
    # Dữ liệu mẫu để lab chạy được khi chưa có Terraform
    return {
        "may_web": {"value": [
            {"ten": "web1", "ip": "127.0.0.1", "cong_ssh": 2201},
            {"ten": "web2", "ip": "127.0.0.1", "cong_ssh": 2202},
        ]},
        "may_db": {"value": [
            {"ten": "db1", "ip": "127.0.0.1", "cong_ssh": 2203},
        ]},
    }


def dung_inventory():
    tf = lay_output_terraform()
    inv = {
        "_meta": {"hostvars": {}},
        "all": {"children": ["web", "db", "ungrouped"]},
        "web": {"hosts": [], "vars": {"vai_tro": "web"}},
        "db": {"hosts": [], "vars": {"vai_tro": "database"}},
    }

    for khoa, nhom in (("may_web", "web"), ("may_db", "db")):
        for may in tf.get(khoa, {}).get("value", []):
            ten = may["ten"]
            inv[nhom]["hosts"].append(ten)
            inv["_meta"]["hostvars"][ten] = {
                "ansible_host": may["ip"],
                "ansible_port": may.get("cong_ssh", 22),
                "ansible_user": "quantri",
                "ansible_ssh_private_key_file": "./khoa_lab",
                "ansible_ssh_common_args":
                    "-o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null",
            }
    return inv


if __name__ == "__main__":
    if "--list" in sys.argv:
        print(json.dumps(dung_inventory(), indent=2, ensure_ascii=False))
    elif "--host" in sys.argv:
        print(json.dumps({}))
    else:
        print("Dùng: --list hoặc --host <tên máy>", file=sys.stderr)
        sys.exit(1)
```

### 🧭 Hướng dẫn làm LAB — step by step

#### Bước 1 — Dựng lại 3 server và tạo cấu trúc role

```bash
# Dựng lại môi trường Ngày 47
cd ~/lab47-ansible && docker compose up -d && cd ~

mkdir -p ~/lab-nt3/{group_vars,roles/web/{defaults,tasks,handlers,templates}}
cd ~/lab-nt3
cp ~/lab47-ansible/khoa_lab* .
cp ~/lab47-ansible/inventory.ini .

# tạo các file theo phần LAB
tree -L 3 2>/dev/null || find . -type d -not -path './.git*' | sort
```

**Bạn sẽ thấy** cấu trúc thư mục role đúng chuẩn.

✅ **Checkpoint:** có đủ `defaults/`, `tasks/`, `handlers/`, `templates/`.

Kiểm tra kết nối:
```bash
ansible all -m ping
```

💡 Để ý không cần `-i inventory.ini` nữa — `ansible.cfg` đã khai sẵn.

#### Bước 2 — Mã hoá một biến bằng Vault

```bash
echo 'matkhau-vault-lab' > .vault-pass
chmod 600 .vault-pass
echo ".vault-pass" >> .gitignore

ansible-vault encrypt_string --vault-password-file .vault-pass \
  'MatKhauDatabaseThatSuBiMat' --name 'mat_khau_db'
```

**Bạn sẽ thấy:**
```text
mat_khau_db: !vault |
          $ANSIBLE_VAULT;1.1;AES256
          61336264396533383864363437...
          ...
Encryption successful
```

Dán vào `group_vars/web.yml` cùng với các biến thường:

```yaml
---
web_tieu_de: "Cửa hàng ABC"
web_cong: 80
ten_database: cuahang

mat_khau_db: !vault |
          $ANSIBLE_VAULT;1.1;AES256
          <dán phần vừa sinh vào đây>
```

Kiểm chứng Ansible đọc được:
```bash
ansible web -m debug -a "var=mat_khau_db" --vault-password-file .vault-pass | head -5
```

**Bạn sẽ thấy:** giá trị thật được giải mã.

✅ **Checkpoint:** biến mã hoá nằm chung file với biến thường, và đọc được.

💡 **So sánh với cách mã hoá cả file ở Ngày 47:**

| | Mã hoá cả file | Mã hoá từng biến |
|---|---|---|
| Nhìn thấy có biến gì | ❌ Cả file là khối nhị phân | ✅ Tên biến đọc được |
| `git diff` | ❌ Vô dụng | ✅ Thấy đúng dòng nào đổi |
| Review Pull Request | ❌ Không review được | ✅ Review được phần không nhạy cảm |

Cách thứ hai gần như luôn tốt hơn.

⚠️ File `.vault-pass` **không bao giờ được commit**. Ở công ty, mật khẩu vault thường lấy từ biến môi trường hoặc từ hệ quản lý bí mật.

#### Bước 3 — Chạy role và kiểm chứng biến ưu tiên

```bash
ansible-playbook site.yml --vault-password-file .vault-pass
```

**Bạn sẽ thấy** Ansible chạy **lần lượt từng máy** (do `serial: 1`):

```text
PLAY [Cập nhật cuốn chiếu cho nhóm web] ****************
TASK [web : Cài các gói cần thiết] *********************
ok: [web1]

TASK [web : Kiểm tra web trả lời được] *****************
ok: [web1]

TASK [[web1] Đã cập nhật xong] *************************
ok: [web1] => msg: ✅ web1 đang chạy v1

PLAY [Cập nhật cuốn chiếu cho nhóm web] ****************
TASK [web : Cài các gói cần thiết] *********************
ok: [web2]
...
```

✅ **Checkpoint:** thấy PLAY chạy **hai lần** — mỗi máy một lượt, không song song.

Kiểm chứng thứ tự ưu tiên biến:

```bash
echo "--- Giá trị từ group_vars ---"
ansible web1 -m debug -a "var=web_tieu_de" --vault-password-file .vault-pass | grep web_tieu_de

echo "--- Ghi đè bằng -e (ưu tiên cao nhất) ---"
ansible web1 -m debug -a "var=web_tieu_de" -e "web_tieu_de=GHI-DE" \
  --vault-password-file .vault-pass | grep web_tieu_de
```

**Bạn sẽ thấy:**
```text
web_tieu_de: Cửa hàng ABC
web_tieu_de: GHI-DE
```

✅ **Checkpoint:** `-e` thắng mọi nguồn khác.

#### Bước 4 — Đo tác dụng của `serial` khi có tải thật

Đây là bước cho thấy vì sao `serial` quan trọng. Mở **hai terminal**.

**Terminal 1** — mô phỏng người dùng liên tục:
```bash
tc=0; tb=0
for i in $(seq 1 120); do
  if docker exec may-web1 curl -fs --max-time 2 localhost > /dev/null 2>&1 \
     || docker exec may-web2 curl -fs --max-time 2 localhost > /dev/null 2>&1; then
    tc=$((tc+1)); printf "."
  else
    tb=$((tb+1)); printf "X"
  fi
  sleep 0.5
done
echo ""; echo "Thành công: $tc | Thất bại: $tb"
```

**Terminal 2** — cập nhật lên phiên bản mới:
```bash
cd ~/lab-nt3
sleep 5
PHIEN_BAN=v2 ansible-playbook site.yml --vault-password-file .vault-pass
```

**Bạn sẽ thấy ở Terminal 1:**
```text
........................................................
Thành công: 120 | Thất bại: 0
```

✅ **Checkpoint:** **không mất một request nào** trong lúc cập nhật.

💡 **Vì sao đạt được điều đó — ba yếu tố kết hợp:**
1. `serial: 1` → mỗi lúc chỉ một máy bị đụng vào, máy kia vẫn phục vụ
2. Handler dùng `reloaded` chứ không `restarted` → nginx nạp cấu hình mới **mà không ngắt kết nối đang có**
3. `post_tasks` kiểm tra máy khoẻ **trước khi** chuyển sang máy tiếp theo

Bỏ `serial: 1` đi thì cả hai máy cùng reload một lúc — và đó là lúc người dùng thấy lỗi.

Kiểm chứng đã lên v2:
```bash
docker exec may-web1 curl -s localhost | grep -E "h1|Phiên bản"
```

#### Bước 5 — `max_fail_percentage` chặn hỏng lan

Cố ý làm một máy lỗi:

```bash
docker exec may-web2 rm -f /usr/sbin/nginx     # phá nginx trên web2
PHIEN_BAN=v3 ansible-playbook site.yml --vault-password-file .vault-pass
echo "Mã thoát: $?"
```

**Bạn sẽ thấy:**
```text
PLAY RECAP ****************************************
web1  : ok=8  changed=1  failed=0
web2  : ok=3  changed=0  failed=1

Mã thoát: 2
```

✅ **Checkpoint:** playbook **dừng lại**, không đi tiếp sang máy khác.

💡 **Hãy hình dung với 20 máy:** không có `max_fail_percentage: 0`, Ansible sẽ vui vẻ hỏng cả 20 máy lần lượt. Có nó, bạn dừng ở máy thứ nhất và còn 19 máy nguyên vẹn để phục vụ trong lúc điều tra.

Đây là dây an toàn quan trọng nhất khi chạy playbook trên hệ thống đang phục vụ.

Sửa lại:
```bash
docker exec may-web2 apt-get install -y --reinstall nginx > /dev/null 2>&1
ansible-playbook site.yml --vault-password-file .vault-pass | tail -5
```

#### Bước 6 — Dùng tag để chạy một phần

Playbook lớn thì không phải lúc nào cũng cần chạy hết:

```bash
echo "--- Xem có những tag nào ---"
ansible-playbook site.yml --list-tags

echo "--- Chỉ chạy phần cấu hình, bỏ qua cài đặt ---"
time ansible-playbook site.yml --tags cau-hinh --vault-password-file .vault-pass | tail -4

echo "--- Bỏ qua phần kiểm tra ---"
ansible-playbook site.yml --skip-tags kiem-tra --vault-password-file .vault-pass | tail -4
```

**Bạn sẽ thấy** lần chạy với `--tags cau-hinh` **nhanh hơn hẳn** vì bỏ qua bước `apt`.

✅ **Checkpoint:** chạy được một phần playbook.

💡 Rất hữu ích khi chỉ cần đẩy một thay đổi cấu hình nhỏ lên 50 máy — không cần chạy lại toàn bộ quy trình cài đặt.

#### Bước 7 — Inventory động

```bash
chmod +x inventory-tu-terraform.py
./inventory-tu-terraform.py --list | head -25
```

**Bạn sẽ thấy** JSON đúng định dạng Ansible mong đợi.

Dùng nó thay cho file tĩnh:

```bash
ansible all -i inventory-tu-terraform.py -m ping
ansible-inventory -i inventory-tu-terraform.py --graph
```

**Bạn sẽ thấy:**
```text
@all:
  |--@web:
  |  |--web1
  |  |--web2
  |--@db:
  |  |--db1
```

✅ **Checkpoint:** inventory sinh từ script, không phải file viết tay.

💡 **Đây là mắt xích nối Terraform với Ansible:**
```text
terraform apply  →  tạo VM
       ↓
terraform output -json  →  danh sách IP
       ↓
inventory động  →  Ansible cấu hình đúng những máy vừa tạo
```

Không có nó, mỗi lần Terraform tạo máy mới bạn lại phải sửa `inventory.ini` bằng tay — và chắc chắn sẽ có lúc quên.

Với cloud thật, dùng plugin có sẵn thay vì tự viết script:

```yaml
# aws_ec2.yml — Ansible tự gọi API AWS, lọc theo thẻ
plugin: amazon.aws.aws_ec2
regions: [ap-southeast-1]
filters:
  tag:moi_truong: production
keyed_groups:
  - key: tags.vai_tro          # tự tạo nhóm theo thẻ vai_tro
    prefix: ""
    separator: ""
```

Chạy: `ansible-playbook -i aws_ec2.yml site.yml` — danh sách máy **luôn khớp thực tế**, không bao giờ lỗi thời.

#### Bước 8 — Dọn dẹp

```bash
cd ~/lab47-ansible && docker compose down
```

### 💡 Đi làm mới thấm

- **Đặt biến vào `defaults/` chứ không phải `vars/`.** Role có mọi thứ trong `vars/` thì không ai ghi đè được, và không ai dùng lại được. Quy tắc: thứ gì người dùng role *có thể* muốn đổi thì để `defaults/`.
- **`serial` là bắt buộc với dịch vụ đang phục vụ.** Đây là khác biệt giữa *"cập nhật hệ thống"* và *"hạ toàn bộ hệ thống cùng lúc"*. Đi kèm `max_fail_percentage: 0` để dừng ở máy đầu tiên bị lỗi.
- **`reload` khác `restart`.** `reload` nạp cấu hình mới **không ngắt kết nối đang có**; `restart` giết tiến trình và mọi kết nối. Handler cho web server gần như luôn nên dùng `reload`.
- **Mã hoá từng biến, không mã hoá cả file.** `encrypt_string` cho phép review Pull Request và đọc được `git diff` — mã hoá cả file thì không.
- **Kiểm thử role bằng Molecule khi role được nhiều nơi dùng.** Nó dựng container sạch, chạy role, kiểm chứng kết quả, rồi **chạy lại lần hai để xác nhận idempotent**. Với role dùng chung toàn công ty, đây là thứ ngăn một thay đổi nhỏ làm hỏng 50 máy.
- **Đọc code role trên Galaxy trước khi dùng.** Bạn đang cho code của người lạ chạy với quyền root trên máy chủ của mình. Và **ghim phiên bản** trong `requirements.yml` — đúng bài học `latest` của Ngày 33.
- **Bật `pipelining = True`.** Một dòng trong `ansible.cfg`, giảm đáng kể số lượt SSH — playbook chạy nhanh hơn rõ rệt trên nhiều máy.

### 📝 Tự kiểm tra

<details>
<summary><b>1. Phân biệt `defaults/main.yml` và `vars/main.yml`. Đặt sai chỗ thì sao?</b></summary>

- **`defaults/`**: ưu tiên **thấp nhất** — người dùng role ghi đè rất dễ
- **`vars/`**: ưu tiên **cao** — khó ghi đè, chỉ thua `-e` và một vài nguồn khác

Đặt sai chỗ (để mọi biến vào `vars/`) khiến role trở nên **cứng nhắc**: người dùng muốn đổi cổng hay tên thư mục cũng không được, phải sửa thẳng vào role. Kết quả là mỗi đội fork một bản riêng — mất hẳn mục đích dùng lại.

Quy tắc: thứ gì người dùng role *có thể* muốn đổi → `defaults/`. Chỉ hằng số nội bộ mới vào `vars/`.
</details>

<details>
<summary><b>2. Vì sao `serial: 1` quan trọng với dịch vụ đang phục vụ?</b></summary>

Mặc định Ansible chạy **song song trên mọi máy**. Nghĩa là nếu playbook có lỗi, hoặc bước restart dịch vụ gây gián đoạn, thì **toàn bộ đội máy bị ảnh hưởng cùng một lúc** — không còn máy nào phục vụ.

`serial: 1` cập nhật lần lượt, nên luôn có máy khác đang phục vụ. Kết hợp với `max_fail_percentage: 0`, bạn dừng ngay ở máy đầu tiên bị lỗi.

Dạng `serial: [1, 5, "50%"]` là canary: một máy thử → năm máy → nửa còn lại.
</details>

<details>
<summary><b>3. Vì sao handler nên dùng `reloaded` thay vì `restarted`?</b></summary>

- **`reload`**: tiến trình nạp lại cấu hình mới, **giữ nguyên các kết nối đang có**. Người dùng không thấy gì.
- **`restart`**: giết tiến trình rồi khởi động lại — **mọi kết nối đang có bị ngắt**, và có một khoảng dịch vụ không phục vụ được.

Với nginx, Apache, HAProxy thì `reload` gần như luôn đủ.

Chỉ cần `restart` khi thay đổi thứ không nạp lại được (ví dụ đổi user chạy tiến trình, hoặc nâng cấp binary).
</details>

<details>
<summary><b>4. Mã hoá cả file và mã hoá từng biến khác nhau thế nào? Cái nào tốt hơn?</b></summary>

**Mã hoá cả file** (`ansible-vault create x.yml`): toàn bộ file thành khối nhị phân. Không biết trong đó có biến gì, `git diff` vô dụng, không review Pull Request được.

**Mã hoá từng biến** (`ansible-vault encrypt_string`): chỉ giá trị nhạy cảm bị che, tên biến vẫn đọc được, nằm chung file với biến thường.

Cách thứ hai gần như luôn tốt hơn: bạn review được phần không nhạy cảm, và `git diff` chỉ ra đúng dòng nào đổi.
</details>

<details>
<summary><b>5. Inventory động giải quyết vấn đề gì? Nêu một cách triển khai.</b></summary>

Vấn đề: hạ tầng tạo bằng Terraform hoặc tự mở rộng thì **danh sách máy thay đổi liên tục**. File `inventory.ini` viết tay sẽ lỗi thời ngay, và bạn sẽ có lúc cấu hình nhầm máy hoặc bỏ sót máy.

Ba cách triển khai:
1. **Plugin cloud** (`amazon.aws.aws_ec2`) — Ansible tự gọi API, lọc theo thẻ, tự tạo nhóm
2. **Script động** — bất kỳ chương trình nào in ra JSON đúng định dạng khi gọi với `--list`
3. **Từ Terraform output** — `terraform output -json` chuyển thành inventory

Cách 3 là mắt xích nối Terraform (tạo máy) với Ansible (cấu hình máy) thành một quy trình liền mạch.
</details>

### 📚 Thuật ngữ Anh–Việt

| Thuật ngữ | Nghĩa |
|---|---|
| **Role** | Cách đóng gói playbook để dùng lại; Ansible tự tìm file theo tên thư mục |
| **`defaults/` vs `vars/`** | Biến dễ ghi đè vs biến khó ghi đè |
| **Variable precedence** | Thứ tự ưu tiên biến; `-e` cao nhất |
| **`serial`** | Cập nhật lần lượt từng nhóm máy thay vì đồng loạt |
| **`max_fail_percentage`** | Tỉ lệ máy lỗi tối đa trước khi dừng toàn bộ |
| **`pre_tasks` / `post_tasks`** | Việc chạy trước / sau role — dùng cho rút khỏi cụm và kiểm tra |
| **Tag** | Nhãn cho task, cho phép chạy hoặc bỏ qua một phần playbook |
| **`encrypt_string`** | Mã hoá **một giá trị**, dán vào file như biến thường |
| **Dynamic inventory** | Danh sách máy sinh tự động từ cloud/Terraform |
| **`keyed_groups`** | Tự tạo nhóm Ansible theo thẻ của tài nguyên cloud |
| **Molecule** | Khung kiểm thử role: dựng container, chạy, kiểm chứng, test idempotent |
| **`pipelining`** | Giảm số lượt SSH mỗi task — tăng tốc đáng kể |
| **Ansible Galaxy** | Kho role cộng đồng; đọc code và ghim phiên bản trước khi dùng |

### 🎯 Đúc kết NT3

**3 điều phải mang theo:**

1. **Role là đơn vị tái sử dụng** — và `defaults/` là thứ quyết định role của bạn có ai dùng lại được hay không.
2. **`serial` + `max_fail_percentage` + `reload`** là bộ ba biến việc cập nhật thành thao tác không gián đoạn. Thiếu chúng, một playbook có thể hạ cả hệ thống trong vài giây.
3. **Inventory động nối Terraform với Ansible.** Terraform tạo máy, xuất IP, Ansible cấu hình — không ai phải sửa danh sách bằng tay.

> 🧠 **Một câu để nhớ:** playbook chạy được trên một máy là bài tập; playbook chạy được trên **năm mươi máy đang phục vụ mà không ai nhận ra** mới là kỹ năng.

**✅ Tự chấm:**

- [ ] Tạo role đúng cấu trúc, biến đặt trong `defaults/`
- [ ] Giải thích thứ tự ưu tiên biến và kiểm chứng `-e` thắng
- [ ] Dùng `serial` và **đo được** không mất request nào khi cập nhật
- [ ] Chứng minh `max_fail_percentage: 0` dừng playbook ở máy lỗi đầu tiên
- [ ] Giải thích vì sao handler dùng `reload` chứ không `restart`
- [ ] Mã hoá biến bằng `encrypt_string` và nói rõ hơn gì so với mã hoá cả file
- [ ] Dùng tag chạy một phần playbook
- [ ] Viết hoặc dùng được inventory động

✅ **Kết quả đạt được:** Ansible ở mức dùng được trong đội — role tái sử dụng, bí mật mã hoá review được, cập nhật không gián đoạn, và danh sách máy luôn khớp thực tế.
