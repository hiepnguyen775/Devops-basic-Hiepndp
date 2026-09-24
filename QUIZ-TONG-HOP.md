# 🧠 QUIZ TỔNG HỢP — Kiểm tra cuối mỗi giai đoạn

> **4 bộ × 20 câu** — làm sau khi xong mỗi giai đoạn. Mỗi bộ gồm **10 câu khái niệm · 5 câu gỡ lỗi · 5 câu tình huống**.
>
> ⏱️ Mỗi bộ ~45 phút · 📏 **Không xem lại tài liệu trong lúc làm.**

---

## Cách làm cho đúng

| Bước | Làm gì |
|---|---|
| 1 | Đọc câu hỏi, **nói to câu trả lời** (nói to — nghĩ thầm luôn thấy mình hiểu) |
| 2 | Mở đáp án, đối chiếu |
| 3 | Tự chấm: **2 điểm** đúng · **1 điểm** đúng một phần · **0 điểm** chưa được |
| 4 | Mọi câu dưới 2 điểm → ghi lại ngày cần ôn |

| Điểm /40 | Đánh giá |
|---|---|
| **34–40** | 🟢 Vững — đi tiếp giai đoạn sau |
| **26–33** | 🟡 Ôn lại các ngày bị mất điểm rồi đi tiếp |
| **Dưới 26** | 🔴 Làm lại LAB Final của giai đoạn trước khi đi tiếp |

---

# BỘ 1 — Giai đoạn 1: Linux & SysOps

