# 🎤 INTERVIEW — Ngân hàng câu hỏi phỏng vấn DevOps

> Câu hỏi thật, theo **tình huống** — không phải định nghĩa học thuộc.
> Mỗi câu có đáp án tham khảo giấu trong `<details>`: **tự trả lời trước, rồi mới mở**.

---

## 📌 Cách dùng file này

| Bước | Làm gì |
|---|---|
| 1 | Đọc câu hỏi, **nói to câu trả lời của bạn** (nói to, không nghĩ thầm — nghĩ thầm luôn thấy mình hiểu) |
| 2 | Mở đáp án, đối chiếu |
| 3 | Tự chấm: ✅ Đúng · 🟡 Đúng một phần · ❌ Chưa được |
| 4 | Mọi câu 🟡 và ❌ → quay lại đúng ngày học đó |

> 🔑 **Nguyên tắc vàng khi phỏng vấn:** với **mọi** câu hỏi, hãy dẫn về dự án bạn đã làm. Câu trả lời có ví dụ cụ thể và **con số** luôn thắng câu trả lời lý thuyết.
>
> So sánh: *"Em biết CI/CD"* với *"Dự án của em rút thời gian từ commit tới chạy thật xuống 4 phút, quay lui 45 giây"*. Người phỏng vấn nghe ra khác biệt ngay.

---

## 🐧 Linux & Hệ thống

