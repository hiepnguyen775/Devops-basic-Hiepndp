# Giai đoạn 2 — Git, Docker & Container hóa

> **Ngày 13–30** · Quản lý mã nguồn chuyên nghiệp, đóng gói ứng dụng thành container, và lần đầu đưa app lên cloud bằng code.
>
> **Khuôn mỗi ngày:** 📘 Lý thuyết → 🧪 Lab cơ bản → 🚀 Lab nâng cao → 🧭 Hướng dẫn làm lab (lệnh → output mẫu → ✅ checkpoint → ⚠️ lỗi) → 💡 Bổ sung thực tế → 📝 Ôn tập → 🎯 Đúc kết.
>
> **Ngày Milestone (21, 30):** 📋 Đề bài → ✅ Yêu cầu → 📐 Tiêu chí chấm điểm → 🔥 Phép thử → 💬 Gợi ý khi bí. **Không hướng dẫn từng bước** — bạn tự làm và tự chấm.
>
> 💻 **Cụm Cloud (26–28) chạy miễn phí:** dùng **LocalStack** (giả lập AWS) và **Multipass** (máy ảo local dùng chính cloud-init như cloud thật) — **không cần thẻ tín dụng**. Mỗi bài đều kèm cách làm trên cloud thật khi bạn sẵn sàng.
>
> ✅ Trung lập nền tảng: ví dụ cloud dùng AWS cho cụ thể, nhưng luôn ghi chú **tương đương GCP/Azure** để bạn áp dụng cho bất kỳ nhà cung cấp nào.

---

## Mục lục