> Làm sau [Ngày 12](./Giai-doan-1-Linux-SysOps.md#ngày-12--milestone-lab-tổng-hợp-giai-đoạn-1)

## Phần A — Khái niệm (10 câu)

<details><summary><b>1. Phân biệt <code>>></code> và <code>></code> khi ghi file. Cái nào nguy hiểm hơn?</b></summary>

`>` **ghi đè** — xoá sạch nội dung cũ rồi ghi mới. `>>` **ghi thêm** vào cuối.

`>` nguy hiểm hơn nhiều: một lệnh `echo "x" > /etc/nginx/nginx.conf` xoá sạch file cấu hình. Không có cảnh báo, không hoàn tác được.

📖 Ngày 2
</details>

<details><summary><b>2. Quyền <code>755</code> và <code>644</code> nghĩa là gì? Vì sao thư mục cần quyền thực thi?</b></summary>

`755` = chủ sở hữu đọc-ghi-chạy, nhóm và người khác đọc-chạy. `644` = chủ đọc-ghi, còn lại chỉ đọc.

Với **thư mục**, bit "thực thi" (`x`) nghĩa là *"được phép đi vào"* — không có nó thì `cd` vào không được, dù có quyền đọc. Đó là lý do thư mục thường `755` còn file thường `644`.

📖 Ngày 4
</details>

<details><summary><b>3. Vì sao không nên dùng <code>chmod 777</code> kể cả khi nó sửa được lỗi ngay?</b></summary>

`777` cho **mọi người dùng** quyền đọc-ghi-chạy. Nó "sửa được lỗi" vì xoá bỏ mọi ràng buộc — giống chữa cửa kẹt bằng cách tháo cánh cửa.

Rủi ro: bất kỳ tiến trình nào bị chiếm quyền đều sửa được file; file thực thi có thể bị thay bằng mã độc. Và nó **che giấu vấn đề thật**, thường là sai chủ sở hữu.

📖 Ngày 4
</details>

<details><summary><b>4. Phân biệt tiến trình nền (<code>&</code>) và dịch vụ systemd.</b></summary>

`&` chạy nền **trong phiên hiện tại** — đóng terminal là tiến trình chết (trừ khi dùng `nohup`/`disown`).

**systemd service** do hệ thống quản lý: tự bật khi máy khởi động, tự restart khi chết, có log qua `journalctl`, có quản lý phụ thuộc.

Mọi thứ cần chạy lâu dài đều nên là service, không phải `&`.

📖 Ngày 3
</details>

<details><summary><b>5. <code>Connection refused</code> khác <code>Connection timed out</code> thế nào?</b></summary>

- **refused** → gói tin **tới được máy**, nhưng không có tiến trình nào nghe ở cổng đó (kernel trả về RST)
- **timed out** → gói tin **bị chặn im lặng**, gần như luôn là tường lửa

Phân biệt được hai cái này cho biết nên đi sửa **dịch vụ** hay sửa **tường lửa** — tiết kiệm rất nhiều thời gian.

📖 Ngày 7, 9
</details>

<details><summary><b>6. Vì sao SSH bằng khoá an toàn hơn mật khẩu?</b></summary>

Mật khẩu có thể bị dò (máy chủ mở cổng 22 ra Internet bị dò hàng nghìn lần mỗi ngày), bị đoán, bị dùng lại từ chỗ khác.

Khoá riêng **không bao giờ rời khỏi máy bạn** — quá trình xác thực chứng minh bạn có khoá mà không gửi nó đi. Không có gì để dò.

Hai dòng cấu hình `PermitRootLogin no` + `PasswordAuthentication no` vô hiệu hoá gần như toàn bộ loại tấn công phổ biến nhất.

📖 Ngày 8, 9
</details>

<details><summary><b>7. <code>set -euo pipefail</code> trong Bash làm gì?</b></summary>

| Cờ | Tác dụng |
|---|---|
| `-e` | Lệnh nào lỗi thì **dừng script ngay** |
| `-u` | Dùng biến chưa khai báo là lỗi |
| `-o pipefail` | Trong pipe, lệnh **nào** lỗi cũng tính là lỗi (không chỉ lệnh cuối) |

Không có nó, script chạy tiếp sau khi một bước thất bại — và làm hỏng thứ bạn không ngờ tới.

📖 Ngày 5, 6
</details>

<details><summary><b>8. Vì sao sao lưu chưa từng khôi phục thử không phải bản sao lưu?</b></summary>

Vì lệnh sao lưu chạy **thành công** không chứng minh file dùng được. File có thể rỗng, thiếu bảng, hỏng, hoặc mất khoá giải mã.

Vô số tổ chức phát hiện điều này theo cách đau nhất: sao lưu chạy đều hai năm, đến lúc cần thì không khôi phục được.

Bắt buộc: script có bước tự kiểm chứng, và diễn tập khôi phục định kỳ.

📖 Ngày 11
</details>

<details><summary><b>9. Quy tắc 3-2-1 là gì?</b></summary>

**3** bản sao dữ liệu · **2** loại phương tiện khác nhau · **1** bản ở nơi khác về địa lý.

Chữ "1" quan trọng nhất: mã độc tống tiền ngày nay **tìm và xoá bản sao lưu trước**, rồi mới mã hoá dữ liệu. Bản sao lưu cùng máy, cùng tài khoản thì cùng chết.

📖 Ngày 11
</details>

<details><summary><b>10. Vì sao web server không nên chạy bằng root?</b></summary>

Nếu ứng dụng bị khai thác, kẻ tấn công có ngay **quyền root trên toàn máy** — đọc mọi file, cài mã độc, xoá log để che dấu vết.

Chạy bằng user riêng thì thiệt hại giới hạn trong phạm vi user đó. Đây là nguyên tắc **đặc quyền tối thiểu**, và bạn sẽ gặp lại nó ở Docker, Kubernetes, CI/CD.

📖 Ngày 4, 9
</details>

## Phần B — Gỡ lỗi (5 câu)

<details><summary><b>11. <code>df -h</code> báo đầy 100% nhưng <code>du -sh /*</code> cộng lại chỉ một nửa. Vì sao?</b></summary>

Thường nhất: có tiến trình đang **giữ một file đã bị xoá**. Kernel chưa giải phóng dung lượng — `du` không thấy file nữa, `df` vẫn tính.

```bash
lsof +L1        # file đã xoá nhưng còn tiến trình giữ
```
Xử lý: khởi động lại tiến trình đó (thường là dịch vụ ghi log).

Hai khả năng khác: **hết inode** (`df -i`), hoặc có phân vùng mount đè lên thư mục đang chứa dữ liệu.

📖 Ngày 3, 10, 11
</details>

<details><summary><b>12. Dịch vụ systemd liên tục restart. Ba lệnh đầu tiên bạn chạy?</b></summary>

```bash
systemctl status ten-dv                       # trạng thái + log cuối
journalctl -u ten-dv -n 50 --no-pager         # log đầy đủ
systemctl cat ten-dv                          # file unit đang thực sự dùng
```

Nguyên nhân hay gặp: sai `ExecStart`, thiếu biến môi trường, sai quyền file cấu hình, hoặc cổng đã bị chiếm (`ss -tlnp`).

📖 Ngày 3, 10
</details>

<details><summary><b>13. Bạn đổi cổng SSH rồi restart, giờ không vào được máy. Nguyên nhân?</b></summary>

Gần như chắc chắn: **quên mở cổng mới trên tường lửa**. UFW vẫn chỉ cho phép 22, mà sshd giờ nghe cổng khác.

Thứ tự đúng: mở cổng mới **trước** → sửa cấu hình → `sshd -t` kiểm tra cú pháp → restart → thử từ phiên mới → đóng cổng cũ.

Và luôn **giữ một phiên SSH dự phòng** trong lúc siết cấu hình.

📖 Ngày 8, 9
</details>

<details><summary><b>14. Cron job không chạy dù script chạy tay bình thường. Ba nguyên nhân?</b></summary>

1. **Đường dẫn tương đối** — cron chạy với thư mục làm việc khác. Luôn dùng đường dẫn tuyệt đối.
2. **Biến môi trường khác** — cron có `PATH` rất tối giản, không có các biến trong `.bashrc`.
3. **Không có log** — không redirect thì lỗi biến mất. Thêm `>> /var/log/x.log 2>&1`.

Cách chẩn đoán: `grep CRON /var/log/syslog` xem cron có chạy không.

📖 Ngày 6
</details>

<details><summary><b>15. Máy chậm bất thường. Bạn kiểm tra gì, theo thứ tự nào?</b></summary>

```bash
uptime              # tải trung bình — so với số nhân (nproc)
top / htop          # tiến trình nào ngốn CPU/RAM
free -h             # còn RAM không? có đang swap không?
df -h               # đĩa đầy chưa? (đĩa đầy gây chậm bất ngờ)
iostat -x 1 3       # đĩa có bị nghẽn I/O không
journalctl -p err -n 30   # có lỗi hệ thống gì không
```

Thứ tự này đi từ **tổng quan** xuống **chi tiết**, mỗi bước loại trừ một nhóm nguyên nhân.

📖 Ngày 3, 10
</details>

## Phần C — Tình huống (5 câu)

<details><summary><b>16. Bạn nhận một máy chủ không ai còn làm ở công ty, không tài liệu. Bắt đầu từ đâu?</b></summary>

**Hiểu trước, sửa sau:**
1. **Đừng đụng gì** vài ngày đầu — quan sát
2. Liệt kê dịch vụ đang chạy: `ss -tlnp`, `systemctl list-units --type=service --state=running`
3. **Kiểm tra sao lưu** — có chạy không, và **đã ai khôi phục thử chưa?** Đây gần như luôn là lỗ hổng lớn nhất
4. Dựng giám sát tối thiểu — ít nhất biết khi nào nó chết
5. Viết tài liệu **dần khi tìm hiểu**, đừng để cuối
6. Cải thiện từng bước, không đập đi xây lại

Câu trả lời tệ: *"em sẽ cài lại từ đầu"*.
</details>

<details><summary><b>17. Sếp muốn tắt tường lửa "cho nhanh, mạng nội bộ mà". Bạn nói gì?</b></summary>

Không phản đối bằng cảm tính, mà nêu rủi ro cụ thể:
- Mạng nội bộ **không an toàn tự động** — một máy nhiễm là lan cả mạng (chuyển động ngang)
- Nếu vấn đề là tường lửa chặn nhầm, cách đúng là **mở đúng cổng cần**, mất 2 phút
- Đề nghị: cho tôi 15 phút tìm cổng đang bị chặn (`journalctl -u ufw`, `ss -tlnp`)

Nếu sếp vẫn quyết: **ghi lại quyết định đó** (email/ticket) và đề xuất giới hạn phạm vi — chỉ tắt trên một máy, trong thời gian có hạn.
</details>

<details><summary><b>18. Ổ đĩa production sắp đầy lúc 2 giờ sáng. Bạn làm gì?</b></summary>

**Cầm máu trước:**
1. Tìm thủ phạm: `du -sh /var/* | sort -h | tail`, `du -sh /var/log/*`
2. Giải phóng an toàn: xoá log cũ đã xoay vòng, xoá cache gói (`apt clean`), xoá file tạm
3. **Kiểm tra file đã xoá nhưng còn bị giữ**: `lsof +L1`

**Không làm:** xoá bừa file không biết là gì; xoá log đang được ghi (dung lượng không giải phóng).

**Sau đó:** bật xoay vòng log, thêm cảnh báo ở ngưỡng 80%, và tìm nguyên nhân vì sao đầy nhanh.
</details>

<details><summary><b>19. Đồng nghiệp chạy <code>rm -rf</code> nhầm thư mục. Bạn phản ứng thế nào?</b></summary>

**Về kỹ thuật:** dừng ngay mọi ghi vào ổ đó, xác định phạm vi, khôi phục từ sao lưu, kiểm chứng dữ liệu đầy đủ.

**Về con người — phần quan trọng hơn:** không đổ lỗi cá nhân. Câu hỏi đúng là *"hệ thống nào đã cho phép một lệnh gõ nhầm gây hậu quả này?"*

Hành động khắc phục nhắm vào hệ thống: sao lưu có kiểm chứng, giới hạn quyền (người đó có thật sự cần root không?), dùng `trash-cli` thay `rm` trên máy chủ, yêu cầu xác nhận với thao tác nguy hiểm.

Nếu người ta sợ bị đổ lỗi, họ sẽ **giấu sai sót** — và bạn mất luôn cơ hội sửa hệ thống.
</details>

<details><summary><b>20. Bạn phải bàn giao máy chủ cho người mới trong 30 phút. Tài liệu gồm gì?</b></summary>

Ngắn thôi, nhưng đủ để tiếp quản:

| Mục | Nội dung |
|---|---|
| Thông tin cơ bản | OS, cách SSH vào, dịch vụ nào chạy ở cổng nào |
| Tài khoản | User nào dùng để làm gì, ai đăng nhập được |
| Sao lưu | Script ở đâu, chạy lúc nào, **khôi phục bằng lệnh nào** |
| Xử lý sự cố | Bảng triệu chứng → lệnh kiểm tra |
| Liên hệ | Ai chịu trách nhiệm, leo thang cho ai |

**Phép thử:** đưa cho họ đọc, rồi hỏi ba câu — máy chạy gì? sao lưu ở đâu? dịch vụ chết thì kiểm tra gì? Trả lời được là tài liệu đạt.
</details>

**Điểm bộ 1: ___ / 40**

---

# BỘ 2 — Giai đoạn 2: Git, Docker & Cloud

> Làm sau [Ngày 30](./Giai-doan-2-Git-Docker-Cloud.md#ngày-30--milestone-lab-tổng-hợp-giai-đoạn-2)

## Phần A — Khái niệm (10 câu)

<details><summary><b>1. Ba khu vực của Git là gì? File đi qua chúng thế nào?</b></summary>

**Working directory** (file bạn đang sửa) → `git add` → **Staging area** (chuẩn bị commit) → `git commit` → **Repository** (lịch sử).

Staging area là thứ cho phép bạn **chọn lọc** thay đổi nào vào commit này — sửa 5 file nhưng chỉ commit 2 file liên quan.

📖 Ngày 13
</details>

<details><summary><b>2. Khi nào dùng merge, khi nào rebase?</b></summary>

**Merge**: giữ nguyên lịch sử, tạo commit merge. Dùng cho nhánh **đã chia sẻ**.
**Rebase**: viết lại lịch sử cho thẳng. Dùng cho nhánh **cá nhân**, trước khi mở PR.

**Quy tắc vàng:** không bao giờ rebase nhánh người khác đã pull về — họ sẽ gặp xung đột rất khó gỡ.

📖 Ngày 14, 25
</details>

<details><summary><b>3. Container khác máy ảo ở điểm cốt lõi nào?</b></summary>

**Máy ảo** ảo hoá **phần cứng** — mỗi VM có kernel riêng, hệ điều hành đầy đủ. Nặng (GB), khởi động chậm (phút).

**Container** ảo hoá **hệ điều hành** — dùng chung kernel với máy chủ, chỉ đóng gói tiến trình và thư viện. Nhẹ (MB), khởi động nhanh (giây).

Hệ quả bảo mật: container **không cách ly bằng VM**. Root trong container gần với root ngoài máy hơn bạn tưởng.

📖 Ngày 16
</details>

<details><summary><b>4. Vì sao <code>COPY package*.json</code> phải đứng trước <code>COPY . .</code>?</b></summary>

Vì **cache lớp Docker phụ thuộc thứ tự dòng** — một lớp đổi thì mọi lớp sau phải làm lại.

Copy `package*.json` rồi `npm ci` trước: sửa code không đổi `package.json` → lớp cài thư viện lấy từ cache → build nhanh.

Đảo thứ tự: mỗi lần sửa một dòng code là cài lại toàn bộ thư viện.

📖 Ngày 17, 18
</details>

<details><summary><b>5. Phân biệt <code>expose</code> và <code>ports</code> trong Compose.</b></summary>

`ports: "3000:3000"` **mở cổng ra ngoài máy chủ** — ai vào được máy là vào được dịch vụ.
`expose: "3000"` chỉ cho container **trong cùng mạng Docker** thấy.

Quy tắc: chỉ reverse proxy dùng `ports`; ứng dụng và database dùng `expose`.

📖 Ngày 19, 28
</details>

<details><summary><b>6. Volume khác bind mount thế nào?</b></summary>

**Volume** do Docker quản lý (`/var/lib/docker/volumes/`), không phụ thuộc cấu trúc thư mục máy chủ, dễ sao lưu và di chuyển. Dùng cho **dữ liệu**.

**Bind mount** gắn một thư mục cụ thể của máy chủ vào container. Dùng cho **mã nguồn khi phát triển** (sửa file là container thấy ngay) và file cấu hình.

📖 Ngày 19
</details>

<details><summary><b>7. Trách nhiệm chia sẻ trên cloud nghĩa là gì?</b></summary>

Nhà cung cấp lo bảo mật **của** cloud: phần cứng, trung tâm dữ liệu, lớp ảo hoá.
**Bạn** lo bảo mật **trong** cloud: cấu hình, phân quyền, dữ liệu, bản vá.

Nghĩa là **"lên cloud" không tự động an toàn**. Bucket cấu hình sai vẫn công khai; khoá lộ trên GitHub vẫn bị lợi dụng.

📖 Ngày 26
</details>

<details><summary><b>8. <code>stop</code> và <code>terminate</code> một máy ảo khác nhau thế nào?</b></summary>

`stop`: tắt máy nhưng **giữ ổ đĩa** → vẫn trả tiền lưu trữ. Và **IP công khai bị mất** — bật lại có IP mới.
`terminate`: xoá hẳn, ổ đĩa xoá theo → hết tính tiền.

Hai nhầm lẫn tốn tiền: tưởng `stop` là hết tính tiền, và quên rằng IP đổi sau khi bật lại.

📖 Ngày 27
</details>

<details><summary><b>9. Terraform state là gì? Mất nó thì sao?</b></summary>

State là **sổ ghi ánh xạ** giữa code và tài nguyên thật.

Mất state → Terraform không biết nó đã tạo gì → `apply` tưởng chưa có gì → **tạo trùng toàn bộ hạ tầng**.

Và state **chứa bí mật ở dạng chữ thường** — không bao giờ commit vào Git.

📖 Ngày 29
</details>

<details><summary><b>10. cloud-init chạy khi nào? Sửa file rồi reboot có tác dụng không?</b></summary>

Chỉ chạy ở **lần khởi động đầu tiên**. Sửa rồi reboot máy cũ **không có tác dụng** — phải tạo máy mới.

Rất nhiều người mất cả buổi vì hiểu nhầm điểm này. Khi có lỗi, xem `/var/log/cloud-init-output.log`.

📖 Ngày 27
</details>

## Phần B — Gỡ lỗi (5 câu)

<details><summary><b>11. Container chết ngay sau khi khởi động. Đọc mã thoát thế nào?</b></summary>

```bash
docker ps -a                      # mã thoát
docker logs <container>           # app nói gì
```

| Mã | Nghĩa |
|---|---|
| `0` | Thoát bình thường — thường là lệnh chạy xong, không phải dịch vụ nền |
| `1` | Lỗi ứng dụng |
| `125` | Lỗi của Docker (sai tham số) |
| `126` | Lệnh không thực thi được (thiếu quyền) |
| `127` | Không tìm thấy lệnh (sai đường dẫn trong `CMD`) |
| `137` | **OOMKilled** — hết RAM |

📖 Ngày 16, 17
</details>

<details><summary><b>12. Backend crash vì database chưa sẵn sàng, dù đã có <code>depends_on</code>. Vì sao?</b></summary>

`depends_on` mặc định chỉ chờ container **khởi động**, không chờ nó **sẵn sàng nhận kết nối**. Postgres mất vài giây để khởi tạo.

Sửa: thêm healthcheck cho db và `condition: service_healthy` cho backend.

Nhưng đừng phụ thuộc hoàn toàn vào Compose — app vẫn nên **tự thử lại kết nối**, vì database có thể restart bất cứ lúc nào.

📖 Ngày 20
</details>

<details><summary><b>13. Bạn <code>git rm</code> file chứa mật khẩu rồi commit. Xong chưa?</b></summary>

**Chưa.** Git lưu toàn bộ lịch sử — ai clone repo vẫn lấy được từ commit cũ.

Thứ tự đúng:
1. **Vô hiệu hoá bí mật ngay** (đổi mật khẩu, thu hồi token) — làm đầu tiên
2. Xoá khỏi lịch sử (`git filter-repo`/BFG)
3. Bật quét tự động

Bí mật đã lộ phải coi như **đã bị đánh cắp**, kể cả repo private.

📖 Ngày 26, 49
</details>

<details><summary><b>14. Image build thành công nhưng chạy báo "not found" cho lệnh trong CMD. Vì sao?</b></summary>

Vài nguyên nhân phổ biến:
- **Image nền alpine** không có `bash` — chỉ có `sh`. `CMD ["bash", "..."]` sẽ lỗi 127.
- File thực thi **không có quyền chạy** — thêm `RUN chmod +x`.
- Đường dẫn sai vì `WORKDIR` khác với bạn nghĩ.
- Multi-stage: quên copy file từ tầng build sang tầng cuối.

Chẩn đoán: `docker run --rm -it <image> sh` rồi tự tìm.

📖 Ngày 17, 18
</details>

<details><summary><b>15. <code>terraform apply</code> báo tài nguyên đã tồn tại. Xử lý thế nào?</b></summary>

Nghĩa là tài nguyên **có thật ngoài đời** nhưng **không có trong state** — thường do tạo tay trước đó, hoặc state bị mất.

Hai lựa chọn:
- `terraform import <resource> <id>` — đưa nó vào state để Terraform quản lý (thường là lựa chọn đúng)
- Xoá tài nguyên thủ công rồi để Terraform tạo lại (chỉ khi nó không chứa dữ liệu quan trọng)

📖 Ngày 29
</details>

## Phần C — Tình huống (5 câu)

<details><summary><b>16. Đội bạn than "trên máy tôi chạy được, trên CI thì không". Ba nguyên nhân?</b></summary>

1. **Phiên bản khác nhau** — máy bạn Node 20, CI Node 18. Sửa bằng cách ghim phiên bản trong Dockerfile/CI.
2. **Thư viện cài từ cache cũ trên máy bạn** — CI cài sạch nên lộ ra thiếu phụ thuộc. Đó chính là lý do CI dùng `npm ci`.
3. **Biến môi trường/file chỉ có trên máy bạn** — `.env` không commit, CI không có.

Nguyên tắc chung: **runner sạch là tính năng, không phải lỗi** — nó ép bạn khai rõ mọi phụ thuộc.
</details>

<details><summary><b>17. Hoá đơn cloud tháng này gấp đôi. Điều tra thế nào?</b></summary>

1. Xem **phân rã theo dịch vụ** — khoản nào tăng
2. **Lọc theo thẻ** — nếu không gắn thẻ thì đây là bài học đầu tiên
3. Ba nghi phạm: tài nguyên mồ côi (ổ đĩa, IP tĩnh, snapshot) · môi trường dev chạy 24/7 · chi phí **truyền dữ liệu**
4. Nghiêm trọng: kiểm tra có tài nguyên lạ không — **khoá lộ bị dùng đào tiền ảo** là kịch bản có thật

Phòng ngừa: cảnh báo ngân sách theo **tốc độ tiêu**, bắt buộc gắn thẻ, rà tài nguyên mồ côi định kỳ.
</details>

<details><summary><b>18. Cần đưa app lên production tuần sau. Chọn Compose trên một VM hay Kubernetes?</b></summary>

Hỏi ngược lại trước: **bài toán là gì?**

Với một app, một máy, đội chưa ai biết K8s, deadline một tuần → **Compose trên VM** gần như chắc chắn đúng: đơn giản, ít thứ hỏng, đội vận hành được ngay.

K8s đáng giá khi: nhiều dịch vụ, nhiều máy, cần tự phục hồi và không gián đoạn, **và có người vận hành được nó**.

Câu trả lời tốt nhất còn nêu đường đi: bắt đầu Compose, đóng gói bằng Docker ngay từ đầu để sau này chuyển sang K8s không phải viết lại.
</details>

<details><summary><b>19. Đồng nghiệp commit thẳng vào <code>main</code> mà không qua PR. Bạn xử lý thế nào?</b></summary>

**Không trách cá nhân** — hỏi tại sao quy trình cho phép điều đó.

Kỹ thuật: bật **branch protection** cho `main` (require PR + require status checks). Khi đó không ai commit thẳng được, kể cả bạn.

Con người: giải thích **vì sao** cần PR — không phải để kiểm soát, mà để có review, có lịch sử, và để CI chặn được code hỏng.

Nếu họ bỏ qua vì PR quá chậm, thì vấn đề thật là **pipeline chậm** — đi sửa cái đó.
</details>

<details><summary><b>20. Bạn phải chọn dải IP cho VPC mới. Cân nhắc gì?</b></summary>

Đây là quyết định **khó đảo ngược nhất** trong thiết kế mạng.

1. **Không trùng** với mạng văn phòng, mạng đối tác, hoặc dải Docker mặc định (`172.17.0.0/16`) — trùng là VPN không kết nối được
2. **Đủ lớn để mở rộng** — dùng `/16`, chia subnet `/24` hoặc `/22`
3. **Chừa khoảng trống** giữa các nhóm subnet
4. **Nhóm theo chức năng** — mọi subnet công khai trong một dải liên tục, để viết một luật tường lửa cho cả nhóm
5. Nhớ **cloud giữ thêm 5 địa chỉ** mỗi subnet

📖 [NT1](./Module-Nen-Tang-Mo-Rong.md#nt1--mạng-chuyên-sâu-subnet-định-tuyến-bắt-gói--tls)
</details>

**Điểm bộ 2: ___ / 40**

---

# BỘ 3 — Giai đoạn 3: CI/CD, Kubernetes & Monitoring

> Làm sau [Ngày 50](./Giai-doan-3-CICD-K8s-Monitoring.md#ngày-50--milestone-lab-tổng-hợp-giai-đoạn-3)

## Phần A — Khái niệm (10 câu)

<details><summary><b>1. Vì sao runner CI luôn là máy sạch? Lợi và bất tiện?</b></summary>

**Lợi:** mọi phụ thuộc phải được khai rõ trong file → không bao giờ dính bệnh *"trên máy tôi chạy được"*. Kết quả tái lập được.

**Bất tiện:** mỗi lần chạy phải tải lại thư viện → chậm. Giải bằng **cache**.

📖 Ngày 31, 32
</details>

<details><summary><b>2. Giải thích vòng điều hoà của Kubernetes.</b></summary>

Một vòng lặp chạy liên tục: đọc **trạng thái mong muốn** (YAML) → so với **thực tế** → khác thì sửa → lặp lại.

Mọi tính năng chỉ là vòng lặp này áp vào tình huống khác nhau: tự phục hồi, tự mở rộng, cập nhật không gián đoạn.

Bạn gặp lại đúng khuôn này ở ArgoCD, Ansible và Terraform.

📖 Ngày 36
</details>

<details><summary><b>3. Service tìm pod bằng cách nào? Vì sao không dùng IP?</b></summary>

Service không giữ danh sách IP — nó giữ một **câu hỏi**: *"pod nào mang nhãn này?"* và hỏi lại liên tục.

Không dùng IP pod vì pod là đồ dùng một lần: chết là bản mới có **IP khác**. Mà pod chết xảy ra suốt — cập nhật, bảo trì, tự mở rộng.

📖 Ngày 38
</details>

<details><summary><b>4. readinessProbe và livenessProbe khác nhau ra sao? Đặt nhầm thì sao?</b></summary>

**readiness** trượt → **rút pod khỏi Service**, pod vẫn sống.
**liveness** trượt → **giết và tạo lại container**.

Đặt nhầm rất nguy hiểm: liveness kiểm tra database → database chậm → mọi pod bị giết cùng lúc → khởi động lại đồng loạt → database càng ngộp → sập dây chuyền.

Quy tắc: liveness **chỉ kiểm tra chính tiến trình đó**.

📖 Ngày 41
</details>

<details><summary><b>5. <code>requests</code> và <code>limits</code> khác nhau về vai trò?</b></summary>

`requests` = *"cần tối thiểu ngần này"*. **Scheduler** dùng để chọn node. Đây là con số bạn **trả tiền**.
`limits` = *"không vượt quá"*. **Kernel** cưỡng chế.

Vượt RAM → **OOMKilled**. Vượt CPU → **bị bóp chậm**, không bị giết.

Không khai `requests` → lớp QoS BestEffort → **bị giết đầu tiên** khi node cạn RAM.

📖 Ngày 41
</details>

<details><summary><b>6. Vì sao counter phải bọc <code>rate()</code>?</b></summary>

Counter chỉ tăng — con số thô (*"3 triệu request từ hôm khai trương"*) gần như vô nghĩa.

Cái bạn cần là **tốc độ hiện tại**: *"đang 120 request/giây, bình thường 40"*. `rate(x[5m])` cho điều đó.

Gauge thì đọc thẳng — bọc `rate()` vào gauge ra kết quả vô nghĩa.

📖 Ngày 44
</details>

<details><summary><b>7. Bốn tín hiệu vàng là gì?</b></summary>

**Traffic** (bao nhiêu khách) · **Errors** (bao nhiêu % hỏng) · **Latency** (khách chờ bao lâu) · **Saturation** (còn dư sức không).

Chúng là **bộ lọc** giúp biết nhìn gì giữa hàng nghìn metric — trả lời *"hệ thống có ổn không?"* trong 5 giây.

📖 Ngày 45
</details>

<details><summary><b>8. GitOps khác CI đẩy thẳng vào cluster ở điểm cốt lõi nào?</b></summary>

**Chiều của kết nối, và ai giữ chìa khoá.**

Push: CI ở ngoài giữ kubeconfig → chiếm được CI là chiếm được cluster.
Pull (GitOps): tác nhân **trong** cluster tự kéo từ Git → không ai bên ngoài cần chìa khoá, và sửa tay bị **tự hoàn tác**.

📖 Ngày 43
</details>

<details><summary><b>9. Loki khác Elasticsearch ở điểm nào? Cái giá?</b></summary>

Loki **chỉ đánh chỉ mục nhãn**, không đánh chỉ mục nội dung → nhẹ hơn nhiều về RAM và đĩa.

Cái giá: **bắt buộc chọn nhãn trước khi tìm** — không tìm khơi khơi trên toàn bộ log được.

📖 Ngày 46
</details>

<details><summary><b>10. Idempotent là gì? Vì sao Ansible cần nó?</b></summary>

Chạy 1 lần hay 100 lần đều cho **cùng kết quả**.

Bash script thường không có: `echo >> file` chạy hai lần là ghi thêm hai lần. Ansible mô tả **trạng thái mong muốn** và tự kiểm tra trước khi hành động.

Nhờ vậy playbook chạy lại lúc nào cũng an toàn — và dùng được để **sửa trôi cấu hình**.

📖 Ngày 47
</details>

## Phần B — Gỡ lỗi (5 câu)

<details><summary><b>11. Pod <code>CrashLoopBackOff</code>. Ba lệnh đầu tiên?</b></summary>

```bash
kubectl describe pod <p>          # Events ở cuối — quan trọng nhất
kubectl logs <p> --previous       # log của LẦN CHẠY TRƯỚC
kubectl get events --sort-by=.lastTimestamp | tail
```

Cờ `--previous` là chìa khoá — không có nó bạn chỉ thấy log container mới, chưa kịp lỗi.

📖 Ngày 37, 41
</details>

<details><summary><b>12. Service không truy cập được. Lệnh đầu tiên?</b></summary>

```bash
kubectl get endpoints <svc>
```

`<none>` → **selector không khớp labels pod**. Đây là nguyên nhân phần lớn ca "gọi Service không được".

📖 Ngày 38
</details>

<details><summary><b>13. Pod <code>Pending</code> mãi không lên. Ba nguyên nhân?</b></summary>

1. **Không node nào đủ tài nguyên** — `requests` quá lớn. Xem `kubectl describe pod` phần Events: *"Insufficient cpu/memory"*
2. **PVC chưa Bound** — không có StorageClass, hoặc ổ RWO đang bị pod khác giữ (`Multi-Attach error`)
3. **Node selector / taint** — pod đòi node có nhãn không tồn tại, hoặc mọi node đều bị taint

📖 Ngày 36, 39, 41
</details>

<details><summary><b>14. Pipeline CI xanh nhưng bản mới không lên cluster. Nguyên nhân?</b></summary>

```bash
kubectl get application -n argocd        # SYNC STATUS?
argocd app diff <app>
git -C cloudnote-config log --oneline -3 # CI đã cập nhật tag chưa?
```

Nghi ngờ nhất: CI build và đẩy image thành công nhưng **chưa cập nhật tag vào repo cấu hình** → GitOps không thấy gì đổi.

Hoặc ArgoCD đang ở chế độ sync thủ công.

📖 Ngày 43, 57
</details>

<details><summary><b>15. HPA hiện <code>&lt;unknown&gt;</code> ở cột TARGETS. Hai nguyên nhân?</b></summary>

1. **metrics-server chưa chạy** — kiểm tra bằng `kubectl top nodes`
2. **Pod chưa khai `requests.cpu`** — HPA tính % dựa trên requests, không có thì không có mẫu số

📖 Ngày 41
</details>

## Phần C — Tình huống (5 câu)

<details><summary><b>16. Production chết, bạn vừa deploy 10 phút trước. Làm gì?</b></summary>

**Quay lui ngay. Đừng debug.**

1. Đánh giá ảnh hưởng (30 giây)
2. **Rollback** — không cần biết nguyên nhân
3. Xác nhận đã khỏi
4. Thông báo
5. **Bây giờ mới** điều tra, trên staging
6. Postmortem không đổ lỗi

Nguyên tắc SRE: **khôi phục dịch vụ ưu tiên hơn tìm nguyên nhân**. Mỗi phút debug là một phút người dùng chịu thiệt.
</details>

<details><summary><b>17. Pipeline chạy 20 phút, đội bắt đầu tìm cách lách. Bạn làm gì?</b></summary>

**Đo trước, tối ưu sau** — mở từng job xem bước nào lâu nhất.

Bốn cách: cache thư viện → cache lớp Docker → chạy song song job độc lập → `concurrency` huỷ run cũ.

Và nói về văn hoá: pipeline chậm thì người ta sẽ bỏ qua nó, lúc đó bạn mất luôn tác dụng của CI. **Tốc độ pipeline là vấn đề văn hoá, không chỉ kỹ thuật.**
</details>

<details><summary><b>18. Cấp trên muốn lên Kubernetes cho hệ thống 3 dịch vụ đang chạy ổn. Bạn nói gì?</b></summary>

Hỏi trước khi đồng ý hay phản đối: vấn đề đang cần giải là gì? Ai vận hành được K8s? Chi phí vận hành thêm có xứng không?

Với 3 dịch vụ trên một máy, **Compose thường là lựa chọn đúng**.

Nhưng nếu tổ chức vẫn quyết (ví dụ vì định hướng dài hạn), đề xuất đường đi an toàn: dùng cụm do cloud quản lý, bắt đầu với dịch vụ ít rủi ro nhất, đầu tư giám sát **trước** khi chuyển production.

Người phỏng vấn muốn thấy: chọn công cụ theo bài toán, **nhưng cũng biết thực thi quyết định của tổ chức một cách an toàn**.
</details>

<details><summary><b>19. Đội muốn bật <code>selfHeal</code> của ArgoCD ngay. Bạn cảnh báo gì?</b></summary>

Ở nơi mọi người quen vá tay, bật `selfHeal` ngay sẽ gây bực bội: *"tôi vừa sửa thì nó tự đổi lại"*.

Cách làm thường thấy: bắt đầu bằng **sync thủ công** (ArgoCD chỉ *báo* khác biệt) vài tuần — để cả đội thấy có bao nhiêu thay đổi đang xảy ra ngoài Git. Khi mọi người đã quen "mọi thay đổi qua Git" rồi mới bật tự động.

Và nhắc: GitOps buộc phải xử lý bí mật tử tế trước (Sealed Secrets/SOPS), vì mọi thứ nằm trong Git.
</details>

<details><summary><b>20. Bạn phải chọn: thêm 3 cảnh báo mới, hay dọn 20 cảnh báo đang nhiễu?</b></summary>

**Dọn trước.**

Lý do: cảnh báo nhiễu gây *alert fatigue* — người ta chai lì và bỏ qua **cả cảnh báo thật**. Thêm 3 cái mới vào một hệ thống đã nhiễu thì chúng cũng bị bỏ qua.

Cách dọn: với mỗi cảnh báo hỏi *"lần cuối nó bắn, có ai làm gì không?"* Nếu không → xoá hoặc hạ cấp thành ghi log.

Rồi mới thêm cảnh báo mới, và chỉ thêm loại gắn với **thứ người dùng cảm nhận được**.
</details>

**Điểm bộ 3: ___ / 40**

---

# BỘ 4 — Giai đoạn 4: SRE & Vận hành

> Làm sau [Ngày 60](./Giai-doan-4-SRE-Capstone.md#ngày-60--tốt-nghiệp--tổng-kết-chứng-chỉ--định-hướng-sự-nghiệp)

## Phần A — Khái niệm (10 câu)

<details><summary><b>1. SLI, SLO, SLA khác nhau thế nào? Quan hệ giữa chúng?</b></summary>

- **SLI** = chỉ số **đo được** (tỉ lệ request thành công)
- **SLO** = mục tiêu **nội bộ** cho SLI (≥ 99,9% trong 30 ngày)
- **SLA** = cam kết với khách hàng, vi phạm là **đền tiền**

Quan hệ luôn là: **SLA < SLO < thực tế**. Đặt SLO chặt hơn SLA để còn thời gian xoay xở trước khi phải đền.

📖 Ngày 51
</details>

<details><summary><b>2. Vì sao SLO 100% là mục tiêu sai?</b></summary>

1. Chi phí tăng **theo cấp số nhân** mỗi lần thêm một số 9
2. Người dùng **không cảm nhận được** — mạng của họ đã kém tin cậy hơn thế
3. Nó **triệt tiêu khả năng thay đổi** — không ngân sách lỗi nghĩa là không được phát hành gì

📖 Ngày 51
</details>

<details><summary><b>3. Ngân sách lỗi giải quyết mâu thuẫn gì?</b></summary>

Đội phát triển muốn nhanh, đội vận hành muốn ổn định — trước đây cãi nhau bằng quan điểm.

Ngân sách lỗi biến nó thành **phép tính**: còn ngân sách thì phát hành; cạn thì dừng lại vá. Cả hai nhìn cùng một con số.

Nhưng chỉ có giá trị nếu tổ chức **thật sự tuân theo** — dashboard đẹp mà vẫn phát hành bất chấp thì chỉ là trang trí.

📖 Ngày 51
</details>

<details><summary><b>4. HA và DR khác nhau thế nào?</b></summary>

**HA** chống **hỏng hóc** một thành phần (3 bản sao, chết 1 còn 2).
**DR** chống **thảm hoạ** (mất sạch thì dựng lại từ sao lưu).

Có HA không miễn trừ DR: gõ nhầm lệnh xoá cả cụm, dữ liệu bị hỏng, hoặc cả region sập → mọi bản sao cùng chết.

📖 Ngày 52
</details>

<details><summary><b>5. RTO và RPO là gì? Chúng quyết định điều gì?</b></summary>

**RPO** = mất tối đa bao nhiêu **dữ liệu** (tính bằng thời gian). **RTO** = mất tối đa bao lâu để **khôi phục**.

Hai con số này quyết định **toàn bộ thiết kế và chi phí**. RPO gần 0 cần nhân bản đồng bộ — đắt hơn sao lưu theo giờ rất nhiều.

Và đây là **quyết định kinh doanh**, không phải kỹ thuật.

📖 Ngày 52
</details>

<details><summary><b>6. Ba nguồn lãng phí lớn nhất trên cloud?</b></summary>

1. **Xin quá nhiều tài nguyên** — lớn nhất và vô hình nhất
2. **Tài nguyên mồ côi** — ổ đĩa, IP tĩnh, snapshot không ai dùng
3. **Chạy khi không cần** — dev chạy 24/7

Điểm chung: **không ai cố ý lãng phí** — nó xảy ra vì không ai nhìn thấy.

📖 Ngày 53
</details>

<details><summary><b>7. Vì sao "chậm" nguy hiểm hơn "chết"?</b></summary>

Chết thì trả lỗi ngay, người gọi xử lý được. **Chậm thì giữ tài nguyên của mọi người gọi nó** — luồng cạn dần, rồi tầng trước cũng chết theo.

Và dịch vụ gây ra sập dây chuyền **không hề chết**, nó chỉ chậm.

📖 Ngày 54
</details>

<details><summary><b>8. Bốn tấm khiên chặn sập dây chuyền? Cái nào quan trọng nhất?</b></summary>

Timeout → retry có giới hạn → circuit breaker → bulkhead.

**Timeout quan trọng nhất** vì không có nó thì ba cái sau vô nghĩa — luồng vẫn bị giữ vô hạn.

Cảnh báo: phần lớn thư viện HTTP **mặc định không có timeout**.

📖 Ngày 54
</details>

<details><summary><b>9. Bốn chỉ số DORA? Phát hiện quan trọng nhất?</b></summary>

Tần suất triển khai · thời gian từ commit tới production · tỉ lệ thay đổi gây lỗi · thời gian khôi phục.

**Phát hiện quan trọng nhất:** tốc độ và ổn định **không đánh đổi nhau**. Đội đi nhanh cũng là đội ổn định nhất — vì mỗi thay đổi nhỏ hơn.

📖 Ngày 55
</details>

<details><summary><b>10. Golden path là gì? Vì sao "lát đường" tốt hơn "dựng rào"?</b></summary>

Golden path = cách làm mặc định **đã lát sẵn, đúng chuẩn, và dễ đi hơn mọi cách khác**.

Nền tảng ép buộc sẽ bị lách bằng những cách sáng tạo và tệ hơn. Làm con đường mặc định dễ đi nhất là cách duy nhất bền vững.

📖 Ngày 55
</details>

## Phần B — Gỡ lỗi (5 câu)

<details><summary><b>11. Cảnh báo bắn liên tục lúc nửa đêm nhưng sáng ra mọi thứ bình thường. Vì sao?</b></summary>

Thường do cảnh báo đặt **ngưỡng tức thời** không có `for:`. Một cú nhấp nháy 30 giây cũng đủ kích hoạt.

Sửa: thêm `for: 5m` (điều kiện phải duy trì), hoặc tốt hơn — chuyển sang **cảnh báo theo tốc độ đốt ngân sách** kiểm tra trên hai khung thời gian.

Cũng cần hỏi: cảnh báo này có gắn với thứ người dùng cảm nhận được không? Nếu không thì nên xoá.

📖 Ngày 44, 51
</details>

<details><summary><b>12. Dashboard hiện p95 tăng vọt nhưng tỉ lệ lỗi vẫn 0%. Ba nguyên nhân?</b></summary>

1. **Database chậm đi** — query không có index, hoặc bảng phình to
2. **Dịch vụ phụ thuộc chậm** — app vẫn trả về đúng, chỉ là lâu hơn
3. **Tài nguyên bão hoà** — CPU bị throttle do chạm `limits`, hoặc hết kết nối trong pool

Cách xác minh: xem `urt` trong log proxy, xem metric của database, xem có throttling không.

📖 Ngày 45, 54
</details>

<details><summary><b>13. Sao lưu chạy đều mỗi đêm nhưng khôi phục thất bại. Nguyên nhân?</b></summary>

Vì **chưa ai từng khôi phục thử**. Các khả năng: file rỗng (lệnh chạy nhưng không ghi được), thiếu bảng, hỏng do lưu trữ, hoặc mất khoá giải mã.

Phòng ngừa bắt buộc: script sao lưu có **bước tự kiểm chứng**, và **diễn tập khôi phục định kỳ** có bấm giờ.

📖 Ngày 52
</details>

<details><summary><b>14. Ansible playbook làm sập cả 20 máy cùng lúc. Sai ở đâu?</b></summary>

Thiếu **`serial`**. Mặc định Ansible chạy song song trên mọi máy — một cấu hình sai hạ toàn bộ đội máy đồng thời.

Sửa: `serial: 1` (hoặc `serial: "25%"`) + `max_fail_percentage: 0` để dừng ở máy lỗi đầu tiên.

Và handler nên dùng `reload` chứ không `restart`.

📖 [NT3](./Module-Nen-Tang-Mo-Rong.md#nt3--ansible-nâng-cao-role-vault-rolling-update--inventory-động)
</details>

<details><summary><b>15. Chứng chỉ HTTPS hết hạn dù certbot chạy thành công. Vì sao?</b></summary>

Gần như chắc chắn: **quên `nginx -s reload` sau khi gia hạn**.

Certbot đổi file chứng chỉ trên đĩa, nhưng nginx vẫn giữ bản cũ **trong bộ nhớ** cho tới khi reload.

Sửa: thêm `--deploy-hook "nginx -s reload"` vào lệnh renew. Và **vẫn phải có cảnh báo hết hạn** — cơ chế tự động cũng hỏng được.

📖 [NT2](./Module-Nen-Tang-Mo-Rong.md#nt2--web-server-production-https-load-balancing--tinh-chỉnh)
</details>

## Phần C — Tình huống (5 câu)

<details><summary><b>16. Đội muốn đặt SLO 99,99% cho hệ thống mới. Bạn nói gì?</b></summary>

Hỏi: **hiện tại đang đạt bao nhiêu?** Nếu chưa đo thì chưa nên đặt SLO.

99,99% = **4 phút chết mỗi tháng** — không đủ cho một lần khởi động lại thủ công. Nghĩa là mọi thứ phải tự động, có dự phòng đa vùng, và có người trực 24/7.

Cách đúng: đo thực tế 30 ngày, thấy đang đạt 99,7% thì đặt SLO **99,5%** (hơi thấp hơn hiện trạng), rồi siết dần.

Đặt mục tiêu ai cũng biết là không thể chỉ khiến mọi người bơ nó đi.
</details>

<details><summary><b>17. Sau sự cố, sếp hỏi "ai làm sai?". Bạn trả lời thế nào?</b></summary>

Chuyển câu hỏi sang hệ thống — nhưng không né tránh trách nhiệm:

> *"Thao tác trực tiếp là X, nhưng câu hỏi quan trọng hơn là vì sao hệ thống cho phép một thao tác đơn lẻ gây hậu quả này. Chúng ta thiếu ba rào chắn: A, B, C. Đây là kế hoạch khắc phục kèm người chịu trách nhiệm và hạn chót."*

Lý do rất thực dụng: nếu người ta sợ bị đổ lỗi, họ sẽ **giấu sai sót** — và bạn mất luôn cơ hội sửa hệ thống. Postmortem không đổ lỗi **vẫn có trách nhiệm**, chỉ là trách nhiệm gắn với *hành động khắc phục*, không gắn với *quy lỗi cá nhân*.
</details>

<details><summary><b>18. Cần cắt 30% chi phí cloud. Bạn làm gì trước?</b></summary>

**Đo trước, cắt sau.**

1. Gắn thẻ và phân rã chi phí theo đội/môi trường
2. Ba khoản dễ nhất: tài nguyên mồ côi · tắt dev ngoài giờ (~70%) · điều chỉnh đúng kích cỡ theo số đo thật
3. Sau đó mới tính tới cam kết dài hạn cho phần tải nền ổn định

**Ràng buộc:** không cắt xuống dưới ngưỡng SLO. Tiết kiệm 200 đô rồi mất một khách hàng lớn là vụ làm ăn tệ.
</details>

<details><summary><b>19. Người mới vào đội mất 3 ngày mới deploy được lần đầu. Vấn đề ở đâu?</b></summary>

Đây là chỉ số **trải nghiệm lập trình viên** — 3 ngày là quá chậm (nhóm tốt: dưới một ngày).

Chẩn đoán: ngồi cạnh họ, **ghi lại mọi chỗ họ vướng và mọi câu họ phải hỏi**. Mỗi câu hỏi là một lỗ hổng trong nền tảng hoặc tài liệu.

Khắc phục thường gặp: golden path (script sinh project chuẩn), tài liệu nằm ngay chỗ cần, và bộ lệnh thống nhất (`make help`).

Và nhớ: nếu bạn là người duy nhất trả lời được, thì **bạn là nút thắt cổ chai** — đó mới là vấn đề thật.
</details>

<details><summary><b>20. Bạn có 3 tháng để nâng độ tin cậy hệ thống. Ưu tiên gì trước?</b></summary>

Theo thứ tự — **đo trước, sửa sau**:

**Tháng 1 — Nhìn thấy:** SLI/SLO cho luồng quan trọng nhất, dashboard 4 tín hiệu vàng, cảnh báo gắn với triệu chứng người dùng. *Không sửa gì cả — chỉ để biết thực tế đang thế nào.*

**Tháng 2 — Chặn chảy máu:** tìm SPOF, kiểm chứng sao lưu bằng khôi phục thật, làm rollback nhanh và dễ, thêm timeout cho mọi lời gọi ra ngoài.

**Tháng 3 — Bền vững:** postmortem cho mọi sự cố, tự động hoá toil lớn nhất, diễn tập sự cố có kịch bản.

Lý do thứ tự này: **không đo được thì không biết sửa gì có tác dụng**. Nhảy thẳng vào "thêm HA" mà không biết hệ thống đang hỏng ở đâu là tiêu tiền vào chỗ sai.
</details>

**Điểm bộ 4: ___ / 40**

---

## 📊 Bảng tổng kết

| Bộ | Giai đoạn | Lần 1 | Lần 2 | Ngày cần ôn |
|---|---|---|---|---|
| 1 | Linux & SysOps | ___/40 | ___/40 | |
| 2 | Git, Docker & Cloud | ___/40 | ___/40 | |
| 3 | CI/CD, K8s & Monitoring | ___/40 | ___/40 | |
| 4 | SRE & Vận hành | ___/40 | ___/40 | |
| | **TỔNG** | **___/160** | **___/160** | |

> 💡 **Làm lại lần hai sau 4–6 tuần.** Chênh lệch giữa hai lần cho biết bạn đang tích luỹ hay đang quên — và đó là thông tin có ích hơn điểm số tuyệt đối.

---

## Liên kết

| File | Dùng khi |
|---|---|
| [PROGRESS.md](./PROGRESS.md) | Ghi điểm và theo dõi tiến độ |
| [GLOSSARY.md](./GLOSSARY.md) | Tra thuật ngữ khi làm quiz |
| [INTERVIEW.md](./INTERVIEW.md) | 25 câu tình huống sâu hơn |
| [PROJECTS.md](./PROJECTS.md) | Áp dụng vào dự án thật |
