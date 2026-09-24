# 🐛 TROUBLESHOOTING — Sổ tay xử lý sự cố

> Toàn bộ lỗi đã gặp trong khoá học, gom theo chủ đề. Dùng khi **đang kẹt**: tìm triệu chứng của bạn, đọc nguyên nhân, làm theo cách sửa.

**118 lỗi** · Trích tự động từ mục 🐛 Gỡ lỗi nhanh của các ngày học.

---

## 🧭 Quy trình chẩn đoán — đọc phần này TRƯỚC khi tra bảng

Tra bảng cho bạn câu trả lời nhanh. Nhưng thứ giúp bạn xử lý được lỗi **chưa từng gặp** là quy trình:

```text
1. HIỂU TRIỆU CHỨNG   Chính xác cái gì hỏng? Ai bị ảnh hưởng? Từ khi nào?
        ↓
2. KHOANH VÙNG TẦNG   Lỗi nằm ở tầng nào?
        ↓
3. THU THẬP BẰNG CHỨNG  Log, trạng thái, số đo — ĐỪNG ĐOÁN
        ↓
4. ĐẶT GIẢ THUYẾT     'Tôi nghĩ nguyên nhân là X vì Y'
        ↓
5. KIỂM CHỨNG         Chạy đúng một lệnh để xác nhận hoặc bác bỏ
        ↓
6. SỬA                Sửa nguyên nhân, không sửa triệu chứng
        ↓
7. XÁC NHẬN           Chứng minh nó đã khỏi
        ↓
8. PHÒNG TÁI DIỄN     Thêm cảnh báo / test / tài liệu
        ↓
9. GHI LẠI            Postmortem không đổ lỗi (Ngày 51)
```

### Khoanh vùng theo tầng

Đi **từ dưới lên**, mỗi tầng loại trừ một khả năng:

```text
Ứng dụng      →  log app nói gì?
Tiến trình    →  nó còn sống không? `systemctl status`, `docker ps`
Container     →  `docker logs`, `kubectl describe`
Máy chủ       →  CPU/RAM/đĩa còn không? `df -h`, `free -h`
Mạng          →  `ping IP` → `ping tên` → `nc -zv host port` → `curl -v`
DNS           →  `dig`, `nslookup`
Tường lửa     →  `refused` = dịch vụ chết · `timeout` = tường lửa chặn
Hạ tầng       →  cloud/cluster có sự cố không?
```

> 🔑 **Hai tín hiệu phải phân biệt được** (Ngày 7, 27):
> - `Connection refused` → tới được máy, nhưng **không có ai nghe** ở cổng đó
> - `Connection timed out` → gói tin **bị chặn im lặng**, thường là tường lửa

### Ba lệnh vạn năng theo nền tảng

| Nền tảng | Chuyện gì xảy ra | App nói gì | Hệ thống vừa làm gì |
|---|---|---|---|
| **Linux** | `systemctl status <dv>` | `journalctl -u <dv> -n 50` | `dmesg -T \| tail` |
| **Docker** | `docker ps -a` | `docker logs <c> --tail 50` | `docker events --since 10m` |
| **Kubernetes** | `kubectl describe pod <p>` | `kubectl logs <p> --previous` | `kubectl get events --sort-by=.lastTimestamp` |

---

## 📑 Mục lục theo chủ đề

