# 📅 HỌC HẰNG NGÀY — Nhịp học ngày · tuần · tháng

> Biết học gì là một chuyện. **Duy trì được nhịp học** là chuyện quyết định bạn có đi hết 60 ngày hay bỏ ở ngày thứ 9.
>
> File này cho bạn ba khuôn: một buổi học, một tuần, một tháng.

---

## Sự thật khó chịu về tự học

Phần lớn người tự học DevOps **không bỏ cuộc vì nội dung khó**. Họ bỏ vì:

| Lý do bỏ cuộc | Cách file này xử lý |
|---|---|
| *"Hôm nay bận quá, mai học bù"* → không bao giờ bù | **Nhịp tối thiểu 30 phút** cho ngày bận |
| Học 6 tiếng cuối tuần rồi kiệt sức | Khuôn buổi học **90 phút có nghỉ** |
| Học xong không nhớ gì | **Ôn 5 phút đầu buổi** + nhật ký tuần |
| Không thấy mình tiến bộ | **Review tuần** + bảng tự đánh giá đo 2 lần |
| Lạc giữa hàng trăm công cụ | Mỗi buổi chỉ **một mục tiêu** |

> 🧠 **Nguyên tắc nền:** *đều thắng nhiều*. 3 buổi/tuần trong 5 tháng thắng 7 buổi/tuần trong 2 tuần rồi bỏ. Kỹ năng vận hành là thứ tích luỹ, không phải thứ nhồi.

---

## 🌅 Khuôn một buổi học (90 phút)

```text
  5'   Ôn lại        │ Mở 🎯 Đúc kết của buổi trước, tự nói lại 3 điều
 20'   Lý thuyết     │ Đọc 📘, KHÔNG gõ lệnh, chỉ hiểu
 45'   LAB           │ Gõ tay, dừng ở mỗi ✅ Checkpoint
 10'   Tự phá        │ Làm hỏng một thứ, quan sát, sửa lại
  5'   Tự chấm       │ Tick ✅ Tự chấm cuối bài
  5'   Ghi chép      │ 3 dòng vào nhật ký + commit lên GitHub
```

### Vì sao thứ tự này

| Đoạn | Vì sao đặt ở đây |
|---|---|
| **Ôn 5 phút đầu** | Nhắc lại trước khi học mới là cách chống quên rẻ nhất. Bỏ đoạn này thì tuần sau bạn không nhớ gì. |
| **Lý thuyết không gõ lệnh** | Vừa đọc vừa gõ thì không đọng lại gì cả. Hiểu trước, làm sau. |
| **Tự phá** | Đây là đoạn **quan trọng nhất** và cũng hay bị bỏ nhất. Lab chạy đúng chỉ dạy bạn quy trình; lab hỏng mới dạy bạn hệ thống. |
| **Ghi chép cuối** | 3 dòng thôi. Nhưng nó là thứ giúp bạn thấy mình đã đi được bao xa. |

### Ngày bận — nhịp tối thiểu 30 phút

Không có 90 phút thì **đừng bỏ hẳn**. Làm bản rút gọn:

```text
  5'   Ôn lại buổi trước
 20'   Đọc lý thuyết + xem LAB (chưa cần làm)
  5'   Ghi 3 dòng: hôm nay hiểu gì, mai sẽ làm LAB nào
```

> 🔑 **Giữ chuỗi ngày quan trọng hơn giữ chất lượng từng buổi.** Một buổi 30 phút vẫn nối được mạch; một ngày bỏ trắng dễ thành ba ngày, rồi thành bỏ hẳn.

### Cuối buổi — luôn commit

```bash
cd ~/devops-60-days
git add .
git commit -m "ngày 14: git branch, merge và xử lý conflict"
git push
```

Biểu đồ đóng góp trên GitHub xanh dần **chính là động lực rẻ nhất** bạn có thể tự tạo cho mình. Và sau 60 ngày, nó là bằng chứng bạn đã học thật.

---

## 📆 Khuôn một tuần

### Lịch tuần mẫu (5 buổi)

| Thứ | Nội dung | Thời lượng |
|---|---|---|
| 2 · 3 · 4 · 5 | Học ngày mới | 90 phút |
| 6 | **Buổi ôn** — làm lại LAB khó nhất tuần, không nhìn tài liệu | 60 phút |
| 7 | *(tuỳ chọn)* Thử thách tuần | 60–90 phút |
| CN | **Nghỉ** | — |