<details>
<summary><b>1. Ổ đĩa báo đầy 100%, nhưng <code>du -sh /*</code> cộng lại chỉ ra một nửa dung lượng. Chuyện gì xảy ra?</b></summary>

**Nguyên nhân thường gặp nhất:** có tiến trình đang **giữ một file đã bị xoá**. Khi file bị `rm` nhưng tiến trình vẫn mở nó, kernel chưa giải phóng dung lượng — `du` không thấy file đó nữa, còn `df` thì vẫn tính.

```bash
lsof +L1                    # liệt kê file đã xoá nhưng còn tiến trình giữ
lsof | grep deleted
```

Cách xử lý: khởi động lại tiến trình đang giữ file (thường là một dịch vụ ghi log). **Không** cần reboot máy.

Hai khả năng khác cần loại trừ:
- **Hết inode** thay vì hết dung lượng: `df -i`. Xảy ra khi có hàng triệu file nhỏ.
- Có phân vùng được **mount đè** lên thư mục đang chứa dữ liệu — dữ liệu cũ bị che khuất nhưng vẫn chiếm chỗ.

📖 Ngày 3, 10, 11
</details>

<details>
<summary><b>2. Vì sao không nên dùng <code>chmod 777</code>, kể cả khi nó "sửa được lỗi ngay"?</b></summary>

`777` nghĩa là **mọi người dùng trên máy đều đọc, ghi và thực thi được**. Nó "sửa được lỗi" vì nó xoá bỏ mọi ràng buộc — giống như chữa cửa kẹt bằng cách tháo luôn cánh cửa.

Rủi ro thật:
- Bất kỳ tiến trình nào bị chiếm quyền đều sửa được file đó
- File thực thi `777` có thể bị thay bằng mã độc
- Nó **che giấu vấn đề thật**, thường là sai chủ sở hữu

Cách đúng: tìm xem tiến trình chạy bằng user nào, rồi `chown` cho đúng. Quyền hợp lý là `755` cho thư mục, `644` cho file thường.

📖 Ngày 4
</details>

<details>
<summary><b>3. Một dịch vụ systemd liên tục restart. Bạn điều tra thế nào?</b></summary>

Thứ tự ba lệnh:

```bash
systemctl status ten-dich-vu          # 1) trạng thái + vài dòng log cuối
journalctl -u ten-dich-vu -n 50 --no-pager   # 2) log đầy đủ
systemctl cat ten-dich-vu             # 3) file unit thật sự đang dùng
```

Nguyên nhân hay gặp: sai đường dẫn trong `ExecStart`, thiếu biến môi trường, sai quyền trên file cấu hình, hoặc cổng đã bị tiến trình khác chiếm (`ss -tlnp`).

Điểm cộng khi trả lời: nhắc tới `Restart=` và `RestartSec=` — nếu đặt `Restart=always` mà không có `RestartSec`, systemd sẽ quay vòng rất nhanh và làm log ngập.

📖 Ngày 3, 10
</details>

---

## 🌐 Mạng

<details>
<summary><b>4. Một dịch vụ nghe ở localhost nhưng không truy cập được từ máy khác. Bạn troubleshoot thế nào?</b></summary>

Đi **theo tầng**, mỗi bước loại trừ một khả năng:

```bash
# 1) Dịch vụ nghe ở đâu? Đây thường là nguyên nhân.
ss -tlnp | grep <cổng>
```

Nếu thấy `127.0.0.1:8080` thì **đó chính là vấn đề** — dịch vụ chỉ nghe trên loopback, không nhận kết nối từ ngoài. Phải sửa cấu hình app cho nghe `0.0.0.0:8080`.

Nếu nó đã nghe `0.0.0.0` mà vẫn không vào được, đi tiếp:

```bash
# 2) Máy có tới được nhau không?
ping -c3 <ip>
# 3) Cổng có mở không?
nc -zv <ip> <cổng>
# 4) Tường lửa
sudo ufw status              # trên máy
# + kiểm tra security group / firewall của cloud
```

**Đọc đúng tín hiệu lỗi:**
- `Connection refused` → tới được máy, **không ai nghe** ở cổng đó
- `Connection timed out` → gói tin **bị chặn im lặng**, gần như chắc chắn là tường lửa

📖 Ngày 7, 9, 27
</details>

<details>
<summary><b>5. Khác biệt giữa 502 và 504 khi đứng sau reverse proxy? Mỗi cái chỉ hướng điều tra nào?</b></summary>

| Mã | Nghĩa | Đi kiểm tra gì |
|---|---|---|
| **502 Bad Gateway** | Proxy **kết nối được** nhưng nhận phản hồi hỏng, hoặc backend từ chối kết nối | Backend có chạy không? Đúng cổng chưa? |
| **504 Gateway Timeout** | Proxy kết nối được nhưng **chờ quá lâu** không có trả lời | Backend chậm — query database? vòng lặp? deadlock? |

Điểm cộng: nói rõ rằng **504 nguy hiểm hơn** vì backend đang *sống nhưng chậm* — nó giữ kết nối của proxy, và nếu không có timeout hợp lý thì proxy sẽ cạn luồng và sập theo. Đó là kịch bản sập dây chuyền.

📖 Ngày 7, 23, 54
</details>

---

## 🔀 Git

<details>
<summary><b>6. Bạn vừa commit và push một file chứa mật khẩu database. Làm gì, theo thứ tự nào?</b></summary>

Thứ tự này quan trọng hơn nội dung — **làm sai thứ tự là hỏng**:

1. **Vô hiệu hoá mật khẩu đó NGAY** — đổi mật khẩu database, thu hồi token. Đây là việc đầu tiên, trước mọi thao tác Git.
2. Xoá khỏi lịch sử: `git filter-repo` hoặc BFG Repo-Cleaner. `git rm` **không đủ** — lịch sử vẫn giữ.
3. Force push, và báo cho cả đội clone lại.
4. Bật quét bí mật tự động (gitleaks trong CI) để không tái diễn.

**Lý do bước 1 phải đứng đầu:** repo public thì có bot quét GitHub liên tục, thời gian từ lúc push tới lúc bí mật bị dùng thường tính bằng **phút**. Dọn lịch sử mất vài chục phút — đến lúc đó thì đã muộn. Và ngay cả repo private cũng phải coi như đã lộ.

📖 Ngày 49
</details>

<details>
<summary><b>7. Khi nào dùng merge, khi nào dùng rebase?</b></summary>

| | Merge | Rebase |
|---|---|---|
| Lịch sử | Giữ nguyên, có commit merge | Thẳng, như thể viết tuần tự |
| Dùng cho | Nhánh đã chia sẻ, nhánh dài | Nhánh cá nhân, trước khi mở PR |
| Rủi ro | Lịch sử rối khi nhiều nhánh | **Viết lại lịch sử** |

**Quy tắc vàng:** đừng bao giờ rebase nhánh mà người khác đã pull về. Bạn viết lại lịch sử thì họ sẽ gặp xung đột rất khó gỡ.

Cách làm phổ biến: rebase nhánh của **riêng mình** lên `main` cho gọn trước khi mở PR, rồi merge PR vào `main`.

📖 Ngày 14, 25
</details>

---

## 🐳 Docker

<details>
<summary><b>8. Image của bạn nặng 1,2 GB. Làm sao giảm xuống? Kể theo thứ tự hiệu quả.</b></summary>

1. **Đổi image nền** — `node:20` (~1,1 GB) sang `node:20-alpine` (~140 MB). Một dòng, hiệu quả nhất.
2. **Multi-stage build** — tầng build cài đủ công cụ, tầng cuối chỉ chép sản phẩm sang.
3. **Bỏ thư viện chỉ dùng khi phát triển** — `npm ci --omit=dev`.
4. **`.dockerignore`** — đừng gửi `node_modules`, `.git` vào trình build.
5. **Distroless** — nhỏ nhất và an toàn nhất, nhưng **không có shell** nên không `docker exec` vào debug được. Đánh đổi có ý thức.

Chẩn đoán lớp nào nặng: `docker history <image> --human`.

Điểm cộng: nói thêm rằng image nhỏ **không chỉ để nhanh** — ít phần mềm thừa nghĩa là ít lỗ hổng bảo mật hơn.

📖 Ngày 18, 33
</details>

<details>
<summary><b>9. Vì sao không nên chạy container bằng root?</b></summary>

Container **không phải máy ảo** — nó dùng chung kernel với máy chủ. Root trong container, trong nhiều cấu hình, tương đương root ngoài máy chủ. Nếu ứng dụng bị khai thác, kẻ tấn công có bàn đạp rất mạnh để thoát ra.

Cách làm đúng:
```dockerfile
RUN addgroup -S nhom && adduser -S ungdung -G nhom
USER ungdung
```

Điểm cộng: nhắc tới các lớp phòng thủ đi kèm — `readOnlyRootFilesystem`, bỏ Linux capability không cần, và **không bao giờ** dùng `--privileged` trừ khi hiểu rõ hậu quả.

📖 Ngày 17, 33, 49
</details>

<details>
<summary><b>10. Container chết ngay sau khi khởi động. Điều tra thế nào?</b></summary>

```bash
docker ps -a                     # mã thoát là gì?
docker logs <container>          # app nói gì trước khi chết
docker inspect <container> --format '{{.State.ExitCode}} {{.State.Error}}'
```

Đọc **mã thoát**:
| Mã | Nghĩa |
|---|---|
| `0` | Thoát bình thường — thường là lệnh chạy xong rồi hết, không phải dịch vụ chạy nền |
| `1` | Lỗi ứng dụng — đọc log |
| `125` | Lỗi của chính Docker (sai tham số) |
| `126` | Lệnh không thực thi được (thiếu quyền) |
| `127` | Không tìm thấy lệnh (sai đường dẫn trong `CMD`) |
| `137` | **Bị giết do hết RAM (OOMKilled)** |

📖 Ngày 16, 17, 41
</details>

---

## ☸️ Kubernetes

<details>
<summary><b>11. Pod ở trạng thái <code>CrashLoopBackOff</code>. Điều tra theo thứ tự nào?</b></summary>

```bash
kubectl describe pod <pod>              # 1) Events ở cuối — quan trọng nhất
kubectl logs <pod> --previous           # 2) log của LẦN CHẠY TRƯỚC
kubectl get events --sort-by=.lastTimestamp | tail
```

Cờ `--previous` là chìa khoá — không có nó bạn chỉ thấy log của container mới khởi động, chưa kịp lỗi.

Nguyên nhân thường gặp:
| Dấu hiệu | Nguyên nhân |
|---|---|
| `OOMKilled`, Exit 137 | Limits RAM quá thấp |
| Lỗi ngay khi khởi động | Thiếu biến môi trường, sai ConfigMap/Secret |
| Chạy được vài giây rồi chết | **livenessProbe quá gắt** — giết pod trong lúc còn đang khởi động |
| `CreateContainerConfigError` | Tên ConfigMap/Secret sai hoặc thiếu khoá |

📖 Ngày 37, 41
</details>

<details>
<summary><b>12. Phân biệt readinessProbe và livenessProbe. Đặt nhầm thì hậu quả gì?</b></summary>

| | readiness | liveness |
|---|---|---|
| Hỏi gì | *"Nhận khách được chưa?"* | *"Còn cứu được không?"* |
| Trượt thì sao | **Rút pod khỏi Service**, pod vẫn sống | **Giết và tạo lại container** |
| `RESTARTS` | Không tăng | Tăng |

**Hậu quả khi đặt nhầm — đây là phần quan trọng nhất của câu trả lời:** nếu livenessProbe kiểm tra kết nối tới database, thì khi database chậm đi, **mọi pod cùng trượt liveness cùng lúc** → K8s giết sạch → tất cả khởi động lại đồng thời → database càng ngộp → vòng xoáy chết. Một sự cố nhỏ thành sập toàn hệ thống.

**Quy tắc:** liveness chỉ kiểm tra **chính tiến trình đó** còn sống hay không. Kiểm tra phụ thuộc bên ngoài là việc của readiness.

📖 Ngày 41
</details>

<details>
<summary><b>13. Service không truy cập được. Lệnh đầu tiên bạn chạy là gì?</b></summary>

```bash
kubectl get endpoints <ten-service>
```

Đây là lệnh chẩn đoán số một về Service. Nó trả lời: *"Service này có tìm thấy pod nào không?"*

- Thấy danh sách IP → Service ổn, vấn đề ở chỗ khác (mạng, cổng, ứng dụng)
- Thấy **`<none>`** → **selector của Service không khớp labels của pod**. Đây là nguyên nhân của phần lớn ca "gọi Service không được".

So hai bên:
```bash
kubectl get svc <svc> -o jsonpath='{.spec.selector}'
kubectl get pods --show-labels
```

📖 Ngày 38
</details>

<details>
<summary><b>14. Deployment khai 3 bản sao dùng chung một PVC kiểu ReadWriteOnce. Chuyện gì xảy ra?</b></summary>

Chỉ **một pod chạy được**; hai pod còn lại kẹt mãi ở `ContainerCreating` kèm lỗi `Multi-Attach error`.

Lý do: `ReadWriteOnce` nghĩa là ổ đĩa chỉ gắn được vào **một node** để ghi. Ba pod rơi vào ba node khác nhau thì hai pod sau không gắn được.

Cách xử lý đúng:
- App **có trạng thái** → dùng **StatefulSet**, mỗi bản một PVC riêng
- Cần nhiều pod cùng ghi một chỗ → cần ổ đĩa `ReadWriteMany` (NFS, CephFS) — ổ đĩa cloud thông thường **không** hỗ trợ
- Database → `replicas: 1` kèm `strategy: Recreate`

Điểm cộng: nhắc rằng nếu để `RollingUpdate` cho database, K8s tạo pod mới **trước khi** xoá pod cũ — và pod mới sẽ kẹt vĩnh viễn vì ổ đĩa còn bị pod cũ giữ.

📖 Ngày 39
</details>

---

## 🔄 CI/CD & GitOps

<details>
<summary><b>15. Vì sao không nên deploy bằng tag <code>latest</code>?</b></summary>

Ba hậu quả cụ thể:

1. **Không biết đang chạy gì.** Hỏi *"production đang chạy code nào?"* → không ai trả lời được.
2. **Không quay lui được.** `latest` đã bị ghi đè, bản cũ không còn tên để gọi.
3. **Không tái lập được.** Hai máy kéo `latest` ở hai thời điểm khác nhau sẽ chạy hai bản khác nhau.

Cách đúng: tag theo **SHA commit** — bất biến, truy ngược được ra đúng dòng code. Vẫn có thể thêm `latest` như bí danh tiện tay, nhưng **deploy luôn dùng tag SHA**.

Khi đó rollback chỉ là đổi một chuỗi ký tự, không cần build lại gì.

📖 Ngày 33, 34
</details>

<details>
<summary><b>16. GitOps khác CI đẩy thẳng vào cluster ở điểm cốt lõi nào?</b></summary>

**Chiều của kết nối.**

| | CI push | GitOps (pull) |
|---|---|---|
| Ai chủ động | CI ở ngoài, đẩy vào cluster | Tác nhân **trong** cluster tự kéo từ Git |
| Chìa khoá cluster | **CI phải giữ** kubeconfig | Không ai bên ngoài cần giữ |
| Sửa tay trên cluster | Tồn tại âm thầm tới lần deploy sau | **Bị phát hiện và tự hoàn tác** |
| Rollback | Chạy lại pipeline cũ | `git revert` |

Điểm cộng: chỉ ra rằng GitOps thực chất là **chính vòng điều hoà của Kubernetes, nâng lên một tầng** — thay vì so etcd với pod, nó so Git với toàn bộ cluster.

Và nói được **nhược điểm**: thêm một thành phần phải vận hành, và bí mật buộc phải xử lý tử tế (Sealed Secrets/SOPS) vì mọi thứ nằm trong Git.

📖 Ngày 43
</details>

<details>
<summary><b>17. Pipeline của đội chạy 20 phút, mọi người bắt đầu tìm cách lách. Bạn làm gì?</b></summary>

**Đo trước, tối ưu sau.** Mở từng job xem bước nào lâu nhất — đừng đoán.

Bốn cách theo hiệu quả giảm dần:
1. **Cache thư viện** — thường là khoản tiết kiệm lớn nhất
2. **Cache lớp Docker** (`cache-from: type=gha`)
3. **Chạy song song** những job không phụ thuộc nhau; chỉ dùng `needs:` khi thật sự cần
4. **Xếp bước rẻ lên trước** — lint 10 giây chặn được lỗi thì không cần chạy test 5 phút

Thêm: `concurrency` với `cancel-in-progress` để push liên tiếp không chạy chồng.

Điểm cộng khi nói về **văn hoá**: pipeline chậm thì người ta sẽ tìm cách bỏ qua nó, và lúc đó bạn mất luôn tác dụng của CI. Tốc độ pipeline là vấn đề văn hoá, không chỉ là vấn đề kỹ thuật.

📖 Ngày 32, 35
</details>

---

## 📊 Giám sát & SRE

<details>
<summary><b>18. Vì sao SLO 100% là mục tiêu sai?</b></summary>

Ba lý do, nên nói đủ cả ba:

1. **Chi phí tăng theo cấp số nhân.** Từ 99% lên 99,9% đã khó; lên 99,99% tốn gấp nhiều lần (đa vùng, tự chuyển đổi, trực 24/7).
2. **Người dùng không cảm nhận được.** Mạng của họ, điện thoại của họ đã kém tin cậy hơn 99,99% rồi.
3. **Nó triệt tiêu khả năng thay đổi.** Không có ngân sách lỗi nghĩa là **không được phép phát hành gì cả** — vì mọi thay đổi đều mang rủi ro.

Câu hỏi đúng không phải *"làm sao đạt 100%?"* mà là *"mức không hoàn hảo nào người dùng vẫn hài lòng, và ta trả nổi?"*.

Điểm cộng: giải thích **ngân sách lỗi** biến tranh cãi giữa đội phát triển và đội vận hành thành một phép tính — còn ngân sách thì phát hành thoải mái, cạn rồi thì dừng lại mà vá.

📖 Ngày 51
</details>

<details>
<summary><b>19. Vì sao nhìn p95 thay vì giá trị trung bình?</b></summary>

Trung bình **che giấu** trải nghiệm tệ. Ví dụ cụ thể:

> 100 request: 95 cái mất 50ms, 5 cái mất 10 giây.
> Trung bình ≈ 550ms — nhìn vào thì thấy "ổn".
> Nhưng có 5 khách hàng đang rất bực.

**p95 = 95% số request nhanh hơn con số này** — nó cho thấy trải nghiệm của nhóm chịu thiệt nhất, đúng nhóm sẽ bỏ đi hoặc gọi điện phàn nàn.

Điểm cộng: nhắc rằng ở quy mô lớn người ta còn nhìn **p99** và **p99.9**, vì 1% của một triệu request vẫn là mười nghìn người.

📖 Ngày 45, 51
</details>

<details>
<summary><b>20. Cardinality explosion là gì và vì sao nó làm sập Prometheus?</b></summary>

Mỗi **tổ hợp nhãn khác nhau** tạo ra một chuỗi time-series riêng, nằm trong RAM. Nếu đặt nhãn động như `user_id`, `request_id` hay đường dẫn thật (`/don-hang/12345`), thì mỗi người dùng hoặc mỗi request lại đẻ ra một chuỗi mới → hàng triệu chuỗi → Prometheus ngốn hết RAM rồi chết.

**Quy tắc:** nhãn chỉ dùng cho giá trị **hữu hạn và ít** — mã HTTP, tên service, môi trường. ID và giá trị vô hạn thuộc về **nội dung log**, không phải nhãn metric.

Điểm cộng: chỉ ra rằng đây là lỗi *phổ biến nhất* làm sập hệ thống giám sát — không phải do tải cao, mà do một dòng code thêm nhãn sai.

📖 Ngày 44, 46
</details>

---

## 🔥 Câu hỏi tình huống — phần quyết định

> Đây là nhóm câu phân biệt người *biết công cụ* với người *vận hành được hệ thống*. Đáp án đúng quan trọng ít hơn **cách bạn suy luận**.

<details>
<summary><b>21. Production đang chết. Bạn vừa deploy 10 phút trước. Làm gì?</b></summary>

**Quay lui ngay lập tức.** Đừng debug.

Thứ tự:
1. **Đánh giá ảnh hưởng** (30 giây) — bao nhiêu người dùng, chức năng nào chết
2. **Rollback** — không cần biết nguyên nhân. Khôi phục dịch vụ trước.
3. **Xác nhận đã khỏi**
4. **Thông báo** cho người liên quan
5. **Bây giờ mới điều tra** — trên môi trường staging, với bản đã bị lỗi
6. **Postmortem không đổ lỗi**

**Sai lầm kinh điển của người mới:** cố tìm nguyên nhân trong lúc hệ thống đang cháy. Mỗi phút bạn debug là một phút người dùng không dùng được. Nguyên tắc SRE: **khôi phục dịch vụ được ưu tiên hơn tìm ra nguyên nhân.**

Điểm cộng rất lớn: nói rằng *"và đó là lý do rollback phải dễ và phải được tập trước — nếu lần đầu dùng nó là lúc 2 giờ sáng thì đã muộn"*.

📖 Ngày 34, 51
</details>

<details>
<summary><b>22. Đội bạn deploy mỗi tháng một lần, mỗi lần 4 tiếng và hay hỏng. Đề xuất ba việc làm trước tiên.</b></summary>

1. **Tự động hoá phần kiểm tra (CI) + branch protection.** Bắt lỗi trong vài phút thay vì lúc đang deploy.
2. **Deploy thường xuyên hơn, mỗi lần nhỏ hơn.** Phản trực giác nhưng đây là phát hiện cốt lõi của DORA: tốc độ và ổn định **không đánh đổi nhau**. Thay đổi nhỏ thì dễ kiểm tra, dễ hiểu, dễ quay lui.
3. **Làm cho rollback nhanh và rẻ** — tag bất biến, một lệnh là về bản cũ. Khi lui rẻ, người ta hết sợ phát hành.

Điểm cộng: đề xuất **đo bốn chỉ số DORA trước** để biết mình đang ở đâu và có bằng chứng cho thấy cải thiện.

Điểm cộng nữa — nói về con người: deploy hằng tháng khiến mỗi lần trở thành một sự kiện to, căng thẳng và đáng sợ. Đó là vấn đề tâm lý tổ chức, không chỉ là vấn đề kỹ thuật.

📖 Ngày 32, 35, 55
</details>

<details>
<summary><b>23. Cấp trên muốn đưa hệ thống lên Kubernetes. Hệ thống hiện có 3 dịch vụ chạy trên một máy, hoạt động ổn định. Bạn nói gì?</b></summary>

Đây là câu kiểm tra **khả năng phản biện có cơ sở** — không phải câu kiểm tra bạn có biết K8s không.

Câu trả lời tốt: hỏi trước khi đồng ý hay phản đối.
- Vấn đề đang cần giải là gì? Không đủ tài nguyên? Cần tự phục hồi? Cần triển khai không gián đoạn?
- Đội có ai vận hành được K8s không? Ai trực khi nó hỏng?
- Chi phí vận hành thêm có xứng với lợi ích không?

Với **3 dịch vụ trên một máy**, Docker Compose thường là lựa chọn đúng. K8s bắt đầu đáng giá khi có nhiều dịch vụ, nhiều máy, và yêu cầu không gián đoạn.

Nhưng **nếu cấp trên vẫn quyết làm** (ví dụ vì định hướng dài hạn), hãy đề xuất đường đi có kiểm soát: dùng cụm K8s do cloud quản lý thay vì tự dựng, bắt đầu với một dịch vụ ít rủi ro nhất, và đầu tư vào giám sát **trước** khi chuyển production.

Cái người phỏng vấn muốn nghe: bạn **chọn công cụ theo bài toán, không theo mốt** — nhưng cũng biết cách thực thi quyết định của tổ chức một cách an toàn.

📖 Ngày 36, 53
</details>

<details>
<summary><b>24. Hoá đơn cloud tháng này tăng gấp đôi mà không ai biết vì sao. Bạn điều tra thế nào?</b></summary>

1. **Xem phân rã hoá đơn theo dịch vụ** — khoản nào tăng?
2. **Lọc theo thẻ** (`moi_truong`, `doi`, `du_an`). Nếu không gắn thẻ thì đây là bài học đầu tiên: **không gắn thẻ thì không quy trách nhiệm được**.
3. **Ba nghi phạm thường gặp:**
   - Tài nguyên mồ côi: ổ đĩa không gắn với ai, IP tĩnh không dùng, snapshot cũ
   - Môi trường dev chạy 24/7 (tắt ngoài giờ tiết kiệm ~70%)
   - Chi phí **truyền dữ liệu** — khoản gây bất ngờ nhiều nhất, nhất là truyền giữa các vùng
4. **Trường hợp nghiêm trọng:** kiểm tra có tài nguyên lạ được tạo ra không — khoá bị lộ và bị dùng để đào tiền ảo là kịch bản có thật.

Phòng ngừa: cảnh báo ngân sách theo **tốc độ tiêu** (không phải theo tổng), bắt buộc gắn thẻ, và rà soát tài nguyên mồ côi định kỳ.

📖 Ngày 26, 53
</details>

<details>
<summary><b>25. Bạn được giao một hệ thống không ai còn làm ở công ty, không có tài liệu. Bắt đầu từ đâu?</b></summary>

Thứ tự ưu tiên — **hiểu trước, sửa sau**:

1. **Đừng đụng gì trong tuần đầu.** Quan sát.
2. **Vẽ lại kiến trúc thực tế** — dịch vụ nào chạy ở đâu, gọi nhau thế nào. Bắt đầu từ `ss -tlnp` trên từng máy, hoặc `kubectl get all -A`.
3. **Tìm nơi nguy hiểm nhất:** sao lưu có chạy không, và **đã ai khôi phục thử chưa?** Đây gần như luôn là lỗ hổng lớn nhất của hệ thống bị bỏ rơi.
4. **Dựng giám sát tối thiểu** — ít nhất biết được khi nào nó chết.
5. **Viết tài liệu dần** khi tìm hiểu, đừng để cuối cùng mới viết.
6. **Đưa vào code từng phần** — đừng viết lại toàn bộ; `terraform import` thứ đang có rồi cải thiện dần.

Câu trả lời tệ là *"em sẽ viết lại toàn bộ bằng Kubernetes"*. Người phỏng vấn muốn thấy **sự thận trọng với hệ thống đang chạy** và khả năng cải thiện từng bước mà không gây gián đoạn.

📖 Ngày 48, 52
</details>

---

## 🎯 Câu bạn nên hỏi ngược lại

Phỏng vấn là hai chiều. Những câu này cho thấy bạn hiểu nghề, và giúp bạn biết có nên nhận việc không:

| Câu hỏi | Bạn đang dò điều gì |
|---|---|
| *"Từ commit tới production mất bao lâu?"* | Mức độ trưởng thành của quy trình |
| *"Đội xử lý sự cố thế nào? Có viết postmortem không?"* | Văn hoá đổ lỗi hay văn hoá học hỏi |
| *"Ai bị gọi dậy khi có sự cố ban đêm? Tần suất thế nào?"* | Chất lượng cảnh báo và mức độ kiệt sức của đội |
| *"Hạ tầng đang được quản lý bằng code bao nhiêu phần trăm?"* | Còn bao nhiêu việc thủ công |
| *"Người mới vào mất bao lâu để deploy được lần đầu?"* | Chất lượng tài liệu và nền tảng nội bộ |

---

## 📋 Bảng tự chấm

Đánh dấu sau mỗi lần luyện. Mọi câu ❌ → quay lại ngày học tương ứng.

| # | Chủ đề | Lần 1 | Lần 2 | Ngày cần ôn |
|---|---|---|---|---|
| 1–3 | Linux | | | 3, 4, 10, 11 |
| 4–5 | Mạng | | | 7, 9, 23 |
| 6–7 | Git | | | 14, 25, 49 |
| 8–10 | Docker | | | 16–18, 33 |
| 11–14 | Kubernetes | | | 37–41 |
| 15–17 | CI/CD & GitOps | | | 32–35, 43 |
| 18–20 | Giám sát & SRE | | | 44–46, 51 |
| 21–25 | Tình huống | | | 34, 51–53 |

> 🧠 **Điều quan trọng nhất:** không câu nào ở đây nên được trả lời bằng định nghĩa thuộc lòng. Mỗi câu đều nên có một câu *"ở dự án của em..."* — đó là thứ khiến người phỏng vấn tin bạn đã thật sự làm.