| Ngày | Chủ đề |
|------|--------|
| [13](#ngày-13--git-cơ-bản--quản-lý-phiên-bản) | Git cơ bản — Quản lý phiên bản |
| [14](#ngày-14--git-branch-merge--xử-lý-conflict) | Git — Branch, Merge & xử lý Conflict |
| [15](#ngày-15--github-remote-collaboration--pull-request) | GitHub — Remote, Collaboration & Pull Request |
| [16](#ngày-16--docker-khái-niệm--container-đầu-tiên) | Docker — Khái niệm & container đầu tiên |
| [17](#ngày-17--docker-dockerfile--build-image) | Docker — Dockerfile & Build Image |
| [18](#ngày-18--docker-image-tối-ưu--multi-stage-build) | Docker — Image tối ưu & Multi-stage Build |
| [19](#ngày-19--docker-volume-network--dữ-liệu-bền-vững) | Docker — Volume, Network & dữ liệu bền vững |
| [20](#ngày-20--docker-compose--quản-lý-multi-container) | Docker Compose — Quản lý multi-container |
| [21](#ngày-21--milestone--đóng-gói-ứng-dụng-full-stack) | **Milestone — Đóng gói ứng dụng full-stack** |
| [22](#ngày-22--yaml-json--định-dạng-cấu-hình) | YAML, JSON & định dạng cấu hình |
| [23](#ngày-23--reverse-proxy--web-server-nginx-chuyên-sâu) | Reverse Proxy & Web Server (Nginx chuyên sâu) |
| [24](#ngày-24--cơ-sở-dữ-liệu-cho-devops) | Cơ sở dữ liệu cho DevOps |
| [25](#ngày-25--git-nâng-cao--rebase-tag-workflow) | Git nâng cao — Rebase, Tag, Workflow |
| [26](#ngày-26--làm-quen-cloud--khái-niệm--free-tier) | Làm quen Cloud — Khái niệm & Free Tier |
| [27](#ngày-27--máy-chủ-cloud--tạo--quản-lý-vm) | Máy chủ Cloud — Tạo & quản lý VM |
| [28](#ngày-28--triển-khai-app-lên-cloud-docker-trên-vm) | Triển khai App lên Cloud (Docker trên VM) |
| [29](#ngày-29--infrastructure-as-code--giới-thiệu-terraform) | Infrastructure as Code — Giới thiệu Terraform |
| [30](#ngày-30--milestone--lab-tổng-hợp-giai-đoạn-2) | **Milestone — LAB tổng hợp Giai đoạn 2** |

---

## Ngày 13 — Git cơ bản & Quản lý phiên bản

> ⏱️ ~90 phút · Loại: Git
>
> 🧭 **Bạn đang ở đâu:** Giai đoạn 1 (Linux/SysOps) → **Ngày 13 (Git — cỗ máy thời gian cho code)** → Ngày 14 (branch & merge). Đây là ngày mở màn Giai đoạn 2 — Git là công cụ bạn dùng *mỗi ngày* suốt sự nghiệp, nền của mọi CI/CD sau này.
>
> ✅ **Chuẩn bị:** đã cài Git (Ngày 1) và khai báo `user.name`/`user.email`. Một thư mục trống để tập.

### 📘 Lý thuyết

#### 1. Git là gì

**Git** là hệ thống quản lý phiên bản **phân tán** (DVCS) — theo dõi mọi thay đổi của code như một "cỗ máy thời gian". Mỗi lần commit, Git chụp lại toàn bộ trạng thái dự án → quay về bất kỳ điểm nào, xem ai sửa gì, khi nào. Thay cho kiểu đặt tên `baocao_final_v2_that_su_cuoi.docx`.

#### 2. Ba trạng thái — xương sống của Git

| Vùng | Là gì | Đưa vào bằng |
|---|---|---|
| **Working Directory** | Bàn làm việc — nơi bạn sửa file | (bạn sửa file) |
| **Staging Area** | Khay "chuẩn bị đóng gói" — chọn file sẽ lưu | `git add` |
| **Repository** | Kho lịch sử — đóng dấu lưu vĩnh viễn | `git commit` |

Vòng đời: sửa file → `git add` (vào Staging) → `git commit` (vào Repo) → `git push` (lên GitHub).

#### 3. Lệnh cốt lõi

| Lệnh | Làm gì |
|---|---|
| `git init` | Biến thư mục thành repo (tạo `.git`) |
| `git status` | Xem file nào đang ở vùng nào |
| `git add <file>` / `git add .` | Đưa vào staging |
| `git commit -m 'msg'` | Lưu ảnh chụp vào lịch sử |
| `git log --oneline` | Xem lịch sử commit |
| `git diff` / `git show <commit>` | Xem khác biệt / chi tiết 1 commit |

#### 4. `.gitignore` — "đừng theo dõi cái này"

Có file không nên đưa vào Git: secret (`.env`), file rác (`*.log`), thư mục nặng (`node_modules/`). Liệt kê chúng trong `.gitignore` để Git bỏ qua.

#### 5. Quay lui (cứu vãn)

- `git restore <file>` — bỏ thay đổi chưa commit của file.
- `git restore --staged <file>` — gỡ file khỏi staging (chưa mất thay đổi).
- `git reset` / `git revert` / `git reflog` — cứu vãn ở nhiều mức (chi tiết ở 💡 Bổ sung).

**Sơ đồ — vòng đời 1 file qua 3 trạng thái Git:**
```mermaid
flowchart LR
    WD["📝 Working Directory<br/>(bạn sửa file)"] -->|"git add"| ST["📦 Staging Area<br/>(chuẩn bị commit)"]
    ST -->|"git commit"| REPO["🗄️ Repository<br/>(lịch sử local)"]
    REPO -->|"git push"| REMOTE["☁️ Remote · GitHub"]
    ST -.->|"git restore --staged"| WD
    REPO -.->|"git reset / restore"| WD
    classDef a fill:#fff3e0,stroke:#f57c00;
    classDef b fill:#e8f5e9,stroke:#2e7d32;
    class WD,ST a;
    class REPO,REMOTE b;
```

### 📖 Hiểu rõ hơn (giải thích cho người mới)

> 📘 đã mô tả 3 vùng và các lệnh. Mục này cho bạn **hình dung** để nhớ lâu — không lặp lại bảng.

**Vì sao có tận 3 vùng, không phải "lưu" một phát là xong?** Vì Git tách bạch *"tôi đã sửa gì"* và *"tôi muốn ghi lại gì"*. Staging Area (khay đóng gói) là chỗ bạn **chọn lọc**: sửa 5 file nhưng chỉ 2 file thuộc về cùng một ý nghĩa → `git add` đúng 2 file đó rồi commit riêng. Nhờ vậy mỗi commit là một "câu chuyện" gọn, chứ không phải đống hỗn độn. Người mới hay khó chịu với bước `add` tưởng như thừa, nhưng chính nó cho bạn quyền biên tập lịch sử *trước khi* đóng dấu.

**"Phân tán" (distributed) nghĩa là gì và vì sao quan trọng?** Mỗi bản `git clone` là một bản sao **đầy đủ** cả lịch sử, không phải chỉ bản mới nhất. Server GitHub sập? Bất kỳ máy nào từng clone đều dựng lại được toàn bộ. Đây là khác biệt lớn với các hệ cũ (SVN) phải luôn online mới làm việc được.

**Vì sao nên commit thường xuyên?** Commit giống một "điểm lưu game" — càng nhiều điểm lưu, càng dễ quay lui khi hỏng. Và Git gần như không đánh mất thứ đã commit: kể cả khi bạn `reset` nhầm, dấu vết vẫn còn trong `reflog`. Thứ đáng sợ là những gì *chưa* commit — thay đổi chưa lưu thì Git chẳng cứu được.

### 🧪 Lab cơ bản

> Mục tiêu: tạo repo, commit nhiều lần, dùng `.gitignore` và xem lịch sử.

**Bước 1 — Tạo repo mới.**
```bash
mkdir my-app && cd my-app
git init
git status        # "No commits yet"
```

**Bước 2 — Commit lần đầu.**
```bash
echo "# My App" > README.md
git add README.md
git commit -m "Khởi tạo dự án"
git log --oneline      # thấy 1 commit
```

**Bước 3 — Commit thêm 2 lần với thay đổi khác nhau.**
```bash
echo "console.log('hi')" > app.js
git add app.js && git commit -m "Thêm app.js"
echo "// ghi chú" >> app.js
git add app.js && git commit -m "Thêm ghi chú vào app.js"
```

**Bước 4 — Dùng `.gitignore`.**
```bash
echo "SECRET=123" > .env
printf ".env\n*.log\n" > .gitignore
git status        # .env KHÔNG xuất hiện
```

**Bước 5 — Xem lịch sử dạng đồ thị.**
```bash
git log --oneline --graph
```
Bạn sẽ thấy danh sách 3 commit theo thứ tự mới → cũ.

### 🚀 Lab nâng cao (best-practice)

> Mục tiêu: tập thói quen commit "sạch" như khi làm trong team thật.

1. **Commit nhỏ, có ý nghĩa** — mỗi commit là 1 thay đổi logic, không gộp 10 việc vào 1 commit. Dùng `git add -p` để stage **từng phần** của file:
   ```bash
   git add -p          # duyệt từng đoạn thay đổi, chọn y/n — commit có chủ đích
   ```
2. **`.gitignore` chuẩn theo ngôn ngữ** — đừng tự viết tay, lấy template chuẩn:
   ```bash
   curl -sL https://www.toptal.com/developers/gitignore/api/node,python,linux > .gitignore
   ```
3. **Viết commit message tốt** (chuẩn 50/72): dòng đầu ≤50 ký tự, mô tả "làm gì", thân commit giải thích "tại sao".
4. **Xem cấu hình & alias hữu ích:**
   ```bash
   git config --global alias.lg "log --oneline --graph --all --decorate"
   git lg              # giờ xem lịch sử đẹp bằng 1 lệnh
   ```

### 💡 Bổ sung thực tế: cứu vãn khi lỡ tay (reset vs revert vs reflog)

> Câu hỏi #1 của người mới: "Tôi lỡ commit/xóa nhầm, làm sao cứu?" — Git gần như **không bao giờ mất dữ liệu đã commit**.

```bash
# Bỏ commit cuối nhưng GIỮ thay đổi trong working dir (sửa lại rồi commit lại)
git reset --soft HEAD~1

# Bỏ thay đổi chưa commit của 1 file (cẩn thận — mất thật)
git restore file.txt

# Hoàn tác 1 commit đã PUSH mà không viết lại lịch sử (an toàn cho nhánh chung)
git revert <commit>

# "Phao cứu sinh": reflog ghi MỌI thao tác, kể cả commit đã reset/xóa
git reflog                       # tìm commit tưởng đã mất
git reset --hard <hash-từ-reflog>  # quay về đúng điểm đó
```
- **reset** = viết lại lịch sử (chỉ dùng trên nhánh **chưa push**).
- **revert** = tạo commit mới đảo ngược (dùng cho nhánh **đã chia sẻ**).
- **reflog** = sổ ghi toàn bộ — nơi tìm lại mọi thứ "tưởng đã mất".

### 🧭 Hướng dẫn làm lab & giải nghĩa lệnh (cho người tự học)

> Làm tuần tự, dừng ở mỗi ✅ **Checkpoint**.

**Bước 1 — Tạo repo và hiểu `git status`.**
```bash
mkdir my-app && cd my-app && git init
git status
```
✅ **Checkpoint:** thấy `No commits yet`.
💡 `git init` tạo thư mục ẩn `.git` — đó là "bộ não" lưu toàn bộ lịch sử.

**Bước 2 — Đi qua 3 vùng bằng mắt.**
```bash
echo "hi" > a.txt
git status                # a.txt màu đỏ (Untracked — ở Working Directory)
git add a.txt
git status                # a.txt màu xanh (Staged)
git commit -m "thêm a.txt"
git status                # working tree clean (đã vào Repository)
```
✅ **Checkpoint:** thấy file đổi trạng thái đỏ → xanh → clean.

**Bước 3 — Xác minh `.gitignore` hoạt động.**
```bash
echo "SECRET=1" > .env && printf ".env\n" > .gitignore
git status                # .env KHÔNG xuất hiện
```
✅ **Checkpoint:** `.env` bị ẩn khỏi danh sách.

**Bước 4 — Tập cứu vãn.**
```bash
echo "sai" >> a.txt
git restore a.txt         # bỏ thay đổi chưa commit
cat a.txt                 # dòng "sai" biến mất
```
✅ **Checkpoint:** file trở về trạng thái đã commit.
💡 Biết file đang ở **vùng nào** quyết định dùng lệnh cứu nào (restore/reset/revert).

### 🐛 Gỡ lỗi nhanh

**🔧 Phao cứu sinh:** `git reflog` ghi MỌI thao tác — commit tưởng đã mất thường tìm lại được. Git gần như không mất thứ đã commit.

| Triệu chứng | Nguyên nhân | Cách sửa |
|---|---|---|
| `Author identity unknown` khi commit | Chưa khai `user.name`/`user.email` | `git config --global user.name/.email` (Ngày 1) |
| Lỡ `git add` file không nên | File vào staging | `git restore --staged <file>` (chưa mất thay đổi) |
| Lỡ commit thiếu/sai message | Commit cuối chưa push | `git commit --amend` sửa lại |
| Lỡ `git reset --hard` mất commit | Reset quá tay | `git reflog` tìm hash → `git reset --hard <hash>` |
| Đã commit nhầm `.env` | `.gitignore` thêm sau khi commit | `git rm --cached .env`; **đổi secret ngay** |

### 📝 Bài ôn tập & Demo đối chiếu

**✍️ Tự kiểm tra:**

<details>
<summary>1. Mô tả vòng đời 1 file qua 3 trạng thái Git.</summary>

> Sửa file (Working Directory) → `git add` (Staging Area) → `git commit` (Repository) → `git push` (Remote/GitHub).
</details>

<details>
<summary>2. Vì sao cần `.gitignore`? Cho 3 ví dụ.</summary>

> Để không đưa file không nên vào Git: `.env` (secret), `*.log` (rác), `node_modules/` (nặng, tái tạo được).
</details>

<details>
<summary>3. `git add` và `git commit` khác nhau thế nào?</summary>

> `git add` đưa file vào **staging** (chọn cái sẽ lưu). `git commit` mới thực sự **lưu** ảnh chụp vào lịch sử.
</details>

<details>
<summary>4. Lỡ `git reset --hard` mất commit, cứu bằng gì?</summary>

> `git reflog` để tìm hash của commit đã mất, rồi `git reset --hard <hash>` quay về.
</details>

**🔬 Demo đối chiếu:**

| Demo đối chiếu | Kết quả mong đợi |
|---|---|
| `git log` sau commit đầu | Hiện commit với message của bạn |
| `git status` (sau commit) | `working tree clean` |
| `git status` (có `.gitignore`) | `.env` không xuất hiện |

### 📚 Thuật ngữ Anh–Việt (ngày này)

| Thuật ngữ | Nghĩa |
|---|---|
| **Repository (repo)** | Kho chứa code + lịch sử |
| **Commit** | Một ảnh chụp trạng thái được lưu |
| **Staging area** | Khu vực chuẩn bị file cho commit |
| **Working directory** | Thư mục làm việc — nơi sửa file |
| **`.gitignore`** | Danh sách file Git bỏ qua |
| **HEAD** | Con trỏ "đang ở commit nào" |
| **reflog** | Sổ ghi mọi thao tác — nơi cứu commit mất |

### 🎯 Đúc kết Ngày 13

**3 điều phải mang theo:**
1. **3 vùng:** Working (sửa) → Staging (`git add`, chọn lọc) → Repository (`git commit`, đóng dấu). Staging cho bạn commit gọn, có ý nghĩa.
2. **`.gitignore` trước, commit sau:** secret (`.env`), rác (`*.log`), thư mục nặng (`node_modules/`) không bao giờ vào Git.
3. **Cứu vãn theo vùng:** `restore` (bỏ sửa), `restore --staged` (gỡ khỏi staging), `reset`/`revert`/`reflog` (mức repo). Biết file đang ở vùng nào là biết dùng lệnh nào.

> 🧠 **Một câu để nhớ:** Git gần như **không bao giờ mất thứ đã commit** — kể cả khi tưởng đã xóa, `git reflog` thường tìm lại được. Nên cứ mạnh dạn commit thường xuyên.

**✅ Tự chấm** *(đánh dấu khi làm được mà không nhìn tài liệu):*
- [ ] Mô tả vòng đời 1 file qua 3 vùng bằng lời của mình
- [ ] Tạo repo, commit ≥3 lần, xem lịch sử bằng `git log --oneline`
- [ ] Dùng `.gitignore` để giấu `.env` khỏi `git status`
- [ ] Dùng `git restore` bỏ thay đổi chưa commit
- [ ] Giải thích `reflog` cứu commit "đã mất" như thế nào

✅ **Kết quả đạt được:** Quản lý phiên bản code cục bộ thành thạo với Git (3 vùng, commit, gitignore, cứu vãn).

---

## Ngày 14 — Git: Branch, Merge & xử lý Conflict

> ⏱️ ~90 phút · Loại: Git
>
> 🧭 **Bạn đang ở đâu:** Ngày 13 (Git cơ bản) → **Ngày 14 (nhánh, merge, xử lý xung đột)** → Ngày 15 (GitHub & Pull Request). Nhánh là cách cả team làm chung 1 dự án mà không giẫm chân nhau — kỹ năng cộng tác cốt lõi.
>
> ✅ **Chuẩn bị:** một repo Git đã có vài commit (từ Ngày 13).

### 📘 Lý thuyết

#### 1. Branch (nhánh) — "vũ trụ song song" của code

Muốn thử tính năng mới nhưng sợ hỏng code đang chạy? Tạo một **nhánh** — bản sao song song để thử thoải mái. Hỏng thì vứt nhánh; ổn thì **merge** (gộp) về nhánh chính (`main`). Nhánh chỉ là 1 con trỏ tới commit → tạo/xoá cực rẻ, đừng ngại tạo.

| Lệnh | Làm gì |
|---|---|
| `git branch` | Liệt kê nhánh (dấu `*` = đang ở) |
| `git switch -c <tên>` | Tạo + chuyển sang nhánh mới |
| `git switch <tên>` | Chuyển nhánh |
| `git branch -d <tên>` | Xoá nhánh (đã merge); `-D` = ép xoá |

#### 2. Merge — hợp nhất nhánh

`git merge <nhánh>` gộp `<nhánh>` vào nhánh hiện tại. Hai kiểu:
- **Fast-forward:** main không đổi từ khi tách → chỉ "dời con trỏ" tới, lịch sử thẳng.
- **3-way merge:** cả hai nhánh đều có commit mới → Git tạo 1 "merge commit" gộp lại.

#### 3. Conflict (xung đột) — nghe sợ nhưng đơn giản

Khi 2 nhánh sửa **cùng một dòng**, Git không biết giữ bản nào → nhờ bạn quyết. Nó đánh dấu trong file:
```
<<<<<<< HEAD
dòng của bạn (nhánh hiện tại)
=======
dòng của họ (nhánh đang merge vào)
>>>>>>> feature-x
```
Bạn xoá các dấu, giữ lại đoạn đúng, rồi `git add` + `git commit`. Xong.

#### 4. `git stash` — cất tạm

Đang sửa dở mà cần chuyển nhánh gấp? `git stash` cất thay đổi vào "ngăn kéo", chuyển nhánh xong `git stash pop` lấy lại.

#### 5. Workflow feature branch

Mỗi tính năng 1 nhánh (`feature/login`), làm xong merge về `main` (qua review — học ở Ngày 15). **Quy tắc vàng:** nhánh sống *càng ngắn càng tốt* — nhánh để cả tháng = conflict khủng khiếp khi merge.

### 📖 Hiểu rõ hơn (giải thích cho người mới)

> 📘 đã có bảng lệnh và cách xử lý conflict. Mục này giúp bạn **hình dung** để bớt sợ.

**Nhánh rẻ đến mức nào?** Trong Git, nhánh chỉ là một *con trỏ* trỏ tới một commit — tạo nhánh không copy file, không tốn dung lượng. Vì vậy đừng tiếc: mỗi ý tưởng, mỗi thử nghiệm một nhánh riêng. Hỏng thì xoá con trỏ, `main` không hề hấn gì. Tư duy này khác hẳn kiểu "sao lưu cả thư mục ra chỗ khác cho chắc".

**Conflict không phải lỗi — là Git lịch sự hỏi ý bạn.** Khi hai nhánh sửa *cùng một dòng*, Git đủ thông minh để biết nó **không được tự quyết** thay bạn, nên nó dừng lại, đánh dấu cả hai phiên bản và giao quyền quyết định. Bạn chỉ cần đọc, giữ đoạn đúng, xoá mấy dấu `<<<`/`===`/`>>>`, rồi commit. Càng luyện tạo conflict giả để tự giải, cảm giác sợ càng biến mất.

**Vì sao nhánh nên "sống ngắn"?** `main` liên tục tiến lên. Nhánh của bạn đứng yên càng lâu thì càng "trôi" xa khỏi `main` → lúc merge càng nhiều điểm đụng nhau. Nhánh 2 giờ merge êm ru; nhánh 2 tuần là cả buổi chiều vật lộn với conflict.

### 🧪 Lab cơ bản

> Mục tiêu: tạo nhánh, merge, và **cố tình tạo conflict rồi tự giải quyết** để hết sợ.

**Bước 1 — Tạo nhánh feature và commit.**
```bash
git switch -c feature-login
echo "login()" > login.js
git add login.js && git commit -m "Thêm login"
git branch          # thấy * feature-login
```

**Bước 2 — Merge về main.**
```bash
git switch main
git merge feature-login
git log --oneline --graph
```

**Bước 3 — Cố tình tạo conflict để tập xử lý.**
```bash
git switch -c feature-a && echo "màu XANH" > style.txt && git commit -am "xanh"
git switch main && echo "màu ĐỎ" > style.txt && git commit -am "đỏ"
git merge feature-a       # → CONFLICT ở style.txt
```
Mở `style.txt`, xoá các dấu `<<<<<<<`, `=======`, `>>>>>>>`, giữ dòng bạn muốn, rồi:
```bash
git add style.txt && git commit -m "Giải quyết conflict style"
```

**Bước 4 — Tập `git stash`.**
```bash
echo "đang dở" >> login.js
git stash              # cất tạm
git switch feature-login
git switch main
git stash pop          # lấy lại thay đổi
```

**Bước 5 — Dọn nhánh đã merge.**
```bash
git branch -d feature-login feature-a
git branch             # danh sách gọn lại
```

### 🚀 Lab nâng cao (best-practice)

> Mục tiêu: làm việc với nhánh như trong team, hạn chế conflict và merge sạch.

1. **Đặt tên nhánh có quy ước:** `feature/login`, `fix/null-pointer`, `chore/update-deps` — đọc là biết mục đích.
2. **Cập nhật nhánh trước khi merge** để giảm conflict:
   ```bash
   git switch feature/login
   git fetch origin
   git rebase origin/main      # đưa feature lên trên main mới nhất
   ```
3. **Dùng merge tool khi conflict phức tạp:**
   ```bash
   git config --global merge.tool vimdiff   # hoặc VS Code: code --wait
   git mergetool
   ```
4. **`git stash` có tên** khi cất nhiều thứ:
   ```bash
   git stash push -m "đang dở phần validate form"
   git stash list; git stash apply stash@{0}
   ```

### 💡 Bổ sung thực tế: hiểu HEAD, detached HEAD & chiến lược nhánh

- **HEAD** là con trỏ "bạn đang ở đâu". `git switch <commit-hash>` đưa bạn vào trạng thái **detached HEAD** (không trên nhánh nào) — commit ở đây sẽ mất nếu không tạo nhánh. Cách thoát: `git switch -c nhánh-mới`.
- **3 chiến lược nhánh phổ biến** (sẽ chọn ở Ngày 25):
  | Chiến lược | Phù hợp |
  |---|---|
  | **GitHub Flow** | nhánh ngắn từ main, deploy liên tục — đa số dự án web |
  | **Git Flow** | có develop/release/hotfix — sản phẩm có nhiều phiên bản |
  | **Trunk-based** | commit thẳng main + feature flag — team CI/CD trưởng thành |
- **Quy tắc vàng giảm đau:** nhánh sống **càng ngắn càng tốt**. Nhánh tồn tại 2 tuần = hội conflict khủng khiếp khi merge.

### 🧭 Hướng dẫn làm lab & giải nghĩa lệnh (cho người tự học)

> Làm tuần tự, dừng ở mỗi ✅ **Checkpoint**. Trọng tâm: hết sợ conflict.

**Bước 1 — Tạo & chuyển nhánh.**
```bash
git switch -c feature-login
git branch
```
✅ **Checkpoint:** dấu `*` nằm ở `feature-login`.

**Bước 2 — Merge và xem đồ thị.**
```bash
git switch main && git merge feature-login
git log --oneline --graph
```
✅ **Checkpoint:** lịch sử cho thấy nhánh đã hợp nhất vào main.

**Bước 3 — Trải nghiệm giải quyết conflict.** (làm theo Lab Bước 3)
```bash
git status        # sau khi merge conflict: "Unmerged paths: style.txt"
# sửa file, xoá dấu <<< === >>>
git add style.txt && git commit
git status        # "working tree clean"
```
✅ **Checkpoint:** sau khi sửa + add + commit → `working tree clean`.
💡 Conflict không đáng sợ — chỉ là Git hỏi "giữ phần nào". Bạn quyết, xoá dấu, commit.

**Bước 4 — Hiểu HEAD & detached HEAD.**
```bash
git switch <một-commit-hash>     # vào detached HEAD
git switch main                  # quay lại nhánh
```
✅ **Checkpoint:** hiểu commit tạo ở detached HEAD sẽ mất nếu không `git switch -c` tạo nhánh.

### 🐛 Gỡ lỗi nhanh

| Triệu chứng | Nguyên nhân | Cách sửa |
|---|---|---|
| `CONFLICT (content)` khi merge | 2 nhánh sửa cùng dòng | Mở file, xoá dấu `<<< === >>>`, giữ đúng, `git add` + `git commit` |
| `git branch -d` báo `not fully merged` | Nhánh chưa merge, sợ mất việc | Merge trước; hoặc chắc chắn bỏ thì `-D` (ép xoá) |
| Lỡ vào "detached HEAD" | `switch` tới commit hash | `git switch -c nhánh-moi` để giữ commit, hoặc `git switch main` |
| Sửa dở, cần đổi nhánh gấp | Git chặn switch khi có thay đổi | `git stash` cất tạm → switch → `git stash pop` |
| Merge nhầm nhánh | Chưa push | `git merge --abort` (khi đang conflict) hoặc `git reset --hard HEAD~1` |

### 📝 Bài ôn tập & Demo đối chiếu

**✍️ Tự kiểm tra:**

<details>
<summary>1. Viết chuỗi lệnh: tạo nhánh hotfix, sửa, merge vào main.</summary>

> `git switch -c hotfix` → sửa file → `git commit -am "fix"` → `git switch main` → `git merge hotfix`.
</details>

<details>
<summary>2. Các dấu `<<<<<<<` `=======` `>>>>>>>` khi conflict nghĩa là gì?</summary>

> `<<<<<<< HEAD` đến `=======` là phần của nhánh hiện tại; `=======` đến `>>>>>>>` là phần của nhánh đang merge vào. Xoá dấu, giữ đoạn đúng.
</details>

<details>
<summary>3. `git stash` dùng khi nào?</summary>

> Khi đang sửa dở (chưa muốn commit) mà cần chuyển nhánh gấp. Cất tạm bằng `stash`, xong việc `stash pop` lấy lại.
</details>

<details>
<summary>4. Vì sao nên giữ nhánh sống ngắn?</summary>

> Nhánh càng lâu, càng khác main nhiều → merge càng dễ conflict lớn. Làm xong tính năng merge ngay.
</details>

**🔬 Demo đối chiếu:**

| Demo đối chiếu | Kết quả mong đợi |
|---|---|
| Tạo & chuyển nhánh | `git branch` hiện `* feature/...` |
| Merge vào main | `git log --graph` thấy nhánh đã hợp nhất |
| Giải quyết conflict | Sau khi sửa, `git status` → all conflicts fixed |

### 📚 Thuật ngữ Anh–Việt (ngày này)

| Thuật ngữ | Nghĩa |
|---|---|
| **Branch** | Nhánh — dòng phát triển song song |
| **Merge** | Hợp nhất nhánh này vào nhánh kia |
| **Conflict** | Xung đột khi 2 nhánh sửa cùng dòng |
| **Fast-forward** | Merge chỉ dời con trỏ (lịch sử thẳng) |
| **stash** | Cất tạm thay đổi chưa commit |
| **Detached HEAD** | Đang ở 1 commit, không trên nhánh nào |
| **Feature branch** | Nhánh riêng cho mỗi tính năng |

### 🎯 Đúc kết Ngày 14

**3 điều phải mang theo:**
1. **Nhánh chỉ là con trỏ** → tạo/xoá cực rẻ. Mỗi tính năng một nhánh (`feature/...`), `main` luôn sạch.
2. **Conflict = Git hỏi "giữ phần nào"**: xoá dấu `<<< === >>>`, giữ đoạn đúng, `git add` + `git commit`. Hết.
3. **`git stash`** cất tạm khi cần đổi nhánh gấp mà chưa muốn commit; **`merge --abort`** huỷ merge đang conflict.

> 🧠 **Một câu để nhớ:** nhánh sống **càng ngắn càng tốt**. Nhánh để cả tháng = hội conflict khủng khiếp khi merge. Làm xong tính năng → merge ngay.

**✅ Tự chấm** *(đánh dấu khi làm được mà không nhìn tài liệu):*
- [ ] Tạo nhánh, commit, merge về `main` và đọc được `git log --graph`
- [ ] Cố tình tạo 1 conflict rồi tự giải quyết trọn vẹn
- [ ] Dùng `git stash` / `stash pop` để đổi nhánh giữa chừng
- [ ] Phân biệt fast-forward và 3-way merge
- [ ] Nói được vì sao không nên để nhánh sống quá lâu

✅ **Kết quả đạt được:** Làm việc với nhánh, merge và xử lý conflict tự tin — kỹ năng cộng tác thiết yếu.

---

## Ngày 15 — GitHub: Remote, Collaboration & Pull Request

> ⏱️ ~90 phút · Loại: Git
>
> 🧭 **Bạn đang ở đâu:** Ngày 14 (branch/merge cục bộ) → **Ngày 15 (đưa code lên mây + cộng tác qua Pull Request)** → Ngày 16 (Docker). Đây là quy trình team thật — và chính là cái bạn sẽ *tự động hoá* bằng CI/CD ở Giai đoạn 3.
>
> ✅ **Chuẩn bị:** repo `my-app` local (Ngày 13), tài khoản GitHub + SSH key kết nối được (Ngày 1/8).

### 📘 Lý thuyết

#### 1. Git vs GitHub — đừng nhầm

- **Git** = công cụ chạy trên máy bạn, quản lý lịch sử code (offline vẫn dùng).
- **GitHub** = dịch vụ web *lưu trữ* repo Git trên mây + tính năng cộng tác (PR, issue, CI/CD).
- Ví von: Git là Word, GitHub là Google Docs (lưu online + chia sẻ).

#### 2. Remote — kết nối repo local với GitHub

| Lệnh | Làm gì |
|---|---|
| `git remote add origin <url>` | Gắn repo local với repo GitHub (`origin` = biệt danh mặc định) |
| `git push -u origin main` | Đẩy commit lên, `-u` để nhớ liên kết |
| `git pull` | Kéo thay đổi về (= `fetch` tải về + `merge` gộp) |
| `git fetch` | Chỉ tải về, KHÔNG gộp (an toàn để xem trước) |
| `git clone <url>` | Sao chép repo về máy |

#### 3. Pull Request (PR) — trái tim của cộng tác

Thay vì sửa thẳng nhánh chính, bạn mở một **PR** = *"đề nghị gộp nhánh của tôi vào main, mọi người xem giúp"*. Người khác **review** (comment, yêu cầu sửa, approve) → rồi mới merge. Đây là cách team đảm bảo chất lượng code.

#### 4. GitHub flow — quy trình chuẩn

```
branch → commit → push → mở PR → review → merge → xoá nhánh
```

#### 5. Công cụ hỗ trợ cộng tác

- **Issue**: phiếu ghi việc/bug/tính năng, gắn label để phân loại.
- **README.md**: "bộ mặt" repo (viết bằng Markdown) — mô tả, cách cài, cách chạy.
- **Fork**: sao chép repo người khác về tài khoản mình để đóng góp (open-source).

> 🔑 Lỡ đẩy secret lên GitHub = coi như **lộ vĩnh viễn** (còn trong lịch sử/cache). Việc cần làm không phải xoá commit, mà **đổi (rotate) secret đó ngay**.

### 📖 Hiểu rõ hơn (giải thích cho người mới)

> 📘 đã phân biệt Git/GitHub và liệt kê lệnh remote. Mục này cho bạn **góc nhìn** để nhớ.

**Git vẫn chạy tốt khi mất mạng — GitHub thì không.** Đây là mấu chốt hay nhầm: commit, branch, merge, xem lịch sử... đều là việc *local*, không cần Internet. GitHub chỉ vào cuộc khi bạn `push`/`pull` — tức là **đồng bộ và chia sẻ**. Nói cách khác, GitHub chỉ là *một* remote (điểm hẹn chung trên mây), không phải "bộ não" của Git; bạn có thể thay bằng GitLab, Bitbucket hay server riêng mà Git không đổi tí nào.

**Pull Request là một cuộc trò chuyện, không phải cái nút "gộp".** Giá trị thật của PR không nằm ở lúc merge, mà ở khoảng thời gian *trước khi* merge: đồng đội đọc, hỏi, gợi ý, chặn lại nếu thấy rủi ro. Nó biến "code của một người" thành "code cả team chịu trách nhiệm" — và là nơi bạn học nhanh nhất khi mới vào nghề.

**Vì sao secret lỡ push là "mất vĩnh viễn"?** Vì Git lưu *cả lịch sử*, không chỉ bản hiện tại. Xoá file trong commit mới không xoá nó khỏi các commit cũ — và một khi đã lên GitHub công khai, bot quét được trong vài giây, người khác có thể đã fork/clone. Đó là lý do việc cần làm không phải "xoá cho khuất mắt" mà là **xoay (rotate) secret ngay**.

### 🧪 Lab cơ bản

> Mục tiêu: đưa repo lên GitHub và đi trọn 1 vòng Pull Request.

**Bước 1 — Tạo repo trên GitHub** (nút **New**, đặt tên `my-app`, để trống — đừng thêm README để khỏi conflict).

**Bước 2 — Kết nối và đẩy lên.**
```bash
cd my-app
git remote add origin git@github.com:<username>/my-app.git
git push -u origin main
```
Tải lại trang GitHub → thấy code đã lên.

**Bước 3 — Viết README.md.**
```bash
nano README.md      # mô tả 1 dòng + cách cài + cách chạy
git add README.md && git commit -m "Thêm README" && git push
```

**Bước 4 — Đi trọn 1 vòng Pull Request.**
```bash
git switch -c feature/doc
echo "## Hướng dẫn" >> README.md
git commit -am "Bổ sung hướng dẫn" && git push -u origin feature/doc
```
Trên GitHub → nút **Compare & pull request** → mô tả → **Create PR** → **Merge**.

**Bước 5 — Tạo 1 Issue và clone thử 1 repo công khai.**
```bash
git clone https://github.com/git/git.git /tmp/git-source
```
Trên GitHub, mở tab **Issues → New issue**, mô tả 1 tính năng, gắn label.

### 🚀 Lab nâng cao (best-practice)

> Mục tiêu: thiết lập repo như một dự án nghiêm túc, có bảo vệ và tự động hóa cộng tác.

1. **Branch protection cho `main`** (Settings → Branches): bắt buộc PR, bắt buộc review, không cho push thẳng. → không ai (kể cả bạn) phá nhánh chính.
2. **PR template** (`.github/pull_request_template.md`) — chuẩn hóa mô tả PR: làm gì, test thế nào, ảnh hưởng gì.
3. **CODEOWNERS** (`.github/CODEOWNERS`) — tự gán người review theo thư mục.
4. **Dùng `gh` CLI** để làm việc nhanh không rời terminal:
   ```bash
   gh pr create --fill          # tạo PR từ nhánh hiện tại
   gh pr checks                 # xem CI pass chưa
   gh pr merge --squash         # merge gọn lịch sử
   ```

### 💡 Bổ sung thực tế: SSH vs HTTPS, fork workflow & viết README "ăn điểm"

- **Remote dùng SSH thay HTTPS** để khỏi nhập token mỗi lần (đã tạo key ở Ngày 1/8):
  ```bash
  git remote set-url origin git@github.com:user/repo.git
  ```
- **Fork workflow** (đóng góp open-source): fork → clone bản fork → thêm remote `upstream` trỏ repo gốc → `git fetch upstream` để đồng bộ → PR từ fork về gốc.
- **README tối thiểu nên có:** mô tả 1 dòng · ảnh/demo · cách cài đặt · cách chạy · cấu trúc thư mục · giấy phép. README tốt = người khác (và bạn 6 tháng sau) chạy được ngay.
- **Quy tắc bảo mật:** nếu lỡ push secret lên GitHub → **coi như đã lộ vĩnh viễn**, phải **xoay (rotate) ngay** secret đó, không chỉ xóa commit (lịch sử vẫn còn ở fork/cache).

### 🧭 Hướng dẫn làm lab & giải nghĩa lệnh (cho người tự học)

> Làm tuần tự, dừng ở mỗi ✅ **Checkpoint**.

**Bước 1 — Kết nối và đẩy lần đầu.**
```bash
git remote add origin git@github.com:<username>/my-app.git
git remote -v          # kiểm tra URL
git push -u origin main
```
✅ **Checkpoint:** GitHub hiển thị code của bạn.
💡 `-u` liên kết nhánh local với remote, từ đó chỉ cần gõ `git push` là đủ.

**Bước 2 — Hiểu `fetch` vs `pull`.**
```bash
git fetch origin       # chỉ TẢI về, không đụng code đang làm
git pull               # tải + gộp (= fetch + merge)
```
✅ **Checkpoint:** hiểu `fetch` an toàn để xem trước, `pull` gộp luôn.

**Bước 3 — Mở Pull Request (theo Lab Bước 4).**
✅ **Checkpoint:** tab **Pull requests** hiện PR đang mở; sau khi merge, nhánh feature gộp vào main.

**Bước 4 — (Nâng cao) bật Branch protection.**
Settings → Branches → thêm rule cho `main` (bắt buộc PR). Thử `git push` thẳng vào main → **bị chặn**.
✅ **Checkpoint:** không ai (kể cả bạn) push thẳng được vào `main`.

### 🐛 Gỡ lỗi nhanh

| Triệu chứng | Nguyên nhân | Cách sửa |
|---|---|---|
| `push` hỏi username/password | Remote dùng HTTPS thay SSH | `git remote set-url origin git@github.com:user/repo.git` |
| `Permission denied (publickey)` | SSH key chưa lên GitHub | Ôn Ngày 1/8: thêm `.pub` vào GitHub |
| `Updates were rejected (fetch first)` | Remote có commit bạn chưa có | `git pull` (gộp) rồi `push` lại |
| `push` bị chặn vào `main` | Branch protection đang bật (đúng ý!) | Mở PR thay vì push thẳng |
| Lỡ push secret | Lộ vĩnh viễn trong lịch sử | **Rotate secret ngay**; thêm `.gitignore`; cân nhắc `git filter-repo` |

### 📝 Bài ôn tập & Demo đối chiếu

**✍️ Tự kiểm tra:**

<details>
<summary>1. `git fetch` và `git pull` khác nhau thế nào?</summary>

> `fetch` chỉ tải commit mới về (không đụng code đang làm). `pull` = `fetch` + `merge` (gộp luôn vào nhánh hiện tại).
</details>

<details>
<summary>2. Quy trình GitHub flow gồm những bước nào?</summary>

> branch → commit → push → mở PR → review → merge → xoá nhánh.
</details>

<details>
<summary>3. Pull Request dùng để làm gì?</summary>

> Đề nghị gộp nhánh vào main và để đồng đội **review** (góp ý, duyệt) trước khi merge — đảm bảo chất lượng, không sửa thẳng nhánh chính.
</details>

<details>
<summary>4. Lỡ push secret lên GitHub thì làm gì đầu tiên?</summary>

> **Đổi (rotate) secret đó ngay** — vì nó đã lộ vĩnh viễn trong lịch sử. Xoá commit là chưa đủ.
</details>

**🔬 Demo đối chiếu:**

| Demo đối chiếu | Kết quả mong đợi |
|---|---|
| `git push` | Repo online cập nhật commit mới |
| Tạo 1 PR | Tab Pull requests hiện PR đang mở |
| `git clone <url>` | Thư mục project xuất hiện |

### 📚 Thuật ngữ Anh–Việt (ngày này)

| Thuật ngữ | Nghĩa |
|---|---|
| **Remote / origin** | Repo trên server / tên mặc định của remote |
| **push / pull / fetch** | Đẩy lên / kéo về (fetch+merge) / chỉ tải về |
| **clone** | Sao chép repo về máy |
| **Pull Request (PR)** | Đề nghị gộp nhánh + để review |
| **Code review** | Đọc & góp ý code trước khi merge |
| **Fork** | Sao chép repo người khác về tài khoản mình |
| **Branch protection** | Quy tắc bảo vệ nhánh chính |

### 🎯 Đúc kết Ngày 15

**3 điều phải mang theo:**
1. **Git = local, GitHub = remote để chia sẻ.** `push` đẩy lên, `pull` (= `fetch` + `merge`) kéo về, `fetch` chỉ tải để xem trước.
2. **GitHub Flow:** branch → commit → push → PR → review → merge → xoá nhánh. PR là nơi đảm bảo chất lượng, không sửa thẳng `main`.
3. **Branch protection** cho `main` (bắt buộc PR + review) để không ai push thẳng phá nhánh chính.

> 🧠 **Một câu để nhớ:** lỡ đẩy secret lên GitHub = coi như **lộ vĩnh viễn** (còn trong lịch sử/fork/cache). Việc cần làm không phải xoá commit, mà **đổi (rotate) secret đó ngay**.

**✅ Tự chấm** *(đánh dấu khi làm được mà không nhìn tài liệu):*
- [ ] Kết nối repo local với GitHub và `push -u` lần đầu
- [ ] Đi trọn 1 vòng Pull Request (tạo nhánh → PR → merge)
- [ ] Phân biệt `fetch` và `pull`
- [ ] Bật branch protection cho `main` và thử push thẳng (bị chặn)
- [ ] Nói được việc đầu tiên phải làm khi lỡ push secret

✅ **Kết quả đạt được:** Cộng tác qua GitHub, đi trọn vòng PR, viết README — sẵn sàng làm việc nhóm thực tế.

---

## Ngày 16 — Docker: Khái niệm & container đầu tiên

> ⏱️ ~90 phút · Loại: Docker
>
> 🧭 **Bạn đang ở đâu:** Ngày 13–15 (Git/GitHub) → **Ngày 16 (Docker — đóng gói app vào "hộp" chạy đâu cũng giống nhau)** → Ngày 17 (tự viết Dockerfile). Docker giải quyết dứt điểm bệnh "works on my machine" — nền tảng của mọi thứ container/K8s về sau.
>
> ✅ **Chuẩn bị:** cài Docker (Docker Desktop, hoặc trên Linux theo docs.docker.com), kiểm tra `docker --version` chạy được.

### 📘 Lý thuyết

#### 1. Vấn đề Docker giải quyết

App chạy ngon trên máy bạn nhưng lên server thì lỗi (thiếu thư viện, khác phiên bản, khác cấu hình) — bệnh *"works on my machine"*. **Docker** đóng gói app *cùng mọi thứ nó cần* vào 1 "hộp" (**container**) → hộp chạy giống hệt nhau ở mọi nơi.

#### 2. Container vs Máy ảo (VM)

| | Máy ảo (VM) | Container |
|---|---|---|
| Đóng gói | Cả 1 hệ điều hành riêng | Chỉ app + thư viện |
| Kernel | Riêng từng VM | **Dùng chung kernel host** |
| Nặng | GB, khởi động phút | MB, khởi động **giây** |
| Ví như | Căn nhà riêng | Căn hộ chung cư |

#### 3. Image vs Container — dễ nhầm nhất

- **Image** = khuôn mẫu **chỉ đọc** (như khuôn bánh / file cài đặt).
- **Container** = một bản **đang chạy** của image (cái bánh làm từ khuôn). Từ 1 image chạy được nhiều container.
- **Docker Hub** = kho chứa image công khai (registry) để `pull` về.

#### 4. Lệnh cơ bản

| Lệnh | Làm gì |
|---|---|
| `docker run <image>` | Tạo + chạy container |
| `docker ps` / `docker ps -a` | Container đang chạy / kể cả đã dừng |
| `docker stop/start/rm <ct>` | Dừng / chạy lại / xoá container |
| `docker images` / `docker rmi` | Liệt kê / xoá image |
| `docker logs <ct>` | Xem log container |
| `docker exec -it <ct> bash` | Vào shell bên trong container |

#### 5. Cờ hay dùng khi `docker run`

- `-d` chạy nền (detached); `--name web` đặt tên.
- `-p 8080:80` map **cổng host : cổng container** (mở `localhost:8080` → tới cổng 80 trong container).
- `-v host_path:container_path` gắn volume để lưu dữ liệu bền vững (Ngày 19).

> 🔑 Container **sống nhờ tiến trình chính (PID 1)**. Tiến trình đó kết thúc → container tắt. Vì thế `docker run ubuntu` thoát ngay (không có gì chạy) còn `nginx` thì sống.

**Sơ đồ — Container vs Máy ảo (vì sao container nhẹ hơn):**
```mermaid
flowchart TB
    subgraph VM["🖥️ Máy ảo (VM) — nặng, khởi động phút"]
        direction TB
        H1["Hạ tầng vật lý"] --> HV["Hypervisor"]
        HV --> G1["Guest OS đầy đủ"] --> A1["App A"]
        HV --> G2["Guest OS đầy đủ"] --> A2["App B"]
    end
    subgraph CT["📦 Container — nhẹ, khởi động giây"]
        direction TB
        H2["Hạ tầng vật lý"] --> OS["Host OS + Kernel (CHIA SẺ)"]
        OS --> DK["Docker Engine"]
        DK --> C1["App A"]
        DK --> C2["App B"]
        DK --> C3["App C"]
    end
    classDef vm fill:#fce4ec,stroke:#c2185b;
    classDef ct fill:#e8f5e9,stroke:#2e7d32;
    class H1,HV,G1,G2,A1,A2 vm;
    class H2,OS,DK,C1,C2,C3 ct;
```

### 📖 Hiểu rõ hơn (giải thích cho người mới)

> 📘 đã có bảng so sánh VM/container và image/container. Mục này cho bạn **hình dung** để nhớ.

**"Dùng chung kernel" — chìa khoá giải thích mọi thứ.** Container không phải máy ảo tí hon; nó là các *tiến trình* chạy thẳng trên kernel của máy chủ, chỉ được Linux "quây" lại cho tưởng mình ở riêng (nhờ namespace + cgroup). Vì không phải khởi động cả một hệ điều hành, container lên trong *tích tắc* và chỉ nặng bằng app + thư viện. Đây là lý do một laptop chạy được 20 container nhưng chật vật với 3 VM.

**Image và container giống class và object trong lập trình.** Image là bản thiết kế *bất biến, chỉ đọc*; container là một *thực thể đang chạy* sinh ra từ nó. Từ một image bạn bật được nhiều container y hệt nhau — và mỗi container khi chạy có thêm một lớp ghi riêng bên trên (xoá container là mất lớp ghi đó, nên dữ liệu quan trọng phải để ra volume — Ngày 19).

**Docker giết "works on my machine" bằng cách gói cả môi trường.** Trước đây bạn giao *code* rồi cầu mong server có đúng thư viện/phiên bản. Với Docker bạn giao *cả cái hộp* đã chứa sẵn mọi thứ — máy nào có Docker là chạy giống hệt. Bài toán "máy tôi chạy được" chuyển thành "cái hộp chạy được ở đâu cũng thế".

### 🧪 Lab cơ bản

> Mục tiêu: chạy container đầu tiên, map cổng, vào trong container, xem log và dọn dẹp.

**Bước 1 — Xác nhận Docker chạy.**
```bash
docker --version
docker run hello-world
```
Bạn sẽ thấy `Hello from Docker!` — xác nhận Docker hoạt động.

**Bước 2 — Chạy nginx và mở trên trình duyệt.**
```bash
docker run -d -p 8080:80 --name web nginx
docker ps        # thấy container "web" đang chạy
```
Mở `http://localhost:8080` → trang **Welcome to nginx!**.

**Bước 3 — Vào bên trong container.**
```bash
docker exec -it web bash
# bên trong: ls /usr/share/nginx/html ; cat /etc/nginx/nginx.conf | head
exit
```

**Bước 4 — Xem log.**
```bash
docker logs web         # thấy log request khi bạn mở trình duyệt
```

**Bước 5 — Dọn dẹp.**
```bash
docker stop web
docker rm web
docker ps -a            # không còn "web"
```

### 🚀 Lab nâng cao (best-practice)

> Mục tiêu: dùng Docker gọn gàng, không để rác chiếm đầy đĩa (lỗi kinh điển sau vài tuần).

1. **Chạy không cần root** — thêm user vào nhóm docker (an toàn hơn `sudo docker`):
   ```bash
   sudo usermod -aG docker $USER   # đăng xuất/đăng nhập lại
   ```
2. **Luôn đặt tên + giới hạn tài nguyên** cho container:
   ```bash
   docker run -d --name web --memory=256m --cpus=0.5 -p 8080:80 nginx
   ```
3. **Dọn rác định kỳ** — image/volume mồ côi ngốn đĩa khủng khiếp:
   ```bash
   docker system df            # xem Docker đang chiếm bao nhiêu đĩa
   docker system prune -a      # dọn image/container/network không dùng
   docker volume prune         # dọn volume mồ côi (cẩn thận dữ liệu!)
   ```
4. **Pin phiên bản image** — `nginx:1.27-alpine` thay vì `nginx:latest` (latest thay đổi bất ngờ, vỡ build).

### 💡 Bổ sung thực tế: kiến trúc Docker & đọc lỗi thường gặp

- **Kiến trúc:** Docker CLI → Docker daemon (dockerd) → containerd → runc. Hiểu điều này giúp bạn debug khi "docker không phản hồi" (thường là daemon chết: `systemctl status docker`).
- **3 lỗi người mới gặp nhiều nhất:**
  | Lỗi | Nguyên nhân & cách xử lý |
  |---|---|
  | `port is already allocated` | Cổng host đã bị chiếm → đổi port hoặc `docker ps` tìm container cũ |
  | `no space left on device` | Image/volume rác → `docker system prune -a` |
  | Container `Exited (0/1)` ngay lập tức | Tiến trình chính kết thúc → xem `docker logs <name>` |
- **Container sống nhờ tiến trình foreground:** container dừng khi tiến trình PID 1 thoát. Đây là lý do `docker run ubuntu` thoát ngay (không có gì chạy), còn `nginx` thì sống (nginx chạy foreground).

### 🧭 Hướng dẫn làm lab & giải nghĩa lệnh (cho người tự học)

> Làm tuần tự, dừng ở mỗi ✅ **Checkpoint**.

**Bước 1 — Chạy nginx nền + map cổng.**
```bash
docker run -d -p 8080:80 --name web nginx
docker ps
```
✅ **Checkpoint:** `docker ps` hiện `web` với `0.0.0.0:8080->80/tcp`, mở `localhost:8080` ra trang nginx.
💡 `-p 8080:80` = "khách gõ cổng 8080 của máy → chuyển vào cổng 80 trong container".

**Bước 2 — Hiểu "container sống nhờ tiến trình chính".**
```bash
docker run --name u ubuntu        # thoát NGAY (Exited)
docker ps -a | grep u             # thấy STATUS Exited (0)
```
✅ **Checkpoint:** container ubuntu ở trạng thái `Exited` ngay, còn `web` (nginx) vẫn `Up`.
💡 ubuntu không có tiến trình foreground nào → PID 1 kết thúc → container tắt. nginx chạy foreground nên sống.

**Bước 3 — Vào trong container xem thực tế.**
```bash
docker exec -it web bash
ls /usr/share/nginx/html ; exit
```
✅ **Checkpoint:** vào được shell, thấy file `index.html`.

**Bước 4 — Dọn dẹp gọn gàng.**
```bash
docker stop web && docker rm web u
docker system df        # xem Docker đang chiếm bao nhiêu đĩa
```
✅ **Checkpoint:** `docker ps -a` không còn container lab.
💡 `docker system prune -a` dọn image/container rác — chạy định kỳ kẻo đầy đĩa.

### 🐛 Gỡ lỗi nhanh

| Triệu chứng | Nguyên nhân | Cách sửa |
|---|---|---|
| `port is already allocated` | Cổng host đã bị container khác giữ | Đổi cổng (`-p 8081:80`) hoặc `docker ps` tìm & dừng cái cũ |
| Container `Exited (0)` ngay | Không có tiến trình foreground | Bình thường với ubuntu; app thật thì xem `docker logs` |
| Container `Exited (1/137)` | App crash / bị kill (OOM) | `docker logs <ct>` đọc lỗi; 137 = hết RAM |
| `Cannot connect to the Docker daemon` | Docker daemon chưa chạy | `sudo systemctl start docker`; Docker Desktop mở chưa |
| `permission denied ... docker.sock` | User chưa trong nhóm docker | `sudo usermod -aG docker $USER` rồi đăng nhập lại |
| `no space left on device` | Image/volume rác | `docker system prune -a`; `docker system df` để xem |

### 📝 Bài ôn tập & Demo đối chiếu

**✍️ Tự kiểm tra:**

<details>
<summary>1. Phân biệt image và container bằng ví dụ đời thực.</summary>

> Image = khuôn bánh (chỉ đọc, tạo sẵn). Container = cái bánh làm ra từ khuôn (bản đang chạy). Một khuôn làm được nhiều bánh.
</details>

<details>
<summary>2. `-p 3000:80` nghĩa là gì?</summary>

> Map cổng 3000 của **máy host** vào cổng 80 **trong container**. Truy cập `localhost:3000` sẽ tới dịch vụ nghe cổng 80 bên trong.
</details>

<details>
<summary>3. Vì sao container nhẹ hơn VM?</summary>

> Container dùng chung kernel của host, chỉ đóng gói app + thư viện (MB, khởi động giây). VM cõng cả hệ điều hành riêng (GB, khởi động phút).
</details>

<details>
<summary>4. Vì sao `docker run ubuntu` thoát ngay còn nginx thì chạy mãi?</summary>

> Container sống nhờ tiến trình PID 1. Ubuntu không chạy gì ở foreground → thoát ngay. nginx chạy foreground → giữ container sống.
</details>

**🔬 Demo đối chiếu:**

| Demo đối chiếu | Kết quả mong đợi |
|---|---|
| `docker run hello-world` | `Hello from Docker!` |
| `docker ps` | Liệt kê container đang chạy |
| Mở `localhost:8080` | Trang `Welcome to nginx!` |

### 📚 Thuật ngữ Anh–Việt (ngày này)

| Thuật ngữ | Nghĩa |
|---|---|
| **Image** | Khuôn mẫu chỉ đọc để tạo container |
| **Container** | Bản đang chạy của một image |
| **Registry / Docker Hub** | Kho chứa image |
| **Port mapping** (`-p`) | Ánh xạ cổng host ↔ container |
| **Volume** | Ổ lưu dữ liệu bền vững ngoài container |
| **Daemon** (dockerd) | Tiến trình nền chạy Docker |
| **detached** (`-d`) | Chạy container ở chế độ nền |

### 🎯 Đúc kết Ngày 16

**3 điều phải mang theo:**
1. **Container nhẹ vì dùng chung kernel host** (không cõng OS riêng như VM) → khởi động giây, nặng MB.
2. **Image (khuôn, chỉ đọc) ≠ Container (bản đang chạy).** Một image → nhiều container.
3. **Container sống nhờ tiến trình PID 1**: tiến trình chính thoát → container tắt. `-p host:container` map cổng, `-d` chạy nền, `docker logs`/`exec` để soi.

> 🧠 **Một câu để nhớ:** container sống nhờ tiến trình chính của nó. Khi tiến trình đó kết thúc, container tắt — đó là lý do `docker run ubuntu` thoát ngay còn `nginx` thì sống.

**✅ Tự chấm** *(đánh dấu khi làm được mà không nhìn tài liệu):*
- [ ] Giải thích vì sao container nhẹ hơn VM
- [ ] Phân biệt image và container bằng ví dụ
- [ ] Chạy nginx nền, map cổng, mở được trên trình duyệt
- [ ] Vào trong container bằng `docker exec -it` và xem `docker logs`
- [ ] Nói được vì sao `docker run ubuntu` thoát ngay

✅ **Kết quả đạt được:** Hiểu container vs VM, chạy được container đầu tiên, map cổng, xem log và dọn dẹp Docker.

---

## Ngày 17 — Docker: Dockerfile & Build Image

> ⏱️ ~90 phút · Loại: Docker
>
> 🧭 **Bạn đang ở đâu:** Ngày 16 (chạy image có sẵn) → **Ngày 17 (tự viết Dockerfile để đóng gói app của mình)** → Ngày 18 (tối ưu image nhỏ gọn). Đây là lúc bạn biến app của mình thành image chạy được ở bất kỳ đâu.
>
> ✅ **Chuẩn bị:** Docker chạy được (Ngày 16). Một app nhỏ để đóng gói (Node.js hoặc Python — mình dùng Node ở lab).

### 📘 Lý thuyết

#### 1. Dockerfile là gì

Là file "công thức nấu ăn" mô tả *từng bước* tạo image của riêng app bạn. `docker build` đọc nó → "nấu" ra image.

#### 2. Các chỉ thị chính

| Chỉ thị | Ý nghĩa | Chạy lúc |
|---|---|---|
| `FROM node:20` | Chọn image nền | build |
| `WORKDIR /app` | Thư mục làm việc trong image | build |
| `COPY src dst` | Chép file vào image | build |
| `RUN <lệnh>` | Chạy lệnh (vd cài thư viện) | **build** |
| `ENV KEY=val` | Đặt biến môi trường | build+run |
| `EXPOSE 3000` | Khai báo cổng (tài liệu) | (thông tin) |
| `CMD [...]` | Lệnh chạy mặc định | **start container** |
| `ENTRYPOINT [...]` | Lệnh chính cố định | start container |

> 🔑 `RUN` chạy lúc **build** (tạo image), `CMD`/`ENTRYPOINT` chạy lúc **start** (chạy container). Đừng nhầm — đây là câu hỏi phỏng vấn kinh điển.

#### 3. Build & tag

```bash
docker build -t my-app:1.0 .    # -t đặt tên:tag, dấu . = build context
```

#### 4. Layer caching — vì sao thứ tự dòng lệnh quan trọng

Mỗi chỉ thị tạo 1 **layer**, Docker **nhớ (cache)** các layer không đổi. Mẹo vàng: chép file thư viện + cài **trước**, chép code **sau**:
```dockerfile
COPY package*.json ./     # đổi ít → cache lại được
RUN npm ci
COPY . .                  # code đổi liên tục → để cuối
```
Sai thứ tự = mỗi lần sửa 1 dòng code phải cài lại toàn bộ thư viện (chậm khủng khiếp).

#### 5. `.dockerignore` & CMD vs ENTRYPOINT

- **`.dockerignore`**: loại `.git`, `node_modules`, `.env` khỏi build context (như `.gitignore`).
- **CMD vs ENTRYPOINT**: `ENTRYPOINT` = lệnh cố định luôn chạy; `CMD` = tham số mặc định, dễ ghi đè khi `docker run`.
- **Tag & push**: `docker tag` đặt tên, `docker push` đẩy lên Docker Hub.

### 📖 Hiểu rõ hơn (giải thích cho người mới)

> 📘 đã liệt kê các chỉ thị và layer cache. Mục này cho bạn **hình dung** để nhớ.

**Dockerfile là công thức, `docker build` là nấu, image là món đã đóng hộp.** Điểm hay: công thức nằm trong Git, ai chạy cũng ra đúng một image — không còn "cài tay theo trí nhớ". Khác biệt lớn nhất người mới cần khắc cốt: có chỉ thị chạy lúc *nấu* (build) và có chỉ thị chỉ chạy khi *mở hộp ra dùng* (start container).

**`RUN` vs `CMD` — nhầm là hỏng.** `RUN` thực thi *khi build* để tạo ra các lớp trong image (vd cài thư viện) — làm một lần rồi đóng băng vào image. `CMD` chỉ định *lệnh mặc định khi container khởi động* — chạy lại mỗi lần bật container. Cùng một Dockerfile: `RUN npm install` đóng gói thư viện sẵn; `CMD ["node","server.js"]` mới là thứ khởi động app.

**Layer cache — vì sao thứ tự dòng lệnh quyết định tốc độ.** Mỗi chỉ thị tạo một *lớp*, và Docker tái dùng lớp nào chưa đổi. Nếu bạn `COPY . .` trước rồi mới cài thư viện, thì sửa *một dòng code* cũng làm đổi lớp copy → mọi lớp sau (kể cả cài thư viện) phải làm lại. Đảo thứ tự — copy `package.json` + cài trước, copy code sau — thì thư viện được cache, build lần sau nhanh gấp nhiều lần. Đây không phải mẹo vặt mà là cách bạn tiết kiệm hàng giờ mỗi tuần.

### 🧪 Lab cơ bản

> Mục tiêu: đóng gói một app Node.js thành image và chạy nó. Các file dưới đây đầy đủ, copy-chạy được.

**Bước 1 — Tạo app nhỏ.** Trong thư mục mới, tạo 3 file:

`package.json`:
```json
{ "name": "my-app", "version": "1.0.0", "main": "server.js" }
```
`server.js`:
```javascript
const http = require('http');
http.createServer((req, res) => res.end('Hello DevOps'))
    .listen(3000, () => console.log('Chạy ở cổng 3000'));
```
`Dockerfile`:
```dockerfile
FROM node:20-alpine
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
EXPOSE 3000
CMD ["node", "server.js"]
```

**Bước 2 — Tạo `.dockerignore`.**
```bash
printf "node_modules\n.git\n.env\n" > .dockerignore
```

**Bước 3 — Build image.**
```bash
docker build -t my-app:1.0 .
```
Bạn sẽ thấy dòng cuối `naming to docker.io/library/my-app:1.0` (build thành công).

**Bước 4 — Chạy và test.**
```bash
docker run -d -p 3000:3000 --name app my-app:1.0
curl localhost:3000        # in: Hello DevOps
```

**Bước 5 — (Tuỳ chọn) đẩy lên Docker Hub.**
```bash
docker login
docker tag my-app:1.0 <dockerhub-user>/my-app:1.0
docker push <dockerhub-user>/my-app:1.0
```

### 🚀 Lab nâng cao (best-practice)

> Mục tiêu: viết Dockerfile tận dụng cache đúng cách và không nhồi rác vào image.

1. **Thứ tự layer để tối ưu cache** — copy dependency trước, code sau:
   ```dockerfile
   COPY package*.json ./      # layer này chỉ đổi khi dependency đổi
   RUN npm ci                 # cache lại nếu package.json không đổi
   COPY . .                   # code đổi thường xuyên → để cuối
   ```
   > Sai thứ tự = mỗi lần sửa 1 dòng code phải cài lại toàn bộ dependency (chậm khủng khiếp).
2. **`.dockerignore` đầy đủ** — không copy `.git`, `node_modules`, `.env` vào image.
3. **Dùng `npm ci` thay `npm install`** trong build (cài đúng theo lock file, tái lập được).
4. **Gắn metadata (label)** chuẩn OCI:
   ```dockerfile
   LABEL org.opencontainers.image.source="https://github.com/user/repo"
   ```

### 💡 Bổ sung thực tế: CMD vs ENTRYPOINT & biến lúc build/run

- **CMD vs ENTRYPOINT** (hay nhầm):
  | | Vai trò |
  |---|---|
  | `ENTRYPOINT ["app"]` | lệnh **cố định** — luôn chạy |
  | `CMD ["--port", "80"]` | **tham số mặc định** — dễ ghi đè khi `docker run` |
  | Kết hợp | `docker run img --port 9000` → ghi đè tham số, giữ entrypoint |
- **ARG vs ENV:** `ARG` chỉ tồn tại lúc **build** (vd version), `ENV` tồn tại lúc **chạy**. ⚠️ Đừng truyền secret qua `ARG`/`ENV` — nó nằm trong layer image, ai cũng đọc được bằng `docker history`.
- **BuildKit** (build engine hiện đại, bật mặc định) hỗ trợ `--secret` để dùng secret lúc build mà không nhúng vào image:
  ```bash
  DOCKER_BUILDKIT=1 docker build --secret id=npmrc,src=$HOME/.npmrc .
  ```

### 🧭 Hướng dẫn làm lab & giải nghĩa lệnh (cho người tự học)

> Làm tuần tự, dừng ở mỗi ✅ **Checkpoint**.

**Bước 1 — Build image.**
```bash
docker build -t my-app:1.0 .
docker images | grep my-app
```
✅ **Checkpoint:** build thành công, `docker images` thấy `my-app 1.0`.
💡 Dấu `.` cuối lệnh là **build context** — thư mục Docker gửi cho daemon (nhớ có `.dockerignore` để không gửi rác).

**Bước 2 — Chạy & kiểm tra app.**
```bash
docker run -d -p 3000:3000 --name app my-app:1.0
curl localhost:3000
```
✅ **Checkpoint:** in `Hello DevOps`.
⚠️ Không thấy gì? `docker logs app` xem app có khởi động không.

**Bước 3 — Trải nghiệm layer cache.**
```bash
docker build -t my-app:1.0 .     # sửa 1 dòng trong server.js rồi build lại
```
✅ **Checkpoint:** lần build lại, các layer `npm install` hiện `CACHED` (không cài lại) vì `package.json` không đổi → nhanh.
💡 Đây là lý do phải `COPY package*.json` + `RUN npm install` TRƯỚC `COPY . .`.

**Bước 4 — Xem cấu tạo image.**
```bash
docker history my-app:1.0
```
✅ **Checkpoint:** thấy từng layer ứng với từng dòng Dockerfile + kích thước.

### 🐛 Gỡ lỗi nhanh

| Triệu chứng | Nguyên nhân | Cách sửa |
|---|---|---|
| Mỗi lần build đều cài lại npm | `COPY . .` đặt trước `RUN npm install` | Đưa `COPY package*.json` + `RUN` lên trước `COPY . .` |
| Build gửi context rất lâu/nặng | Thiếu `.dockerignore` (gửi cả `.git`, `node_modules`) | Tạo `.dockerignore` |
| `CMD` không chạy như mong đợi | Nhầm dạng shell vs exec | Dùng dạng JSON: `CMD ["node","server.js"]` |
| App chạy nhưng `curl` không tới | Chưa `-p` map cổng, hoặc app nghe `127.0.0.1` | `-p 3000:3000`; app nên nghe `0.0.0.0` |
| Secret lộ trong image | Truyền qua `ARG`/`ENV` | Dùng BuildKit `--secret`; không nhúng secret vào layer |

### 📝 Bài ôn tập & Demo đối chiếu

**✍️ Tự kiểm tra:**

<details>
<summary>1. `RUN` và `CMD` khác nhau thế nào?</summary>

> `RUN` chạy lúc **build** (tạo layer trong image, vd cài thư viện). `CMD` chạy lúc **start container** (lệnh mặc định khi container khởi động).
</details>

<details>
<summary>2. Vì sao nên COPY package.json + cài dependency TRƯỚC khi COPY toàn bộ code?</summary>

> Để tận dụng **layer cache**: code đổi liên tục nhưng dependency ít đổi. Đặt cài dependency trước → build lại chỉ tốn thời gian ở bước copy code, không cài lại thư viện.
</details>

<details>
<summary>3. Viết Dockerfile tối giản cho app Python (Flask).</summary>

> ```dockerfile
> FROM python:3.12-slim
> WORKDIR /app
> COPY requirements.txt ./
> RUN pip install -r requirements.txt
> COPY . .
> CMD ["python", "app.py"]
> ```
</details>

<details>
<summary>4. `.dockerignore` để làm gì?</summary>

> Loại file không cần khỏi build context (`.git`, `node_modules`, `.env`) → build nhanh hơn, image gọn hơn, tránh lộ secret.
</details>

**🔬 Demo đối chiếu:**

| Demo đối chiếu | Kết quả mong đợi |
|---|---|
| `docker build -t my-app:1.0 .` | Build thành công, có tag |
| `docker images` | Hiện `my-app` |
| `curl localhost:3000` | `Hello DevOps` |

### 📚 Thuật ngữ Anh–Việt (ngày này)

| Thuật ngữ | Nghĩa |
|---|---|
| **Dockerfile** | Công thức để build image |
| **Build context** | Thư mục gửi cho Docker khi build (dấu `.`) |
| **Layer** | Một tầng của image (mỗi chỉ thị tạo 1 layer) |
| **Cache** | Docker tái dùng layer không đổi để build nhanh |
| **CMD / ENTRYPOINT** | Lệnh mặc định / lệnh chính cố định |
| **Tag** | Nhãn phiên bản của image (`:1.0`) |
| **`.dockerignore`** | Danh sách file bỏ khỏi build context |

### 🎯 Đúc kết Ngày 17

**3 điều phải mang theo:**
1. **`RUN` chạy lúc build** (đóng vào image), **`CMD`/`ENTRYPOINT` chạy lúc start** (khởi động container). Đừng nhầm.
2. **Thứ tự layer = tốc độ build:** `COPY package*.json` + cài dependency TRƯỚC `COPY . .` để cache thư viện.
3. **`.dockerignore`** loại `.git`/`node_modules`/`.env` khỏi build context → nhanh, gọn, không lộ secret.

> 🧠 **Một câu để nhớ:** `RUN` chạy lúc *build*, `CMD` chạy lúc *start*. Đừng nhầm — đây là câu hỏi phỏng vấn kinh điển.

**✅ Tự chấm** *(đánh dấu khi làm được mà không nhìn tài liệu):*
- [ ] Viết Dockerfile đóng gói 1 app nhỏ và `docker build` thành công
- [ ] Giải thích khác biệt `RUN` vs `CMD`
- [ ] Sắp xếp layer đúng để tận dụng cache (thấy `CACHED` khi build lại)
- [ ] Tạo `.dockerignore` và biết nó giúp gì
- [ ] Đọc `docker history` để thấy từng layer

✅ **Kết quả đạt được:** Tự build image từ Dockerfile, hiểu layer cache, đẩy image lên registry.

---

## Ngày 18 — Docker: Image tối ưu & Multi-stage Build

> ⏱️ ~90 phút · Loại: Docker
>
> 🧭 **Bạn đang ở đâu:** Ngày 17 (viết Dockerfile) → **Ngày 18 (làm image nhỏ, nhanh, an toàn bằng multi-stage)** → Ngày 19 (Volume & Network). Đây là bước từ "image chạy được" lên "image chuẩn production".
>
> ✅ **Chuẩn bị:** đã build được image ở Ngày 17. Cài `trivy` nếu muốn thử quét lỗ hổng (tuỳ chọn).

### 📘 Lý thuyết

#### 1. Vấn đề: image dễ "béo phì"

Để build app cần compiler, thư viện dev, công cụ... nhưng khi *chạy* thì không cần. Nhét hết vào image → nặng cả GB → chậm tải, nhiều lỗ hổng.

#### 2. Multi-stage build — "nấu ở bếp lớn, dọn ra đĩa nhỏ"

Dùng nhiều `FROM` trong 1 Dockerfile:
- **Stage 1 (bếp):** image to, đủ công cụ → build ra sản phẩm.
- **Stage 2 (đĩa):** image nhỏ → chỉ `COPY --from=build` sản phẩm sang, vứt hết công cụ build.

Kết quả: image cuối nhỏ gọn (vd 1.2GB → 150MB).

#### 3. Chọn base image nhỏ

| Base | Kích thước | Ghi chú |
|---|---|---|
| `node:20` | ~1GB | Đầy đủ, nặng |
| `node:20-slim` | ~200MB | Gọn hơn |
| `node:20-alpine` | ~130MB | Rất nhỏ (Alpine Linux) |
| `distroless` | Nhỏ nhất | Không có cả shell → an toàn nhất |

#### 4. Vì sao image nhỏ quan trọng (không chỉ tiết kiệm chỗ)

- Tải/khởi động nhanh hơn → **scale nhanh**.
- **Ít gói = ít lỗ hổng** (bề mặt tấn công nhỏ).
- Chạy bằng `USER` thường (không root) → bị hack cũng hạn chế thiệt hại.

#### 5. Các kỹ thuật tối ưu & bảo mật khác

- **Giảm layer:** gộp lệnh `RUN a && b && dọn-cache` trong 1 layer.
- **`USER node`:** không chạy bằng root.
- **Pin tag rõ ràng** (`1.0.2`) thay vì `latest` (latest thay đổi bất ngờ, không rollback chính xác được).
- **Quét lỗ hổng:** `trivy image <img>` hoặc `docker scout`.
- **Phân tích:** `docker history` (layer nào nặng), `docker inspect`.

> 🔑 Image production lý tưởng **không có** compiler, `git`, hay cả shell nếu không cần. Mỗi thứ thừa là 1 rủi ro.

### 📖 Hiểu rõ hơn (giải thích cho người mới)

> 📘 đã có bảng base image và kỹ thuật tối ưu. Mục này cho bạn **hình dung** để nhớ.

**Vì sao image hay "béo phì"?** Vì đồ *để build* và đồ *để chạy* rất khác nhau. Muốn build bạn cần compiler, thư viện dev, công cụ — nhưng khi app đã chạy thì chẳng dùng đến. Nếu build và chạy trong cùng một image, mọi công cụ build đó bị kéo theo mãi mãi, phình lên cả GB.

**Multi-stage = "nấu ở bếp lớn, bưng ra đĩa nhỏ".** Bạn dùng một stage đầy đủ công cụ để *nấu* ra sản phẩm (binary/dist), rồi mở một stage mới với base tí hon và chỉ `COPY --from` đúng sản phẩm sang — toàn bộ "gian bếp" bị bỏ lại. Kết quả: image cuối chỉ còn thứ cần để *chạy*, nhỏ đi nhiều lần.

**Image nhỏ không chỉ để tiết kiệm ổ đĩa — nó là chuyện tốc độ và an ninh.** Nhỏ thì pull/khởi động nhanh → scale kịp lúc tải tăng. Ít gói thì *ít CVE* → bề mặt tấn công hẹp. Thêm `USER` không-root thì kẻ đột nhập cũng khó leo quyền. Ba lợi ích này đi cùng nhau, nên "làm image nhỏ" là một thói quen production chứ không phải cầu toàn.

### 🧪 Lab cơ bản

> Mục tiêu: thấy tận mắt image nhỏ đi nhờ multi-stage, và quét lỗ hổng.

**Bước 1 — Build phiên bản "béo" (1 stage) để so sánh.** Dùng `Dockerfile` của Ngày 17 (FROM node:20 đầy đủ), build:
```bash
docker build -t my-app:fat -f Dockerfile .
docker images my-app
```
Ghi lại cột SIZE (vd ~1GB).

**Bước 2 — Viết multi-stage `Dockerfile.slim`.**
```dockerfile
# Stage build
FROM node:20 AS build
WORKDIR /app
COPY package*.json ./
RUN npm ci
COPY . .

# Stage chạy — base nhỏ, user thường
FROM node:20-alpine
WORKDIR /app
COPY --from=build /app/node_modules ./node_modules
COPY --from=build /app .
USER node
EXPOSE 3000
CMD ["node", "server.js"]
```

**Bước 3 — Build và so sánh kích thước.**
```bash
docker build -t my-app:slim -f Dockerfile.slim .
docker images my-app
```
Bạn sẽ thấy `my-app:slim` **nhỏ hơn rõ rệt** so với `:fat`.

**Bước 4 — Quét lỗ hổng (tuỳ chọn).**
```bash
trivy image my-app:slim        # bảng CVE theo mức độ
```

**Bước 5 — Xem layer nào nặng.**
```bash
docker history my-app:slim
```

### 🚀 Lab nâng cao (best-practice)

> Mục tiêu: image production thật sự — nhỏ, an toàn, chạy bằng user thường.

1. **Multi-stage mẫu cho Node.js:**
   ```dockerfile
   # Stage build
   FROM node:20 AS build
   WORKDIR /app
   COPY package*.json ./
   RUN npm ci
   COPY . .
   RUN npm run build

   # Stage chạy — chỉ lấy artifact, base nhỏ, user thường
   FROM node:20-alpine
   WORKDIR /app
   COPY --from=build /app/dist ./dist
   COPY --from=build /app/node_modules ./node_modules
   USER node
   EXPOSE 3000
   CMD ["node", "dist/server.js"]
   ```
2. **Quét lỗ hổng tự động** trước khi push:
   ```bash
   trivy image myapp:1.0      # liệt kê CVE theo mức độ nghiêm trọng
   ```
3. **Distroless cho mức bảo mật cao nhất** — không có shell, gần như không có gì để khai thác: `FROM gcr.io/distroless/nodejs20`.
4. **HEALTHCHECK** để Docker/orchestrator biết container thực sự khỏe:
   ```dockerfile
   HEALTHCHECK --interval=30s --timeout=3s CMD wget -qO- http://localhost:3000/health || exit 1
   ```

### 💡 Bổ sung thực tế: vì sao image nhỏ quan trọng hơn bạn nghĩ

- **Image 1.2GB vs 80MB** không chỉ là dung lượng: image nhỏ → pull nhanh hơn (deploy/scale nhanh), **bề mặt tấn công nhỏ hơn** (ít gói = ít CVE), khởi động nhanh hơn.
- **Quy tắc:** image production **không nên có** compiler, `curl`, `git`, hay shell nếu không cần. Mỗi binary thừa là một rủi ro bảo mật.
- **Đo và truy vết "image phình":** `docker history --no-trunc myapp` cho thấy layer nào nặng → thường là `RUN` quên dọn cache, hoặc copy nhầm `node_modules`/`.git`.
- **`.dockerignore` là tuyến phòng thủ đầu** — thiếu nó, `docker build` gửi cả `.git` 500MB vào build context.

### 🧭 Hướng dẫn làm lab & giải nghĩa lệnh (cho người tự học)

> Làm tuần tự, dừng ở mỗi ✅ **Checkpoint**.

**Bước 1 — So sánh fat vs slim.**
```bash
docker images my-app
```
✅ **Checkpoint:** `my-app:slim` nhỏ hơn `my-app:fat` rõ rệt (thường vài lần).
💡 Stage build (compiler, dev deps) bị bỏ lại ở stage 1 → chỉ artifact + base nhỏ được giữ.

**Bước 2 — Xác nhận app vẫn chạy với image nhỏ.**
```bash
docker run -d -p 3001:3000 --name app-slim my-app:slim
curl localhost:3001        # vẫn: Hello DevOps
```
✅ **Checkpoint:** app phản hồi y hệt bản fat, dù image nhỏ hơn nhiều.

**Bước 3 — Kiểm chứng chạy bằng user thường.**
```bash
docker exec app-slim whoami     # in: node (không phải root)
```
✅ **Checkpoint:** in `node` — không chạy bằng root.
💡 Bị hack container cũng khó leo quyền vì không phải root.

**Bước 4 — Tìm layer phình (nếu image vẫn to).**
```bash
docker history --no-trunc my-app:slim
```
✅ **Checkpoint:** đọc được layer nào nặng (thường do quên dọn cache hoặc copy nhầm `node_modules`/`.git`).

### 🐛 Gỡ lỗi nhanh

| Triệu chứng | Nguyên nhân | Cách sửa |
|---|---|---|
| Image slim vẫn to | `.dockerignore` thiếu / copy cả `.git`, dev deps | Bổ sung `.dockerignore`; chỉ `COPY --from=build` artifact cần |
| App lỗi trên alpine mà chạy trên node:20 | Alpine thiếu thư viện hệ thống (glibc) | Cài gói còn thiếu, hoặc dùng `-slim` thay `-alpine` |
| `permission denied` sau khi thêm `USER node` | File thuộc root, user node không ghi được | `COPY --chown=node:node` hoặc chỉnh quyền trước |
| `latest` gây lỗi bất ngờ khi deploy | Image `latest` đã đổi | Pin tag semver/SHA rõ ràng |
| trivy báo nhiều CVE | Base image cũ | Cập nhật base (`node:20-alpine` mới), rebuild |

### 📝 Bài ôn tập & Demo đối chiếu

**✍️ Tự kiểm tra:**

<details>
<summary>1. Multi-stage build giảm kích thước image bằng cách nào?</summary>

> Stage build chứa compiler/dev deps để tạo artifact; stage cuối chỉ `COPY --from=build` artifact sang base nhỏ, bỏ hết công cụ build → image cuối nhẹ.
</details>

<details>
<summary>2. Vì sao không nên chạy container bằng root?</summary>

> Nếu container bị khai thác, chạy bằng root cho kẻ tấn công nhiều quyền hơn (dễ leo thang, phá host). Dùng `USER` thường để giới hạn thiệt hại.
</details>

<details>
<summary>3. Vì sao tránh tag `latest` ở production?</summary>

> `latest` không cố định — mỗi lần pull có thể ra bản khác → không tái lập được, không rollback chính xác. Pin `1.0.2`/SHA.
</details>

<details>
<summary>4. Distroless là gì và lợi ích?</summary>

> Base image tối giản, không có shell/package manager → bề mặt tấn công gần như bằng 0, nhưng khó debug (không vào shell được).
</details>

**🔬 Demo đối chiếu:**

| Demo đối chiếu | Kết quả mong đợi |
|---|---|
| `docker images` fat vs slim | slim nhỏ hơn rõ rệt |
| `curl` app slim | Phản hồi không đổi |
| `docker exec ... whoami` | `node` (không phải root) |

### 📚 Thuật ngữ Anh–Việt (ngày này)

| Thuật ngữ | Nghĩa |
|---|---|
| **Multi-stage build** | Build nhiều tầng, tầng cuối chỉ lấy artifact |
| **`COPY --from`** | Chép file từ stage khác |
| **Base image** | Image nền (alpine/slim/distroless) |
| **Alpine** | Bản Linux siêu nhỏ hay dùng làm base |
| **Distroless** | Image không có shell/OS thừa — an toàn nhất |
| **CVE** | Lỗ hổng bảo mật đã được ghi nhận |
| **`USER`** | Chỉ thị chạy container bằng user không-root |

### 🎯 Đúc kết Ngày 18

**3 điều phải mang theo:**
1. **Multi-stage build:** stage "bếp" build ra artifact, stage cuối base nhỏ chỉ `COPY --from` artifact → image gọn nhiều lần.
2. **Base nhỏ + `USER` không-root** (`alpine`/`slim`/`distroless`) → chạy bằng user thường để giới hạn thiệt hại khi bị hack.
3. **Pin tag rõ ràng** (`1.0.2`/SHA) thay `latest`; **quét CVE** (`trivy`/`docker scout`) trước khi push.

> 🧠 **Một câu để nhớ:** image production lý tưởng **không có** compiler, `git`, hay cả shell nếu không cần. Mỗi thứ thừa là 1 rủi ro.

**✅ Tự chấm** *(đánh dấu khi làm được mà không nhìn tài liệu):*
- [ ] Viết Dockerfile multi-stage và thấy image nhỏ hơn bản 1-stage rõ rệt
- [ ] Giải thích vì sao image nhỏ = an toàn hơn (không chỉ nhẹ hơn)
- [ ] Chạy container bằng `USER` thường và kiểm bằng `whoami`
- [ ] Nói được vì sao tránh tag `latest` ở production
- [ ] Dùng `docker history` tìm layer phình

✅ **Kết quả đạt được:** Tối ưu image nhỏ gọn, bảo mật, chạy bằng user thường — kỹ năng Docker chuyên nghiệp.

---

## Ngày 19 — Docker: Volume, Network & dữ liệu bền vững

> ⏱️ ~90 phút · Loại: Docker
>
> 🧭 **Bạn đang ở đâu:** Ngày 18 (tối ưu image) → **Ngày 19 (lưu dữ liệu bền vững + cho container nói chuyện)** → Ngày 20 (Docker Compose). Đây là 2 mảnh còn thiếu để ghép nhiều container thành 1 hệ thống thật.
>
> ✅ **Chuẩn bị:** Docker chạy được. Sẽ dùng image `postgres` để minh hoạ dữ liệu bền vững.

### 📘 Lý thuyết

#### 1. Vấn đề: container "khỏe nhưng hay quên"

Container thiết kế để *dùng xong vứt* (ephemeral). Xoá container = mất sạch dữ liệu bên trong. Vậy database chạy trong container thì sao? → cần **Volume**.

#### 2. Ba cách lưu trữ

| Loại | Cú pháp | Dùng khi |
|---|---|---|
| **Volume** (khuyến nghị) | `-v tên:/path` | Dữ liệu quan trọng (database) — Docker quản lý, backup được |
| **Bind mount** | `-v /host/path:/path` | Dev — gắn thẳng thư mục máy, sửa code thấy ngay |
| **tmpfs** | `--tmpfs /path` | Dữ liệu tạm trong RAM (không bền vững) |

Volume nằm **ngoài** vòng đời container → xoá container, dữ liệu vẫn còn.

#### 3. Docker Network — cách container "nói chuyện"

| Mode | Dùng khi |
|---|---|
| `bridge` (mặc định) | Đa số — container có IP riêng, cô lập |
| `host` | Cần hiệu năng mạng tối đa (mất cô lập) |
| `none` | Container không cần mạng |

- Tạo: `docker network create mynet`; dùng: `--network mynet` khi `run`.
- **DNS nội bộ:** container cùng network gọi nhau bằng **tên** (không cần IP). Vd app gọi DB bằng `db:5432` — Docker tự dịch `db` → IP container database. Đây là nền tảng ghép microservice.

#### 4. Inspect

`docker volume inspect <vol>`, `docker network inspect <net>` để xem chi tiết.

> 🔑 Dữ liệu quan trọng (nhất là database) **bắt buộc** để trong volume. Cẩn thận `docker compose down -v` — chữ `-v` xoá luôn volume = **mất dữ liệu thật**.

### 📖 Hiểu rõ hơn (giải thích cho người mới)

> 📘 đã có bảng 3 cách lưu trữ và các network mode. Mục này cho bạn **hình dung** để nhớ.

**Container "hay quên" là cố ý, không phải lỗi.** Triết lý container là *dùng xong vứt* (ephemeral): xoá và tạo lại thoải mái để dễ scale, dễ nâng cấp. Nhưng dữ liệu thì không được "vứt" theo. Volume tách phần *dữ liệu cần giữ* ra khỏi phần *container dùng một lần* — nhờ đó bạn xoá/thay container mà database vẫn nguyên. Hình dung volume là ổ cứng gắn ngoài, còn container là chiếc laptop có thể đổi bất cứ lúc nào.

**Volume vs bind mount — cùng "gắn ổ" nhưng khác mục đích.** Volume do Docker quản lý (backup/di chuyển được, hợp cho database production). Bind mount trỏ thẳng vào một thư mục trên máy bạn — tiện cho *dev* vì sửa code trên máy là container thấy ngay, nhưng phụ thuộc đường dẫn máy nên không hợp production.

**Đặt tên là có DNS — nền tảng của microservice.** Khi các container ở *cùng một network do bạn tạo*, Docker cấp cho mỗi container một "cái tên gọi được": app cứ kết nối tới `db:5432`, Docker tự dịch tên `db` ra IP hiện thời. Bạn không bao giờ phải hard-code IP (vốn đổi mỗi lần tạo lại). Lưu ý cái bẫy: mạng `bridge` *mặc định* KHÔNG có DNS theo tên — phải tự tạo network mới có.

### 🧪 Lab cơ bản

> Mục tiêu: chứng minh volume giữ dữ liệu qua xoá container, và 2 container gọi nhau qua tên.

**Bước 1 — Chứng minh dữ liệu bền vững với volume.**
```bash
docker volume create dbdata
docker run -d --name pg -v dbdata:/var/lib/postgresql/data \
  -e POSTGRES_PASSWORD=secret postgres:16-alpine
docker exec -it pg psql -U postgres -c "CREATE TABLE t(x int); INSERT INTO t VALUES(42);"
docker rm -f pg          # XOÁ container
docker run -d --name pg -v dbdata:/var/lib/postgresql/data \
  -e POSTGRES_PASSWORD=secret postgres:16-alpine
docker exec -it pg psql -U postgres -c "SELECT * FROM t;"
```
Bạn sẽ thấy `42` vẫn còn dù đã xoá container — nhờ volume.

**Bước 2 — Tạo network riêng và cho 2 container nói chuyện.**
```bash
docker network create mynet
docker run -d --name db --network mynet -e POSTGRES_PASSWORD=secret postgres:16-alpine
docker run -it --rm --network mynet postgres:16-alpine \
  psql -h db -U postgres -c "SELECT 1;"     # gọi DB bằng TÊN "db", không cần IP
```

**Bước 3 — Bind mount cho dev.**
```bash
docker run -d --name web -p 8080:80 -v "$(pwd)":/usr/share/nginx/html:ro nginx
# sửa file index.html trên máy → tải lại trình duyệt thấy đổi ngay
```

**Bước 4 — Inspect.**
```bash
docker volume inspect dbdata
docker network inspect mynet     # thấy các container đang nối
```

**Bước 5 — Dọn dẹp.**
```bash
docker rm -f pg db web; docker network rm mynet
# (giữ hoặc xoá volume: docker volume rm dbdata)
```

### 🚀 Lab nâng cao (best-practice)

> Mục tiêu: tách biệt dữ liệu và mạng đúng chuẩn production.

1. **Volume cho dữ liệu, bind mount cho dev** — đừng nhầm vai trò: database production luôn dùng **named volume** (Docker quản lý, backup được), bind mount chỉ cho dev (sửa code nóng).
2. **Tách network theo tầng** — frontend không cần thấy database:
   ```bash
   docker network create frontend
   docker network create backend
   # app nối cả 2; db chỉ nối backend → cô lập, an toàn hơn
   ```
3. **Backup volume đúng cách:**
   ```bash
   docker run --rm -v mydata:/data -v $(pwd):/backup alpine \
     tar -czf /backup/mydata-backup.tar.gz -C /data .
   ```
4. **Không bao giờ** đặt dữ liệu quan trọng trong lớp ghi của container — luôn ra volume.

### 💡 Bổ sung thực tế: network mode & bẫy "dữ liệu biến mất"

- **3 network mode cần biết:**
  | Mode | Dùng khi |
  |---|---|
  | `bridge` (mặc định) | đa số trường hợp — container có IP riêng, cô lập |
  | `host` | cần hiệu năng mạng tối đa, container dùng thẳng mạng host (mất cô lập) |
  | `none` | container không cần mạng (job xử lý offline) |
- **Bẫy kinh điển:** "dữ liệu DB biến mất sau khi `docker compose down`". Lý do: quên khai báo volume, dữ liệu nằm trong lớp ghi của container → xóa container là mất. **Database BẮT BUỘC có volume.**
- **DNS nội bộ là chìa khóa microservice:** app kết nối DB bằng `postgres://db:5432` (tên service `db`), không phải IP. Docker tự phân giải tên trong cùng network.
- **`docker compose down -v` xóa cả volume** — lệnh nguy hiểm, đọc kỹ trước khi gõ trên môi trường có dữ liệu thật.

### 🧭 Hướng dẫn làm lab & giải nghĩa lệnh (cho người tự học)

> Làm tuần tự, dừng ở mỗi ✅ **Checkpoint**.

**Bước 1 — Kiểm chứng "không volume = mất dữ liệu".**
```bash
docker run -d --name pg-tmp -e POSTGRES_PASSWORD=secret postgres:16-alpine
docker exec -it pg-tmp psql -U postgres -c "CREATE TABLE t(x int);"
docker rm -f pg-tmp
# tạo lại KHÔNG volume → bảng t biến mất
```
✅ **Checkpoint:** hiểu container không volume → xoá là mất sạch.

**Bước 2 — Làm lại CÓ volume (theo Lab Bước 1).**
✅ **Checkpoint:** sau khi xoá & tạo lại container, `SELECT * FROM t;` vẫn ra `42`.
💡 Volume nằm NGOÀI vòng đời container → dữ liệu sống sót.

**Bước 3 — 2 container gọi nhau qua tên.**
```bash
docker network inspect mynet | grep Name
```
✅ **Checkpoint:** `psql -h db` (dùng tên) kết nối được — không cần biết IP.
💡 DNS nội bộ là nền tảng để app gọi `db:5432` trong microservice.

### 🐛 Gỡ lỗi nhanh

| Triệu chứng | Nguyên nhân | Cách sửa |
|---|---|---|
| Dữ liệu DB mất sau khi tái tạo container | Quên gắn volume | `-v tên:/var/lib/postgresql/data` |
| Container A không gọi được B bằng tên | Không cùng network, hoặc dùng default bridge | Tạo network riêng, cùng `--network`; default bridge KHÔNG có DNS theo tên |
| `docker compose down -v` mất dữ liệu | `-v` xoá cả volume | Không dùng `-v` khi có dữ liệu thật cần giữ |
| Bind mount không thấy file | Sai đường dẫn host / quyền | Dùng đường dẫn tuyệt đối; kiểm quyền thư mục |
| Volume ngốn đĩa | Volume mồ côi tích tụ | `docker volume ls`, `docker volume prune` (cẩn thận) |

### 📝 Bài ôn tập & Demo đối chiếu

**✍️ Tự kiểm tra:**

<details>
<summary>1. Volume và bind mount khác nhau, khi nào dùng cái nào?</summary>

> Volume do Docker quản lý, dùng cho dữ liệu quan trọng (database) — backup được, bền vững. Bind mount gắn thẳng thư mục máy vào container, tiện cho dev (sửa code thấy ngay).
</details>

<details>
<summary>2. 2 container gọi nhau qua tên thế nào?</summary>

> Đặt chúng vào **cùng một network do bạn tạo** (`docker network create`), rồi gọi bằng tên container/service (Docker có DNS nội bộ). Default bridge không hỗ trợ DNS theo tên.
</details>

<details>
<summary>3. Vì sao database trong container BẮT BUỘC có volume?</summary>

> Vì container ephemeral — xoá/tái tạo là mất dữ liệu ở lớp ghi. Volume nằm ngoài vòng đời container nên giữ được dữ liệu.
</details>

<details>
<summary>4. `docker compose down -v` nguy hiểm ở chỗ nào?</summary>

> Cờ `-v` xoá luôn các volume → mất dữ liệu thật. Bình thường chỉ `down` (không `-v`).
</details>

**🔬 Demo đối chiếu:**

| Demo đối chiếu | Kết quả mong đợi |
|---|---|
| Tạo volume, xoá container, tạo lại | Dữ liệu vẫn còn (`42`) |
| `docker network ls` | Hiện network vừa tạo |
| `psql -h db` qua tên | Kết nối thành công |

### 📚 Thuật ngữ Anh–Việt (ngày này)

| Thuật ngữ | Nghĩa |
|---|---|
| **Volume** | Ổ lưu dữ liệu bền vững do Docker quản lý |
| **Bind mount** | Gắn thẳng thư mục host vào container |
| **Ephemeral** | Tạm thời — xoá là mất |
| **Network (bridge/host/none)** | Mạng của container |
| **DNS nội bộ** | Gọi container bằng tên trong cùng network |
| **Persistent data** | Dữ liệu bền vững (giữ qua restart) |
| **tmpfs** | Lưu trong RAM, không bền vững |

### 🎯 Đúc kết Ngày 19

**3 điều phải mang theo:**
1. **Container ephemeral → dữ liệu quan trọng BẮT BUỘC ra volume** (nhất là database). Xoá container, volume vẫn còn.
2. **Volume** (Docker quản lý, cho production) khác **bind mount** (trỏ thư mục máy, cho dev).
3. **Cùng network tự tạo → gọi nhau bằng tên** (DNS nội bộ). `bridge` mặc định không có DNS theo tên.

> 🧠 **Một câu để nhớ:** dữ liệu quan trọng (nhất là database) **bắt buộc** để trong volume. Và cẩn thận `docker compose down -v` — chữ `-v` xoá luôn volume = mất dữ liệu thật.

**✅ Tự chấm** *(đánh dấu khi làm được mà không nhìn tài liệu):*
- [ ] Chứng minh volume giữ dữ liệu qua việc xoá & tạo lại container
- [ ] Phân biệt khi nào dùng volume, khi nào bind mount
- [ ] Cho 2 container gọi nhau qua tên trong network tự tạo
- [ ] Giải thích vì sao `bridge` mặc định không gọi được theo tên
- [ ] Nói được `docker compose down -v` nguy hiểm ở đâu

✅ **Kết quả đạt được:** Quản lý dữ liệu bền vững (volume) và mạng giữa các container — 2 mảnh để ghép hệ thống thật.

---

## Ngày 20 — Docker Compose: Quản lý multi-container

> ⏱️ ~90 phút · Loại: Docker
>
> 🧭 **Bạn đang ở đâu:** Ngày 19 (volume & network) → **Ngày 20 (mô tả cả hệ thống nhiều container trong 1 file)** → Ngày 21 (Milestone full-stack). Compose là công cụ bạn dùng mỗi ngày cho local/dev.
>
> ✅ **Chuẩn bị:** Docker + Docker Compose (`docker compose version`). App Node từ Ngày 17 để ghép với database.

### 📘 Lý thuyết

#### 1. Vấn đề: app thật có nhiều mảnh

Một web app thật gồm frontend + backend + database + cache... Chạy từng `docker run` (kèm cả tá `-p`, `-v`, `--network`) rất cực và dễ sai.

#### 2. Docker Compose — "1 file mô tả cả dàn nhạc"

Viết 1 file `docker-compose.yml` (YAML) liệt kê mọi service, network, volume. Rồi:

| Lệnh | Làm gì |
|---|---|
| `docker compose up -d` | Tạo & chạy tất cả service (nền) |
| `docker compose ps` | Xem trạng thái các service |
| `docker compose logs -f` | Xem log gộp mọi service |
| `docker compose down` | Tắt tất cả (thêm `-v` = xoá cả volume ⚠️) |
| `docker compose config` | In cấu hình đã merge (bắt lỗi YAML sớm) |

#### 3. Cấu trúc file

Các khoá chính: `services` (danh sách dịch vụ), mỗi service có `image` hoặc `build`, `ports`, `volumes`, `environment`, `depends_on`, `networks`.

#### 4. Biến môi trường & scale

- File `.env` được Compose **tự đọc** → không hard-code mật khẩu trong YAML.
- Scale: `docker compose up --scale web=3` (3 bản của service `web`).

#### 5. `depends_on` — cái bẫy người mới

`depends_on` chỉ đảm bảo container khởi động *theo thứ tự*, **KHÔNG** đảm bảo dịch vụ bên trong đã *sẵn sàng*. DB "đã start" nhưng còn đang khởi tạo → app connect lỗi. Giải pháp: thêm **healthcheck** + `condition: service_healthy`.

> 🔑 Compose tuyệt cho **dev và app nhỏ**. Cần tự scale, tự phục hồi, chạy nhiều máy → đó là việc của Kubernetes (Giai đoạn 3). Đừng ép Compose làm việc của K8s.

### 📖 Hiểu rõ hơn (giải thích cho người mới)

> 📘 đã có bảng lệnh và cấu trúc file Compose. Mục này cho bạn **hình dung** để nhớ.

**Compose biến "trí nhớ trong đầu" thành "file trong Git".** Chạy tay 4 container nghĩa là bạn phải nhớ đúng 4 lệnh `docker run` kèm cả tá cờ `-p -v --network` — sai một cờ là hỏng, và không ai khác lặp lại được. Compose gói tất cả vào một file `docker-compose.yml`: cả hệ thống trở thành *tài liệu chạy được*, ai clone về gõ `up` cũng ra y hệt. Đây chính là tinh thần "mọi thứ là code" áp cho môi trường dev.

**Nhạc trưởng, không phải nhạc công.** Một lệnh `up` dựng cả dàn (tạo network, volume, khởi động service đúng thứ tự); một lệnh `down` dẹp gọn. Bạn điều khiển *cả hệ thống* như một khối, thay vì bấm nút từng container.

**Cái bẫy `depends_on` mà gần như ai cũng dính.** `depends_on` chỉ đảm bảo thứ tự *bật* container — nó KHÔNG biết dịch vụ bên trong đã *sẵn sàng nhận kết nối* chưa. Database container "đã lên" nhưng Postgres còn đang khởi tạo vài giây → app lao vào kết nối và ăn lỗi. Cách đúng: gắn `healthcheck` cho DB rồi để app chờ `condition: service_healthy` (hoặc để app tự retry). "Đã chạy" và "đã sẵn sàng" là hai chuyện khác nhau.

### 🧪 Lab cơ bản

> Mục tiêu: dựng stack web + database + adminer chỉ bằng 1 file và 1 lệnh.

**Bước 1 — Tạo `.env`** (Compose tự đọc):
```bash
POSTGRES_PASSWORD=secret123
```

**Bước 2 — Viết `docker-compose.yml`** (file đầy đủ):
```yaml
services:
  db:
    image: postgres:16-alpine
    environment:
      POSTGRES_PASSWORD: ${POSTGRES_PASSWORD}
    volumes:
      - dbdata:/var/lib/postgresql/data
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U postgres"]
      interval: 5s
      retries: 5
  adminer:
    image: adminer
    ports:
      - "8080:8080"
    depends_on:
      db:
        condition: service_healthy
volumes:
  dbdata:
```

**Bước 3 — Chạy toàn bộ.**
```bash
docker compose up -d
docker compose ps        # thấy db (healthy) + adminer (Up)
```
Mở `http://localhost:8080` (Adminer) → đăng nhập vào Postgres (server `db`, user `postgres`, mật khẩu từ `.env`).

**Bước 4 — Xem log gộp và validate.**
```bash
docker compose config    # in cấu hình đã merge (thấy biến .env đã thay)
docker compose logs -f   # Ctrl+C để dừng theo dõi
```

**Bước 5 — Test dữ liệu bền vững.**
```bash
docker compose down      # KHÔNG có -v → giữ volume
docker compose up -d     # dữ liệu DB vẫn còn
```

### 🚀 Lab nâng cao (best-practice)

> Mục tiêu: viết Compose chuẩn — có healthcheck, thứ tự đúng, secret an toàn.

1. **`depends_on` với điều kiện healthcheck** (không chỉ "đã start" mà "đã sẵn sàng"):
   ```yaml
   services:
     app:
       build: .
       depends_on:
         db:
           condition: service_healthy
     db:
       image: postgres:16-alpine
       environment:
         POSTGRES_PASSWORD_FILE: /run/secrets/db_pass
       healthcheck:
         test: ["CMD-SHELL", "pg_isready -U postgres"]
         interval: 5s
         retries: 5
       volumes:
         - dbdata:/var/lib/postgresql/data
   volumes:
     dbdata:
   ```
2. **Tách file theo môi trường:** `docker-compose.yml` (base) + `docker-compose.override.yml` (dev) / `docker-compose.prod.yml`.
3. **Đặt `restart: unless-stopped`** cho dịch vụ production.
4. **Validate trước khi chạy:** `docker compose config` (in cấu hình đã merge, bắt lỗi YAML sớm).

### 💡 Bổ sung thực tế: depends_on KHÔNG đảm bảo gì & profiles

- **Hiểu lầm chết người:** `depends_on` (không kèm condition) chỉ đảm bảo **thứ tự khởi động container**, KHÔNG đảm bảo dịch vụ bên trong đã **sẵn sàng nhận kết nối**. DB container "up" nhưng Postgres còn đang khởi tạo → app connect lỗi. → Luôn cần **healthcheck** hoặc app tự retry kết nối.
- **`profiles`** — bật/tắt nhóm dịch vụ (vd chỉ chạy `adminer`/`mailhog` khi dev):
  ```yaml
  adminer:
    image: adminer
    profiles: ["dev"]      # chỉ lên khi: docker compose --profile dev up
  ```
- **Compose cho dev, không phải production scale:** Compose tuyệt cho local/staging và app nhỏ. Khi cần HA, auto-scaling, self-healing → Kubernetes (Giai đoạn 3). Đừng cố ép Compose làm việc của K8s.
- **`.env` ≠ bảo mật:** `.env` chỉ tiện, không phải kho secret. Thêm `.env` vào `.gitignore`; production dùng secret manager.

### 🧭 Hướng dẫn làm lab & giải nghĩa lệnh (cho người tự học)

> Làm tuần tự, dừng ở mỗi ✅ **Checkpoint**.

**Bước 1 — Validate cấu hình TRƯỚC khi chạy.**
```bash
docker compose config
```
✅ **Checkpoint:** in ra cấu hình đã merge, thấy `${POSTGRES_PASSWORD}` đã thay bằng giá trị thật từ `.env`.
💡 Bắt lỗi YAML (thụt lề sai) sớm, trước khi tốn công `up`.

**Bước 2 — Chạy và kiểm tra trạng thái.**
```bash
docker compose up -d
docker compose ps
```
✅ **Checkpoint:** `db` hiện `(healthy)`, `adminer` hiện `Up`.

**Bước 3 — Hiểu `depends_on` + healthcheck.**
✅ **Checkpoint:** `adminer` chỉ start SAU khi `db` đã `healthy` (nhờ `condition: service_healthy`).
💡 Bỏ `condition` đi → adminer có thể lên trước khi DB sẵn sàng → lỗi kết nối. `depends_on` trơn chỉ đảm bảo **thứ tự start**, không đảm bảo **sẵn sàng**.

**Bước 4 — Test bền vững & dọn.**
```bash
docker compose down       # giữ volume
docker compose up -d      # dữ liệu còn
docker compose down -v    # ⚠️ chỉ khi muốn XOÁ sạch cả dữ liệu
```
✅ **Checkpoint:** phân biệt được `down` (giữ dữ liệu) vs `down -v` (xoá sạch).

### 🐛 Gỡ lỗi nhanh

| Triệu chứng | Nguyên nhân | Cách sửa |
|---|---|---|
| `yaml: line X: ...` | Thụt lề YAML sai (dùng tab) | Dùng **space** (2 space), `docker compose config` để kiểm |
| App connect DB lỗi lúc khởi động | `depends_on` không chờ DB sẵn sàng | Thêm `healthcheck` + `condition: service_healthy`, hoặc app tự retry |
| Biến `.env` không được thay | `.env` không cùng thư mục / sai tên | Đặt `.env` cạnh compose; kiểm bằng `docker compose config` |
| Mất dữ liệu sau `down` | Lỡ dùng `-v` | Không dùng `-v`; hoặc backup volume trước |
| Port conflict | Cổng host đã bị chiếm | Đổi `ports` sang cổng khác |

### 📝 Bài ôn tập & Demo đối chiếu

**✍️ Tự kiểm tra:**

<details>
<summary>1. Compose giúp gì so với chạy nhiều `docker run`?</summary>

> Mô tả cả hệ thống (nhiều service + network + volume) trong 1 file YAML, khởi động/tắt tất cả bằng 1 lệnh, tái lập được và version hoá được.
</details>

<details>
<summary>2. `depends_on` đảm bảo gì và KHÔNG đảm bảo gì?</summary>

> Đảm bảo **thứ tự khởi động container**. KHÔNG đảm bảo dịch vụ bên trong đã **sẵn sàng nhận kết nối**. Cần healthcheck + `condition: service_healthy`.
</details>

<details>
<summary>3. Viết service Compose tối giản chạy nginx cổng 8080.</summary>

> ```yaml
> services:
>   web:
>     image: nginx
>     ports:
>       - "8080:80"
> ```
</details>

<details>
<summary>4. Khi nào KHÔNG nên dùng Compose mà cần Kubernetes?</summary>

> Khi cần auto-scaling, self-healing, chạy trên nhiều máy, high availability — đó là việc của K8s (GĐ3). Compose hợp cho dev/local & app nhỏ.
</details>

**🔬 Demo đối chiếu:**

| Demo đối chiếu | Kết quả mong đợi |
|---|---|
| `docker compose up -d` | Các service `Creating ... done` |
| `docker compose ps` | db `(healthy)`, adminer `Up` |
| Mở `localhost:8080` | Adminer đăng nhập được vào Postgres |

### 📚 Thuật ngữ Anh–Việt (ngày này)

| Thuật ngữ | Nghĩa |
|---|---|
| **Docker Compose** | Công cụ mô tả & chạy nhiều container bằng 1 file |
| **Service** | Một dịch vụ (container) trong compose |
| **`depends_on`** | Khai báo thứ tự khởi động |
| **healthcheck** | Kiểm tra dịch vụ đã sẵn sàng chưa |
| **`.env`** | File biến môi trường Compose tự đọc |
| **`condition: service_healthy`** | Chờ service kia khoẻ mới start |
| **profiles** | Bật/tắt nhóm service theo môi trường |

### 🎯 Đúc kết Ngày 20

**3 điều phải mang theo:**
1. **Compose = cả hệ thống trong 1 file YAML**, `up`/`down` một lệnh, tái lập & version hoá được.
2. **`depends_on` chỉ đảm bảo thứ tự bật, KHÔNG đảm bảo sẵn sàng** → cần `healthcheck` + `condition: service_healthy` hoặc app tự retry.
3. **`.env` Compose tự đọc** (đừng hard-code mật khẩu); `docker compose config` để validate trước khi `up`.

> 🧠 **Một câu để nhớ:** Compose tuyệt cho **dev và app nhỏ**. Khi cần tự scale, tự phục hồi, chạy nhiều máy → đó là việc của Kubernetes (Giai đoạn 3). Đừng ép Compose làm việc của K8s.

**✅ Tự chấm** *(đánh dấu khi làm được mà không nhìn tài liệu):*
- [ ] Viết `docker-compose.yml` dựng ≥2 service liên kết nhau
- [ ] Dùng `.env` cho biến, và `docker compose config` để kiểm
- [ ] Giải thích `depends_on` đảm bảo gì / không đảm bảo gì
- [ ] Thêm `healthcheck` + `condition: service_healthy`
- [ ] Phân biệt `down` và `down -v`

✅ **Kết quả đạt được:** Định nghĩa và chạy ứng dụng đa container bằng 1 lệnh, hiểu healthcheck & thứ tự khởi động.

---

## Ngày 21 — MILESTONE: Đóng gói ứng dụng full-stack

> ⏱️ ~150 phút · Loại: LAB Final
>
> 🧭 **Bạn đang ở đâu:** Ngày 16–20 (Docker, Dockerfile, multi-stage, volume, mạng, Compose) → **Ngày 21 (ghép thành một hệ thống nhiều tầng hoàn chỉnh)** → Ngày 22 (YAML, cấu hình).
>
> ✅ **Chuẩn bị:** Docker và Docker Compose đang chạy.
>
> 🎯 **Đề bài + tiêu chí chấm.** Không hướng dẫn từng bước.

### 📋 Đề bài — "Đóng gói một hệ thống ba tầng"

> Bạn nhận một ứng dụng gồm frontend, API backend và database. Nhiệm vụ: đóng gói toàn bộ sao cho **người khác clone repo về, chạy một lệnh, là hệ thống lên** — không cài Node, không cài PostgreSQL, không đọc hướng dẫn dài.

```text
   Trình duyệt :8080
        │
        ▼
   [ nginx ] ──/api──> [ backend ] ──> [ postgres ]
   (frontend)           (API)           (dữ liệu bền)
```

### ✅ Yêu cầu

#### Bắt buộc

| # | Yêu cầu | Kiến thức từ |
|---|---|---|
| 1 | Ba dịch vụ chạy bằng **một lệnh** `docker compose up -d` | Ngày 20 |
| 2 | Backend dùng **multi-stage build**, image dưới 200 MB | Ngày 18 |
| 3 | Container **không chạy bằng root** | Ngày 17 |
| 4 | Dữ liệu database **sống sót** khi xoá và tạo lại container | Ngày 19 |
| 5 | Backend và database **không lộ cổng ra ngoài** — chỉ nginx mở | Ngày 19 |
| 6 | Backend chờ database **sẵn sàng** rồi mới khởi động | Ngày 20 |
| 7 | Có `HEALTHCHECK` cho backend và database | Ngày 17 |
| 8 | Biến môi trường trong `.env`, có `.env.example`, **không commit `.env`** | Ngày 20 |
| 9 | `.dockerignore` đầy đủ | Ngày 17, 18 |
| 10 | README: chạy thế nào, dừng thế nào, xoá sạch thế nào | — |

#### Nâng cao

| # | Yêu cầu |
|---|---|
| 11 | Có profile `dev` (nạp lại code tự động) và `prod` (tối ưu) |
| 12 | Giới hạn log để không đầy ổ đĩa |
| 13 | Khai `resources.limits` cho từng dịch vụ |
| 14 | Script `khoi-dong.sh` một lệnh: dựng, chờ khoẻ, in địa chỉ truy cập |
| 15 | Image dưới 100 MB (dùng distroless hoặc alpine tối giản) |

### 📐 Tiêu chí chấm (100 điểm)

| Hạng mục | Điểm | Đạt tối đa khi |
|---|---:|---|
| Chạy được bằng một lệnh | 15 | `docker compose up -d` từ repo sạch là lên, không thao tác thêm |
| Chất lượng Dockerfile | 20 | Multi-stage, user thường, cache layer đúng thứ tự, `.dockerignore` |
| Kích thước image | 10 | Backend dưới 200 MB (dưới 100 MB được tối đa) |
| Dữ liệu bền | 15 | Xoá container, tạo lại, dữ liệu còn nguyên |
| Mạng & bảo mật | 15 | Chỉ nginx lộ cổng; backend/db chỉ thấy trong mạng nội bộ |
| Thứ tự khởi động & healthcheck | 10 | Backend chờ db khoẻ; mọi dịch vụ có healthcheck |
| Quản lý cấu hình | 10 | `.env` + `.env.example`, không commit bí mật |
| Tài liệu | 5 | README đủ để người lạ chạy được |

> 🎯 **Từ 75 điểm** là vững để sang phần Cloud.

### 🧪 Bộ kiểm chứng

```bash
#!/usr/bin/env bash
# cham-diem.sh — tự chấm LAB Final Docker
diem=0
kiem() {
  if eval "$2" &>/dev/null; then echo "  ✅ $1 (+$3)"; diem=$((diem+$3));
  else echo "  ❌ $1"; fi
}

echo "▸ Khởi động"
kiem "Ba dịch vụ đang chạy" "[ \$(docker compose ps --services --filter status=running | wc -l) -ge 3 ]" 15

echo "▸ Dockerfile"
kiem "Backend không chạy bằng root" "[ \"\$(docker compose exec -T backend whoami)\" != 'root' ]" 8
kiem "Có multi-stage build"         "grep -c 'FROM' backend/Dockerfile | grep -qE '[2-9]'" 7
kiem "Có .dockerignore"             "[ -f backend/.dockerignore ]" 5

echo "▸ Kích thước image"
kich_thuoc=$(docker images --format '{{.Repository}} {{.Size}}' | grep backend | head -1)
echo "  ℹ️  $kich_thuoc"

echo "▸ Mạng"
kiem "nginx lộ cổng ra ngoài"       "docker compose port nginx 80" 5
kiem "Backend KHÔNG lộ cổng"        "! docker compose port backend 3000 2>/dev/null | grep -q ." 5
kiem "Database KHÔNG lộ cổng"       "! docker compose port db 5432 2>/dev/null | grep -q ." 5

echo "▸ Healthcheck"
kiem "Backend có healthcheck"       "docker inspect \$(docker compose ps -q backend) --format '{{.Config.Healthcheck}}' | grep -q CMD" 5
kiem "Database có healthcheck"      "docker inspect \$(docker compose ps -q db) --format '{{.Config.Healthcheck}}' | grep -q CMD" 5

echo "▸ Cấu hình"
kiem "Có .env.example"              "[ -f .env.example ]" 5
kiem ".env KHÔNG bị commit"         "! git ls-files | grep -q '^\.env$'" 5
kiem "Có README"                    "[ -f README.md ]" 5

echo ""
echo "  ĐIỂM (phần tự động): $diem / 75"
echo "  25 điểm còn lại: dữ liệu bền + thứ tự khởi động — kiểm bằng 2 phép thử dưới"
```

### 🔥 Hai phép thử quyết định

**Phép thử 1 — Dữ liệu có thật sự bền không? (15 điểm)**

```bash
# Ghi dữ liệu
docker compose exec -T db psql -U postgres -c \
  "CREATE TABLE thu(id serial, ten text); INSERT INTO thu(ten) VALUES ('kiem-chung');"

# Xoá SẠCH container (giữ volume)
docker compose down
docker compose up -d
sleep 10

# Dữ liệu phải còn
docker compose exec -T db psql -U postgres -c "SELECT * FROM thu;"
```
> Mất dữ liệu nghĩa là bạn chưa gắn volume, hoặc gắn sai đường dẫn.

**Phép thử 2 — Người lạ có chạy được không? (15 điểm)**

```bash
# Mô phỏng người mới clone repo
cd /tmp && rm -rf thu-nghiem
git clone <repo-cua-ban> thu-nghiem && cd thu-nghiem
cp .env.example .env         # bước duy nhất được phép yêu cầu
docker compose up -d
sleep 20
curl -s localhost:8080
```
> Phải chạy được. Mỗi bước thủ công thêm là một lỗ hổng trong đóng gói của bạn.

### ⚠️ Những cái bẫy hay gặp

| Bẫy | Hậu quả | Cách tránh |
|---|---|---|
| `COPY . .` trước `RUN npm ci` | Sửa một dòng code là cài lại toàn bộ thư viện | Copy `package*.json` trước |
| Dùng `ports` cho backend/db | Lộ database ra Internet | Dùng `expose`, hoặc không khai gì |
| `depends_on` không kèm `condition` | Backend khởi động khi db chưa sẵn sàng → crash | `condition: service_healthy` |
| Gắn volume sai đường dẫn dữ liệu | Tưởng có volume mà vẫn mất dữ liệu | Kiểm bằng Phép thử 1 |
| Commit `.env` | Lộ mật khẩu | `.gitignore` từ commit đầu |
| Không có `.dockerignore` | Build chậm, image lẫn `node_modules` và `.git` | Tạo ngay từ đầu |

### 💬 Gợi ý khi bí

<details>
<summary><b>Làm sao để backend chờ database thật sự sẵn sàng?</b></summary>

`depends_on` thường chỉ chờ container **khởi động**, không chờ nó **sẵn sàng nhận kết nối**. Phải kết hợp healthcheck:

```yaml
  db:
    image: postgres:16-alpine
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U postgres"]
      interval: 5s
      timeout: 3s
      retries: 5

  backend:
    depends_on:
      db:
        condition: service_healthy    # chờ db BÁO KHOẺ mới khởi động
```

Nhưng đừng phụ thuộc hoàn toàn vào Compose: ứng dụng vẫn nên **tự thử lại kết nối**. Database có thể khởi động lại giữa chừng, và lúc đó Compose không giúp gì được.
</details>

<details>
<summary><b>Làm sao giảm kích thước image backend?</b></summary>

Theo thứ tự hiệu quả giảm dần:

1. **Đổi image nền:** `node:20` (~1,1 GB) → `node:20-alpine` (~140 MB). Hiệu quả nhất, chỉ một dòng.
2. **Multi-stage:** tầng build cài cả devDependencies, tầng cuối chỉ chép `node_modules` production và code.
3. **`npm ci --omit=dev`:** bỏ toàn bộ thư viện chỉ dùng khi phát triển.
4. **`.dockerignore`:** đừng gửi `node_modules`, `.git`, `test` vào trình build.
5. **Distroless** (`gcr.io/distroless/nodejs20`): nhỏ nhất và an toàn nhất, nhưng **không có shell** — không `docker exec` vào debug được. Đánh đổi có ý thức.

Xem lớp nào nặng nhất: `docker history <image> --human --format "{{.Size}}\t{{.CreatedBy}}" | head -10`
</details>

### 🎯 Đúc kết Ngày 21 — Tổng kết phần Docker

**3 điều phải mang theo:**

1. **"Một lệnh là chạy" là tiêu chuẩn, không phải điều xa xỉ.** Mỗi bước thủ công bạn bắt người dùng làm là một chỗ họ có thể làm sai.
2. **Container là đồ dùng một lần, volume thì không.** Ranh giới đó quyết định bạn mất dữ liệu hay chỉ mất một container.
3. **Chỉ lộ ra thứ cần lộ.** Database không bao giờ nên nhìn thấy được từ Internet — nguyên tắc này đúng từ Docker Compose cho tới Kubernetes.

> 🧠 **Một câu để nhớ:** đóng gói tốt được đo bằng **số bước người lạ phải làm để chạy được hệ thống** — càng ít càng tốt, lý tưởng là một.

**✅ Tự chấm Milestone:**

- [ ] Đạt từ 75 điểm trở lên
- [ ] Phép thử 1: dữ liệu sống sót sau `down` rồi `up`
- [ ] Phép thử 2: người lạ clone về chạy được
- [ ] Image backend dưới 200 MB
- [ ] Giải thích được vì sao mỗi dịch vụ dùng `expose` hay `ports`

✅ **Kết quả đạt được:** Một hệ thống ba tầng đóng gói hoàn chỉnh, chạy bằng một lệnh ở bất cứ máy nào có Docker — sẵn sàng để đưa lên cloud ở Ngày 26–28.

---

## Ngày 22 — YAML, JSON & định dạng cấu hình

> ⏱️ ~60 phút · Loại: DevOps
>
> 🧭 **Bạn đang ở đâu:** Ngày 21 (Milestone Docker) → **Ngày 22 (ngôn ngữ cấu hình của cả ngành: YAML/JSON)** → Ngày 23 (Nginx). Mọi công cụ sau này (Compose, K8s, CI/CD, Ansible) đều viết bằng YAML — nắm chắc hôm nay để đỡ khổ về sau.
>
> ✅ **Chuẩn bị:** cài `jq` và `yq` (`sudo apt install -y jq`; yq tải từ GitHub), và `yamllint` (`pip install yamllint`).

### 📘 Lý thuyết

#### 1. YAML & JSON — hai cách viết cấu hình

| | YAML | JSON |
|---|---|---|
| Dùng ở đâu | Cấu hình (Compose, K8s, CI/CD, Ansible) | Đầu ra API & CLI (`docker inspect`, `kubectl -o json`) |
| Cú pháp | Thụt lề (space), dễ đọc cho người | Ngoặc nhọn `{}`, mảng `[]` |
| Quan hệ | JSON hợp lệ **cũng là** YAML hợp lệ | Tập con của YAML |

#### 2. Cú pháp YAML cốt lõi

```yaml
# comment bắt đầu bằng #
key: value              # cặp khoá-giá trị (nhớ khoảng trắng sau :)
danh_sach:              # danh sách dùng dấu -
  - phan_tu_1
  - phan_tu_2
long_nhau:
  con:                  # cấp bậc thể hiện bằng THỤT LỀ (space, KHÔNG tab)
    chau: 123
```

#### 3. `jq` và `yq` — "dao mổ" JSON/YAML

- `jq` lọc/trích JSON: `curl ... | jq '.field'`.
- `yq` xử lý/sửa YAML: `yq '.services.web.image = "nginx:1.27"' -i file.yml`.

#### 4. Anchor & alias — chống lặp trong YAML

```yaml
x-common: &common          # định nghĩa 1 lần
  restart: unless-stopped
services:
  web: { image: nginx, <<: *common }   # tái dùng bằng *
```

#### 5. Cạm bẫy YAML (ai cũng dính 1 lần)

- **TAB bị cấm** — phải thụt lề bằng **space**. Lỗi #1.
- **"Norway problem":** `country: NO` bị hiểu thành `false`! (cùng `yes/no/on/off`) → quote chuỗi dễ nhầm: `"NO"`.
- Thiếu khoảng trắng sau `:` (`key:value` ❌ → `key: value` ✅).

> 🔑 YAML báo lỗi khó hiểu? Đừng soi mắt thường — dùng `yamllint` hoặc `docker compose config` để máy chỉ ra lỗi.

### 📖 Hiểu rõ hơn (giải thích cho người mới)

> 📘 đã có bảng so sánh YAML/JSON và cạm bẫy. Mục này cho bạn **hình dung** để nhớ.

**Vì sao học YAML lại "đáng tiền" đến vậy?** Vì nó là *ngôn ngữ chung* của gần như mọi công cụ bạn sẽ gặp: Docker Compose, Kubernetes, GitHub Actions, Ansible... đều viết bằng YAML. Nắm chắc một lần, xài lại cả sự nghiệp. JSON thì thường xuất hiện ở chiều ngược lại — là *đầu ra* của các lệnh (`docker inspect`, `kubectl -o json`, API) để máy khác đọc.

**`jq`/`yq` biến "biển chữ" thành đúng một dòng bạn cần.** Output của công cụ DevOps thường dài hàng trăm dòng JSON. Thay vì mắt dò, bạn "hỏi" đúng phần cần: `... | jq '.[0].NetworkSettings.IPAddress'`. Đây là kỹ năng tự động hoá then chốt — hầu hết script vận hành đều có một khúc lọc JSON như vậy.

**Vì sao YAML hay "cắn" người mới?** Vì nó dựa vào *khoảng trắng* để hiểu cấp bậc — thứ mắt người rất khó soi. Hai thủ phạm kinh điển: (1) lỡ dùng **TAB** thay space; (2) "Norway problem" — `NO`, `yes`, `on`, `off` không quote bị hiểu thành boolean. Cách sống sót không phải căng mắt nhìn, mà là để máy kiểm: `yamllint`, `docker compose config`, `kubectl --dry-run`.

### 🧪 Lab cơ bản

> Mục tiêu: viết YAML đúng cú pháp, lọc JSON bằng jq, và thấy tận mắt lỗi thụt lề.

**Bước 1 — Viết file YAML `app.yml`.**
```yaml
app:
  name: my-app
  port: 3000
servers:
  - host: web-01
    ip: 10.0.0.11
  - host: web-02
    ip: 10.0.0.12
```

**Bước 2 — Validate.**
```bash
yamllint app.yml        # không báo lỗi = OK
```

**Bước 3 — Lọc JSON bằng jq.**
```bash
curl -s https://api.github.com | jq '.current_user_url'
echo '{"users":[{"name":"An","active":true},{"name":"Bo","active":false}]}' \
  | jq '.users[] | select(.active) | .name'      # in: "An"
```

**Bước 4 — Chuyển JSON ↔ YAML bằng yq.**
```bash
yq -o=json app.yml          # in ra dạng JSON tương đương
```

**Bước 5 — Cố tạo lỗi để thấy báo.**
```bash
printf "a:\n\tb: 1\n" > loi.yml     # dùng TAB
yamllint loi.yml                    # báo lỗi tab/thụt lề
```

### 🚀 Lab nâng cao (best-practice)

> Mục tiêu: dùng jq/yq như công cụ hàng ngày để xử lý output JSON/YAML của mọi công cụ DevOps.

1. **jq thực chiến** — lọc output JSON của các CLI (docker, kubectl, aws đều xuất JSON):
   ```bash
   docker inspect web | jq '.[0].NetworkSettings.IPAddress'
   curl -s api/users | jq '.[] | select(.active==true) | .name'   # lọc + trích
   ```
2. **yq sửa file YAML từ script** (tự động hóa, không sửa tay):
   ```bash
   yq '.services.web.image = "nginx:1.27"' -i docker-compose.yml
   ```
3. **Anchor/alias chống lặp** trong YAML lớn:
   ```yaml
   x-common: &common
     restart: unless-stopped
     logging: { driver: json-file, options: { max-size: "10m" } }
   services:
     web: { image: nginx, <<: *common }
     api: { image: myapi, <<: *common }
   ```
4. **Validate trong CI** — `yamllint .` chặn YAML lỗi trước khi merge.

### 💡 Bổ sung thực tế: vì sao YAML "đau" và cách tránh

- **Thủ phạm #1 gây lỗi YAML: TAB.** YAML cấm tab để thụt lề. Cấu hình editor hiển thị whitespace và auto-convert tab → space.
- **Bẫy "Norway problem":** `country: NO` bị YAML hiểu thành `false` (boolean)! Tương tự `yes/no/on/off`. → Luôn **quote chuỗi** dễ nhầm: `country: "NO"`, `version: "3.9"` (số cũng nên quote khi cần giữ nguyên).
- **JSON là tập con của YAML** — mọi JSON hợp lệ đều là YAML hợp lệ. Tiện khi cần dán nhanh.
- **Quy tắc khi debug cấu hình lạ:** chạy `yamllint` + `docker compose config`/`kubectl --dry-run` để máy validate, đừng soi mắt thường.

### 🧭 Hướng dẫn làm lab & giải nghĩa lệnh (cho người tự học)

> Làm tuần tự, dừng ở mỗi ✅ **Checkpoint**.

**Bước 1 — Viết & validate YAML.**
```bash
yamllint app.yml
```
✅ **Checkpoint:** không có dòng lỗi nào in ra.
💡 Thụt lề bằng **space** (2 space/cấp), danh sách bằng `-`, nhớ khoảng trắng sau `:`.

**Bước 2 — Lọc JSON có điều kiện.**
```bash
echo '{"users":[{"name":"An","active":true},{"name":"Bo","active":false}]}' \
  | jq '.users[] | select(.active) | .name'
```
✅ **Checkpoint:** in `"An"` (lọc đúng user active).
💡 `jq` xử lý output JSON của mọi CLI DevOps (docker/kubectl/aws đều xuất JSON).

**Bước 3 — Trải nghiệm lỗi TAB.**
```bash
printf "a:\n\tb: 1\n" > loi.yml && yamllint loi.yml
```
✅ **Checkpoint:** yamllint báo lỗi liên quan tab/thụt lề.

**Bước 4 — Bẫy "Norway problem".**
```bash
echo 'country: NO' | yq '.country'      # ra false (boolean)!
echo 'country: "NO"' | yq '.country'    # ra "NO" (đúng)
```
✅ **Checkpoint:** thấy `NO` không quote biến thành `false` — nhớ quote chuỗi dễ nhầm.

### 🐛 Gỡ lỗi nhanh

| Triệu chứng | Nguyên nhân | Cách sửa |
|---|---|---|
| `found character '\t'` | Dùng tab thụt lề | Đổi hết tab → space; cấu hình editor hiện whitespace |
| `mapping values are not allowed` | Thiếu space sau `:` hoặc thụt lề sai | `key: value` (có space); dùng `yamllint` |
| Giá trị `NO`/`yes`/`on` bị đổi thành boolean | Norway problem | Quote chuỗi: `"NO"` |
| `jq: error: Cannot index...` | Truy cập sai đường dẫn JSON | Xem cấu trúc trước: `jq '.'`; rồi đi từng cấp |
| Số phiên bản `3.10` thành `3.1` | YAML hiểu là số | Quote: `version: "3.10"` |

### 📝 Bài ôn tập & Demo đối chiếu

**✍️ Tự kiểm tra:**

<details>
<summary>1. Vì sao YAML cấm dùng tab để thụt lề?</summary>

> YAML dùng thụt lề để thể hiện cấp bậc; tab hiển thị khác nhau trên mỗi editor → gây nhập nhằng. Chuẩn YAML bắt buộc space.
</details>

<details>
<summary>2. Viết YAML mô tả danh sách 3 server (tên + IP).</summary>

> ```yaml
> servers:
>   - {host: web-01, ip: 10.0.0.11}
>   - {host: web-02, ip: 10.0.0.12}
>   - {host: web-03, ip: 10.0.0.13}
> ```
</details>

<details>
<summary>3. `jq` dùng để làm gì?</summary>

> Lọc, trích, biến đổi dữ liệu JSON từ dòng lệnh — rất hữu ích để xử lý output của docker/kubectl/aws.
</details>

<details>
<summary>4. "Norway problem" là gì?</summary>

> `NO` (và `yes/no/on/off`) không quote bị YAML hiểu thành boolean `false/true`. Luôn quote chuỗi dễ nhầm: `"NO"`.
</details>

**🔬 Demo đối chiếu:**

| Demo đối chiếu | Kết quả mong đợi |
|---|---|
| `yamllint app.yml` | Không báo lỗi |
| `jq` lọc JSON | In đúng giá trị cần |
| `yq -o=json app.yml` | JSON tương đương, đúng cấu trúc |

### 📚 Thuật ngữ Anh–Việt (ngày này)

| Thuật ngữ | Nghĩa |
|---|---|
| **YAML** | Định dạng cấu hình dựa trên thụt lề |
| **JSON** | Định dạng dữ liệu ngoặc nhọn (API/CLI output) |
| **jq / yq** | Công cụ lọc/xử lý JSON / YAML |
| **Indentation** | Thụt lề (thể hiện cấp bậc trong YAML) |
| **Anchor & alias** (`&`, `*`) | Định nghĩa 1 lần, tái dùng nhiều nơi |
| **Lint** | Kiểm tra cú pháp tự động (`yamllint`) |
| **Norway problem** | Bẫy `NO` → `false` khi không quote |

### 🎯 Đúc kết Ngày 22

**3 điều phải mang theo:**
1. **YAML = ngôn ngữ cấu hình của cả ngành** (Compose/K8s/CI/CD/Ansible); JSON = đầu ra của API & CLI. JSON hợp lệ cũng là YAML hợp lệ.
2. **Thụt lề bằng SPACE, không bao giờ TAB**; nhớ khoảng trắng sau `:`; quote chuỗi dễ nhầm (`"NO"`, `"3.10"`).
3. **`jq`/`yq`** để lọc/sửa JSON/YAML từ dòng lệnh — công cụ tự động hoá hằng ngày.

> 🧠 **Một câu để nhớ:** khi YAML báo lỗi khó hiểu, đừng soi mắt thường — dùng `yamllint` hoặc `docker compose config` để máy chỉ ra lỗi.

**✅ Tự chấm** *(đánh dấu khi làm được mà không nhìn tài liệu):*
- [ ] Viết YAML nhiều cấp đúng cú pháp và `yamllint` sạch
- [ ] Lọc JSON có điều kiện bằng `jq` (dùng `select`)
- [ ] Chuyển YAML ↔ JSON bằng `yq`
- [ ] Nhận diện & sửa lỗi TAB và "Norway problem"
- [ ] Nói được khi nào gặp YAML, khi nào gặp JSON trong công việc

✅ **Kết quả đạt được:** Đọc/viết YAML và JSON thành thạo, dùng jq/yq — ngôn ngữ cấu hình của toàn bộ DevOps.

---

## Ngày 23 — Reverse Proxy & Web Server (Nginx chuyên sâu)

> ⏱️ ~90 phút · Loại: SysOps
>
> 🧭 **Bạn đang ở đâu:** Ngày 22 (YAML/JSON) → **Ngày 23 (nginx: reverse proxy, load balancing, HTTPS)** → Ngày 24 (Database). Kiến thức này dùng lại nguyên ở Kubernetes — Ingress Controller thường chính là nginx.
>
> ✅ **Chuẩn bị:** một app backend để proxy tới (vd app Node Ngày 17 chạy cổng 3000). nginx cài trực tiếp hoặc chạy container.

### 📘 Lý thuyết

#### 1. Reverse proxy là gì (hay gây bối rối)

"Proxy" = người trung gian. Hai loại:
- **Forward proxy** đứng trước *client* (giấu người dùng — như VPN).
- **Reverse proxy** đứng trước *server* (giấu máy chủ). nginx ở đây là reverse proxy — "lễ tân" nhận mọi request từ Internet rồi chuyển vào backend phía trong.

#### 2. Reverse proxy làm được gì

| Việc | Lợi ích |
|---|---|
| **Che giấu** backend | Internet chỉ thấy nginx |
| **Load balancing** | Nhiều backend → chia request luân phiên |
| **SSL/HTTPS termination** | nginx lo mã hoá, backend nhẹ gánh, chứng chỉ quản 1 chỗ |
| **Serve static + cache + gzip** | Nhanh hơn |

#### 3. Cấu trúc config nginx

```nginx
server {
    listen 80;
    server_name example.com;
    location / {
        proxy_pass http://localhost:3000;   # chuyển request tới backend
    }
}
```
Các khối chính: `server` (1 site), `location` (đường dẫn), `proxy_pass` (chuyển tiếp), `listen`, `server_name`.

#### 4. Load balancing với `upstream`

```nginx
upstream backend {
    server 127.0.0.1:3001;
    server 127.0.0.1:3002;      # round-robin mặc định; least_conn nếu muốn
}
```

#### 5. Kiểm tra & reload — kỷ luật bắt buộc

`nginx -t` (test cú pháp) → `systemctl reload nginx` (nạp config mới, giữ kết nối liên tục).

> 🔑 Sửa config sai mà `restart` = nginx **không lên lại** = **website chết**. Luôn `nginx -t` TRƯỚC, rồi `reload` (không `restart`). HTTPS miễn phí: Let's Encrypt + `certbot --nginx`.

### 📖 Hiểu rõ hơn (giải thích cho người mới)

> 📘 đã có bảng chức năng và cấu trúc config. Mục này cho bạn **hình dung** để nhớ.

**"Forward" hay "reverse" — nhìn xem nó đứng che cho ai.** Forward proxy đứng trước *client*, che người dùng (như VPN: server thấy proxy, không thấy bạn). Reverse proxy đứng trước *server*, che máy chủ (client thấy nginx, không thấy backend thật phía sau). Cùng là "trung gian", nhưng quay mặt về hai phía khác nhau — nhớ được điều này là hết bối rối.

**Một nginx làm được việc của nhiều thứ.** Cùng một con nginx vừa là cửa ngõ nhận request, vừa chia tải cho nhiều backend, vừa gánh phần mã hoá HTTPS (SSL termination) để backend nhẹ đi, vừa phục vụ file tĩnh và cache. Vì "đa năng" như vậy nên kiến thức nginx theo bạn rất xa — ở Kubernetes (GĐ3), thứ đứng ngoài nhận traffic (Ingress Controller) thường *chính là* nginx.

**"Test trước, nạp sau" là kỷ luật, không phải lời khuyên.** Config nginx sai cú pháp mà bạn `restart` thì nginx tắt và *không lên lại được* = website chết ngay. Vì thế luôn `nginx -t` để máy soi cú pháp trước; hợp lệ mới `reload` (nạp nóng, giữ kết nối đang chạy liên tục). Một dấu `;` quên có thể là khác biệt giữa "êm ru" và "sự cố lúc nửa đêm".

### 🧪 Lab cơ bản

> Mục tiêu: cấu hình nginx làm reverse proxy + load balancing, test config đúng cách.

**Bước 1 — Chạy 2 backend giả để proxy tới.**
```bash
docker run -d --name b1 -p 3001:80 nginxdemos/hello
docker run -d --name b2 -p 3002:80 nginxdemos/hello
```

**Bước 2 — Viết config `/etc/nginx/conf.d/lab.conf`** (hoặc file riêng nếu dùng container):
```nginx
upstream backend {
    server 127.0.0.1:3001;
    server 127.0.0.1:3002;
}
server {
    listen 8080;
    location / {
        proxy_pass http://backend;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```

**Bước 3 — Test config TRƯỚC khi reload.**
```bash
sudo nginx -t
```
Bạn sẽ thấy: `syntax is ok` và `test is successful`.

**Bước 4 — Reload và kiểm tra load balancing.**
```bash
sudo nginx -s reload      # hoặc: systemctl reload nginx
curl localhost:8080       # refresh nhiều lần → server ID luân phiên b1/b2
```

**Bước 5 — (Tuỳ chọn) HTTPS thật.**
```bash
sudo certbot --nginx -d example.com     # cần domain thật trỏ về máy
```

### 🚀 Lab nâng cao (best-practice)

> Mục tiêu: cấu hình nginx như một reverse proxy production — có HTTPS, header bảo mật, gzip.

1. **Reverse proxy chuẩn với header đầy đủ:**
   ```nginx
   location / {
       proxy_pass http://backend;
       proxy_set_header Host $host;
       proxy_set_header X-Real-IP $remote_addr;
       proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
       proxy_set_header X-Forwarded-Proto $scheme;
   }
   ```
   > Thiếu các header này, app backend không biết IP thật của client (log sai, rate-limit sai).
2. **HTTPS thật miễn phí với Certbot** + tự động gia hạn:
   ```bash
   sudo certbot --nginx -d example.com
   sudo systemctl status certbot.timer   # tự gia hạn chứng chỉ
   ```
3. **Header bảo mật** (HSTS, X-Frame-Options) và **gzip** cho hiệu năng.
4. **Rate limiting** chống lạm dụng:
   ```nginx
   limit_req_zone $binary_remote_addr zone=api:10m rate=10r/s;
   ```

### 💡 Bổ sung thực tế: forward vs reverse proxy & "luôn nginx -t trước reload"

- **Forward proxy vs Reverse proxy:**
  | | Đứng trước | Phục vụ |
  |---|---|---|
  | Forward proxy | client | giấu client (VPN, lọc nội dung) |
  | Reverse proxy | server | giấu server, LB, SSL, cache |
- **`nginx -t` trước `reload` là kỷ luật bắt buộc:** config lỗi + `restart` = nginx **không lên lại** = website chết. `reload` chỉ nạp config mới nếu hợp lệ, giữ kết nối hiện tại liên tục.
- **SSL termination:** nginx giải mã HTTPS rồi nói HTTP với backend nội bộ → backend nhẹ gánh, chứng chỉ quản lý 1 chỗ.
- **Nginx là "dao đa năng":** reverse proxy, load balancer, static server, API gateway, cache — hiểu sâu nó là khoản đầu tư xứng đáng (các ingress controller K8s ở GĐ3 thường chính là nginx).

### 🧭 Hướng dẫn làm lab & giải nghĩa lệnh (cho người tự học)

> Làm tuần tự, dừng ở mỗi ✅ **Checkpoint**.

**Bước 1 — Luôn `nginx -t` trước khi reload.**
```bash
sudo nginx -t
```
✅ **Checkpoint:** `syntax is ok` + `test is successful`.
💡 Cố tình bỏ 1 dấu `;` rồi chạy lại `nginx -t` → nó báo **đúng dòng** lỗi. Đây là lý do luôn test trước.

**Bước 2 — Reload (không restart).**
```bash
sudo nginx -s reload
```
✅ **Checkpoint:** web vẫn phục vụ liên tục (không đứt kết nối).
⚠️ `restart` khi config lỗi = nginx không lên lại = **web chết**. Luôn `-t` rồi `reload`.

**Bước 3 — Xem load balancing hoạt động.**
```bash
for i in 1 2 3 4; do curl -s localhost:8080 | grep -i "server address"; done
```
✅ **Checkpoint:** địa chỉ server luân phiên giữa 2 backend (round-robin).

**Bước 4 — Hiểu vai trò header.**
✅ **Checkpoint:** hiểu vì sao cần `proxy_set_header X-Real-IP` — thiếu nó backend log sai IP client (nhìn ai cũng thành IP của nginx).

### 🐛 Gỡ lỗi nhanh

| Triệu chứng | Nguyên nhân | Cách sửa |
|---|---|---|
| Web chết sau khi sửa config | `restart` với config lỗi | Luôn `nginx -t` trước; sửa lỗi rồi `reload` |
| `502 Bad Gateway` | Backend không tới được | Kiểm backend chạy chưa (`curl` trực tiếp); đúng địa chỉ `proxy_pass` |
| `504 Gateway Timeout` | Backend phản hồi chậm/treo | Kiểm backend; tăng `proxy_read_timeout` |
| Backend log toàn 1 IP (của nginx) | Thiếu header X-Real-IP/X-Forwarded-For | Thêm `proxy_set_header` |
| `address already in use` | Cổng `listen` bị chiếm | Đổi cổng hoặc dừng dịch vụ đang giữ |

### 📝 Bài ôn tập & Demo đối chiếu

**✍️ Tự kiểm tra:**

<details>
<summary>1. Reverse proxy khác forward proxy thế nào?</summary>

> Reverse proxy đứng trước **server** (giấu backend, load balance, SSL, cache). Forward proxy đứng trước **client** (giấu người dùng — như VPN/lọc nội dung).
</details>

<details>
<summary>2. `proxy_pass` làm gì?</summary>

> Chuyển tiếp request nginx nhận được tới một backend (địa chỉ/upstream) — trái tim của reverse proxy.
</details>

<details>
<summary>3. Vì sao luôn `nginx -t` trước khi reload?</summary>

> Config lỗi mà reload/restart có thể làm nginx không phục vụ được = web chết. `nginx -t` kiểm cú pháp trước, an toàn.
</details>

<details>
<summary>4. `502` và `504` khác nhau thế nào?</summary>

> 502 Bad Gateway = không kết nối được backend (backend chết/sai địa chỉ). 504 Gateway Timeout = kết nối được nhưng backend phản hồi quá chậm.
</details>

**🔬 Demo đối chiếu:**

| Demo đối chiếu | Kết quả mong đợi |
|---|---|
| `nginx -t` | `syntax is ok, test is successful` |
| Truy cập `localhost:8080` | Chuyển tới backend qua nginx |
| Refresh nhiều lần | Server luân phiên (load balancing) |

### 📚 Thuật ngữ Anh–Việt (ngày này)

| Thuật ngữ | Nghĩa |
|---|---|
| **Reverse proxy** | Proxy đứng trước server |
| **`proxy_pass`** | Chuyển tiếp request tới backend |
| **upstream** | Nhóm backend để load balance |
| **Load balancing** | Chia tải giữa nhiều backend |
| **SSL/TLS termination** | nginx giải mã HTTPS thay backend |
| **`nginx -t`** | Test cú pháp config |
| **Ingress Controller** | "nginx của Kubernetes" (GĐ3) |

### 🎯 Đúc kết Ngày 23

**3 điều phải mang theo:**
1. **Reverse proxy đứng trước server** (che backend, load balance, SSL termination, cache); forward proxy đứng trước client.
2. **`nginx -t` TRƯỚC, rồi `reload` (không `restart`)** — config lỗi + restart = web chết.
3. **`proxy_pass` + header** (`X-Real-IP`, `X-Forwarded-For`) để backend biết IP thật của client; `upstream` để chia tải.

> 🧠 **Một câu để nhớ:** nginx là "dao đa năng" (web server, reverse proxy, load balancer, cache). Kiến thức này dùng lại nguyên ở Kubernetes — Ingress Controller thường chính là nginx.

**✅ Tự chấm** *(đánh dấu khi làm được mà không nhìn tài liệu):*
- [ ] Cấu hình nginx reverse proxy `proxy_pass` tới 1 backend
- [ ] Dùng `upstream` chia tải 2 backend và quan sát round-robin
- [ ] Luôn `nginx -t` trước khi `reload`
- [ ] Giải thích vì sao cần `X-Real-IP`/`X-Forwarded-For`
- [ ] Phân biệt lỗi `502` và `504`

✅ **Kết quả đạt được:** Cấu hình reverse proxy, load balancing, hiểu SSL termination — kỹ năng vận hành web quan trọng.

---

## Ngày 24 — Cơ sở dữ liệu cho DevOps

> ⏱️ ~90 phút · Loại: SysOps
>
> 🧭 **Bạn đang ở đâu:** Ngày 23 (Nginx) → **Ngày 24 (vận hành database: chạy, backup, restore, bảo mật)** → Ngày 25 (Git nâng cao). DevOps không cần là DBA, nhưng phải giữ database *chạy an toàn và cứu được khi hỏng*.
>
> ✅ **Chuẩn bị:** Docker chạy được (để chạy Postgres/Redis). Ôn lại volume (Ngày 19) và backup (Ngày 11).

### 📘 Lý thuyết

#### 1. Vai trò DevOps với database

Bạn **không** cần là chuyên gia tối ưu query. Việc của DevOps: **triển khai, backup, khôi phục, giám sát, bảo mật** database. Hiểu đủ để vận hành an toàn.

#### 2. SQL vs NoSQL — chọn cái nào

| Loại | Ví dụ | Dùng khi |
|---|---|---|
| **SQL** (quan hệ) | PostgreSQL, MySQL | Dữ liệu có quan hệ, cần giao dịch (ACID) — **mặc định chọn cái này** |
| **Redis** | (key-value, trong RAM) | Cache, session, hàng đợi, rate-limit — rất nhanh |
| **MongoDB** | (document) | Schema linh hoạt, hay thay đổi |

#### 3. Chạy DB bằng container (ôn Ngày 19)

Luôn kèm **volume** để dữ liệu bền vững:
```bash
docker run -d --name db -v pgdata:/var/lib/postgresql/data \
  -e POSTGRES_PASSWORD=secret postgres:16-alpine
```

#### 4. Backup/restore — KHÁC backup file thường

Không copy thẳng file dữ liệu DB đang chạy (ra bản **không nhất quán**). Dùng công cụ chuyên dụng:
```bash
docker exec db pg_dump -U postgres --single-transaction mydb | gzip > mydb.sql.gz   # backup
gunzip -c mydb.sql.gz | docker exec -i db psql -U postgres mydb                       # restore
```
`--single-transaction` = ảnh chụp nhất quán mà không khoá bảng.

#### 5. Migration — sửa schema an toàn

Đừng sửa cấu trúc bảng bằng tay trên production. Dùng **migration tool** (Flyway, Liquibase, Alembic, Prisma) — schema được version hoá, rollback được, áp dụng theo thứ tự.

#### 6. Bảo mật DB — 3 việc PHẢI làm

1. Backup tự động + **test restore** định kỳ.
2. **Không** expose cổng DB ra Internet (chỉ network nội bộ; truy cập xa qua SSH tunnel — Ngày 8).
3. Mật khẩu mạnh, không dùng mặc định.

> 🔑 Production nên cân nhắc **managed DB** (RDS/Cloud SQL/Azure DB) để khỏi tự lo backup, HA, patching. Tự host thì phải rất chắc về volume + backup + replication.

### 📖 Hiểu rõ hơn (giải thích cho người mới)

> 📘 đã có bảng SQL/NoSQL và các lệnh backup. Mục này cho bạn **hình dung** để nhớ.

**Vai trò DevOps với database: người gác cổng, không phải kiến trúc sư dữ liệu.** Bạn không cần tối ưu truy vấn tinh vi (việc của DBA/dev). Việc của bạn là giữ nó *sống an toàn và cứu được khi hỏng*: triển khai, backup, khôi phục, giám sát, khoá cửa bảo mật. Chọn loại DB cũng theo tư duy đơn giản: mặc định SQL (Postgres/MySQL) cho dữ liệu có quan hệ; Redis khi cần *nhanh và tạm* (cache/session); MongoDB khi schema hay đổi.

**Vì sao không copy thẳng file dữ liệu để backup?** Vì DB đang chạy *liên tục ghi* — chép file lúc đó chẳng khác nào chụp ảnh người đang chạy: nhoè, nửa vời, restore không lên. `pg_dump`/`mysqldump` (với `--single-transaction`) "chụp" một ảnh *nhất quán* tại một thời điểm mà không cần khoá bảng. Đây là khác biệt cốt lõi giữa backup DB và backup file thường.

**Backup chưa test restore = chưa có backup.** Rất nhiều người ngủ ngon với đống file dump để rồi phát hiện chúng hỏng đúng lúc cần nhất. Vòng đời thật phải là: dump → *thử* drop → restore → kiểm dữ liệu khớp. Và tuyệt đối đừng sửa cấu trúc bảng bằng tay trên production — dùng *migration tool* (Flyway/Liquibase/Alembic) để mọi thay đổi được version hoá và rollback được.

### 🧪 Lab cơ bản

> Mục tiêu: chạy Postgres có volume, tạo dữ liệu, backup rồi **test restore** — vòng đời DB thật.

**Bước 1 — Chạy Postgres có volume.**
```bash
docker run -d --name db -v pgdata:/var/lib/postgresql/data \
  -e POSTGRES_PASSWORD=secret postgres:16-alpine
```

**Bước 2 — Tạo bảng & chèn dữ liệu.**
```bash
docker exec -it db psql -U postgres -c \
  "CREATE TABLE users(id serial, name text); INSERT INTO users(name) VALUES('An'),('Bo');"
docker exec -it db psql -U postgres -c "SELECT * FROM users;"     # thấy An, Bo
```

**Bước 3 — Backup.**
```bash
docker exec db pg_dump -U postgres --single-transaction postgres > backup.sql
ls -lh backup.sql
```

**Bước 4 — Xoá dữ liệu rồi RESTORE.**
```bash
docker exec -it db psql -U postgres -c "DROP TABLE users;"
cat backup.sql | docker exec -i db psql -U postgres
docker exec -it db psql -U postgres -c "SELECT * FROM users;"     # An, Bo trở lại
```

**Bước 5 — Thử Redis.**
```bash
docker run -d --name cache redis:alpine
docker exec -it cache redis-cli set ten "DevOps"
docker exec -it cache redis-cli get ten        # in: "DevOps"
```

### 🚀 Lab nâng cao (best-practice)

> Mục tiêu: vận hành DB an toàn + quản lý schema bằng migration (không sửa schema bằng tay trên production).

1. **Backup nhất quán + nén + timestamp** (nhắc lại Ngày 11, áp dụng cho DB):
   ```bash
   docker exec db pg_dump -U postgres --single-transaction mydb | gzip > mydb-$(date +%F).sql.gz
   ```
2. **Migration bằng công cụ** thay vì chạy SQL tay — schema được version hóa, rollback được:
   - Flyway / Liquibase (đa ngôn ngữ), hoặc migration tích hợp framework (Prisma, Alembic, Sequelize).
   ```bash
   flyway migrate    # áp dụng các file V1__, V2__... theo thứ tự, idempotent
   ```
3. **Connection pooling** (PgBouncer) — DB có giới hạn kết nối; app scale lên là cạn ngay nếu không pool.
4. **DB tuyệt đối không expose ra internet** — chỉ network nội bộ; truy cập từ xa qua SSH tunnel (Ngày 8).

### 💡 Bổ sung thực tế: chọn SQL/NoSQL & "DB trong container ở production?"

- **Khi nào SQL, khi nào NoSQL:**
  | Chọn | Khi |
  |---|---|
  | **SQL** (Postgres/MySQL) | dữ liệu có quan hệ, cần giao dịch (ACID), báo cáo phức tạp — **mặc định nên chọn cái này** |
  | **Redis** | cache, session, hàng đợi, rate-limit — nhanh, trong RAM |
  | **MongoDB** | document linh hoạt, schema thay đổi nhiều |
- **DB stateful trong container — cẩn trọng:** chạy DB trong Docker tốt cho dev/test. Production thì cân nhắc **managed DB** (RDS/Cloud SQL/Azure DB) để khỏi tự lo backup, HA, patching — hoặc nếu tự host thì phải rất chắc về volume + backup + replication.
- **3 việc DevOps PHẢI làm với mọi DB:** (1) backup tự động + **test restore**, (2) giám sát (kết nối, dung lượng, query chậm), (3) không để mật khẩu mặc định / không expose port.
- **Migration là một chiều an toàn:** luôn viết migration **forward**, có kế hoạch rollback, test trên staging trước. Sửa schema tay trên production là công thức gây sự cố.

### 🧭 Hướng dẫn làm lab & giải nghĩa lệnh (cho người tự học)

> Làm tuần tự, dừng ở mỗi ✅ **Checkpoint**. Trọng tâm: vòng backup → restore.

**Bước 1 — Chạy DB & tạo dữ liệu.**
```bash
docker exec -it db psql -U postgres -c "\dt"    # liệt kê bảng
```
✅ **Checkpoint:** kết nối được, thấy bảng `users` với dữ liệu An/Bo.

**Bước 2 — Backup nhất quán.**
```bash
docker exec db pg_dump -U postgres --single-transaction postgres | gzip > b.sql.gz
```
✅ **Checkpoint:** file `b.sql.gz` được tạo.
💡 `--single-transaction` chụp ảnh nhất quán mà không khoá bảng — an toàn cả khi DB đang chạy.

**Bước 3 — Test restore (bước quan trọng nhất).**
```bash
docker exec -it db psql -U postgres -c "DROP TABLE users;"
gunzip -c b.sql.gz | docker exec -i db psql -U postgres
docker exec -it db psql -U postgres -c "SELECT * FROM users;"
```
✅ **Checkpoint:** An/Bo trở lại → backup thực sự dùng được.
💡 Backup chưa test restore = backup giả (Ngày 11).

**Bước 4 — Kiểm chứng bảo mật.**
✅ **Checkpoint:** DB chỉ nghe trong network nội bộ / không map cổng ra ngoài → máy khác không kết nối thẳng được.

### 🐛 Gỡ lỗi nhanh

| Triệu chứng | Nguyên nhân | Cách sửa |
|---|---|---|
| Restore ra dữ liệu hỏng/nửa vời | Đã copy file DB thay vì dump | Dùng `pg_dump`/`mysqldump` |
| `password authentication failed` | Sai user/mật khẩu | Kiểm biến `POSTGRES_PASSWORD`, user đúng chưa |
| App connect DB `Connection refused` | DB chưa sẵn sàng / sai host | Chờ healthcheck; dùng tên service trong cùng network |
| DB bị dò từ Internet | Lỡ map cổng `-p 5432:5432` ra ngoài | Bỏ map cổng; chỉ để network nội bộ; truy cập xa qua SSH tunnel |
| Đổi schema làm vỡ app | Sửa tay trên production | Dùng migration tool, test staging trước |

### 📝 Bài ôn tập & Demo đối chiếu

**✍️ Tự kiểm tra:**

<details>
<summary>1. Khi nào chọn SQL, khi nào NoSQL?</summary>

> SQL (Postgres/MySQL) khi dữ liệu có quan hệ + cần giao dịch (ACID) — mặc định nên chọn. Redis cho cache/session (nhanh, trong RAM). MongoDB cho document schema linh hoạt.
</details>

<details>
<summary>2. Viết lệnh pg_dump backup database `mydb`.</summary>

> `pg_dump -U postgres --single-transaction mydb | gzip > mydb-$(date +%F).sql.gz`
</details>

<details>
<summary>3. Vì sao không expose cổng database ra Internet?</summary>

> DB lộ ra ngoài là mục tiêu tấn công/dò mật khẩu. Chỉ để network nội bộ; truy cập từ xa qua SSH tunnel hoặc VPN.
</details>

<details>
<summary>4. Vì sao không backup DB bằng copy file thẳng?</summary>

> DB đang ghi → file copy ở trạng thái nửa vời, không nhất quán, restore lỗi. Dùng `pg_dump`/`mysqldump` để có ảnh chụp nhất quán.
</details>

**🔬 Demo đối chiếu:**

| Demo đối chiếu | Kết quả mong đợi |
|---|---|
| Kết nối DB | `psql` đăng nhập, `\dt` liệt kê bảng |
| Tạo bảng & chèn | `SELECT *` trả bản ghi vừa thêm |
| Backup & restore | Dump → drop → restore → dữ liệu khớp |

### 📚 Thuật ngữ Anh–Việt (ngày này)

| Thuật ngữ | Nghĩa |
|---|---|
| **SQL / NoSQL** | CSDL quan hệ / phi quan hệ |
| **ACID** | Đảm bảo giao dịch chính xác |
| **`pg_dump` / `mysqldump`** | Công cụ backup DB nhất quán |
| **Migration** | Thay đổi schema có version, rollback được |
| **Connection pooling** | Tái dùng kết nối DB (PgBouncer) |
| **Managed DB** | DB do cloud vận hành (RDS/Cloud SQL) |
| **Replication** | Nhân bản DB để HA/đọc mở rộng |

### 🎯 Đúc kết Ngày 24

**3 điều phải mang theo:**
1. **DevOps lo vận hành DB** (triển khai, backup, restore, giám sát, bảo mật) — không cần thành DBA. Mặc định chọn SQL.
2. **Backup DB phải dùng `pg_dump`/`mysqldump`** (ảnh chụp nhất quán), KHÔNG copy file thẳng. Và **luôn test restore**.
3. **Bảo mật DB:** không expose cổng ra Internet, mật khẩu mạnh, sửa schema qua migration tool (không sửa tay production).

> 🧠 **Một câu để nhớ:** 3 việc PHẢI làm với mọi DB: (1) backup tự động + **test restore**, (2) **không** expose cổng DB ra Internet, (3) mật khẩu mạnh. Sửa cấu trúc bảng thì dùng *migration tool*, không sửa tay trên production.

**✅ Tự chấm** *(đánh dấu khi làm được mà không nhìn tài liệu):*
- [ ] Chạy Postgres có volume và tạo dữ liệu
- [ ] Backup bằng `pg_dump --single-transaction`
- [ ] Đi trọn vòng drop → restore → kiểm dữ liệu khớp
- [ ] Giải thích vì sao không copy file DB để backup
- [ ] Nói được 3 việc bảo mật bắt buộc với mọi DB

✅ **Kết quả đạt được:** Triển khai, backup/restore database trong container, hiểu bảo mật & migration — vận hành DB an toàn.

---

## Ngày 25 — Git nâng cao — Rebase, Tag, Workflow

> ⏱️ ~90 phút · Loại: Git
>
> 🧭 **Bạn đang ở đâu:** Ngày 15 (GitHub/PR) → **Ngày 25 (Git chuyên nghiệp: rebase, tag, versioning)** → Ngày 26 (Cloud). Đây là các kỹ năng Git "level team" — lịch sử sạch, version có ý nghĩa, changelog tự động.
>
> ✅ **Chuẩn bị:** repo Git có nhiều commit để tập rebase/tag (có thể dùng repo `my-app`).

### 📘 Lý thuyết

#### 1. Merge vs Rebase — 2 cách gộp, khác ở "lịch sử"

| | Lịch sử | Dùng khi |
|---|---|---|
| **merge** | Giữ nguyên, có "merge commit" (hình cây) | Nhánh chung, muốn giữ ngữ cảnh thật |
| **rebase** | Viết lại thành **tuyến tính** (thẳng, sạch) | Nhánh riêng, dọn trước khi mở PR |

> ⚠️ **Quy tắc vàng:** KHÔNG rebase nhánh **đã push/chia sẻ**. Rebase nhánh người khác đang dùng = phá lịch sử của họ → hỗn loạn.

#### 2. Interactive rebase — dọn commit

`git rebase -i HEAD~3` mở editor để **squash** (gộp), sửa message, sắp xếp lại commit → lịch sử gọn trước khi merge.

#### 3. Tag & Semantic Versioning

`git tag -a v1.2.3 -m "..."` đánh dấu mốc phát hành. Số `MAJOR.MINOR.PATCH`:

| Phần | Ví dụ | Nghĩa |
|---|---|---|
| **PATCH** | 1.2.3 → 1.2.4 | Sửa lỗi nhỏ, an toàn nâng |
| **MINOR** | 1.2 → 1.3 | Thêm tính năng, vẫn tương thích |
| **MAJOR** | 1.x → 2.0 | **Breaking change** — đọc kỹ migration |

#### 4. Conventional Commits

Viết message theo chuẩn → công cụ tự sinh changelog + tự bump version:
```
feat: thêm đăng nhập Google      → tăng MINOR
fix: sửa lỗi tràn bộ nhớ          → tăng PATCH
feat!: đổi format API (breaking)  → tăng MAJOR
```

#### 5. Công cụ khác

- **`git cherry-pick <hash>`**: lấy 1 commit cụ thể sang nhánh hiện tại.
- **`git bisect`**: tìm commit gây bug bằng nhị phân — vàng khi "không biết bug từ đâu".
- **Workflow**: GitHub Flow (đơn giản, phổ biến), Git Flow (nhiều phiên bản), trunk-based (CI/CD trưởng thành).

### 📖 Hiểu rõ hơn (giải thích cho người mới)

> 📘 đã có bảng merge/rebase và SemVer. Mục này cho bạn **hình dung** để nhớ.

**Merge kể sự thật, rebase kể chuyện gọn.** Merge giữ nguyên lịch sử đúng như đã xảy ra — có nhánh, có "merge commit", nhìn như cái cây. Rebase *viết lại* các commit của bạn cho nằm thẳng hàng trên `main`, lịch sử phẳng và dễ đọc như một dòng thời gian. Không cái nào "đúng" tuyệt đối: rebase để dọn nhánh *riêng* trước khi mở PR; merge để giữ ngữ cảnh thật trên nhánh *chung*.

**Quy tắc vàng gói trong một câu: đừng bao giờ rebase thứ đã công khai.** Rebase tạo ra các commit *mới* (hash khác) thay cho commit cũ. Nếu nhánh đó người khác đã pull về, lịch sử của họ và của bạn "lệch pha" → hỗn loạn. Cứ nhánh nào *chỉ mình bạn* thì rebase thoải mái; nhánh đã push/chia sẻ thì đừng đụng.

**Version không phải số cho đẹp — nó là lời hứa với người dùng.** `MAJOR.MINOR.PATCH`: tăng PATCH nghĩa "chỉ sửa lỗi, nâng cấp yên tâm"; MINOR "có thêm đồ mới nhưng vẫn tương thích"; MAJOR "có breaking change, đọc kỹ trước khi nâng". Viết commit theo *Conventional Commits* (`feat:`/`fix:`/`feat!:`) thì công cụ tự suy ra số version và tự sinh changelog cho bạn.

### 🧪 Lab cơ bản

> Mục tiêu: dọn lịch sử bằng rebase, đánh tag phiên bản, và tập cherry-pick.

**Bước 1 — Tạo vài commit nhỏ để squash.**
```bash
git switch -c dep-clean
for m in "wip 1" "wip 2" "wip 3"; do echo "$m" >> notes.txt; git commit -am "$m"; done
```

**Bước 2 — Squash 3 commit thành 1.**
```bash
git rebase -i HEAD~3
# trong editor: giữ dòng đầu là "pick", đổi 2 dòng sau thành "squash" (hoặc "s")
git log --oneline      # 3 commit gộp còn 1
```

**Bước 3 — Đánh annotated tag & push.**
```bash
git switch main
git tag -a v1.0.0 -m "Release 1.0"
git push origin v1.0.0
git tag           # thấy v1.0.0
```

**Bước 4 — Viết commit theo Conventional Commits.**
```bash
echo x >> f; git commit -am "feat: thêm tính năng x"
echo y >> f; git commit -am "fix: sửa lỗi y"
```

**Bước 5 — Cherry-pick 1 commit sang nhánh khác.**
```bash
git switch -c hotfix
git cherry-pick <hash-commit-fix>    # lấy đúng 1 commit
```
Trên GitHub: tạo **Release** từ tag `v1.0.0`.

### 🚀 Lab nâng cao (best-practice)

> Mục tiêu: dùng Git như team chuyên nghiệp — lịch sử sạch, version có ý nghĩa, changelog tự động.

1. **Conventional Commits + tự sinh changelog/version:**
   ```
   feat: thêm đăng nhập Google      → tăng MINOR
   fix: sửa lỗi tràn bộ nhớ          → tăng PATCH
   feat!: đổi format API (breaking)  → tăng MAJOR
   ```
   Công cụ `semantic-release` / `release-please` đọc commit → tự bump version + viết CHANGELOG + tạo GitHub Release.
2. **Rebase an toàn:** chỉ rebase nhánh **của riêng bạn** trước khi mở PR, để lịch sử sạch khi merge.
3. **`git bisect`** — tìm commit gây bug bằng nhị phân (vàng khi "không biết bug từ đâu"):
   ```bash
   git bisect start; git bisect bad; git bisect good v1.0.0
   # Git tự checkout giữa, bạn test rồi đánh dấu good/bad → ra đúng commit lỗi
   ```
4. **Bảo vệ tag** và ký tag (`git tag -s`) cho release quan trọng.

### 💡 Bổ sung thực tế: merge vs rebase — chọn cái nào?

- **Khác biệt cốt lõi:**
  | | Lịch sử | Dùng khi |
  |---|---|---|
  | **merge** | giữ nguyên, có merge commit | nhánh chung, muốn giữ ngữ cảnh thật |
  | **rebase** | viết lại thành tuyến tính | nhánh riêng, muốn lịch sử sạch trước PR |
- **Quy tắc vàng của rebase:** *"Đừng bao giờ rebase thứ đã công khai."* Rebase nhánh người khác đang dùng = phá lịch sử của họ, gây hỗn loạn.
- **Semantic Versioning quyết định gì:** người dùng nhìn version là biết có **breaking change** (MAJOR) không. `2.3.1 → 2.4.0` = an toàn nâng cấp; `2.4.0 → 3.0.0` = đọc kỹ migration guide.
- **Squash khi merge PR:** nhiều team bật "Squash and merge" → 1 PR = 1 commit gọn trên main, lịch sử main rất sạch để đọc.

### 🧭 Hướng dẫn làm lab & giải nghĩa lệnh (cho người tự học)

> Làm tuần tự, dừng ở mỗi ✅ **Checkpoint**.

**Bước 1 — Squash và xem lịch sử gọn.**
```bash
git rebase -i HEAD~3      # đổi pick → squash cho 2 dòng sau
git log --oneline
```
✅ **Checkpoint:** 3 commit "wip" gộp thành 1.
💡 Chỉ squash nhánh **của riêng bạn**, trước khi mở PR.

**Bước 2 — Đánh tag & push.**
```bash
git tag -a v1.0.0 -m "Release 1.0" && git push origin v1.0.0
```
✅ **Checkpoint:** `git tag` hiện `v1.0.0`, GitHub thấy tag.

**Bước 3 — Đọc version có ý nghĩa.**
✅ **Checkpoint:** nhìn `2.4.0 → 2.4.1` biết là an toàn (PATCH); `2.x → 3.0.0` biết phải đọc migration (MAJOR).

**Bước 4 — (Nâng cao) tìm bug bằng bisect.**
```bash
git bisect start; git bisect bad; git bisect good v1.0.0
# Git checkout giữa, bạn test rồi đánh dấu good/bad → ra đúng commit lỗi
git bisect reset
```
✅ **Checkpoint:** bisect chỉ ra commit đầu tiên gây bug.

### 🐛 Gỡ lỗi nhanh

| Triệu chứng | Nguyên nhân | Cách sửa |
|---|---|---|
| Rebase gây conflict | 2 nhánh sửa cùng chỗ | Sửa file, `git add`, `git rebase --continue`; hoặc `--abort` để huỷ |
| Đồng đội phàn nàn lịch sử bị "lệch" | Rebase nhánh đã public | Không rebase nhánh chung; nếu lỡ, phối hợp `pull --rebase` |
| `push` tag không lên | Chưa push tag riêng | `git push origin <tag>` hoặc `git push --tags` |
| Cherry-pick trùng lặp commit | Lấy commit đã có sẵn ở nhánh | Kiểm `git log` trước; dùng `-x` để ghi nguồn |
| Kẹt trong bisect | Quên reset | `git bisect reset` về trạng thái ban đầu |

### 📝 Bài ôn tập & Demo đối chiếu

**✍️ Tự kiểm tra:**

<details>
<summary>1. Khi nào KHÔNG được rebase?</summary>

> Khi nhánh đã **push/chia sẻ** với người khác. Rebase viết lại lịch sử → phá commit của người đang dùng nhánh đó.
</details>

<details>
<summary>2. Semantic Versioning: 1.4.2 → cần lên số nào nếu thêm tính năng tương thích?</summary>

> Tăng MINOR: `1.4.2 → 1.5.0`. (PATCH cho sửa lỗi, MAJOR cho breaking change.)
</details>

<details>
<summary>3. merge và rebase khác nhau về lịch sử thế nào?</summary>

> merge giữ nguyên lịch sử phân nhánh + tạo merge commit. rebase dời commit lên đầu nhánh chính → lịch sử tuyến tính, sạch.
</details>

<details>
<summary>4. `git bisect` dùng để làm gì?</summary>

> Tìm commit đầu tiên gây bug bằng tìm kiếm nhị phân — nhanh hơn nhiều so với dò từng commit.
</details>

**🔬 Demo đối chiếu:**

| Demo đối chiếu | Kết quả mong đợi |
|---|---|
| Rebase/squash | `git log` gọn, tuyến tính |
| Tạo tag | `git tag` hiện `v1.0.0`, push thành Release |
| Cherry-pick | Commit chỉ định xuất hiện ở nhánh mới |

### 📚 Thuật ngữ Anh–Việt (ngày này)

| Thuật ngữ | Nghĩa |
|---|---|
| **Rebase** | Viết lại lịch sử thành tuyến tính |
| **Squash** | Gộp nhiều commit thành 1 |
| **Tag** | Nhãn đánh dấu phiên bản phát hành |
| **Semantic Versioning** | Đánh số MAJOR.MINOR.PATCH có quy tắc |
| **Conventional Commits** | Chuẩn message (`feat:`/`fix:`) |
| **cherry-pick** | Lấy 1 commit cụ thể sang nhánh khác |
| **bisect** | Tìm commit gây bug bằng nhị phân |

### 🎯 Đúc kết Ngày 25

**3 điều phải mang theo:**
1. **Merge (giữ lịch sử thật) vs rebase (viết thẳng, sạch)** — rebase để dọn nhánh riêng trước PR.
2. **KHÔNG rebase nhánh đã push/chia sẻ** — phá lịch sử của người khác.
3. **SemVer là lời hứa tương thích** (PATCH/MINOR/MAJOR); Conventional Commits → tự sinh version + changelog. Bí bug thì nhớ `git bisect`.

> 🧠 **Một câu để nhớ:** `git bisect` là phép màu khi "không biết bug từ đâu" — dùng nhị phân tìm đúng commit gây lỗi trong vài bước. Nhớ tới nó khi bí.

**✅ Tự chấm** *(đánh dấu khi làm được mà không nhìn tài liệu):*
- [ ] Squash nhiều commit bằng `rebase -i`
- [ ] Nói được khi nào KHÔNG được rebase
- [ ] Tạo annotated tag và push thành Release
- [ ] Giải thích 1.4.2 lên số nào khi thêm tính năng tương thích
- [ ] Mô tả `git bisect` tìm commit gây bug

✅ **Kết quả đạt được:** Dùng Git như chuyên gia — rebase, tag, versioning, workflow chuẩn, tìm bug bằng bisect.

---

## Ngày 26 — Làm quen Cloud — Khái niệm & Free Tier

> ⏱️ ~90 phút · Loại: Cloud
>
> 🧭 **Bạn đang ở đâu:** Ngày 25 (Git nâng cao) → **Ngày 26 (bước chân vào cloud: khái niệm + tài khoản an toàn)** → Ngày 27 (tạo máy ảo). Ngày đầu tiên với cloud — làm đúng ngay từ đầu để tránh hai tai nạn kinh điển: **hoá đơn nghìn đô** và **lộ khoá truy cập**.
>
> 🌐 *Ví dụ dùng AWS. Tương đương: **GCP** (Compute Engine / Cloud Storage / IAM), **Azure** (VM / Blob / Entra ID). Khái niệm giống nhau, chỉ khác tên.*
>
> ✅ **Chuẩn bị:** Docker (cho LAB miễn phí). Tài khoản cloud thật là **tuỳ chọn** — phần A của lab chạy hoàn toàn trên máy bạn.
>
> 🎁 **Cuối ngày bạn có gì:** thao tác thành thạo với API cloud qua `aws` CLI **mà không tốn một đồng**, cộng một checklist an toàn tài khoản mà bạn sẽ dùng thật khi mở tài khoản.

### 📘 Lý thuyết

#### 1. Cloud là đổi "mua tài sản" lấy "thuê theo mức dùng"

Trước đây: mua máy chủ (tốn tiền lớn một lần), tự lo điện, mạng, thay ổ cứng. Mua thừa thì phí, mua thiếu thì kẹt cả tháng chờ hàng về.

Cloud biến nó thành hoá đơn kiểu tiền điện: cần bao nhiêu bật bấy nhiêu, không dùng thì tắt. Nhưng chính sự tiện lợi đó là con dao hai lưỡi — **quên tắt là vẫn bị tính tiền, 24 giờ mỗi ngày**.

#### 2. IaaS / PaaS / SaaS — bạn tự lo bao nhiêu phần

| Mức | Ví như | Bạn lo | Ví dụ |
|---|---|---|---|
| **IaaS** | Thuê đất, tự xây nhà | Hệ điều hành trở lên | EC2, Compute Engine |
| **PaaS** | Thuê nhà có nội thất | Chỉ code | App Engine, Elastic Beanstalk |
| **SaaS** | Ở khách sạn | Không lo gì | Gmail, Notion |

Chọn mức nào là chọn đánh đổi giữa **quyền kiểm soát** và **công sức vận hành**.

#### 3. Năm dịch vụ cốt lõi (tên khác giữa các hãng, ý giống nhau)

| AWS | Làm gì | GCP | Azure |
|---|---|---|---|
| **EC2** | Máy ảo | Compute Engine | Virtual Machines |
| **S3** | Kho chứa file | Cloud Storage | Blob Storage |
| **VPC** | Mạng riêng ảo | VPC | Virtual Network |
| **IAM** | Người dùng & quyền | IAM | Entra ID |
| **RDS** | Database do nhà cung cấp vận hành | Cloud SQL | Azure SQL |

#### 4. Region và Availability Zone

**Region** = một khu vực địa lý (ví dụ `ap-southeast-1` là Singapore). **Availability Zone** = một trung tâm dữ liệu riêng biệt bên trong region đó.

Chọn region ảnh hưởng ba thứ: **độ trễ** (gần người dùng), **giá** (khác nhau giữa các region), và **tuân thủ pháp lý** (dữ liệu được phép đặt ở đâu).

> 🔑 Nhiều AZ trong cùng một region cho bạn HA chống hỏng một trung tâm dữ liệu. Nhưng **cả region vẫn có thể sập** — muốn chống điều đó phải triển khai nhiều region, và đắt hơn hẳn (Ngày 52).

#### 5. Trách nhiệm chia sẻ — hiểu sai là trả giá

Nhà cung cấp lo bảo mật **của** cloud (phần cứng, trung tâm dữ liệu, lớp ảo hoá). **Bạn** lo bảo mật **trong** cloud (cấu hình, phân quyền, dữ liệu, bản vá).

Nói cách khác: **"lên cloud" không tự động an toàn.** Bucket cấu hình sai vẫn công khai ra Internet; khoá truy cập lộ trên GitHub vẫn bị lợi dụng. Đó là phần của bạn.

#### 6. Hai tai nạn kinh điển và cách phòng

| Tai nạn | Vì sao xảy ra | Cách phòng |
|---|---|---|
| **Hoá đơn nghìn đô** | Quên tắt tài nguyên; hoặc khoá bị lộ rồi bị dùng để đào tiền ảo | Đặt cảnh báo ngân sách **ngay ngày đầu**; luôn `destroy` sau buổi học |
| **Lộ khoá truy cập** | Commit `AWS_SECRET_ACCESS_KEY` lên GitHub | Không bao giờ để khoá trong code; quét bí mật (Ngày 49) |

> ⚠️ Có những bot **liên tục quét GitHub** tìm khoá AWS mới commit. Thời gian từ lúc bạn push tới lúc khoá bị dùng để đào tiền ảo thường tính bằng **phút**. Đây không phải chuyện hiếm — đó là chuyện xảy ra hằng ngày.

### 🧪 LAB Phần A — Học API cloud mà không tốn tiền

> **LocalStack** giả lập các dịch vụ AWS ngay trên máy bạn. Cùng một lệnh `aws` CLI, cùng khái niệm, nhưng **không tài khoản, không thẻ, không hoá đơn**.

**Thư mục:**

```text
lab26-cloud/
├── docker-compose.yml       # LocalStack
└── chinh-sach-doc.json      # chính sách IAM chỉ cho đọc
```

#### File 1 — `docker-compose.yml`

```yaml
services:
  localstack:
    image: localstack/localstack:3.8
    container_name: localstack
    ports:
      - "4566:4566"                   # một cổng duy nhất cho mọi dịch vụ
    environment:
      SERVICES: s3,iam,sts,logs
      DEBUG: 0
      AWS_DEFAULT_REGION: ap-southeast-1
    volumes:
      - localstack-data:/var/lib/localstack
      - /var/run/docker.sock:/var/run/docker.sock

volumes:
  localstack-data:
```

#### File 2 — `chinh-sach-doc.json`

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "ChiChoPhepDocMotBucket",
      "Effect": "Allow",
      "Action": [
        "s3:GetObject",
        "s3:ListBucket"
      ],
      "Resource": [
        "arn:aws:s3:::kho-tai-lieu",
        "arn:aws:s3:::kho-tai-lieu/*"
      ]
    }
  ]
}
```

### 🧭 Hướng dẫn làm LAB Phần A — step by step

#### Bước 1 — Khởi động LocalStack và cài AWS CLI

```bash
mkdir -p ~/lab26-cloud && cd ~/lab26-cloud
# tạo 2 file theo phần LAB
docker compose up -d

# Cài AWS CLI nếu chưa có
aws --version 2>/dev/null || {
  curl -s "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o awscli.zip
  unzip -q awscli.zip && sudo ./aws/install && rm -rf awscli.zip aws
}
aws --version
```

**Bạn sẽ thấy:**
```text
aws-cli/2.x.x Python/3.x.x Linux/...
```

✅ **Checkpoint:** AWS CLI in ra phiên bản, container `localstack` đang `Up`.

Tạo một hồ sơ trỏ vào LocalStack (giá trị khoá là giả, LocalStack không kiểm tra):

```bash
aws configure set aws_access_key_id     test --profile local
aws configure set aws_secret_access_key test --profile local
aws configure set region ap-southeast-1 --profile local

# Đặt hàm rút gọn để đỡ gõ endpoint mỗi lần
alias awsl='aws --endpoint-url=http://localhost:4566 --profile local'
awsl sts get-caller-identity
```

**Bạn sẽ thấy:**
```text
{
    "UserId": "AKIAIOSFODNN7EXAMPLE",
    "Account": "000000000000",
    "Arn": "arn:aws:iam::000000000000:root"
}
```

✅ **Checkpoint:** CLI nói chuyện được với LocalStack.

💡 Chú ý bạn vừa dùng **đúng lệnh `aws` thật**, chỉ đổi endpoint. Mọi thứ học ở đây chuyển sang AWS thật chỉ bằng cách bỏ `--endpoint-url`.

#### Bước 2 — S3: kho chứa file

```bash
awsl s3 mb s3://kho-tai-lieu
awsl s3 ls

echo "Báo cáo quý 4 - nội dung thử nghiệm" > bao-cao.txt
awsl s3 cp bao-cao.txt s3://kho-tai-lieu/tai-lieu/bao-cao.txt
awsl s3 ls s3://kho-tai-lieu --recursive
```

**Bạn sẽ thấy:**
```text
make_bucket: kho-tai-lieu
2026-09-23 14:30:00 kho-tai-lieu

upload: ./bao-cao.txt to s3://kho-tai-lieu/tai-lieu/bao-cao.txt
2026-09-23 14:30:05        39 tai-lieu/bao-cao.txt
```

✅ **Checkpoint:** tải lên và liệt kê được file.

Tải về để kiểm chứng:
```bash
awsl s3 cp s3://kho-tai-lieu/tai-lieu/bao-cao.txt ve-lai.txt
cat ve-lai.txt
```

💡 **S3 không phải ổ đĩa, nó là kho đối tượng.** Không có thư mục thật — `tai-lieu/bao-cao.txt` chỉ là *một cái tên có chứa dấu gạch chéo*. Hiểu điều này giúp bạn khỏi bối rối khi thấy "thư mục rỗng tự biến mất".

#### Bước 3 — Bật những thứ đáng lẽ phải bật mặc định

Bucket mới tạo **không** có phiên bản, **không** mã hoá, và **có thể** công khai. Đây chính là nguồn gốc của vô số vụ rò rỉ dữ liệu.

```bash
# 1) Bật phiên bản — cứu bạn khi lỡ ghi đè hoặc xoá nhầm
awsl s3api put-bucket-versioning \
  --bucket kho-tai-lieu \
  --versioning-configuration Status=Enabled

# 2) Bật mã hoá khi lưu
awsl s3api put-bucket-encryption --bucket kho-tai-lieu \
  --server-side-encryption-configuration \
  '{"Rules":[{"ApplyServerSideEncryptionByDefault":{"SSEAlgorithm":"AES256"}}]}'

# 3) Chặn mọi truy cập công khai
awsl s3api put-public-access-block --bucket kho-tai-lieu \
  --public-access-block-configuration \
  "BlockPublicAcls=true,IgnorePublicAcls=true,BlockPublicPolicy=true,RestrictPublicBuckets=true"

awsl s3api get-bucket-versioning --bucket kho-tai-lieu
```

**Bạn sẽ thấy:**
```text
{
    "Status": "Enabled"
}
```

✅ **Checkpoint:** phiên bản đã bật.

Thấy tác dụng của phiên bản ngay:

```bash
echo "Phiên bản 2 - đã sửa" > bao-cao.txt
awsl s3 cp bao-cao.txt s3://kho-tai-lieu/tai-lieu/bao-cao.txt
awsl s3api list-object-versions --bucket kho-tai-lieu \
  --prefix tai-lieu/bao-cao.txt --query 'Versions[].[VersionId,LastModified]' --output table
```

**Bạn sẽ thấy** hai phiên bản — bản cũ **vẫn còn** dù đã bị ghi đè.

✅ **Checkpoint:** thấy hai phiên bản của cùng một file.

💡 **Ba lệnh ở trên là ba câu hỏi Checkov sẽ hỏi bạn ở Ngày 49.** Giờ bạn đã biết chúng có ý nghĩa gì trong thực tế, chứ không phải chỉ là luật để chiều lòng công cụ.

#### Bước 4 — IAM và nguyên tắc đặc quyền tối thiểu

```bash
awsl iam create-user --user-name ung-dung-doc
awsl iam create-policy --policy-name ChiDoc \
  --policy-document file://chinh-sach-doc.json
awsl iam attach-user-policy --user-name ung-dung-doc \
  --policy-arn arn:aws:iam::000000000000:policy/ChiDoc

awsl iam list-attached-user-policies --user-name ung-dung-doc
```

**Bạn sẽ thấy:**
```text
{
    "AttachedPolicies": [
        {
            "PolicyName": "ChiDoc",
            "PolicyArn": "arn:aws:iam::000000000000:policy/ChiDoc"
        }
    ]
}
```

✅ **Checkpoint:** người dùng đã được gắn chính sách chỉ đọc.

💡 Đọc lại `chinh-sach-doc.json`: nó cho phép đúng hai hành động (`GetObject`, `ListBucket`) trên đúng một bucket. Đó là **đặc quyền tối thiểu** — thứ bạn đã gặp ở Ngày 33 (`permissions` của workflow) và sẽ gặp lại ở Ngày 39 (RBAC), Ngày 49.

⚠️ Cám dỗ lớn nhất khi mới học cloud là gán `AdministratorAccess` cho mọi thứ "cho nhanh". Đó chính là lý do một khoá bị lộ có thể dẫn tới mất toàn bộ tài khoản, thay vì chỉ mất một bucket.

#### Bước 5 — Dọn dẹp Phần A

```bash
cd ~/lab26-cloud
docker compose down -v
```

### 🔐 LAB Phần B — Mở tài khoản cloud an toàn (nếu bạn muốn dùng thật)

> Phần này làm **một lần duy nhất** và dùng cho cả Ngày 27–28. Nếu chưa muốn mở tài khoản, cứ dùng phương án thay thế miễn phí ở Ngày 27.

#### Bước 6 — Danh sách kiểm tra bắt buộc

Làm **đúng thứ tự này**, đừng bỏ bước nào:

| # | Việc | Vì sao bắt buộc |
|---|---|---|
| 1 | Đăng ký, chọn region gần bạn (`ap-southeast-1`) | Độ trễ thấp hơn |
| 2 | **Bật MFA cho tài khoản gốc** | Tài khoản gốc mất là mất tất cả |
| 3 | **Tạo một IAM user riêng** để dùng hằng ngày | Không bao giờ dùng tài khoản gốc cho việc thường |
| 4 | **Đặt cảnh báo ngân sách 1 USD** | Biết ngay khi có gì đó phát sinh chi phí |
| 5 | **Cất tài khoản gốc đi**, chỉ dùng IAM user | Giảm thiệt hại nếu lộ thông tin |
| 6 | Bật MFA cho cả IAM user | Lớp bảo vệ thứ hai |

> ⚠️ **Bước 4 là bước quan trọng nhất.** Cảnh báo ngân sách 1 USD nghĩa là **bất kỳ khoản phát sinh nào** cũng làm bạn nhận email ngay. Đây là thứ đứng giữa bạn và một hoá đơn bất ngờ.

Đặt cảnh báo ngân sách bằng CLI (khi đã có tài khoản thật):

```bash
cat > ngan-sach.json <<'EOF'
{
  "BudgetName": "canh-bao-1-do",
  "BudgetLimit": { "Amount": "1", "Unit": "USD" },
  "TimeUnit": "MONTHLY",
  "BudgetType": "COST"
}
EOF

cat > thong-bao.json <<'EOF'
[{
  "Notification": {
    "NotificationType": "ACTUAL",
    "ComparisonOperator": "GREATER_THAN",
    "Threshold": 1,
    "ThresholdType": "PERCENTAGE"
  },
  "Subscribers": [{ "SubscriptionType": "EMAIL", "Address": "ban@example.com" }]
}]
EOF

aws budgets create-budget \
  --account-id <so-tai-khoan-cua-ban> \
  --budget file://ngan-sach.json \
  --notifications-with-subscribers file://thong-bao.json
```

✅ **Checkpoint:** vào **Billing → Budgets** thấy ngân sách vừa tạo.

#### Bước 7 — Tự kiểm tra an toàn tài khoản

```bash
echo "▸ Đang dùng danh tính nào?"
aws sts get-caller-identity --query Arn --output text
echo "  (phải là :user/<ten-iam-user>, KHÔNG được là :root)"

echo "▸ Tài khoản gốc đã bật MFA chưa?"
aws iam get-account-summary --query 'SummaryMap.AccountMFAEnabled'
echo "  (phải là 1)"

echo "▸ Có khoá truy cập nào của tài khoản gốc không?"
aws iam get-account-summary --query 'SummaryMap.AccountAccessKeysPresent'
echo "  (phải là 0 — tài khoản gốc KHÔNG nên có khoá)"
```

⚠️ **Nếu dòng đầu ra `:root`** — bạn đang dùng tài khoản gốc. Dừng lại, tạo IAM user và chuyển sang dùng nó trước khi đi tiếp.

### 💡 Đi làm mới thấm (sách cơ bản hay bỏ quên)

- **Free tier không phải miễn phí vô điều kiện.** Nó miễn phí *trong hạn mức*: 750 giờ máy nhỏ mỗi tháng, 5 GB S3... Vượt hạn mức là tính tiền bình thường, và **không có ai chặn bạn lại**. Cảnh báo ngân sách là thứ duy nhất báo cho bạn biết.
- **Khoá truy cập bị lộ là sự cố tính bằng phút.** Bot quét GitHub liên tục. Nếu lỡ commit khoá: **vô hiệu hoá nó ngay lập tức** (trước cả khi xoá khỏi lịch sử), rồi kiểm tra hoá đơn và các tài nguyên lạ xem có gì được tạo ra không.
- **Xoá tài nguyên đúng cách, đừng chỉ tắt.** `stop` một máy ảo vẫn tính tiền ổ đĩa. Ổ đĩa mồ côi, IP tĩnh không dùng, snapshot cũ — tất cả vẫn tính tiền hằng tháng (Ngày 53). Tập thói quen dọn sạch sau mỗi buổi học.
- **Chọn region rồi thì đừng đổi tuỳ tiện.** Tài nguyên ở region khác **không thấy nhau** một cách tự nhiên, và người mới hay hoảng vì "máy ảo của tôi biến mất" — thực ra chỉ là đang xem nhầm region.
- **Dùng LocalStack để học và để chạy test.** Không chỉ hợp cho người mới: nhiều đội dùng nó trong CI để kiểm thử mã tương tác với AWS mà không tốn tiền và không cần tài khoản thật.
- **Mọi thứ hôm nay bấm tay, ba ngày nữa sẽ viết thành code.** Ngày 29 bạn học Terraform và làm lại đúng những việc này bằng khai báo. Hãy bấm tay hôm nay để hiểu *cái gì đang được tạo ra* — rồi mới tự động hoá.

### 📝 Tự kiểm tra

> Nghĩ câu trả lời **thành lời** trước khi mở đáp án — nghĩ thầm luôn thấy mình hiểu.

<details>
<summary><b>1. Mô hình trách nhiệm chia sẻ: nhà cung cấp lo gì, bạn lo gì? Cho một ví dụ mà 'lên cloud' KHÔNG tự động an toàn.</b></summary>

Nhà cung cấp lo bảo mật **của** cloud: phần cứng, trung tâm dữ liệu, lớp ảo hoá. **Bạn** lo bảo mật **trong** cloud: cấu hình, phân quyền, dữ liệu, bản vá.

Ví dụ điển hình: một bucket S3 cấu hình sai quyền vẫn công khai ra Internet — AWS không ngăn bạn làm điều đó, vì đó là phần của bạn. Tương tự với khoá truy cập lỡ commit lên GitHub.

</details>

<details>
<summary><b>2. Vì sao phải đặt cảnh báo ngân sách TRƯỚC khi tạo tài nguyên đầu tiên, chứ không phải sau?</b></summary>

Vì hoá đơn cloud về **sau một tháng** — biết mình tiêu quá thì đã tiêu xong rồi. Cảnh báo ngân sách 1 USD nghĩa là bất kỳ khoản phát sinh nào cũng làm bạn nhận email ngay.

Và free tier **không phải miễn phí vô điều kiện**: nó miễn phí trong hạn mức, vượt hạn mức là tính tiền bình thường, không ai chặn bạn lại.

</details>

<details>
<summary><b>3. Bạn lỡ commit `AWS_SECRET_ACCESS_KEY` lên GitHub. Việc đầu tiên phải làm là gì, và vì sao đúng thứ tự đó?</b></summary>

**Vô hiệu hoá khoá đó ngay lập tức** — trước cả khi xoá khỏi lịch sử Git.

Lý do về thời gian: có bot liên tục quét GitHub tìm khoá mới commit. Thời gian từ lúc push tới lúc khoá bị dùng để đào tiền ảo thường tính bằng **phút**. Dọn lịch sử Git mất vài chục phút — đến lúc đó thì đã muộn.

Sau khi thu hồi mới tới: dọn lịch sử (`git filter-repo`/BFG), kiểm tra hoá đơn và tài nguyên lạ, rồi bật quét bí mật tự động.

</details>

### 📚 Thuật ngữ Anh–Việt (ngày này)

| Thuật ngữ | Nghĩa |
|---|---|
| **IaaS / PaaS / SaaS** | Ba mức 'ăn sẵn' — càng lên cao bạn càng lo ít, càng mất quyền kiểm soát |
| **Region** | Khu vực địa lý đặt trung tâm dữ liệu; ảnh hưởng độ trễ, giá, tuân thủ pháp lý |
| **Availability Zone (AZ)** | Một trung tâm dữ liệu riêng biệt bên trong một region |
| **Shared Responsibility** | Nhà cung cấp lo bảo mật *của* cloud, bạn lo bảo mật *trong* cloud |
| **IAM** | Hệ quản lý người dùng và quyền trên cloud |
| **Least privilege** | Đặc quyền tối thiểu — cho đúng quyền cần thiết, không hơn |
| **Free tier** | Hạn mức dùng miễn phí; **vượt hạn mức vẫn tính tiền bình thường** |
| **LocalStack** | Công cụ giả lập dịch vụ AWS trên máy — học và test không tốn chi phí |

### 🎯 Đúc kết Ngày 26

**3 điều phải mang theo:**

1. **Cloud tiện nên dễ quên tắt.** Đặt cảnh báo ngân sách **trước** khi tạo tài nguyên đầu tiên, không phải sau.
2. **Trách nhiệm chia sẻ:** nhà cung cấp lo phần cứng, **bạn lo cấu hình**. Lên cloud không tự động an toàn.
3. **Đặc quyền tối thiểu ngay từ ngày đầu.** Không dùng tài khoản gốc, không gán quyền quản trị cho mọi thứ — để một khoá lộ không đồng nghĩa mất tất cả.

> 🧠 **Một câu để nhớ:** thứ đắt nhất trên cloud không phải máy chủ — mà là **tài nguyên bạn quên mất là mình đang thuê**.

**✅ Tự chấm** *(đánh dấu khi làm được mà không nhìn tài liệu):*

- [ ] Phân biệt IaaS / PaaS / SaaS và cho ví dụ từng loại
- [ ] Giải thích mô hình trách nhiệm chia sẻ
- [ ] Dùng `aws` CLI tạo bucket, tải file lên, tải về
- [ ] Bật phiên bản + mã hoá + chặn công khai cho bucket, nói rõ vì sao
- [ ] Viết một chính sách IAM chỉ cho phép đúng việc cần
- [ ] Kể đủ 6 bước mở tài khoản an toàn và nói bước nào quan trọng nhất
- [ ] Nói rõ việc cần làm đầu tiên khi lỡ commit khoá truy cập lên Git

✅ **Kết quả đạt được:** Thao tác được với cloud qua dòng lệnh mà không tốn chi phí, và có checklist an toàn tài khoản để dùng thật — hai điều kiện trước khi tạo máy ảo ở Ngày 27.

---

## Ngày 27 — Máy chủ Cloud — Tạo & quản lý VM

> ⏱️ ~90 phút · Loại: Cloud
>
> 🧭 **Bạn đang ở đâu:** Ngày 26 (tài khoản cloud an toàn) → **Ngày 27 (tạo và vận hành một máy ảo)** → Ngày 28 (đưa ứng dụng Docker lên máy đó). Đây là lúc kiến thức Linux, SSH và hardening của Giai đoạn 1 gặp cloud.
>
> 🌐 *EC2 (AWS) ≈ Compute Engine (GCP) ≈ Virtual Machines (Azure). Security Group ≈ Firewall rules ≈ Network Security Group.*
>
> ✅ **Chuẩn bị:** máy Linux. LAB chính dùng **Multipass** — tạo máy ảo Ubuntu thật ngay trên máy bạn, **miễn phí hoàn toàn**. Phần cuối có hướng dẫn làm trên cloud thật.
>
> 🎁 **Cuối ngày bạn có gì:** một máy chủ dựng **hoàn toàn tự động từ file cấu hình** — có user riêng, SSH chỉ dùng khoá, tường lửa bật sẵn — dựng lại trong 90 giây bất cứ lúc nào.

### 📘 Lý thuyết

#### 1. Máy ảo trên cloud — bốn thứ bạn phải chọn

| Lựa chọn | Là gì | Lưu ý cho người mới |
|---|---|---|
| **Ảnh hệ điều hành** (AMI) | Hệ điều hành cài sẵn | Ubuntu LTS là lựa chọn an toàn |
| **Loại máy** (instance type) | CPU + RAM bao nhiêu | Bắt đầu nhỏ, mở rộng sau; loại nhỏ thường nằm trong free tier |
| **Ổ đĩa** | Dung lượng và loại đĩa | **Vẫn tính tiền kể cả khi máy đã tắt** |
| **Mạng & tường lửa** | Máy nằm ở mạng nào, mở cổng nào | Mặc định chặn hết — bạn phải chủ động mở |

#### 2. Khoá SSH — chìa khoá vào máy

Cloud **không dùng mật khẩu** cho máy mới. Bạn tạo một cặp khoá, phần công khai được nạp vào máy lúc khởi tạo, phần riêng bạn giữ.

```bash
ssh -i khoa-rieng.pem ubuntu@<dia-chi-ip>
```

Ba điều hay vấp:
- File khoá phải `chmod 400` — quyền rộng hơn là SSH từ chối dùng
- AWS chỉ cho tải file `.pem` **đúng một lần** — mất là không vào được máy nữa
- Tên người dùng khác nhau tuỳ ảnh hệ điều hành: `ubuntu` (Ubuntu), `ec2-user` (Amazon Linux), `debian` (Debian)

#### 3. Hai lớp tường lửa — đừng nhầm lẫn

| | **Tường lửa của cloud** (Security Group) | **Tường lửa trong máy** (UFW) |
|---|---|---|
| Nằm ở đâu | Trước khi gói tin tới máy | Bên trong hệ điều hành |
| Ai quản | Nhà cung cấp cloud | Bạn, qua SSH |
| Mặc định | **Chặn hết chiều vào** | Thường tắt |
| Khi chặn | Gói tin bị bỏ im lặng → **timeout** | Thường trả về **refused** |

> 🔑 Có cả hai gọi là **phòng thủ nhiều lớp**. Và mẹo chẩn đoán từ Ngày 7 rất hữu ích ở đây: **`timeout` thường là tường lửa cloud chặn; `connection refused` thường là dịch vụ chưa chạy**. Phân biệt được hai cái đó tiết kiệm rất nhiều thời gian mò mẫm.

#### 4. cloud-init — máy tự cấu hình lúc sinh ra

Đây là khái niệm quan trọng nhất hôm nay, và cũng là thứ người mới hay bỏ qua.

Thay vì tạo máy rồi SSH vào cài đặt thủ công, bạn đưa cho nó một **file cấu hình khởi tạo**. Máy tự làm mọi thứ ngay lần khởi động đầu tiên: tạo user, nạp khoá SSH, cài gói, bật tường lửa.

```text
  Cách thủ công:   tạo máy → SSH vào → gõ 20 lệnh → hy vọng không quên gì
  Cách cloud-init: viết file 1 lần → mọi máy sinh ra đều giống hệt nhau
```

Trên AWS nó gọi là **user data**; trên GCP là **startup script** — cùng một cơ chế cloud-init bên dưới. Đây là bước đệm dẫn tới Ansible (Ngày 47) và Terraform (Ngày 29).

#### 5. Vòng đời máy — `stop` khác `terminate`

| Hành động | Máy | Ổ đĩa | Địa chỉ IP | Còn tính tiền? |
|---|---|---|---|---|
| **stop** | Tắt | **Giữ nguyên** | IP công khai **mất** | **Có** — vẫn trả tiền ổ đĩa |
| **terminate** | Xoá hẳn | Xoá (theo mặc định) | Mất | Không |

> ⚠️ Hai nhầm lẫn tốn tiền và tốn thời gian: (1) tưởng `stop` là hết tính tiền — không, ổ đĩa vẫn tính; (2) `stop` rồi `start` thì **địa chỉ IP công khai đổi**, nên mọi thứ trỏ tới IP cũ đều hỏng. Muốn IP cố định phải xin một IP tĩnh — và IP tĩnh **không gắn với máy nào cũng bị tính tiền**.

### 🧪 LAB — Dựng máy chủ hoàn toàn tự động

> Dùng **Multipass** (của Canonical) để tạo máy ảo Ubuntu thật trên máy bạn. Nó dùng **chính cloud-init** như AWS/GCP, nên mọi thứ bạn học ở đây chuyển sang cloud thật gần như nguyên vẹn.

**Thư mục:**

```text
lab27-vm/
├── cloud-init.yaml      # file cấu hình khởi tạo (chính là "user data")
└── kiem-tra.sh          # kiểm chứng máy đã đúng chuẩn
```

#### File 1 — `cloud-init.yaml`

```yaml
#cloud-config
# Dòng đầu tiên BẮT BUỘC phải là #cloud-config — thiếu nó, file bị bỏ qua hoàn toàn

# ---- Tạo người dùng quản trị, KHÔNG dùng root ----
users:
  - name: quantri
    groups: [sudo, docker]
    shell: /bin/bash
    sudo: "ALL=(ALL) NOPASSWD:ALL"
    lock_passwd: true                # không cho đăng nhập bằng mật khẩu
    ssh_authorized_keys:
      - KHOA_CONG_KHAI_CUA_BAN       # script sẽ thay bằng khoá thật

# ---- Cài gói cần thiết ----
package_update: true
package_upgrade: false               # bật ở production; tắt ở lab cho nhanh
packages:
  - ufw
  - fail2ban
  - curl
  - htop
  - ca-certificates

# ---- Ghi file cấu hình ----
write_files:
  - path: /etc/ssh/sshd_config.d/99-siet-chat.conf
    content: |
      # Hardening SSH — đúng bài học Ngày 9
      PermitRootLogin no
      PasswordAuthentication no
      PubkeyAuthentication yes
      MaxAuthTries 3
      ClientAliveInterval 300
    permissions: "0644"

  - path: /etc/motd
    content: |
      ============================================
        Máy chủ dựng bằng cloud-init
        Mọi thay đổi thủ công sẽ MẤT khi dựng lại
      ============================================
    permissions: "0644"

# ---- Lệnh chạy lần đầu, theo thứ tự ----
runcmd:
  # Tường lửa: chặn hết chiều vào, chỉ mở những gì cần
  - ufw default deny incoming
  - ufw default allow outgoing
  - ufw allow 22/tcp comment 'SSH'
  - ufw allow 80/tcp comment 'HTTP'
  - ufw allow 443/tcp comment 'HTTPS'
  - ufw --force enable

  # Chặn dò mật khẩu
  - systemctl enable --now fail2ban

  # Nạp lại cấu hình SSH đã siết
  - systemctl restart ssh

  # Cài Docker (chuẩn bị cho Ngày 28)
  - curl -fsSL https://get.docker.com | sh
  - usermod -aG docker quantri

  # Đánh dấu đã xong để bên ngoài kiểm tra được
  - date -Is > /var/log/cloud-init-xong.txt

final_message: "Máy đã sẵn sàng sau $UPTIME giây"
```

#### File 2 — `kiem-tra.sh`

```bash
#!/usr/bin/env bash
# Kiểm chứng máy đã được dựng đúng chuẩn
set -uo pipefail
MAY="${1:-may-web}"

echo "═══════════════════════════════════════════"
echo "  KIỂM TRA MÁY: $MAY"
echo "═══════════════════════════════════════════"

chay() { multipass exec "$MAY" -- bash -c "$1" 2>/dev/null; }

kiem() {
  local mo_ta="$1" lenh="$2" mong_doi="$3"
  local kq; kq=$(chay "$lenh")
  if echo "$kq" | grep -q "$mong_doi"; then
    echo "  ✅ $mo_ta"
  else
    echo "  ❌ $mo_ta  (nhận được: ${kq:-rỗng})"
  fi
}

echo ""
echo "▸ Người dùng và quyền"
kiem "User quantri tồn tại"        "id quantri"                    "quantri"
kiem "quantri có quyền sudo"       "groups quantri"                "sudo"
kiem "quantri thuộc nhóm docker"   "groups quantri"                "docker"

echo ""
echo "▸ Hardening SSH"
kiem "Cấm đăng nhập bằng root"     "sshd -T | grep permitrootlogin" "permitrootlogin no"
kiem "Cấm đăng nhập bằng mật khẩu" "sshd -T | grep passwordauth"    "passwordauthentication no"

echo ""
echo "▸ Tường lửa"
kiem "UFW đang bật"                "sudo ufw status | head -1"      "active"
kiem "Cổng 22 đã mở"               "sudo ufw status"                "22/tcp"
kiem "Cổng 80 đã mở"               "sudo ufw status"                "80/tcp"

echo ""
echo "▸ Dịch vụ"
kiem "fail2ban đang chạy"          "systemctl is-active fail2ban"   "active"
kiem "Docker đã cài"               "docker --version"               "Docker version"

echo ""
echo "▸ cloud-init"
kiem "cloud-init hoàn tất"         "cat /var/log/cloud-init-xong.txt" "20"
echo ""
```

### 🧭 Hướng dẫn làm LAB — step by step

#### Bước 1 — Cài Multipass

```bash
sudo snap install multipass
multipass version
```

**Bạn sẽ thấy:**
```text
multipass   1.15.x
multipassd  1.15.x
```

✅ **Checkpoint:** in ra phiên bản.

⚠️ Không có `snap`? Xem hướng dẫn tại [multipass.run/install](https://multipass.run/install). Hoặc thay bằng **Vagrant + VirtualBox** — khái niệm cloud-init giống hệt.

#### Bước 2 — Tạo khoá SSH riêng cho lab và chèn vào file cấu hình

```bash
mkdir -p ~/lab27-vm && cd ~/lab27-vm
ssh-keygen -t ed25519 -f ./khoa-may-chu -N "" -C "lab27"

# tạo cloud-init.yaml theo phần LAB, rồi chèn khoá công khai vào
sed -i "s|KHOA_CONG_KHAI_CUA_BAN|$(cat khoa-may-chu.pub)|" cloud-init.yaml
grep -A1 ssh_authorized_keys cloud-init.yaml
```

**Bạn sẽ thấy:**
```text
    ssh_authorized_keys:
      - ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAI... lab27
```

✅ **Checkpoint:** khoá công khai đã nằm trong file cấu hình.

💡 Đây đúng là cách cloud hoạt động: **phần công khai nạp vào máy lúc sinh ra, phần riêng bạn giữ**. Không có mật khẩu nào cả — và đó là điều tốt.

#### Bước 3 — Dựng máy và bấm giờ

```bash
time multipass launch 24.04 \
  --name may-web \
  --cpus 1 --memory 1G --disk 5G \
  --cloud-init cloud-init.yaml
```

**Bạn sẽ thấy** (lần đầu mất vài phút để tải ảnh hệ điều hành):
```text
Launched: may-web

real    1m32.418s
```

✅ **Checkpoint:** máy được tạo, không lỗi.

```bash
multipass list
```

**Bạn sẽ thấy:**
```text
Name      State     IPv4            Image
may-web   Running   10.115.42.118   Ubuntu 24.04 LTS
```

💡 **Hãy dừng lại và nhận ra điều vừa xảy ra:** trong 90 giây, một máy chủ đã được tạo, có user riêng, SSH đã siết chặt, tường lửa đã bật, fail2ban đang chạy và Docker đã cài — **bạn chưa gõ một lệnh nào bên trong nó**. Làm tay từng bước sẽ mất khoảng 20 phút và rất dễ quên.

#### Bước 4 — Kiểm chứng mọi thứ đúng như khai báo

```bash
chmod +x kiem-tra.sh
./kiem-tra.sh may-web
```

**Bạn sẽ thấy:**
```text
▸ Người dùng và quyền
  ✅ User quantri tồn tại
  ✅ quantri có quyền sudo
  ✅ quantri thuộc nhóm docker

▸ Hardening SSH
  ✅ Cấm đăng nhập bằng root
  ✅ Cấm đăng nhập bằng mật khẩu

▸ Tường lửa
  ✅ UFW đang bật
  ✅ Cổng 22 đã mở
  ✅ Cổng 80 đã mở

▸ Dịch vụ
  ✅ fail2ban đang chạy
  ✅ Docker đã cài

▸ cloud-init
  ✅ cloud-init hoàn tất
```

✅ **Checkpoint:** tất cả đều ✅.

⚠️ **Nếu vài mục ❌:** cloud-init có thể chưa chạy xong. Chờ thêm 30 giây rồi chạy lại. Vẫn lỗi thì xem nhật ký:
```bash
multipass exec may-web -- sudo cat /var/log/cloud-init-output.log | tail -30
```
Đây là **file nhật ký quan trọng nhất** khi cloud-init không như ý — nó ghi lại đúng lỗi của từng lệnh trong `runcmd`.

#### Bước 5 — SSH bằng khoá, đúng cách của cloud

```bash
IP=$(multipass info may-web --format json | python3 -c "import sys,json; print(json.load(sys.stdin)['info']['may-web']['ipv4'][0])")
echo "Địa chỉ IP: $IP"

ssh -i ./khoa-may-chu -o StrictHostKeyChecking=no quantri@$IP hostname
```

**Bạn sẽ thấy:** tên máy in ra — bạn vừa SSH vào bằng **đúng quy trình dùng trên cloud thật**.

✅ **Checkpoint:** đăng nhập được bằng khoá.

Thử những thứ đáng lẽ phải bị chặn:

```bash
echo "--- Thử đăng nhập bằng root (phải bị từ chối) ---"
ssh -i ./khoa-may-chu -o StrictHostKeyChecking=no -o BatchMode=yes \
  root@$IP hostname 2>&1 | head -2

echo "--- Thử đăng nhập bằng mật khẩu (phải bị từ chối) ---"
ssh -o PreferredAuthentications=password -o PubkeyAuthentication=no \
  -o StrictHostKeyChecking=no -o ConnectTimeout=5 quantri@$IP 2>&1 | head -2
```

**Bạn sẽ thấy:**
```text
--- Thử đăng nhập bằng root ---
Permission denied (publickey).

--- Thử đăng nhập bằng mật khẩu ---
Permission denied (publickey).
```

✅ **Checkpoint:** cả hai đường tấn công phổ biến nhất đều bị chặn.

💡 Máy chủ mở cổng 22 ra Internet sẽ bị dò mật khẩu **liên tục, hàng nghìn lần mỗi ngày**. Hai dòng cấu hình (`PermitRootLogin no`, `PasswordAuthentication no`) vô hiệu hoá gần như toàn bộ loại tấn công đó.

#### Bước 6 — Thấy tường lửa hoạt động thật

```bash
multipass exec may-web -- sudo ufw status numbered
```

**Bạn sẽ thấy:**
```text
Status: active

     To                         Action      From
     --                         ------      ----
[ 1] 22/tcp                     ALLOW IN    Anywhere    # SSH
[ 2] 80/tcp                     ALLOW IN    Anywhere    # HTTP
[ 3] 443/tcp                    ALLOW IN    Anywhere    # HTTPS
```

Kiểm chứng cổng **không** mở thì hành xử ra sao:

```bash
multipass exec may-web -- bash -c "python3 -m http.server 8888 &>/dev/null &"
sleep 2
echo "Cổng 80 (đã mở trong tường lửa, chưa có dịch vụ):"
timeout 5 curl -s -o /dev/null -w "  %{http_code}\n" http://$IP:80 || echo "  refused (dịch vụ chưa chạy)"
echo "Cổng 8888 (có dịch vụ, nhưng tường lửa CHẶN):"
timeout 5 curl -s -o /dev/null http://$IP:8888 || echo "  timeout (tường lửa chặn im lặng)"
```

✅ **Checkpoint:** thấy rõ khác biệt giữa **refused** (không có dịch vụ) và **timeout** (tường lửa chặn).

💡 **Đây chính xác là bài học Ngày 7, giờ gặp lại trong bối cảnh cloud.** Khi ứng dụng "không vào được", phân biệt hai tín hiệu này cho bạn biết ngay nên đi sửa tường lửa hay đi xem dịch vụ.

#### Bước 7 — Chứng minh máy dựng lại được (điểm cốt lõi)

Hãy phá máy đi:

```bash
multipass exec may-web -- sudo rm -rf /etc/ufw /home/quantri/.ssh
multipass exec may-web -- sudo systemctl stop fail2ban
./kiem-tra.sh may-web | grep "❌" | head -5
```

Giờ dựng lại từ đầu:

```bash
multipass delete may-web --purge
time multipass launch 24.04 --name may-web --cpus 1 --memory 1G --disk 5G \
  --cloud-init cloud-init.yaml
./kiem-tra.sh may-web | grep -c "✅"
```

**Bạn sẽ thấy:**
```text
real    1m28.102s
11
```

✅ **Checkpoint:** máy mới đạt lại **toàn bộ** tiêu chí, trong khoảng 90 giây.

💡 **Đây là ý tưởng "máy chủ dùng một lần" (cattle, not pets).** Máy hỏng thì không cần chẩn đoán và chữa — **xoá đi dựng lại**, vì mọi cấu hình đều nằm trong file. Tư duy này là nền của Kubernetes (Ngày 36) và của toàn bộ hạ tầng hiện đại.

#### Bước 8 — Dọn dẹp

```bash
multipass delete may-web --purge
multipass list
```

### ☁️ Làm trên cloud thật (khi bạn đã sẵn sàng)

Cùng file `cloud-init.yaml`, chỉ khác cách đưa nó vào:

```bash
# AWS — nội dung file chính là "user data"
aws ec2 run-instances \
  --image-id ami-xxxxxxxx \
  --instance-type t3.micro \
  --key-name khoa-cua-ban \
  --security-group-ids sg-xxxxxxxx \
  --user-data file://cloud-init.yaml \
  --tag-specifications 'ResourceType=instance,Tags=[{Key=moi_truong,Value=lab},{Key=chu_so_huu,Value=hoc-vien}]'

# GCP — gọi là "startup script"
gcloud compute instances create may-web \
  --machine-type=e2-micro \
  --image-family=ubuntu-2404-lts-amd64 --image-project=ubuntu-os-cloud \
  --metadata-from-file=user-data=cloud-init.yaml \
  --labels=moi_truong=lab,chu_so_huu=hoc-vien
```

⚠️ **Ba điều bắt buộc khi làm thật:**
1. **Kiểm tra cảnh báo ngân sách đã bật** (Ngày 26) trước khi tạo bất cứ thứ gì.
2. **`terminate` sau khi học xong**, không phải `stop` — `stop` vẫn tính tiền ổ đĩa.
3. **Gắn thẻ mọi tài nguyên** ngay từ đầu (Ngày 53) — nếu không, một tháng sau bạn sẽ không nhớ nổi thứ này để làm gì.

Kiểm tra không còn gì sót lại:
```bash
aws ec2 describe-instances \
  --query 'Reservations[].Instances[?State.Name!=`terminated`].[InstanceId,State.Name]' --output table
aws ec2 describe-volumes --query 'Volumes[?State==`available`].[VolumeId,Size]' --output table
aws ec2 describe-addresses --query 'Addresses[?AssociationId==null].[PublicIp]' --output table
```
Cả ba bảng phải **rỗng**. Ổ đĩa `available` và IP tĩnh không gắn với gì đều đang **âm thầm tính tiền**.

### 💡 Đi làm mới thấm (sách cơ bản hay bỏ quên)

- **`stop` không phải là hết tiền.** Ổ đĩa vẫn tính phí hằng tháng dù máy đã tắt. Muốn dừng hẳn chi phí thì phải `terminate` và xoá ổ đĩa. Đây là khoản lãng phí phổ biến nhất của người mới học cloud.
- **Địa chỉ IP công khai đổi sau mỗi lần stop/start.** Mọi thứ trỏ tới IP cũ sẽ hỏng. Giải pháp là IP tĩnh — nhưng nhớ rằng IP tĩnh **không gắn với máy nào** lại bị tính tiền, đúng kiểu tài nguyên mồ côi ở Ngày 53.
- **Đừng SSH vào sửa tay rồi quên.** Nó chính là **trôi cấu hình** của Ngày 43 và 47, ở tầng máy chủ. Máy dựng lại là mọi sửa tay biến mất. Sửa vào `cloud-init.yaml`, rồi dựng lại — đó mới là cách làm bền.
- **cloud-init chỉ chạy ở lần khởi động đầu tiên.** Sửa file rồi khởi động lại máy cũ **không** có tác dụng gì. Phải tạo máy mới. Nhiều người mất cả buổi vì hiểu nhầm điểm này.
- **Đọc `/var/log/cloud-init-output.log` khi có chuyện.** Đây là nơi duy nhất cho biết lệnh nào trong `runcmd` đã thất bại và vì sao. Không có nó thì bạn chỉ đoán mò.
- **Ảnh hệ điều hành tự dựng (golden image) cho môi trường lớn.** cloud-init chạy lúc khởi động nên máy mất 1–2 phút mới sẵn sàng. Khi cần mở rộng nhanh, người ta nướng sẵn mọi thứ vào một ảnh hệ điều hành (bằng Packer) — máy lên là dùng được ngay. Cùng tư duy với Docker image ở Ngày 17.

### 📝 Tự kiểm tra

> Nghĩ câu trả lời **thành lời** trước khi mở đáp án — nghĩ thầm luôn thấy mình hiểu.

<details>
<summary><b>1. cloud-init chạy vào lúc nào? Sửa file rồi khởi động lại máy cũ có tác dụng không?</b></summary>

cloud-init **chỉ chạy ở lần khởi động đầu tiên** của máy. Sửa file rồi reboot máy cũ **không** có tác dụng gì — phải tạo máy mới.

Rất nhiều người mất cả buổi vì hiểu nhầm điểm này. Khi cloud-init không như ý, xem `/var/log/cloud-init-output.log` — đó là nơi duy nhất cho biết lệnh nào trong `runcmd` đã thất bại và vì sao.

</details>

<details>
<summary><b>2. Phân biệt tường lửa của cloud và tường lửa trong máy. Hai loại lỗi kết nối tương ứng là gì?</b></summary>

**Tường lửa cloud** (Security Group) đứng *trước* khi gói tin tới máy, do nhà cung cấp quản, mặc định chặn hết chiều vào. **Tường lửa trong máy** (UFW) nằm bên trong hệ điều hành, do bạn quản qua SSH.

Hai tín hiệu lỗi:
- `Connection timed out` → gói tin bị **chặn im lặng**, thường là tường lửa cloud
- `Connection refused` → tới được máy nhưng **không có dịch vụ nào nghe** ở cổng đó

Phân biệt được hai cái này tiết kiệm rất nhiều thời gian mò mẫm.

</details>

<details>
<summary><b>3. `stop` và `terminate` khác nhau thế nào về chi phí? Nêu thêm một hệ quả kỹ thuật của `stop`.</b></summary>

**`stop`**: tắt máy nhưng **giữ ổ đĩa** → vẫn trả tiền lưu trữ hằng tháng. **`terminate`**: xoá hẳn, ổ đĩa cũng xoá theo mặc định → hết tính tiền.

Hệ quả kỹ thuật của `stop`: **địa chỉ IP công khai bị mất**. Bật lại máy sẽ có IP mới, nên mọi thứ trỏ tới IP cũ đều hỏng. Muốn IP cố định phải xin IP tĩnh — và IP tĩnh **không gắn với máy nào cũng bị tính tiền**.

</details>

### 📚 Thuật ngữ Anh–Việt (ngày này)

| Thuật ngữ | Nghĩa |
|---|---|
| **cloud-init** | Cơ chế máy tự cấu hình ở lần khởi động đầu tiên (AWS gọi là *user data*) |
| **Security Group** | Tường lửa ở tầng cloud, đứng trước máy; mặc định chặn hết chiều vào |
| **Key pair** | Cặp khoá SSH — phần công khai nạp vào máy, phần riêng bạn giữ |
| **AMI / Image** | Ảnh hệ điều hành dùng để tạo máy ảo |
| **Elastic IP / IP tĩnh** | Địa chỉ IP cố định; không gắn với máy nào thì vẫn bị tính tiền |
| **stop vs terminate** | Tắt (giữ ổ đĩa, vẫn tính tiền) vs xoá hẳn (hết tính tiền) |
| **Cattle, not pets** | Coi máy chủ là đồ dùng một lần — hỏng thì xoá dựng lại, không ngồi chữa |
| **Golden image** | Ảnh hệ điều hành nướng sẵn mọi thứ; máy lên là dùng được ngay (Packer) |

### 🎯 Đúc kết Ngày 27

**3 điều phải mang theo:**

1. **cloud-init biến việc dựng máy thành một file.** Máy sinh ra đã đúng chuẩn, giống nhau mọi lần, không phụ thuộc trí nhớ ai.
2. **Hai lớp tường lửa, hai tín hiệu lỗi khác nhau.** `timeout` là tường lửa chặn; `refused` là dịch vụ chưa chạy.
3. **Máy chủ là đồ dùng một lần.** Hỏng thì xoá dựng lại trong 90 giây, đừng ngồi chữa — mọi thứ đã nằm trong file cấu hình.

> 🧠 **Một câu để nhớ:** nếu bạn phải SSH vào máy để cấu hình nó, thì máy tiếp theo sẽ lại cần bạn SSH vào lần nữa. **Đưa cấu hình vào file** là cách duy nhất thoát khỏi vòng lặp đó.

**✅ Tự chấm** *(đánh dấu khi làm được mà không nhìn tài liệu):*

- [ ] Viết `cloud-init.yaml` tạo user, nạp khoá SSH, cài gói, bật tường lửa
- [ ] Giải thích cloud-init chạy vào lúc nào và vì sao sửa rồi reboot không ăn
- [ ] SSH bằng khoá và chứng minh root cùng mật khẩu đều bị chặn
- [ ] Phân biệt tường lửa cloud với tường lửa trong máy, và hai tín hiệu lỗi
- [ ] Nói rõ `stop` khác `terminate` ở điểm nào về chi phí
- [ ] Xoá máy rồi dựng lại đạt đủ tiêu chí trong dưới 2 phút
- [ ] Biết đọc `/var/log/cloud-init-output.log` khi có lỗi
- [ ] Kiểm tra được tài nguyên mồ côi còn sót trên cloud

✅ **Kết quả đạt được:** Một máy chủ dựng hoàn toàn từ khai báo — an toàn ngay từ giây đầu tiên và dựng lại được bất cứ lúc nào. Ngày 28 sẽ đưa ứng dụng lên chính máy này.

---

## Ngày 28 — Triển khai App lên Cloud (Docker trên VM)

> ⏱️ ~90 phút · Loại: Cloud
>
> 🧭 **Bạn đang ở đâu:** Ngày 27 (máy chủ dựng bằng cloud-init) → **Ngày 28 (đưa ứng dụng thật lên chạy)** → Ngày 29 (Terraform). Hôm nay bạn deploy **bằng tay** — và quan trọng không kém: **cảm nhận rõ nó tệ ở chỗ nào**. Đó chính là động cơ cho Giai đoạn 3.
>
> ✅ **Chuẩn bị:** máy ảo từ Ngày 27 (`multipass launch` với `cloud-init.yaml`), hoặc một VM cloud thật đã cài Docker.
>
> 🎁 **Cuối ngày bạn có gì:** một ứng dụng đang phục vụ qua reverse proxy, tự khởi động lại khi máy reboot — **và một danh sách năm điểm đau do chính bạn đo được**, sẽ được Giai đoạn 3 giải quyết từng cái một.

### 📘 Lý thuyết

#### 1. Ba cách đưa ứng dụng lên máy chủ

| Cách | Làm gì | Vấn đề |
|---|---|---|
| **Chép file thủ công** | `scp` code lên, chạy trực tiếp | Phụ thuộc môi trường máy đích; "máy tôi chạy được" |
| **Docker + Compose** ← hôm nay | Đóng gói rồi chạy container | Vẫn phải tự lo cập nhật, chưa tự phục hồi tốt |
| **Điều phối (Kubernetes)** | Cụm máy tự quản lý | Phức tạp hơn, học ở Ngày 36+ |

#### 2. Reverse proxy — vì sao không cho ứng dụng nghe thẳng cổng 80

Ứng dụng Node của bạn nghe cổng 3000. Cám dỗ là cho nó nghe thẳng cổng 80. Đừng — hãy đặt **nginx đứng trước**:

```text
   Internet :80/:443  →  nginx  →  app :3000 (chỉ nghe nội bộ)
                          │
                          ├── chấm dứt kết nối HTTPS
                          ├── phục vụ file tĩnh (nhanh hơn Node nhiều)
                          ├── giới hạn tần suất, chặn request rác
                          ├── nén gzip
                          └── định tuyến nhiều ứng dụng trên cùng một máy
```

Thêm một lý do quan trọng: cổng dưới 1024 cần quyền root. Không có reverse proxy, bạn phải chạy ứng dụng bằng root — điều đã bị cảnh báo suốt từ Ngày 33.

#### 3. Ứng dụng phải sống lại sau khi máy khởi động lại

Máy chủ sẽ khởi động lại: vá lỗi kernel, mất điện, nhà cung cấp bảo trì. Nếu ứng dụng không tự lên, bạn sẽ biết điều đó qua một cuộc gọi lúc nửa đêm.

Với Docker Compose, chỉ cần một dòng:

```yaml
restart: unless-stopped     # tự bật lại khi Docker khởi động, trừ khi BẠN chủ động dừng
```

| Giá trị | Hành vi |
|---|---|
| `no` (mặc định) | Không bao giờ tự bật lại |
| `on-failure` | Chỉ bật lại khi thoát với mã lỗi |
| `always` | Luôn bật lại, kể cả khi bạn cố ý dừng |
| **`unless-stopped`** | Bật lại, **trừ** khi bạn chủ động dừng ← nên dùng |

#### 4. Deploy thủ công — năm điểm đau (hãy tự cảm nhận hôm nay)

| # | Điểm đau | Giải quyết ở |
|---|---|---|
| 1 | Quy trình nằm trong đầu một người | Ngày 31 — viết thành pipeline |
| 2 | Không có dấu vết ai deploy gì, lúc nào | Ngày 31 — log của CI |
| 3 | Dễ quên bước (`npm install`, migration...) | Ngày 32 — máy làm, không quên |
| 4 | Có gián đoạn khi cập nhật | Ngày 37 — cập nhật cuốn chiếu |
| 5 | Quay lui = làm lại thủ công, run tay | Ngày 34 — quay lui bằng một lệnh |

> 🔑 **Hôm nay bạn sẽ đo cả năm điểm này bằng số liệu thật.** Đừng chỉ đọc bảng — hãy tự bấm giờ. Con số bạn ghi lại hôm nay sẽ được đem ra so sánh ở Ngày 34.

### 🧪 LAB — Đưa ứng dụng lên máy chủ

**Cấu trúc trên máy chủ:**

```text
/opt/ungdung/
├── docker-compose.yml       # app + nginx
├── nginx.conf               # cấu hình reverse proxy
├── .env                     # biến môi trường (KHÔNG commit)
└── app/
    ├── Dockerfile
    ├── package.json
    └── app.js
```

#### File 1 — `app/app.js`

```javascript
const http = require('node:http');
const os = require('node:os');

const PORT = process.env.PORT || 3000;
const PHIEN_BAN = process.env.PHIEN_BAN || 'chua-ro';

const server = http.createServer((req, res) => {
  if (req.url === '/health') {
    res.writeHead(200, { 'Content-Type': 'application/json' });
    return res.end(JSON.stringify({ trangThai: 'ok' }));
  }
  res.writeHead(200, { 'Content-Type': 'application/json' });
  res.end(JSON.stringify({
    thongDiep: 'Ứng dụng đang chạy trên máy chủ',
    phienBan: PHIEN_BAN,
    may: os.hostname(),
    thoiGianChay: Math.round(process.uptime()) + 's',
  }, null, 2));
});

server.listen(PORT, () => console.log(`Đang nghe cổng ${PORT}, phiên bản ${PHIEN_BAN}`));
```

#### File 2 — `app/package.json`

```json
{
  "name": "ung-dung-cloud",
  "version": "1.0.0",
  "main": "app.js",
  "scripts": { "start": "node app.js" },
  "license": "MIT"
}
```

#### File 3 — `app/Dockerfile`

```dockerfile
FROM node:20-alpine
WORKDIR /app

ENV NODE_ENV=production

RUN addgroup -S nhom && adduser -S ungdung -G nhom

COPY package.json ./
COPY app.js ./

USER ungdung
EXPOSE 3000

HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
  CMD wget -qO- http://127.0.0.1:3000/health || exit 1

CMD ["node", "app.js"]
```

#### File 4 — `nginx.conf`

```nginx
upstream ung_dung {
    server app:3000;
    keepalive 16;
}

# Giới hạn tần suất: chống một client làm ngộp máy chủ
limit_req_zone $binary_remote_addr zone=gioi_han:10m rate=20r/s;

server {
    listen 80;
    server_name _;

    # Ẩn phiên bản nginx khỏi header phản hồi
    server_tokens off;

    # Vài header bảo mật cơ bản
    add_header X-Content-Type-Options nosniff;
    add_header X-Frame-Options SAMEORIGIN;

    gzip on;
    gzip_types application/json text/plain text/css application/javascript;

    location / {
        limit_req zone=gioi_han burst=40 nodelay;

        proxy_pass http://ung_dung;
        proxy_http_version 1.1;
        proxy_set_header Host              $host;
        proxy_set_header X-Real-IP         $remote_addr;
        proxy_set_header X-Forwarded-For   $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;

        # Timeout — bài học Ngày 54, áp dụng ngay từ bây giờ
        proxy_connect_timeout 2s;
        proxy_read_timeout    10s;
    }

    # Điểm kiểm tra sức khoẻ, không ghi log cho đỡ nhiễu
    location /health {
        access_log off;
        proxy_pass http://ung_dung/health;
    }
}
```

#### File 5 — `docker-compose.yml`

```yaml
services:
  app:
    build: ./app
    container_name: ung-dung
    restart: unless-stopped          # tự lên lại sau khi máy khởi động lại
    environment:
      PHIEN_BAN: ${PHIEN_BAN:-v1}
      NODE_ENV: production
    expose:
      - "3000"                       # CHỈ mở trong mạng nội bộ, không ra ngoài
    healthcheck:
      test: ["CMD", "wget", "-qO-", "http://127.0.0.1:3000/health"]
      interval: 15s
      timeout: 3s
      retries: 3
    logging:
      driver: json-file
      options:
        max-size: "10m"              # chặn log làm đầy ổ đĩa
        max-file: "3"

  nginx:
    image: nginx:1.27-alpine
    container_name: cong-vao
    restart: unless-stopped
    ports:
      - "80:80"                      # CHỈ nginx mở ra ngoài
    volumes:
      - ./nginx.conf:/etc/nginx/conf.d/default.conf:ro
    depends_on:
      app:
        condition: service_healthy   # chờ app khoẻ rồi mới nhận khách
    logging:
      driver: json-file
      options:
        max-size: "10m"
        max-file: "3"
```

### 🧭 Hướng dẫn làm LAB — step by step

#### Bước 1 — Dựng lại máy chủ từ Ngày 27

```bash
cd ~/lab27-vm
multipass launch 24.04 --name may-web --cpus 1 --memory 1G --disk 5G \
  --cloud-init cloud-init.yaml
IP=$(multipass info may-web --format json | python3 -c "import sys,json; print(json.load(sys.stdin)['info']['may-web']['ipv4'][0])")
echo "Máy chủ: $IP"
multipass exec may-web -- docker --version
```

**Bạn sẽ thấy:** `Docker version 27.x.x` — Docker đã có sẵn nhờ cloud-init.

✅ **Checkpoint:** máy chạy, Docker sẵn sàng.

#### Bước 2 — Tạo ứng dụng ở máy cá nhân

```bash
mkdir -p ~/lab28-deploy/app && cd ~/lab28-deploy
# tạo 5 file theo phần LAB
find . -type f | sort
```

✅ **Checkpoint:** đủ 5 file.

#### Bước 3 — Chuyển lên máy chủ (và bấm giờ — đây là điểm đau số 1)

```bash
BAT_DAU=$(date +%s)

multipass exec may-web -- sudo mkdir -p /opt/ungdung
multipass exec may-web -- sudo chown quantri:quantri /opt/ungdung

multipass transfer -r ~/lab28-deploy/app  may-web:/opt/ungdung/
multipass transfer ~/lab28-deploy/docker-compose.yml may-web:/opt/ungdung/
multipass transfer ~/lab28-deploy/nginx.conf         may-web:/opt/ungdung/

multipass exec may-web -- bash -c "echo 'PHIEN_BAN=v1' > /opt/ungdung/.env"
multipass exec may-web -- ls -la /opt/ungdung
```

**Bạn sẽ thấy** danh sách file đã nằm trên máy chủ.

✅ **Checkpoint:** đủ file trong `/opt/ungdung`.

💡 Đếm thử số lệnh bạn vừa gõ. **Sáu lệnh, đúng thứ tự, không được sai.** Quên `chown` là bước sau lỗi quyền. Đây chính là điểm đau số 1: *quy trình nằm trong đầu bạn*.

#### Bước 4 — Khởi động ứng dụng

```bash
multipass exec may-web -- bash -c "cd /opt/ungdung && docker compose up -d --build"
sleep 10
multipass exec may-web -- bash -c "cd /opt/ungdung && docker compose ps"
```

**Bạn sẽ thấy:**
```text
NAME        IMAGE              STATUS                   PORTS
cong-vao    nginx:1.27-alpine  Up 8 seconds             0.0.0.0:80->80/tcp
ung-dung    ungdung-app        Up 9 seconds (healthy)   3000/tcp
```

✅ **Checkpoint:** cả hai `Up`, container ứng dụng có chữ **(healthy)**.

Kiểm chứng từ bên ngoài:

```bash
KET_THUC=$(date +%s)
curl -s http://$IP/ | head -8
echo ""
echo "⏱️  Thời gian deploy lần đầu: $((KET_THUC - BAT_DAU)) giây"
```

**Bạn sẽ thấy:**
```text
{
  "thongDiep": "Ứng dụng đang chạy trên máy chủ",
  "phienBan": "v1",
  "may": "abc123def456",
  "thoiGianChay": "12s"
}

⏱️  Thời gian deploy lần đầu: 94 giây
```

✅ **Checkpoint:** ứng dụng phục vụ qua cổng 80, và bạn **có một con số** để so sánh về sau.

#### Bước 5 — Xác nhận ứng dụng không hở ra ngoài

```bash
echo "▸ Cổng 80 (nginx) — phải vào được:"
curl -s -o /dev/null -w "  HTTP %{http_code}\n" http://$IP/

echo "▸ Cổng 3000 (ứng dụng) — KHÔNG được vào được từ ngoài:"
timeout 5 curl -s -o /dev/null http://$IP:3000/ \
  && echo "  ❌ HỞ RA NGOÀI" || echo "  ✅ đã đóng đúng"
```

**Bạn sẽ thấy:**
```text
▸ Cổng 80 (nginx) — phải vào được:
  HTTP 200
▸ Cổng 3000 (ứng dụng) — KHÔNG được vào được từ ngoài:
  ✅ đã đóng đúng
```

✅ **Checkpoint:** chỉ nginx lộ ra Internet.

💡 Hai lớp cùng bảo vệ: `expose` (thay vì `ports`) khiến Docker không mở cổng ra máy chủ, và UFW chỉ cho phép 22/80/443. **Phòng thủ nhiều lớp** đúng như Ngày 27.

#### Bước 6 — Kiểm chứng ứng dụng sống lại sau khi máy khởi động lại

Đây là bước rất nhiều người bỏ qua — cho tới ngày máy chủ tự reboot.

```bash
multipass restart may-web
sleep 45
curl -s http://$IP/ | head -4
```

**Bạn sẽ thấy** ứng dụng trả lời bình thường, `thoiGianChay` được tính lại từ đầu.

✅ **Checkpoint:** ứng dụng tự lên sau khi máy khởi động lại, **không ai làm gì cả**.

💡 Công lao của `restart: unless-stopped`. Nếu bỏ dòng đó, bạn phải tự SSH vào bật lại — và nếu máy reboot lúc 3 giờ sáng thì hệ thống chết tới sáng.

#### Bước 7 — Cập nhật phiên bản, và đo điểm đau số 4 (gián đoạn)

Sửa ứng dụng rồi deploy lại — **đồng thời đo xem người dùng có bị ảnh hưởng không**.

**Terminal 1** — theo dõi liên tục:
```bash
IP=$(multipass info may-web --format json | python3 -c "import sys,json; print(json.load(sys.stdin)['info']['may-web']['ipv4'][0])")
tc=0; tb=0
for i in $(seq 1 100); do
  if curl -fs --max-time 2 http://$IP/health > /dev/null 2>&1; then
    tc=$((tc+1)); printf "."
  else
    tb=$((tb+1)); printf "X"
  fi
  sleep 0.3
done
echo ""
echo "Thành công: $tc | Thất bại: $tb"
```

**Terminal 2** — trong lúc đó, deploy bản mới:
```bash
sleep 5
sed -i "s/Ứng dụng đang chạy trên máy chủ/Ứng dụng PHIÊN BẢN 2/" ~/lab28-deploy/app/app.js
multipass transfer ~/lab28-deploy/app/app.js may-web:/opt/ungdung/app/app.js
multipass exec may-web -- bash -c \
  "cd /opt/ungdung && echo 'PHIEN_BAN=v2' > .env && docker compose up -d --build"
```

**Bạn sẽ thấy ở Terminal 1:**
```text
.............XXXXXXXXX..............................
Thành công: 91 | Thất bại: 9
```

✅ **Checkpoint:** có **khoảng 3 giây gián đoạn** — người dùng thật sự bị lỗi trong lúc bạn deploy.

```bash
curl -s http://$IP/ | grep -E "thongDiep|phienBan"
```

**Bạn sẽ thấy:** `"thongDiep": "Ứng dụng PHIÊN BẢN 2"`, `"phienBan": "v2"`.

💡 **Đây là điểm đau số 4, đo được bằng con số.** Docker Compose dừng container cũ rồi mới tạo container mới — giữa hai việc đó là khoảng trống. Với trang web cá nhân thì không sao; với hệ thống bán hàng thì mỗi lần deploy là mất đơn. **Ngày 37 (cập nhật cuốn chiếu của Kubernetes)** sinh ra để xoá khoảng trống này.

#### Bước 8 — Thử quay lui, và cảm nhận điểm đau số 5

Bản v2 có lỗi, cần về v1 ngay. Bấm giờ:

```bash
BAT_DAU=$(date +%s)

sed -i "s/Ứng dụng PHIÊN BẢN 2/Ứng dụng đang chạy trên máy chủ/" ~/lab28-deploy/app/app.js
multipass transfer ~/lab28-deploy/app/app.js may-web:/opt/ungdung/app/app.js
multipass exec may-web -- bash -c \
  "cd /opt/ungdung && echo 'PHIEN_BAN=v1' > .env && docker compose up -d --build"

KET_THUC=$(date +%s)
curl -s http://$IP/ | grep phienBan
echo "⏱️  Thời gian quay lui: $((KET_THUC - BAT_DAU)) giây"
```

**Bạn sẽ thấy:**
```text
  "phienBan": "v1",
⏱️  Thời gian quay lui: 38 giây
```

✅ **Checkpoint:** quay lui được, nhưng bằng cách **sửa code ngược lại và build lại**.

💡 **Hãy nhận ra vấn đề thật sự ở đây:** bạn không "quay lui" — bạn **làm lại thủ công**. Bản v1 không còn tồn tại ở đâu cả, bạn phải tái tạo nó. Nếu quên chính xác v1 có gì thì không về được. Và lúc 2 giờ sáng, tay run, sửa code ngược lại là cách rất dễ gây thêm lỗi.
>
> **Ngày 33** (tag image bất biến) và **Ngày 34** (quay lui bằng tag cũ) giải đúng chỗ này: bản cũ vẫn nằm nguyên trong kho, quay lui chỉ là chọn một chuỗi ký tự khác.

#### Bước 9 — Ghi lại năm con số của bạn

Đây là bảng bạn sẽ mở lại ở Ngày 34 để so sánh:

```bash
cat > ~/lab28-deploy/diem-dau.md <<'EOF'
# Đo đạc deploy thủ công — Ngày 28

| # | Điểm đau | Số đo của tôi | Sẽ giải quyết ở |
|---|---|---|---|
| 1 | Số lệnh phải gõ đúng thứ tự | 6 lệnh | Ngày 31 (pipeline) |
| 2 | Dấu vết ai deploy lúc nào | KHÔNG CÓ | Ngày 31 (log CI) |
| 3 | Thời gian deploy lần đầu | ___ giây | Ngày 32 |
| 4 | Thời gian gián đoạn khi cập nhật | ___ giây | Ngày 37 (rolling update) |
| 5 | Thời gian quay lui | ___ giây (phải build lại) | Ngày 34 (đổi tag) |

## Điều khó chịu nhất
(tự ghi lại cảm nhận của bạn)

## Câu hỏi không trả lời được
- Ba tuần nữa, ai deploy bản đang chạy? Lúc nào? Từ code nào?
EOF

echo "Đã ghi vào ~/lab28-deploy/diem-dau.md — điền số đo của bạn vào."
```

💡 **Điền số thật vào file này.** Ngày 34, khi pipeline của bạn deploy trong 4 phút và quay lui trong 45 giây **mà không ai chạm vào server**, bạn sẽ mở lại bảng này. Cảm giác so sánh đó có giá trị hơn nhiều so với đọc một bảng lý thuyết.

#### Bước 10 — Dọn dẹp

```bash
multipass exec may-web -- bash -c "cd /opt/ungdung && docker compose down"
multipass delete may-web --purge
```

⚠️ **Nếu bạn dùng VM cloud thật:** `terminate`, đừng chỉ `stop` — và kiểm tra lại ổ đĩa mồ côi theo lệnh ở Ngày 27.

### 💡 Đi làm mới thấm (sách cơ bản hay bỏ quên)

- **Giới hạn log là việc bắt buộc, không phải tuỳ chọn.** Container chạy vài tháng có thể đẻ ra hàng chục GB log và làm đầy ổ đĩa — kéo theo toàn bộ dịch vụ trên máy đó chết. `max-size` và `max-file` trong compose là hai dòng cứu bạn khỏi một sự cố rất vô duyên.
- **`expose` khác `ports`.** `ports: "3000:3000"` mở cổng ra ngoài máy; `expose: "3000"` chỉ cho các container trong cùng mạng thấy. Ứng dụng phía sau reverse proxy **luôn** dùng `expose`.
- **File `.env` không bao giờ được commit.** Nó chứa thông tin kết nối và mật khẩu. Thêm vào `.gitignore` ngay từ commit đầu tiên, và dùng `.env.example` (chỉ có tên biến, không có giá trị) để người khác biết cần khai gì.
- **HTTPS ở production là bắt buộc.** Lab này dùng HTTP cho gọn. Ngoài đời, cách nhanh nhất là dùng **Caddy** (tự xin và gia hạn chứng chỉ Let's Encrypt, chỉ cần vài dòng cấu hình) hoặc `certbot` với nginx.
- **`docker compose up -d --build` trên máy chủ production là cách làm tạm.** Nó build ngay trên máy đang phục vụ — tốn CPU, và nếu build lỗi thì bạn kẹt ở trạng thái nửa vời. Cách đúng: **build ở nơi khác, đẩy lên registry, máy chủ chỉ kéo image về chạy** (Ngày 33).
- **Nếu phải deploy tay, ít nhất hãy viết thành script.** Một file `deploy.sh` có `set -euo pipefail` vẫn tốt hơn nhiều so với gõ tay sáu lệnh. Nó là bước đệm tự nhiên dẫn tới pipeline ở Ngày 31 — thực chất pipeline chỉ là script đó, chạy bởi máy, có log và có dấu vết.

### 📝 Tự kiểm tra

> Nghĩ câu trả lời **thành lời** trước khi mở đáp án — nghĩ thầm luôn thấy mình hiểu.

<details>
<summary><b>1. Vì sao đặt nginx trước ứng dụng thay vì cho ứng dụng nghe thẳng cổng 80?</b></summary>

Năm lý do:
1. **Chấm dứt HTTPS** ở một chỗ, thay vì cấu hình TLS cho từng ứng dụng
2. **Phục vụ file tĩnh** nhanh hơn Node/Python rất nhiều
3. **Giới hạn tần suất**, chặn request rác trước khi tới ứng dụng
4. **Định tuyến nhiều ứng dụng** trên cùng một máy
5. Cổng dưới 1024 cần quyền root — không có proxy thì phải chạy ứng dụng bằng root

</details>

<details>
<summary><b>2. Phân biệt `expose` và `ports` trong Docker Compose. Dịch vụ nào dùng cái nào?</b></summary>

`ports: "3000:3000"` **mở cổng ra ngoài máy chủ** — ai truy cập được máy là truy cập được dịch vụ.

`expose: "3000"` chỉ cho các container **trong cùng mạng Docker** thấy — không lộ ra ngoài.

Quy tắc: chỉ **reverse proxy** dùng `ports`. Mọi thứ phía sau (ứng dụng, database) dùng `expose`. Đây là nguyên tắc chỉ mở ra thứ cần mở.

</details>

<details>
<summary><b>3. Vì sao quay lui bằng cách 'sửa code ngược lại rồi build lại' không phải là quay lui thật?</b></summary>

Vì bạn không **quay lui** — bạn đang **tái tạo** bản cũ. Bản cũ không còn tồn tại ở đâu cả.

Hậu quả: nếu quên chính xác bản cũ có gì thì không về được. Và lúc 2 giờ sáng, tay run, sửa code ngược lại là cách rất dễ gây thêm lỗi.

Quay lui thật đòi hỏi bản cũ **vẫn tồn tại dưới một cái tên bất biến** — đó là lý do Ngày 33 tag image theo SHA commit.

</details>

### 📚 Thuật ngữ Anh–Việt (ngày này)

| Thuật ngữ | Nghĩa |
|---|---|
| **Reverse proxy** | Máy chủ đứng trước ứng dụng, nhận request thay rồi chuyển vào trong |
| **expose vs ports** | Chỉ cho container nội bộ thấy vs mở cổng ra ngoài máy chủ |
| **restart: unless-stopped** | Tự bật lại container sau khi máy khởi động lại, trừ khi bạn chủ động dừng |
| **Log rotation** | Giới hạn dung lượng log (`max-size`, `max-file`) để không làm đầy ổ đĩa |
| **Rate limiting** | Giới hạn số request mỗi giây từ một nguồn, chống làm ngộp máy chủ |
| **Graceful degradation** | Suy giảm có kiểm soát — mất bớt chức năng nhưng vẫn phục vụ được |

### 🎯 Đúc kết Ngày 28

**3 điều phải mang theo:**

1. **Reverse proxy đứng trước ứng dụng** — lo HTTPS, nén, giới hạn tần suất, và giữ cho ứng dụng không phải lộ ra Internet.
2. **`restart: unless-stopped` là một dòng nhưng cứu bạn khỏi cuộc gọi lúc nửa đêm.** Máy chủ sẽ khởi động lại, đó là chuyện chắc chắn xảy ra.
3. **Deploy thủ công chạy được, nhưng không lặp lại được, không có dấu vết, có gián đoạn và không quay lui được.** Năm con số bạn vừa đo chính là lý do tồn tại của cả Giai đoạn 3.

> 🧠 **Một câu để nhớ:** deploy tay không sai — nó chỉ **không lặp lại được**. Và thứ không lặp lại được thì không thể tin cậy, dù hôm nay nó chạy tốt.

**✅ Tự chấm** *(đánh dấu khi làm được mà không nhìn tài liệu):*

- [ ] Giải thích vì sao cần reverse proxy thay vì cho ứng dụng nghe cổng 80
- [ ] Phân biệt `expose` và `ports`, nói rõ khi nào dùng cái nào
- [ ] Chọn đúng chính sách `restart` và giải thích lý do
- [ ] Kiểm chứng ứng dụng tự lên sau khi máy khởi động lại
- [ ] Đo được thời gian gián đoạn khi cập nhật bằng cách này
- [ ] Nói rõ vì sao quay lui thủ công là "làm lại" chứ không phải "quay lui"
- [ ] Kể đủ 5 điểm đau và biết mỗi cái được giải quyết ở ngày nào

✅ **Kết quả đạt được:** Ứng dụng đang phục vụ thật sau reverse proxy, tự phục hồi sau reboot — và quan trọng hơn: **năm con số đo được** làm động cơ cho toàn bộ Giai đoạn 3.

---

## Ngày 29 — Infrastructure as Code — Giới thiệu Terraform

> ⏱️ ~90 phút · Loại: IaC
>
> 🧭 **Bạn đang ở đâu:** Ngày 28 (deploy tay — thấy nỗi đau) → **Ngày 29 (tạo hạ tầng bằng CODE — Terraform)** → Ngày 30 (Milestone GĐ2). Đây là bước nhảy tư duy lớn nhất của DevOps: mô tả cả hạ tầng bằng file, chạy lại được.
>
> ✅ **Chuẩn bị:** tài khoản cloud + access key cấu hình cục bộ (`aws configure`, KHÔNG commit key). Cài Terraform (`terraform version`).

### 📘 Lý thuyết

#### 1. Infrastructure as Code (IaC) là gì

Thay vì vào console *click chuột* tạo server (mệt, dễ quên, không lặp lại), bạn **mô tả hạ tầng bằng code**. Chạy file → máy tự tạo đúng y. Cần 10 server giống nhau? Đổi 1 con số. Muốn xoá sạch? 1 lệnh. IaC giải đúng "5 điểm yếu" của Ngày 28: lặp lại được, version trong Git, review qua PR, có dấu vết, rollback bằng revert code.

#### 2. Terraform & các khái niệm

Viết file `.tf` bằng ngôn ngữ HCL, đa cloud. Khái niệm cốt lõi:

| Khái niệm | Nghĩa |
|---|---|
| **provider** | Nhà cung cấp (AWS, GCP, Azure...) |
| **resource** | Tài nguyên cần tạo (EC2, S3...) |
| **variable** | Tham số hoá cấu hình |
| **output** | Giá trị xuất ra (IP, URL) |
| **state file** | Ghi nhớ trạng thái hạ tầng hiện tại |

#### 3. Vòng làm việc

| Lệnh | Làm gì |
|---|---|
| `terraform init` | Chuẩn bị (tải provider) |
| `terraform plan` | **Xem trước** sẽ tạo/sửa/xoá gì (chưa làm gì) |
| `terraform apply` | Thực thi thật |
| `terraform destroy` | Xoá sạch (tránh tốn tiền sau khi học) |

#### 4. State file — "trái tim" của Terraform

Terraform lưu `terraform.tfstate` ghi "nó đang quản những gì". Nó so sánh **code ↔ state ↔ thực tế trên cloud** để quyết định hành động. **3 điều cấm kỵ:**
1. **Sửa tay** `.tfstate` — sai 1 ký tự là mất dấu tài nguyên.
2. **Commit lên Git** — chứa secret plaintext.
3. **Không khoá khi làm team** — 2 người `apply` cùng lúc = state hỏng → dùng remote backend (S3 + DynamoDB lock).

#### 5. Idempotent

Chạy `apply` nhiều lần ra **cùng** kết quả mong muốn (lần 2 báo `0 to add/change`). Bạn mô tả *trạng thái muốn*, Terraform lo *cách đạt*.

> 🔑 **Luôn đọc `terraform plan` TRƯỚC khi `apply`** — đặc biệt để ý dòng `destroy`. Nhiều sự cố production do apply mà không đọc plan, vô tình xoá nhầm tài nguyên.

### 📖 Hiểu rõ hơn (giải thích cho người mới)

> 📘 đã liệt kê khái niệm. Mục này cho bạn **hình dung** để nhớ — không lặp lại bảng.

**IaC như công thức nấu ăn, không phải món ăn sẵn:** click chuột tạo server = tự nấu một lần rồi thôi, lần sau quên mất đã làm gì. Viết Terraform = ghi lại **công thức**: ai cầm công thức cũng nấu ra đúng món đó, muốn 10 phần thì nhân lên, muốn bỏ thì đốt công thức. Hạ tầng của bạn giờ **tái tạo được** và nằm trong Git y như code.

**State file — vì sao nó là "trái tim":** Terraform không nhớ gì trong đầu; toàn bộ "nó đang quản cái gì" nằm trong file `.tfstate`. Mỗi lần chạy, nó đối chiếu 3 thứ — *code bạn viết* ↔ *state* ↔ *thực tế trên cloud* — rồi mới quyết định tạo/sửa/xoá. Mất hoặc hỏng state = Terraform "mất trí nhớ", có thể tạo trùng hoặc xoá nhầm. Đó là lý do state phải giữ gìn cẩn thận (không sửa tay, không commit, khoá khi làm team).

### 🧪 Lab cơ bản

> Mục tiêu: tạo 1 VM bằng code, đi trọn vòng init → plan → apply → destroy.

**Bước 1 — Viết `main.tf`** (file đầy đủ, ví dụ AWS):
```hcl
terraform {
  required_providers {
    aws = { source = "hashicorp/aws", version = "~> 5.0" }
  }
}
provider "aws" {
  region = "ap-southeast-1"
}
resource "aws_instance" "web" {
  ami           = "ami-xxxxxxxx"   # thay bằng AMI Ubuntu của region bạn
  instance_type = "t2.micro"
  tags = { Name = "tf-lab-web" }
}
output "public_ip" {
  value = aws_instance.web.public_ip
}
```

**Bước 2 — Khởi tạo.**
```bash
terraform init
```
Bạn sẽ thấy: `Terraform has been successfully initialized!`.

**Bước 3 — Xem trước (đọc KỸ).**
```bash
terraform plan
```
Bạn sẽ thấy: `Plan: 1 to add, 0 to change, 0 to destroy.`

**Bước 4 — Tạo thật.**
```bash
terraform apply      # gõ yes để xác nhận
```
Kết thúc in `Apply complete!` và `public_ip = ...`.

**Bước 5 — Xoá sạch (tránh tốn phí).**
```bash
terraform destroy    # gõ yes
```
✅ Xác nhận `Destroy complete!` và tài nguyên biến mất khỏi Console.

### 🚀 Lab nâng cao (best-practice)

> Mục tiêu: viết Terraform có cấu trúc + state an toàn — nền móng cho IaC nghiêm túc.

1. **Remote state** thay vì file local — bắt buộc khi làm team (state là "sự thật" về hạ tầng):
   ```hcl
   terraform {
     backend "s3" {
       bucket = "my-tfstate"
       key    = "prod/terraform.tfstate"
       region = "ap-southeast-1"
       # + DynamoDB table để khóa state, tránh 2 người apply cùng lúc
     }
   }
   ```
2. **Tham số hóa bằng `variables.tf` + `terraform.tfvars`** — tách config khỏi code, tái dùng cho dev/prod.
3. **Quy trình chuẩn trước khi apply:**
   ```bash
   terraform fmt        # format chuẩn
   terraform validate   # kiểm cú pháp
   terraform plan -out=tfplan   # lưu plan để apply đúng cái đã review
   terraform apply tfplan
   ```
4. **Không bao giờ** commit `.tfstate` hay `*.tfvars` chứa secret lên Git (`.gitignore`).

### 💡 Bổ sung thực tế: những cái đi làm mới thấm (sách cơ bản hay bỏ quên)

- **`terraform import` — cứu tinh khi hạ tầng đã tạo tay:** thực tế bạn hiếm khi bắt đầu từ số 0, thường đã có server tạo tay từ trước. `import` đưa tài nguyên có sẵn vào state để Terraform quản, khỏi phải xoá đi tạo lại.
- **Dùng remote backend ngay từ ĐẦU, đừng để state local:** S3 + DynamoDB (AWS) hoặc GCS (GCP) để (1) cả team dùng chung 1 state, (2) khoá tránh 2 người apply cùng lúc, (3) không mất state khi hỏng máy.
- **`terraform plan -out=tfplan` rồi `apply tfplan`:** đảm bảo cái bạn apply đúng y cái đã review — giữa lúc plan và apply, hạ tầng thật có thể đã đổi.
- **Gói thành module để tái dùng:** đừng copy-paste khối `resource` cho dev/prod. Gói thành **module** rồi truyền biến vào — 1 chỗ sửa, mọi nơi hưởng.
- **Terraform ≠ cấu hình bên trong máy:** Terraform tạo *hạ tầng* (VM, network, DB). Cài phần mềm & cấu hình *bên trong* VM là việc của Ansible — đừng nhồi script cài đặt dài vào `user_data`.

### 🧭 Hướng dẫn làm lab & giải nghĩa lệnh (cho người tự học)

> Làm tuần tự, dừng ở mỗi ✅ **Checkpoint**. Quy tắc số 1: **đọc plan trước khi apply**.

**Bước 1 — init.**
```bash
terraform init
```
✅ **Checkpoint:** `Terraform has been successfully initialized!`.

**Bước 2 — plan và đọc kỹ.**
```bash
terraform plan
```
✅ **Checkpoint:** `1 to add, 0 to change, 0 to destroy`. Luôn để ý số **destroy** — nếu bất ngờ > 0 thì DỪNG, xem lại.

**Bước 3 — apply và lấy output.**
```bash
terraform apply
terraform output public_ip
```
✅ **Checkpoint:** `Apply complete!`, có IP; tài nguyên xuất hiện trong Console.

**Bước 4 — Chứng minh tính idempotent.**
```bash
terraform apply       # lần 2
```
✅ **Checkpoint:** báo `0 to add, 0 to change, 0 to destroy` — không tạo lại.
💡 Bạn mô tả *trạng thái mong muốn*, Terraform chỉ hành động khi có chênh lệch.

**Bước 5 — destroy.**
```bash
terraform destroy
```
✅ **Checkpoint:** `Destroy complete!` — không còn tốn phí.

### 🐛 Gỡ lỗi nhanh

| Triệu chứng | Nguyên nhân | Cách sửa |
|---|---|---|
| `No valid credential sources` | Chưa cấu hình access key | `aws configure` (không commit key) |
| `plan` báo destroy bất ngờ | Đổi thuộc tính "force new" | Đọc kỹ plan; cân nhắc trước khi apply |
| `Error acquiring the state lock` | Người khác/tiến trình cũ đang giữ lock | Chờ, hoặc `force-unlock` (cẩn thận) |
| State "drift" | Ai đó sửa tay tài nguyên trên Console | Đừng sửa tay; `apply` để đưa về đúng code |
| Lỡ commit `.tfstate` | Chứa secret | Gỡ khỏi Git, thêm `.gitignore`, chuyển remote state |

### 📝 Bài ôn tập & Demo đối chiếu

**✍️ Tự kiểm tra:**

<details>
<summary>1. IaC giải quyết vấn đề gì so với click thủ công?</summary>

> Lặp lại được, version trong Git, review qua PR, có dấu vết, rollback bằng revert code, tạo/xoá hàng loạt bằng 1 thay đổi. Giải đúng 5 điểm yếu của deploy tay.
</details>

<details>
<summary>2. Vai trò của `terraform plan` trước `apply`?</summary>

> Cho xem **chính xác** sẽ tạo/sửa/xoá gì trước khi thực thi — để không vô tình xoá nhầm tài nguyên. Luôn đọc kỹ dòng `destroy`.
</details>

<details>
<summary>3. Vì sao không sửa tay `tfstate`?</summary>

> `.tfstate` là bản đồ giữa code ↔ tài nguyên thật. Sửa sai là Terraform mất dấu, gây tạo trùng/xoá nhầm. Nó cũng chứa secret nên không commit lên Git.
</details>

<details>
<summary>4. "Idempotent" trong Terraform nghĩa là gì?</summary>

> Chạy `apply` nhiều lần ra cùng kết quả; lần sau không tạo lại nếu thực tế đã khớp với code (`0 to add/change`).
</details>

**🔬 Demo đối chiếu:**

| Demo đối chiếu | Kết quả mong đợi |
|---|---|
| `terraform init` | `successfully initialized` |
| `terraform plan` | `1 to add, 0 to change, 0 to destroy` |
| `terraform apply` | `Apply complete!`, tài nguyên xuất hiện |

### 📚 Thuật ngữ Anh–Việt (ngày này)

| Thuật ngữ | Nghĩa |
|---|---|
| **IaC** | Hạ tầng dưới dạng code |
| **Terraform / HCL** | Công cụ IaC / ngôn ngữ của nó |
| **provider / resource** | Nhà cung cấp / tài nguyên cần tạo |
| **state file** | Bản đồ trạng thái hạ tầng |
| **plan / apply / destroy** | Xem trước / thực thi / xoá |
| **Idempotent** | Chạy lại ra cùng kết quả |
| **Drift** | Thực tế lệch khỏi code (do sửa tay) |

### 🎯 Đúc kết Ngày 29

**3 điều phải mang theo:**
1. **IaC = mô tả hạ tầng bằng code** → lặp lại được, version trong Git, review qua PR, rollback bằng revert (giải đúng 5 điểm yếu của deploy tay ở Ngày 28).
2. **Vòng làm việc:** `init` → `plan` (xem trước) → `apply` (làm thật) → `destroy` (dọn). Idempotent: chạy lại chỉ đổi khi có chênh lệch.
3. **State file là "trí nhớ" của Terraform** — giữ gìn cẩn thận: không sửa tay, không commit, khoá khi làm team (remote backend).

> 🧠 **Một câu để nhớ:** **luôn đọc `terraform plan` trước khi `apply`** — đặc biệt để ý dòng `destroy`. Nhiều sự cố production do apply mà không đọc plan, vô tình xoá nhầm tài nguyên.

**✅ Tự chấm** *(đánh dấu khi làm được mà không nhìn tài liệu):*
- [ ] Giải thích được IaC hơn gì so với click chuột (nêu ≥3 lợi ích)
- [ ] Đi trọn vòng `init → plan → apply → destroy` trên 1 VM thật
- [ ] Nói được vì sao không sửa tay / không commit `.tfstate`
- [ ] Giải thích "idempotent" bằng lời của mình
- [ ] Biết remote backend giải quyết vấn đề gì khi làm team

✅ **Kết quả đạt được:** Tạo hạ tầng cloud bằng code với Terraform (init→plan→apply→destroy), hiểu state & idempotent — kỹ năng DevOps hiện đại cốt lõi.

---

## Ngày 30 — MILESTONE: LAB tổng hợp Giai đoạn 2

> ⏱️ ~180 phút · Loại: LAB Final
>
> 🧭 **Bạn đang ở đâu:** Ngày 13–29 (Git, Docker, Compose, Nginx, database, Cloud, Terraform) → **Ngày 30 (ghép tất cả: hạ tầng bằng code, ứng dụng bằng container, mọi thứ trong Git)** → Giai đoạn 3 (CI/CD & Kubernetes).
>
> ✅ **Chuẩn bị:** Docker, Terraform, Multipass (hoặc VM cloud thật). Hệ thống ba tầng từ Ngày 21.
>
> 🎯 **Đề bài + tiêu chí chấm.** Đây là bài lớn nhất của Giai đoạn 2 — hãy dành đủ thời gian.

### 📋 Đề bài — "Từ repo Git tới hệ thống đang chạy"

> Yêu cầu duy nhất, nhưng khắt khe: **xoá sạch mọi thứ, rồi dựng lại toàn bộ hệ thống từ số 0 chỉ bằng các lệnh có trong README** — hạ tầng lẫn ứng dụng. Không bấm chuột, không thao tác nhớ trong đầu.

```text
   Git repo
      │
      ├── terraform/        → dựng máy chủ (Ngày 29)
      ├── app/              → ứng dụng 3 tầng (Ngày 21)
      ├── cloud-init.yaml   → máy tự cấu hình (Ngày 27)
      └── deploy.sh         → đưa ứng dụng lên máy (Ngày 28)
```

### ✅ Yêu cầu

#### Bắt buộc

| # | Yêu cầu | Kiến thức từ |
|---|---|---|
| 1 | **Terraform** dựng được máy chủ, có biến và output | Ngày 29 |
| 2 | Máy tự cấu hình bằng **cloud-init**: user, SSH khoá, tường lửa, Docker | Ngày 27 |
| 3 | Ứng dụng ba tầng chạy bằng **Docker Compose** sau reverse proxy | Ngày 21, 28 |
| 4 | Database có **volume**, dữ liệu sống sót khi tạo lại container | Ngày 19 |
| 5 | **Script deploy** một lệnh: đưa code lên và khởi động | Ngày 6, 28 |
| 6 | **Lịch sử Git sạch**: commit có ý nghĩa, có nhánh, có tag phiên bản | Ngày 13–15, 25 |
| 7 | **Không bí mật nào trong Git** — dùng `.env` và `.env.example` | Ngày 26 |
| 8 | `terraform destroy` **xoá sạch**, không sót tài nguyên | Ngày 29 |
| 9 | README: dựng từ số 0 thế nào, xoá thế nào | — |

#### Nâng cao

| # | Yêu cầu |
|---|---|
| 10 | Terraform tách **module** thay vì viết phẳng |
| 11 | Hai môi trường dev/prod khác quy mô từ cùng bộ code |
| 12 | Script sao lưu database tự động, có kiểm chứng |
| 13 | HTTPS bằng chứng chỉ tự ký hoặc Caddy tự động |
| 14 | Tag Git khớp với phiên bản đang chạy trên máy chủ |

### 📐 Tiêu chí chấm (100 điểm)

| Hạng mục | Điểm | Đạt tối đa khi |
|---|---:|---|
| Hạ tầng bằng code | 20 | `apply` từ số 0 ra máy chủ hoạt động; có biến, output; `destroy` sạch |
| Máy tự cấu hình | 15 | cloud-init lo hết; không SSH vào cài tay thứ gì |
| Đóng gói ứng dụng | 15 | Ba tầng chạy được, chỉ proxy lộ cổng, dữ liệu bền |
| Tự động hoá deploy | 15 | Một lệnh; có xử lý lỗi; chạy lại được nhiều lần |
| Thực hành Git | 10 | Commit rõ nghĩa, có nhánh và tag, không file rác |
| Bảo mật | 15 | Không bí mật trong Git, SSH chỉ khoá, tường lửa chặn mặc định |
| Tài liệu | 10 | Người lạ dựng lại được toàn bộ hệ thống |

> 🎯 **Từ 75 điểm** là sẵn sàng cho Giai đoạn 3.

### 🔥 Phép thử lớn: "Xoá sạch rồi dựng lại"

Đây là **bài kiểm tra duy nhất thật sự quan trọng** của ngày hôm nay. Bấm giờ từ đầu đến cuối.

```bash
BAT_DAU=$(date +%s)

# ---- BƯỚC 1: XOÁ SẠCH ----
cd terraform && terraform destroy -auto-approve && cd ..
multipass list          # phải trống (hoặc: kiểm tra trên cloud không còn gì)

# ---- BƯỚC 2: DỰNG LẠI, CHỈ DÙNG LỆNH TRONG README ----
cd terraform
terraform init && terraform apply -auto-approve
IP=$(terraform output -raw dia_chi_ip)
cd ..

./deploy.sh "$IP"

# ---- BƯỚC 3: KIỂM CHỨNG ----
sleep 15
curl -s "http://$IP/" | head -5
curl -s -o /dev/null -w "HTTP %{http_code}\n" "http://$IP/api/health"

KET_THUC=$(date +%s)
echo "⏱️  Dựng lại toàn bộ từ số 0: $(( (KET_THUC-BAT_DAU)/60 )) phút $(( (KET_THUC-BAT_DAU)%60 )) giây"
```

| Thời gian | Đánh giá |
|---|---|
| Dưới 10 phút | 🟢 Tự động hoá tốt |
| 10–20 phút | 🟡 Còn vài bước thủ công |
| Trên 20 phút, hoặc phải sửa gì đó giữa chừng | 🔴 Chưa thật sự là Infrastructure as Code |

> 💡 **Mỗi lần bạn phải dừng lại gõ thêm một lệnh không có trong README, đó là một lỗi.** Ghi lại và bổ sung vào script. Lặp lại phép thử tới khi chạy trót lọt một mạch.

### 🧪 Bộ kiểm chứng

```bash
#!/usr/bin/env bash
diem=0
kiem() { if eval "$2" &>/dev/null; then echo "  ✅ $1 (+$3)"; diem=$((diem+$3)); else echo "  ❌ $1"; fi; }

echo "▸ Hạ tầng bằng code"
kiem "Terraform hợp lệ"              "terraform -chdir=terraform validate" 7
kiem "Có biến có mô tả"              "grep -q 'description' terraform/variables.tf" 4
kiem "Có output"                     "[ -f terraform/outputs.tf ] || grep -q 'output' terraform/*.tf" 4
kiem "KHÔNG commit state"            "! git ls-files | grep -q tfstate" 5

echo "▸ Máy tự cấu hình"
kiem "Có cloud-init"                 "[ -f cloud-init.yaml ] || grep -rq 'cloud-config' ." 8
kiem "cloud-init có khai tường lửa"  "grep -q 'ufw' cloud-init.yaml" 7

echo "▸ Ứng dụng"
kiem "Có docker-compose"             "[ -f app/docker-compose.yml ] || [ -f docker-compose.yml ]" 5
kiem "Có định nghĩa volume"          "grep -rq 'volumes:' app/docker-compose.yml docker-compose.yml 2>/dev/null" 5
kiem "Có healthcheck"                "grep -rq 'healthcheck' app/docker-compose.yml docker-compose.yml 2>/dev/null" 5

echo "▸ Tự động hoá"
kiem "Có script deploy"              "[ -x deploy.sh ]" 8
kiem "Script có xử lý lỗi"           "head -5 deploy.sh | grep -q 'set -e'" 7

echo "▸ Git"
kiem "Có nhiều hơn 10 commit"        "[ \$(git rev-list --count HEAD) -gt 10 ]" 4
kiem "Có tag phiên bản"              "git tag | grep -q ." 3
kiem "Có .gitignore"                 "[ -f .gitignore ]" 3

echo "▸ Bảo mật"
kiem "Không commit .env"             "! git ls-files | grep -qE '^\.env$'" 5
kiem "Có .env.example"               "[ -f .env.example ] || [ -f app/.env.example ]" 5
kiem "Không có khoá riêng trong Git" "! git ls-files | grep -qE '\.pem$|id_rsa$|id_ed25519$'" 5

echo "▸ Tài liệu"
kiem "README có hướng dẫn dựng"      "grep -qiE 'terraform apply|deploy' README.md" 5
kiem "README có hướng dẫn xoá"       "grep -qi 'destroy' README.md" 5

echo ""
echo "  ĐIỂM: $diem / 100"
```

Chạy thêm bộ quét bí mật để chắc chắn:
```bash
docker run --rm -v "$PWD:/repo" zricethezav/gitleaks:latest detect --source=/repo --no-banner
```

### ⚠️ Những cái bẫy hay gặp

| Bẫy | Hậu quả | Cách tránh |
|---|---|---|
| Sửa tay trên máy chủ rồi quên | Dựng lại là mất hết | Mọi thay đổi vào `cloud-init.yaml` hoặc `deploy.sh` |
| Commit `terraform.tfstate` | **Lộ bí mật**, và xung đột khi làm nhóm | `.gitignore` từ commit đầu |
| Commit file khoá `.pem` | Ai clone cũng vào được máy chủ | Đưa vào `.gitignore`, sinh khoá lúc chạy |
| `destroy` không sạch | Tài nguyên mồ côi vẫn tính tiền | Kiểm tra lại sau mỗi lần destroy |
| README viết lúc mới bắt đầu | Không khớp với thực tế cuối cùng | Viết lại **sau khi** làm xong phép thử lớn |
| Script deploy chỉ chạy đúng lần đầu | Lần hai lỗi vì thư mục đã tồn tại | Viết script **chạy lại được nhiều lần** |

### 💬 Gợi ý khi bí

<details>
<summary><b>Script deploy nên viết thế nào cho chạy lại được nhiều lần?</b></summary>

Nguyên tắc: mọi bước đều phải an toàn khi chạy lần thứ hai (đây chính là **idempotent** mà Ngày 47 sẽ gọi tên).

```bash
#!/usr/bin/env bash
set -euo pipefail

IP="${1:?Dùng: ./deploy.sh <dia-chi-ip>}"
KHOA="${KHOA_SSH:-./khoa-may-chu}"
USER="${SSH_USER:-quantri}"
DICH="/opt/ungdung"

ssh_chay() { ssh -i "$KHOA" -o StrictHostKeyChecking=no "$USER@$IP" "$@"; }

echo "[1/5] Chờ SSH sẵn sàng..."
for i in $(seq 1 30); do
  ssh_chay true 2>/dev/null && break
  sleep 5
done

echo "[2/5] Tạo thư mục (an toàn khi đã tồn tại)..."
ssh_chay "sudo mkdir -p $DICH && sudo chown $USER:$USER $DICH"

echo "[3/5] Đồng bộ mã nguồn..."
rsync -az --delete -e "ssh -i $KHOA -o StrictHostKeyChecking=no" \
  --exclude '.git' --exclude 'node_modules' \
  ./app/ "$USER@$IP:$DICH/"

echo "[4/5] Khởi động dịch vụ..."
ssh_chay "cd $DICH && docker compose up -d --build"

echo "[5/5] Kiểm tra sức khoẻ..."
for i in $(seq 1 20); do
  if curl -fs --max-time 3 "http://$IP/health" >/dev/null; then
    echo "✅ Hệ thống đã sẵn sàng: http://$IP"
    exit 0
  fi
  sleep 3
done
echo "❌ Không phản hồi sau 60 giây"
ssh_chay "cd $DICH && docker compose logs --tail 30"
exit 1
```

Bốn điểm khiến script này dùng được thật: `set -euo pipefail`, chờ SSH sẵn sàng, `mkdir -p` an toàn khi lặp, và **kiểm tra sức khoẻ ở cuối** — không có bước cuối thì script luôn báo thành công kể cả khi ứng dụng chết.
</details>

<details>
<summary><b>Làm sao tránh lộ khoá SSH trong Git?</b></summary>

Đừng commit khoá — **sinh nó ra lúc chạy**:

```bash
# Trong README, bước đầu tiên:
ssh-keygen -t ed25519 -f ./khoa-may-chu -N "" -C "lab30"
```

```gitignore
# .gitignore
khoa-may-chu
khoa-may-chu.pub
*.pem
.env
terraform.tfstate*
.terraform/
```

Terraform đọc khoá công khai từ file lúc `apply`:
```hcl
variable "duong_dan_khoa_cong_khai" {
  description = "Đường dẫn tới file khoá công khai"
  type        = string
  default     = "../khoa-may-chu.pub"
}
```

Như vậy repo không chứa bí mật nào, mà người khác clone về vẫn dựng được — họ chỉ cần sinh khoá của chính họ.
</details>

<details>
<summary><b>README nên có gì?</b></summary>

Đúng bốn mục, và mục thứ hai phải **copy-dán chạy được**:

```markdown
## Hệ thống này là gì
Ứng dụng 3 tầng chạy trên máy chủ được dựng hoàn toàn bằng code.

## Dựng từ số 0
```bash
ssh-keygen -t ed25519 -f ./khoa-may-chu -N ""
cd terraform && terraform init && terraform apply -auto-approve
IP=$(terraform output -raw dia_chi_ip) && cd ..
./deploy.sh "$IP"
```
Mở http://$IP

## Xoá sạch
```bash
cd terraform && terraform destroy -auto-approve
```

## Kiến trúc
(sơ đồ Mermaid)
```

Nguyên tắc kiểm tra: **mọi lệnh trong README phải copy-dán chạy được**, không có chỗ nào ghi "sau đó cấu hình X" mà không nói cấu hình thế nào.
</details>

### 🎯 Đúc kết Ngày 30 — Tổng kết Giai đoạn 2

**3 điều phải mang theo:**

1. **"Dựng lại được từ số 0" là thước đo duy nhất đáng tin.** Hệ thống chạy tốt nhưng không dựng lại được thì bạn đang sở hữu một quả bom hẹn giờ.
2. **Mọi thứ phải nằm trong Git** — hạ tầng, cấu hình máy, đóng gói ứng dụng, script deploy. Thứ gì chỉ tồn tại trên máy chủ là thứ sẽ mất.
3. **Bí mật không bao giờ vào Git.** Sinh khoá lúc chạy, cấu hình qua `.env`, và luôn có `.env.example` để người khác biết cần khai gì.

> 🧠 **Một câu để nhớ:** hết Giai đoạn 2, bạn không còn "có một máy chủ" — bạn có **công thức để tạo ra máy chủ đó bất cứ lúc nào**. Đó là khác biệt lớn nhất giữa vận hành thủ công và vận hành bằng code.

**✅ Tự chấm Milestone Giai đoạn 2:**

- [ ] Đạt từ 75 điểm ở bộ kiểm chứng
- [ ] **Phép thử lớn:** xoá sạch rồi dựng lại một mạch, dưới 20 phút
- [ ] Gitleaks không phát hiện bí mật nào
- [ ] `terraform destroy` xoá sạch, không sót tài nguyên
- [ ] README đủ để người lạ dựng lại toàn bộ
- [ ] Giải thích được vì sao mỗi thứ nằm ở chỗ của nó

✅ **Kết quả đạt được:** Toàn bộ hệ thống — hạ tầng lẫn ứng dụng — nằm trong Git và dựng lại được bằng vài lệnh. Giai đoạn 3 sẽ để **máy tự chạy những lệnh đó thay bạn**.

---

## Phụ lục A — Lỗi thường gặp (Git · Docker · Cloud)

| Lỗi kinh điển | Hậu quả | Cách làm đúng |
|---|---|---|
| `git push --force` lên nhánh chung | Xóa commit của người khác | Dùng `--force-with-lease`, không force nhánh chung |
| Commit `.env`/key/`.tfstate` lên Git | Lộ secret vĩnh viễn | `.gitignore` ngay; nếu lỡ → **rotate secret** |
| Rebase nhánh đã push/chia sẻ | Phá lịch sử của team | Chỉ rebase nhánh riêng chưa push |
| `docker compose down -v` nhầm | Xóa cả volume → mất dữ liệu | Đọc kỹ `-v`; backup volume trước |
| Dùng tag `latest` ở production | Build/deploy ra phiên bản bất ngờ | Pin tag rõ ràng `1.2.3` |
| DB không có volume | Mất dữ liệu khi xóa container | Database luôn gắn named volume |
| Security Group mở `0.0.0.0/0` cổng 22 | Bị brute-force liên tục | Chỉ mở SSH từ IP của bạn |
| Quên tắt instance / NAT GW | Hóa đơn cloud bất ngờ | Billing alert + `terraform destroy` sau demo |
| Sửa tay `.tfstate` hoặc console khi đã dùng IaC | Lệch state ↔ thực tế (drift) | Mọi thay đổi qua code + `apply` |
| Chạy `apply` không đọc `plan` | Vô tình xóa tài nguyên | Luôn `plan -out` rồi review trước `apply` |

## Phụ lục B — Playbook xử lý sự cố

**🔴 "Container chết ngay sau khi chạy"**
```bash
docker logs <container>              # đọc lỗi — 90% nằm ở đây
docker ps -a                         # Exit code? 0=xong việc, 1+=lỗi, 137=OOM/killed
docker run -it --entrypoint sh <img> # vào shell debug thủ công
```

**🔴 "App không kết nối được database" (trong Compose)**
1. Cùng network chưa? `docker network inspect <net>`
2. Dùng đúng **tên service** chưa? (host = `db`, không phải `localhost`)
3. DB sẵn sàng chưa? → thiếu healthcheck/retry → app connect trước khi DB lên.
4. Sai mật khẩu/biến env? `docker compose config` xem giá trị đã merge.

**🔴 "Build Docker chậm/lặp lại từ đầu mỗi lần"**
- Sai thứ tự layer (copy code trước dependency) → sửa thứ tự Dockerfile.
- Thiếu `.dockerignore` → build context khổng lồ.
- `docker build --progress=plain` xem layer nào không hit cache.

**🔴 "SSH vào EC2 báo lỗi permission / timeout"**
- `Permissions 0644 too open` → `chmod 400 key.pem`.
- `timeout` → Security Group chưa mở 22 từ IP bạn / sai public IP.
- `Connection refused` → instance chưa boot xong / sshd chưa lên.

**🔴 "terraform apply lỗi / state lệch"**
```bash
terraform plan          # xem drift giữa code và thực tế
terraform refresh       # đồng bộ state với thực tế
terraform state list    # xem state đang quản tài nguyên nào
terraform import ...     # đưa tài nguyên tạo tay vào state
```

## Phụ lục C — Cheat sheet

```text
# GIT HÀNG NGÀY
git switch -c feature/x          # tạo + chuyển nhánh
git add -p                       # stage từng phần có chủ đích
git commit -m "feat: ..."        # conventional commits
git rebase origin/main           # cập nhật nhánh trước PR
git reflog                       # cứu commit "đã mất"
git revert <commit>              # hoàn tác an toàn nhánh chung

# DOCKER HÀNG NGÀY
docker compose up -d             # chạy nền
docker compose logs -f <svc>     # theo dõi log 1 service
docker exec -it <ct> sh          # vào trong container
docker system prune -a           # dọn rác (đĩa đầy)
docker stats                     # CPU/RAM realtime các container
docker build --progress=plain .  # debug build

# CLOUD / VM
ssh -i key.pem ubuntu@<ip>       # vào VM (key chmod 400)
chmod 400 key.pem                # quyền bắt buộc cho key
# Security Group: chỉ mở cổng cần, SSH từ IP của bạn

# TERRAFORM
terraform fmt && terraform validate
terraform plan -out=tfplan       # luôn xem trước
terraform apply tfplan           # apply đúng cái đã review
terraform destroy                # dọn để khỏi tốn phí
terraform state list             # tài nguyên đang quản
```

> 💬 **Lời khuyên cuối Giai đoạn 2:** Bạn vừa đi từ "gõ lệnh trên 1 máy" đến "mô tả cả hạ tầng + ứng dụng bằng code, version trong Git". Bước nhảy tư duy quan trọng nhất là: **mọi thứ nên là code, lặp lại được, review được** — không còn "click thủ công rồi quên". Giai đoạn 3 sẽ tự động hóa nốt phần deploy (CI/CD) và điều phối container ở quy mô lớn (Kubernetes).

> ➡️ **Tiếp theo — Giai đoạn 3 (Ngày 31–50):** CI/CD, Kubernetes & Monitoring. Trái tim của DevOps.