> 📌 Buổi thứ Sáu đừng bỏ. Làm lại một LAB **không nhìn hướng dẫn** là phép thử duy nhất cho biết bạn thật sự nắm hay chỉ chép được.

### Review cuối tuần (15 phút)

Chép khuôn này vào `nhat-ky/tuan-XX.md`:

```markdown
## Tuần ___ (Ngày ___ → ___)

**Đã học:**
-

**Bất ngờ nhất:**
-

**Kẹt ở đâu:**
-

**Tự gỡ được bằng cách nào:**
-

**Còn chưa hiểu (→ mang sang tuần sau):**
-

**Điểm tự đánh giá tuần này:** ___/10
```

> 💡 Mục *"Còn chưa hiểu"* là mục giá trị nhất. Nếu một điều xuất hiện ở đó **ba tuần liên tiếp**, đó là dấu hiệu bạn cần quay lại học lại hẳn phần đó, không phải cố đi tiếp.

### Thử thách tuần

Mỗi tuần một bài, làm **không nhìn tài liệu**:

| Tuần | Thử thách |
|---|---|
| 1 | Dựng máy Linux mới, siết SSH, bật tường lửa — trong 20 phút |
| 2 | Viết script sao lưu có kiểm chứng, đặt lịch chạy |
| 3 | Từ repo trống tới app chạy bằng Docker Compose — 30 phút |
| 4 | Đóng gói một app bất kỳ trên GitHub thành image dưới 150 MB |
| 5 | Dựng VM bằng Terraform, cấu hình bằng Ansible, xoá sạch |
| 6 | Pipeline CI xanh cho một repo mới — 20 phút |
| 7 | Deploy app lên K8s với probe và 3 bản sao — không nhìn tài liệu |
| 8 | Dựng Prometheus + Grafana, tạo 1 dashboard và 1 alert |
| 9 | Chọn một dịch vụ bất kỳ, viết SLO và tính ngân sách lỗi |
| 10+ | Làm [một dự án](./PROJECTS.md) |

---

## 🗓️ Khuôn một tháng

### Cuối mỗi tháng — ba việc

**1. Làm một dự án** (xem [PROJECTS.md](./PROJECTS.md))

| Sau tháng | Làm dự án |
|---|---|
| 1 | Dự án 01 — Máy chủ Linux |
| 2 | Dự án 02 — Container app |
| 3 | Dự án 04 — CI/CD |
| 4 | Dự án 05 — Observability + Capstone |

**2. Đo lại năng lực** — mở bảng tự đánh giá 16 lĩnh vực trong [PROGRESS.md](./PROGRESS.md), chấm lại từ đầu. So với tháng trước.

**3. Ôn có hệ thống** (60 phút):

```bash
# Mở GLOSSARY, che cột "Nghĩa", tự giải thích từng thuật ngữ
# Cái nào không nói được → ghi lại → quay về bài gốc
```

Rồi làm bộ [quiz tổng hợp](./QUIZ-TONG-HOP.md) của giai đoạn vừa xong.

### Review tháng

```markdown
## Tháng ___

**Đã xong:** Ngày ___ → ___ (___ ngày học)
**Dự án đã làm:** ___  · Điểm: ___/100

**Ba thứ nắm chắc nhất:**
1.
2.
3.

**Ba thứ yếu nhất (→ ưu tiên tháng sau):**
1.
2.
3.

**Điểm tự đánh giá:** ___/48  (tháng trước: ___/48)

**Điều chỉnh nhịp học:**
```

---

## 🧭 Ba chế độ học — chọn theo hoàn cảnh

### Chế độ 1 — Toàn thời gian (2 tháng)

```text
Sáng   90'  ngày mới
Chiều  60'  làm lại LAB + đọc docs chính thức của chủ đề đó
Tối    30'  ghi chép + commit
```
Phù hợp: đang thất nghiệp, nghỉ giữa hai công việc.
⚠️ **Rủi ro:** kiệt sức. Bắt buộc nghỉ trọn một ngày mỗi tuần.

### Chế độ 2 — Đi làm (3 tháng) ← phổ biến nhất

```text
Thứ 2–6   90'  buổi tối
Thứ 7     90'  ôn + thử thách tuần
Chủ nhật  nghỉ
```
Phù hợp: đang đi làm toàn thời gian.
💡 **Mẹo:** cố định **một khung giờ** và giữ nguyên. Ý chí thua thói quen; khung giờ cố định biến việc học thành phản xạ.