- [Linux & hệ thống](#linux-hệ-thống) — 28 lỗi
- [Mạng & SSH](#mạng-ssh) — 16 lỗi
- [Log, lưu trữ & sao lưu](#log-lưu-trữ-sao-lưu) — 8 lỗi
- [Git & GitHub](#git-github) — 20 lỗi
- [Docker & Compose](#docker-compose) — 26 lỗi
- [Cấu hình, Nginx & Database](#cấu-hình-nginx-database) — 20 lỗi
- [Cloud & Terraform](#cloud-terraform) — 5 lỗi

---

## Linux & hệ thống

| Triệu chứng | Nguyên nhân | Cách sửa | Bài |
|---|---|---|---|
| `git: command not found` | Git chưa được cài | `sudo apt install -y git` / `sudo dnf install -y git` | [Ngày 1](./Giai-doan-1-Linux-SysOps.md#ngày-1-devops-sysops-là-gì-tổng-quan-toàn-ngành) |
| `ssh -T` báo `Permission denied (publickey)` | Chưa gắn public key lên GitHub, hoặc gắn nhầm file | Copy lại `id_ed25519.pub` (đúng file `.pub`) và thêm vào GitHub | [Ngày 1](./Giai-doan-1-Linux-SysOps.md#ngày-1-devops-sysops-là-gì-tổng-quan-toàn-ngành) |
| `Could not open a connection to your authentication agent` | ssh-agent chưa chạy | `eval "$(ssh-agent -s)"` rồi `ssh-add ~/.ssh/id_ed25519` | [Ngày 1](./Giai-doan-1-Linux-SysOps.md#ngày-1-devops-sysops-là-gì-tổng-quan-toàn-ngành) |
| `git push` vẫn hỏi username/password | Repo dùng URL `https://` thay vì SSH | Đổi remote sang SSH: `git remote set-url origin git@github.com:user/repo.git` | [Ngày 1](./Giai-doan-1-Linux-SysOps.md#ngày-1-devops-sysops-là-gì-tổng-quan-toàn-ngành) |
| Commit hiện sai tên/email | Chưa `git config` hoặc gõ sai | Chạy lại Bước 2, kiểm tra bằng `git config --global --list` | [Ngày 1](./Giai-doan-1-Linux-SysOps.md#ngày-1-devops-sysops-là-gì-tổng-quan-toàn-ngành) |
| `No such file or directory` | Gõ sai đường dẫn, hoặc đang đứng nhầm thư mục | `pwd` kiểm tra vị trí; `ls` xem tên file thật | [Ngày 2](./Giai-doan-1-Linux-SysOps.md#ngày-2-linux-cơ-bản-điều-hướng-quản-lý-file) |
| `Permission denied` | Không đủ quyền với file/thư mục đó | Xem quyền `ls -l`; cần quyền cao thì thêm `sudo` (học kỹ Ngày 4) | [Ngày 2](./Giai-doan-1-Linux-SysOps.md#ngày-2-linux-cơ-bản-điều-hướng-quản-lý-file) |
| `mkdir: cannot create ... File exists` | Thư mục đã tồn tại | Thêm `-p`: `mkdir -p` không báo lỗi nếu đã có | [Ngày 2](./Giai-doan-1-Linux-SysOps.md#ngày-2-linux-cơ-bản-điều-hướng-quản-lý-file) |
| Lỡ tay `rm` mất file | Linux không có Thùng rác | Không khôi phục được → **luôn `ls` đường dẫn trước khi `rm`**; đặt `alias rm='rm -i'` | [Ngày 2](./Giai-doan-1-Linux-SysOps.md#ngày-2-linux-cơ-bản-điều-hướng-quản-lý-file) |
| `rm -rf $DIR/` xoá nhầm cả `/` | `$DIR` rỗng → thành `rm -rf /` | Luôn `echo "$DIR"` kiểm tra trước; quote biến `"$DIR"` | [Ngày 2](./Giai-doan-1-Linux-SysOps.md#ngày-2-linux-cơ-bản-điều-hướng-quản-lý-file) |
| Dịch vụ `failed` / không lên | Lỗi cấu hình, cổng bị chiếm, thiếu quyền | `journalctl -u <dv>` đọc lý do; sửa rồi `systemctl restart` | [Ngày 3](./Giai-doan-1-Linux-SysOps.md#ngày-3-linux-quản-lý-tiến-trình-phần-mềm) |
| Dịch vụ mất sau khi reboot | Chỉ `start`, quên `enable` | `sudo systemctl enable <dv>` | [Ngày 3](./Giai-doan-1-Linux-SysOps.md#ngày-3-linux-quản-lý-tiến-trình-phần-mềm) |
| `kill <PID>` không tắt được | Tiến trình treo cứng, không nhận TERM | Bất đắc dĩ mới `kill -9 <PID>` (ép buộc, có thể mất dữ liệu) | [Ngày 3](./Giai-doan-1-Linux-SysOps.md#ngày-3-linux-quản-lý-tiến-trình-phần-mềm) |
| SSH báo `UNPROTECTED PRIVATE KEY FILE` | Quyền key quá mở | `chmod 600 ~/.ssh/id_ed25519` | [Ngày 4](./Giai-doan-1-Linux-SysOps.md#ngày-4-linux-người-dùng-nhóm-phân-quyền) |
| `Permission denied` khi chạy `./script.sh` | Thiếu quyền `x` | `chmod +x script.sh` | [Ngày 4](./Giai-doan-1-Linux-SysOps.md#ngày-4-linux-người-dùng-nhóm-phân-quyền) |
| User mới không dùng được `sudo` | Chưa thêm vào nhóm sudo/wheel, hoặc chưa đăng nhập lại | `usermod -aG sudo <user>`; đăng xuất/vào lại để áp nhóm | [Ngày 4](./Giai-doan-1-Linux-SysOps.md#ngày-4-linux-người-dùng-nhóm-phân-quyền) |
| Lỡ `usermod -G` (thiếu -a) làm mất nhóm | Ghi đè hết nhóm cũ | Thêm lại từng nhóm: `usermod -aG sudo,docker <user>` | [Ngày 4](./Giai-doan-1-Linux-SysOps.md#ngày-4-linux-người-dùng-nhóm-phân-quyền) |
| Sửa `/etc/sudoers` xong bị khoá sudo | Sai cú pháp | Luôn dùng `visudo` (nó chặn lưu file sai cú pháp) | [Ngày 4](./Giai-doan-1-Linux-SysOps.md#ngày-4-linux-người-dùng-nhóm-phân-quyền) |
| `Permission denied` | Chưa cấp quyền chạy | `chmod +x script.sh` | [Ngày 5](./Giai-doan-1-Linux-SysOps.md#ngày-5-bash-scripting-cơ-bản) |
| `command not found` khi gõ tên script | Thiếu `./` (bash không tìm ở thư mục hiện tại) | Gõ `./script.sh` | [Ngày 5](./Giai-doan-1-Linux-SysOps.md#ngày-5-bash-scripting-cơ-bản) |
| `TEN: command not found` | Viết `TEN = 'x'` có khoảng trắng | Bỏ khoảng trắng: `TEN='x'` | [Ngày 5](./Giai-doan-1-Linux-SysOps.md#ngày-5-bash-scripting-cơ-bản) |
| `[: too many arguments` | Biến rỗng/có space không quote | Quote biến: `[ "$x" = "y" ]` | [Ngày 5](./Giai-doan-1-Linux-SysOps.md#ngày-5-bash-scripting-cơ-bản) |
| `bad interpreter` | Sai shebang hoặc file có ký tự Windows (CRLF) | Kiểm tra dòng `#!/bin/bash`; `dos2unix script.sh` | [Ngày 5](./Giai-doan-1-Linux-SysOps.md#ngày-5-bash-scripting-cơ-bản) |
| Script chạy tay OK, cron thì không | Cron thiếu `$PATH`, dùng đường dẫn tương đối | Dùng đường dẫn tuyệt đối cho mọi lệnh/file | [Ngày 6](./Giai-doan-1-Linux-SysOps.md#ngày-6-bash-scripting-nâng-cao-tự-động-hóa) |
| Không biết cron có chạy không | Không ghi log | Thêm `>> /path/cron.log 2>&1` vào dòng cron | [Ngày 6](./Giai-doan-1-Linux-SysOps.md#ngày-6-bash-scripting-nâng-cao-tự-động-hóa) |
| `tar: Removing leading /` (cảnh báo) | Dùng đường dẫn tuyệt đối trong tar | Bình thường; hoặc dùng `-C <thư_mục>` rồi đường dẫn tương đối | [Ngày 6](./Giai-doan-1-Linux-SysOps.md#ngày-6-bash-scripting-nâng-cao-tự-động-hóa) |
| So sánh số báo `integer expression expected` | Biến chứa ký tự (vd còn dấu `%`) | Lọc sạch bằng `tr -d '%'` trước khi so sánh | [Ngày 6](./Giai-doan-1-Linux-SysOps.md#ngày-6-bash-scripting-nâng-cao-tự-động-hóa) |
| Cron chạy sai giờ | Nhầm thứ tự 5 trường, hoặc sai múi giờ | Nhớ `phút giờ ngày tháng thứ`; kiểm `timedatectl` | [Ngày 6](./Giai-doan-1-Linux-SysOps.md#ngày-6-bash-scripting-nâng-cao-tự-động-hóa) |

## Mạng & SSH

| Triệu chứng | Nguyên nhân | Cách sửa | Bài |
|---|---|---|---|
| Ping IP được, ping tên fail | DNS hỏng | Kiểm tra `/etc/resolv.conf`; thử `dig @1.1.1.1 <tên>` | [Ngày 7](./Giai-doan-1-Linux-SysOps.md#ngày-7-mạng-máy-tính-cho-devops-cơ-bản) |
| `Connection refused` | Cổng đóng / không có dịch vụ nghe | Dịch vụ chưa chạy — kiểm `ss -tlnp` trên máy đích | [Ngày 7](./Giai-doan-1-Linux-SysOps.md#ngày-7-mạng-máy-tính-cho-devops-cơ-bản) |
| `Connection timed out` | Firewall chặn im lặng | Kiểm firewall (Ngày 9), security group cloud | [Ngày 7](./Giai-doan-1-Linux-SysOps.md#ngày-7-mạng-máy-tính-cho-devops-cơ-bản) |
| Ping được nhưng web không vào | Dịch vụ ở cổng 80/443 chết | `curl -v`; kiểm `systemctl status nginx` | [Ngày 7](./Giai-doan-1-Linux-SysOps.md#ngày-7-mạng-máy-tính-cho-devops-cơ-bản) |
| `curl` trả 502/504 | Reverse proxy không tới được backend | Kiểm backend có chạy không (học kỹ Ngày 23) | [Ngày 7](./Giai-doan-1-Linux-SysOps.md#ngày-7-mạng-máy-tính-cho-devops-cơ-bản) |
| `Permission denied (publickey)` | Public key chưa lên server, hoặc sai key | `ssh-copy-id` lại; kiểm `~/.ssh/authorized_keys` trên server | [Ngày 8](./Giai-doan-1-Linux-SysOps.md#ngày-8-ssh-kết-nối-quản-lý-server-từ-xa) |
| `UNPROTECTED PRIVATE KEY FILE` | Quyền key quá mở | `chmod 600 ~/.ssh/id_ed25519`, `chmod 700 ~/.ssh` | [Ngày 8](./Giai-doan-1-Linux-SysOps.md#ngày-8-ssh-kết-nối-quản-lý-server-từ-xa) |
| `Connection refused` cổng 22 | Dịch vụ ssh không chạy / sai cổng | Kiểm `systemctl status ssh` trên server; đúng `-p <cổng>` | [Ngày 8](./Giai-doan-1-Linux-SysOps.md#ngày-8-ssh-kết-nối-quản-lý-server-từ-xa) |
| `Connection timed out` | Firewall / security group chặn | Mở cổng 22 (Ngày 9 / cloud security group) | [Ngày 8](./Giai-doan-1-Linux-SysOps.md#ngày-8-ssh-kết-nối-quản-lý-server-từ-xa) |
| `Host key verification failed` | Host key đổi (cài lại server / MITM) | Xác minh rồi xoá dòng cũ: `ssh-keygen -R <host>` | [Ngày 8](./Giai-doan-1-Linux-SysOps.md#ngày-8-ssh-kết-nối-quản-lý-server-từ-xa) |
| Vẫn hỏi mật khẩu dù có key | Key chưa được server chấp nhận | `ssh -v` xem nó có "offer" key không; `ssh-copy-id` lại | [Ngày 8](./Giai-doan-1-Linux-SysOps.md#ngày-8-ssh-kết-nối-quản-lý-server-từ-xa) |
| Mất SSH sau `ufw enable` | Chưa `allow 22` | (Cần console/VM) `sudo ufw allow 22`; lần sau mở cổng trước | [Ngày 9](./Giai-doan-1-Linux-SysOps.md#ngày-9-tường-lửa-bảo-mật-hardening) |
| Sửa sshd_config xong mất SSH | Sai cú pháp / cấm nhầm | Dùng phiên đang mở: `sudo sshd -t` tìm lỗi, sửa, `reload` | [Ngày 9](./Giai-doan-1-Linux-SysOps.md#ngày-9-tường-lửa-bảo-mật-hardening) |
| fail2ban không chặn gì | Chưa bật jail sshd | Tạo `/etc/fail2ban/jail.local` với `[sshd] enabled=true` | [Ngày 9](./Giai-doan-1-Linux-SysOps.md#ngày-9-tường-lửa-bảo-mật-hardening) |
| Lỡ commit secret lên Git | `.gitignore` thêm sau khi đã commit | Gỡ khỏi tracking: `git rm --cached .env`; **xoay (đổi) secret ngay** | [Ngày 9](./Giai-doan-1-Linux-SysOps.md#ngày-9-tường-lửa-bảo-mật-hardening) |
| `ufw status` báo inactive | Chưa `enable` | `sudo ufw enable` | [Ngày 9](./Giai-doan-1-Linux-SysOps.md#ngày-9-tường-lửa-bảo-mật-hardening) |

## Log, lưu trữ & sao lưu

| Triệu chứng | Nguyên nhân | Cách sửa | Bài |
|---|---|---|---|
| Đĩa đầy 100% | Log phình to không xoay | `du -sh /var/log/*` tìm file to; bật logrotate; `journalctl --vacuum-size=200M` | [Ngày 10](./Giai-doan-1-Linux-SysOps.md#ngày-10-quản-lý-log-giám-sát-hệ-thống) |
| Hết RAM, app bị kill | OOM (out of memory) | `grep -i "out of memory" /var/log/syslog`; thêm RAM/giảm tải | [Ngày 10](./Giai-doan-1-Linux-SysOps.md#ngày-10-quản-lý-log-giám-sát-hệ-thống) |
| Log không có gì bất thường mà vẫn lỗi | Nhìn nhầm mức/nguồn | Thử `-p warning`, hoặc xem log app riêng trong `/var/log/<app>/` | [Ngày 10](./Giai-doan-1-Linux-SysOps.md#ngày-10-quản-lý-log-giám-sát-hệ-thống) |
| `tar: ... Cannot open: No such file` | Sai đường dẫn nguồn | `pwd`/`ls` kiểm tra vị trí & tên | [Ngày 11](./Giai-doan-1-Linux-SysOps.md#ngày-11-lưu-trữ-backup-khôi-phục) |
| Restore ra dữ liệu DB hỏng | Đã copy file DB đang chạy | Backup DB bằng `pg_dump`/`mysqldump --single-transaction` | [Ngày 11](./Giai-doan-1-Linux-SysOps.md#ngày-11-lưu-trữ-backup-khôi-phục) |
| `rsync --delete` xoá nhầm | Sai chiều nguồn/đích | Kiểm kỹ thứ tự `nguồn/ đích/`; chạy thử với `--dry-run` trước | [Ngày 11](./Giai-doan-1-Linux-SysOps.md#ngày-11-lưu-trữ-backup-khôi-phục) |
| `sha256sum -c` báo `FAILED` | File backup bị hỏng/đổi | Backup không dùng được — tạo lại; kiểm ổ đĩa | [Ngày 11](./Giai-doan-1-Linux-SysOps.md#ngày-11-lưu-trữ-backup-khôi-phục) |
| Đĩa đầy khi backup | Backup cũ không được dọn | Retention: `find <dir> -name 'backup-*' -mtime +7 -delete` | [Ngày 11](./Giai-doan-1-Linux-SysOps.md#ngày-11-lưu-trữ-backup-khôi-phục) |

## Git & GitHub

| Triệu chứng | Nguyên nhân | Cách sửa | Bài |
|---|---|---|---|
| `Author identity unknown` khi commit | Chưa khai `user.name`/`user.email` | `git config --global user.name/.email` (Ngày 1) | [Ngày 13](./Giai-doan-2-Git-Docker-Cloud.md#ngày-13-git-cơ-bản-quản-lý-phiên-bản) |
| Lỡ `git add` file không nên | File vào staging | `git restore --staged <file>` (chưa mất thay đổi) | [Ngày 13](./Giai-doan-2-Git-Docker-Cloud.md#ngày-13-git-cơ-bản-quản-lý-phiên-bản) |
| Lỡ commit thiếu/sai message | Commit cuối chưa push | `git commit --amend` sửa lại | [Ngày 13](./Giai-doan-2-Git-Docker-Cloud.md#ngày-13-git-cơ-bản-quản-lý-phiên-bản) |
| Lỡ `git reset --hard` mất commit | Reset quá tay | `git reflog` tìm hash → `git reset --hard <hash>` | [Ngày 13](./Giai-doan-2-Git-Docker-Cloud.md#ngày-13-git-cơ-bản-quản-lý-phiên-bản) |
| Đã commit nhầm `.env` | `.gitignore` thêm sau khi commit | `git rm --cached .env`; **đổi secret ngay** | [Ngày 13](./Giai-doan-2-Git-Docker-Cloud.md#ngày-13-git-cơ-bản-quản-lý-phiên-bản) |
| `CONFLICT (content)` khi merge | 2 nhánh sửa cùng dòng | Mở file, xoá dấu `<<< === >>>`, giữ đúng, `git add` + `git commit` | [Ngày 14](./Giai-doan-2-Git-Docker-Cloud.md#ngày-14-git-branch-merge-xử-lý-conflict) |
| `git branch -d` báo `not fully merged` | Nhánh chưa merge, sợ mất việc | Merge trước; hoặc chắc chắn bỏ thì `-D` (ép xoá) | [Ngày 14](./Giai-doan-2-Git-Docker-Cloud.md#ngày-14-git-branch-merge-xử-lý-conflict) |
| Lỡ vào "detached HEAD" | `switch` tới commit hash | `git switch -c nhánh-moi` để giữ commit, hoặc `git switch main` | [Ngày 14](./Giai-doan-2-Git-Docker-Cloud.md#ngày-14-git-branch-merge-xử-lý-conflict) |
| Sửa dở, cần đổi nhánh gấp | Git chặn switch khi có thay đổi | `git stash` cất tạm → switch → `git stash pop` | [Ngày 14](./Giai-doan-2-Git-Docker-Cloud.md#ngày-14-git-branch-merge-xử-lý-conflict) |
| Merge nhầm nhánh | Chưa push | `git merge --abort` (khi đang conflict) hoặc `git reset --hard HEAD~1` | [Ngày 14](./Giai-doan-2-Git-Docker-Cloud.md#ngày-14-git-branch-merge-xử-lý-conflict) |
| `push` hỏi username/password | Remote dùng HTTPS thay SSH | `git remote set-url origin git@github.com:user/repo.git` | [Ngày 15](./Giai-doan-2-Git-Docker-Cloud.md#ngày-15-github-remote-collaboration-pull-request) |
| `Permission denied (publickey)` | SSH key chưa lên GitHub | Ôn Ngày 1/8: thêm `.pub` vào GitHub | [Ngày 15](./Giai-doan-2-Git-Docker-Cloud.md#ngày-15-github-remote-collaboration-pull-request) |
| `Updates were rejected (fetch first)` | Remote có commit bạn chưa có | `git pull` (gộp) rồi `push` lại | [Ngày 15](./Giai-doan-2-Git-Docker-Cloud.md#ngày-15-github-remote-collaboration-pull-request) |
| `push` bị chặn vào `main` | Branch protection đang bật (đúng ý!) | Mở PR thay vì push thẳng | [Ngày 15](./Giai-doan-2-Git-Docker-Cloud.md#ngày-15-github-remote-collaboration-pull-request) |
| Lỡ push secret | Lộ vĩnh viễn trong lịch sử | **Rotate secret ngay**; thêm `.gitignore`; cân nhắc `git filter-repo` | [Ngày 15](./Giai-doan-2-Git-Docker-Cloud.md#ngày-15-github-remote-collaboration-pull-request) |
| Rebase gây conflict | 2 nhánh sửa cùng chỗ | Sửa file, `git add`, `git rebase --continue`; hoặc `--abort` để huỷ | [Ngày 25](./Giai-doan-2-Git-Docker-Cloud.md#ngày-25-git-nâng-cao-rebase-tag-workflow) |
| Đồng đội phàn nàn lịch sử bị "lệch" | Rebase nhánh đã public | Không rebase nhánh chung; nếu lỡ, phối hợp `pull --rebase` | [Ngày 25](./Giai-doan-2-Git-Docker-Cloud.md#ngày-25-git-nâng-cao-rebase-tag-workflow) |
| `push` tag không lên | Chưa push tag riêng | `git push origin <tag>` hoặc `git push --tags` | [Ngày 25](./Giai-doan-2-Git-Docker-Cloud.md#ngày-25-git-nâng-cao-rebase-tag-workflow) |
| Cherry-pick trùng lặp commit | Lấy commit đã có sẵn ở nhánh | Kiểm `git log` trước; dùng `-x` để ghi nguồn | [Ngày 25](./Giai-doan-2-Git-Docker-Cloud.md#ngày-25-git-nâng-cao-rebase-tag-workflow) |
| Kẹt trong bisect | Quên reset | `git bisect reset` về trạng thái ban đầu | [Ngày 25](./Giai-doan-2-Git-Docker-Cloud.md#ngày-25-git-nâng-cao-rebase-tag-workflow) |

## Docker & Compose

| Triệu chứng | Nguyên nhân | Cách sửa | Bài |
|---|---|---|---|
| `port is already allocated` | Cổng host đã bị container khác giữ | Đổi cổng (`-p 8081:80`) hoặc `docker ps` tìm & dừng cái cũ | [Ngày 16](./Giai-doan-2-Git-Docker-Cloud.md#ngày-16-docker-khái-niệm-container-đầu-tiên) |
| Container `Exited (0)` ngay | Không có tiến trình foreground | Bình thường với ubuntu; app thật thì xem `docker logs` | [Ngày 16](./Giai-doan-2-Git-Docker-Cloud.md#ngày-16-docker-khái-niệm-container-đầu-tiên) |
| Container `Exited (1/137)` | App crash / bị kill (OOM) | `docker logs <ct>` đọc lỗi; 137 = hết RAM | [Ngày 16](./Giai-doan-2-Git-Docker-Cloud.md#ngày-16-docker-khái-niệm-container-đầu-tiên) |
| `Cannot connect to the Docker daemon` | Docker daemon chưa chạy | `sudo systemctl start docker`; Docker Desktop mở chưa | [Ngày 16](./Giai-doan-2-Git-Docker-Cloud.md#ngày-16-docker-khái-niệm-container-đầu-tiên) |
| `permission denied ... docker.sock` | User chưa trong nhóm docker | `sudo usermod -aG docker $USER` rồi đăng nhập lại | [Ngày 16](./Giai-doan-2-Git-Docker-Cloud.md#ngày-16-docker-khái-niệm-container-đầu-tiên) |
| `no space left on device` | Image/volume rác | `docker system prune -a`; `docker system df` để xem | [Ngày 16](./Giai-doan-2-Git-Docker-Cloud.md#ngày-16-docker-khái-niệm-container-đầu-tiên) |
| Mỗi lần build đều cài lại npm | `COPY . .` đặt trước `RUN npm install` | Đưa `COPY package*.json` + `RUN` lên trước `COPY . .` | [Ngày 17](./Giai-doan-2-Git-Docker-Cloud.md#ngày-17-docker-dockerfile-build-image) |
| Build gửi context rất lâu/nặng | Thiếu `.dockerignore` (gửi cả `.git`, `node_modules`) | Tạo `.dockerignore` | [Ngày 17](./Giai-doan-2-Git-Docker-Cloud.md#ngày-17-docker-dockerfile-build-image) |
| `CMD` không chạy như mong đợi | Nhầm dạng shell vs exec | Dùng dạng JSON: `CMD ["node","server.js"]` | [Ngày 17](./Giai-doan-2-Git-Docker-Cloud.md#ngày-17-docker-dockerfile-build-image) |
| App chạy nhưng `curl` không tới | Chưa `-p` map cổng, hoặc app nghe `127.0.0.1` | `-p 3000:3000`; app nên nghe `0.0.0.0` | [Ngày 17](./Giai-doan-2-Git-Docker-Cloud.md#ngày-17-docker-dockerfile-build-image) |
| Secret lộ trong image | Truyền qua `ARG`/`ENV` | Dùng BuildKit `--secret`; không nhúng secret vào layer | [Ngày 17](./Giai-doan-2-Git-Docker-Cloud.md#ngày-17-docker-dockerfile-build-image) |
| Image slim vẫn to | `.dockerignore` thiếu / copy cả `.git`, dev deps | Bổ sung `.dockerignore`; chỉ `COPY --from=build` artifact cần | [Ngày 18](./Giai-doan-2-Git-Docker-Cloud.md#ngày-18-docker-image-tối-ưu-multi-stage-build) |
| App lỗi trên alpine mà chạy trên node:20 | Alpine thiếu thư viện hệ thống (glibc) | Cài gói còn thiếu, hoặc dùng `-slim` thay `-alpine` | [Ngày 18](./Giai-doan-2-Git-Docker-Cloud.md#ngày-18-docker-image-tối-ưu-multi-stage-build) |
| `permission denied` sau khi thêm `USER node` | File thuộc root, user node không ghi được | `COPY --chown=node:node` hoặc chỉnh quyền trước | [Ngày 18](./Giai-doan-2-Git-Docker-Cloud.md#ngày-18-docker-image-tối-ưu-multi-stage-build) |
| `latest` gây lỗi bất ngờ khi deploy | Image `latest` đã đổi | Pin tag semver/SHA rõ ràng | [Ngày 18](./Giai-doan-2-Git-Docker-Cloud.md#ngày-18-docker-image-tối-ưu-multi-stage-build) |
| trivy báo nhiều CVE | Base image cũ | Cập nhật base (`node:20-alpine` mới), rebuild | [Ngày 18](./Giai-doan-2-Git-Docker-Cloud.md#ngày-18-docker-image-tối-ưu-multi-stage-build) |
| Dữ liệu DB mất sau khi tái tạo container | Quên gắn volume | `-v tên:/var/lib/postgresql/data` | [Ngày 19](./Giai-doan-2-Git-Docker-Cloud.md#ngày-19-docker-volume-network-dữ-liệu-bền-vững) |
| Container A không gọi được B bằng tên | Không cùng network, hoặc dùng default bridge | Tạo network riêng, cùng `--network`; default bridge KHÔNG có DNS theo tên | [Ngày 19](./Giai-doan-2-Git-Docker-Cloud.md#ngày-19-docker-volume-network-dữ-liệu-bền-vững) |
| `docker compose down -v` mất dữ liệu | `-v` xoá cả volume | Không dùng `-v` khi có dữ liệu thật cần giữ | [Ngày 19](./Giai-doan-2-Git-Docker-Cloud.md#ngày-19-docker-volume-network-dữ-liệu-bền-vững) |
| Bind mount không thấy file | Sai đường dẫn host / quyền | Dùng đường dẫn tuyệt đối; kiểm quyền thư mục | [Ngày 19](./Giai-doan-2-Git-Docker-Cloud.md#ngày-19-docker-volume-network-dữ-liệu-bền-vững) |
| Volume ngốn đĩa | Volume mồ côi tích tụ | `docker volume ls`, `docker volume prune` (cẩn thận) | [Ngày 19](./Giai-doan-2-Git-Docker-Cloud.md#ngày-19-docker-volume-network-dữ-liệu-bền-vững) |
| `yaml: line X: ...` | Thụt lề YAML sai (dùng tab) | Dùng **space** (2 space), `docker compose config` để kiểm | [Ngày 20](./Giai-doan-2-Git-Docker-Cloud.md#ngày-20-docker-compose-quản-lý-multi-container) |
| App connect DB lỗi lúc khởi động | `depends_on` không chờ DB sẵn sàng | Thêm `healthcheck` + `condition: service_healthy`, hoặc app tự retry | [Ngày 20](./Giai-doan-2-Git-Docker-Cloud.md#ngày-20-docker-compose-quản-lý-multi-container) |
| Biến `.env` không được thay | `.env` không cùng thư mục / sai tên | Đặt `.env` cạnh compose; kiểm bằng `docker compose config` | [Ngày 20](./Giai-doan-2-Git-Docker-Cloud.md#ngày-20-docker-compose-quản-lý-multi-container) |
| Mất dữ liệu sau `down` | Lỡ dùng `-v` | Không dùng `-v`; hoặc backup volume trước | [Ngày 20](./Giai-doan-2-Git-Docker-Cloud.md#ngày-20-docker-compose-quản-lý-multi-container) |
| Port conflict | Cổng host đã bị chiếm | Đổi `ports` sang cổng khác | [Ngày 20](./Giai-doan-2-Git-Docker-Cloud.md#ngày-20-docker-compose-quản-lý-multi-container) |

## Cấu hình, Nginx & Database

| Triệu chứng | Nguyên nhân | Cách sửa | Bài |
|---|---|---|---|
| `found character '\t'` | Dùng tab thụt lề | Đổi hết tab → space; cấu hình editor hiện whitespace | [Ngày 22](./Giai-doan-2-Git-Docker-Cloud.md#ngày-22-yaml-json-định-dạng-cấu-hình) |
| `mapping values are not allowed` | Thiếu space sau `:` hoặc thụt lề sai | `key: value` (có space); dùng `yamllint` | [Ngày 22](./Giai-doan-2-Git-Docker-Cloud.md#ngày-22-yaml-json-định-dạng-cấu-hình) |
| Giá trị `NO`/`yes`/`on` bị đổi thành boolean | Norway problem | Quote chuỗi: `"NO"` | [Ngày 22](./Giai-doan-2-Git-Docker-Cloud.md#ngày-22-yaml-json-định-dạng-cấu-hình) |
| `jq: error: Cannot index...` | Truy cập sai đường dẫn JSON | Xem cấu trúc trước: `jq '.'`; rồi đi từng cấp | [Ngày 22](./Giai-doan-2-Git-Docker-Cloud.md#ngày-22-yaml-json-định-dạng-cấu-hình) |
| Số phiên bản `3.10` thành `3.1` | YAML hiểu là số | Quote: `version: "3.10"` | [Ngày 22](./Giai-doan-2-Git-Docker-Cloud.md#ngày-22-yaml-json-định-dạng-cấu-hình) |
| Web chết sau khi sửa config | `restart` với config lỗi | Luôn `nginx -t` trước; sửa lỗi rồi `reload` | [Ngày 23](./Giai-doan-2-Git-Docker-Cloud.md#ngày-23-reverse-proxy-web-server-nginx-chuyên-sâu) |
| `502 Bad Gateway` | Backend không tới được | Kiểm backend chạy chưa (`curl` trực tiếp); đúng địa chỉ `proxy_pass` | [Ngày 23](./Giai-doan-2-Git-Docker-Cloud.md#ngày-23-reverse-proxy-web-server-nginx-chuyên-sâu) |
| `504 Gateway Timeout` | Backend phản hồi chậm/treo | Kiểm backend; tăng `proxy_read_timeout` | [Ngày 23](./Giai-doan-2-Git-Docker-Cloud.md#ngày-23-reverse-proxy-web-server-nginx-chuyên-sâu) |
| Backend log toàn 1 IP (của nginx) | Thiếu header X-Real-IP/X-Forwarded-For | Thêm `proxy_set_header` | [Ngày 23](./Giai-doan-2-Git-Docker-Cloud.md#ngày-23-reverse-proxy-web-server-nginx-chuyên-sâu) |
| `address already in use` | Cổng `listen` bị chiếm | Đổi cổng hoặc dừng dịch vụ đang giữ | [Ngày 23](./Giai-doan-2-Git-Docker-Cloud.md#ngày-23-reverse-proxy-web-server-nginx-chuyên-sâu) |
| Restore ra dữ liệu hỏng/nửa vời | Đã copy file DB thay vì dump | Dùng `pg_dump`/`mysqldump` | [Ngày 24](./Giai-doan-2-Git-Docker-Cloud.md#ngày-24-cơ-sở-dữ-liệu-cho-devops) |
| `password authentication failed` | Sai user/mật khẩu | Kiểm biến `POSTGRES_PASSWORD`, user đúng chưa | [Ngày 24](./Giai-doan-2-Git-Docker-Cloud.md#ngày-24-cơ-sở-dữ-liệu-cho-devops) |
| App connect DB `Connection refused` | DB chưa sẵn sàng / sai host | Chờ healthcheck; dùng tên service trong cùng network | [Ngày 24](./Giai-doan-2-Git-Docker-Cloud.md#ngày-24-cơ-sở-dữ-liệu-cho-devops) |
| DB bị dò từ Internet | Lỡ map cổng `-p 5432:5432` ra ngoài | Bỏ map cổng; chỉ để network nội bộ; truy cập xa qua SSH tunnel | [Ngày 24](./Giai-doan-2-Git-Docker-Cloud.md#ngày-24-cơ-sở-dữ-liệu-cho-devops) |
| Đổi schema làm vỡ app | Sửa tay trên production | Dùng migration tool, test staging trước | [Ngày 24](./Giai-doan-2-Git-Docker-Cloud.md#ngày-24-cơ-sở-dữ-liệu-cho-devops) |
| Rebase gây conflict | 2 nhánh sửa cùng chỗ | Sửa file, `git add`, `git rebase --continue`; hoặc `--abort` để huỷ | [Ngày 25](./Giai-doan-2-Git-Docker-Cloud.md#ngày-25-git-nâng-cao-rebase-tag-workflow) |
| Đồng đội phàn nàn lịch sử bị "lệch" | Rebase nhánh đã public | Không rebase nhánh chung; nếu lỡ, phối hợp `pull --rebase` | [Ngày 25](./Giai-doan-2-Git-Docker-Cloud.md#ngày-25-git-nâng-cao-rebase-tag-workflow) |
| `push` tag không lên | Chưa push tag riêng | `git push origin <tag>` hoặc `git push --tags` | [Ngày 25](./Giai-doan-2-Git-Docker-Cloud.md#ngày-25-git-nâng-cao-rebase-tag-workflow) |
| Cherry-pick trùng lặp commit | Lấy commit đã có sẵn ở nhánh | Kiểm `git log` trước; dùng `-x` để ghi nguồn | [Ngày 25](./Giai-doan-2-Git-Docker-Cloud.md#ngày-25-git-nâng-cao-rebase-tag-workflow) |
| Kẹt trong bisect | Quên reset | `git bisect reset` về trạng thái ban đầu | [Ngày 25](./Giai-doan-2-Git-Docker-Cloud.md#ngày-25-git-nâng-cao-rebase-tag-workflow) |

## Cloud & Terraform

| Triệu chứng | Nguyên nhân | Cách sửa | Bài |
|---|---|---|---|
| `No valid credential sources` | Chưa cấu hình access key | `aws configure` (không commit key) | [Ngày 29](./Giai-doan-2-Git-Docker-Cloud.md#ngày-29-infrastructure-as-code-giới-thiệu-terraform) |
| `plan` báo destroy bất ngờ | Đổi thuộc tính "force new" | Đọc kỹ plan; cân nhắc trước khi apply | [Ngày 29](./Giai-doan-2-Git-Docker-Cloud.md#ngày-29-infrastructure-as-code-giới-thiệu-terraform) |
| `Error acquiring the state lock` | Người khác/tiến trình cũ đang giữ lock | Chờ, hoặc `force-unlock` (cẩn thận) | [Ngày 29](./Giai-doan-2-Git-Docker-Cloud.md#ngày-29-infrastructure-as-code-giới-thiệu-terraform) |
| State "drift" | Ai đó sửa tay tài nguyên trên Console | Đừng sửa tay; `apply` để đưa về đúng code | [Ngày 29](./Giai-doan-2-Git-Docker-Cloud.md#ngày-29-infrastructure-as-code-giới-thiệu-terraform) |
| Lỡ commit `.tfstate` | Chứa secret | Gỡ khỏi Git, thêm `.gitignore`, chuyển remote state | [Ngày 29](./Giai-doan-2-Git-Docker-Cloud.md#ngày-29-infrastructure-as-code-giới-thiệu-terraform) |

---

## 💡 Nguyên tắc rút ra từ 60 ngày

| Nguyên tắc | Vì sao |
|---|---|
| **Đọc log trước khi đoán** | 90% lỗi đã tự nói ra nguyên nhân trong log. Đoán mò tốn thời gian hơn đọc. |
| **Đổi một thứ tại một thời điểm** | Đổi ba thứ rồi hết lỗi thì bạn không biết cái nào đã sửa — lần sau gặp lại vẫn bí. |
| **Ghi lại lệnh đã chạy** | Lúc 3 giờ sáng bạn sẽ không nhớ mình đã thử gì. Mở một file `nhat-ky-su-co.md`. |
| **Khôi phục dịch vụ trước, tìm nguyên nhân sau** | Vừa deploy xong mà hỏng → **quay lui ngay**, đừng debug trên hệ thống đang cháy (Ngày 51). |
| **Lỗi nào cũng thành một dòng ở đây** | Sổ tay này là tài sản của bạn. Gặp lỗi mới thì thêm vào. |

---

## ➕ Thêm lỗi của chính bạn

```markdown
| Triệu chứng bạn thấy | Nguyên nhân thật | Cách sửa | Ngày/dự án |
```

> 📌 File này được **sinh tự động** từ mục 🐛 của các bài học. Lỗi bạn tự gặp hãy thêm vào cuối file, dưới heading `## Lỗi của tôi` — phần đó sẽ không bị ghi đè.