### Chế độ 3 — Bận (5 tháng)

```text
3 buổi/tuần × 90'
1 buổi cuối tuần ôn
```
Phù hợp: có con nhỏ, đi làm nhiều ca.
🔑 **Vẫn về đích.** 5 tháng học đều **hơn hẳn** 2 tuần học dồn rồi bỏ.

---

## 🔥 Khi mất động lực

Ai cũng có lúc này. Bốn cách xử lý, theo thứ tự nên thử:

| Tình huống | Làm gì |
|---|---|
| **Chán vì toàn lý thuyết** | Nhảy tới một [dự án](./PROJECTS.md) — làm thứ chạy được sẽ khơi lại hứng thú |
| **Kẹt một chỗ quá lâu** | Bỏ qua, đi tiếp 2–3 ngày, rồi quay lại. Nhiều thứ tự sáng ra khi có thêm ngữ cảnh |
| **Thấy mình không tiến bộ** | Mở nhật ký tuần đầu tiên và đọc lại. Bạn sẽ ngạc nhiên |
| **Quá tải, muốn bỏ** | Hạ xuống **30 phút/ngày** trong một tuần. Giữ chuỗi quan trọng hơn giữ cường độ |

> 🧠 Có một điều gần như chắc chắn: **ngày bạn muốn bỏ nhất thường là ngày trước khi mọi thứ bắt đầu ghép lại với nhau**. Giai đoạn 2 và đầu Giai đoạn 3 là lúc nhiều người bỏ nhất — cũng là ngay trước lúc các mảnh rời rạc bắt đầu thành một bức tranh.

---

## 📋 Thiết lập ban đầu (làm một lần, 10 phút)

```bash
# 1) Repo ghi chép của riêng bạn
mkdir -p ~/devops-60-days/{nhat-ky,lab,du-an}
cd ~/devops-60-days && git init -b main

# 2) File theo dõi
cat > README.md <<'EOF'
# Hành trình DevOps 60 ngày

Bắt đầu: ___
Mục tiêu: ___

## Tiến độ
- [ ] Giai đoạn 1 (Ngày 1–12)
- [ ] Giai đoạn 2 (Ngày 13–30)
- [ ] Giai đoạn 3 (Ngày 31–50)
- [ ] Giai đoạn 4 (Ngày 51–60)

## Dự án
- [ ] 01 Linux · [ ] 02 Container · [ ] 03 IaC · [ ] 04 CI/CD · [ ] 05 Observability
EOF

printf 'node_modules/\n.env\n*.pem\n*.key\nterraform.tfstate*\n.terraform/\n' > .gitignore
git add . && git commit -m "Bắt đầu hành trình DevOps 60 ngày"
```

Rồi tạo repo trên GitHub và push. **Đây là portfolio của bạn trong 60 ngày tới.**

---

## ✅ Danh sách kiểm tra mỗi buổi

Dán cái này cạnh màn hình:

```text
TRƯỚC:
  □ Mở PROGRESS.md, biết hôm nay học ngày nào
  □ Ôn 🎯 Đúc kết của buổi trước (5 phút)

TRONG:
  □ Đọc lý thuyết TRƯỚC, chưa gõ lệnh
  □ Gõ tay, không copy-paste
  □ Dừng ở mỗi ✅ Checkpoint — khớp rồi mới đi tiếp
  □ Làm phần TỰ PHÁ (đừng bỏ!)

SAU:
  □ Tick ✅ Tự chấm cuối bài
  □ Tick PROGRESS.md
  □ Ghi 3 dòng nhật ký
  □ git commit && git push
```

---

## Liên kết

| File | Dùng khi |
|---|---|
| [PROGRESS.md](./PROGRESS.md) | Tick tiến độ, bảng tự đánh giá |
| [PROJECTS.md](./PROJECTS.md) | Dự án cuối tháng |
| [QUIZ-TONG-HOP.md](./QUIZ-TONG-HOP.md) | Ôn cuối mỗi giai đoạn |
| [ROADMAP.md](./ROADMAP.md) | Khi thấy lạc, không biết đang ở đâu |
| [TROUBLESHOOTING.md](./TROUBLESHOOTING.md) | Kẹt quá 30 phút |
