# Giai đoạn 3 — CI/CD, Kubernetes & Tự động hóa nâng cao

> **Ngày 31–50** · Trái tim của DevOps: pipeline tự động và điều phối container ở quy mô lớn.
>
> **Khuôn mỗi ngày:** 📘 Lý thuyết (mở bằng vấn đề có thật) → 🧪 LAB (file đầy đủ, copy là chạy) → 🧭 Hướng dẫn step by step (lệnh → output mẫu → ✅ checkpoint → ⚠️ lỗi cụ thể → 💡 vì sao) → 💡 Đi làm mới thấm → 🎯 Đúc kết + tự chấm.
>
> **Ngày Milestone (35, 40, 50):** 📋 Đề bài → ✅ Yêu cầu → 📐 Tiêu chí chấm điểm → 🔥 Phép thử → 💬 Gợi ý khi bí. **Không hướng dẫn từng bước.**
>
> 🧵 **Một dự án xuyên suốt:** repo `ci-demo` khởi tạo ở Ngày 31 được dùng lại và mở rộng qua Ngày 32–35; stack giám sát dựng ở Ngày 44 được cắm thêm Grafana (45), Loki (46) rồi SLO (51). Bạn xây **một** hệ thống lớn dần, không phải 20 bài rời rạc.
>
> 💻 **Mọi LAB chạy miễn phí trên máy bạn:** Docker + minikube + GitHub Actions (runner miễn phí). Ngày 34 dùng **self-hosted runner** để biến chính máy bạn thành "server" — không cần thuê VM.
>
> ✅ Trung lập nền tảng: ví dụ CI dùng GitHub Actions, K8s dùng Minikube — đều có ghi chú công cụ tương đương (GitLab CI, Jenkins, EKS/GKE/AKS...).

---

## Mục lục

| Ngày | Chủ đề |
|------|--------|
| [31](#ngày-31--cicd-khái-niệm--github-actions-cơ-bản) | CI/CD — Khái niệm & GitHub Actions cơ bản |
| [32](#ngày-32--ci-pipeline-build-test--lint-tự-động) | CI Pipeline — Build, Test & Lint tự động |
| [33](#ngày-33--cd-pipeline-build--push-docker-image) | CD Pipeline — Build & Push Docker Image |
| [34](#ngày-34--cd-pipeline-tự-động-deploy-lên-server) | CD Pipeline — Tự động Deploy lên Server |
| [35](#ngày-35--milestone-pipeline-cicd-hoàn-chỉnh) | **Milestone — Pipeline CI/CD hoàn chỉnh** |
| [36](#ngày-36--kubernetes-khái-niệm--kiến-trúc) | Kubernetes — Khái niệm & Kiến trúc |
| [37](#ngày-37--kubernetes-pod-deployment--replicaset) | Kubernetes — Pod, Deployment & ReplicaSet |
| [38](#ngày-38--kubernetes-service--networking) | Kubernetes — Service & Networking |
| [39](#ngày-39--kubernetes-configmap-secret--storage) | Kubernetes — ConfigMap, Secret & Storage |
| [40](#ngày-40--milestone-deploy-full-stack-lên-kubernetes) | **Milestone — Deploy Full-stack lên Kubernetes** |
| [41](#ngày-41--kubernetes-health-check-resource--autoscaling) | Kubernetes — Health Check, Resource & Autoscaling |
| [42](#ngày-42--helm-package-manager-cho-kubernetes) | Helm — Package Manager cho Kubernetes |
| [43](#ngày-43--gitops-argocd--triển-khai-khai-báo) | GitOps — ArgoCD & Triển khai khai báo |
| [44](#ngày-44--monitoring-prometheus--metrics) | Monitoring — Prometheus & Metrics |
| [45](#ngày-45--monitoring-grafana-dashboard) | Monitoring — Grafana Dashboard |
| [46](#ngày-46--logging-tập-trung-loki) | Logging tập trung — Loki |
| [47](#ngày-47--configuration-management-ansible) | Configuration Management — Ansible |
| [48](#ngày-48--terraform-nâng-cao-module-remote-state--workspace) | Terraform nâng cao — Module, Remote State |
| [49](#ngày-49--bảo-mật-devsecops--best-practices) | Bảo mật DevSecOps & Best Practices |
| [50](#ngày-50--milestone-lab-tổng-hợp-giai-đoạn-3) | **Milestone — LAB tổng hợp Giai đoạn 3** |

---

## Ngày 31 — CI/CD: Khái niệm & GitHub Actions cơ bản

> ⏱️ ~90 phút · Loại: CI/CD
>
> 🧭 **Bạn đang ở đâu:** Giai đoạn 2 (Git, Docker, Cloud, IaC) → **Ngày 31 (CI/CD — robot tự build/test khi bạn push)** → Ngày 32 (pipeline CI đầy đủ). Đây là kỹ năng "định danh" của nghề DevOps, và là lời giải cho nỗi đau deploy tay ở Ngày 28.
>
> 🔧 *Ví dụ dùng GitHub Actions vì miễn phí và không phải cài gì. Tương đương: **GitLab CI** (`.gitlab-ci.yml`), **Jenkins** (`Jenkinsfile`), **CircleCI** — khác cú pháp, giống hệt nhau về tư duy.*
>
> ✅ **Chuẩn bị:** tài khoản GitHub + Git đã cấu hình (Ngày 1), Node.js trên máy (`node --version`, cần ≥ 18). Không cần cài server CI — GitHub cấp máy chạy sẵn.
>
> 🎁 **Cuối ngày bạn có gì:** repo `ci-demo` với một ứng dụng Node nhỏ và workflow đầu tiên tự chạy test mỗi lần bạn push. **Repo này dùng xuyên suốt Ngày 31 → 35**, đừng xoá.

### 📘 Lý thuyết

#### 1. Vấn đề có thật: vì sao cần robot

Nhớ lại Ngày 28 — bạn deploy bằng tay: SSH vào server, `git pull`, `npm install`, restart. Nó chạy được. Nhưng:

- Hôm bạn nghỉ phép, **không ai khác biết thứ tự các bước**.
- Có hôm bạn quên chạy test → đẩy bug lên production, phát hiện sau 3 tiếng.
- Có hôm bạn quên bước `npm install` → app chết vì thiếu thư viện.
- Hỏi "lần deploy tuần trước ai làm, lúc mấy giờ, từ commit nào?" → **không ai trả lời được**.

Điểm chung: quy trình nằm **trong đầu một người**, không nằm trong code. CI/CD là việc lấy quy trình đó ra khỏi đầu bạn và **viết nó thành file**, để máy chạy — mỗi lần y hệt nhau, có log, có dấu vết.

| | Viết tắt | Máy làm gì cho bạn |
|---|---|---|
| **CI** | Continuous Integration | Mỗi lần push → tự **build + test + lint**, báo lỗi trong vài phút |
| **CD** | Continuous Delivery/Deployment | Test đạt → tự **đưa lên** staging/production |

#### 2. GitHub Actions — robot có sẵn ngay trong repo

Bạn đặt một file YAML vào đúng thư mục `.github/workflows/`. GitHub thấy file đó, và mỗi khi có sự kiện (push, mở Pull Request), nó **mượn cho bạn một máy ảo sạch**, tải code về, rồi chạy đúng các bước bạn ghi. Không cần dựng server CI, không tốn tiền với repo cá nhân.

#### 3. Ba tầng: Workflow → Job → Step

| Tầng | Là gì | Chạy thế nào |
|---|---|---|
| **Workflow** | Cả quy trình = 1 file YAML | Khởi động bởi **trigger** (`on:`) |
| **Job** | Một nhóm việc, chạy trên **1 máy ảo riêng** | Các job **chạy song song** mặc định; dùng `needs:` để bắt xếp hàng |
| **Step** | Từng bước trong job | **Tuần tự** từ trên xuống |

> ⚠️ Điểm này người mới hay vấp: **hai job khác nhau = hai máy khác nhau**. Job A tạo file thì job B *không thấy file đó*. Muốn chuyển đồ giữa các job phải dùng **artifact** (Ngày 32).

#### 4. Bốn thứ bạn sẽ gặp trong mọi workflow

- **Trigger** (`on:`) — khi nào chạy: `push`, `pull_request`, `schedule` (theo giờ), `workflow_dispatch` (bấm tay).
- **Runner** (`runs-on:`) — máy ảo GitHub cấp (`ubuntu-latest`), **xoá sạch sau mỗi lần chạy**. Chính vì sạch nên CI không bao giờ dính bệnh "máy tôi chạy được".
- **Action** (`uses:`) — khối dựng sẵn người khác viết, cài bằng 1 dòng: `actions/checkout` (tải code), `actions/setup-node` (cài Node).
- **Lệnh shell** (`run:`) — gõ gì trên Linux thì viết y vậy: `npm ci`, `npm test`.

#### 5. Secret — chỗ cất chìa khoá

Token, mật khẩu **không bao giờ** được viết thẳng vào YAML, vì YAML nằm trong repo — commit lên là lộ vĩnh viễn (kể cả sau này xoá đi, lịch sử Git vẫn còn). Cất ở **Settings → Secrets and variables → Actions**, rồi đọc bằng `${{ secrets.TEN_BIEN }}`. GitHub tự thay giá trị bằng `***` trong log.

### 🧪 LAB — Ứng dụng Node + workflow CI đầu tiên

> **Mục tiêu:** tạo repo `ci-demo`, viết app nhỏ có test, rồi để GitHub tự chạy test mỗi lần push. Toàn bộ file dưới đây đầy đủ, copy là chạy.

**Cây thư mục sẽ tạo:**

```text
ci-demo/
├── .github/
│   └── workflows/
│       └── ci.yml          # workflow đầu tiên
├── src/
│   └── tinh-tien.js        # hàm nghiệp vụ để có cái mà test
├── test/
│   └── tinh-tien.test.js   # test tự động
├── app.js                  # web server nhỏ
└── package.json
```

#### File 1 — `package.json`

```json
{
  "name": "ci-demo",
  "version": "1.0.0",
  "description": "App mẫu để học CI/CD",
  "main": "app.js",
  "scripts": {
    "start": "node app.js",
    "test": "node --test test/"
  },
  "license": "MIT"
}
```

> 📌 `node --test` là bộ chạy test **có sẵn trong Node từ bản 18** — không phải cài thêm thư viện nào. Bớt được một tầng phức tạp cho người mới.

#### File 2 — `src/tinh-tien.js`

```javascript
// Tính tiền đơn hàng: cộng tiền các món rồi áp mã giảm giá (nếu có).
function tinhTien(cacMon, phanTramGiam = 0) {
  if (!Array.isArray(cacMon)) {
    throw new Error('cacMon phải là một mảng');
  }
  const tongTho = cacMon.reduce((tong, mon) => tong + mon.gia * mon.soLuong, 0);
  return Math.round(tongTho * (1 - phanTramGiam / 100));
}

module.exports = { tinhTien };
```

#### File 3 — `test/tinh-tien.test.js`

```javascript
const test = require('node:test');
const assert = require('node:assert');
const { tinhTien } = require('../src/tinh-tien');

test('cộng đúng tiền nhiều món', () => {
  const gioHang = [
    { gia: 20000, soLuong: 2 },
    { gia: 15000, soLuong: 1 },
  ];
  assert.strictEqual(tinhTien(gioHang), 55000);
});

test('áp dụng giảm giá 10%', () => {
  const gioHang = [{ gia: 100000, soLuong: 1 }];
  assert.strictEqual(tinhTien(gioHang, 10), 90000);
});

test('giỏ rỗng thì trả 0', () => {
  assert.strictEqual(tinhTien([]), 0);
});

test('truyền sai kiểu thì báo lỗi', () => {
  assert.throws(() => tinhTien('không phải mảng'));
});
```

#### File 4 — `app.js`

```javascript
const http = require('node:http');
const { tinhTien } = require('./src/tinh-tien');

const PORT = process.env.PORT || 3000;

const server = http.createServer((req, res) => {
  if (req.url === '/health') {
    res.writeHead(200, { 'Content-Type': 'application/json' });
    return res.end(JSON.stringify({ trangThai: 'ok' }));
  }
  const demo = tinhTien([{ gia: 20000, soLuong: 2 }], 10);
  res.writeHead(200, { 'Content-Type': 'application/json' });
  res.end(JSON.stringify({ thongDiep: 'ci-demo đang chạy', donHangMau: demo }));
});

server.listen(PORT, () => console.log(`Đang nghe ở cổng ${PORT}`));
```

#### File 5 — `.github/workflows/ci.yml` ← nhân vật chính hôm nay

```yaml
name: CI

# KHI NÀO chạy
on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  test:                          # tên job, bạn tự đặt
    runs-on: ubuntu-latest       # máy ảo GitHub cấp, sạch mỗi lần chạy

    steps:
      - name: Tải code về runner
        uses: actions/checkout@v4      # thiếu bước này thì runner rỗng, không có gì để test

      - name: Cài Node.js
        uses: actions/setup-node@v4
        with:
          node-version: '20'

      - name: Chạy test
        run: npm test                  # gõ gì trên Linux thì viết y vậy

      - name: Báo cáo kết quả
        run: echo "✅ Test đã chạy xong trên commit ${{ github.sha }}"
```

> 📌 **Về số phiên bản action** (`@v4`): luôn **ghim phiên bản**, đừng dùng `@main`. `@main` nghĩa là "lấy bản mới nhất bất kể nó đổi gì" — hôm nay chạy, mai tác giả sửa là pipeline bạn gãy, tệ hơn là bị chèn mã độc. Muốn biết bản mới nhất hiện tại, tra tên action trên [GitHub Marketplace](https://github.com/marketplace?type=actions).

### 🧭 Hướng dẫn làm LAB — step by step

> Làm **tuần tự**. Sau mỗi bước, đối chiếu khối *"Bạn sẽ thấy"* rồi mới đi tiếp.

#### Bước 1 — Tạo repo trên GitHub

Vào GitHub → **New repository** → tên `ci-demo` → chọn **Private** → **Create repository**.

✅ **Checkpoint:** GitHub hiện trang repo rỗng kèm hướng dẫn `git remote add origin ...`.

💡 *Vì sao Private:* từ Ngày 34 bạn sẽ gắn máy của mình vào repo này làm nơi chạy lệnh. Repo public thì người lạ mở Pull Request cũng có thể khiến code của họ chạy trên máy bạn — rất nguy hiểm. Tập thói quen Private ngay từ đầu.

#### Bước 2 — Tạo project ở máy và viết 5 file

```bash
mkdir -p ~/ci-demo/.github/workflows ~/ci-demo/src ~/ci-demo/test
cd ~/ci-demo
```

Tạo lần lượt 5 file ở phần LAB (dùng `nano` hoặc VS Code). Rồi kiểm tra cây thư mục:

```bash
find . -type f -not -path './.git/*' | sort
```

**Bạn sẽ thấy:**
```text
./.github/workflows/ci.yml
./app.js
./package.json
./src/tinh-tien.js
./test/tinh-tien.test.js
```

✅ **Checkpoint:** đủ 5 file, và `ci.yml` nằm đúng trong `.github/workflows/`.

⚠️ **Sai chỗ này là hỏng cả ngày:** phải đúng `.github/workflows/` — có dấu chấm đầu, `workflows` số nhiều. Đặt vào `.github/workflow/` hay `github/workflows/` thì GitHub **im lặng bỏ qua**, không báo lỗi gì cả, và bạn sẽ ngồi tự hỏi vì sao tab Actions trống trơn.

#### Bước 3 — Chạy test ở máy trước khi đẩy lên

Luôn chạy thử ở máy trước — đừng dùng CI làm nơi thử lần đầu.

```bash
npm install          # không có thư viện ngoài, nhưng lệnh này sinh ra package-lock.json
npm test
```

**Bạn sẽ thấy:**
```text
✔ cộng đúng tiền nhiều món (1.2ms)
✔ áp dụng giảm giá 10% (0.3ms)
✔ giỏ rỗng thì trả 0 (0.2ms)
✔ truyền sai kiểu thì báo lỗi (0.4ms)
# pass 4
# fail 0
```

✅ **Checkpoint:** `# pass 4` và `# fail 0`.

⚠️ **Nếu báo `Cannot find module '../src/tinh-tien'`:** sai đường dẫn hoặc sai tên file. Kiểm tra lại bằng `ls src/`.

💡 *Vì sao chạy `npm install` dù không có thư viện nào:* nó sinh ra `package-lock.json` — file khoá phiên bản. Ngày 32 sẽ dùng `npm ci` (nhanh hơn, chính xác hơn) và lệnh đó **bắt buộc** phải có lock file.

#### Bước 4 — Đẩy lên GitHub

```bash
git init -b main
git add .
git commit -m "Khởi tạo app ci-demo + workflow CI đầu tiên"
git remote add origin git@github.com:<ten-github-cua-ban>/ci-demo.git
git push -u origin main
```

**Bạn sẽ thấy:**
```text
Enumerating objects: 11, done.
...
To github.com:<ten-cua-ban>/ci-demo.git
 * [new branch]      main -> main
```

✅ **Checkpoint:** vào trang repo trên GitHub, thấy đủ 5 file.

⚠️ **Nếu `git push` đòi username/password:** remote đang dùng HTTPS. Đổi sang SSH (bạn đã tạo khoá từ Ngày 1):
```bash
git remote set-url origin git@github.com:<ten-cua-ban>/ci-demo.git
```

#### Bước 5 — Xem robot chạy lần đầu

Mở repo trên GitHub → tab **Actions**.

**Bạn sẽ thấy:** một dòng tên đúng bằng commit message của bạn, có chấm vàng 🟡 đang quay (đang chạy), rồi chuyển ✅ xanh sau khoảng 20–40 giây.

✅ **Checkpoint:** dấu ✅ xanh.

Bấm vào dòng đó → bấm job **test** → mở rộng từng bước. Bạn sẽ thấy đúng 4 bước đã viết, kèm thời gian từng bước và log của `npm test` với `# pass 4`.

⚠️ **Nếu tab Actions trống rỗng:** file đặt sai chỗ (xem lại Bước 2), hoặc YAML sai cú pháp. Kiểm tra ngay tại chỗ: mở file `ci.yml` **trên giao diện GitHub** — nếu YAML hỏng, GitHub hiện cảnh báo đỏ kèm số dòng.

💡 Để ý bước *"Tải code về runner"* mất vài giây: đó là máy ảo đang `git clone` repo về. **Máy này hoàn toàn sạch** — không có code, không có Node, không có gì của bạn. Mọi thứ nó cần đều phải khai trong YAML. Đây chính là lý do CI không bao giờ dính bệnh "trên máy tôi vẫn chạy".

#### Bước 6 — Cố ý làm hỏng để thấy CI bắt lỗi

CI chỉ có giá trị khi nó **chặn được cái sai**. Kiểm chứng ngay:

```bash
# Sửa logic cho sai: đổi dấu trừ thành dấu cộng
sed -i 's|1 - phanTramGiam / 100|1 + phanTramGiam / 100|' src/tinh-tien.js
npm test
```

**Bạn sẽ thấy ở máy:**
```text
✔ cộng đúng tiền nhiều món
✖ áp dụng giảm giá 10%
  ...
  expected: 90000
  actual:   110000
# pass 3
# fail 1
```

Giờ cứ đẩy cái sai đó lên:

```bash
git commit -am "Thử: cố ý làm sai công thức giảm giá"
git push
```

**Bạn sẽ thấy trên tab Actions:** ❌ đỏ. Bấm vào xem log — đúng dòng `expected: 90000 / actual: 110000`, kèm email báo lỗi gửi về hộp thư của bạn.

✅ **Checkpoint:** thấy run ❌ đỏ và đọc được **chính xác test nào hỏng**.

💡 **Đây là toàn bộ giá trị của CI trong một câu:** bug bị bắt sau 30 giây bởi máy, thay vì sau 3 ngày bởi khách hàng.

Sửa lại cho đúng rồi đẩy lên:
```bash
sed -i 's|1 + phanTramGiam / 100|1 - phanTramGiam / 100|' src/tinh-tien.js
git commit -am "Sửa lại công thức giảm giá"
git push
```
Run mới phải ✅ xanh trở lại.

#### Bước 7 — Chứng minh "hai job = hai máy khác nhau"

Đây là hiểu lầm phổ biến nhất về CI. Tự tay kiểm chứng. Thêm vào cuối `ci.yml`:

```yaml
  # THÊM vào cuối file ci.yml, thụt lề ngang hàng với job "test"
  job-a:
    runs-on: ubuntu-latest
    steps:
      - run: echo "xin chào từ job A" > ghichu.txt
      - run: cat ghichu.txt

  job-b:
    runs-on: ubuntu-latest
    steps:
      - run: cat ghichu.txt || echo "❌ Không thấy file — vì đây là MÁY KHÁC"
```

Push lên và xem tab Actions.

**Bạn sẽ thấy:** 3 job (`test`, `job-a`, `job-b`) chạy **cùng lúc**, và `job-b` in ra dòng `❌ Không thấy file — vì đây là MÁY KHÁC`.

✅ **Checkpoint:** hiểu rằng file do `job-a` tạo hoàn toàn không tồn tại ở `job-b`.

💡 Muốn job chạy **xếp hàng** thay vì song song, thêm `needs:`:
```yaml
  job-b:
    needs: job-a        # chờ job-a xong mới chạy
```
Còn muốn **chuyển file** giữa các job thì phải dùng **artifact** — học ở Ngày 32.

Dọn dẹp: xoá `job-a` và `job-b` khỏi `ci.yml` rồi push (đó chỉ là thí nghiệm).

#### Bước 8 — Dùng thử Secret

Tạo secret: repo → **Settings → Secrets and variables → Actions → New repository secret**
- Name: `LOI_CHAO`
- Secret: `xin-chao-tu-secret`

Thêm bước này vào cuối job `test` trong `ci.yml`:

```yaml
      - name: Thử đọc secret
        run: |
          echo "Giá trị secret là: ${{ secrets.LOI_CHAO }}"
          echo "Độ dài chuỗi: ${#LOI_CHAO}"
        env:
          LOI_CHAO: ${{ secrets.LOI_CHAO }}
```

Push và xem log.

**Bạn sẽ thấy:**
```text
Giá trị secret là: ***
Độ dài chuỗi: 18
```

✅ **Checkpoint:** giá trị bị che thành `***`, nhưng độ dài vẫn in ra `18` — chứng tỏ workflow **thực sự đọc được** secret, chỉ là không hiện ra log.

💡 **Bài học quan trọng:** việc che `***` chỉ là lớp bảo vệ cuối. Nếu bạn *biến đổi* secret rồi mới in (ví dụ `base64`, cắt chuỗi), phần đã biến đổi **không được che nữa** → vẫn lộ. Nguyên tắc cứng: không bao giờ in secret ra log.

### 💡 Đi làm mới thấm (sách cơ bản hay bỏ quên)

- **Pull Request từ fork KHÔNG được cấp secrets.** Đây là cố tình, để người lạ không thể mở PR chỉ nhằm `echo` trộm token của bạn. Vì vậy dự án mã nguồn mở phải tách các job cần secret ra khỏi CI chạy trên PR. (`pull_request_target` cấp lại secrets nhưng là con dao hai lưỡi nổi tiếng — đừng dùng khi chưa hiểu kỹ.)
- **`concurrency` chống chạy chồng.** Push liên tiếp 5 commit thì mặc định *cả 5* run cùng chạy — tốn phút runner, và nếu là job deploy thì chúng đè lên nhau. Thêm vào đầu workflow:
  ```yaml
  concurrency:
    group: ${{ github.workflow }}-${{ github.ref }}
    cancel-in-progress: true      # huỷ run cũ, chỉ giữ run mới nhất
  ```
- **Siết quyền của `GITHUB_TOKEN`.** Token mặc định mạnh hơn bạn tưởng. Khai `permissions: { contents: read }` ở đầu workflow rồi chỉ nới đúng thứ cần (`packages: write` khi push image ở Ngày 33). Nếu một action bạn dùng bị chèn mã độc, thiệt hại bị giới hạn lại.
- **Đừng copy-paste YAML giữa các repo.** Khi 5–10 repo cùng một pipeline, tách thành **reusable workflow** (`workflow_call`) — sửa một chỗ, áp dụng mọi nơi. Đúng tư duy "đừng lặp code", chỉ là áp cho pipeline.
- **Phút runner không miễn phí vô hạn.** Repo public thì free thật; repo private có hạn mức tháng. Pipeline chạy 10 phút × 50 lần/ngày là con số thật sự tốn tiền ở công ty — đó là lý do Ngày 32 học **cache** và **xếp bước rẻ lên trước**.
- **Ghim action bằng SHA cho môi trường nhạy cảm.** `@v4` vẫn là một nhãn có thể bị đẩy đi nơi khác. Mức bảo mật cao nhất là ghim nguyên SHA: `uses: actions/checkout@8f4b7f8...`. Đây là chuẩn ở các công ty làm nghiêm về supply chain.

### 📝 Tự kiểm tra

> Nghĩ câu trả lời **thành lời** trước khi mở đáp án — nghĩ thầm luôn thấy mình hiểu.

<details>
<summary><b>1. Vì sao workflow luôn cần `actions/checkout` ở bước đầu tiên?</b></summary>

Vì runner là **máy ảo hoàn toàn sạch** — nó không có code của bạn, không có Node, không có gì cả. `checkout` chính là bước `git clone` repo về máy đó.

Thiếu bước này thì mọi lệnh sau đều chạy trên thư mục rỗng. Đây cũng chính là lý do CI không bao giờ dính bệnh *'trên máy tôi vẫn chạy'* — máy sạch buộc bạn phải khai rõ mọi thứ cần thiết.

</details>

<details>
<summary><b>2. Hai job trong cùng một workflow có chia sẻ file với nhau không? Nếu cần chuyển file thì làm sao?</b></summary>

**Không.** Hai job = hai máy ảo hoàn toàn khác nhau. Job A tạo file thì job B không hề thấy file đó.

Muốn chuyển đồ giữa các job phải dùng **artifact**: job này `upload-artifact`, job kia `download-artifact`.

Muốn job chạy **xếp hàng** thay vì song song thì dùng `needs:` — nhưng `needs:` chỉ xếp thứ tự, **không** chia sẻ file.

</details>

<details>
<summary><b>3. GitHub che secret thành `***` trong log. Vì sao đó không phải bùa hộ mệnh?</b></summary>

Việc che chỉ khớp **giá trị nguyên vẹn** của secret. Nếu bạn *biến đổi* nó rồi mới in — mã hoá base64, cắt chuỗi, nối thêm ký tự — thì phần đã biến đổi **không được che nữa** và vẫn lộ ra log.

Nguyên tắc cứng: **không bao giờ in secret ra log**, kể cả khi nghĩ rằng đã 'mã hoá nhẹ'.

</details>

### 📚 Thuật ngữ Anh–Việt (ngày này)

| Thuật ngữ | Nghĩa |
|---|---|
| **Workflow / Job / Step** | Cả quy trình (1 file YAML) / nhóm việc trên 1 máy / từng bước trong job |
| **Runner** | Máy ảo chạy job — **sạch mỗi lần chạy** |
| **Trigger (`on:`)** | Sự kiện kích hoạt workflow: push, pull_request, schedule... |
| **Action (`uses:`)** | Khối dựng sẵn người khác viết, dùng lại bằng một dòng |
| **Artifact** | Gói file lưu lại sau khi job xong — cách duy nhất chuyển đồ giữa các job |
| **GitHub Secrets** | Nơi cất token/mật khẩu; đọc bằng `${{ secrets.TÊN }}`, che `***` trong log |
| **Ghim phiên bản action** | Dùng `@v4` thay `@main` để pipeline không gãy khi tác giả sửa |

### 🎯 Đúc kết Ngày 31

**3 điều phải mang theo:**

1. **CI/CD là lấy quy trình ra khỏi đầu bạn và viết thành file** để máy chạy lại y hệt mỗi lần, có log, có dấu vết. Công cụ nào cũng chỉ là chi tiết.
2. **Runner là máy sạch** — mọi thứ nó cần phải khai trong YAML. Vì sạch nên "trên máy tôi vẫn chạy" không còn là cái cớ được nữa.
3. **Job song song, mỗi job một máy riêng.** Muốn xếp thứ tự dùng `needs:`, muốn chuyển file dùng artifact.

> 🧠 **Một câu để nhớ:** CI không làm code bạn đúng hơn — nó chỉ đảm bảo **cái sai bị phát hiện trong 30 giây thay vì 3 ngày**.

**✅ Tự chấm** *(đánh dấu khi làm được mà không nhìn tài liệu):*

- [ ] Viết được workflow tối thiểu chạy được: `on:` → `jobs:` → `runs-on:` → `steps:`
- [ ] Nói đúng đường dẫn bắt buộc của file workflow và điều gì xảy ra nếu đặt sai
- [ ] Giải thích vì sao luôn cần `actions/checkout` ở bước đầu
- [ ] Chứng minh được hai job chạy trên hai máy khác nhau
- [ ] Dùng Secret và nói rõ vì sao che `***` không phải bùa hộ mệnh
- [ ] Tự gây lỗi và đọc log CI tìm ra đúng test nào hỏng

✅ **Kết quả đạt được:** Một repo có CI thật — mỗi lần push, máy tự tải code, cài Node, chạy test và báo đỏ/xanh cho bạn.

---

## Ngày 32 — CI Pipeline: Build, Test & Lint tự động

> ⏱️ ~90 phút · Loại: CI/CD
>
> 🧭 **Bạn đang ở đâu:** Ngày 31 (workflow đầu tiên) → **Ngày 32 (pipeline CI nhiều tầng: lint → test nhiều phiên bản → build → lưu sản phẩm)** → Ngày 33 (đóng gói thành Docker image). Hôm nay bạn biến workflow đồ chơi thành pipeline dùng được thật.
>
> ✅ **Chuẩn bị:** repo `ci-demo` của Ngày 31 đang ✅ xanh. Kiểm tra nhanh: `cd ~/ci-demo && npm test`.
>
> 🎁 **Cuối ngày bạn có gì:** pipeline 3 tầng chạy đúng thứ tự, test song song trên 2 phiên bản Node, có cache cho nhanh, đóng gói sản phẩm tải về được — và `main` bị **khoá không cho merge khi CI đỏ**.

### 📘 Lý thuyết

#### 1. Vì sao phải xếp lớp: kinh tế học của thời gian chờ

Pipeline giống nhiều tấm lưới lọc đặt nối tiếp nhau:

| Lớp | Bắt loại lỗi | Mất bao lâu |
|---|---|---|
| **Lint** | Lỗi hình thức: biến thừa, gọi tên không tồn tại, style lộn xộn | ~10 giây |
| **Test** | Lỗi logic: tính sai, xử lý thiếu trường hợp | ~1–5 phút |
| **Build** | Lỗi ghép nối: thiếu file, import sai, không đóng gói được | ~1–10 phút |

Nguyên tắc: **xếp lớp rẻ và nhanh lên trước**. Một lỗi gõ nhầm tên biến bị lint chặn trong 10 giây thì không đáng để chạy hết bộ test 5 phút rồi mới phát hiện. Thứ tự các bước trong pipeline không phải ngẫu nhiên — nó là bài toán tiết kiệm thời gian chờ của cả đội.

#### 2. `needs:` — bắt các job xếp hàng

Ngày 31 bạn đã tự chứng minh job chạy **song song** mặc định. Nhưng build mà chạy song song với test thì vô nghĩa: test còn chưa biết đúng sai, đóng gói làm gì?

```yaml
jobs:
  lint:  { ... }
  test:  { needs: lint }          # chờ lint xong, xanh mới chạy
  build: { needs: test }          # chờ test xong, xanh mới chạy
```

`needs:` vừa xếp thứ tự, vừa có nghĩa "job trước **đỏ thì job sau không chạy**" — tự động dừng dây chuyền khi hỏng.

#### 3. Matrix — cùng công thức, nhiều loại bếp

Bạn viết code trên Node 20. Nhưng server công ty đang chạy Node 18. Nó có chạy được không? Đừng đoán — hãy thử cả hai **cùng lúc**:

```yaml
strategy:
  matrix:
    node: [18, 20]
```

GitHub sẽ nhân job đó ra thành 2 bản chạy song song, một bản Node 18, một bản Node 20. Thêm một phiên bản vào danh sách = thêm một bản chạy, không phải viết lại gì.

#### 4. Cache — đừng tải lại thứ đã tải

Runner sạch mỗi lần chạy, nghĩa là mỗi lần đều phải tải lại toàn bộ thư viện từ Internet. Dự án thật có vài trăm thư viện → 2–3 phút chỉ để chờ tải, mỗi lần push.

**Cache** lưu lại thư mục thư viện, lần sau lấy ra dùng. Khoá cache dựa trên `package-lock.json`: file lock không đổi → thư viện không đổi → dùng lại được. Với `actions/setup-node` chỉ cần một dòng `cache: 'npm'`.

#### 5. Artifact — cách duy nhất chuyển đồ giữa các job

Nhớ Ngày 31: hai job = hai máy khác nhau, file không tự đi theo. **Artifact** là nơi gửi đồ: job này `upload-artifact`, job kia `download-artifact`. Nó cũng là cách để **bạn tải sản phẩm về máy** từ giao diện GitHub.

#### 6. `npm ci` khác `npm install` thế nào

| | `npm install` | `npm ci` ← dùng trong CI |
|---|---|---|
| Đọc file nào | `package.json` (khoảng phiên bản) | `package-lock.json` (phiên bản chính xác) |
| Có sửa lock không | Có — âm thầm nâng phiên bản | **Không bao giờ** |
| Thư mục cũ | Cài đè lên | Xoá sạch rồi cài lại |
| Kết quả | Có thể khác nhau giữa các lần | **Luôn giống hệt nhau** |

CI cần tính tái lập → luôn `npm ci`. Nó cũng nhanh hơn đáng kể.

#### 7. Branch protection — biến CI từ trang trí thành rào chắn

CI mà không có branch protection giống như **lắp camera an ninh nhưng vẫn để cửa mở**: bạn *nhìn thấy* code đỏ, nhưng vẫn bấm merge được. Bật branch protection cho `main` là biến kết quả CI thành **điều kiện bắt buộc** — chưa xanh thì nút Merge khoá cứng, không ai phá lệ được, kể cả bạn.

### 🧪 LAB — Pipeline CI 3 tầng hoàn chỉnh

> **Mục tiêu:** nâng cấp `ci-demo` thành pipeline thật. Làm tiếp trên repo cũ.

**Những file sẽ thêm/sửa:**

```text
ci-demo/
├── .github/workflows/ci.yml   # VIẾT LẠI hoàn toàn
├── eslint.config.js           # THÊM — luật cho lint
├── package.json               # SỬA — thêm script lint
└── (các file cũ giữ nguyên)
```

#### File 1 — `eslint.config.js` (thêm mới)

```javascript
// ESLint 9 dùng "flat config" — cấu hình là một mảng các khối luật.
module.exports = [
  {
    files: ['**/*.js'],
    languageOptions: {
      ecmaVersion: 2022,
      sourceType: 'commonjs',
      // Khai báo các biến toàn cục của Node để ESLint không báo "không tồn tại"
      globals: {
        require: 'readonly',
        module: 'writable',
        process: 'readonly',
        console: 'readonly',
        __dirname: 'readonly',
      },
    },
    rules: {
      'no-unused-vars': 'error',   // biến khai rồi không dùng → lỗi
      'no-undef': 'error',         // dùng tên không tồn tại → lỗi
      'eqeqeq': 'error',           // bắt buộc === thay vì == (tránh bẫy so sánh lỏng)
      'no-console': 'off',         // app nhỏ, cho phép console.log
    },
  },
];
```

#### File 2 — `package.json` (sửa lại)

```json
{
  "name": "ci-demo",
  "version": "1.0.0",
  "description": "App mẫu để học CI/CD",
  "main": "app.js",
  "scripts": {
    "start": "node app.js",
    "test": "node --test test/",
    "lint": "eslint ."
  },
  "devDependencies": {
    "eslint": "^9.0.0"
  },
  "license": "MIT"
}
```

> 📌 `devDependencies` = thư viện chỉ cần khi phát triển/kiểm tra, **không đi theo lên production**. ESLint đúng là loại đó.

#### File 3 — `.github/workflows/ci.yml` (viết lại toàn bộ)

```yaml
name: CI

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

# Push liên tiếp thì huỷ run cũ, chỉ giữ run mới nhất — đỡ tốn phút runner
concurrency:
  group: ${{ github.workflow }}-${{ github.ref }}
  cancel-in-progress: true

# Mặc định chỉ cho đọc; job nào cần hơn thì tự khai thêm
permissions:
  contents: read

jobs:
  # ---------- TẦNG 1: rẻ nhất, chạy trước ----------
  lint:
    name: Kiểm tra chất lượng code
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-node@v4
        with:
          node-version: '20'
          cache: 'npm'              # bật cache thư viện npm

      - name: Cài thư viện
        run: npm ci

      - name: Chạy ESLint
        run: npm run lint

  # ---------- TẦNG 2: test trên nhiều phiên bản Node ----------
  test:
    name: Test trên Node ${{ matrix.node }}
    needs: lint                     # lint đỏ thì không chạy
    runs-on: ubuntu-latest
    strategy:
      fail-fast: false              # Node 18 hỏng vẫn chạy nốt Node 20 để biết toàn cảnh
      matrix:
        node: [18, 20]
    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-node@v4
        with:
          node-version: ${{ matrix.node }}
          cache: 'npm'

      - run: npm ci

      - name: Chạy test
        run: npm test

  # ---------- TẦNG 3: đóng gói sản phẩm ----------
  build:
    name: Đóng gói
    needs: test                     # chỉ đóng gói khi MỌI bản test đều xanh
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-node@v4
        with:
          node-version: '20'
          cache: 'npm'

      - run: npm ci

      - name: Tạo thư mục sản phẩm
        run: |
          mkdir -p dist
          cp -r app.js src package.json package-lock.json dist/
          echo "Commit: ${{ github.sha }}"      >  dist/PHIEN-BAN.txt
          echo "Nhánh:  ${{ github.ref_name }}" >> dist/PHIEN-BAN.txt
          ls -la dist/

      - name: Lưu sản phẩm để tải về
        uses: actions/upload-artifact@v4
        with:
          name: ci-demo-build
          path: dist/
          retention-days: 7         # tự xoá sau 7 ngày, đỡ chật kho
```

### 🧭 Hướng dẫn làm LAB — step by step

#### Bước 1 — Cài ESLint ở máy và sinh lại lock file

```bash
cd ~/ci-demo
npm install --save-dev eslint
```

**Bạn sẽ thấy:**
```text
added 90 packages, and audited 91 packages in 6s
found 0 vulnerabilities
```

✅ **Checkpoint:** có thư mục `node_modules/` và `package-lock.json` đã được cập nhật.

💡 `--save-dev` ghi ESLint vào mục `devDependencies`. Đây là lý do `npm ci` trên runner sau này biết phải cài ESLint.

#### Bước 2 — Tạo `eslint.config.js` rồi chạy thử ở máy

Tạo file theo nội dung phần LAB, rồi:

```bash
npm run lint
```

**Bạn sẽ thấy:** không có dòng nào in ra (im lặng = sạch, không lỗi).

✅ **Checkpoint:** lệnh kết thúc, không có lỗi. Kiểm tra mã trả về: `echo $?` phải ra `0`.

Giờ thử cho nó bắt lỗi thật — thêm một biến thừa vào cuối `src/tinh-tien.js`:

```bash
echo "const bienThua = 123;" >> src/tinh-tien.js
npm run lint
```

**Bạn sẽ thấy:**
```text
/home/ban/ci-demo/src/tinh-tien.js
  12:7  error  'bienThua' is assigned a value but never used  no-unused-vars

✖ 1 problem (1 error, 0 warnings)
```

✅ **Checkpoint:** ESLint chỉ đúng số dòng và tên luật bị vi phạm.

Xoá dòng thừa đi trước khi đi tiếp:
```bash
sed -i '/const bienThua/d' src/tinh-tien.js
npm run lint      # phải im lặng trở lại
```

⚠️ **Nếu báo `Cannot find module 'eslint'`:** chưa chạy `npm install --save-dev eslint` ở Bước 1.

#### Bước 3 — Đừng quên `.gitignore`

```bash
printf 'node_modules/\ndist/\n' > .gitignore
git status --short
```

**Bạn sẽ thấy:** danh sách file thay đổi **không có** `node_modules/`.

✅ **Checkpoint:** `node_modules` không xuất hiện trong `git status`.

⚠️ **Lỡ commit `node_modules` là một nỗi khổ kinh điển** — repo phình lên hàng trăm MB và mọi lần pull đều chậm. Nếu lỡ rồi: `git rm -r --cached node_modules` rồi commit lại.

#### Bước 4 — Thay `ci.yml` và đẩy lên

Viết lại `.github/workflows/ci.yml` theo nội dung phần LAB, rồi:

```bash
git add .
git commit -m "Nâng cấp CI: lint -> test (matrix) -> build + artifact"
git push
```

Mở tab **Actions** trên GitHub, bấm vào run mới nhất.

**Bạn sẽ thấy sơ đồ các job như thế này:**
```text
Kiểm tra chất lượng code  ✅
        ↓
Test trên Node 18  ✅        Test trên Node 20  ✅     ← hai ô này chạy SONG SONG
        ↓
Đóng gói  ✅
```

✅ **Checkpoint:** đúng 4 ô job, nối bằng mũi tên, tất cả xanh.

⚠️ **Nếu job `lint` đỏ với `npm ci can only install with an existing package-lock.json`:** bạn chưa commit `package-lock.json`. Kiểm tra: `git ls-files | grep lock`. Nếu trống thì `git add package-lock.json` rồi push lại.

💡 Để ý sơ đồ tự vẽ ra mũi tên đúng như `needs:` bạn khai — GitHub hiểu được thứ tự phụ thuộc và hiển thị thành hình.

#### Bước 5 — Tải sản phẩm về máy

Trong trang run vừa chạy, kéo xuống cuối → mục **Artifacts** → có ô `ci-demo-build`.

Bấm tải về, giải nén, mở file `PHIEN-BAN.txt`.

**Bạn sẽ thấy:**
```text
Commit: 3f7a2c9d8e1b4a6c5f0d9e8b7a6c5d4e3f2a1b0c
Nhánh:  main
```

✅ **Checkpoint:** mã commit trong file khớp đúng với commit bạn vừa push.

💡 **Vì sao phải nhúng mã commit vào sản phẩm:** ba tuần nữa, khi production gặp lỗi lạ, câu hỏi đầu tiên luôn là *"bản đang chạy được build từ commit nào?"*. Không nhúng thì không ai trả lời được. Đây là thói quen nhỏ mà cực kỳ giá trị lúc sự cố.

#### Bước 6 — Đo hiệu quả của cache

Push một commit nhỏ (không đổi thư viện):

```bash
echo "# ci-demo" > README.md
git add README.md && git commit -m "Thêm README" && git push
```

Mở run mới, vào job `lint`, mở rộng bước **Cài Node.js**.

**Bạn sẽ thấy:**
```text
Cache restored successfully
Cache restored from key: node-cache-Linux-x64-npm-8f3d2a...
```

Rồi so sánh thời gian bước `npm ci` giữa run đầu tiên và run này.

✅ **Checkpoint:** run sau nhanh hơn rõ rệt (thường từ ~8 giây xuống ~2 giây).

💡 Dự án thật có 500+ thư viện thì khoản tiết kiệm này là **2–3 phút mỗi lần push**. Nhân với 50 lần push/ngày của cả đội — đó là lý do cache không phải chuyện nhỏ.

#### Bước 7 — Kiểm chứng `needs:` thực sự chặn dây chuyền

Cố ý làm lint đỏ:

```bash
echo "const rac = 999;" >> app.js
git commit -am "Thử: cố ý để biến thừa cho lint bắt"
git push
```

**Bạn sẽ thấy trên tab Actions:**
```text
Kiểm tra chất lượng code  ❌
        ↓
Test trên Node 18  ⊘ Skipped      Test trên Node 20  ⊘ Skipped
        ↓
Đóng gói  ⊘ Skipped
```

✅ **Checkpoint:** 3 job sau đều **Skipped** — không hề chạy.

💡 **Đây chính là "kinh tế học của thời gian":** một biến thừa bị chặn sau 15 giây, thay vì để pipeline chạy hết 6 phút rồi mới báo hỏng. Trên pipeline thật có build Docker và deploy, khoản tiết kiệm này rất lớn.

Sửa lại rồi push:
```bash
sed -i '/const rac/d' app.js
git commit -am "Bỏ biến thừa"
git push
```

#### Bước 8 — Khoá `main`: biến CI thành rào bắt buộc

Vào repo → **Settings → Branches → Add branch protection rule** *(giao diện mới: **Settings → Rules → Rulesets → New branch ruleset**)*.

Điền:
- **Branch name pattern:** `main`
- ✅ **Require a pull request before merging**
- ✅ **Require status checks to pass before merging** → ô tìm kiếm, gõ và chọn: `Kiểm tra chất lượng code`, `Test trên Node 18`, `Test trên Node 20`
- ✅ **Require branches to be up to date before merging**

Bấm **Create** / **Save changes**.

✅ **Checkpoint:** trang Branches hiện luật đang áp cho `main`.

⚠️ **Nếu ô tìm status check không thấy tên job:** GitHub chỉ gợi ý những check **đã từng chạy ít nhất một lần**. Push một commit bất kỳ rồi quay lại.

#### Bước 9 — Thử phá luật để thấy nó chặn thật

```bash
git checkout -b thu-pha-luat
echo "const lai_rac = 1;" >> app.js
git commit -am "Thử: PR có lỗi lint"
git push -u origin thu-pha-luat
```

Vào GitHub → bấm **Compare & pull request** → **Create pull request**.

**Bạn sẽ thấy trong trang PR:**
```text
❌ Some checks were not successful
   ❌ Kiểm tra chất lượng code — Failing after 18s
   ⊘  Test trên Node 18 — Skipped

🔒 Merging is blocked
   Required statuses must pass before merging
```

Và **nút Merge bị làm mờ, không bấm được**.

✅ **Checkpoint:** nút Merge thực sự bị khoá.

💡 **Đây là khoảnh khắc CI đổi vai:** từ chỗ *"một cái đèn để nhìn"* thành *"một cánh cửa có khoá"*. Chất lượng không còn phụ thuộc vào việc có ai nhớ nhìn CI hay không.

Dọn dẹp:
```bash
git checkout main
git branch -D thu-pha-luat
git push origin --delete thu-pha-luat
```

### 💡 Đi làm mới thấm (sách cơ bản hay bỏ quên)

- **`fail-fast: false` — chi tiết nhỏ, khác biệt lớn.** Mặc định matrix là `fail-fast: true`: Node 18 hỏng thì GitHub **huỷ luôn** bản Node 20 đang chạy. Kết quả: bạn chỉ biết "18 hỏng", không biết 20 có hỏng không → sửa xong lại phải chờ một vòng nữa. Đặt `false` để nhìn toàn cảnh ngay lần đầu.
- **Cache có thể "ôi thiu".** Cache đánh khoá theo `package-lock.json`. Nếu pipeline hành xử lạ lùng mà code không sai, hãy nghi cache: xoá ở **Actions → Caches**, chạy lại. Đây là một trong những lỗi tốn thời gian nhất vì nó không giống lỗi tí nào.
- **Đừng đưa bước deploy vào cùng workflow với CI khi chưa cần.** CI chạy trên *mọi* PR, kể cả PR của người lạ. Deploy phải có trigger riêng, hẹp hơn (chỉ `main`, hoặc chỉ khi gắn tag) — Ngày 34 sẽ làm đúng cách.
- **`timeout-minutes` cứu bạn khỏi hoá đơn bất ngờ.** Một test treo có thể chạy đến tận 6 tiếng (giới hạn mặc định của GitHub) rồi mới bị giết. Thêm `timeout-minutes: 10` vào mỗi job là thói quen tốt.
- **Lint và test đo hai thứ khác nhau — đừng gộp.** Lint bảo *"code viết có sạch không"*, test bảo *"code chạy có đúng không"*. Code lint sạch tuyệt đối vẫn có thể tính sai tiền. Nhiều người mới tưởng lint xanh là yên tâm.
- **Test coverage là con dao hai lưỡi.** Ép "phải đạt 80% coverage" thường đẻ ra một đống test rỗng chỉ để chạy qua code chứ không kiểm tra gì. Coverage thấp là tín hiệu đáng xem xét; coverage cao **không** chứng minh chất lượng.

### 📝 Tự kiểm tra

> Nghĩ câu trả lời **thành lời** trước khi mở đáp án — nghĩ thầm luôn thấy mình hiểu.

<details>
<summary><b>1. Vì sao xếp lint trước test, test trước build? Nêu con số minh hoạ.</b></summary>

Đây là bài toán **tiết kiệm thời gian chờ**:

| Lớp | Bắt lỗi gì | Mất bao lâu |
|---|---|---|
| Lint | Biến thừa, gọi tên sai | ~10 giây |
| Test | Lỗi logic | ~1–5 phút |
| Build | Lỗi ghép nối | ~1–10 phút |

Một lỗi gõ nhầm tên biến bị lint chặn trong 10 giây thì không đáng để chạy hết bộ test 5 phút rồi mới phát hiện. Nhân với số lần push mỗi ngày của cả đội — đó là con số thật.

</details>

<details>
<summary><b>2. `npm ci` khác `npm install` ở điểm nào? Vì sao CI phải dùng `npm ci`?</b></summary>

`npm install` đọc `package.json` (khoảng phiên bản) và **có thể âm thầm nâng phiên bản**, sửa cả lock file. `npm ci` đọc `package-lock.json` (phiên bản chính xác), **không bao giờ sửa lock**, và xoá sạch `node_modules` trước khi cài.

CI cần **tính tái lập** — chạy hôm nay và chạy tháng sau phải cho kết quả giống hệt. `npm ci` đảm bảo điều đó, và còn nhanh hơn.

</details>

<details>
<summary><b>3. CI xanh nhưng vẫn có code hỏng vào `main`. Vì sao, và sửa thế nào?</b></summary>

Vì **CI không có branch protection chỉ là một cái đèn để nhìn, không phải cánh cửa có khoá**. Bạn *thấy* code đỏ nhưng vẫn bấm merge được.

Sửa: bật branch protection cho `main` với *Require status checks to pass before merging*. Khi đó nút Merge bị khoá cứng tới khi CI xanh — không ai phá lệ được, kể cả bạn.

Đây là bước biến CI từ **trang trí** thành **rào chắn**.

</details>

### 📚 Thuật ngữ Anh–Việt (ngày này)

| Thuật ngữ | Nghĩa |
|---|---|
| **`needs:`** | Khai báo job này chờ job kia xong mới chạy; job trước đỏ thì job sau bị skip |
| **Matrix** | Chạy cùng một job trên nhiều phiên bản/OS song song |
| **`fail-fast: false`** | Một bản matrix hỏng vẫn chạy nốt các bản còn lại để thấy toàn cảnh |
| **Cache** | Lưu lại thư viện đã tải để lần sau không tải lại — tiết kiệm phút runner |
| **`npm ci`** | Cài đúng theo lock file, không sửa lock — bắt buộc dùng trong CI |
| **Branch protection** | Luật chặn merge vào nhánh chính khi CI chưa xanh |
| **`concurrency`** | Huỷ các lần chạy cũ khi push liên tiếp, chỉ giữ lần mới nhất |
| **Test coverage** | Tỉ lệ code được test chạy qua; cao **không** chứng minh chất lượng |

### 🎯 Đúc kết Ngày 32

**3 điều phải mang theo:**

1. **Xếp lớp rẻ-nhanh lên trước** (lint → test → build) và nối bằng `needs:`. Lỗi bị chặn càng sớm càng đỡ tốn thời gian chờ của cả đội.
2. **Runner sạch nên mỗi job phải tự lo lấy đồ:** `checkout` → `setup-node` (kèm `cache`) → `npm ci`. Muốn chuyển sản phẩm sang job khác hay tải về máy thì dùng **artifact**.
3. **CI không có branch protection chỉ là trang trí.** Bật rào bắt buộc thì code đỏ không thể merge, kể cả bạn cũng không phá lệ được.

> 🧠 **Một câu để nhớ:** CI cho bạn *nhìn thấy* code hỏng; **branch protection** mới là thứ *ngăn* code hỏng vào `main`.

**✅ Tự chấm** *(đánh dấu khi làm được mà không nhìn tài liệu):*

- [ ] Giải thích vì sao lint phải đứng trước test, test đứng trước build
- [ ] Viết được `needs:` và chứng minh job sau bị Skipped khi job trước đỏ
- [ ] Dùng matrix test 2 phiên bản Node và nói rõ tác dụng của `fail-fast: false`
- [ ] Bật cache và chỉ ra được dòng `Cache restored` trong log
- [ ] Tạo artifact, tải về, và nói vì sao phải nhúng mã commit vào sản phẩm
- [ ] Phân biệt `npm ci` với `npm install` và biết vì sao CI phải dùng `npm ci`
- [ ] Bật branch protection và tự kiểm chứng nút Merge bị khoá

✅ **Kết quả đạt được:** Một pipeline CI đúng chuẩn đi làm — nhiều tầng, chạy song song hợp lý, có cache, có sản phẩm tải về, và chặn được code hỏng vào nhánh chính.

---

## Ngày 33 — CD Pipeline: Build & Push Docker Image

> ⏱️ ~90 phút · Loại: CI/CD
>
> 🧭 **Bạn đang ở đâu:** Ngày 32 (CI kiểm tra code) → **Ngày 33 (đóng gói thành Docker image và đẩy lên kho)** → Ngày 34 (kéo image đó về server để chạy). Đây là chữ **CD** đầu tiên: từ "code đúng" sang "**có bản chạy được, đánh số rõ ràng, ai cũng kéo về được**".
>
> ✅ **Chuẩn bị:** repo `ci-demo` với CI đang ✅ xanh (Ngày 32); Docker trên máy (Ngày 16–18). Kiểm tra: `docker --version`.
>
> 🎁 **Cuối ngày bạn có gì:** mỗi lần push lên `main`, GitHub tự build Docker image và đẩy lên kho GHCR với tag theo mã commit — bạn kéo về máy chạy được ngay bằng một lệnh.

### 📘 Lý thuyết

#### 1. Vì sao artifact `.zip` của Ngày 32 chưa đủ

Hôm qua bạn đã có sản phẩm tải về được. Nhưng đem cái `.zip` đó lên server thì vẫn phải: cài đúng phiên bản Node, cài thư viện, đặt biến môi trường, viết systemd service... — tức là **vẫn phụ thuộc vào việc server được chuẩn bị đúng cách**.

Docker image giải quyết triệt để: nó gói **cả hệ điều hành nền, runtime, thư viện và code** vào một khối duy nhất. Server chỉ cần biết chạy Docker, không cần biết bên trong là Node hay Python.

| | Artifact `.zip` (Ngày 32) | Docker image (hôm nay) |
|---|---|---|
| Chứa gì | Chỉ code của bạn | Code + Node + thư viện + OS nền |
| Server cần gì | Đúng phiên bản Node, đúng thư viện | Chỉ cần Docker |
| Chạy thế nào | Nhiều bước chuẩn bị | `docker run` một lệnh |
| Chạy chỗ khác | Hay lệch môi trường | Giống hệt nhau ở mọi nơi |

#### 2. Registry — kho chứa image

Build xong image nằm ở máy runner, mà runner thì **bị xoá sau vài phút**. Phải đẩy image lên một cái kho để nó sống tiếp — đó là **registry**.

| Registry | Địa chỉ | Ghi chú |
|---|---|---|
| **GHCR** (GitHub Container Registry) | `ghcr.io` | Nằm ngay trong GitHub, **không cần tạo tài khoản mới** ← dùng hôm nay |
| Docker Hub | `docker.io` | Phổ biến nhất, bản free có giới hạn lượt kéo |
| AWS ECR / Google Artifact Registry | theo cloud | Dùng khi hạ tầng đã ở cloud đó |

Chọn GHCR vì bạn đăng nhập bằng **token có sẵn của workflow** (`GITHUB_TOKEN`) — không phải tạo và cất thêm mật khẩu nào.

#### 3. Tag image — chỗ 90% người mới làm sai

Cám dỗ lớn nhất là tag mọi thứ là `latest`. Nhưng `latest` chỉ là **một cái nhãn dán di động**, không phải một phiên bản:

- Production đang chạy `latest`. Hỏi *"đang chạy code nào?"* → **không ai biết**.
- Cần quay về bản hôm qua → **không có gì để quay về**, vì `latest` đã bị ghi đè.

Cách làm đúng: **mỗi lần build gắn một tag bất biến theo mã commit**, rồi *thêm* `latest` như một bí danh tiện tay:

```text
ghcr.io/ban/ci-demo:3f7a2c9     ← tag bất biến, không bao giờ ghi đè  ✅ dùng để deploy
ghcr.io/ban/ci-demo:latest      ← bí danh trỏ tới bản mới nhất        ⚠️ chỉ để thử nhanh
```

Deploy **luôn dùng tag bất biến**. Khi đó "quay về bản trước" chỉ là đổi một chuỗi ký tự.

#### 4. Multi-stage build — nhắc lại từ Ngày 18, giờ dùng thật

Image cồng kềnh thì chậm đẩy, chậm kéo, và chứa nhiều thứ thừa để kẻ xấu khai thác. **Multi-stage**: tầng đầu dùng image to để cài/biên dịch, tầng cuối chỉ chép sang phần cần thiết.

#### 5. `GITHUB_TOKEN` và `permissions`

Mỗi lần workflow chạy, GitHub tự cấp một token tạm sống đúng trong lần chạy đó. Mặc định nó **chỉ được đọc**. Muốn đẩy image lên GHCR phải xin thêm quyền:

```yaml
permissions:
  contents: read
  packages: write      # ← không có dòng này thì push bị từ chối 403
```

Nguyên tắc **đặc quyền tối thiểu**: xin đúng thứ cần, không xin thừa.

### 🧪 LAB — Tự động build & đẩy image lên GHCR

**Những file sẽ thêm:**

```text
ci-demo/
├── Dockerfile                       # THÊM
├── .dockerignore                    # THÊM
└── .github/workflows/
    ├── ci.yml                       # giữ nguyên từ Ngày 32
    └── cd-image.yml                 # THÊM — workflow đóng gói
```

#### File 1 — `Dockerfile`

```dockerfile
# ---------- Tầng 1: cài thư viện ----------
FROM node:20-alpine AS deps
WORKDIR /app
COPY package.json package-lock.json ./
RUN npm ci --omit=dev          # --omit=dev: BỎ eslint và mọi devDependencies

# ---------- Tầng 2: image cuối, chỉ giữ thứ cần để chạy ----------
FROM node:20-alpine
WORKDIR /app

ENV NODE_ENV=production

# Tạo user thường — KHÔNG chạy app bằng root
RUN addgroup -S nhom && adduser -S ungdung -G nhom

COPY --from=deps /app/node_modules ./node_modules
COPY app.js package.json ./
COPY src ./src

USER ungdung                   # từ đây trở đi container chạy bằng user thường

EXPOSE 3000

# Docker tự kiểm tra sức khoẻ app, không cần chờ người phát hiện
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
  CMD wget -qO- http://127.0.0.1:3000/health || exit 1

CMD ["node", "app.js"]
```

#### File 2 — `.dockerignore`

```text
node_modules
.git
.github
test
dist
*.md
.gitignore
eslint.config.js
```

> 📌 **Vì sao cần file này:** không có nó, Docker gửi *toàn bộ* thư mục (kể cả `node_modules` hàng chục MB và cả lịch sử `.git`) sang trình build → build chậm và image có thể lẫn thứ không nên có.

#### File 3 — `.github/workflows/cd-image.yml`

```yaml
name: CD - Đóng gói image

on:
  push:
    branches: [main]          # CHỈ main — không đóng gói cho mọi nhánh nháp
  workflow_dispatch:          # cho phép bấm tay chạy lại từ giao diện

permissions:
  contents: read
  packages: write             # BẮT BUỘC để đẩy image lên GHCR

jobs:
  build-push:
    name: Build & đẩy image
    runs-on: ubuntu-latest
    timeout-minutes: 15

    steps:
      - uses: actions/checkout@v4

      # Tên image trên GHCR BẮT BUỘC viết thường; username có chữ hoa sẽ lỗi
      - name: Chuẩn bị tên image (viết thường)
        run: echo "IMAGE=ghcr.io/$(echo '${{ github.repository }}' | tr '[:upper:]' '[:lower:]')" >> $GITHUB_ENV

      - name: Đăng nhập GHCR
        uses: docker/login-action@v3
        with:
          registry: ghcr.io
          username: ${{ github.actor }}
          password: ${{ secrets.GITHUB_TOKEN }}     # token tự cấp, không cần tự tạo

      - name: Bật Buildx (trình build có cache)
        uses: docker/setup-buildx-action@v3

      - name: Build và đẩy image
        uses: docker/build-push-action@v6
        with:
          context: .
          push: true
          tags: |
            ${{ env.IMAGE }}:${{ github.sha }}
            ${{ env.IMAGE }}:latest
          cache-from: type=gha          # dùng lại cache lớp Docker của lần build trước
          cache-to: type=gha,mode=max

      - name: In ra lệnh để kéo image về
        run: |
          echo "### Image đã sẵn sàng 🎉" >> $GITHUB_STEP_SUMMARY
          echo '```bash' >> $GITHUB_STEP_SUMMARY
          echo "docker pull ${{ env.IMAGE }}:${{ github.sha }}" >> $GITHUB_STEP_SUMMARY
          echo '```' >> $GITHUB_STEP_SUMMARY
```

### 🧭 Hướng dẫn làm LAB — step by step

#### Bước 1 — Build và chạy thử ở máy trước

Luôn kiểm chứng Dockerfile tại chỗ — đừng để CI là nơi thử lần đầu.

```bash
cd ~/ci-demo
docker build -t ci-demo:thu .
```

**Bạn sẽ thấy:**
```text
[+] Building 12.4s (15/15) FINISHED
 => [deps 3/4] COPY package.json package-lock.json ./
 => [deps 4/4] RUN npm ci --omit=dev
 => exporting to image
 => => naming to docker.io/library/ci-demo:thu
```

✅ **Checkpoint:** dòng cuối `FINISHED`, không có `ERROR`.

⚠️ **Nếu lỗi `npm ci ... lock file not found`:** chưa commit/chưa có `package-lock.json`, hoặc bị `.dockerignore` loại nhầm. Kiểm tra: `ls package-lock.json`.

#### Bước 2 — Chạy container và gọi thử

```bash
docker run -d --name thu -p 3000:3000 ci-demo:thu
sleep 2
curl -s localhost:3000/health
echo
curl -s localhost:3000
```

**Bạn sẽ thấy:**
```text
{"trangThai":"ok"}
{"thongDiep":"ci-demo đang chạy","donHangMau":36000}
```

✅ **Checkpoint:** cả 2 lệnh `curl` trả về JSON.

Kiểm tra luôn hai điều best-practice vừa đưa vào Dockerfile:

```bash
docker exec thu whoami            # phải ra: ungdung  (KHÔNG phải root)
docker ps --format '{{.Names}}\t{{.Status}}'
```

**Bạn sẽ thấy:**
```text
ungdung
thu     Up 40 seconds (healthy)
```

✅ **Checkpoint:** user là `ungdung`, và trạng thái có chữ **(healthy)** — đó là `HEALTHCHECK` đang hoạt động.

💡 *Vì sao không chạy bằng root:* nếu app bị khai thác, kẻ tấn công chỉ có quyền của `ungdung` bên trong container, thay vì quyền root. Đây là một trong những mục bị soi đầu tiên khi kiểm tra bảo mật.

Dọn dẹp:
```bash
docker rm -f thu
```

#### Bước 3 — Xem kích thước image (và vì sao multi-stage đáng giá)

```bash
docker images ci-demo:thu --format '{{.Size}}'
docker images node:20 --format '{{.Size}}' 2>/dev/null || echo "(chưa tải node:20 đầy đủ)"
```

**Bạn sẽ thấy:** khoảng `~140MB` cho image của bạn, so với `~1.1GB` của `node:20` đầy đủ.

✅ **Checkpoint:** image dưới 200MB.

💡 Nhỏ hơn không chỉ để đẹp: đẩy nhanh hơn, kéo nhanh hơn, **và ít phần mềm thừa nghĩa là ít lỗ hổng hơn** (Ngày 49 sẽ quét bảo mật chính image này).

#### Bước 4 — Đẩy code lên và xem GitHub tự build

```bash
git add Dockerfile .dockerignore .github/workflows/cd-image.yml
git commit -m "Thêm Dockerfile + workflow tự đẩy image lên GHCR"
git push
```

Mở tab **Actions** → sẽ thấy **hai** workflow cùng chạy: `CI` (của Ngày 32) và `CD - Đóng gói image`.

Bấm vào `CD - Đóng gói image` → job `Build & đẩy image`.

**Bạn sẽ thấy ở bước cuối:**
```text
#15 pushing manifest for ghcr.io/ban/ci-demo:3f7a2c9...
#15 DONE 1.2s
```

✅ **Checkpoint:** workflow ✅ xanh, và ở trang tóm tắt (Summary) có sẵn lệnh `docker pull ...` để copy.

⚠️ **Nếu lỗi `denied: permission_denied: write_package`:** thiếu `permissions: packages: write` trong workflow. Kiểm tra lại đúng phần khai báo.

⚠️ **Nếu lỗi `invalid reference format: repository name must be lowercase`:** username GitHub của bạn có chữ hoa. Bước "Chuẩn bị tên image" đã xử lý việc này — kiểm tra xem bạn có chép thiếu bước đó không.

#### Bước 5 — Tìm image vừa đẩy lên

Vào trang chính của repo → cột bên phải, mục **Packages** → bấm `ci-demo`.

**Bạn sẽ thấy:** trang package liệt kê các tag, trong đó có tag bằng đúng mã commit và tag `latest`.

✅ **Checkpoint:** ít nhất 2 tag, và cột *Published* vừa mới đây.

💡 Mặc định package này là **Private**, kế thừa từ repo. Muốn người khác kéo được thì vào **Package settings → Change visibility → Public**.

#### Bước 6 — Kéo image từ kho về và chạy (đây là lúc thấy CD có nghĩa)

Đăng nhập GHCR ở máy. Cần một **Personal Access Token (classic)** có quyền `read:packages`: GitHub → **Settings → Developer settings → Personal access tokens → Tokens (classic) → Generate new token** → tick `read:packages`.

```bash
echo "<dan-token-vao-day>" | docker login ghcr.io -u <ten-github-cua-ban> --password-stdin
```

**Bạn sẽ thấy:** `Login Succeeded`.

Giờ kéo đúng bản vừa build (thay `<sha>` bằng mã commit trong log workflow):

```bash
docker pull ghcr.io/<ten-cua-ban>/ci-demo:<sha>
docker run -d --name tu-kho -p 3001:3000 ghcr.io/<ten-cua-ban>/ci-demo:<sha>
curl -s localhost:3001/health
```

**Bạn sẽ thấy:**
```text
{"trangThai":"ok"}
```

✅ **Checkpoint:** app chạy từ image **kéo trên Internet về**, không phải image bạn build ở máy.

💡 **Dừng lại một chút và nhận ra điều vừa xảy ra:** bạn push code → máy của GitHub tự đóng gói → đẩy lên kho → máy khác kéo về chạy được ngay. **Không ai chạm tay vào server nào cả.** Đó chính là CD. Ngày mai chỉ còn việc nối bước cuối: tự động kéo về server thật.

Dọn dẹp:
```bash
docker rm -f tu-kho
```

#### Bước 7 — Kiểm chứng vì sao `latest` không đáng tin

Sửa một dòng cho khác đi rồi push:

```bash
sed -i "s/ci-demo đang chạy/ci-demo bản thứ hai/" app.js
git commit -am "Đổi thông điệp để thấy khác biệt giữa hai bản"
git push
```

Chờ workflow xanh, rồi ở máy:

```bash
docker pull ghcr.io/<ten-cua-ban>/ci-demo:latest
docker run --rm -p 3002:3000 -d --name thu-latest ghcr.io/<ten-cua-ban>/ci-demo:latest
curl -s localhost:3002
docker rm -f thu-latest
```

**Bạn sẽ thấy:** `"thongDiep":"ci-demo bản thứ hai"` — `latest` **đã âm thầm trỏ sang bản mới**, dù bạn không đổi gì trong lệnh chạy.

Trong khi đó, chạy lại bằng tag commit **cũ** vẫn ra đúng nội dung cũ:

```bash
docker run --rm -p 3003:3000 -d --name thu-cu ghcr.io/<ten-cua-ban>/ci-demo:<sha-cu>
curl -s localhost:3003          # vẫn là "ci-demo đang chạy"
docker rm -f thu-cu
```

✅ **Checkpoint:** thấy rõ `latest` đổi nội dung sau lưng bạn, còn tag theo commit thì bất biến.

💡 **Bài học đắt giá nhất hôm nay:** production mà chạy `latest` thì bạn **không biết đang chạy gì** và **không có gì để quay về**. Deploy luôn dùng tag bất biến.

### 💡 Đi làm mới thấm (sách cơ bản hay bỏ quên)

- **Image tag bất biến là điều kiện tiên quyết để rollback.** "Quay về bản trước" chỉ đơn giản khi bản trước còn tồn tại dưới một cái tên không đổi. Đây là lý do mọi nơi làm nghiêm túc đều deploy theo SHA hoặc theo version tag, không bao giờ theo `latest`.
- **Build cache của Docker phụ thuộc vào thứ tự dòng.** `COPY package*.json` rồi `RUN npm ci` **trước** `COPY . .` — nhờ vậy sửa code không làm mất cache lớp cài thư viện. Đảo thứ tự là mỗi lần build đều cài lại từ đầu.
- **`cache-from: type=gha` tiết kiệm rất nhiều thời gian.** Không có nó, mỗi lần build trên runner sạch đều làm lại từ số 0. Có nó, các lớp không đổi được lấy lại ngay.
- **Đừng nhét secret vào image.** Mọi `ENV` và mọi file `COPY` vào đều nằm trong lịch sử các lớp — ai kéo image về cũng đọc được bằng `docker history`. Secret phải được đưa vào **lúc chạy** (biến môi trường, file mount), không phải lúc build.
- **Kho image phình rất nhanh.** Mỗi commit một image, vài tháng là hàng nghìn tag chiếm hàng chục GB. Đặt chính sách dọn dẹp (giữ N bản gần nhất) — nếu không, một ngày đẹp trời bạn sẽ nhận hoá đơn hoặc cảnh báo hết dung lượng.
- **Multi-arch khi đội dùng máy Apple Silicon.** Image build trên runner là `amd64`; máy M1/M2/M3 là `arm64` → chạy qua giả lập, chậm hoặc lỗi lạ. Khi cần, thêm `platforms: linux/amd64,linux/arm64` vào `build-push-action`.

### 📝 Tự kiểm tra

> Nghĩ câu trả lời **thành lời** trước khi mở đáp án — nghĩ thầm luôn thấy mình hiểu.

<details>
<summary><b>1. Deploy bằng tag `latest` gây ra ba vấn đề gì?</b></summary>

1. **Không biết đang chạy gì** — hỏi *'production đang chạy code nào?'* thì không ai trả lời được
2. **Không quay lui được** — `latest` đã bị ghi đè, bản cũ không còn tên để gọi
3. **Không tái lập được** — hai máy kéo `latest` ở hai thời điểm sẽ chạy hai bản khác nhau

Cách đúng: tag theo **SHA commit** (bất biến, truy ngược ra code được). Có thể thêm `latest` làm bí danh tiện tay, nhưng deploy luôn dùng tag SHA.

</details>

<details>
<summary><b>2. Vì sao `COPY package*.json` phải đứng TRƯỚC `COPY . .` trong Dockerfile?</b></summary>

Vì **cache lớp Docker phụ thuộc vào thứ tự dòng**. Docker cache từng lớp; một lớp đổi thì mọi lớp sau đều phải làm lại.

Copy `package*.json` rồi `npm ci` trước, sau đó mới `COPY . .`: sửa code không làm đổi `package.json` → lớp cài thư viện được lấy từ cache → build nhanh.

Đảo thứ tự lại: mỗi lần sửa một dòng code là cài lại toàn bộ thư viện từ đầu.

</details>

<details>
<summary><b>3. Vì sao không được đưa secret vào image bằng `ENV` hoặc `COPY`?</b></summary>

Vì mọi `ENV` và mọi file `COPY` vào đều nằm trong **lịch sử các lớp** của image. Bất kỳ ai kéo image về đều đọc được bằng `docker history` hoặc giải nén các lớp — kể cả khi lớp sau đã xoá file đi.

Secret phải được đưa vào **lúc chạy**: biến môi trường khi `docker run`, file mount, hoặc hệ quản lý bí mật.

</details>

### 📚 Thuật ngữ Anh–Việt (ngày này)

| Thuật ngữ | Nghĩa |
|---|---|
| **Registry** | Kho chứa image (GHCR, Docker Hub, ECR); nơi image sống sau khi runner bị xoá |
| **GHCR** | GitHub Container Registry — đăng nhập bằng `GITHUB_TOKEN` có sẵn |
| **Tag bất biến** | Tag không bao giờ bị ghi đè (thường là SHA commit) — điều kiện để rollback |
| **`latest`** | Nhãn dán di động trỏ tới bản mới nhất — **không dùng để deploy** |
| **Multi-stage build** | Tầng đầu cài/biên dịch, tầng cuối chỉ chép phần cần chạy → image nhỏ |
| **`.dockerignore`** | Danh sách file không gửi vào trình build — build nhanh hơn, image sạch hơn |
| **HEALTHCHECK** | Lệnh Docker tự chạy để biết container còn khoẻ không |
| **SBOM** | Danh mục thành phần phần mềm — trả lời 'ta có dùng thư viện dính CVE không?' |

### 🎯 Đúc kết Ngày 33

**3 điều phải mang theo:**

1. **Image = code + runtime + thư viện + OS nền trong một khối.** Server chỉ cần biết chạy Docker, hết phụ thuộc vào việc ai đã cài gì trên máy đó.
2. **Tag bất biến theo commit là thứ cho phép bạn rollback.** `latest` chỉ là nhãn dán di động — tiện để thử, không dùng để deploy.
3. **GHCR + `GITHUB_TOKEN` + `permissions: packages: write`** là bộ ba tối thiểu để pipeline tự đẩy image, không phải tự quản lý thêm mật khẩu nào.

> 🧠 **Một câu để nhớ:** deploy bằng `latest` nghĩa là **không biết đang chạy gì, và không có đường lui**.

**✅ Tự chấm** *(đánh dấu khi làm được mà không nhìn tài liệu):*

- [ ] Viết Dockerfile multi-stage có user thường và `HEALTHCHECK`
- [ ] Giải thích vì sao cần `.dockerignore` và điều gì xảy ra nếu thiếu
- [ ] Đăng nhập GHCR trong workflow bằng `GITHUB_TOKEN` và khai đúng `permissions`
- [ ] Gắn 2 tag (SHA + latest) và nói rõ tag nào dùng để deploy
- [ ] Kéo image từ GHCR về máy khác và chạy được
- [ ] Chứng minh `latest` đổi nội dung sau lưng, còn tag SHA thì không

✅ **Kết quả đạt được:** Mỗi lần push lên `main`, hệ thống tự đóng gói ứng dụng thành Docker image có đánh số rõ ràng và đưa lên kho — sẵn sàng cho bất kỳ server nào kéo về chạy.

---

## Ngày 34 — CD Pipeline: Tự động Deploy lên Server

> ⏱️ ~90 phút · Loại: CI/CD
>
> 🧭 **Bạn đang ở đâu:** Ngày 33 (image đã nằm trong kho) → **Ngày 34 (tự động đưa image đó lên server và chạy)** → Ngày 35 (Milestone: ghép cả dây chuyền). Hôm nay là mắt xích cuối: từ `git push` tới "bản mới đang phục vụ người dùng", không ai chạm tay vào server.
>
> ✅ **Chuẩn bị:** repo `ci-demo` với workflow đóng gói image đang ✅ xanh (Ngày 33); máy Linux có Docker + Docker Compose.
>
> 🎁 **Cuối ngày bạn có gì:** push code lên `main` → khoảng 2 phút sau, bản mới **tự chạy** trên "server" của bạn, kèm kiểm tra sức khoẻ tự động và **nút rollback bấm một cái là về bản cũ**.
>
> 💻 **Về chuyện "server":** bài này dùng **chính máy Linux của bạn** làm server, thông qua **self-hosted runner** — miễn phí, không cần thuê cloud, không cần IP public. Cuối bài có phương án SSH tới VM thật khi bạn đã có server.

### 📘 Lý thuyết

#### 1. Hai mô hình deploy — chọn đúng ngay từ đầu

| | **Push** (CI đẩy vào server) | **Pull** (agent trong server tự kéo) |
|---|---|---|
| Cách chạy | CI giữ khoá SSH / kubeconfig, chủ động vào server ra lệnh | Một tiến trình nằm sẵn trong server, tự hỏi "có bản mới không?" rồi tự cập nhật |
| Khoá bí mật | **CI phải giữ chìa khoá vào server** | Server không cần mở cửa cho ai |
| Server cần | Mở cổng SSH cho runner ngoài Internet | Không cần mở cổng vào |
| Học ở | **Hôm nay** | Ngày 43 (GitOps/ArgoCD) |

Hôm nay học mô hình **push** vì nó trực quan và vẫn cực kỳ phổ biến. Nhưng hãy nhớ nhược điểm cốt lõi: **CI phải giữ chìa khoá vào server production** — chìa khoá càng nhiều nơi giữ thì càng dễ lộ. Ngày 43 sẽ cho thấy cách lật ngược chiều để không ai phải giữ chìa khoá.

#### 2. Self-hosted runner — cách để máy bạn trở thành "server"

Đến giờ mọi job đều chạy trên máy ảo GitHub cấp. GitHub cũng cho phép **bạn tự cắm máy của mình vào**: cài một agent nhỏ, nó kết nối *ra ngoài* tới GitHub và hỏi "có việc gì cho tôi không?".

```text
Máy của bạn  ──(kết nối đi ra)──>  GitHub
             <──(giao việc)───────
```

Điểm hay: **không cần IP public, không cần mở cổng firewall nào** — vì chính máy bạn là bên chủ động gọi ra. Job nào khai `runs-on: self-hosted` sẽ chạy ngay trên máy đó, tức là chạy *trên server*.

> ⚠️ **Cảnh báo bảo mật quan trọng:** **tuyệt đối không** gắn self-hosted runner vào repo **public**. Người lạ mở một Pull Request là code của họ chạy thẳng trên máy bạn. Đây là lý do Ngày 31 bắt bạn tạo repo **Private**.

#### 3. Deploy đúng cách nghĩa là gì

Một lần deploy tử tế phải trả lời được 4 câu:

| Câu hỏi | Cách làm hôm nay |
|---|---|
| Đang chạy **bản nào**? | Deploy theo **tag SHA**, ghi lại vào file trên server |
| Bản mới **có sống không**? | Gọi `/health` sau khi khởi động, thất bại thì báo đỏ |
| Có **quay lui** được không? | Giữ lại SHA bản trước → đổi tag, chạy lại |
| **Ai** deploy, **lúc nào**? | Log workflow lưu vĩnh viễn trong GitHub |

Thiếu bất kỳ câu nào thì đó là "chép file lên server", không phải deploy.

#### 4. Environment — cổng có người gác

GitHub có khái niệm **Environment** (`production`, `staging`). Gắn job deploy vào một environment sẽ cho bạn:

- **Yêu cầu người duyệt**: job dừng lại chờ ai đó bấm *Approve* mới chạy tiếp.
- **Secret riêng theo môi trường**: khoá của staging khác khoá của production.
- **Lịch sử deploy**: GitHub hiện rõ bản nào đang chạy ở đâu.

Đây là thứ ngăn một cú `git push` lúc 11 giờ đêm đi thẳng ra production.

### 🧪 LAB — Tự động deploy lên server của chính bạn

**Những file sẽ thêm:**

```text
ci-demo/
├── deploy/
│   └── docker-compose.prod.yml      # THÊM — mô tả cách chạy trên "server"
└── .github/workflows/
    └── deploy.yml                   # THÊM — workflow deploy
```

#### File 1 — `deploy/docker-compose.prod.yml`

```yaml
services:
  app:
    # Tag image được truyền vào lúc deploy qua biến môi trường IMAGE_TAG
    image: ${IMAGE_NAME}:${IMAGE_TAG}
    container_name: ci-demo-prod
    restart: unless-stopped
    ports:
      - "8080:3000"          # máy: 8080  ->  container: 3000
    environment:
      NODE_ENV: production
    healthcheck:
      test: ["CMD", "wget", "-qO-", "http://127.0.0.1:3000/health"]
      interval: 10s
      timeout: 3s
      retries: 3
      start_period: 5s
    logging:
      driver: json-file
      options:
        max-size: "10m"      # chặn log phình vô hạn làm đầy ổ đĩa
        max-file: "3"
```

#### File 2 — `.github/workflows/deploy.yml`

```yaml
name: Deploy lên server

on:
  # Chỉ chạy SAU KHI workflow đóng gói image đã xong và thành công
  workflow_run:
    workflows: ["CD - Đóng gói image"]
    types: [completed]
    branches: [main]
  # Cho phép bấm tay, và nhập SHA cũ để ROLLBACK
  workflow_dispatch:
    inputs:
      image_tag:
        description: 'Tag image cần deploy (để trống = bản mới nhất trên main)'
        required: false
        type: string

permissions:
  contents: read
  packages: read

jobs:
  deploy:
    name: Deploy
    runs-on: self-hosted            # ← chạy trên MÁY CỦA BẠN, không phải máy GitHub
    timeout-minutes: 10
    environment: production         # ← gắn cổng có người gác

    # Nếu được kích bởi workflow_run thì chỉ chạy khi workflow kia THÀNH CÔNG
    if: ${{ github.event_name == 'workflow_dispatch' || github.event.workflow_run.conclusion == 'success' }}

    steps:
      - uses: actions/checkout@v4

      - name: Xác định image cần deploy
        run: |
          IMAGE_NAME="ghcr.io/$(echo '${{ github.repository }}' | tr '[:upper:]' '[:lower:]')"
          # Ưu tiên tag người dùng nhập tay (dùng khi rollback); không có thì lấy commit hiện tại
          TAG="${{ inputs.image_tag }}"
          if [ -z "$TAG" ]; then
            TAG="${{ github.event.workflow_run.head_sha || github.sha }}"
          fi
          echo "IMAGE_NAME=$IMAGE_NAME" >> $GITHUB_ENV
          echo "IMAGE_TAG=$TAG"         >> $GITHUB_ENV
          echo "Sắp deploy: $IMAGE_NAME:$TAG"

      - name: Đăng nhập GHCR
        run: echo "${{ secrets.GITHUB_TOKEN }}" | docker login ghcr.io -u ${{ github.actor }} --password-stdin

      - name: Ghi lại bản ĐANG chạy (để còn đường lui)
        run: |
          mkdir -p ~/trien-khai
          if [ -f ~/trien-khai/tag-hien-tai.txt ]; then
            cp ~/trien-khai/tag-hien-tai.txt ~/trien-khai/tag-truoc-do.txt
          fi

      - name: Kéo image mới
        run: docker pull "$IMAGE_NAME:$IMAGE_TAG"

      - name: Khởi động bản mới
        working-directory: deploy
        run: docker compose -f docker-compose.prod.yml up -d

      - name: Kiểm tra sức khoẻ (thử 10 lần, mỗi lần cách 3 giây)
        run: |
          for i in $(seq 1 10); do
            if curl -fs http://localhost:8080/health > /dev/null; then
              echo "✅ App khoẻ sau $((i*3)) giây"
              curl -s http://localhost:8080/health; echo
              echo "$IMAGE_TAG" > ~/trien-khai/tag-hien-tai.txt
              exit 0
            fi
            echo "Lần $i: chưa sẵn sàng, chờ thêm..."
            sleep 3
          done
          echo "❌ App không phản hồi sau 30 giây — deploy THẤT BẠI"
          docker compose -f deploy/docker-compose.prod.yml logs --tail 50
          exit 1

      - name: Tóm tắt kết quả
        if: success()
        run: |
          echo "### ✅ Deploy thành công" >> $GITHUB_STEP_SUMMARY
          echo "- Image: \`$IMAGE_NAME:$IMAGE_TAG\`" >> $GITHUB_STEP_SUMMARY
          echo "- Bản trước: \`$(cat ~/trien-khai/tag-truoc-do.txt 2>/dev/null || echo 'chưa có')\`" >> $GITHUB_STEP_SUMMARY
```

### 🧭 Hướng dẫn làm LAB — step by step

#### Bước 1 — Cắm máy bạn vào GitHub làm runner

Vào repo → **Settings → Actions → Runners → New self-hosted runner** → chọn **Linux / x64**.

GitHub hiện sẵn một loạt lệnh **có token riêng của bạn**. Chạy đúng theo trang đó, đại ý:

```bash
mkdir -p ~/actions-runner && cd ~/actions-runner
curl -o actions-runner-linux-x64.tar.gz -L <duong-dan-GitHub-cho-san>
tar xzf actions-runner-linux-x64.tar.gz
./config.sh --url https://github.com/<ten-cua-ban>/ci-demo --token <TOKEN-GITHUB-CHO>
```

Khi `config.sh` hỏi, cứ **Enter** để lấy mặc định (nhóm runner, tên runner, thư mục làm việc).

**Bạn sẽ thấy:**
```text
√ Runner successfully added
√ Runner connection is good
√ Settings Saved.
```

✅ **Checkpoint:** dòng `Runner successfully added`.

Giờ cho nó chạy nền như một dịch vụ hệ thống (để tắt terminal vẫn sống):

```bash
sudo ./svc.sh install
sudo ./svc.sh start
sudo ./svc.sh status
```

**Bạn sẽ thấy:**
```text
● actions.runner.<ten-cua-ban>-ci-demo.<ten-may>.service - GitHub Actions Runner
   Active: active (running) since ...
```

✅ **Checkpoint:** quay lại **Settings → Actions → Runners** trên GitHub, runner hiện chấm xanh **Idle**.

⚠️ **Nếu runner báo Offline:** dịch vụ chưa chạy. Xem log: `sudo journalctl -u actions.runner.* -n 50 --no-pager`.

⚠️ **Nhắc lại lần cuối:** repo phải là **Private**. Runner trên repo public = người lạ chạy được code tuỳ ý trên máy bạn.

#### Bước 2 — Cho runner quyền dùng Docker

Runner chạy dưới user của bạn, user đó phải thuộc nhóm `docker`:

```bash
sudo usermod -aG docker $USER
sudo ./svc.sh stop && sudo ./svc.sh start     # khởi động lại để nhận nhóm mới
docker ps                                      # nếu lệnh này chạy được, là ổn
```

✅ **Checkpoint:** `docker ps` chạy không cần `sudo`.

⚠️ Nếu vẫn `permission denied ... docker.sock`, hãy đăng xuất/đăng nhập lại phiên làm việc rồi khởi động lại dịch vụ runner.

#### Bước 3 — Tạo Environment `production` có người duyệt

Vào repo → **Settings → Environments → New environment** → tên `production` → **Configure environment**:

- ✅ **Required reviewers** → thêm chính bạn
- **Save protection rules**

✅ **Checkpoint:** mục Environments hiện `production` kèm dòng *1 required reviewer*.

💡 Bạn tự duyệt chính mình nghe hơi buồn cười, nhưng hãy làm — để **tận mắt thấy pipeline dừng lại chờ**. Ở công ty, đây chính là cánh cổng ngăn một cú push lúc nửa đêm đi thẳng ra production.

#### Bước 4 — Đẩy 2 file mới lên

```bash
cd ~/ci-demo
mkdir -p deploy
# tạo deploy/docker-compose.prod.yml và .github/workflows/deploy.yml theo phần LAB
git add deploy .github/workflows/deploy.yml
git commit -m "Thêm deploy tự động lên self-hosted runner"
git push
```

Vào tab **Actions**, quan sát thứ tự:

**Bạn sẽ thấy:**
```text
1. CI                       ✅  (khoảng 40 giây)
2. CD - Đóng gói image      ✅  (khoảng 1 phút)
3. Deploy lên server        🟡  Waiting for review     ← dừng lại ở đây!
```

✅ **Checkpoint:** workflow deploy dừng ở trạng thái chờ duyệt.

💡 Để ý cơ chế: `workflow_run` khiến deploy **chỉ khởi động sau khi** workflow đóng gói image kết thúc thành công. Đây là cách nối hai workflow rời thành một dây chuyền — image chưa có thì không bao giờ deploy hụt.

#### Bước 5 — Duyệt và xem nó chạy trên máy bạn

Bấm vào run đang chờ → **Review deployments** → tick `production` → **Approve and deploy**.

Mở một terminal khác và xem trực tiếp:

```bash
watch -n 1 'docker ps --format "table {{.Names}}\t{{.Status}}\t{{.Ports}}"'
```

**Bạn sẽ thấy container hiện ra:**
```text
NAME            STATUS                    PORTS
ci-demo-prod    Up 8 seconds (healthy)    0.0.0.0:8080->3000/tcp
```

Và trong log của job:
```text
Lần 1: chưa sẵn sàng, chờ thêm...
✅ App khoẻ sau 6 giây
{"trangThai":"ok"}
```

Tự kiểm chứng:
```bash
curl -s localhost:8080
```

**Bạn sẽ thấy:**
```text
{"thongDiep":"ci-demo bản thứ hai","donHangMau":36000}
```

✅ **Checkpoint:** app đang phục vụ ở cổng 8080, và bạn **chưa gõ một lệnh docker nào** để đưa nó lên.

#### Bước 6 — Deploy lần thứ hai: thấy cả dây chuyền tự chạy

```bash
sed -i 's/ci-demo bản thứ hai/ci-demo bản thứ BA - deploy tự động/' app.js
git commit -am "Bản thứ ba"
git push
```

Giờ chỉ việc ngồi xem: CI ✅ → đóng gói image ✅ → deploy chờ duyệt → bạn Approve → container tự thay bản mới.

```bash
curl -s localhost:8080
cat ~/trien-khai/tag-hien-tai.txt
cat ~/trien-khai/tag-truoc-do.txt
```

**Bạn sẽ thấy:**
```text
{"thongDiep":"ci-demo bản thứ BA - deploy tự động","donHangMau":36000}
9c4e1f2...        <- SHA đang chạy
3f7a2c9...        <- SHA bản trước, chính là đường lui của bạn
```

✅ **Checkpoint:** nội dung đổi, và file ghi lại đủ **bản đang chạy + bản trước đó**.

💡 Hai dòng SHA này chính là câu trả lời cho hai câu hỏi hay gặp nhất lúc sự cố: *"đang chạy bản nào?"* và *"lui về đâu?"*.

#### Bước 7 — Rollback: quay lui trong 30 giây

Giả sử bản vừa lên có bug. Lấy SHA bản trước:

```bash
cat ~/trien-khai/tag-truoc-do.txt
```

Vào GitHub → **Actions** → workflow **Deploy lên server** → **Run workflow** → dán SHA đó vào ô *Tag image cần deploy* → **Run workflow** → Approve.

Sau khoảng 30 giây:

```bash
curl -s localhost:8080
```

**Bạn sẽ thấy:** nội dung **bản cũ** quay trở lại.

✅ **Checkpoint:** rollback xong mà không cần `git revert`, không cần build lại, không cần SSH vào đâu cả.

💡 **Đây chính là phần thưởng của việc gắn tag bất biến ở Ngày 33.** Bản cũ vẫn nằm nguyên trong kho, nên quay lui chỉ là "chạy lại pipeline với một chuỗi ký tự khác". Nếu hôm qua bạn dùng `latest`, lúc này sẽ không có gì để quay về.

#### Bước 8 — Kiểm chứng healthcheck thật sự chặn deploy hỏng

Cố tình làm app chết ngay khi khởi động:

```bash
sed -i "s|const PORT = process.env.PORT || 3000;|const PORT = 9999; // cố ý sai cổng|" app.js
git commit -am "Thử: cố ý deploy bản hỏng"
git push
```

Chờ image build xong, Approve deploy, rồi xem log job.

**Bạn sẽ thấy:**
```text
Lần 1: chưa sẵn sàng, chờ thêm...
Lần 2: chưa sẵn sàng, chờ thêm...
...
Lần 10: chưa sẵn sàng, chờ thêm...
❌ App không phản hồi sau 30 giây — deploy THẤT BẠI
```

Và job chuyển ❌ đỏ.

✅ **Checkpoint:** pipeline **tự phát hiện bản hỏng** và báo đỏ, thay vì lặng lẽ để hệ thống chết.

Quay lui về bản tốt bằng đúng cách ở Bước 7, rồi sửa code:
```bash
sed -i "s|const PORT = 9999; // cố ý sai cổng|const PORT = process.env.PORT \|\| 3000;|" app.js
git commit -am "Sửa lại cổng"
git push
```

💡 **Lưu ý thẳng thắn về giới hạn của bài này:** khi bản mới hỏng, `docker compose up -d` đã thay container cũ rồi mới kiểm tra sức khoẻ → có một khoảng thời gian dịch vụ chết. Đây là kiểu deploy đơn giản nhất. Muốn **không gián đoạn giây nào** thì cần chạy song song bản cũ và bản mới rồi mới chuyển hướng người dùng — đó là **rolling update / blue-green**, học ở Ngày 37 và 41 với Kubernetes.

### 🔁 Phương án B — Deploy tới VM thật qua SSH

Khi bạn đã có server thật (VM cloud từ Ngày 27), đổi job deploy sang chạy trên runner của GitHub và điều khiển server qua SSH.

Tạo 3 secret trong **Settings → Secrets and variables → Actions**: `SSH_HOST`, `SSH_USER`, `SSH_KHOA_RIENG` (nội dung khoá private, phần công khai đã nạp vào `~/.ssh/authorized_keys` trên server).

```yaml
  deploy-ssh:
    runs-on: ubuntu-latest
    environment: production
    steps:
      - name: Nạp khoá SSH
        run: |
          mkdir -p ~/.ssh
          echo "${{ secrets.SSH_KHOA_RIENG }}" > ~/.ssh/id_ed25519
          chmod 600 ~/.ssh/id_ed25519
          ssh-keyscan -H "${{ secrets.SSH_HOST }}" >> ~/.ssh/known_hosts

      - name: Deploy trên server
        run: |
          ssh -i ~/.ssh/id_ed25519 ${{ secrets.SSH_USER }}@${{ secrets.SSH_HOST }} bash -s <<'KETTHUC'
            set -e
            echo "${GHCR_TOKEN}" | docker login ghcr.io -u "${GHCR_USER}" --password-stdin
            docker pull ghcr.io/ban/ci-demo:TAG_CAN_DEPLOY
            docker stop ci-demo-prod 2>/dev/null || true
            docker rm   ci-demo-prod 2>/dev/null || true
            docker run -d --name ci-demo-prod -p 8080:3000 --restart unless-stopped \
              ghcr.io/ban/ci-demo:TAG_CAN_DEPLOY
          KETTHUC

      - name: Kiểm tra sức khoẻ từ xa
        run: curl -fs http://${{ secrets.SSH_HOST }}:8080/health
```

⚠️ **Ba điều bắt buộc khi làm cách này:**
1. **`ssh-keyscan` là bắt buộc** — thiếu nó SSH sẽ treo chờ câu hỏi "Are you sure you want to continue connecting?" cho đến khi job hết giờ. (Tuyệt đối không dùng `StrictHostKeyChecking=no` để né — đó là mở đường cho tấn công xen giữa.)
2. **Khoá riêng phải là khoá dành riêng cho deploy**, chỉ có quyền tối thiểu trên server — không bao giờ dùng khoá cá nhân của bạn.
3. **Server phải mở cổng SSH ra Internet** cho runner vào. Đây chính là nhược điểm của mô hình push mà GitOps (Ngày 43) sinh ra để giải quyết.

### 💡 Đi làm mới thấm (sách cơ bản hay bỏ quên)

- **Deploy thành công ≠ hệ thống khoẻ.** Container `Up` không có nghĩa app phục vụ được — nó có thể đang chờ database, chờ migration, hoặc đã chết bên trong. Vì vậy **bước kiểm tra sức khoẻ sau deploy là bắt buộc**, không phải tuỳ chọn.
- **Rollback phải tập trước khi cần.** Ai cũng nói "có rollback", nhưng lần đầu dùng nó thường là lúc 2 giờ sáng, hệ thống đang chết, tay run. Hãy bấm thử rollback vài lần lúc bình thường để nó thành phản xạ.
- **Migration database là phần không thể rollback dễ dàng.** Code lui về bản cũ được; nhưng một cột đã bị xoá thì không tự mọc lại. Nguyên tắc sống còn: migration phải **tương thích ngược** (thêm cột trước, bỏ cột ở lần triển khai sau), không bao giờ xoá thứ gì bản đang chạy còn cần.
- **Self-hosted runner là con dao hai lưỡi.** Nó không sạch sau mỗi lần chạy như runner GitHub — rác, cache và cả secret của lần trước đều còn đó. Đừng bao giờ gắn vào repo public, và định kỳ dọn: `docker system prune -af --filter "until=168h"`.
- **`concurrency` cho job deploy quan trọng hơn cho CI.** Hai lần deploy chạy chồng nhau có thể để lại hệ thống ở trạng thái nửa vời, khó đoán. Với deploy hãy dùng `cancel-in-progress: false` (xếp hàng, đừng huỷ) — khác với CI.
- **Giữ log deploy như tài sản.** Câu hỏi "ai deploy cái gì lúc mấy giờ" xuất hiện trong *mọi* buổi mổ xẻ sự cố. Lịch sử Actions trả lời được điều đó — đây là một lợi ích của CD mà người mới thường không để ý.

### 📝 Tự kiểm tra

> Nghĩ câu trả lời **thành lời** trước khi mở đáp án — nghĩ thầm luôn thấy mình hiểu.

<details>
<summary><b>1. Mô hình push và pull khác nhau ở điểm cốt lõi nào về bảo mật?</b></summary>

**Chiều của kết nối, và ai giữ chìa khoá.**

- **Push** (hôm nay): CI ở ngoài giữ khoá SSH/kubeconfig và chủ động vào server ra lệnh. Ai chiếm được CI thì chiếm được cả server.
- **Pull** (GitOps, Ngày 43): một tác nhân sống **bên trong** hạ tầng tự kéo từ Git về. Không ai bên ngoài cần giữ chìa khoá, và server không cần mở cổng vào.

Đây chính là nhược điểm của push mà GitOps sinh ra để giải quyết.

</details>

<details>
<summary><b>2. Vì sao self-hosted runner tuyệt đối không được gắn vào repo public?</b></summary>

Vì bất kỳ ai cũng mở được Pull Request vào repo public, và workflow sẽ chạy code của họ **ngay trên máy bạn** — với quyền của user chạy runner.

Thêm nữa, runner tự host **không sạch sau mỗi lần chạy** như runner của GitHub: rác, cache và cả secret của lần trước đều còn đó.

Đó là lý do Ngày 31 bắt tạo repo Private ngay từ đầu.

</details>

<details>
<summary><b>3. Deploy thành công nhưng tại sao vẫn phải kiểm tra sức khoẻ sau đó?</b></summary>

Vì **container `Up` không có nghĩa là ứng dụng phục vụ được**. Nó có thể đang chờ database, đang chạy migration, hoặc đã chết bên trong mà tiến trình vẫn sống.

Không có bước kiểm tra sức khoẻ thì pipeline luôn báo xanh kể cả khi vừa đẩy một bản hỏng ra production — và bạn chỉ biết khi người dùng gọi điện.

Bước kiểm tra phải có **thử lại** (vài lần, cách nhau vài giây) vì ứng dụng cần thời gian khởi động.

</details>

### 📚 Thuật ngữ Anh–Việt (ngày này)

| Thuật ngữ | Nghĩa |
|---|---|
| **Push vs Pull deployment** | CI đẩy vào hạ tầng vs tác nhân trong hạ tầng tự kéo về |
| **Self-hosted runner** | Máy của bạn tự cắm vào GitHub nhận việc; không cần IP public |
| **Environment** | Cổng có người gác trong GitHub Actions — chờ duyệt mới deploy |
| **`workflow_run`** | Trigger chạy workflow này sau khi workflow kia kết thúc |
| **Health check sau deploy** | Gọi `/health` có thử lại; thất bại thì báo đỏ, chặn bản hỏng |
| **Rollback** | Quay về bản trước bằng cách deploy lại tag SHA cũ |
| **`ssh-keyscan`** | Nạp host key trước khi SSH tự động, tránh treo chờ xác nhận |
| **Migration tương thích ngược** | Thêm cột trước, bỏ cột ở lần sau — để code cũ vẫn chạy được |

### 🎯 Đúc kết Ngày 34

**3 điều phải mang theo:**

1. **Deploy là một pipeline có kiểm chứng, không phải thao tác chép file.** Đủ bốn thứ: tag bất biến, kiểm tra sức khoẻ, đường lui, và dấu vết ai-làm-gì-lúc-nào.
2. **Push model đơn giản nhưng buộc CI giữ chìa khoá vào server.** Nhớ nhược điểm này — Ngày 43 (GitOps) sinh ra chính là để lật ngược chiều kết nối.
3. **Rollback chỉ dễ khi bản cũ còn tồn tại dưới một cái tên bất biến.** Đây là lúc bạn thu hoạch thành quả của việc tag theo SHA ở Ngày 33.

> 🧠 **Một câu để nhớ:** deploy tự động không phải để **nhanh hơn**, mà để **lặp lại được và quay lui được** — tốc độ chỉ là phần thưởng đi kèm.

**✅ Tự chấm** *(đánh dấu khi làm được mà không nhìn tài liệu):*

- [ ] Cài self-hosted runner và nói rõ vì sao nó không cần IP public
- [ ] Giải thích rủi ro của self-hosted runner trên repo public
- [ ] Dùng `workflow_run` để nối hai workflow thành dây chuyền
- [ ] Gắn Environment có người duyệt và thấy pipeline dừng lại chờ
- [ ] Viết bước kiểm tra sức khoẻ có thử lại, và chứng minh nó chặn được bản hỏng
- [ ] Thực hiện rollback bằng tag SHA cũ, không cần build lại
- [ ] Nói được vì sao migration database không rollback dễ như code

✅ **Kết quả đạt được:** Dây chuyền hoàn chỉnh từ `git push` tới bản đang phục vụ: kiểm tra code → đóng gói image → chờ duyệt → tự deploy → tự kiểm tra sức khoẻ → có đường lui. Đây chính là CD.

---

## Ngày 35 — MILESTONE: Pipeline CI/CD hoàn chỉnh

> ⏱️ ~150 phút · Loại: LAB Final
>
> 🧭 **Bạn đang ở đâu:** Ngày 31–34 (GitHub Actions, CI nhiều tầng, đóng gói image, deploy tự động) → **Ngày 35 (ghép thành một dây chuyền duy nhất và đo nó)** → Ngày 36 (Kubernetes).
>
> ✅ **Chuẩn bị:** repo `ci-demo` với CI, workflow đóng gói image và deploy từ Ngày 31–34.
>
> 🎯 **Đề bài + tiêu chí chấm.** Và hôm nay có một việc đặc biệt: **mở lại file `diem-dau.md` của Ngày 28** để so sánh.

### 📋 Đề bài — "Dây chuyền hoàn chỉnh, đo được"

> Từ `git push` tới ứng dụng đang phục vụ, không ai chạm tay vào server. Và bạn phải **chứng minh bằng số liệu** rằng nó tốt hơn cách làm tay ở Ngày 28.

```text
  git push
     ↓
  [CI]    lint → test (matrix) → build → artifact
     ↓
  [Quét]  bí mật · lỗ hổng · Dockerfile
     ↓
  [Đóng gói]  image tag = SHA → registry
     ↓
  [Duyệt]  environment có người xác nhận
     ↓
  [Deploy]  tự động + kiểm tra sức khoẻ
     ↓
  Quay lui được bằng một thao tác
```

### ✅ Yêu cầu

#### Bắt buộc

| # | Yêu cầu | Kiến thức từ |
|---|---|---|
| 1 | CI nhiều tầng có `needs:`, matrix, cache | Ngày 32 |
| 2 | Ba lớp quét bảo mật, **thực sự chặn được** | Ngày 49 (áp dụng sớm) |
| 3 | Image tag theo SHA, đẩy lên registry | Ngày 33 |
| 4 | Deploy tự động sau khi image sẵn sàng | Ngày 34 |
| 5 | Kiểm tra sức khoẻ sau deploy, hỏng thì báo đỏ | Ngày 34 |
| 6 | Quay lui bằng một thao tác, dưới 2 phút | Ngày 34 |
| 7 | Branch protection: CI đỏ không merge được | Ngày 32 |
| 8 | Không bí mật nào trong repo | Ngày 31 |
| 9 | **Bảng so sánh với Ngày 28**, có số liệu thật | Ngày 28 |

#### Nâng cao

| # | Yêu cầu |
|---|---|
| 10 | Pipeline chạy dưới 4 phút |
| 11 | `concurrency` chống chạy chồng |
| 12 | `permissions` khai tối thiểu cho từng job |
| 13 | Thông báo kết quả deploy ra kênh chat |
| 14 | Ghim action bằng SHA thay vì nhãn phiên bản |

### 📐 Tiêu chí chấm (100 điểm)

| Hạng mục | Điểm | Đạt tối đa khi |
|---|---:|---|
| Cấu trúc pipeline | 20 | Nhiều tầng hợp lý, song song đúng chỗ, có cache |
| Bảo mật trong pipeline | 20 | 3 lớp quét, chặn thật, quyền tối thiểu |
| Đóng gói & gắn tag | 15 | Tag bất biến, truy ngược ra commit được |
| Tự động deploy | 15 | Không thao tác tay, có cổng duyệt |
| Kiểm tra sau deploy | 10 | Có thử lại, chặn được bản hỏng |
| Quay lui | 10 | Một thao tác, đã bấm giờ thật |
| Đo đạc & so sánh | 10 | Bảng so sánh với Ngày 28, số liệu thật |

### 🔥 Bốn phép thử bắt buộc

**Phép thử 1 — Toàn bộ dây chuyền (bấm giờ).**
```bash
cd ~/ci-demo
echo "// thay đổi $(date +%s)" >> app.js
BAT_DAU=$(date +%s)
git commit -am "Đo thời gian dây chuyền" && git push
# ... chờ tới khi bản mới thật sự đang phục vụ ...
echo "Thời gian từ commit tới chạy thật: $(( $(date +%s) - BAT_DAU )) giây"
```

**Phép thử 2 — CI chặn được code hỏng.** Mở PR có lỗi lint hoặc test hỏng → nút Merge phải bị khoá.

**Phép thử 3 — Quét bảo mật chặn được.** Commit một chuỗi giống token → job quét bí mật phải đỏ.

**Phép thử 4 — Quay lui (bấm giờ).** Deploy bản hỏng, rồi quay lui về bản trước bằng tag SHA cũ. Ghi lại thời gian.

### 📊 Bảng so sánh — phần thưởng của cả Giai đoạn 3

Mở lại `~/lab28-deploy/diem-dau.md` và điền cột bên phải:

| # | Điểm đau | Ngày 28 (làm tay) | Hôm nay (tự động) |
|---|---|---|---|
| 1 | Số lệnh phải gõ đúng thứ tự | 6 lệnh | **0** — chỉ `git push` |
| 2 | Dấu vết ai deploy, lúc nào, từ code nào | Không có | Lịch sử Actions, tag SHA |
| 3 | Thời gian deploy | ___ giây | ___ giây |
| 4 | Gián đoạn khi cập nhật | ___ giây | ___ giây |
| 5 | Thời gian quay lui | ___ giây (phải build lại) | ___ giây (đổi tag) |
| 6 | Nguy cơ quên bước | Cao | Không — máy không quên |
| 7 | Deploy được khi bạn nghỉ phép | Không | Có |

> 💡 **Hãy thật sự điền bảng này.** Nó là thứ bạn mang vào buổi phỏng vấn, và cũng là thứ chứng minh cho chính bạn rằng bốn ngày vừa rồi đáng giá. Con số thuyết phục hơn mọi lời giải thích.

### 🧪 Bộ kiểm chứng

```bash
#!/usr/bin/env bash
cd ~/ci-demo
diem=0
kiem() { if eval "$2" &>/dev/null; then echo "  ✅ $1 (+$3)"; diem=$((diem+$3)); else echo "  ❌ $1"; fi; }

echo "▸ Cấu trúc pipeline"
kiem "Có dùng needs (nhiều tầng)"    "grep -rq 'needs:' .github/workflows/" 7
kiem "Có matrix"                     "grep -rq 'matrix:' .github/workflows/" 5
kiem "Có cache"                      "grep -rq 'cache:' .github/workflows/" 4
kiem "Có concurrency"                "grep -rq 'concurrency:' .github/workflows/" 4

echo "▸ Bảo mật"
for t in gitleaks trivy hadolint; do
  kiem "Có quét bằng $t" "grep -rqi '$t' .github/workflows/" 5
done
kiem "Khai permissions tối thiểu"    "grep -rq 'permissions:' .github/workflows/" 5

echo "▸ Đóng gói"
kiem "Tag theo SHA"                  "grep -rq 'github.sha' .github/workflows/" 8
kiem "Không deploy bằng latest"      "! grep -rq 'deploy.*:latest' .github/workflows/" 7

echo "▸ Deploy"
kiem "Có environment (cổng duyệt)"   "grep -rq 'environment:' .github/workflows/" 8
kiem "Có kiểm tra sức khoẻ"          "grep -rqE 'health|curl -fs' .github/workflows/" 7

echo "▸ Repo sạch"
kiem "Không bí mật trong Git"        "! git ls-files | grep -qE '\.env$|\.pem$'" 5
kiem "Có .gitignore"                 "[ -f .gitignore ]" 3
kiem "Có ghim phiên bản action"      "! grep -rq 'uses:.*@main' .github/workflows/" 4

echo ""
echo "  ĐIỂM (tự động): $diem / 77"
echo "  23 điểm còn lại: 4 phép thử + bảng so sánh"
```

### ⚠️ Những cái bẫy hay gặp

| Bẫy | Hậu quả | Cách tránh |
|---|---|---|
| Deploy chạy trên mọi nhánh | Nhánh nháp cũng lên production | Giới hạn trigger: chỉ `main` |
| Quét bảo mật để chế độ cảnh báo | Không ai đọc, không chặn gì | `exit-code: 1` cho HIGH/CRITICAL |
| Không có cổng duyệt cho production | Push nhầm là lên thẳng | Environment có người xác nhận |
| Pipeline 15 phút | Cả đội bắt đầu tìm cách lách | Cache + song song + xếp bước rẻ trước |
| Chưa từng thử quay lui | Lúc cần thì luống cuống | Phép thử 4, làm ít nhất một lần |
| Ghim action bằng `@main` | Tác giả sửa là pipeline gãy | Ghim phiên bản, lý tưởng là SHA |

### 💬 Gợi ý khi bí

<details>
<summary><b>Pipeline nên chia thành mấy workflow?</b></summary>

Ba workflow tách biệt, nối với nhau bằng `workflow_run` — đây là cấu trúc dùng phổ biến:

| Workflow | Chạy khi | Việc |
|---|---|---|
| `ci.yml` | push + PR | lint, test, build |
| `bao-mat.yml` | push + PR + theo lịch | 3 lớp quét |
| `cd.yml` | chỉ sau khi CI xanh trên `main` | đóng gói image + deploy |

Vì sao tách: CI và quét cần chạy trên **mọi PR** (kể cả từ người ngoài), còn deploy **chỉ** được chạy trên `main` và cần quyền cao hơn. Gộp chung một file dễ dẫn tới cấu hình quyền quá rộng.
</details>

<details>
<summary><b>Làm sao rút pipeline xuống dưới 4 phút?</b></summary>

Đo trước — mở từng job trong giao diện Actions xem bước nào lâu nhất. Bốn cách theo hiệu quả giảm dần:

1. **Cache thư viện** (`cache: 'npm'`) — thường tiết kiệm nhiều nhất
2. **Cache lớp Docker** (`cache-from: type=gha`)
3. **Chạy song song** — lint và quét bảo mật không cần chờ nhau
4. **`fail-fast` hợp lý** — lỗi sớm thì dừng sớm, khỏi chờ hết

Một cách nữa hay bị bỏ qua: **đừng chạy lại mọi thứ cho mỗi commit trong PR**. `concurrency` với `cancel-in-progress: true` huỷ các lần chạy cũ khi bạn push liên tiếp.
</details>

### 🎯 Đúc kết Ngày 35 — Tổng kết phần CI/CD

**3 điều phải mang theo:**

1. **Dây chuyền được đo bằng thời gian từ commit tới chạy thật**, không bằng số công cụ nó dùng.
2. **Quay lui dễ quan trọng hơn deploy nhanh.** Khi lui rẻ, người ta hết sợ phát hành — và phát hành thường xuyên hơn thì mỗi lần lại an toàn hơn.
3. **Tự động hoá lấy quy trình ra khỏi đầu người và đặt vào file.** Bảng so sánh với Ngày 28 cho thấy chính xác bạn vừa thu được gì.

> 🧠 **Một câu để nhớ:** giá trị lớn nhất của CI/CD không phải tốc độ — mà là **hệ thống vẫn deploy được khi bạn đang đi nghỉ**.

**✅ Tự chấm Milestone:**

- [ ] Đạt từ 75 điểm
- [ ] Bốn phép thử đều đạt, có ghi số liệu
- [ ] Bảng so sánh với Ngày 28 đã điền đủ
- [ ] Pipeline dưới 5 phút
- [ ] Quay lui dưới 2 phút

✅ **Kết quả đạt được:** Một dây chuyền tự động hoàn chỉnh, đo được, và có bằng chứng bằng số liệu cho thấy nó hơn hẳn cách làm tay.

---

## Ngày 36 — Kubernetes: Khái niệm & Kiến trúc

> ⏱️ ~90 phút · Loại: Kubernetes
>
> 🧭 **Bạn đang ở đâu:** Ngày 35 (CI/CD hoàn chỉnh trên một máy) → **Ngày 36 (Kubernetes — bộ não điều phối container trên nhiều máy)** → Ngày 37 (chạy app bằng Deployment). Hôm nay chỉ tập trung vào **cách K8s nghĩ**; Ngày 37 mới đi sâu vào triển khai ứng dụng.
>
> ☸️ *Học trên **Minikube** (miễn phí, ngay trên máy bạn). Cùng một kiến thức áp dụng được cho **kind**, **k3s**, và cluster thật: **EKS** (AWS) / **GKE** (GCP) / **AKS** (Azure).*
>
> ✅ **Chuẩn bị:** máy Linux có Docker đang chạy, còn trống ít nhất **4 GB RAM** và ~10 GB đĩa.
>
> 🎁 **Cuối ngày bạn có gì:** một cluster Kubernetes chạy trên máy, và bạn sẽ **tự tay giết pod nhiều lần để thấy nó tự hồi sinh** — hiểu được thứ làm nên toàn bộ sức mạnh của K8s.

### 📘 Lý thuyết

#### 1. Vấn đề: hôm qua bạn deploy 1 container lên 1 máy

Ngày 34 pipeline của bạn chạy `docker compose up -d` trên một máy. Nó hoạt động tốt. Giờ hãy hỏi tiếp:

| Tình huống | Với Docker Compose một máy | Ai sẽ xử lý? |
|---|---|---|
| Container chết lúc 3 giờ sáng | `restart: unless-stopped` cứu được nếu tiến trình chết, nhưng app "treo mà chưa chết" thì không | **Bạn** |
| Cả máy chủ hỏng | Toàn bộ dịch vụ chết | **Bạn**, bằng tay, lúc nửa đêm |
| Lượng truy cập tăng gấp 10 | Phải tự thêm máy, tự chia tải | **Bạn** |
| Cập nhật không được gián đoạn | Compose thay container → có khoảng chết | **Bạn** |
| 40 dịch vụ trên 8 máy | Ai nhớ nổi cái gì đang chạy ở đâu? | **Không ai** |

Kubernetes sinh ra để những ô đó ghi **"hệ thống tự lo"**. Nó là phần mềm làm thay đúng công việc mà một người trực đêm phải làm: theo dõi, khởi động lại, phân bổ, thay thế.

#### 2. Điểm cốt lõi nhất: khai báo thay vì ra lệnh

Đây là chỗ khác biệt lớn nhất so với mọi thứ bạn đã học, và cũng là chỗ khó chuyển đổi tư duy nhất:

| | **Ra lệnh** (imperative) — Docker, Bash | **Khai báo** (declarative) — Kubernetes |
|---|---|---|
| Bạn nói gì | *"Chạy container này lên"* | *"Tôi muốn **luôn luôn** có 3 bản đang chạy"* |
| Ai chịu trách nhiệm giữ đúng | Bạn | **Hệ thống** |
| Container chết | Nó chết, đến khi bạn phát hiện | K8s tạo cái mới, **trong vài giây** |
| Tài liệu hệ thống nằm đâu | Trong đầu người vận hành | **Trong file YAML**, đọc là biết |

Bạn nộp cho K8s một bản mô tả **trạng thái mong muốn**. K8s nhận lấy và tự xoay xở để biến nó thành sự thật — rồi **giữ mãi như vậy**.

#### 3. Vòng điều hoà — trái tim của Kubernetes

Tất cả sức mạnh của K8s nằm trong một vòng lặp đơn giản đến bất ngờ, chạy không ngừng:

```text
        ┌──────────────────────────────────────────┐
        │                                          │
        ▼                                          │
  Đọc "mong muốn"  ──>  So với "thực tế"  ──>  Khác nhau?
  (bạn khai: 3 pod)     (đang có: 2 pod)      → Tạo thêm 1 pod
        ▲                                          │
        └──────────── lặp lại mỗi vài giây ────────┘
```

Không có phép màu nào cả. Chỉ là một vòng lặp **so sánh mong muốn với thực tế rồi sửa cho khớp**, chạy suốt 24/7. "Tự phục hồi", "tự mở rộng", "cập nhật không gián đoạn" — tất cả đều chỉ là vòng lặp này áp vào các tình huống khác nhau.

#### 4. Kiến trúc — hình dung như một công ty

| Thành phần | Vai trò trong "công ty" |
|---|---|
| **Control Plane** | Ban giám đốc — ra quyết định, không trực tiếp chạy app |
| ├ **API Server** | Lễ tân: mọi yêu cầu đều đi qua đây. `kubectl` nói chuyện với chính nó |
| ├ **etcd** | Sổ cái: ghi *"mọi thứ đang phải như thế nào"*. Mất etcd = mất trí nhớ cluster |
| ├ **Scheduler** | Người xếp việc: pod mới nên chạy trên máy nào (còn RAM? còn CPU?) |
| └ **Controller Manager** | Quản đốc: chạy các **vòng điều hoà** ở mục 3 |
| **Worker Node** | Nhân viên — nơi container thật sự chạy |
| ├ **kubelet** | Tổ trưởng tại chỗ: nhận lệnh từ API Server, bảo Docker chạy container |
| └ **kube-proxy** | Bưu tá: lo đường mạng cho pod |

> 🔑 **Điểm mấu chốt:** `kubectl` của bạn **không bao giờ** nói chuyện trực tiếp với container. Nó chỉ ghi "mong muốn" vào sổ cái qua lễ tân (API Server). Phần còn lại do các vòng điều hoà tự xử lý. Đây là lý do K8s vẫn tiếp tục hoạt động ngay cả khi bạn tắt máy tính đi ngủ.

#### 5. Ba danh từ phải phân biệt được

- **Pod** — đơn vị nhỏ nhất K8s quản lý. Chứa 1 (thường là vậy) hoặc vài container dùng chung mạng và ổ đĩa. **Pod là thứ dùng một lần rồi bỏ** — chết là thay cái mới, không cứu chữa.
- **Node** — một máy (ảo hoặc vật lý) trong cluster, nơi pod chạy.
- **Cluster** — control plane + toàn bộ node.

> ⚠️ Người mới hay coi pod như "một cái máy nhỏ" cần chăm sóc. Sai. Hãy coi pod như **cốc giấy dùng một lần**: bẩn thì vứt, lấy cái mới. Mọi thiết kế trên K8s đều dựa vào giả định này.

**Sơ đồ — kiến trúc Kubernetes:**
```mermaid
flowchart TB
    kubectl["💻 kubectl<br/>(khai báo mong muốn)"] --> API
    subgraph CP["🧠 Control Plane"]
        API["API Server<br/>(lễ tân)"] --> ETCD[("etcd<br/>sổ cái")]
        API --> SCH["Scheduler<br/>(xếp việc)"]
        API --> CM["Controller Manager<br/>(vòng điều hoà)"]
    end
    subgraph N1["⚙️ Worker Node"]
        KUBELET["kubelet"] --> POD1["Pod A"]
        KUBELET --> POD2["Pod B"]
        PROXY["kube-proxy"]
    end
    CM -.->|"thiếu pod → tạo thêm"| KUBELET
    SCH -.->|"xếp pod vào node này"| KUBELET
    classDef cp fill:#e3f2fd,stroke:#1976d2;
    classDef wk fill:#e8f5e9,stroke:#2e7d32;
    class API,ETCD,SCH,CM cp;
    class KUBELET,POD1,POD2,PROXY wk;
```

### 🧪 LAB — Dựng cluster và tự tay kiểm chứng vòng điều hoà

> **Mục tiêu:** có cluster chạy, hiểu các thành phần bằng cách **nhìn thấy chúng**, rồi giết pod nhiều kiểu để thấy K8s phản ứng.

**File sẽ tạo:**

```text
lab36-k8s/
├── pod-tran.yaml          # Pod trần — để thấy nó KHÔNG tự hồi sinh
└── deployment-web.yaml    # Deployment — để thấy nó CÓ tự hồi sinh
```

#### File 1 — `pod-tran.yaml`

```yaml
apiVersion: v1
kind: Pod                      # Pod "trần" — không ai quản lý nó
metadata:
  name: web-tran
  labels:
    app: thu-nghiem
spec:
  containers:
    - name: web
      image: nginx:1.27        # tag cụ thể, KHÔNG dùng :latest
      ports:
        - containerPort: 80
      resources:               # xin tài nguyên vừa đủ, tránh chiếm hết máy
        requests:
          memory: "64Mi"
          cpu: "50m"
        limits:
          memory: "128Mi"
```

#### File 2 — `deployment-web.yaml`

```yaml
apiVersion: apps/v1
kind: Deployment               # Deployment = có "quản đốc" trông chừng
metadata:
  name: web
  labels:
    app: web
spec:
  replicas: 3                  # ĐÂY là "mong muốn": luôn có 3 bản chạy
  selector:
    matchLabels:
      app: web                 # quản lý những pod mang nhãn app=web
  template:                    # khuôn để đúc ra pod
    metadata:
      labels:
        app: web               # PHẢI khớp selector ở trên
    spec:
      containers:
        - name: web
          image: nginx:1.27
          ports:
            - containerPort: 80
          resources:
            requests:
              memory: "64Mi"
              cpu: "50m"
            limits:
              memory: "128Mi"
```

### 🧭 Hướng dẫn làm LAB — step by step

#### Bước 1 — Cài `kubectl`

```bash
curl -LO "https://dl.k8s.io/release/$(curl -Ls https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
sudo install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl
rm kubectl
kubectl version --client
```

**Bạn sẽ thấy:**
```text
Client Version: v1.31.x
Kustomize Version: v5.x.x
```

✅ **Checkpoint:** in ra được `Client Version`.

💡 `kubectl` chỉ là **cái điều khiển từ xa** — nó chưa cần cluster nào để cài. Bước sau mới dựng cluster cho nó điều khiển.

#### Bước 2 — Cài Minikube và khởi động cluster

```bash
curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
sudo install minikube-linux-amd64 /usr/local/bin/minikube
rm minikube-linux-amd64

minikube start --driver=docker --memory=3072 --cpus=2
```

**Bạn sẽ thấy** (mất 2–5 phút lần đầu vì phải tải image):
```text
😄  minikube v1.34.0 on Ubuntu 24.04
✨  Using the docker driver based on user configuration
🔥  Creating docker container (CPUs=2, Memory=3072MB) ...
🐳  Preparing Kubernetes v1.31.0 on Docker 27.x ...
🏄  Done! kubectl is now configured to use "minikube" cluster
```

✅ **Checkpoint:** dòng `Done! kubectl is now configured...`.

⚠️ **Nếu lỗi `Exiting due to RSRC_INSUFFICIENT_MEMORY`:** máy không đủ RAM trống. Hạ xuống `--memory=2048`, đóng bớt ứng dụng khác.

⚠️ **Nếu lỗi `permission denied ... docker.sock`:** user chưa vào nhóm docker (Ngày 34 Bước 2): `sudo usermod -aG docker $USER` rồi đăng xuất/đăng nhập lại.

💡 Minikube dựng **cả một cluster Kubernetes bên trong một container Docker**. Kiểm chứng ngay: `docker ps` sẽ thấy một container tên `minikube` — cả cluster của bạn nằm trong đó.

#### Bước 3 — Nhìn thấy cluster và node

```bash
kubectl get nodes -o wide
```

**Bạn sẽ thấy:**
```text
NAME       STATUS   ROLES           AGE   VERSION   INTERNAL-IP    OS-IMAGE
minikube   Ready    control-plane   62s   v1.31.0   192.168.49.2   Ubuntu 22.04
```

✅ **Checkpoint:** `STATUS` là `Ready`.

⚠️ **Nếu `The connection to the server ... was refused`:** cluster chưa lên. Kiểm tra `minikube status`; nếu `Stopped` thì `minikube start`.

💡 Ở đây chỉ có **một** node và nó vừa là control plane vừa là worker (cluster học tập). Cluster thật thường 3 control plane + N worker — nhưng mọi khái niệm hoàn toàn giống nhau.

#### Bước 4 — Nhìn thấy chính các thành phần ở phần Lý thuyết

Đây là bước làm lý thuyết trở nên có thật. Các thành phần control plane cũng chỉ là... pod:

```bash
kubectl get pods -n kube-system
```

**Bạn sẽ thấy:**
```text
NAME                               READY   STATUS    RESTARTS   AGE
coredns-7db6d8ff4d-x8k2n           1/1     Running   0          2m
etcd-minikube                      1/1     Running   0          2m
kube-apiserver-minikube            1/1     Running   0          2m
kube-controller-manager-minikube   1/1     Running   0          2m
kube-proxy-9lhdw                   1/1     Running   0          2m
kube-scheduler-minikube            1/1     Running   0          2m
storage-provisioner                1/1     Running   0          2m
```

✅ **Checkpoint:** nhận ra đủ 4 thành phần control plane: `etcd`, `kube-apiserver`, `kube-controller-manager`, `kube-scheduler`.

💡 **Đây chính là bảng ở mục Lý thuyết #4, bằng xương bằng thịt.** `-n kube-system` nghĩa là "trong namespace kube-system" — namespace là cách chia ngăn cluster; phần của bạn mặc định nằm ở namespace `default`.

Xem địa chỉ lễ tân (API Server) mà `kubectl` đang gọi:
```bash
kubectl cluster-info
```
**Bạn sẽ thấy:** `Kubernetes control plane is running at https://192.168.49.2:8443`.

#### Bước 5 — Pod đầu tiên, và chứng minh pod trần rất mong manh

```bash
mkdir -p ~/lab36-k8s && cd ~/lab36-k8s
# tạo pod-tran.yaml theo phần LAB
kubectl apply -f pod-tran.yaml
kubectl get pods
```

**Bạn sẽ thấy:**
```text
pod/web-tran created

NAME       READY   STATUS    RESTARTS   AGE
web-tran   1/1     Running   0          8s
```

✅ **Checkpoint:** `STATUS` là `Running`, cột `READY` là `1/1`.

Giờ giết nó đi:

```bash
kubectl delete pod web-tran
kubectl get pods
```

**Bạn sẽ thấy:**
```text
pod "web-tran" deleted

No resources found in default namespace.
```

✅ **Checkpoint:** pod biến mất **vĩnh viễn**, không có gì tạo lại.

💡 **Vì sao:** pod trần không có ai "mong muốn" nó tồn tại cả. Bạn bảo tạo thì K8s tạo; bạn bảo xoá thì nó xoá; nó chết thì cũng chẳng ai quan tâm. **Đây là lý do thực tế gần như không ai tạo Pod trần** — luôn dùng Deployment.

#### Bước 6 — Deployment: giờ mới có người trông chừng

```bash
# tạo deployment-web.yaml theo phần LAB
kubectl apply -f deployment-web.yaml
kubectl get deployments
kubectl get pods -o wide
```

**Bạn sẽ thấy:**
```text
NAME   READY   UP-TO-DATE   AVAILABLE   AGE
web    3/3     3            3           12s

NAME                   READY   STATUS    RESTARTS   AGE   IP           NODE
web-6f8d9c7b5d-2xk4p   1/1     Running   0          12s   10.244.0.5   minikube
web-6f8d9c7b5d-7mnwq   1/1     Running   0          12s   10.244.0.6   minikube
web-6f8d9c7b5d-k9zlt   1/1     Running   0          12s   10.244.0.7   minikube
```

✅ **Checkpoint:** đúng **3 pod**, tên đều bắt đầu bằng `web-` kèm hai đoạn mã ngẫu nhiên.

💡 Bạn chỉ viết `replicas: 3` — **không hề ra lệnh tạo pod nào**. Vòng điều hoà đọc thấy "mong muốn 3, thực tế 0" nên tự tạo đủ 3.

#### Bước 7 — Giết pod và bấm giờ xem nó hồi sinh

Đây là bước quan trọng nhất cả ngày. Mở **hai terminal**.

**Terminal 1** — theo dõi trực tiếp:
```bash
kubectl get pods -w
```

**Terminal 2** — giết một pod (thay tên bằng pod thật của bạn):
```bash
kubectl delete pod web-6f8d9c7b5d-2xk4p
```

**Bạn sẽ thấy ở Terminal 1:**
```text
web-6f8d9c7b5d-2xk4p   1/1     Terminating         0     3m
web-6f8d9c7b5d-vv8qr   0/1     Pending             0     0s
web-6f8d9c7b5d-vv8qr   0/1     ContainerCreating   0     0s
web-6f8d9c7b5d-vv8qr   1/1     Running             0     2s
```

✅ **Checkpoint:** pod mới (tên khác) đạt `Running` trong khoảng **2–3 giây**.

💡 **Hãy dừng lại và ngẫm điều vừa xảy ra:** bạn phá, hệ thống tự sửa, trong 2 giây, lúc 3 giờ sáng cũng vậy, không ai phải thức dậy. **Toàn bộ giá trị của Kubernetes gói gọn ở đây.** Và nó chỉ là vòng lặp ở Lý thuyết #3 đang làm việc: "mong muốn 3, thực tế 2 → tạo thêm 1".

Thử ác hơn — giết sạch cả 3:
```bash
kubectl delete pods --all
kubectl get pods
```

**Bạn sẽ thấy:** 3 pod **mới toanh** đang được tạo. Không cách nào "giết chết" một Deployment bằng cách xoá pod.

#### Bước 8 — Thử cãi lại hệ thống (và thua)

Hãy thử sửa trực tiếp thực tế xem K8s phản ứng ra sao:

```bash
kubectl scale deployment web --replicas=5      # ra lệnh trực tiếp: 5 bản
kubectl get pods --no-headers | wc -l          # đếm: 5
```

Nhưng file YAML của bạn vẫn ghi `replicas: 3`. Giờ áp lại file:

```bash
kubectl apply -f deployment-web.yaml
sleep 3
kubectl get pods --no-headers | wc -l
```

**Bạn sẽ thấy:** quay về `3`.

✅ **Checkpoint:** hiểu rằng **file YAML là nguồn sự thật**, lệnh gõ tay chỉ là sửa tạm.

💡 **Bài học lớn:** nếu ai đó `kubectl scale` lúc nửa đêm để chữa cháy mà không sửa file, thì lần deploy sau con số sẽ âm thầm quay lại — sự cố tái diễn và **không ai hiểu vì sao**. Đây chính là lý do Ngày 43 (GitOps) tồn tại: bắt buộc mọi thay đổi phải đi qua Git.

#### Bước 9 — Ba lệnh điều tra dùng suốt đời làm K8s

```bash
POD=$(kubectl get pods -l app=web -o jsonpath='{.items[0].metadata.name}')

kubectl describe pod $POD | tail -20      # 1) chuyện gì đã xảy ra với pod này
kubectl logs $POD                          # 2) app bên trong nói gì
kubectl get events --sort-by=.lastTimestamp | tail -10   # 3) cluster vừa làm gì
```

**Bạn sẽ thấy ở `describe`** phần `Events` cuối cùng:
```text
Events:
  Type    Reason     Age   From               Message
  ----    ------     ----  ----               -------
  Normal  Scheduled  2m    default-scheduler  Successfully assigned default/web-... to minikube
  Normal  Pulled     2m    kubelet            Container image "nginx:1.27" already present
  Normal  Created    2m    kubelet            Created container web
  Normal  Started    2m    kubelet            Started container web
```

✅ **Checkpoint:** đọc được dòng `Scheduled` (Scheduler xếp việc) rồi `Started` (kubelet chạy container) — đúng luồng ở mục Lý thuyết #4.

💡 **Ghi nhớ thứ tự điều tra này:** `describe` (vì sao pod ở trạng thái đó) → `logs` (app nói gì) → `events` (cluster vừa làm gì). 90% sự cố K8s được khoanh vùng chỉ bằng ba lệnh này.

#### Bước 10 — Mở thử trang web và dọn dẹp

```bash
kubectl port-forward deployment/web 8081:80 &
sleep 2
curl -s localhost:8081 | head -5
kill %1
```

**Bạn sẽ thấy:** đoạn HTML `<title>Welcome to nginx!</title>`.

✅ **Checkpoint:** truy cập được vào pod.

💡 `port-forward` chỉ là **đường hầm tạm cho lập trình viên**, không phải cách người dùng thật vào ứng dụng. Cách đúng là **Service** và **Ingress** — học ở Ngày 38.

Dọn dẹp:
```bash
kubectl delete -f deployment-web.yaml
minikube stop            # dừng cluster, GIỮ nguyên mọi thứ cho Ngày 37
# minikube delete        # chỉ dùng khi muốn xoá sạch cluster làm lại từ đầu
```

⚠️ Dùng `minikube stop`, **đừng** `minikube delete` — Ngày 37 sẽ dùng lại chính cluster này.

### 💡 Đi làm mới thấm (sách cơ bản hay bỏ quên)

- **K8s không tự làm app bạn đáng tin cậy.** Nó chỉ đảm bảo *có đủ số pod đang chạy*. Nếu app khởi động mất 60 giây, hoặc treo mà tiến trình vẫn sống, K8s vẫn tưởng mọi thứ ổn. Muốn nó hiểu đúng thế nào là "khoẻ" thì phải khai **probe** (Ngày 41).
- **`kubectl get` nói *cái gì*, `describe` nói *vì sao*.** Người mới hay dán ảnh `kubectl get pods` rồi hỏi "sao pod lỗi?". Câu trả lời gần như luôn nằm ở phần `Events` cuối `kubectl describe`.
- **Namespace không chỉ để cho gọn.** Nó là ranh giới để đặt **quota tài nguyên** và **phân quyền RBAC**. Ở công ty, mỗi đội/môi trường thường một namespace riêng — một đội không thể vô tình xoá đồ của đội khác.
- **Luôn khai `resources.requests`.** Không khai thì Scheduler không biết pod cần bao nhiêu → xếp nhầm chỗ → các pod tranh nhau RAM → node lăn ra chết kéo theo mọi thứ trên đó. Đây là nguyên nhân sự cố cực kỳ phổ biến ở cluster của đội mới dùng K8s.
- **etcd là thứ phải backup.** Mất etcd = cluster mất trí nhớ hoàn toàn. Với managed K8s (EKS/GKE/AKS), nhà cung cấp lo giúp — đây là một lý do rất chính đáng để **không tự dựng cluster** khi chưa có đội chuyên trách.
- **Đừng vội lên K8s.** Nếu bạn chỉ có 2–3 dịch vụ trên một máy, Docker Compose (Ngày 20) đơn giản hơn nhiều và **hoàn toàn đủ dùng**. K8s bắt đầu đáng giá khi có nhiều dịch vụ, nhiều máy, và yêu cầu không gián đoạn. Chọn công cụ theo bài toán, không theo mốt.

### 📝 Tự kiểm tra

> Nghĩ câu trả lời **thành lời** trước khi mở đáp án — nghĩ thầm luôn thấy mình hiểu.

<details>
<summary><b>1. Giải thích vòng điều hoà của Kubernetes bằng lời của bạn. Vì sao nó là gốc của mọi tính năng?</b></summary>

Một vòng lặp chạy liên tục: **đọc trạng thái mong muốn** (bạn khai trong YAML) → **so với thực tế** (pod đang chạy) → **khác nhau thì sửa cho khớp** → lặp lại sau vài giây.

Không có phép màu nào cả. Và mọi tính năng chỉ là vòng lặp này áp vào tình huống khác nhau:
- *Tự phục hồi* = mong muốn 3, thực tế 2 → tạo thêm 1
- *Tự mở rộng* = HPA sửa con số mong muốn
- *Cập nhật không gián đoạn* = đổi mong muốn từ từ

Bạn sẽ gặp lại đúng khuôn này ở ArgoCD (Ngày 43), Ansible (47) và Terraform (48).

</details>

<details>
<summary><b>2. Vì sao thực tế gần như không ai tạo Pod trần?</b></summary>

Vì **không ai 'mong muốn' nó tồn tại cả**. Bạn bảo tạo thì K8s tạo; pod chết thì thôi, không có gì tạo lại.

Deployment thì khác: nó khai `replicas: 3` là một *trạng thái mong muốn*, và vòng điều hoà sẽ giữ đúng con số đó. Giết pod bao nhiêu lần cũng có pod mới thay thế trong vài giây.

Pod là **đồ dùng một lần** — đừng chăm sóc pod, hãy mô tả cái bạn muốn có.

</details>

<details>
<summary><b>3. Ai đó `kubectl scale` lên 10 pod lúc nửa đêm để chữa cháy nhưng không sửa file YAML. Chuyện gì xảy ra sau đó?</b></summary>

Con số 10 tồn tại cho tới lần `kubectl apply` tiếp theo — có thể là **vài tuần sau**, khi không ai còn nhớ. Lúc đó nó âm thầm quay về con số trong file, **sự cố tái diễn, và không ai hiểu vì sao**.

Hiện tượng này gọi là **trôi cấu hình** (configuration drift). File YAML là nguồn sự thật; lệnh gõ tay chỉ là sửa tạm.

Đây chính là vấn đề mà GitOps (Ngày 43) sinh ra để giải quyết — ở đó, sửa tay sẽ bị **tự động hoàn tác trong 30 giây**.

</details>

### 📚 Thuật ngữ Anh–Việt (ngày này)

| Thuật ngữ | Nghĩa |
|---|---|
| **Declarative** | Khai báo trạng thái mong muốn, không ra lệnh từng bước |
| **Vòng điều hoà (reconciliation loop)** | So mong muốn với thực tế rồi sửa cho khớp — gốc của mọi tính năng K8s |
| **Control Plane** | Ban giám đốc cluster: API Server, etcd, Scheduler, Controller Manager |
| **etcd** | Sổ cái lưu toàn bộ trạng thái cluster — mất etcd là cluster mất trí nhớ |
| **kubelet** | Tổ trưởng trên mỗi node: nhận lệnh từ API Server, bảo runtime chạy container |
| **Pod** | Đơn vị nhỏ nhất K8s quản lý; **đồ dùng một lần**, chết là thay cái mới |
| **Namespace** | Ranh giới chia ngăn cluster — dùng cho quota và phân quyền RBAC |
| **Configuration drift** | Thực tế trôi khỏi file khai báo, thường do ai đó sửa tay |

### 🎯 Đúc kết Ngày 36

**3 điều phải mang theo:**

1. **Khai báo, không ra lệnh.** Bạn mô tả trạng thái mong muốn vào YAML; K8s tự làm cho khớp và **giữ mãi**. File YAML là nguồn sự thật, không phải lệnh bạn gõ tay.
2. **Mọi phép màu chỉ là một vòng lặp** so mong muốn với thực tế rồi sửa. Tự phục hồi, tự mở rộng, cập nhật không gián đoạn — cùng một cơ chế.
3. **Pod là đồ dùng một lần.** Đừng chăm sóc pod; hãy mô tả đúng cái bạn muốn có và để Deployment lo phần thay thế.

> 🧠 **Một câu để nhớ:** Kubernetes không chạy container giùm bạn — nó **liên tục sửa cho thực tế khớp với điều bạn đã khai**.

**✅ Tự chấm** *(đánh dấu khi làm được mà không nhìn tài liệu):*

- [ ] Dựng được cluster local và giải thích `kubectl` nói chuyện với thành phần nào
- [ ] Kể tên 4 thành phần control plane và nhìn thấy chúng bằng `kubectl get pods -n kube-system`
- [ ] Giải thích vòng điều hoà bằng lời của mình
- [ ] Chứng minh Pod trần không tự hồi sinh còn Deployment thì có
- [ ] Giết pod và giải thích vì sao pod mới xuất hiện sau 2 giây
- [ ] Nói được vì sao `kubectl scale` bằng tay là nguy hiểm nếu không sửa file
- [ ] Dùng đúng thứ tự điều tra: `describe` → `logs` → `events`

✅ **Kết quả đạt được:** Một cluster Kubernetes chạy trên máy bạn, và quan trọng hơn — bạn đã tận mắt thấy cơ chế tự phục hồi hoạt động, nền tảng cho mọi thứ học trong 14 ngày tới.

---

## Ngày 37 — Kubernetes: Pod, Deployment & ReplicaSet

> ⏱️ ~90 phút · Loại: Kubernetes
>
> 🧭 **Bạn đang ở đâu:** Ngày 36 (kiến trúc K8s + pod đầu tiên) → **Ngày 37 (chạy app bằng Deployment)** → Ngày 38 (Service — cho app nhận request từ ngoài). Hôm nay bạn học cách *chạy và cập nhật ứng dụng đúng chuẩn*.
>
> ✅ **Chuẩn bị trước khi làm:** cluster local đã chạy từ Ngày 36 (`minikube start`) và `kubectl get nodes` trả về STATUS `Ready`. Nếu chưa, quay lại Ngày 36.

### 📘 Lý thuyết

#### 1. Ba lớp: Pod → ReplicaSet → Deployment

Đây là kiến thức xương sống của K8s. Ba đối tượng này **lồng nhau như búp bê Nga**, mỗi lớp thêm một khả năng:

| Đối tượng | Là gì | Khả năng thêm vào | Bạn có tự tạo không? |
|---|---|---|---|
| **Pod** | Đơn vị nhỏ nhất K8s chạy được, bọc 1 (hoặc vài) container dùng chung mạng + ổ đĩa | Không có gì thêm — chạy trần | ❌ Hầu như không bao giờ |
| **ReplicaSet** | Bộ điều khiển giữ "luôn có đúng **N** pod giống nhau" | **Self-healing** + **scaling** | ❌ Rất hiếm (để Deployment lo) |
| **Deployment** | Bộ điều khiển quản lý ReplicaSet | **Rolling update** + **rollback** | ✅ **Đây là thứ bạn dùng 99% thời gian** |

Khi bạn tạo 1 **Deployment**, chuỗi tự động diễn ra: **Deployment** tạo ra **ReplicaSet**, **ReplicaSet** tạo ra các **Pod**. Bạn chỉ khai báo lớp trên cùng.

```
Bạn khai báo:   Deployment (web, replicas=3)
                      │  tạo & quản lý
                      ▼
                 ReplicaSet (web-7d9f, giữ đúng 3 pod)
                      │  tạo & quản lý
          ┌───────────┼───────────┐
          ▼           ▼           ▼
        Pod web-a   Pod web-b   Pod web-c   ← nơi container thật sự chạy
```

#### 2. Vì sao KHÔNG bao giờ tạo Pod trần

Một Pod tạo trực tiếp (không qua Deployment) chết là **mất vĩnh viễn** — không ai tạo lại. ReplicaSet mới là "người canh gác": nó liên tục đếm pod, thiếu thì tạo bù. Đây chính là **self-healing**. Vì thế quy tắc vàng: *luôn bọc Pod trong một Deployment*.

#### 3. Cấu trúc một manifest (file YAML khai báo)

Mọi đối tượng K8s đều có **4 khối bắt buộc**. Hiểu 4 khối này là đọc được mọi YAML:

| Khối | Ý nghĩa | Ví dụ |
|---|---|---|
| `apiVersion` | Phiên bản API dùng để hiểu đối tượng | `apps/v1` (cho Deployment) |
| `kind` | Loại đối tượng | `Deployment`, `Pod`, `Service`... |
| `metadata` | Tên + nhãn (label) để nhận diện | `name: web`, `labels: {app: web}` |
| `spec` | **Trạng thái mong muốn** — mô tả bạn muốn gì | replicas, image, ports... |

#### 4. Label & Selector — "keo dán" gắn các đối tượng

- **Label** = cái nhãn dán tùy ý lên đối tượng, dạng `key: value` (vd `app: web`).
- **Selector** = câu điều kiện "chọn mọi đối tượng có nhãn này".

Deployment dùng `selector.matchLabels` để biết *"những Pod nào là của tôi"*. Đây cũng là cách Service (Ngày 38) và hệ thống monitoring tìm đúng Pod. **Nhãn ở `selector` phải khớp y hệt nhãn trong `template.metadata.labels`** — sai chỗ này là lỗi kinh điển của người mới.

#### 5. Rolling update — cập nhật không downtime

Khi đổi phiên bản image, K8s **không tắt hết rồi bật lại** (sẽ downtime). Nó thay **từng Pod một**: dựng Pod mới → chờ khỏe → xóa Pod cũ → lặp lại. Luôn còn Pod phục vụ → người dùng không thấy gián đoạn. Hai "van" điều khiển tốc độ:

- `maxSurge`: được phép tạo thừa tối đa bao nhiêu Pod so với mong muốn (vd `1` = tạo trước 1 pod mới).
- `maxUnavailable`: được phép thiếu tối đa bao nhiêu Pod (vd `0` = không bao giờ thiếu → zero-downtime tuyệt đối).

Về mặt cơ chế: mỗi lần đổi image, Deployment tạo một **ReplicaSet mới**, tăng dần pod ở RS mới và giảm dần pod ở RS cũ. Vì RS cũ vẫn còn đó (chỉ scale về 0), nên **rollback = bật lại RS cũ** → nhanh trong vài giây: `kubectl rollout undo`.

#### 6. Scaling — co giãn bằng một con số

`kubectl scale deployment web --replicas=5` chỉ đổi con số `replicas`. ReplicaSet thấy 3≠5 → tạo thêm 2 pod. Đây là nền tảng của autoscaling (Ngày 41).

#### 7. Manifest Deployment tối thiểu (đọc để hình dung, sẽ dùng ở Lab)

```yaml
apiVersion: apps/v1          # Deployment thuộc nhóm API "apps"
kind: Deployment
metadata:
  name: web                  # tên Deployment
  labels:
    app: web
spec:
  replicas: 3                # MUỐN có 3 pod
  selector:
    matchLabels:
      app: web               # "pod của tôi là pod có nhãn app=web"
  template:                  # ← khuôn để đúc ra từng Pod
    metadata:
      labels:
        app: web             # PHẢI khớp selector ở trên
    spec:
      containers:
        - name: web
          image: nginx:1.27  # dùng tag cụ thể, KHÔNG dùng :latest
          ports:
            - containerPort: 80
```

> 🔑 Để ý: từ `template:` trở xuống chính là "định nghĩa một Pod". Deployment = "khuôn đúc Pod (`template`)" + "muốn bao nhiêu cái (`replicas`)" + "nhận diện chúng bằng nhãn nào (`selector`)".

### 📖 Hiểu rõ hơn (giải thích cho người mới)

> Phần 📘 ở trên đã liệt kê "cái gì". Mục này cho bạn **một hình dung để nhớ** — không lặp lại bảng.

**Ba lớp giống một cây quản lý theo cấp.** **Deployment** là sếp đặt chính sách: *"luôn có 3 người trực, và khi đổi ca thì thay từ từ"*. **ReplicaSet** là tổ trưởng chỉ chăm chăm đếm đầu người: thiếu một là gọi thêm cho đủ. **Pod** là nhân viên làm việc thật. Cái hay là bạn **chỉ nói chuyện với sếp** (khai Deployment) — tổ trưởng và nhân viên tự sinh ra và tự vận hành theo chính sách đó.

**Rolling update như thay lốp xe khi xe vẫn đang chạy.** Thay vì dừng xe (tắt hết → downtime), K8s thay từng bánh một: lắp bánh mới, chắc nó ăn đường rồi mới tháo bánh cũ, cứ thế. `maxUnavailable: 0` nghĩa là "không lúc nào được thiếu bánh". Và vì bánh cũ (ReplicaSet cũ) vẫn để trong cốp, hỏng giữa chừng thì `rollout undo` lắp lại ngay — rollback tính bằng giây.

**Vì sao Pod "trần" lại nguy hiểm.** Pod tạo trực tiếp không có ai "đếm đầu người" phía trên: nó chết là mất hẳn, không mọc lại. Deployment cho bạn self-healing + rolling update + rollback gần như **miễn phí** — chỉ tốn thêm vài dòng YAML để khai `replicas` và `selector`. Đây là lý do ngoài thực tế gần như không ai chạy Pod trần.

### 🧪 Lab cơ bản

> Mục tiêu: tự tay tạo Deployment 3 pod, scale, rolling update và rollback. Dùng image `nginx` có sẵn nên **không cần build gì**.

**Bước 1 — Tạo thư mục làm việc và file manifest.**
```bash
mkdir -p ~/k8s-lab/ngay37 && cd ~/k8s-lab/ngay37
nano deployment.yaml
```
Dán **toàn bộ** nội dung sau vào file (đây là file hoàn chỉnh, copy-chạy được ngay):
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: web
  labels:
    app: web
spec:
  replicas: 3
  selector:
    matchLabels:
      app: web
  template:
    metadata:
      labels:
        app: web
    spec:
      containers:
        - name: web
          image: nginx:1.27
          ports:
            - containerPort: 80
```
Lưu lại: `Ctrl+O` → `Enter` → `Ctrl+X`.

**Bước 2 — Áp dụng file lên cluster.**
```bash
kubectl apply -f deployment.yaml
```

**Bước 3 — Xem kết quả.**
```bash
kubectl get deployments
kubectl get pods
```

**Bước 4 — Scale lên 5 rồi xuống 2.**
```bash
kubectl scale deployment web --replicas=5
kubectl get pods          # đếm lại số pod
kubectl scale deployment web --replicas=2
```

**Bước 5 — Rolling update: đổi phiên bản image.**
```bash
kubectl set image deployment/web web=nginx:1.28
kubectl rollout status deployment/web
```

**Bước 6 — Rollback về bản trước.**
```bash
kubectl rollout undo deployment/web
kubectl rollout status deployment/web
```

**Bước 7 — Dọn dẹp (để làm lại từ đầu nếu muốn).**
```bash
kubectl delete -f deployment.yaml
```

### 🚀 Lab nâng cao (best-practice)

> Mục tiêu: viết một Deployment **chuẩn production** — chiến lược rolling update zero-downtime, label chuẩn hoá, và tự quan sát K8s tự chữa lành (self-healing).

**Bước 1 — Tạo manifest production.** Tạo file `deployment-prod.yaml` với **đầy đủ 4 khối** (khác lab cơ bản ở khối `strategy` và bộ label chuẩn):
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: web
  labels:
    app.kubernetes.io/name: web        # bộ label khuyến nghị của K8s
    app.kubernetes.io/version: "1.27"
spec:
  replicas: 3
  strategy:
    type: RollingUpdate
    rollingUpdate:
      maxSurge: 1            # tạo dư tối đa 1 pod khi update
      maxUnavailable: 0      # KHÔNG bao giờ thiếu pod → zero-downtime
  selector:
    matchLabels:
      app.kubernetes.io/name: web
  template:
    metadata:
      labels:
        app.kubernetes.io/name: web    # PHẢI khớp selector
        app.kubernetes.io/version: "1.27"
    spec:
      containers:
        - name: web
          image: nginx:1.27            # tag cụ thể, KHÔNG dùng :latest
          ports:
            - containerPort: 80
```
```bash
kubectl apply -f deployment-prod.yaml
```

**Bước 2 — Quan sát rolling update zero-downtime.** Mở **2 cửa sổ terminal**:
- Terminal A (theo dõi liên tục): `kubectl get pods -w`
- Terminal B (kích hoạt update): `kubectl set image deployment/web web=nginx:1.28`

Nhìn Terminal A: pod mới `ContainerCreating` → `Running` **rồi** pod cũ mới `Terminating`. Nhờ `maxUnavailable: 0`, luôn đủ 3 pod phục vụ.

**Bước 3 — Thử nghiệm rollback khi update hỏng.** Cố tình đặt tag sai:
```bash
kubectl set image deployment/web web=nginx:khong-ton-tai
kubectl get pods            # pod mới kẹt ở ImagePullBackOff, pod cũ VẪN chạy
kubectl rollout undo deployment/web   # cứu về bản tốt
```

**Bước 4 — Kiểm chứng self-healing.** Xoá tay một pod và xem ReplicaSet tạo lại:
```bash
kubectl get pods
kubectl delete pod <tên-một-pod>      # thay bằng tên thật ở lệnh trên
kubectl get pods                      # thấy pod mới xuất hiện thay thế
```

**Nguyên tắc production rút ra:**
- **Luôn dùng tag bất biến** (số phiên bản hoặc SHA), không dùng `:latest` — `latest` khiến rolling update và rollback không đoán trước được.
- **`maxUnavailable: 0`** cho dịch vụ cần zero-downtime.
- **Bộ label chuẩn** `app.kubernetes.io/*` để Service (Ngày 38) và monitoring (Ngày 44) chọn đúng pod.
- Bộ lệnh `kubectl rollout` để kiểm soát vòng đời triển khai:
  ```bash
  kubectl rollout status  deployment/web   # theo dõi tiến trình update
  kubectl rollout history deployment/web   # xem lịch sử các bản
  kubectl rollout undo    deployment/web   # rollback bản gần nhất
  ```

### 💡 Bổ sung thực tế: những cái đi làm mới thấm

- **Rollback nhanh vì ReplicaSet cũ *được giữ lại*:** `rollout undo` không build hay kéo gì mới — nó chỉ scale ReplicaSet cũ lên và ReplicaSet mới xuống. K8s giữ ~10 bản gần nhất (`revisionHistoryLimit`), đó là lý do rollback tính bằng giây.
- **`maxSurge`/`maxUnavailable` là đánh đổi tốc độ ↔ an toàn:** `maxUnavailable: 0` + `maxSurge: 1` cho zero-downtime nhưng cần dư tài nguyên cho pod thứ N+1; muốn update nhanh hơn thì tăng `maxSurge`, chấp nhận tốn RAM/CPU tạm thời.
- **Rolling update "thành công" vẫn có thể làm user lỗi — nếu thiếu readiness probe:** không có probe, K8s coi pod "sẵn sàng" ngay khi container *khởi động*, rồi dịch traffic vào dù app chưa nạp xong → thỉnh thoảng 502. Luôn kèm **readiness probe** (Ngày 41) để rolling update thật sự an toàn.
- **`kubectl set image` gây "config drift":** đổi image bằng lệnh thì file YAML trong Git *không* đổi → lần `apply` sau sẽ kéo về bản cũ. Ở production, sửa YAML rồi `apply` — đừng dùng lệnh imperative để đổi trạng thái lâu dài.
- **Deployment chỉ hợp app *stateless*:** mọi pod của Deployment là bản sao ngang hàng, thay thế lẫn nhau. App có trạng thái/danh tính riêng (database, hàng đợi) cần **StatefulSet** (Ngày 39) — đừng nhồi database vào Deployment.

### 🧭 Hướng dẫn làm lab & giải nghĩa lệnh (cho người tự học)

> Làm **tuần tự từng bước**. Sau mỗi bước, đối chiếu với "Bạn sẽ thấy" và dừng lại ở dòng ✅ **Checkpoint** trước khi đi tiếp. Chưa qua checkpoint thì đừng vội sang bước sau.

**Bước 1 — Kiểm tra cluster đã sẵn sàng.**
```bash
kubectl get nodes
```
Bạn sẽ thấy (Minikube 1 node):
```
NAME       STATUS   ROLES           AGE   VERSION
minikube   Ready    control-plane   3d    v1.30.x
```
✅ **Checkpoint:** STATUS là `Ready`.
⚠️ Nếu lỗi `connection refused` hoặc không có node → cluster chưa chạy: `minikube start` rồi thử lại.

**Bước 2 — Tạo Deployment từ file.**
```bash
kubectl apply -f deployment.yaml
```
Bạn sẽ thấy:
```
deployment.apps/web created
```
✅ **Checkpoint:** có chữ `created`. (Chạy lại lệnh này lần 2 sẽ thấy `unchanged` — đó là bản chất *declarative*: áp dụng nhiều lần vẫn ra một kết quả.)

**Bước 3 — Xác nhận 3 pod đã chạy.**
```bash
kubectl get deployments
kubectl get pods
```
Bạn sẽ thấy:
```
NAME   READY   UP-TO-DATE   AVAILABLE   AGE
web    3/3     3            3           20s

NAME                   READY   STATUS    RESTARTS   AGE
web-7d9f8c6b5-2xk4p    1/1     Running   0          20s
web-7d9f8c6b5-8fq2m    1/1     Running   0          20s
web-7d9f8c6b5-lp9wz    1/1     Running   0          20s
```
✅ **Checkpoint:** Deployment `READY 3/3` và có đúng **3 pod** `Running`.
⚠️ Nếu pod kẹt ở `Pending`/`ContainerCreating` quá lâu → chạy `kubectl describe pod <tên>`, đọc mục **Events** ở cuối để biết lý do (thường là đang kéo image, chờ chút).
💡 *Vì sao tên pod có hậu tố lạ (`web-7d9f8c6b5-2xk4p`)?* `web-7d9f8c6b5` là tên **ReplicaSet** do Deployment sinh ra, `-2xk4p` là mã ngẫu nhiên của từng Pod. Bạn vừa nhìn thấy chuỗi Deployment → ReplicaSet → Pod bằng mắt thật.

**Bước 4 — Scale và quan sát.**
```bash
kubectl scale deployment web --replicas=5
kubectl get pods        # đếm: giờ phải là 5 pod
kubectl scale deployment web --replicas=2
kubectl get pods        # 3 pod dư bị xoá, còn 2
```
✅ **Checkpoint:** số pod thay đổi theo đúng con số `--replicas`.
💡 *Kết quả cho thấy:* bạn không tạo/xoá pod thủ công — chỉ đổi *mong muốn*, ReplicaSet tự điều chỉnh cho khớp.

**Bước 5 — Rolling update.**
```bash
kubectl set image deployment/web web=nginx:1.28
kubectl rollout status deployment/web
```
Bạn sẽ thấy:
```
Waiting for deployment "web" rollout to finish: 1 out of 2 new replicas have been updated...
deployment "web" successfully rolled out
```
✅ **Checkpoint:** dòng cuối là `successfully rolled out`.
💡 *Muốn thấy tận mắt "không downtime"?* Mở terminal thứ 2 chạy `kubectl get pods -w` **trước khi** gõ lệnh `set image` — bạn sẽ thấy pod mới lên `Running` rồi pod cũ mới `Terminating`.

**Bước 6 — Rollback.**
```bash
kubectl rollout history deployment/web   # xem có mấy revision
kubectl rollout undo deployment/web
kubectl rollout status deployment/web
```
✅ **Checkpoint:** rollout thành công, image quay về `nginx:1.27`. Kiểm chứng:
```bash
kubectl describe deployment web | grep -i image
```
💡 *Vì sao rollback nhanh vậy?* ReplicaSet cũ (chạy `1.27`) không bị xoá, chỉ bị scale về 0. `undo` = bật lại nó → vài giây, không cần kéo lại image.

**Bước 7 — Dọn dẹp.**
```bash
kubectl delete -f deployment.yaml
kubectl get pods        # danh sách trống dần rồi rỗng
```
✅ **Checkpoint:** không còn pod `web` nào.

---

**⚠️ Ba lỗi kinh điển của người mới ở ngày này:**
1. **Nhãn `selector` ≠ nhãn `template`** → `kubectl apply` báo lỗi `selector does not match template labels`. Hai chỗ nhãn PHẢI y hệt nhau.
2. **Tạo Pod trần** (`kind: Pod`) thay vì Deployment → pod chết là mất luôn, không self-healing.
3. **Dùng `image: nginx:latest`** → mỗi lần pull có thể ra bản khác nhau, rolling update/rollback không đoán trước được. Luôn ghi tag cụ thể.

💡 **Hiểu sâu để nhớ lâu:** mỗi lần bạn đổi image, Deployment **không sửa pod cũ** — nó tạo hẳn một **ReplicaSet mới**, rồi dịch dần số pod từ RS cũ sang RS mới (tăng bên mới, giảm bên cũ). Đó là lý do vừa *không downtime* (luôn còn pod phục vụ) vừa *rollback tức thì* (RS cũ vẫn nằm đó chờ được bật lại).

### 🐛 Gỡ lỗi nhanh (kỹ năng dùng cả đời làm K8s)

> Khi có gì đó "không chạy", **đừng đoán mò**. Luôn đi theo đúng 3 lệnh này, theo thứ tự — 90% sự cố lộ ra ngay.

**🔧 3 lệnh debug vạn năng:**
```bash
kubectl get pods                 # 1. NHÌN TỔNG QUAN: pod nào lỗi? STATUS gì?
kubectl describe pod <tên-pod>   # 2. TÌM NGUYÊN NHÂN: đọc mục "Events" ở CUỐI output
kubectl logs <tên-pod>           # 3. XEM APP NÓI GÌ: log bên trong container
```
Quy tắc: `get` để *thấy triệu chứng* → `describe` để *biết vì sao K8s không xếp/chạy được* (Events) → `logs` để *biết app tự chết vì lý do gì*.

**📋 Bảng lỗi thường gặp ở ngày này:**

| STATUS bạn thấy (`get pods`) | Nghĩa là gì | Nguyên nhân hay gặp | Cách sửa |
|---|---|---|---|
| `ImagePullBackOff` / `ErrImagePull` | Không kéo được image | Gõ sai tên/tag image, hoặc tag không tồn tại | Kiểm tra lại chính tả image; dùng tag có thật (vd `nginx:1.27`) |
| `CrashLoopBackOff` | Container khởi động rồi chết, lặp mãi | App lỗi khi chạy, thiếu config/biến môi trường | `kubectl logs <pod>` đọc lý do app chết |
| `Pending` (kẹt lâu) | Chưa được xếp lên node nào | Node hết CPU/RAM, hoặc cluster chưa Ready | `kubectl describe pod` đọc Events; kiểm tra `kubectl get nodes` |
| `apply` báo `selector does not match template labels` | Manifest sai | Nhãn ở `selector.matchLabels` ≠ nhãn ở `template.metadata.labels` | Sửa cho 2 chỗ nhãn **y hệt nhau** |
| `0/3` mãi không lên `3/3` | Pod không sẵn sàng | Thường là 1 trong các lỗi trên | Chạy 3 lệnh debug ở trên để truy nguyên |

### 📝 Bài ôn tập & Demo đối chiếu

**✍️ Tự kiểm tra (nghĩ câu trả lời rồi mới bấm xem đáp án):**

<details>
<summary>1. Giải thích chuỗi Deployment → ReplicaSet → Pod. Vì sao không tạo Pod trần?</summary>

> Bạn khai báo **Deployment**, nó tạo **ReplicaSet** (giữ đúng số pod), ReplicaSet tạo các **Pod** (chạy container). Không tạo Pod trần vì pod trần chết là mất luôn — không ai tạo lại; ReplicaSet mới có self-healing.
</details>

<details>
<summary>2. Rolling update giúp tránh điều gì, và nhờ tham số nào?</summary>

> Tránh **downtime** khi cập nhật. K8s thay từng pod một, luôn giữ đủ pod phục vụ. `maxUnavailable: 0` đảm bảo không bao giờ thiếu pod; `maxSurge` cho phép tạo dư pod mới trong lúc chuyển.
</details>

<details>
<summary>3. Viết lệnh scale deployment "web" lên 4 replica.</summary>

> `kubectl scale deployment web --replicas=4`
</details>

<details>
<summary>4. Thấy pod ở STATUS `ImagePullBackOff` thì làm gì đầu tiên?</summary>

> `kubectl describe pod <tên>` đọc mục Events — thường là gõ sai tên/tag image. Sửa lại tag cho đúng.
</details>

**🔬 Demo đối chiếu (làm xong phải khớp bảng này):**

| Demo đối chiếu | Kết quả mong đợi |
|---|---|
| Tạo Deployment | `kubectl get deploy` → READY 3/3 |
| Xem các Pod | `kubectl get pods` → tất cả Running |
| Thử xóa 1 pod | K8s tự tạo lại pod mới (self-healing) |
| Rolling update rồi rollback | `rollout status` → `successfully rolled out`, image quay về bản cũ |

### 📚 Thuật ngữ Anh–Việt (ngày này)

| Thuật ngữ | Nghĩa |
|---|---|
| **Replica** | Bản sao của pod. `replicas: 3` = muốn 3 bản sao giống nhau |
| **Rolling update** | Cập nhật cuốn chiếu, thay từng pod một để không downtime |
| **Rollback** | Quay về phiên bản trước khi bản mới lỗi |
| **Selector / Label** | Nhãn dán lên đối tượng + câu điều kiện chọn theo nhãn |
| **Manifest** | File YAML mô tả đối tượng K8s (trạng thái mong muốn) |
| **Self-healing** | K8s tự tạo lại pod khi pod chết, để luôn đủ số mong muốn |
| **Declarative** | Khai báo *cái muốn* (YAML), K8s tự lo *cách đạt* |

### 🎯 Đúc kết Ngày 37

**3 điều phải mang theo:**
1. **Chuỗi Deployment → ReplicaSet → Pod:** bạn chỉ khai Deployment, phần còn lại tự sinh. Đừng bao giờ tạo Pod trần.
2. **Rolling update thay từng pod** (`maxUnavailable: 0` = zero-downtime); **rollback = quay về ReplicaSet cũ** trong giây (`rollout undo`).
3. **Scale = đổi một con số** (`--replicas`), nhưng rolling update *an toàn* cần readiness probe (Ngày 41).

> 🧠 **Một câu để nhớ:** đừng bao giờ tạo Pod trần — luôn dùng **Deployment** để có self-healing + rolling update + rollback miễn phí.

**✅ Tự chấm** *(đánh dấu khi làm được mà không cần nhìn tài liệu):*
- [ ] Viết Deployment YAML (replicas / selector / template) và `apply`
- [ ] Scale lên/xuống bằng `kubectl scale`
- [ ] Rolling update đổi image + theo dõi `kubectl rollout status`
- [ ] Rollback bằng `rollout undo` và giải thích vì sao nó nhanh
- [ ] Giải thích chuỗi Deployment → ReplicaSet → Pod qua tên pod

✅ **Kết quả đạt được:** Triển khai và scale ứng dụng bằng Deployment, rolling update & rollback an toàn, và biết dùng 3 lệnh debug + bảng lỗi để tự gỡ sự cố.

---

## Ngày 38 — Kubernetes: Service & Networking

> ⏱️ ~90 phút · Loại: Kubernetes
>
> 🧭 **Bạn đang ở đâu:** Ngày 37 (Deployment chạy nhiều bản sao) → **Ngày 38 (làm sao gọi tới chúng — Service, DNS, Ingress)** → Ngày 39 (ConfigMap, Secret, lưu trữ). Hôm qua bạn có 3 pod nhưng chưa ai vào được; hôm nay mở đường.
>
> ✅ **Chuẩn bị:** cluster đang chạy (`minikube start`) và `kubectl get nodes` ra `Ready`.
>
> 🎁 **Cuối ngày bạn có gì:** một app truy cập được bằng **tên miền** thật (`shop.local`) qua Ingress, hiểu rõ khi nào dùng ClusterIP / NodePort / Ingress — và tự chứng minh được vì sao **không bao giờ gọi pod bằng IP**.

### 📘 Lý thuyết

#### 1. Vấn đề: IP của pod biến mất liên tục

Ngày 36 bạn đã thấy `kubectl get pods -o wide` hiện IP từng pod, ví dụ `10.244.0.5`. Cám dỗ đầu tiên là dùng luôn IP đó để gọi. Đừng.

Pod là đồ dùng một lần: nó chết, bản mới sinh ra với **IP hoàn toàn khác**. Mà pod chết thì xảy ra suốt: cập nhật phiên bản, node bảo trì, tự mở rộng, hết RAM. Ghi IP pod vào cấu hình là tự đặt bom hẹn giờ.

Thêm nữa: có **3 pod** thì gọi cái nào? Ai chia đều tải?

**Service** giải quyết cả hai: nó là **một địa chỉ cố định đứng trước một nhóm pod hay thay đổi**, và tự chia đều yêu cầu cho các pod còn sống.

```text
                    ┌──────────────┐
  Người gọi  ───>   │   Service    │  tên: web-svc, IP không đổi
                    │  (cửa trước) │
                    └──────┬───────┘
                     chia đều tải
              ┌────────────┼────────────┐
              ▼            ▼            ▼
           Pod A        Pod B        Pod C     ← IP thay đổi liên tục, không sao cả
```

#### 2. Service tìm pod bằng nhãn, không bằng IP

Đây là ý tưởng thanh lịch nhất của Kubernetes. Service không giữ danh sách IP nào cả. Nó chỉ khai:

```yaml
selector:
  app: web        # "khách hàng của tôi là MỌI pod mang nhãn app=web"
```

Pod mới sinh ra mang nhãn `app: web` → **tự động** được nhận vào nhóm. Pod chết → tự động bị loại. Không ai phải cập nhật danh sách gì hết.

> ⚠️ **Lỗi số một khi làm việc với Service:** `selector` của Service không khớp `labels` của pod → Service không tìm thấy ai, gọi vào là treo hoặc lỗi kết nối. Bước 4 phần thực hành sẽ dạy bạn cách phát hiện chỉ trong 5 giây.

#### 3. Ba loại Service — chọn đúng loại

| Loại | Ai gọi được | Dùng khi nào |
|---|---|---|
| **ClusterIP** *(mặc định)* | **Chỉ bên trong cluster** | Backend, database, mọi dịch vụ nội bộ — **90% trường hợp** |
| **NodePort** | Bên ngoài, qua `IP-của-node:30000-32767` | Thử nghiệm, lab. Cổng xấu, khó quản |
| **LoadBalancer** | Bên ngoài, qua IP công cộng | Production trên cloud (cloud tự cấp bộ cân bằng tải, **có tính phí**) |

> 🔑 Quy tắc thực tế: **mặc định luôn dùng ClusterIP**. Chỉ mở ra ngoài đúng những gì cần mở, và mở qua **Ingress** (mục 5) thay vì cấp cho mỗi dịch vụ một LoadBalancer riêng.

#### 4. DNS nội bộ — gọi nhau bằng tên

Cluster có sẵn máy chủ DNS riêng (chính là pod `coredns` bạn thấy ở Ngày 36). Nhờ nó, mọi Service đều có một cái **tên** gọi được:

```text
web-svc                          ← cùng namespace, gọi ngắn gọn thế này
web-svc.default                  ← nói rõ namespace
web-svc.default.svc.cluster.local ← tên đầy đủ
```

Nghĩa là trong code backend, bạn viết `http://api-svc:8080` — **không IP, không cấu hình, không cần biết pod nằm đâu**. Đây là thứ khiến kiến trúc nhiều dịch vụ trên K8s trở nên dễ chịu.

#### 5. Ingress — một cửa vào cho tất cả

Có 10 dịch vụ cần mở ra Internet. Cấp 10 LoadBalancer? Đắt và rối.

**Ingress** là **một cửa duy nhất** biết định tuyến theo tên miền và đường dẫn:

```text
                          ┌─────────────────────┐
  shop.local/       ───>  │                     │ ───>  Service web
  shop.local/api    ───>  │  Ingress Controller │ ───>  Service api
  blog.local/       ───>  │   (một cửa vào)     │ ───>  Service blog
                          └─────────────────────┘
```

Nó cũng là nơi tập trung lo **HTTPS/chứng chỉ** — thay vì cấu hình TLS ở từng dịch vụ.

> 📌 **Phân biệt hai thứ hay bị lẫn:** *Ingress* chỉ là **tờ khai luật định tuyến** (một object YAML). *Ingress Controller* mới là **phần mềm thật sự chạy** và thực thi các luật đó (thường là nginx). Khai Ingress mà chưa cài Controller thì **không có gì xảy ra cả** — đây là bẫy kinh điển của người mới.

### 🧪 LAB — Từ pod kín tới tên miền truy cập được

**File sẽ tạo:**

```text
lab38-network/
├── app-web.yaml        # Deployment + Service ClusterIP (trang chủ)
├── app-api.yaml        # Deployment + Service ClusterIP (dịch vụ thứ hai)
└── ingress.yaml        # Luật định tuyến theo tên miền/đường dẫn
```

#### File 1 — `app-web.yaml`

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: web
spec:
  replicas: 3
  selector:
    matchLabels:
      app: web
  template:
    metadata:
      labels:
        app: web                      # nhãn này là thứ Service sẽ tìm
    spec:
      containers:
        - name: web
          image: nginx:1.27
          ports:
            - containerPort: 80
          resources:
            requests:
              memory: "64Mi"
              cpu: "50m"
            limits:
              memory: "128Mi"
          # Ghi tên pod vào trang chủ để LÁT NỮA THẤY RÕ việc chia tải
          command: ["/bin/sh", "-c"]
          args:
            - echo "Xin chào từ pod $HOSTNAME" > /usr/share/nginx/html/index.html
              && nginx -g 'daemon off;'
          env:
            - name: HOSTNAME
              valueFrom:
                fieldRef:
                  fieldPath: metadata.name
---
apiVersion: v1
kind: Service
metadata:
  name: web-svc
spec:
  type: ClusterIP                     # mặc định — chỉ gọi được từ trong cluster
  selector:
    app: web                          # PHẢI khớp labels của pod ở trên
  ports:
    - port: 80                        # cổng của Service (người khác gọi vào đây)
      targetPort: 80                  # cổng của container
```

#### File 2 — `app-api.yaml`

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: api
spec:
  replicas: 2
  selector:
    matchLabels:
      app: api
  template:
    metadata:
      labels:
        app: api
    spec:
      containers:
        - name: api
          image: hashicorp/http-echo:1.0    # image nhỏ, trả về đúng một chuỗi
          args:
            - "-text=Đây là dịch vụ API"
            - "-listen=:5678"
          ports:
            - containerPort: 5678
          resources:
            requests:
              memory: "16Mi"
              cpu: "20m"
            limits:
              memory: "64Mi"
---
apiVersion: v1
kind: Service
metadata:
  name: api-svc
spec:
  type: ClusterIP
  selector:
    app: api
  ports:
    - port: 8080          # bên ngoài gọi cổng 8080...
      targetPort: 5678    # ...Service chuyển tới cổng 5678 của container
```

#### File 3 — `ingress.yaml`

```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: cong-vao
  annotations:
    nginx.ingress.kubernetes.io/rewrite-target: /
spec:
  ingressClassName: nginx
  rules:
    - host: shop.local                # truy cập bằng tên miền này
      http:
        paths:
          - path: /api                # shop.local/api  -> api-svc
            pathType: Prefix
            backend:
              service:
                name: api-svc
                port:
                  number: 8080
          - path: /                   # shop.local/     -> web-svc
            pathType: Prefix
            backend:
              service:
                name: web-svc
                port:
                  number: 80
```

> 📌 Thứ tự `paths` có ý nghĩa: đường dẫn **cụ thể hơn phải đứng trước**. Để `/` lên đầu thì nó nuốt hết mọi yêu cầu, `/api` không bao giờ tới lượt.

### 🧭 Hướng dẫn làm LAB — step by step

#### Bước 1 — Chứng minh vì sao không được dùng IP pod

```bash
mkdir -p ~/lab38-network && cd ~/lab38-network
# tạo app-web.yaml theo phần LAB
kubectl apply -f app-web.yaml
kubectl get pods -o wide
```

Ghi lại IP của một pod bất kỳ, rồi giết nó:

```bash
POD=$(kubectl get pods -l app=web -o jsonpath='{.items[0].metadata.name}')
kubectl get pod $POD -o jsonpath='{.status.podIP}'; echo      # IP cũ
kubectl delete pod $POD
sleep 5
kubectl get pods -l app=web -o wide
```

**Bạn sẽ thấy:** pod mới có **IP hoàn toàn khác** IP bạn vừa ghi.

✅ **Checkpoint:** tự mắt thấy IP pod là thứ không bền.

💡 Giờ hãy tưởng tượng bạn đã ghi IP cũ đó vào cấu hình backend. Ứng dụng sẽ chết vào đúng lần cập nhật tiếp theo — và vào lúc 3 giờ sáng thì rất khó đoán ra nguyên nhân.

#### Bước 2 — Service: địa chỉ không bao giờ đổi

Service đã nằm sẵn trong `app-web.yaml`. Xem nó:

```bash
kubectl get svc web-svc
kubectl get endpoints web-svc
```

**Bạn sẽ thấy:**
```text
NAME      TYPE        CLUSTER-IP      PORT(S)   AGE
web-svc   ClusterIP   10.102.33.178   80/TCP    1m

NAME      ENDPOINTS
web-svc   10.244.0.11:80,10.244.0.12:80,10.244.0.13:80
```

✅ **Checkpoint:** `ENDPOINTS` liệt kê đúng **3 địa chỉ** — chính là 3 pod đang sống.

💡 **`kubectl get endpoints` là lệnh chẩn đoán quan trọng nhất về Service.** Nó trả lời: *"Service này có thực sự tìm thấy pod nào không?"* Danh sách trống nghĩa là selector sai — và đó là nguyên nhân của phần lớn lỗi "gọi Service không được".

#### Bước 3 — Gọi Service từ bên trong cluster và thấy chia tải

ClusterIP chỉ gọi được từ trong cluster, nên ta tạo một pod tạm để đứng bên trong mà gọi ra:

```bash
kubectl run thu-nghiem --rm -it --image=curlimages/curl:8.11.0 --restart=Never -- sh
```

Bên trong pod đó, gõ:

```sh
for i in 1 2 3 4 5 6; do curl -s http://web-svc; done
exit
```

**Bạn sẽ thấy:**
```text
Xin chào từ pod web-5d9f7c8b6-k2xqp
Xin chào từ pod web-5d9f7c8b6-vv8qr
Xin chào từ pod web-5d9f7c8b6-t7m3n
Xin chào từ pod web-5d9f7c8b6-k2xqp
...
```

✅ **Checkpoint:** tên pod **thay đổi giữa các lần gọi** — Service đang chia đều tải thật.

💡 Chú ý bạn gọi bằng **`http://web-svc`**, không phải IP. Đó là DNS nội bộ của cluster đang làm việc. Trong code ứng dụng thật, bạn cũng viết đúng như vậy.

#### Bước 4 — Cố ý làm sai selector để học cách chẩn đoán

Đây là lỗi bạn chắc chắn sẽ gặp, nên hãy gặp nó **ngay bây giờ, có chủ đích**:

```bash
kubectl patch svc web-svc -p '{"spec":{"selector":{"app":"web-sai-ten"}}}'
kubectl get endpoints web-svc
```

**Bạn sẽ thấy:**
```text
NAME      ENDPOINTS
web-svc   <none>            ← không tìm thấy pod nào!
```

✅ **Checkpoint:** `ENDPOINTS` là `<none>`.

💡 **Ghi nhớ phản xạ này:** khi "gọi Service mà không được", đừng đoán — chạy `kubectl get endpoints <ten-svc>`. Thấy `<none>` là biết ngay: selector của Service không khớp labels của pod. So hai bên bằng:
```bash
kubectl get svc web-svc -o jsonpath='{.spec.selector}'; echo
kubectl get pods --show-labels | head -3
```

Sửa lại cho đúng:
```bash
kubectl patch svc web-svc -p '{"spec":{"selector":{"app":"web"}}}'
kubectl get endpoints web-svc        # 3 địa chỉ trở lại
```

#### Bước 5 — Dịch vụ nói chuyện với dịch vụ

Triển khai dịch vụ thứ hai và gọi chéo:

```bash
# tạo app-api.yaml theo phần LAB
kubectl apply -f app-api.yaml
kubectl get pods -l app=api

kubectl run thu-nghiem --rm -it --image=curlimages/curl:8.11.0 --restart=Never -- sh
```

Bên trong:
```sh
curl -s http://api-svc:8080        # gọi dịch vụ khác bằng TÊN
nslookup api-svc                   # xem DNS cluster phân giải ra gì
exit
```

**Bạn sẽ thấy:**
```text
Đây là dịch vụ API

Name:   api-svc.default.svc.cluster.local
Address: 10.108.71.24
```

✅ **Checkpoint:** gọi được dịch vụ khác bằng tên, và DNS trả về tên đầy đủ `.default.svc.cluster.local`.

💡 Chú ý cổng: bạn gọi `:8080` nhưng container thật sự nghe ở `:5678`. Service đã dịch giúp (`port` → `targetPort`). Nhờ vậy đổi cổng bên trong app không ảnh hưởng người gọi.

#### Bước 6 — NodePort: mở ra ngoài kiểu thô sơ

```bash
kubectl expose deployment web --type=NodePort --port=80 --name=web-nodeport
kubectl get svc web-nodeport
```

**Bạn sẽ thấy:**
```text
NAME           TYPE       CLUSTER-IP     PORT(S)        AGE
web-nodeport   NodePort   10.98.44.201   80:31673/TCP   3s
```

Số `31673` là cổng được cấp trên node. Mở thử:

```bash
minikube service web-nodeport --url
curl -s $(minikube service web-nodeport --url)
```

**Bạn sẽ thấy:** `Xin chào từ pod web-...`.

✅ **Checkpoint:** truy cập được từ ngoài cluster.

💡 **Vì sao NodePort không dùng cho production:** cổng bị giới hạn trong dải 30000–32767 (không ai muốn địa chỉ web là `example.com:31673`), mỗi dịch vụ chiếm một cổng riêng trên **mọi** node, và không có HTTPS. Nó tiện cho lab, thế thôi.

```bash
kubectl delete svc web-nodeport
```

#### Bước 7 — Bật Ingress Controller

Nhớ mục Lý thuyết #5: khai Ingress mà chưa có Controller thì vô nghĩa. Bật trước:

```bash
minikube addons enable ingress
kubectl get pods -n ingress-nginx
```

**Bạn sẽ thấy** (chờ khoảng 1 phút):
```text
NAME                                      READY   STATUS      RESTARTS   AGE
ingress-nginx-controller-7d4b9f8c-x9k2m   1/1     Running     0          58s
```

✅ **Checkpoint:** pod controller ở trạng thái `Running` (không phải `Pending` hay `ContainerCreating`).

⚠️ Nếu mãi `ContainerCreating` — nó đang tải image, chờ thêm. Theo dõi: `kubectl get pods -n ingress-nginx -w`.

#### Bước 8 — Định tuyến theo tên miền

```bash
# tạo ingress.yaml theo phần LAB
kubectl apply -f ingress.yaml
kubectl get ingress
```

**Bạn sẽ thấy:**
```text
NAME       CLASS   HOSTS        ADDRESS          PORTS   AGE
cong-vao   nginx   shop.local   192.168.49.2     80      20s
```

✅ **Checkpoint:** cột `ADDRESS` **có IP** (chờ ~30 giây nếu đang trống).

Trỏ tên miền `shop.local` về cluster bằng file hosts của máy bạn:

```bash
echo "$(minikube ip) shop.local" | sudo tee -a /etc/hosts
cat /etc/hosts | tail -2
```

Giờ thử cả hai đường dẫn:

```bash
curl -s http://shop.local
curl -s http://shop.local/api
```

**Bạn sẽ thấy:**
```text
Xin chào từ pod web-5d9f7c8b6-k2xqp
Đây là dịch vụ API
```

✅ **Checkpoint:** cùng **một tên miền, một cổng 80**, nhưng hai đường dẫn đi tới hai dịch vụ khác nhau.

💡 **Đây chính là mô hình dùng ở production thật:** một cửa vào, định tuyến theo host/path, và cũng là nơi gắn chứng chỉ HTTPS (Module nâng cao — cert-manager). So với NodePort thì khác một trời một vực.

⚠️ **Nếu nhận `404 Not Found` từ nginx:** thường là sai `ingressClassName` hoặc Service không có endpoint. Kiểm tra theo thứ tự:
```bash
kubectl describe ingress cong-vao | tail -15     # xem phần Rules và Events
kubectl get endpoints web-svc api-svc            # cả hai phải có địa chỉ
```

#### Bước 9 — Nhìn toàn cảnh rồi dọn dẹp

```bash
kubectl get all
```

**Bạn sẽ thấy** đủ bộ: 5 pod, 3 service, 2 deployment, 2 replicaset — toàn bộ hệ thống nhỏ bạn vừa dựng.

Dọn dẹp:
```bash
kubectl delete -f ingress.yaml -f app-api.yaml -f app-web.yaml
sudo sed -i '/shop.local/d' /etc/hosts
minikube stop
```

⚠️ Nhớ xoá dòng trong `/etc/hosts` — để lại sẽ gây bối rối vào một ngày nào đó rất xa.

### 💡 Đi làm mới thấm (sách cơ bản hay bỏ quên)

- **`kubectl get endpoints` là bạn thân lúc sự cố.** Trước khi nghi ngờ mạng, firewall hay DNS, hãy hỏi câu đơn giản nhất: Service này có tìm thấy pod nào không? `<none>` trả lời được 70% ca "gọi không được".
- **Service chia tải ở tầng 4 (TCP), không phải tầng 7 (HTTP).** Nghĩa là nó không hiểu HTTP, không định tuyến theo đường dẫn, và với **kết nối giữ lâu** (gRPC, WebSocket, HTTP keep-alive) thì một kết nối dính chặt vào một pod — tải có thể lệch hẳn. Đây là lý do người ta cần Ingress hoặc service mesh (Ngày 54).
- **Headless Service (`clusterIP: None`) cho database.** Khi bạn cần gọi *đúng một bản* cụ thể (ví dụ node primary của cơ sở dữ liệu) thay vì bản ngẫu nhiên, Service thường không dùng được. Headless trả về IP của từng pod — đây là nền của StatefulSet.
- **Mỗi LoadBalancer trên cloud là một hoá đơn.** 10 dịch vụ mở kiểu `type: LoadBalancer` = 10 bộ cân bằng tải tính tiền theo giờ. Một Ingress đứng trước tất cả rẻ hơn rất nhiều — và đây là lỗi tốn tiền phổ biến của đội mới lên cloud.
- **NetworkPolicy mặc định KHÔNG bật.** Nhiều người tưởng namespace là bức tường bảo mật. Không phải: mặc định **mọi pod gọi được mọi pod**, kể cả khác namespace. Muốn chặn phải khai `NetworkPolicy` (và CNI phải hỗ trợ).
- **DNS trong cluster có bộ nhớ đệm.** Khi Service vừa đổi mà ứng dụng vẫn gọi vào địa chỉ cũ, thủ phạm thường là cache DNS phía client (nhiều thư viện HTTP tự cache). Không phải lúc nào cũng tại K8s.

### 📝 Tự kiểm tra

> Nghĩ câu trả lời **thành lời** trước khi mở đáp án — nghĩ thầm luôn thấy mình hiểu.

<details>
<summary><b>1. Vì sao tuyệt đối không gọi pod bằng IP của nó?</b></summary>

Vì pod là đồ dùng một lần: nó chết thì bản mới sinh ra với **IP hoàn toàn khác**. Mà pod chết xảy ra suốt — cập nhật phiên bản, node bảo trì, tự mở rộng, hết RAM.

Ghi IP pod vào cấu hình là tự đặt bom hẹn giờ: ứng dụng sẽ chết vào đúng lần cập nhật tiếp theo, và lúc 3 giờ sáng thì rất khó đoán nguyên nhân.

Gọi qua **Service** — một địa chỉ cố định đứng trước nhóm pod, và gọi bằng **tên** chứ không phải IP.

</details>

<details>
<summary><b>2. Gọi Service không được. Lệnh đầu tiên bạn chạy là gì, và nó trả lời câu hỏi gì?</b></summary>

```bash
kubectl get endpoints <ten-service>
```

Nó trả lời: *'Service này có tìm thấy pod nào không?'*

- Thấy danh sách IP → Service ổn, vấn đề ở chỗ khác (cổng, ứng dụng, mạng)
- Thấy **`<none>`** → **selector của Service không khớp labels của pod**

Trường hợp thứ hai là nguyên nhân của phần lớn ca 'gọi Service không được'. So hai bên bằng `kubectl get svc <svc> -o jsonpath='{.spec.selector}'` và `kubectl get pods --show-labels`.

</details>

<details>
<summary><b>3. Phân biệt Ingress và Ingress Controller. Khai Ingress mà chưa cài Controller thì sao?</b></summary>

**Ingress** chỉ là một **tờ khai luật định tuyến** — một object YAML, bản thân nó không làm gì cả.

**Ingress Controller** mới là **phần mềm thật sự chạy** (thường là nginx) đọc các tờ khai đó và thực thi.

Khai Ingress mà chưa cài Controller thì **không có gì xảy ra cả** — không báo lỗi, chỉ là truy cập không được và cột `ADDRESS` trống. Đây là bẫy kinh điển của người mới.

</details>

### 📚 Thuật ngữ Anh–Việt (ngày này)

| Thuật ngữ | Nghĩa |
|---|---|
| **Service** | Địa chỉ cố định đứng trước nhóm pod hay thay đổi; tự chia tải |
| **Selector / Label** | Service tìm pod bằng **nhãn**, không giữ danh sách IP |
| **Endpoints** | Danh sách IP pod mà Service tìm thấy — lệnh chẩn đoán số một |
| **ClusterIP** | Loại Service mặc định — chỉ gọi được từ trong cluster (90% trường hợp) |
| **NodePort** | Mở cổng 30000–32767 trên mọi node; tiện cho lab, không dùng production |
| **LoadBalancer** | Cloud cấp bộ cân bằng tải riêng — mỗi cái là một hoá đơn |
| **Ingress** | Tờ khai luật định tuyến theo tên miền/đường dẫn |
| **Ingress Controller** | Phần mềm thực thi các luật Ingress — **phải cài riêng** |
| **DNS nội bộ** | `web-svc.default.svc.cluster.local` — gọi dịch vụ bằng tên, không IP |
| **NetworkPolicy** | Luật giới hạn pod nào gọi được pod nào; **mặc định KHÔNG bật** |

### 🎯 Đúc kết Ngày 38

**3 điều phải mang theo:**

1. **Không bao giờ gọi pod bằng IP.** Gọi qua Service — một địa chỉ cố định đứng trước nhóm pod, tự chia tải, tự cập nhật thành viên qua **nhãn**.
2. **ClusterIP là mặc định, Ingress là cửa ra.** Giữ mọi thứ kín bên trong; chỉ mở ra ngoài qua một cửa duy nhất biết định tuyến theo tên miền/đường dẫn.
3. **Ingress là tờ khai, Ingress Controller là phần mềm thực thi.** Thiếu Controller thì khai bao nhiêu cũng không có gì xảy ra.

> 🧠 **Một câu để nhớ:** Service không giữ danh sách IP — nó giữ **một câu hỏi** ("pod nào mang nhãn này?") và hỏi lại liên tục. Nhờ vậy pod chết đi sống lại bao nhiêu lần cũng không ai phải sửa cấu hình.

**✅ Tự chấm** *(đánh dấu khi làm được mà không nhìn tài liệu):*

- [ ] Giải thích vì sao IP pod không dùng được, và chứng minh bằng thực nghiệm
- [ ] Viết Service ClusterIP có selector khớp đúng nhãn pod
- [ ] Dùng `kubectl get endpoints` để chẩn đoán Service không tìm thấy pod
- [ ] Gọi dịch vụ khác bằng tên DNS và giải thích `web-svc.default.svc.cluster.local`
- [ ] Phân biệt ClusterIP / NodePort / LoadBalancer và biết khi nào dùng cái nào
- [ ] Dựng Ingress định tuyến 2 đường dẫn về 2 dịch vụ trên cùng một tên miền
- [ ] Nói rõ khác biệt giữa Ingress và Ingress Controller

✅ **Kết quả đạt được:** Hệ thống hai dịch vụ gọi nhau bằng tên trong cluster, và mở ra ngoài qua một tên miền duy nhất — đúng mô hình mạng dùng ở production.

---

## Ngày 39 — Kubernetes: ConfigMap, Secret & Storage

> ⏱️ ~90 phút · Loại: Kubernetes
>
> 🧭 **Bạn đang ở đâu:** Ngày 38 (mạng — gọi được tới app) → **Ngày 39 (cấu hình, bí mật và dữ liệu không được phép mất)** → Ngày 40 (Milestone: ghép full-stack lên K8s). Đây là mảnh ghép cuối trước khi bạn chạy được một hệ thống thật có database.
>
> ✅ **Chuẩn bị:** cluster đang chạy (`minikube start`), đã quen `kubectl apply` (Ngày 36–38).
>
> 🎁 **Cuối ngày bạn có gì:** một app đọc cấu hình từ ConfigMap, mật khẩu từ Secret, và một database **giữ nguyên dữ liệu sau khi bạn xoá pod** — cộng một bài học bảo mật khiến bạn không bao giờ nhìn Secret của K8s như cũ nữa.

### 📘 Lý thuyết

#### 1. Vấn đề: cấu hình không được nằm trong image

Ngày 33 bạn đóng gói app thành image. Giả sử bạn nhét luôn địa chỉ database vào trong đó. Hậu quả:

- Muốn chạy bản staging trỏ database khác → **phải build image mới**.
- Đổi mật khẩu → **build lại image**.
- Ai kéo được image cũng **đọc được mật khẩu** bằng `docker history`.

Nguyên tắc nền tảng (điều số 3 của [12-Factor App](https://12factor.net/config)): **image là bất biến và giống nhau ở mọi môi trường; thứ khác nhau giữa các môi trường phải được tiêm vào lúc chạy**.

Kubernetes cho hai công cụ để tiêm:

| | **ConfigMap** | **Secret** |
|---|---|---|
| Chứa gì | Cấu hình thường: URL, cổng, tên miền, số lượng | Dữ liệu nhạy cảm: mật khẩu, token, khoá API |
| Lưu thế nào | Chữ thường, đọc được ngay | **Base64** — *chỉ là mã hoá dạng, KHÔNG phải mã hoá bảo mật* |
| Dùng thế nào | Hoàn toàn giống nhau: biến môi trường hoặc file |  |

#### 2. Sự thật quan trọng nhất về Secret

**Secret của Kubernetes mặc định KHÔNG được mã hoá.** Nó chỉ được mã hoá dạng base64 — thứ mà bất kỳ ai cũng giải ngược trong một giây.

Vậy nó khác ConfigMap chỗ nào? Ở ba điểm thực tế:

1. Không bị in ra màn hình khi `kubectl get` (đỡ lộ lúc chia sẻ màn hình).
2. Có thể **phân quyền RBAC riêng** — cho phép đọc ConfigMap nhưng cấm đọc Secret.
3. Có thể bật **mã hoá khi lưu trong etcd** (`EncryptionConfiguration`) — nhưng đó là việc quản trị cluster phải làm thêm, không tự có.

> ⚠️ Bước 5 phần thực hành bạn sẽ tự tay giải mã một Secret. Hãy làm thật — nó sẽ thay đổi cách bạn xử lý bí mật mãi mãi.

#### 3. Hai cách tiêm — khác nhau ở một điểm sống còn

| | **Biến môi trường** (`env`) | **Gắn thành file** (`volumeMount`) |
|---|---|---|
| App đọc thế nào | `process.env.TEN_BIEN` | Đọc file trong thư mục |
| Sửa ConfigMap thì sao | **KHÔNG tự cập nhật** — phải khởi động lại pod | **Tự cập nhật** sau ~1 phút |
| Hợp với | Giá trị đơn giản, ngắn | File cấu hình cả khối (`nginx.conf`, `app.yaml`) |

> 🔑 Đây là câu hỏi phỏng vấn kinh điển và cũng là nguồn gốc của rất nhiều sự bối rối: *"Tôi sửa ConfigMap rồi mà app vẫn chạy giá trị cũ?"* — Vì bạn tiêm bằng `env`. Biến môi trường được ấn định **lúc container khởi động** và không bao giờ đổi sau đó.

#### 4. Lưu trữ: pod chết thì dữ liệu đi đâu?

Mặc định, mọi thứ container ghi ra đều **mất sạch khi pod chết**. Với app không trạng thái thì tốt. Với database thì là thảm hoạ.

| Loại | Sống được bao lâu | Dùng cho |
|---|---|---|
| Ổ đĩa của container | Pod chết là mất | File tạm |
| **emptyDir** | Sống theo pod (các container trong pod dùng chung) | Cache, thư mục làm việc tạm |
| **PersistentVolume (PV)** | **Sống độc lập với pod** | Database, file người dùng tải lên |

Cách dùng PV có ba phần, hiểu đúng thì mọi thứ sáng ra:

```text
  PVC  (Yêu cầu)          StorageClass (Nhà cung cấp)        PV (Ổ đĩa thật)
  "Tôi cần 1Gi,      ──>  "Được, để tôi cấp cho"       ──>  Ổ đĩa được tạo
   đọc-ghi"                 (tự động)                        và gắn vào pod
```

Bạn **chỉ viết PVC** — phần còn lại cluster tự lo. Trên cloud, StorageClass sẽ tạo ra ổ đĩa thật (EBS trên AWS, Persistent Disk trên GCP).

#### 5. Access mode — chi tiết hay làm hỏng việc

| Mode | Nghĩa | Thực tế |
|---|---|---|
| **RWO** (ReadWriteOnce) | Chỉ **một node** gắn được để ghi | Mặc định của hầu hết ổ đĩa cloud |
| **ROX** (ReadOnlyMany) | Nhiều node đọc | Ít gặp |
| **RWX** (ReadWriteMany) | Nhiều node cùng ghi | Cần hệ thống file mạng (NFS...), **không phải ổ đĩa cloud thường** |

> ⚠️ Bẫy rất hay gặp: khai `replicas: 3` cho một Deployment gắn PVC kiểu **RWO**. Ba pod rơi vào ba node khác nhau → chỉ pod đầu chạy được, hai pod còn lại kẹt mãi ở trạng thái `ContainerCreating`. Đây là lý do app có trạng thái nên dùng **StatefulSet** (mỗi bản một ổ đĩa riêng), không phải Deployment.

### 🧪 LAB — Cấu hình, bí mật và dữ liệu bền

**File sẽ tạo:**

```text
lab39-config/
├── cau-hinh.yaml       # ConfigMap: dạng biến + dạng file
├── bi-mat.yaml         # Secret
├── app.yaml            # Deployment dùng cả ConfigMap lẫn Secret
└── postgres.yaml       # PVC + Postgres — để kiểm chứng dữ liệu bền
```

#### File 1 — `cau-hinh.yaml`

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: cau-hinh-app
data:
  # Kiểu 1: từng cặp khoá-giá trị đơn giản -> hợp để tiêm làm biến môi trường
  TEN_UNG_DUNG: "Cửa hàng ABC"
  MOI_TRUONG: "staging"
  SO_KET_QUA_MOI_TRANG: "20"

  # Kiểu 2: nguyên một file -> hợp để gắn vào thư mục
  trang-chu.html: |
    <!DOCTYPE html>
    <html lang="vi">
      <head><meta charset="utf-8"><title>Trang từ ConfigMap</title></head>
      <body>
        <h1>Nội dung này đến từ ConfigMap</h1>
        <p>Sửa ConfigMap rồi chờ khoảng 1 phút, trang này tự đổi.</p>
      </body>
    </html>
```

#### File 2 — `bi-mat.yaml`

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: bi-mat-app
type: Opaque
stringData:                     # stringData: viết chữ thường, K8s tự mã hoá base64 giúp
  MAT_KHAU_DB: "MatKhauSieuBiMat123"
  KHOA_API: "sk-abc123xyz789"
```

> 📌 Dùng `stringData` thay vì `data` để khỏi phải tự chạy `base64` — dễ đọc và ít sai hơn hẳn.

#### File 3 — `app.yaml`

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: app-cau-hinh
spec:
  replicas: 1
  selector:
    matchLabels:
      app: app-cau-hinh
  template:
    metadata:
      labels:
        app: app-cau-hinh
    spec:
      containers:
        - name: web
          image: nginx:1.27
          ports:
            - containerPort: 80

          # ---- Cách 1: tiêm thành BIẾN MÔI TRƯỜNG ----
          envFrom:
            - configMapRef:
                name: cau-hinh-app      # lấy TẤT CẢ khoá làm biến môi trường
          env:
            - name: MAT_KHAU_DB         # lấy đúng MỘT khoá từ Secret
              valueFrom:
                secretKeyRef:
                  name: bi-mat-app
                  key: MAT_KHAU_DB

          # ---- Cách 2: gắn thành FILE ----
          volumeMounts:
            - name: trang-web
              mountPath: /usr/share/nginx/html/index.html
              subPath: trang-chu.html   # chỉ gắn 1 khoá, không đè cả thư mục
            - name: kho-bi-mat
              mountPath: /etc/bi-mat
              readOnly: true

          resources:
            requests:
              memory: "64Mi"
              cpu: "50m"
            limits:
              memory: "128Mi"

      volumes:
        - name: trang-web
          configMap:
            name: cau-hinh-app
        - name: kho-bi-mat
          secret:
            secretName: bi-mat-app
```

#### File 4 — `postgres.yaml`

```yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: du-lieu-postgres
spec:
  accessModes:
    - ReadWriteOnce               # một node gắn để ghi — đúng cho database
  resources:
    requests:
      storage: 1Gi                # xin 1 GB
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: postgres
spec:
  replicas: 1                     # CHỈ 1 — nhiều bản cùng ghi một ổ RWO sẽ hỏng
  selector:
    matchLabels:
      app: postgres
  strategy:
    type: Recreate                # xoá pod cũ RỒI mới tạo pod mới (không giành ổ đĩa)
  template:
    metadata:
      labels:
        app: postgres
    spec:
      containers:
        - name: postgres
          image: postgres:16-alpine
          env:
            - name: POSTGRES_PASSWORD
              valueFrom:
                secretKeyRef:
                  name: bi-mat-app
                  key: MAT_KHAU_DB
            - name: POSTGRES_DB
              value: cuahang
            - name: PGDATA
              value: /var/lib/postgresql/data/pgdata   # thư mục con, tránh lỗi "not empty"
          ports:
            - containerPort: 5432
          volumeMounts:
            - name: kho-du-lieu
              mountPath: /var/lib/postgresql/data
          resources:
            requests:
              memory: "128Mi"
              cpu: "100m"
            limits:
              memory: "512Mi"
      volumes:
        - name: kho-du-lieu
          persistentVolumeClaim:
            claimName: du-lieu-postgres
---
apiVersion: v1
kind: Service
metadata:
  name: postgres-svc
spec:
  selector:
    app: postgres
  ports:
    - port: 5432
      targetPort: 5432
```

### 🧭 Hướng dẫn làm LAB — step by step

#### Bước 1 — Tạo ConfigMap và Secret

```bash
mkdir -p ~/lab39-config && cd ~/lab39-config
# tạo cau-hinh.yaml và bi-mat.yaml theo phần LAB
kubectl apply -f cau-hinh.yaml -f bi-mat.yaml
kubectl get configmap cau-hinh-app
kubectl get secret bi-mat-app
```

**Bạn sẽ thấy:**
```text
NAME           DATA   AGE
cau-hinh-app   4      5s

NAME         TYPE     DATA   AGE
bi-mat-app   Opaque   2      5s
```

✅ **Checkpoint:** ConfigMap có `DATA = 4`, Secret có `DATA = 2`.

#### Bước 2 — Xem nội dung: một cái đọc được, một cái "có vẻ" không

```bash
kubectl get configmap cau-hinh-app -o yaml | head -12
echo "-----"
kubectl get secret bi-mat-app -o yaml | grep -A3 "^data:"
```

**Bạn sẽ thấy:**
```text
data:
  MOI_TRUONG: staging
  SO_KET_QUA_MOI_TRANG: "20"
  TEN_UNG_DUNG: Cửa hàng ABC
-----
data:
  KHOA_API: c2stYWJjMTIzeHl6Nzg5
  MAT_KHAU_DB: TWF0S2hhdVNpZXVCaU1hdDEyMw==
```

✅ **Checkpoint:** ConfigMap đọc thẳng được; Secret hiện ra chuỗi ký tự lộn xộn.

#### Bước 3 — Triển khai app dùng cả hai

```bash
# tạo app.yaml theo phần LAB
kubectl apply -f app.yaml
kubectl rollout status deployment/app-cau-hinh
```

**Bạn sẽ thấy:** `deployment "app-cau-hinh" successfully rolled out`.

✅ **Checkpoint:** rollout thành công.

⚠️ **Nếu pod kẹt ở `CreateContainerConfigError`:** hầu như luôn là tên ConfigMap/Secret sai hoặc khoá không tồn tại. Xem nguyên nhân chính xác:
```bash
kubectl describe pod -l app=app-cau-hinh | grep -A5 Events
```

#### Bước 4 — Kiểm chứng cả hai cách tiêm

```bash
POD=$(kubectl get pods -l app=app-cau-hinh -o jsonpath='{.items[0].metadata.name}')

echo "--- Tiêm dạng BIẾN MÔI TRƯỜNG ---"
kubectl exec $POD -- printenv TEN_UNG_DUNG MOI_TRUONG MAT_KHAU_DB

echo "--- Tiêm dạng FILE ---"
kubectl exec $POD -- ls -l /etc/bi-mat
kubectl exec $POD -- cat /etc/bi-mat/KHOA_API; echo
kubectl exec $POD -- head -6 /usr/share/nginx/html/index.html
```

**Bạn sẽ thấy:**
```text
--- Tiêm dạng BIẾN MÔI TRƯỜNG ---
Cửa hàng ABC
staging
MatKhauSieuBiMat123

--- Tiêm dạng FILE ---
total 0
lrwxrwxrwx 1 root root 15 ... KHOA_API -> ..data/KHOA_API
lrwxrwxrwx 1 root root 18 ... MAT_KHAU_DB -> ..data/MAT_KHAU_DB
sk-abc123xyz789
<!DOCTYPE html>
<html lang="vi">
...
```

✅ **Checkpoint:** giá trị đến được bên trong container bằng **cả hai** đường, và nội dung trang chủ đúng là HTML từ ConfigMap.

💡 Chú ý: bên trong container, Secret hiện ra là **chữ thường**, không phải base64. Base64 chỉ là cách lưu trong etcd — K8s tự giải mã khi đưa vào pod.

#### Bước 5 — Bài học bảo mật: tự tay giải mã Secret

Làm thật bước này.

```bash
kubectl get secret bi-mat-app -o jsonpath='{.data.MAT_KHAU_DB}' | base64 -d; echo
```

**Bạn sẽ thấy:**
```text
MatKhauSieuBiMat123
```

✅ **Checkpoint:** bạn vừa đọc mật khẩu bằng **một lệnh, không cần quyền gì đặc biệt**.

💡 **Đây là điều phải khắc cốt ghi tâm:** `base64` là **mã hoá dạng**, không phải **mã hoá bảo mật**. Hệ quả thực tế:

- **Không bao giờ commit file Secret vào Git.** Cả thế giới đọc được. Nếu buộc phải để Secret trong Git thì dùng **Sealed Secrets** hoặc **SOPS** (mã hoá thật).
- **Ai có quyền `get secret` trên namespace là có mọi mật khẩu ở đó.** Phải siết bằng RBAC.
- Ở công ty làm nghiêm túc, người ta thường **không lưu bí mật trong K8s** mà dùng **HashiCorp Vault** hoặc dịch vụ bí mật của cloud (Module nâng cao — bài NC2).

#### Bước 6 — Chứng minh `env` KHÔNG tự cập nhật, còn file thì có

Đây là điểm ở Lý thuyết #3. Sửa ConfigMap:

```bash
kubectl patch configmap cau-hinh-app --type merge \
  -p '{"data":{"MOI_TRUONG":"production","trang-chu.html":"<h1>NỘI DUNG ĐÃ ĐỔI</h1>"}}'
```

Kiểm tra ngay lập tức:

```bash
kubectl exec $POD -- printenv MOI_TRUONG            # biến môi trường
kubectl exec $POD -- cat /usr/share/nginx/html/index.html   # file
```

**Bạn sẽ thấy ngay lúc này:**
```text
staging                  ← VẪN GIÁ TRỊ CŨ (biến môi trường không đổi)
<!DOCTYPE html>...       ← file cũng chưa đổi (cần chờ)
```

Chờ khoảng 60–90 giây rồi kiểm tra lại:

```bash
sleep 75
kubectl exec $POD -- printenv MOI_TRUONG
kubectl exec $POD -- cat /usr/share/nginx/html/index.html
```

**Bạn sẽ thấy:**
```text
staging                  ← VẪN CŨ, mãi mãi cũ
<h1>NỘI DUNG ĐÃ ĐỔI</h1> ← file ĐÃ TỰ CẬP NHẬT
```

✅ **Checkpoint:** thấy rõ sự khác biệt — file tự đổi, biến môi trường thì không.

💡 **Cách sửa đúng khi cần biến môi trường mới:** khởi động lại pod theo kiểu cuốn chiếu, không gián đoạn:
```bash
kubectl rollout restart deployment/app-cau-hinh
kubectl rollout status deployment/app-cau-hinh
POD=$(kubectl get pods -l app=app-cau-hinh -o jsonpath='{.items[0].metadata.name}')
kubectl exec $POD -- printenv MOI_TRUONG      # giờ mới ra: production
```

**Bạn sẽ thấy:** `production`.

💡 Ở công ty, người ta thường gắn **hash của ConfigMap vào annotation của pod template** — ConfigMap đổi thì hash đổi, K8s tự coi đó là phiên bản mới và tự khởi động lại. Helm (Ngày 42) có sẵn mẹo này.

#### Bước 7 — Dữ liệu bền: dựng Postgres có PVC

```bash
# tạo postgres.yaml theo phần LAB
kubectl apply -f postgres.yaml
kubectl get pvc
kubectl rollout status deployment/postgres
```

**Bạn sẽ thấy:**
```text
NAME               STATUS   VOLUME          CAPACITY   ACCESS MODES   STORAGECLASS
du-lieu-postgres   Bound    pvc-a3f2...     1Gi        RWO            standard
```

✅ **Checkpoint:** `STATUS` là **`Bound`** (đã được cấp ổ đĩa thật).

⚠️ **Nếu PVC kẹt ở `Pending`:** không có StorageClass nào cấp ổ. Trên minikube thì addon `storage-provisioner` lo việc này — kiểm tra: `kubectl get storageclass`. Không có dòng nào `(default)` thì bật: `minikube addons enable default-storageclass`.

#### Bước 8 — Ghi dữ liệu, giết pod, và kiểm tra dữ liệu còn không

Đây là bước đáng giá nhất hôm nay.

```bash
PG=$(kubectl get pods -l app=postgres -o jsonpath='{.items[0].metadata.name}')

kubectl exec $PG -- psql -U postgres -d cuahang -c \
  "CREATE TABLE khach (id serial primary key, ten text);"
kubectl exec $PG -- psql -U postgres -d cuahang -c \
  "INSERT INTO khach (ten) VALUES ('Chị An'), ('Anh Bình');"
kubectl exec $PG -- psql -U postgres -d cuahang -c "SELECT * FROM khach;"
```

**Bạn sẽ thấy:**
```text
 id |   ten
----+----------
  1 | Chị An
  2 | Anh Bình
(2 rows)
```

Giờ giết pod database:

```bash
kubectl delete pod $PG
kubectl rollout status deployment/postgres
PG=$(kubectl get pods -l app=postgres -o jsonpath='{.items[0].metadata.name}')
kubectl exec $PG -- psql -U postgres -d cuahang -c "SELECT * FROM khach;"
```

**Bạn sẽ thấy:**
```text
 id |   ten
----+----------
  1 | Chị An
  2 | Anh Bình
(2 rows)
```

✅ **Checkpoint:** **pod hoàn toàn mới, dữ liệu vẫn nguyên.**

💡 **Đây chính là ý nghĩa của "bền vững":** pod là đồ dùng một lần, nhưng ổ đĩa thì không. PVC sống độc lập — pod chết, ổ đĩa vẫn nằm đó chờ pod mới gắn vào.

Để so sánh, hãy xem điều gì xảy ra **nếu không có PVC**:
```bash
kubectl run tam-thoi --image=postgres:16-alpine --env="POSTGRES_PASSWORD=abc" --restart=Never
sleep 15
kubectl exec tam-thoi -- psql -U postgres -c "CREATE TABLE t (x int); INSERT INTO t VALUES (42);"
kubectl delete pod tam-thoi
# Pod mất -> dữ liệu mất theo, không có đường lấy lại
```

#### Bước 9 — Dọn dẹp (và một cái bẫy nhỏ)

```bash
kubectl delete -f app.yaml -f postgres.yaml -f cau-hinh.yaml -f bi-mat.yaml
kubectl get pvc
```

**Bạn sẽ thấy:** PVC `du-lieu-postgres` **vẫn còn đó**!

✅ **Checkpoint:** hiểu rằng xoá Deployment **không** xoá PVC.

💡 Đây là **thiết kế có chủ đích** — để bạn không mất database chỉ vì lỡ tay xoá nhầm Deployment. Muốn xoá thật thì phải nói rõ:
```bash
kubectl delete pvc du-lieu-postgres
minikube stop
```

⚠️ Ở công ty, PVC mồ côi (không còn ai dùng nhưng vẫn tồn tại) là **khoản tiền chảy âm thầm** trên hoá đơn cloud. Nên có thói quen rà soát định kỳ.

### 💡 Đi làm mới thấm (sách cơ bản hay bỏ quên)

- **Secret của K8s không phải giải pháp quản lý bí mật.** Nó chỉ là chỗ chứa. Giải pháp thật là Vault / AWS Secrets Manager / GCP Secret Manager, có xoay vòng khoá tự động và nhật ký truy cập. Với Git thì dùng **Sealed Secrets** hoặc **SOPS**.
- **`kubectl rollout restart` là lệnh nên thuộc lòng.** Nó khởi động lại pod theo kiểu cuốn chiếu, **không gián đoạn dịch vụ** — dùng khi đổi ConfigMap dạng `env`, hoặc khi cần pod lấy lại chứng chỉ/khoá mới.
- **PVC `ReadWriteOnce` + `replicas > 1` = kẹt.** Nếu bạn thấy pod đứng mãi ở `ContainerCreating` kèm lỗi `Multi-Attach error`, gần như chắc chắn là lỗi này. App có trạng thái phải dùng **StatefulSet**, mỗi bản một PVC riêng.
- **`strategy: Recreate` cho database, không phải `RollingUpdate`.** Mặc định K8s tạo pod mới trước rồi mới xoá pod cũ — nhưng hai pod database không thể cùng gắn một ổ RWO, nên pod mới sẽ kẹt vĩnh viễn. File `postgres.yaml` ở trên đã xử lý sẵn điều này.
- **PVC không tự thu nhỏ, và thường không tự phình.** Mở rộng được (nếu StorageClass cho phép `allowVolumeExpansion`) nhưng **không bao giờ thu nhỏ lại được**. Xin dung lượng phải tính trước.
- **Đừng để database trong K8s nếu chưa có đội vận hành mạnh.** Đây là lời khuyên thật lòng: sao lưu, khôi phục, nâng cấp phiên bản, chuyển đổi dự phòng — database quản lý bởi cloud (RDS, Cloud SQL) đáng đồng tiền hơn nhiều so với tự vận hành trên K8s. Lab thì cứ làm để hiểu; production thì hãy cân nhắc rất kỹ.

### 📝 Tự kiểm tra

> Nghĩ câu trả lời **thành lời** trước khi mở đáp án — nghĩ thầm luôn thấy mình hiểu.

<details>
<summary><b>1. Bạn sửa ConfigMap nhưng ứng dụng vẫn chạy giá trị cũ. Vì sao, và sửa thế nào?</b></summary>

Vì bạn tiêm bằng **biến môi trường** (`env`/`envFrom`). Biến môi trường được ấn định **lúc container khởi động** và không bao giờ đổi sau đó.

Ngược lại, ConfigMap gắn thành **file** (`volumeMount`) sẽ **tự cập nhật** sau khoảng 1 phút.

Sửa: `kubectl rollout restart deployment/<ten>` — khởi động lại theo kiểu cuốn chiếu, không gián đoạn dịch vụ.

Cách làm chuyên nghiệp hơn: gắn hash của ConfigMap vào annotation của pod template, ConfigMap đổi thì hash đổi và K8s tự coi là phiên bản mới (Helm có sẵn mẹo này).

</details>

<details>
<summary><b>2. Secret của Kubernetes có được mã hoá không? Hệ quả thực tế là gì?</b></summary>

**Không.** Nó chỉ được mã hoá dạng **base64** — ai cũng giải ngược trong một giây bằng `base64 -d`.

Ba hệ quả thực tế:
1. **Không bao giờ commit Secret vào Git** — cả thế giới đọc được
2. Ai có quyền `get secret` trên namespace là **có mọi mật khẩu** ở đó → phải siết RBAC
3. Bí mật thật nên nằm ở **Vault** hoặc dịch vụ bí mật của cloud; nếu buộc phải để trong Git thì dùng **Sealed Secrets** hoặc **SOPS** (mã hoá thật)

Secret khác ConfigMap ở chỗ: không bị in ra khi `kubectl get`, phân quyền RBAC riêng được, và **có thể** bật mã hoá trong etcd (nhưng phải cấu hình thêm).

</details>

<details>
<summary><b>3. Vì sao database cần `strategy: Recreate` thay vì `RollingUpdate` mặc định?</b></summary>

Vì `RollingUpdate` **tạo pod mới trước rồi mới xoá pod cũ**. Nhưng hai pod database không thể cùng gắn một ổ đĩa `ReadWriteOnce` — pod mới sẽ kẹt vĩnh viễn ở `ContainerCreating` với lỗi `Multi-Attach error`.

`Recreate` xoá pod cũ **rồi mới** tạo pod mới → không tranh chấp ổ đĩa. Đánh đổi: có một khoảng gián đoạn ngắn — chấp nhận được với database một bản.

Đi kèm: database phải `replicas: 1`. Cần nhiều bản thì dùng **StatefulSet**, mỗi bản một PVC riêng.

</details>

### 📚 Thuật ngữ Anh–Việt (ngày này)

| Thuật ngữ | Nghĩa |
|---|---|
| **ConfigMap** | Nơi chứa cấu hình thường: URL, cổng, tên miền |
| **Secret** | Nơi chứa dữ liệu nhạy cảm — **chỉ base64, KHÔNG phải mã hoá** |
| **`envFrom` vs `volumeMount`** | Tiêm thành biến môi trường (cố định) vs thành file (tự cập nhật) |
| **`kubectl rollout restart`** | Khởi động lại pod cuốn chiếu, không gián đoạn dịch vụ |
| **PV / PVC** | Ổ đĩa thật / yêu cầu xin ổ đĩa; bạn chỉ viết PVC, cluster lo phần còn lại |
| **StorageClass** | Nhà cung cấp ổ đĩa — tự tạo PV khi có PVC |
| **RWO / RWX** | ReadWriteOnce (một node ghi) / ReadWriteMany (nhiều node cùng ghi) |
| **`strategy: Recreate`** | Xoá pod cũ rồi mới tạo mới — bắt buộc cho database dùng ổ RWO |
| **Sealed Secrets / SOPS** | Mã hoá thật để commit bí mật vào Git an toàn |

### 🎯 Đúc kết Ngày 39

**3 điều phải mang theo:**

1. **Image bất biến, cấu hình tiêm vào lúc chạy.** Một image duy nhất chạy được ở mọi môi trường — chỉ ConfigMap/Secret thay đổi.
2. **`env` cố định lúc khởi động, file thì tự cập nhật.** Sửa ConfigMap dạng biến môi trường thì phải `kubectl rollout restart`.
3. **Secret chỉ là base64.** Bất kỳ ai có quyền đọc đều lấy được bí mật. Bí mật thật phải nằm ở Vault hoặc dịch vụ bí mật của cloud.

> 🧠 **Một câu để nhớ:** pod là đồ dùng một lần, **PVC thì không** — đó là ranh giới giữa "mất dữ liệu" và "chỉ mất một cái pod".

**✅ Tự chấm** *(đánh dấu khi làm được mà không nhìn tài liệu):*

- [ ] Giải thích vì sao cấu hình không được nằm trong image
- [ ] Tiêm ConfigMap theo cả hai cách: biến môi trường và file
- [ ] Giải mã một Secret bằng `base64 -d` và nói rõ hệ quả bảo mật
- [ ] Chứng minh `env` không tự cập nhật còn file mount thì có
- [ ] Tạo PVC, ghi dữ liệu, xoá pod và xác nhận dữ liệu còn nguyên
- [ ] Nói được vì sao database cần `strategy: Recreate` và `replicas: 1` với ổ RWO
- [ ] Biết rằng xoá Deployment không xoá PVC, và vì sao thiết kế như vậy

✅ **Kết quả đạt được:** Ứng dụng nhận cấu hình và bí mật từ bên ngoài, cùng một database giữ được dữ liệu qua các lần pod sinh-diệt — đủ mảnh ghép để ghép hệ thống full-stack ở Ngày 40.

---

## Ngày 40 — MILESTONE: Deploy Full-stack lên Kubernetes

> ⏱️ ~150 phút · Loại: LAB Final
>
> 🧭 **Bạn đang ở đâu:** Ngày 36–39 (kiến trúc K8s, Deployment, Service, Ingress, ConfigMap, Secret, PVC) → **Ngày 40 (ghép thành một hệ thống nhiều tầng chạy trên cluster)** → Ngày 41 (probe, HPA).
>
> ✅ **Chuẩn bị:** cluster đang chạy (`minikube start`), Ingress addon đã bật.
>
> 🎯 **Đề bài + tiêu chí chấm.** Đây là bài kiểm tra xem bạn đã thật sự nắm Kubernetes hay chỉ mới chép được YAML.

### 📋 Đề bài — "Hệ thống ba tầng trên cluster"

> Đưa hệ thống ba tầng của Ngày 21 lên Kubernetes. Yêu cầu khắt khe nhất: **xoá toàn bộ namespace rồi dựng lại từ file YAML** — và mọi thứ phải trở lại y như cũ, kể cả dữ liệu.

```text
   Trình duyệt → shop.local
        │
     [Ingress]
        ├── /      → Service web  → 3 pod frontend
        └── /api   → Service api  → 2 pod backend
                                        │
                                   Service db → 1 pod postgres (PVC)
```

### ✅ Yêu cầu

#### Bắt buộc

| # | Yêu cầu | Kiến thức từ |
|---|---|---|
| 1 | Namespace riêng cho hệ thống | Ngày 36 |
| 2 | Frontend: Deployment 3 bản + Service | Ngày 37, 38 |
| 3 | Backend: Deployment 2 bản + Service | Ngày 37, 38 |
| 4 | Database: 1 bản + **PVC**, `strategy: Recreate` | Ngày 39 |
| 5 | Ingress định tuyến `/` và `/api` về hai Service | Ngày 38 |
| 6 | Cấu hình qua **ConfigMap**, mật khẩu qua **Secret** | Ngày 39 |
| 7 | Mọi container khai `resources.requests` | Ngày 36 |
| 8 | Chỉ Ingress ra ngoài; Service đều là ClusterIP | Ngày 38 |
| 9 | Toàn bộ nằm trong file YAML, `kubectl apply -f` là dựng lại được | Ngày 36 |
| 10 | Dữ liệu database sống sót khi xoá pod | Ngày 39 |

#### Nâng cao

| # | Yêu cầu |
|---|---|
| 11 | Dùng Kustomize hoặc chia thư mục theo môi trường |
| 12 | `NetworkPolicy` chỉ cho backend gọi được database |
| 13 | `resources.limits` cho RAM ở mọi container |
| 14 | Nhãn chuẩn `app.kubernetes.io/*` cho mọi tài nguyên |
| 15 | Một lệnh duy nhất dựng toàn bộ (`make trien-khai`) |

### 📐 Tiêu chí chấm (100 điểm)

| Hạng mục | Điểm | Đạt tối đa khi |
|---|---:|---|
| Cấu trúc tài nguyên | 15 | Namespace riêng, nhãn nhất quán, tên rõ nghĩa |
| Deployment | 20 | Đủ số bản, selector khớp nhãn, khai requests |
| Mạng | 20 | Service đúng loại, Ingress định tuyến đúng, không lộ thừa |
| Cấu hình & bí mật | 15 | ConfigMap và Secret tách bạch, không viết cứng trong YAML |
| Lưu trữ | 15 | PVC gắn đúng, dữ liệu bền, `Recreate` cho database |
| Dựng lại được | 15 | Xoá namespace rồi `apply` lại ra đúng hệ thống cũ |

### 🔥 Ba phép thử quyết định

**Phép thử 1 — Tự phục hồi (15 điểm).**
```bash
kubectl -n cua-hang delete pod -l app=web --wait=false
kubectl -n cua-hang get pods -w
```
> Pod mới phải lên trong vài giây, và trang web **không được** gián đoạn (còn 2 bản kia phục vụ).

**Phép thử 2 — Dữ liệu bền (15 điểm).**
```bash
# Ghi dữ liệu
kubectl -n cua-hang exec deploy/db -- psql -U postgres -c \
  "CREATE TABLE thu(x int); INSERT INTO thu VALUES (42);"

# Giết pod database
kubectl -n cua-hang delete pod -l app=db
kubectl -n cua-hang rollout status deploy/db

# Dữ liệu phải còn
kubectl -n cua-hang exec deploy/db -- psql -U postgres -c "SELECT * FROM thu;"
```

**Phép thử 3 — Dựng lại toàn bộ (15 điểm).**
```bash
kubectl delete namespace cua-hang
kubectl apply -f k8s/            # hoặc: kubectl apply -k k8s/overlays/dev
sleep 60
curl -s http://shop.local/ | head -3
curl -s http://shop.local/api/health
```
> Toàn bộ hệ thống phải trở lại. Nếu phải gõ thêm lệnh nào ngoài `apply` thì bạn còn thiếu file.

### 🧪 Bộ kiểm chứng

```bash
#!/usr/bin/env bash
NS=cua-hang
diem=0
kiem() { if eval "$2" &>/dev/null; then echo "  ✅ $1 (+$3)"; diem=$((diem+$3)); else echo "  ❌ $1"; fi; }

echo "▸ Cấu trúc"
kiem "Có namespace riêng"          "kubectl get ns $NS" 5
kiem "Dùng nhãn chuẩn"             "kubectl -n $NS get deploy -o yaml | grep -q 'app.kubernetes.io/name'" 5
kiem "Mọi pod đang Running"        "! kubectl -n $NS get pods --no-headers | grep -qvE 'Running|Completed'" 5

echo "▸ Deployment"
kiem "Frontend có 3 bản"           "[ \$(kubectl -n $NS get deploy web -o jsonpath='{.status.readyReplicas}') -eq 3 ]" 7
kiem "Backend có 2 bản"            "[ \$(kubectl -n $NS get deploy api -o jsonpath='{.status.readyReplicas}') -eq 2 ]" 7
kiem "Mọi container khai requests" "! kubectl -n $NS get pods -o json | grep -q '\"resources\":{}'" 6

echo "▸ Mạng"
kiem "Service web có endpoint"     "[ -n \"\$(kubectl -n $NS get endpoints web -o jsonpath='{.subsets}')\" ]" 6
kiem "Service api có endpoint"     "[ -n \"\$(kubectl -n $NS get endpoints api -o jsonpath='{.subsets}')\" ]" 6
kiem "Không Service nào NodePort"  "! kubectl -n $NS get svc -o yaml | grep -q 'type: NodePort'" 4
kiem "Có Ingress với địa chỉ"      "[ -n \"\$(kubectl -n $NS get ingress -o jsonpath='{.items[0].status.loadBalancer.ingress}')\" ]" 4

echo "▸ Cấu hình"
kiem "Có ConfigMap"                "kubectl -n $NS get configmap | grep -qv NAME" 5
kiem "Có Secret"                   "kubectl -n $NS get secret | grep -q Opaque" 5
kiem "Không mật khẩu viết cứng"    "! grep -rqiE 'password:\s*[\"'\'']?[a-z0-9]{6,}' k8s/*.yaml" 5

echo "▸ Lưu trữ"
kiem "PVC đã Bound"                "kubectl -n $NS get pvc -o jsonpath='{.items[0].status.phase}' | grep -q Bound" 8
kiem "Database dùng Recreate"      "kubectl -n $NS get deploy db -o jsonpath='{.spec.strategy.type}' | grep -q Recreate" 7

echo ""
echo "  ĐIỂM (tự động): $diem / 85"
```

### ⚠️ Những cái bẫy hay gặp

| Bẫy | Hậu quả | Cách tránh |
|---|---|---|
| `selector` không khớp `labels` | Service không tìm thấy pod, gọi vào treo | `kubectl get endpoints` — thấy `<none>` là biết |
| Database dùng `RollingUpdate` | Pod mới kẹt vì không gắn được ổ RWO | `strategy: Recreate` |
| Database `replicas: 2` với ổ RWO | `Multi-Attach error`, pod kẹt mãi | Chỉ 1 bản, hoặc dùng StatefulSet |
| Mật khẩu viết thẳng trong YAML | Lộ khi commit | ConfigMap cho cấu hình, Secret cho bí mật |
| Không khai `requests` | Scheduler xếp nhầm, pod bị giết trước khi node cạn RAM | Luôn khai requests |
| Khai Ingress mà chưa bật Controller | Không có gì xảy ra cả | `minikube addons enable ingress` |
| Backend gọi database bằng IP pod | Hỏng ngay lần pod database restart đầu tiên | Gọi bằng tên Service |

### 💬 Gợi ý khi bí

<details>
<summary><b>Nên tổ chức thư mục YAML thế nào?</b></summary>

Cách đơn giản, dùng được ngay:

```text
k8s/
├── 00-namespace.yaml
├── 01-configmap.yaml
├── 02-secret.yaml
├── 10-db-pvc.yaml
├── 11-db-deployment.yaml
├── 12-db-service.yaml
├── 20-api-deployment.yaml
├── 21-api-service.yaml
├── 30-web-deployment.yaml
├── 31-web-service.yaml
└── 40-ingress.yaml
```

Đánh số ở đầu tên file để `kubectl apply -f k8s/` áp theo đúng thứ tự (namespace trước, ingress sau cùng). Đơn giản mà hiệu quả.

Khi cần nhiều môi trường, chuyển sang **Kustomize**: một thư mục `base/` chung và các `overlays/dev`, `overlays/prod` chỉ ghi phần khác biệt. Helm (Ngày 42) là bước tiếp theo nữa.
</details>

<details>
<summary><b>Backend kết nối database thế nào cho đúng?</b></summary>

Gọi bằng **tên Service**, và lấy mật khẩu từ Secret:

```yaml
        env:
          - name: DB_HOST
            value: "db"                      # tên Service, KHÔNG phải IP
          - name: DB_PORT
            value: "5432"
          - name: DB_NAME
            valueFrom:
              configMapKeyRef:
                name: cau-hinh-app
                key: TEN_DATABASE
          - name: DB_PASSWORD
            valueFrom:
              secretKeyRef:
                name: bi-mat-db
                key: MAT_KHAU
```

Kiểm chứng từ bên trong cluster:
```bash
kubectl -n cua-hang exec deploy/api -- nslookup db
kubectl -n cua-hang exec deploy/api -- nc -zv db 5432
```
</details>

<details>
<summary><b>Ingress trả 404, kiểm tra theo thứ tự nào?</b></summary>

Bốn bước, dừng lại ở bước nào sai thì sửa ngay bước đó:

```bash
# 1) Controller có chạy không?
kubectl get pods -n ingress-nginx

# 2) Ingress có nhận được địa chỉ chưa?
kubectl -n cua-hang get ingress

# 3) Service phía sau có endpoint không? (nguyên nhân phổ biến nhất)
kubectl -n cua-hang get endpoints

# 4) Luật định tuyến có đúng không?
kubectl -n cua-hang describe ingress | grep -A10 Rules
```

Hai lỗi hay gặp nhất: **thiếu `ingressClassName: nginx`**, và **đặt `/` trước `/api`** khiến `/` nuốt hết mọi đường dẫn.
</details>

### 🎯 Đúc kết Ngày 40 — Tổng kết phần Kubernetes cơ bản

**3 điều phải mang theo:**

1. **Toàn bộ hệ thống phải nằm trong YAML.** Xoá namespace rồi `apply` lại ra đúng hệ thống cũ — đó là thước đo bạn đã làm đúng tinh thần khai báo hay chưa.
2. **Không trạng thái thì nhân bản thoải mái; có trạng thái thì phải cẩn thận.** Frontend và backend chạy nhiều bản; database cần PVC, một bản, và `Recreate`.
3. **Chỉ mở ra ngoài đúng một cửa.** Mọi Service là ClusterIP, Ingress là lối vào duy nhất.

> 🧠 **Một câu để nhớ:** nếu bạn không dám xoá namespace vì sợ không dựng lại được, thì hệ thống của bạn **chưa nằm trong YAML** — nó vẫn nằm trong những lệnh bạn đã gõ.

**✅ Tự chấm Milestone:**

- [ ] Đạt từ 75 điểm
- [ ] Phép thử 1: giết pod, dịch vụ không gián đoạn
- [ ] Phép thử 2: dữ liệu database sống sót
- [ ] Phép thử 3: xoá namespace rồi dựng lại hoàn chỉnh
- [ ] Giải thích được vì sao database khác frontend về cách triển khai

✅ **Kết quả đạt được:** Hệ thống ba tầng chạy trên Kubernetes, mô tả hoàn toàn bằng YAML, tự phục hồi và giữ được dữ liệu — nền để Ngày 41 thêm probe và tự co giãn.

---

## Ngày 41 — Kubernetes: Health Check, Resource & Autoscaling

> ⏱️ ~90 phút · Loại: Kubernetes
>
> 🧭 **Bạn đang ở đâu:** Ngày 40 (Milestone full-stack) → **Ngày 41 (dạy K8s biết thế nào là "app khoẻ", và tự co giãn theo tải)** → Ngày 42 (Helm đóng gói). Ngày 36 có nhắc: K8s chỉ đảm bảo *đủ số pod*, chứ chưa biết app bên trong có thật sự phục vụ được không. Hôm nay vá đúng lỗ hổng đó.
>
> ✅ **Chuẩn bị:** cluster đang chạy (`minikube start`). Bật sẵn bộ đo tài nguyên: `minikube addons enable metrics-server`.
>
> 🎁 **Cuối ngày bạn có gì:** app có 3 loại probe hoạt động (bạn sẽ **tự làm nó "ốm"** để xem K8s phản ứng), và một HPA tự nhân bản pod khi bạn đổ tải vào — rồi tự thu lại khi hết tải.

### 📘 Lý thuyết

#### 1. Vấn đề: "Running" không có nghĩa là "phục vụ được"

Pod hiện `Running` chỉ nghĩa là **tiến trình chưa chết**. Nhưng app có thể:

- đang khởi động, chưa nạp xong cấu hình (30 giây nữa mới sẵn sàng);
- mất kết nối tới database, nhận request nào lỗi request đó;
- treo hoàn toàn (deadlock) nhưng tiến trình vẫn còn sống nhăn.

Trong cả ba trường hợp, K8s vẫn thản nhiên gửi người dùng vào — vì với nó, pod đang `Running`. **Probe** chính là cách bạn dạy K8s phân biệt "còn thở" với "phục vụ được".

#### 2. Ba loại probe — mỗi loại một câu hỏi khác nhau

| Probe | Câu hỏi | Trả lời SAI thì K8s làm gì |
|---|---|---|
| **startupProbe** | *"Khởi động xong chưa?"* | Chờ tiếp, **tạm hoãn** hai probe kia |
| **readinessProbe** | *"Nhận khách được chưa?"* | **Rút pod khỏi Service** (ngừng gửi request), pod vẫn sống |
| **livenessProbe** | *"Còn cứu được không?"* | **Giết và tạo lại container** |

> 🔑 Phân biệt hai cái hay nhầm nhất:
> - **readiness** = *"tạm thời đừng gửi khách vào"* — pod vẫn được giữ lại, khoẻ lại thì tự nhận khách trở lại.
> - **liveness** = *"hết cứu, khai sinh lại từ đầu"* — container bị giết.
>
> Đặt nhầm liveness ở chỗ đáng lẽ dùng readiness là một lỗi **rất nguy hiểm**: database chậm 10 giây → liveness fail → K8s giết toàn bộ pod → khởi động lại đồng loạt → database càng quá tải → giết tiếp. Một sự cố nhỏ biến thành sập dây chuyền.

#### 3. Ba cách hỏi

```yaml
# 1) Gọi HTTP — phổ biến nhất cho web/API
httpGet:
  path: /health
  port: 3000

# 2) Thử mở cổng TCP — cho database, dịch vụ không nói HTTP
tcpSocket:
  port: 5432

# 3) Chạy lệnh trong container — linh hoạt nhất
exec:
  command: ["cat", "/tmp/san-sang"]
```

Các tham số đi kèm, hiểu đúng để không tự bắn vào chân:

| Tham số | Nghĩa | Gợi ý |
|---|---|---|
| `initialDelaySeconds` | Chờ bao lâu rồi mới bắt đầu hỏi | Nên dùng `startupProbe` thay cho việc đoán con số này |
| `periodSeconds` | Bao lâu hỏi lại một lần | 10s là hợp lý |
| `timeoutSeconds` | Chờ trả lời bao lâu thì coi là trượt | 1–3s |
| `failureThreshold` | Trượt mấy lần liên tiếp mới xử lý | 3 |

#### 4. requests và limits — hai con số hoàn toàn khác vai trò

| | `requests` | `limits` |
|---|---|---|
| Nghĩa | *"Pod này **cần tối thiểu** ngần này"* | *"Không được vượt quá ngần này"* |
| Ai dùng | **Scheduler** — để chọn node còn đủ chỗ | **Kernel** — để cưỡng chế lúc chạy |
| Vượt ngưỡng | — | RAM: **bị giết (OOMKilled)** · CPU: **bị bóp chậm lại (throttle)** |

Ba lớp ưu tiên (**QoS**) sinh ra từ hai con số này, quyết định **ai bị hy sinh trước khi node hết RAM**:

| Lớp | Điều kiện | Khi node cạn RAM |
|---|---|---|
| **Guaranteed** | requests = limits (cả CPU lẫn RAM) | Bị giết **cuối cùng** |
| **Burstable** | Có requests, limits khác hoặc thiếu | Ở giữa |
| **BestEffort** | Không khai gì cả | **Bị giết đầu tiên** |

> ⚠️ Không khai `requests` nghĩa là pod của bạn tự nguyện xếp hàng đầu tiên trong danh sách hy sinh. Đây là lý do Ngày 36 đã nhấn mạnh: **luôn khai requests**.

#### 5. Một điểm gây tranh cãi: có nên đặt `limits` cho CPU?

Đặt **limits RAM** thì gần như luôn đúng — RAM là tài nguyên không nén được, một pod rò rỉ bộ nhớ có thể kéo sập cả node.

Nhưng **limits CPU** thì khác. CPU là tài nguyên **nén được**: vượt ngưỡng không bị giết, chỉ bị **bóp chậm lại**. Thực tế nhiều đội đã bỏ CPU limit vì nó gây độ trễ bất thường ngay cả khi node đang rảnh rỗi — pod bị bóp trong khi CPU còn thừa.

Khuyến nghị thực dụng hiện nay:

- **Luôn** đặt `requests` cho cả CPU và RAM.
- **Luôn** đặt `limits` cho RAM.
- **Cân nhắc** với `limits` CPU: nên có ở môi trường dùng chung/nhiều khách thuê; có thể bỏ ở dịch vụ nhạy cảm về độ trễ — nhưng khi đó phải giám sát chặt.

#### 6. HPA — tự tăng giảm số pod theo tải

**HPA** (Horizontal Pod Autoscaler) theo dõi mức sử dụng và tự điều chỉnh `replicas`:

```text
  CPU trung bình > mục tiêu   →  thêm pod
  CPU trung bình < mục tiêu   →  bớt pod (sau thời gian chờ ổn định)
```

Công thức nó dùng, đơn giản đến bất ngờ:

```text
số pod mong muốn = ceil( số pod hiện tại × (mức đo được / mức mục tiêu) )
```

Ví dụ: 2 pod, CPU trung bình 90%, mục tiêu 50% → `ceil(2 × 90/50)` = `ceil(3.6)` = **4 pod**.

> ⚠️ **HPA tính phần trăm theo `requests`, không theo dung lượng của node.** Pod khai `requests: 100m` mà đang dùng `90m` thì HPA hiểu là **90%** — dù node còn rảnh 90%. Không khai `requests` thì HPA **không hoạt động được**.

### 🧪 LAB — Làm app "ốm" và xem K8s tự chữa

**File sẽ tạo:**

```text
lab41-health/
├── app-probe.yaml      # Deployment đủ 3 probe + Service
└── hpa-demo.yaml       # App tốn CPU + HPA
```

#### File 1 — `app-probe.yaml`

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: web-khoe
spec:
  replicas: 2
  selector:
    matchLabels:
      app: web-khoe
  template:
    metadata:
      labels:
        app: web-khoe
    spec:
      containers:
        - name: web
          image: nginx:1.27
          ports:
            - containerPort: 80

          # Tạo 2 file làm "công tắc sức khoẻ" để lát nữa ta tự tay tắt
          command: ["/bin/sh", "-c"]
          args:
            - echo "OK" > /usr/share/nginx/html/khoe.html
              && echo "SAN SANG" > /usr/share/nginx/html/san-sang.html
              && echo "Xin chào từ $HOSTNAME" > /usr/share/nginx/html/index.html
              && nginx -g 'daemon off;'

          # 1) Khởi động xong chưa? Cho tối đa 30 x 2 = 60 giây
          startupProbe:
            httpGet:
              path: /khoe.html
              port: 80
            periodSeconds: 2
            failureThreshold: 30

          # 2) Nhận khách được chưa? Trượt -> RÚT KHỎI SERVICE (không giết)
          readinessProbe:
            httpGet:
              path: /san-sang.html
              port: 80
            periodSeconds: 5
            timeoutSeconds: 2
            failureThreshold: 2

          # 3) Còn cứu được không? Trượt -> GIẾT VÀ TẠO LẠI
          livenessProbe:
            httpGet:
              path: /khoe.html
              port: 80
            periodSeconds: 10
            timeoutSeconds: 2
            failureThreshold: 3

          resources:
            requests:
              memory: "64Mi"
              cpu: "50m"
            limits:
              memory: "128Mi"      # limits RAM: có. limits CPU: cố ý không đặt (mục 5)
---
apiVersion: v1
kind: Service
metadata:
  name: web-khoe-svc
spec:
  selector:
    app: web-khoe
  ports:
    - port: 80
      targetPort: 80
```

#### File 2 — `hpa-demo.yaml`

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: tinh-nang
spec:
  replicas: 1
  selector:
    matchLabels:
      app: tinh-nang
  template:
    metadata:
      labels:
        app: tinh-nang
    spec:
      containers:
        - name: tinh-nang
          image: registry.k8s.io/hpa-example    # app mẫu chính thức: mỗi request tính toán nặng
          ports:
            - containerPort: 80
          resources:
            requests:
              cpu: "100m"        # BẮT BUỘC có — HPA tính % dựa trên con số này
              memory: "64Mi"
            limits:
              memory: "128Mi"
---
apiVersion: v1
kind: Service
metadata:
  name: tinh-nang-svc
spec:
  selector:
    app: tinh-nang
  ports:
    - port: 80
      targetPort: 80
---
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: tinh-nang-hpa
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: tinh-nang
  minReplicas: 1
  maxReplicas: 8
  metrics:
    - type: Resource
      resource:
        name: cpu
        target:
          type: Utilization
          averageUtilization: 50      # giữ CPU trung bình quanh 50% của requests
  behavior:
    scaleDown:
      stabilizationWindowSeconds: 60  # chờ 60s ổn định rồi mới thu bớt, tránh giật cục
```

### 🧭 Hướng dẫn làm LAB — step by step

#### Bước 1 — Bật bộ đo tài nguyên

```bash
minikube addons enable metrics-server
kubectl -n kube-system rollout status deployment/metrics-server
kubectl top nodes
```

**Bạn sẽ thấy** (chờ ~1 phút để có số liệu đầu tiên):
```text
NAME       CPU(cores)   CPU%   MEMORY(bytes)   MEMORY%
minikube   243m         12%    1420Mi          46%
```

✅ **Checkpoint:** `kubectl top nodes` ra số, không báo lỗi.

⚠️ **Nếu báo `Metrics API not available`:** metrics-server chưa sẵn sàng, chờ thêm 1 phút. Không có nó thì **HPA không chạy được** — nó không biết lấy số ở đâu.

#### Bước 2 — Triển khai app có đủ 3 probe

```bash
mkdir -p ~/lab41-health && cd ~/lab41-health
# tạo app-probe.yaml theo phần LAB
kubectl apply -f app-probe.yaml
kubectl get pods -l app=web-khoe
kubectl get endpoints web-khoe-svc
```

**Bạn sẽ thấy:**
```text
NAME                        READY   STATUS    RESTARTS   AGE
web-khoe-6b7d8f9c4-h2xk9    1/1     Running   0          20s
web-khoe-6b7d8f9c4-p8mlt    1/1     Running   0          20s

NAME           ENDPOINTS
web-khoe-svc   10.244.0.21:80,10.244.0.22:80
```

✅ **Checkpoint:** `READY` là `1/1` cho cả hai pod, và Service có **2 endpoint**.

💡 Cột `READY 1/1` nghĩa là **readinessProbe đang đạt**. Nếu readiness trượt, cột này thành `0/1` dù `STATUS` vẫn là `Running` — hai cột nói hai chuyện khác nhau.

#### Bước 3 — Tắt công tắc "sẵn sàng" và xem pod bị rút khỏi Service

Đây là bước làm rõ ranh giới readiness/liveness.

```bash
POD=$(kubectl get pods -l app=web-khoe -o jsonpath='{.items[0].metadata.name}')
kubectl exec $POD -- rm /usr/share/nginx/html/san-sang.html
sleep 12
kubectl get pods -l app=web-khoe
kubectl get endpoints web-khoe-svc
```

**Bạn sẽ thấy:**
```text
NAME                        READY   STATUS    RESTARTS   AGE
web-khoe-6b7d8f9c4-h2xk9    0/1     Running   0          2m      ← READY tụt xuống 0/1
web-khoe-6b7d8f9c4-p8mlt    1/1     Running   0          2m

NAME           ENDPOINTS
web-khoe-svc   10.244.0.22:80                                    ← chỉ còn 1 địa chỉ
```

✅ **Checkpoint:** pod vẫn `Running`, `RESTARTS` vẫn `0`, nhưng đã **bị loại khỏi danh sách nhận khách**.

💡 **Đây chính xác là điều bạn muốn khi app tạm thời bận:** người dùng không bị ném vào pod đang có vấn đề, nhưng pod không bị giết oan — khoẻ lại là tự động nhận khách trở lại.

Bật lại công tắc:
```bash
kubectl exec $POD -- sh -c 'echo "SAN SANG" > /usr/share/nginx/html/san-sang.html'
sleep 8
kubectl get endpoints web-khoe-svc        # 2 địa chỉ trở lại
```

✅ **Checkpoint:** pod tự quay lại Service mà không cần ai can thiệp.

#### Bước 4 — Tắt công tắc "còn sống" và xem container bị khai sinh lại

```bash
kubectl exec $POD -- rm /usr/share/nginx/html/khoe.html

# Theo dõi trực tiếp — sẽ mất khoảng 30 giây (3 lần trượt x 10 giây)
kubectl get pods -l app=web-khoe -w
```

**Bạn sẽ thấy** (bấm `Ctrl+C` để thoát sau khi quan sát xong):
```text
web-khoe-6b7d8f9c4-h2xk9   1/1   Running   0     3m
web-khoe-6b7d8f9c4-h2xk9   0/1   Running   1     3m30s     ← RESTARTS nhảy lên 1
web-khoe-6b7d8f9c4-h2xk9   1/1   Running   1     3m35s     ← khoẻ lại, nhận khách tiếp
```

Xem K8s nói gì:
```bash
kubectl describe pod $POD | grep -A6 Events
```

**Bạn sẽ thấy:**
```text
  Warning  Unhealthy  35s   kubelet  Liveness probe failed: HTTP probe failed with statuscode: 404
  Normal   Killing    35s   kubelet  Container web failed liveness probe, will be restarted
```

✅ **Checkpoint:** `RESTARTS` tăng lên `1`, và log ghi rõ lý do là liveness probe trượt.

💡 **So sánh hai bước vừa rồi — đây là bài học cốt lõi hôm nay:**

| | Bước 3 (readiness trượt) | Bước 4 (liveness trượt) |
|---|---|---|
| Pod bị làm gì | Rút khỏi Service | **Container bị giết và tạo lại** |
| `RESTARTS` | 0 | 1 |
| Trạng thái bên trong | Giữ nguyên | **Mất sạch** (bộ nhớ, kết nối, file tạm) |

💡 Chú ý pod tự khoẻ lại sau khi restart — vì container mới chạy lại `args` và tạo lại file. Đó cũng là điều xảy ra ngoài đời: khởi động lại thường chữa được lỗi tạm thời.

#### Bước 5 — Nhìn thấy `limits` RAM cưỡng chế thật

```bash
kubectl run an-ram --image=polinux/stress --restart=Never \
  --overrides='{"spec":{"containers":[{"name":"an-ram","image":"polinux/stress","resources":{"limits":{"memory":"64Mi"}},"command":["stress","--vm","1","--vm-bytes","200M","--vm-hang","1"]}]}}'

sleep 20
kubectl get pod an-ram
kubectl describe pod an-ram | grep -E "Reason|Exit Code|OOM"
```

**Bạn sẽ thấy:**
```text
NAME     READY   STATUS      RESTARTS   AGE
an-ram   0/1     OOMKilled   0          20s

      Reason:       OOMKilled
      Exit Code:    137
```

✅ **Checkpoint:** thấy đúng chữ **`OOMKilled`** và mã thoát **137**.

💡 **Ghi nhớ cặp dấu hiệu này** — `OOMKilled` + `Exit Code 137` là một trong những sự cố K8s phổ biến nhất bạn sẽ gặp. Nó có nghĩa: container xin 200MB trong khi limits chỉ cho 64MB → kernel giết ngay lập tức, không thương lượng.

```bash
kubectl delete pod an-ram
```

#### Bước 6 — Dựng app cho HPA và xem trạng thái ban đầu

```bash
# tạo hpa-demo.yaml theo phần LAB
kubectl apply -f hpa-demo.yaml
kubectl rollout status deployment/tinh-nang
sleep 45                      # chờ metrics-server thu số liệu đầu tiên
kubectl get hpa
```

**Bạn sẽ thấy:**
```text
NAME            REFERENCE              TARGETS        MINPODS   MAXPODS   REPLICAS
tinh-nang-hpa   Deployment/tinh-nang   cpu: 0%/50%    1         8         1
```

✅ **Checkpoint:** cột `TARGETS` hiện **số phần trăm**, không phải `<unknown>`.

⚠️ **Nếu là `<unknown>`:** hoặc metrics-server chưa sẵn sàng, hoặc **pod chưa khai `requests.cpu`**. Không có `requests` thì HPA không có mẫu số để tính phần trăm.

#### Bước 7 — Đổ tải vào và xem pod tự nhân lên

Mở **hai terminal**.

**Terminal 1** — theo dõi:
```bash
kubectl get hpa tinh-nang-hpa -w
```

**Terminal 2** — tạo tải liên tục:
```bash
kubectl run tao-tai --rm -it --image=busybox:1.36 --restart=Never -- \
  /bin/sh -c "while true; do wget -q -O- http://tinh-nang-svc > /dev/null; done"
```

**Bạn sẽ thấy ở Terminal 1** (sau khoảng 1–3 phút):
```text
NAME            TARGETS         REPLICAS
tinh-nang-hpa   cpu: 0%/50%     1
tinh-nang-hpa   cpu: 178%/50%   1        ← tải tăng vọt
tinh-nang-hpa   cpu: 178%/50%   4        ← HPA nhân lên 4 pod
tinh-nang-hpa   cpu: 89%/50%    4
tinh-nang-hpa   cpu: 89%/50%    7        ← vẫn cao, tăng tiếp
tinh-nang-hpa   cpu: 47%/50%    7        ← ổn định quanh mục tiêu
```

```bash
kubectl get pods -l app=tinh-nang
```

✅ **Checkpoint:** số pod tăng từ 1 lên nhiều pod, và CPU trung bình hạ dần về gần 50%.

💡 Đối chiếu với công thức ở Lý thuyết #6: 1 pod × (178/50) = 3,56 → làm tròn lên **4 pod**. Con số HPA chọn không hề bí ẩn — bạn tính tay ra được.

#### Bước 8 — Ngắt tải và quan sát chiều ngược lại

Ở Terminal 2, bấm `Ctrl+C` để dừng tạo tải. Tiếp tục nhìn Terminal 1.

**Bạn sẽ thấy** (sau khoảng 1–2 phút, chậm hơn lúc tăng):
```text
tinh-nang-hpa   cpu: 0%/50%    7
tinh-nang-hpa   cpu: 0%/50%    3
tinh-nang-hpa   cpu: 0%/50%    1
```

✅ **Checkpoint:** số pod giảm dần về `minReplicas: 1`.

💡 **Vì sao thu lại chậm hơn lúc tăng:** đó là chủ ý (`stabilizationWindowSeconds: 60`). Tải thật thường lên xuống thất thường; nếu thu ngay thì hệ thống sẽ liên tục tạo-xoá pod (hiện tượng *thrashing*). Nguyên tắc: **tăng nhanh để cứu người dùng, giảm chậm để chắc chắn**.

#### Bước 9 — Dọn dẹp

```bash
kubectl delete -f hpa-demo.yaml -f app-probe.yaml
minikube stop
```

### 💡 Đi làm mới thấm (sách cơ bản hay bỏ quên)

- **livenessProbe đặt sai còn tệ hơn không đặt.** Kịch bản thật hay xảy ra: database chậm → mọi pod trượt liveness cùng lúc → K8s giết sạch → khởi động lại đồng loạt → database càng ngộp → vòng xoáy chết. Quy tắc an toàn: **liveness chỉ kiểm tra chính tiến trình đó còn sống hay không**, tuyệt đối **không** gọi sang database hay dịch vụ ngoài. Việc kiểm tra phụ thuộc là của *readiness*.
- **`startupProbe` sinh ra để bạn khỏi phải đoán `initialDelaySeconds`.** App khởi động chậm (JVM, nạp mô hình) mà đặt delay quá ngắn thì bị giết ngay khi đang khởi động; đặt quá dài thì lỗi thật cũng chậm phát hiện. `startupProbe` cho một khoảng rộng lúc khởi động, sau đó trả lại nhịp kiểm tra bình thường.
- **HPA và VPA xung đột nhau trên cùng một chỉ số.** HPA thêm *số lượng* pod, VPA đổi *kích cỡ* pod. Cùng nhìn CPU thì hai cái đánh nhau. Dùng chung phải tách chỉ số rõ ràng.
- **HPA không cứu được nghẽn ở database.** Nhân pod lên 10 lần chỉ khiến 10 lần số kết nối đổ vào cùng một database đang ngộp. Trước khi bật HPA, hãy biết **điểm nghẽn thật sự nằm ở đâu**.
- **Cluster Autoscaler là tầng khác.** HPA thêm pod; nếu node không còn chỗ, pod mới nằm `Pending` mãi. Muốn tự thêm **máy** thì cần Cluster Autoscaler (cloud) hoặc Karpenter. Nhiều người tưởng HPA lo cả hai.
- **PodDisruptionBudget bảo vệ bạn lúc bảo trì.** Khi node được nâng cấp, K8s sẽ dồn pod đi nơi khác — không có PDB thì nó có thể xoá cùng lúc mọi bản sao của bạn. Khai `minAvailable: 1` là đủ tránh một sự cố rất vô duyên.

### 📝 Tự kiểm tra

> Nghĩ câu trả lời **thành lời** trước khi mở đáp án — nghĩ thầm luôn thấy mình hiểu.

<details>
<summary><b>1. Phân biệt readinessProbe và livenessProbe. Hậu quả khi đặt nhầm là gì?</b></summary>

| | readiness | liveness |
|---|---|---|
| Hỏi gì | *'Nhận khách được chưa?'* | *'Còn cứu được không?'* |
| Trượt thì sao | **Rút pod khỏi Service** | **Giết và tạo lại container** |
| `RESTARTS` | Không tăng | Tăng |

**Hậu quả khi đặt nhầm:** nếu liveness kiểm tra kết nối tới database, thì khi database chậm đi, **mọi pod trượt liveness cùng lúc** → K8s giết sạch → khởi động lại đồng thời → database càng ngộp → vòng xoáy chết. Một sự cố nhỏ thành sập toàn hệ thống.

Quy tắc: **liveness chỉ kiểm tra chính tiến trình đó**; kiểm tra phụ thuộc bên ngoài là việc của readiness.

</details>

<details>
<summary><b>2. `requests` và `limits` khác nhau thế nào về vai trò? Ai dùng con số nào?</b></summary>

- **`requests`** = *'pod này cần tối thiểu ngần này'*. **Scheduler** dùng nó để chọn node còn đủ chỗ. Đây cũng là con số bạn **trả tiền**.
- **`limits`** = *'không được vượt quá'*. **Kernel** cưỡng chế lúc chạy.

Vượt ngưỡng: RAM → **bị giết (OOMKilled, Exit 137)**; CPU → **bị bóp chậm lại (throttle)**, không bị giết.

Ba lớp QoS sinh ra từ hai con số này, quyết định ai bị hy sinh trước khi node cạn RAM: **Guaranteed** (requests=limits) bị giết cuối, **BestEffort** (không khai gì) bị giết **đầu tiên**.

</details>

<details>
<summary><b>3. HPA báo `<unknown>` ở cột TARGETS. Hai nguyên nhân có thể là gì?</b></summary>

1. **metrics-server chưa chạy** — HPA không có nguồn số liệu. Kiểm tra bằng `kubectl top nodes`.
2. **Pod chưa khai `requests.cpu`** — HPA tính phần trăm **dựa trên requests**, không có requests thì không có mẫu số để chia.

Điểm quan trọng hay bị hiểu nhầm: HPA tính % theo `requests`, **không** theo dung lượng node. Pod khai `requests: 100m` mà dùng `90m` thì HPA hiểu là **90%** — dù node còn rảnh 90%.

</details>

### 📚 Thuật ngữ Anh–Việt (ngày này)

| Thuật ngữ | Nghĩa |
|---|---|
| **startupProbe** | Hỏi 'khởi động xong chưa?' — tạm hoãn hai probe kia trong lúc app đang lên |
| **readinessProbe** | Hỏi 'nhận khách được chưa?' — trượt thì **rút khỏi Service**, pod vẫn sống |
| **livenessProbe** | Hỏi 'còn cứu được không?' — trượt thì **giết và tạo lại container** |
| **`requests`** | Tài nguyên đặt chỗ; Scheduler dùng để xếp node, HPA dùng làm mẫu số |
| **`limits`** | Trần cứng; vượt RAM → OOMKilled, vượt CPU → bị bóp chậm |
| **OOMKilled / Exit 137** | Container bị kernel giết vì vượt limits RAM |
| **QoS class** | Guaranteed / Burstable / BestEffort — quyết định ai bị giết trước khi cạn RAM |
| **HPA** | Tự tăng giảm **số pod** theo tải; cần metrics-server và requests |
| **Cluster Autoscaler** | Tự thêm **node** khi pod không còn chỗ — tầng khác với HPA |
| **PodDisruptionBudget** | Đảm bảo tối thiểu N pod sống khi node được bảo trì |

### 🎯 Đúc kết Ngày 41

**3 điều phải mang theo:**

1. **`Running` ≠ phục vụ được.** Probe là cách duy nhất để K8s hiểu app bạn thật sự khoẻ hay không.
2. **readiness rút khỏi Service, liveness giết container.** Nhầm hai cái này có thể biến một sự cố nhỏ thành sập dây chuyền.
3. **`requests` là nền của mọi thứ** — Scheduler dùng nó để xếp chỗ, HPA dùng nó làm mẫu số, QoS dùng nó để quyết định ai bị hy sinh trước.

> 🧠 **Một câu để nhớ:** readiness bảo *"khoan hãy gửi khách vào"*; liveness bảo *"hết cứu, làm lại từ đầu"*. Chọn nhầm chữ là chọn nhầm hậu quả.

**✅ Tự chấm** *(đánh dấu khi làm được mà không nhìn tài liệu):*

- [ ] Phân biệt 3 loại probe và nói rõ K8s làm gì khi từng loại trượt
- [ ] Tự làm readiness trượt và chứng minh pod bị rút khỏi endpoints
- [ ] Tự làm liveness trượt và chỉ ra `RESTARTS` tăng cùng lý do trong Events
- [ ] Giải thích vì sao liveness không được gọi sang database
- [ ] Nhận diện `OOMKilled` / `Exit Code 137` và biết nguyên nhân
- [ ] Nói được 3 lớp QoS và ai bị giết trước khi node cạn RAM
- [ ] Dựng HPA, tạo tải, và tính tay ra được số pod mà HPA sẽ chọn

✅ **Kết quả đạt được:** Ứng dụng biết tự báo cáo sức khoẻ và cụm biết tự co giãn theo tải — hai điều kiện để một hệ thống chạy được qua đêm mà không cần ai trực.

---

## Ngày 42 — Helm: Package Manager cho Kubernetes

> ⏱️ ~90 phút · Loại: Kubernetes
>
> 🧭 **Bạn đang ở đâu:** Ngày 41 (probe, tài nguyên, autoscaling) → **Ngày 42 (đóng gói tất cả YAML đó thành một gói cài được)** → Ngày 43 (GitOps tự đồng bộ từ Git). Đến giờ bạn đã có cả chục file YAML rời rạc — hôm nay biến chúng thành một thứ cài bằng **một lệnh**.
>
> ✅ **Chuẩn bị:** cluster đang chạy (`minikube start`).
>
> 🎁 **Cuối ngày bạn có gì:** một **chart Helm của riêng bạn** cài được vào bất kỳ cluster nào với cấu hình khác nhau cho từng môi trường, kèm khả năng **nâng cấp và quay lui bằng một lệnh**.

### 📘 Lý thuyết

#### 1. Vấn đề: YAML sinh sôi rất nhanh

Hệ thống nhỏ ở Ngày 40 đã cần: Deployment, Service, Ingress, ConfigMap, Secret, PVC, HPA — **7 file cho một ứng dụng**. Giờ nhân lên:

- 3 môi trường (dev / staging / production) → **21 file**, khác nhau vài dòng.
- Đổi tag image → sửa tay ở 3 chỗ, quên một chỗ là môi trường lệch nhau.
- Người mới vào đội hỏi "cài hệ thống này thế nào?" → *"apply 21 file, theo đúng thứ tự này..."*.

Helm giải đúng bài toán ấy, y như `apt` đã làm với Linux:

| | Không có Helm | Có Helm |
|---|---|---|
| Cài | `kubectl apply` từng file, đúng thứ tự | `helm install cuahang ./chart` |
| Khác biệt giữa môi trường | Copy cả bộ file rồi sửa tay | Một bộ khuôn + nhiều file `values` |
| Nâng cấp | Sửa file, apply lại, tự theo dõi | `helm upgrade` |
| Quay lui | Tự tìm lại YAML cũ trong Git | `helm rollback cuahang 1` |
| Gỡ bỏ | Nhớ và xoá từng thứ | `helm uninstall cuahang` |

#### 2. Ba khái niệm phải phân biệt

| Khái niệm | Là gì | Ví dụ tương đương |
|---|---|---|
| **Chart** | Gói khuôn mẫu (template + giá trị mặc định) | File cài đặt `.deb` |
| **Values** | Giá trị bạn truyền vào để điền chỗ trống | Tuỳ chọn khi cài |
| **Release** | **Một lần cài** chart vào cluster, có tên riêng | Phần mềm đã cài xong |

Một chart có thể cài nhiều lần thành nhiều release khác nhau: `helm install shop-dev ./chart` và `helm install shop-prod ./chart` — cùng khuôn, khác cấu hình, sống song song.

#### 3. Cấu trúc một chart

```text
chart-cua-toi/
├── Chart.yaml          # Tên, phiên bản chart, mô tả
├── values.yaml         # GIÁ TRỊ MẶC ĐỊNH — nơi người dùng chart cần đọc
├── templates/          # YAML có chỗ trống chờ điền
│   ├── deployment.yaml
│   ├── service.yaml
│   ├── ingress.yaml
│   ├── _helpers.tpl    # hàm dùng lại (đặt tên, nhãn chuẩn)
│   └── NOTES.txt       # lời nhắn in ra sau khi cài xong
└── charts/             # chart phụ thuộc (vd: postgresql)
```

#### 4. Cú pháp template — chỉ cần bốn thứ

```yaml
# 1) Lấy giá trị từ values.yaml
image: {{ .Values.image.repository }}:{{ .Values.image.tag }}

# 2) Thông tin về release/chart
name: {{ .Release.Name }}-web        # .Release.Name = tên bạn đặt lúc install

# 3) Có điều kiện — chỉ sinh ra khi được bật
{{- if .Values.ingress.enabled }}
...phần Ingress...
{{- end }}

# 4) Lặp
{{- range .Values.hosts }}
  - host: {{ . }}
{{- end }}
```

> 📌 Dấu `-` trong `{{-` nghĩa là "nuốt khoảng trắng phía trước". Thiếu nó thì YAML sinh ra đầy dòng trống và **sai thụt lề** — lỗi khó chịu nhất khi mới viết chart. Bước 6 sẽ cho bạn cách nhìn thấy kết quả trước khi cài.

#### 5. Nâng cấp và quay lui — Helm nhớ giúp bạn

Mỗi lần `helm upgrade`, Helm lưu lại một **revision**. Muốn quay lui thì không cần tìm YAML cũ:

```bash
helm history cuahang        # xem các đời đã qua
helm rollback cuahang 2     # quay về đời số 2
```

Đây là lợi ích rất thực tế mà `kubectl apply` thuần không có.

### 🧪 LAB — Dùng chart người khác, rồi tự viết chart của mình

**Phần A:** cài một chart có sẵn để hiểu cách dùng.
**Phần B:** tự tạo chart cho ứng dụng của bạn.

### 🧭 Hướng dẫn làm LAB — step by step

#### Bước 1 — Cài Helm

```bash
curl -fsSL https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3 | bash
helm version
```

**Bạn sẽ thấy:**
```text
version.BuildInfo{Version:"v3.16.x", GitCommit:"...", GoVersion:"go1.22.x"}
```

✅ **Checkpoint:** in ra `Version:"v3.x"`.

💡 Chỉ cần nhớ **Helm 3**. Helm 2 có một thành phần chạy trong cluster tên Tiller với quyền rất lớn — đã bị khai tử vì lý do bảo mật. Tài liệu cũ nào nhắc tới Tiller thì bỏ qua.

#### Bước 2 — Cài một chart có sẵn

```bash
helm repo add podinfo https://stefanprodan.github.io/podinfo
helm repo update
helm search repo podinfo
```

**Bạn sẽ thấy:**
```text
NAME            CHART VERSION   APP VERSION   DESCRIPTION
podinfo/podinfo 6.7.x           6.7.x         Podinfo Helm chart for Kubernetes
```

Trước khi cài, hãy xem chart này cho phép chỉnh những gì:

```bash
helm show values podinfo/podinfo | head -25
```

✅ **Checkpoint:** thấy danh sách giá trị mặc định (`replicaCount`, `image`, `service`...).

💡 **`helm show values` là việc đầu tiên nên làm với bất kỳ chart lạ nào.** Nó là "bảng điều khiển" — cho biết bạn được phép đổi gì mà không phải đọc template.

Giờ cài:

```bash
helm install demo podinfo/podinfo --set replicaCount=2
kubectl get pods -l app.kubernetes.io/name=podinfo
helm list
```

**Bạn sẽ thấy:**
```text
NAME    NAMESPACE   REVISION   STATUS     CHART           APP VERSION
demo    default     1          deployed   podinfo-6.7.x   6.7.x
```

✅ **Checkpoint:** `STATUS` là `deployed`, `REVISION` là `1`, và có **2 pod** đang chạy.

💡 Một lệnh vừa tạo ra Deployment + Service + mọi thứ chart định nghĩa. Đây chính là điều Helm mang lại so với việc apply từng file.

#### Bước 3 — Nâng cấp và quay lui

```bash
helm upgrade demo podinfo/podinfo --set replicaCount=4
kubectl get pods -l app.kubernetes.io/name=podinfo --no-headers | wc -l
helm history demo
```

**Bạn sẽ thấy:**
```text
4

REVISION   STATUS       DESCRIPTION
1          superseded   Install complete
2          deployed     Upgrade complete
```

Giờ quay lui:

```bash
helm rollback demo 1
sleep 5
kubectl get pods -l app.kubernetes.io/name=podinfo --no-headers | wc -l
helm history demo
```

**Bạn sẽ thấy:**
```text
2

REVISION   STATUS       DESCRIPTION
1          superseded   Install complete
2          superseded   Upgrade complete
3          deployed     Rollback to 1
```

✅ **Checkpoint:** số pod về lại 2, và lịch sử ghi rõ `Rollback to 1`.

💡 Để ý rollback **không xoá lịch sử** mà tạo thêm revision 3. Nhờ vậy bạn luôn biết chuyện gì đã xảy ra — rất quan trọng khi mổ xẻ sự cố.

Dọn:
```bash
helm uninstall demo
```

#### Bước 4 — Tạo chart của riêng bạn

```bash
cd ~
helm create cuahang
find cuahang -type f | sort
```

**Bạn sẽ thấy:**
```text
cuahang/.helmignore
cuahang/Chart.yaml
cuahang/charts
cuahang/templates/NOTES.txt
cuahang/templates/_helpers.tpl
cuahang/templates/deployment.yaml
cuahang/templates/hpa.yaml
cuahang/templates/ingress.yaml
cuahang/templates/service.yaml
cuahang/templates/serviceaccount.yaml
cuahang/templates/tests/test-connection.yaml
cuahang/values.yaml
```

✅ **Checkpoint:** có đủ `Chart.yaml`, `values.yaml` và thư mục `templates/`.

💡 `helm create` dựng sẵn một chart mẫu **đầy đủ chuẩn thực hành tốt** (probe, HPA, service account, nhãn chuẩn). Ở công ty người ta hầu như luôn bắt đầu từ đây rồi sửa, chứ ít khi viết từ con số không.

#### Bước 5 — Sửa `values.yaml` cho ứng dụng của bạn

Thay toàn bộ `cuahang/values.yaml` bằng:

```yaml
replicaCount: 2

image:
  repository: nginx
  tag: "1.27"                 # tag cụ thể, không dùng latest
  pullPolicy: IfNotPresent

service:
  type: ClusterIP
  port: 80

ingress:
  enabled: false              # mặc định tắt; môi trường nào cần thì bật
  className: nginx
  hosts:
    - host: cuahang.local
      paths:
        - path: /
          pathType: Prefix

resources:
  requests:
    cpu: 50m
    memory: 64Mi
  limits:
    memory: 128Mi

autoscaling:
  enabled: false
  minReplicas: 2
  maxReplicas: 8
  targetCPUUtilizationPercentage: 50

# Giá trị riêng của ứng dụng — sẽ được tiêm vào pod làm biến môi trường
ungDung:
  tenCuaHang: "Cửa hàng ABC"
  moiTruong: "dev"

serviceAccount:
  create: true
  name: ""

podSecurityContext: {}
securityContext: {}
nodeSelector: {}
tolerations: []
affinity: {}
```

Rồi thêm phần biến môi trường vào `cuahang/templates/deployment.yaml`. Tìm khối `ports:` trong container và **thêm ngay dưới nó**:

```yaml
          env:
            - name: TEN_CUA_HANG
              value: {{ .Values.ungDung.tenCuaHang | quote }}
            - name: MOI_TRUONG
              value: {{ .Values.ungDung.moiTruong | quote }}
            - name: TEN_RELEASE
              value: {{ .Release.Name | quote }}
```

> 📌 `| quote` tự thêm dấu nháy. Thiếu nó, giá trị như `dev` vẫn ổn nhưng `"20"` hay `true` sẽ bị YAML hiểu thành số/boolean và gây lỗi kiểu dữ liệu. **Thói quen tốt: mọi giá trị chuỗi đều `| quote`.**

#### Bước 6 — Xem trước kết quả TRƯỚC khi cài (bước quan trọng nhất)

```bash
helm lint ./cuahang
```

**Bạn sẽ thấy:**
```text
==> Linting ./cuahang
1 chart(s) linted, 0 chart(s) failed
```

Giờ xem YAML thật sự sẽ được sinh ra:

```bash
helm template thu-nghiem ./cuahang | head -40
```

**Bạn sẽ thấy** YAML hoàn chỉnh với mọi chỗ trống đã điền:
```text
apiVersion: v1
kind: ServiceAccount
metadata:
  name: thu-nghiem-cuahang
...
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: thu-nghiem-cuahang
spec:
  replicas: 2
...
          env:
            - name: TEN_CUA_HANG
              value: "Cửa hàng ABC"
```

✅ **Checkpoint:** thấy `{{ }}` đã được thay bằng giá trị thật, và tên có tiền tố `thu-nghiem-`.

💡 **`helm template` là công cụ gỡ lỗi số một khi viết chart.** Nó chạy **hoàn toàn ngoại tuyến**, không đụng tới cluster. Sai thụt lề hay sai tên biến lộ ra ngay tại đây, thay vì làm hỏng cluster rồi mới biết.

Thử đổi giá trị xem template phản ứng:
```bash
helm template thu-nghiem ./cuahang --set ingress.enabled=true | grep -A5 "kind: Ingress"
```

**Bạn sẽ thấy** phần Ingress xuất hiện — trong khi lúc nãy không có, vì `{{- if .Values.ingress.enabled }}` trả về false.

#### Bước 7 — Cài chart của bạn cho hai môi trường cùng lúc

Tạo file `values-prod.yaml` ngoài thư mục chart:

```yaml
replicaCount: 3

ungDung:
  moiTruong: "production"
  tenCuaHang: "Cửa hàng ABC - Chính thức"

autoscaling:
  enabled: true
  minReplicas: 3
  maxReplicas: 10

resources:
  requests:
    cpu: 100m
    memory: 128Mi
  limits:
    memory: 256Mi
```

Cài cả hai:

```bash
helm install shop-dev  ./cuahang
helm install shop-prod ./cuahang -f values-prod.yaml
helm list
kubectl get pods -l app.kubernetes.io/instance=shop-dev
kubectl get pods -l app.kubernetes.io/instance=shop-prod
```

**Bạn sẽ thấy:**
```text
NAME        REVISION   STATUS     CHART
shop-dev    1          deployed   cuahang-0.1.0
shop-prod   1          deployed   cuahang-0.1.0

(2 pod shop-dev...)
(3 pod shop-prod...)
```

Kiểm chứng cấu hình khác nhau thật:

```bash
kubectl exec deploy/shop-dev-cuahang  -- printenv MOI_TRUONG TEN_CUA_HANG
echo "---"
kubectl exec deploy/shop-prod-cuahang -- printenv MOI_TRUONG TEN_CUA_HANG
```

**Bạn sẽ thấy:**
```text
dev
Cửa hàng ABC
---
production
Cửa hàng ABC - Chính thức
```

✅ **Checkpoint:** **một chart duy nhất**, hai release sống song song với cấu hình khác nhau.

💡 **Đây là toàn bộ giá trị của Helm gói trong một màn hình.** Không copy file, không sửa tay, không lệch môi trường — chỉ khác nhau ở file values.

#### Bước 8 — Nâng cấp an toàn với `--atomic`

```bash
helm upgrade shop-prod ./cuahang -f values-prod.yaml \
  --set image.tag=1.27-alpine \
  --atomic --timeout 2m

helm history shop-prod
```

**Bạn sẽ thấy:**
```text
REVISION   STATUS       DESCRIPTION
1          superseded   Install complete
2          deployed     Upgrade complete
```

✅ **Checkpoint:** nâng cấp xong, revision lên `2`.

💡 **`--atomic` là thói quen nên có cho mọi lần upgrade production:** nếu bản mới không lên được trong thời gian `--timeout`, Helm **tự động quay lui** về bản cũ. Không có nó, bạn sẽ mắc kẹt ở trạng thái nửa vời — một nửa pod mới hỏng, một nửa pod cũ, và phải tự dọn.

Thử với một tag không tồn tại để thấy nó cứu bạn:
```bash
helm upgrade shop-prod ./cuahang -f values-prod.yaml \
  --set image.tag=khong-ton-tai-dau --atomic --timeout 60s
```

**Bạn sẽ thấy:**
```text
Error: UPGRADE FAILED: release shop-prod failed, and has been rolled back due to atomic being set: ...
```

```bash
kubectl get pods -l app.kubernetes.io/instance=shop-prod
helm history shop-prod
```

✅ **Checkpoint:** các pod **vẫn chạy bản cũ bình thường**, và lịch sử ghi lại lần thất bại + lần rollback tự động.

#### Bước 9 — Dọn dẹp

```bash
helm uninstall shop-dev shop-prod
helm list
minikube stop
```

**Bạn sẽ thấy:** danh sách release trống.

💡 Một lệnh `uninstall` gỡ sạch mọi thứ chart đã tạo — không sót Service hay ConfigMap mồ côi như khi xoá tay.

### 💡 Đi làm mới thấm (sách cơ bản hay bỏ quên)

- **`helm template` trước, `helm install` sau.** Luôn xem YAML sẽ sinh ra trước khi đụng vào cluster. Với production thì thêm `helm diff upgrade` (plugin `helm-diff`) để thấy **chính xác cái gì sắp đổi** — đây là bước mà người làm lâu năm không bao giờ bỏ qua.
- **Đừng để chart phụ thuộc kéo theo cả một database production.** Nhiều chart tiện tay gói luôn PostgreSQL/Redis làm chart con. Rất hợp cho lab, nhưng database production nên đứng ngoài, do dịch vụ quản lý của cloud lo — vòng đời của nó **không nên gắn với vòng đời một release ứng dụng**.
- **Ghim phiên bản chart, đừng chỉ ghim image.** `helm install ... --version 6.7.1`. Không ghim thì hôm nay cài ra một kiểu, tháng sau cài lại ra kiểu khác — đúng bài học `latest` của Ngày 33, chỉ là ở tầng chart.
- **Helm lưu trạng thái release trong Secret của namespace.** `kubectl get secret -l owner=helm` sẽ thấy. Xoá nhầm những Secret này là Helm mất trí nhớ về release đó. Biết để đừng "dọn dẹp" nhầm.
- **`--set` tiện nhưng chóng quên.** Giá trị truyền bằng `--set` không nằm trong Git → không ai biết production đang chạy cấu hình gì. Dùng `--set` khi thử nghiệm; với môi trường thật hãy để mọi thứ trong **file values được commit vào Git** (đây chính là tiền đề của GitOps ngày mai).
- **Chart của bạn cũng cần đánh phiên bản.** `Chart.yaml` có hai trường: `version` (phiên bản của *chart*) và `appVersion` (phiên bản của *ứng dụng*). Sửa template thì tăng `version`; đổi image thì đổi `appVersion`. Lẫn lộn hai cái là rắc rối về sau.

### 📝 Tự kiểm tra

> Nghĩ câu trả lời **thành lời** trước khi mở đáp án — nghĩ thầm luôn thấy mình hiểu.

<details>
<summary><b>1. Phân biệt chart, values và release.</b></summary>

- **Chart**: gói khuôn mẫu (template + giá trị mặc định) — như file cài đặt `.deb`
- **Values**: giá trị bạn truyền vào để điền chỗ trống — như tuỳ chọn khi cài
- **Release**: **một lần cài** chart vào cluster, có tên riêng — như phần mềm đã cài xong

Một chart cài được nhiều lần thành nhiều release: `helm install shop-dev ./chart` và `helm install shop-prod ./chart -f values-prod.yaml` — cùng khuôn, khác cấu hình, sống song song.

</details>

<details>
<summary><b>2. Vì sao luôn chạy `helm template` trước `helm install`?</b></summary>

Vì nó **render YAML thật sự sẽ được sinh ra** mà **không đụng tới cluster** — chạy hoàn toàn ngoại tuyến.

Sai thụt lề, sai tên biến, điều kiện `if` không như ý — tất cả lộ ra ngay tại đây, thay vì làm hỏng cluster rồi mới biết.

Với production, thêm `helm diff upgrade` (plugin) để thấy **chính xác cái gì sắp đổi**. Đây là bước người làm lâu năm không bao giờ bỏ qua — cùng tinh thần với `terraform plan` và `ansible --check`.

</details>

<details>
<summary><b>3. `helm upgrade --atomic` làm gì? Vì sao nên dùng cho production?</b></summary>

Nếu bản mới **không lên được** trong thời gian `--timeout`, Helm **tự động quay lui** về bản cũ.

Không có nó, bạn mắc kẹt ở trạng thái nửa vời: một nửa pod mới hỏng, một nửa pod cũ, và phải tự dọn bằng tay — đúng lúc đang căng thẳng.

Kiểm chứng dễ: `helm upgrade ... --set image.tag=khong-ton-tai --atomic` → Helm báo lỗi nhưng các pod **vẫn chạy bản cũ bình thường**, và lịch sử ghi lại cả lần thất bại lẫn lần rollback tự động.

</details>

### 📚 Thuật ngữ Anh–Việt (ngày này)

| Thuật ngữ | Nghĩa |
|---|---|
| **Chart** | Gói khuôn mẫu Kubernetes (templates + values mặc định) |
| **Values** | Giá trị truyền vào chart để điền chỗ trống |
| **Release** | Một lần cài chart vào cluster, có tên riêng |
| **Revision** | Mỗi lần upgrade tạo một đời mới — `helm history` xem, `helm rollback` quay lui |
| **`helm template`** | Render YAML ngoại tuyến, không đụng cluster — công cụ gỡ lỗi số một |
| **`helm lint`** | Kiểm tra chart hợp lệ trước khi cài |
| **`--atomic`** | Upgrade thất bại thì tự động quay lui về bản cũ |
| **`{{ .Values.x }}`** | Cú pháp lấy giá trị từ values.yaml trong template |
| **`{{-`** | Nuốt khoảng trắng phía trước — thiếu nó là sai thụt lề YAML |
| **`version` vs `appVersion`** | Phiên bản của *chart* vs phiên bản của *ứng dụng* |

### 🎯 Đúc kết Ngày 42

**3 điều phải mang theo:**

1. **Một chart + nhiều file values = nhiều môi trường** mà không nhân bản YAML. Hết cảnh "dev và prod lệch nhau mà không ai biết vì sao".
2. **`helm template` và `helm lint` chạy ngoại tuyến** — bắt lỗi trước khi đụng cluster. Đây là thói quen tách người mới với người đã làm thật.
3. **`helm upgrade --atomic` + `helm rollback`** biến việc nâng cấp thành thao tác có đường lui, thay vì một canh bạc.

> 🧠 **Một câu để nhớ:** Helm không làm K8s dễ hơn — nó làm **YAML của bạn ngừng nhân bản mất kiểm soát**.

**✅ Tự chấm** *(đánh dấu khi làm được mà không nhìn tài liệu):*

- [ ] Phân biệt chart / values / release
- [ ] Dùng `helm show values` để biết một chart lạ cho phép chỉnh gì
- [ ] Tạo chart riêng bằng `helm create` và sửa `values.yaml` theo ứng dụng
- [ ] Dùng `helm template` để xem YAML sinh ra và gỡ lỗi ngoại tuyến
- [ ] Cài một chart thành hai release với cấu hình khác nhau
- [ ] Nâng cấp bằng `--atomic` và chứng minh nó tự quay lui khi thất bại
- [ ] Xem `helm history` và rollback về một revision cụ thể

✅ **Kết quả đạt được:** Một chart Helm của riêng bạn, cài được nhiều môi trường từ cùng một khuôn, nâng cấp và quay lui an toàn — sẵn sàng để Ngày 43 giao cho Git tự động quản lý.

---

## Ngày 43 — GitOps: ArgoCD & Triển khai khai báo

> ⏱️ ~90 phút · Loại: Kubernetes / CD
>
> 🧭 **Bạn đang ở đâu:** Ngày 42 (Helm đóng gói) → **Ngày 43 (để Git tự lái cluster — GitOps)** → Ngày 44 (giám sát). Nhớ hai điều còn dang dở: Ngày 34 bạn phải **giao chìa khoá server cho CI**, và Ngày 36 bạn thấy `kubectl scale` bằng tay **âm thầm bị ghi đè**. Hôm nay giải quyết cả hai.
>
> ✅ **Chuẩn bị:** cluster đang chạy, `kubectl` và Git đã sẵn sàng. Cần một repo GitHub mới (để **Public** cho đơn giản — không phải cấu hình khoá truy cập).
>
> 🎁 **Cuối ngày bạn có gì:** cluster tự đồng bộ từ Git. Bạn sửa file trên GitHub → cluster tự đổi theo. Bạn sửa tay trên cluster → **nó tự khôi phục về đúng như Git**.

### 📘 Lý thuyết

#### 1. Hai vấn đề còn tồn đọng từ các ngày trước

**Vấn đề 1 — chìa khoá nằm sai chỗ (Ngày 34).** Pipeline muốn deploy thì phải giữ khoá SSH hoặc kubeconfig của production. Nghĩa là: ai chiếm được CI thì chiếm được cả cluster. Khoá càng nhiều nơi giữ thì càng khó kiểm soát.

**Vấn đề 2 — cluster trôi khỏi tài liệu (Ngày 36).** Nửa đêm sự cố, ai đó `kubectl scale` lên 10 pod để chữa cháy. Sáng hôm sau không ai nhớ. File YAML trong Git vẫn ghi 3. Lần deploy sau, con số âm thầm về 3 → sự cố tái diễn và **không ai hiểu vì sao**. Hiện tượng này gọi là **trôi cấu hình** (configuration drift).

#### 2. GitOps — lật ngược chiều kết nối

Ý tưởng chỉ gồm hai câu:

> **1. Git là nguồn sự thật duy nhất** về "cluster phải trông như thế nào".
> **2. Một tác nhân sống bên trong cluster tự kéo từ Git về và sửa cho khớp.**

```text
  MÔ HÌNH PUSH (Ngày 34)                MÔ HÌNH PULL (GitOps — hôm nay)

  CI  ──(giữ chìa khoá)──>  Cluster     Git  <──(tự đi kéo)──  ArgoCD
      đẩy vào                                                  (sống TRONG cluster)
                                                                     │
  ⚠️ CI có toàn quyền cluster            ✅ Không ai bên ngoài cần chìa khoá
```

Nghe đơn giản, nhưng hệ quả rất lớn:

| | Deploy kiểu push (Ngày 34) | GitOps |
|---|---|---|
| Ai giữ chìa khoá cluster | CI (bên ngoài) | **Không ai** — tác nhân ở trong cluster |
| Cluster có khớp tài liệu không | Hy vọng là có | **Được kiểm tra liên tục** |
| Sửa tay lúc nửa đêm | Không ai biết | **Bị phát hiện, và tự hoàn tác** |
| Quay lui | Chạy lại pipeline cũ | **`git revert`** |
| Ai đổi gì, lúc nào | Rải rác trong log CI | **Lịch sử Git** |

#### 3. Vòng điều hoà — lần thứ hai bạn gặp nó

Ngày 36 bạn học: K8s liên tục so **mong muốn** (trong etcd) với **thực tế** (pod đang chạy) rồi sửa.

ArgoCD làm **đúng y như vậy, nhưng ở một tầng cao hơn**: so **mong muốn** (trong Git) với **thực tế** (trong cluster) rồi sửa.

```text
  Tầng của K8s:     etcd  <──so sánh──>  pod đang chạy
  Tầng của ArgoCD:  Git   <──so sánh──>  toàn bộ cluster
```

Nhận ra cùng một khuôn tư duy lặp lại là bạn đã nắm được tinh thần của Kubernetes.

#### 4. Ba trạng thái của ArgoCD

| Trạng thái | Nghĩa |
|---|---|
| **Synced** | Cluster khớp Git ✅ |
| **OutOfSync** | Có khác biệt — do ai đó sửa tay, hoặc Git vừa đổi mà chưa kịp đồng bộ |
| **Healthy / Degraded** | Sức khoẻ thật của ứng dụng (pod có chạy được không) |

> 📌 **Hai trục khác nhau, đừng lẫn:** *Synced* nói **"có giống Git không"**; *Healthy* nói **"có chạy được không"**. Một app hoàn toàn có thể `Synced` mà `Degraded` — tức Git mô tả đúng ý bạn, nhưng thứ bạn mô tả lại đang hỏng.

#### 5. Hai chế độ đồng bộ

```yaml
syncPolicy:
  automated:
    prune: true        # Git xoá file -> xoá luôn tài nguyên trong cluster
    selfHeal: true     # ai sửa tay trên cluster -> tự kéo về đúng như Git
```

- **Thủ công** (mặc định): ArgoCD chỉ *báo* khác biệt, chờ người bấm Sync. Hợp với production lúc mới bắt đầu.
- **Tự động + selfHeal**: tự sửa mọi khác biệt. Đây là GitOps đúng nghĩa — nhưng cũng nghĩa là **bạn không thể vá tay lên cluster nữa**, mọi thứ buộc phải đi qua Git.

#### 6. Tách hai repo — chi tiết nhỏ nhưng quan trọng

| Repo | Chứa gì | Ai sửa |
|---|---|---|
| **Repo mã nguồn** (`ci-demo`) | Code, Dockerfile, test | Lập trình viên |
| **Repo cấu hình** (`ci-demo-config`) | YAML/Helm mô tả cluster | CI (cập nhật tag image) + người vận hành |

Vì sao tách? Vì mỗi lần deploy là một commit vào repo cấu hình. Gộp chung thì lịch sử code bị ngập trong commit "cập nhật tag image", và mỗi lần đổi cấu hình lại kích hoạt chạy lại toàn bộ CI một cách vô nghĩa.

### 🧪 LAB — Để Git lái cluster

**Repo cấu hình bạn sẽ tạo:**

```text
ci-demo-config/                 ← repo GitHub MỚI, để Public
└── ung-dung/
    ├── deployment.yaml
    └── service.yaml
```

**Và một file khai báo cho ArgoCD (giữ ở máy):**

```text
~/lab43-gitops/
└── application.yaml            # bảo ArgoCD: hãy theo dõi repo kia
```

#### File 1 — `ung-dung/deployment.yaml` (trong repo cấu hình)

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: web-gitops
  labels:
    app: web-gitops
spec:
  replicas: 2
  selector:
    matchLabels:
      app: web-gitops
  template:
    metadata:
      labels:
        app: web-gitops
    spec:
      containers:
        - name: web
          image: nginx:1.27
          ports:
            - containerPort: 80
          command: ["/bin/sh", "-c"]
          args:
            - echo "<h1>Phiên bản 1 - lái bởi Git</h1>" > /usr/share/nginx/html/index.html
              && nginx -g 'daemon off;'
          resources:
            requests:
              memory: "64Mi"
              cpu: "50m"
            limits:
              memory: "128Mi"
```

#### File 2 — `ung-dung/service.yaml` (trong repo cấu hình)

```yaml
apiVersion: v1
kind: Service
metadata:
  name: web-gitops-svc
spec:
  selector:
    app: web-gitops
  ports:
    - port: 80
      targetPort: 80
```

#### File 3 — `application.yaml` (giữ ở máy)

```yaml
apiVersion: argoproj.io/v1alpha1
kind: Application
metadata:
  name: web-gitops
  namespace: argocd
spec:
  project: default

  # NGUỒN SỰ THẬT: repo nào, nhánh nào, thư mục nào
  source:
    repoURL: https://github.com/<TEN-GITHUB-CUA-BAN>/ci-demo-config.git
    targetRevision: main
    path: ung-dung

  # ĐÍCH ĐẾN: cluster nào, namespace nào
  destination:
    server: https://kubernetes.default.svc
    namespace: default

  syncPolicy:
    automated:
      prune: true        # Git xoá file -> xoá tài nguyên tương ứng
      selfHeal: true     # sửa tay trên cluster -> tự kéo về đúng Git
    syncOptions:
      - CreateNamespace=true
```

### 🧭 Hướng dẫn làm LAB — step by step

#### Bước 1 — Cài ArgoCD vào cluster

```bash
minikube start
kubectl create namespace argocd
kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml
kubectl -n argocd rollout status deployment/argocd-server --timeout=300s
```

**Bạn sẽ thấy** (lần đầu mất 2–4 phút để tải image):
```text
deployment "argocd-server" successfully rolled out
```

```bash
kubectl get pods -n argocd
```

**Bạn sẽ thấy** khoảng 7 pod, tất cả `Running`:
```text
argocd-application-controller-0            1/1   Running
argocd-repo-server-6b9c7d8f4-xk2mp         1/1   Running
argocd-server-7d4f8b9c5-t7m3n              1/1   Running
...
```

✅ **Checkpoint:** mọi pod trong namespace `argocd` đều `Running`.

💡 Chú ý: ArgoCD **chạy bên trong cluster**. Đó chính là điều khiến nó không cần ai đưa chìa khoá từ bên ngoài — nó đã ở sẵn trong nhà.

#### Bước 2 — Vào giao diện ArgoCD

Lấy mật khẩu admin:

```bash
kubectl -n argocd get secret argocd-initial-admin-secret \
  -o jsonpath="{.data.password}" | base64 -d; echo
```

**Bạn sẽ thấy** một chuỗi ngẫu nhiên, ví dụ `k8Jx2mQpL9nRt4Wz`.

💡 Để ý: lại là `base64 -d` — đúng bài học Ngày 39. Secret của K8s chưa bao giờ là mã hoá thật.

Mở đường hầm tới giao diện:

```bash
kubectl port-forward svc/argocd-server -n argocd 8088:443 > /dev/null 2>&1 &
sleep 3
echo "Mở trình duyệt: https://localhost:8088  (user: admin)"
```

Trình duyệt sẽ cảnh báo chứng chỉ không tin cậy → chọn **Advanced → Proceed** (chứng chỉ tự ký, bình thường với lab).

✅ **Checkpoint:** đăng nhập được, thấy màn hình Applications trống.

#### Bước 3 — Tạo repo cấu hình trên GitHub

Tạo repo mới tên `ci-demo-config`, để **Public** (ArgoCD kéo được ngay, khỏi cấu hình khoá).

```bash
mkdir -p ~/ci-demo-config/ung-dung && cd ~/ci-demo-config
# tạo ung-dung/deployment.yaml và ung-dung/service.yaml theo phần LAB
git init -b main
git add .
git commit -m "Cấu hình ban đầu: 2 bản sao, phiên bản 1"
git remote add origin git@github.com:<TEN-GITHUB-CUA-BAN>/ci-demo-config.git
git push -u origin main
```

✅ **Checkpoint:** vào GitHub thấy thư mục `ung-dung/` với 2 file.

#### Bước 4 — Bảo ArgoCD theo dõi repo đó

```bash
mkdir -p ~/lab43-gitops && cd ~/lab43-gitops
# tạo application.yaml theo phần LAB — NHỚ thay <TEN-GITHUB-CUA-BAN>
kubectl apply -f application.yaml
sleep 20
kubectl get application -n argocd
```

**Bạn sẽ thấy:**
```text
NAME         SYNC STATUS   HEALTH STATUS
web-gitops   Synced        Healthy
```

```bash
kubectl get pods -l app=web-gitops
```

**Bạn sẽ thấy 2 pod đang chạy** — mà **bạn chưa hề `kubectl apply` cái deployment nào**.

✅ **Checkpoint:** `Synced` + `Healthy`, và 2 pod tự xuất hiện.

💡 **Dừng lại và nhận ra điều vừa xảy ra:** bạn chỉ nói với ArgoCD *"nguồn sự thật nằm ở repo này"*. Nó tự đọc Git, tự tạo mọi thứ. Từ giờ, muốn đổi gì trên cluster thì **sửa Git**, không gõ `kubectl` nữa.

Trên giao diện, bấm vào app `web-gitops` — bạn sẽ thấy sơ đồ cây: Application → Deployment → ReplicaSet → 2 Pod, kèm màu sức khoẻ từng thứ.

#### Bước 5 — Đổi Git, cluster tự đổi theo

```bash
cd ~/ci-demo-config
sed -i 's/replicas: 2/replicas: 4/' ung-dung/deployment.yaml
sed -i 's/Phiên bản 1/Phiên bản 2 - đã đổi qua Git/' ung-dung/deployment.yaml
git commit -am "Tăng lên 4 bản sao, cập nhật nội dung"
git push
```

Theo dõi (ArgoCD kiểm tra Git khoảng mỗi 3 phút; muốn nhanh thì bấm **Refresh** trên giao diện):

```bash
kubectl get pods -l app=web-gitops -w
```

**Bạn sẽ thấy** pod thứ 3 và 4 tự xuất hiện, rồi các pod lần lượt được thay bằng phiên bản mới.

Kiểm chứng nội dung:
```bash
kubectl port-forward svc/web-gitops-svc 8090:80 > /dev/null 2>&1 &
sleep 2
curl -s localhost:8090
kill %1
```

**Bạn sẽ thấy:**
```text
<h1>Phiên bản 2 - đã đổi qua Git</h1>
```

✅ **Checkpoint:** cluster đổi theo Git mà bạn **không chạy lệnh `kubectl` nào**.

💡 Không có pipeline nào đẩy vào cluster ở đây cả. ArgoCD **tự đi kéo**. Đó là toàn bộ khác biệt giữa push và pull.

#### Bước 6 — Sửa tay trên cluster và xem nó bị hoàn tác

Đây là bước trả lời câu hỏi còn treo từ Ngày 36.

```bash
kubectl scale deployment web-gitops --replicas=10
kubectl get pods -l app=web-gitops --no-headers | wc -l     # 10 ngay lập tức
```

Giờ chờ khoảng 10–30 giây rồi đếm lại:

```bash
sleep 30
kubectl get pods -l app=web-gitops --no-headers | wc -l
kubectl get application web-gitops -n argocd
```

**Bạn sẽ thấy:**
```text
4

NAME         SYNC STATUS   HEALTH STATUS
web-gitops   Synced        Healthy
```

✅ **Checkpoint:** số pod **tự quay về 4** — đúng như Git ghi.

💡 **Đây là `selfHeal: true` đang làm việc.** Hãy so với Ngày 36: lúc đó `kubectl scale` tồn tại cho đến lần `apply` tiếp theo — có thể là vài tuần sau, khi không ai còn nhớ. Bây giờ, mọi sửa tay đều bị hoàn tác trong vài chục giây.

💡 **Điều này thay đổi văn hoá làm việc:** "vá tay lên production" không còn là lựa chọn. Muốn đổi thì mở Pull Request — nghĩa là có review, có lịch sử, có người biết.

Trên giao diện ArgoCD, mở tab **EVENTS** của app — bạn sẽ thấy dòng ghi lại lần tự sửa này.

#### Bước 7 — Quay lui bằng `git revert`

Giả sử bản vừa lên có vấn đề:

```bash
cd ~/ci-demo-config
git revert --no-edit HEAD
git push
```

Bấm **Refresh** trên giao diện ArgoCD rồi kiểm tra:

```bash
sleep 20
kubectl get pods -l app=web-gitops --no-headers | wc -l
kubectl port-forward svc/web-gitops-svc 8090:80 > /dev/null 2>&1 &
sleep 2
curl -s localhost:8090
kill %1
```

**Bạn sẽ thấy:**
```text
2
<h1>Phiên bản 1 - lái bởi Git</h1>
```

✅ **Checkpoint:** quay lui hoàn toàn — cả số bản sao lẫn nội dung — chỉ bằng một lệnh Git.

💡 **So sánh ba cách rollback bạn đã học:**

| Cách | Lệnh | Dấu vết để lại |
|---|---|---|
| Ngày 34 (pipeline) | Chạy lại workflow với tag cũ | Log CI |
| Ngày 42 (Helm) | `helm rollback` | Lịch sử Helm |
| **Hôm nay (GitOps)** | `git revert` | **Một commit — cả đội nhìn thấy, review được** |

Cách thứ ba mạnh hơn ở chỗ: rollback cũng là một thay đổi *được ghi nhận*, không phải một thao tác âm thầm của người trực.

#### Bước 8 — Thấy `prune` dọn rác

```bash
cd ~/ci-demo-config
git rm ung-dung/service.yaml
git commit -m "Bỏ service"
git push
```

Refresh trên giao diện, chờ ~20 giây:

```bash
kubectl get svc web-gitops-svc
```

**Bạn sẽ thấy:**
```text
Error from server (NotFound): services "web-gitops-svc" not found
```

✅ **Checkpoint:** xoá file trong Git → tài nguyên trong cluster cũng biến mất.

💡 **`prune: true` là con dao hai lưỡi.** Nó giữ cluster sạch, không để lại tài nguyên mồ côi. Nhưng nghĩa là **xoá nhầm file trong Git = xoá thật trên cluster**. Ở production, nhiều đội bật `prune` nhưng kèm `PruneLast=true` và bảo vệ nhánh `main` bằng Pull Request bắt buộc (đúng như Ngày 32 bạn đã làm).

Khôi phục lại:
```bash
git revert --no-edit HEAD
git push
```

#### Bước 9 — Dọn dẹp

```bash
kubectl delete -f ~/lab43-gitops/application.yaml
kubectl delete namespace argocd
minikube stop
```

⚠️ Xoá `Application` sẽ xoá luôn những gì nó tạo ra (vì `prune: true`). Muốn giữ lại tài nguyên thì phải thêm annotation `argocd.argoproj.io/delete: "false"` hoặc xoá kèm `--cascade=orphan`.

### 💡 Đi làm mới thấm (sách cơ bản hay bỏ quên)

- **CI cập nhật repo cấu hình, không chạm vào cluster.** Mô hình hoàn chỉnh ở công ty: pipeline build image → **commit tag mới vào repo cấu hình** → ArgoCD thấy Git đổi → tự deploy. CI không bao giờ có kubeconfig của production. Đây chính là mảnh ghép nối Ngày 33 với hôm nay.
- **Chỉ bật `selfHeal` khi đội đã sẵn sàng.** Ở nơi mọi người quen vá tay, bật `selfHeal` sẽ gây bực bội: "tôi vừa sửa thì nó tự đổi lại". Cách làm thường thấy là bắt đầu bằng sync thủ công (ArgoCD chỉ báo khác biệt) vài tuần, đến khi cả đội quen với "mọi thay đổi qua Git" rồi mới bật tự động.
- **GitOps buộc bí mật phải xử lý tử tế.** Mọi thứ nằm trong Git, mà Secret thì chỉ là base64 (Ngày 39) → **không thể** commit thẳng. Đây là lý do **Sealed Secrets** / **SOPS** / **External Secrets Operator** gần như luôn đi kèm với GitOps.
- **App-of-Apps để quản lý quy mô lớn.** Một Application đặc biệt trỏ tới thư mục chứa các Application khác → cài cả một nền tảng bằng một lần khai báo. Đây là cách các đội quản lý hàng chục dịch vụ.
- **ArgoCD mặc định hỏi Git mỗi 3 phút.** Muốn phản hồi tức thì thì gắn **webhook** từ GitHub → cluster. Không có webhook thì đừng hoảng khi thấy chậm — đó là hành vi bình thường, không phải lỗi.
- **`Synced` không có nghĩa là đúng.** ArgoCD chỉ đảm bảo cluster *giống Git*. Nếu Git sai thì cluster sai một cách rất trung thành. Chất lượng của GitOps phụ thuộc hoàn toàn vào chất lượng review Pull Request — đây là lý do branch protection (Ngày 32) trở nên quan trọng gấp bội.

### 📝 Tự kiểm tra

> Nghĩ câu trả lời **thành lời** trước khi mở đáp án — nghĩ thầm luôn thấy mình hiểu.

<details>
<summary><b>1. GitOps giải quyết hai vấn đề nào còn tồn đọng từ Ngày 34 và Ngày 36?</b></summary>

**Vấn đề 1 — chìa khoá nằm sai chỗ (Ngày 34):** deploy kiểu push buộc CI giữ khoá SSH/kubeconfig của production. Ai chiếm được CI thì chiếm được cluster. GitOps lật ngược chiều: tác nhân **trong** cluster tự kéo từ Git, **không ai bên ngoài cần giữ chìa khoá**.

**Vấn đề 2 — trôi cấu hình (Ngày 36):** ai đó `kubectl scale` lúc nửa đêm, sáng ra không ai nhớ, và lần deploy sau nó âm thầm quay lại. GitOps với `selfHeal: true` **phát hiện và tự hoàn tác trong 30 giây**.

</details>

<details>
<summary><b>2. Phân biệt trạng thái `Synced` và `Healthy` của ArgoCD. Có thể vừa Synced vừa Degraded không?</b></summary>

Hai **trục hoàn toàn khác nhau**:
- **Synced** = cluster có **giống Git** không
- **Healthy** = ứng dụng có **chạy được** không

Hoàn toàn có thể `Synced` mà `Degraded`: nghĩa là Git mô tả **đúng ý bạn**, nhưng thứ bạn mô tả **đang hỏng** (ví dụ image tag không tồn tại).

Hệ quả quan trọng: ArgoCD chỉ đảm bảo cluster giống Git. **Git sai thì cluster sai một cách rất trung thành.** Chất lượng GitOps phụ thuộc hoàn toàn vào chất lượng review Pull Request — đó là lý do branch protection (Ngày 32) trở nên quan trọng gấp bội.

</details>

<details>
<summary><b>3. Vì sao GitOps bắt buộc phải xử lý bí mật tử tế?</b></summary>

Vì **mọi thứ đều nằm trong Git** — đó là cả điểm mạnh lẫn ràng buộc. Mà Secret của K8s chỉ là base64 (Ngày 39), nên **không thể commit thẳng**.

Ba giải pháp thường đi kèm GitOps:
- **Sealed Secrets**: mã hoá bằng khoá công khai của cluster, chỉ cluster giải được
- **SOPS**: mã hoá file bằng khoá từ KMS/age
- **External Secrets Operator**: Git chỉ chứa *tham chiếu*, giá trị thật nằm ở Vault/cloud

</details>

### 📚 Thuật ngữ Anh–Việt (ngày này)

| Thuật ngữ | Nghĩa |
|---|---|
| **GitOps** | Git là nguồn sự thật; tác nhân trong cluster tự kéo về và sửa cho khớp |
| **ArgoCD** | Công cụ GitOps phổ biến nhất cho Kubernetes |
| **Application (CRD)** | Object khai báo: theo dõi repo nào, nhánh nào, thư mục nào, deploy vào đâu |
| **Synced / OutOfSync** | Cluster có khớp Git không |
| **Healthy / Degraded** | Ứng dụng có chạy được không — **trục khác** với Synced |
| **`selfHeal`** | Tự hoàn tác mọi thay đổi thủ công trên cluster |
| **`prune`** | Xoá file trong Git thì xoá luôn tài nguyên trong cluster — con dao hai lưỡi |
| **Repo cấu hình** | Repo riêng chứa YAML/Helm values; tách khỏi repo mã nguồn |
| **App-of-Apps** | Một Application trỏ tới thư mục chứa các Application khác |

### 🎯 Đúc kết Ngày 43

**3 điều phải mang theo:**

1. **Git là nguồn sự thật, tác nhân trong cluster tự kéo về.** Không ai bên ngoài cần giữ chìa khoá cluster nữa — giải đúng nhược điểm của Ngày 34.
2. **Trôi cấu hình bị phát hiện và tự hoàn tác.** Vá tay lúc nửa đêm không còn tồn tại âm thầm được nữa.
3. **`git revert` là nút rollback tốt nhất** vì nó vừa khôi phục hệ thống, vừa để lại dấu vết cả đội nhìn thấy được.

> 🧠 **Một câu để nhớ:** GitOps không phải công cụ mới — nó là **chính vòng điều hoà của Kubernetes, nâng lên một tầng**: thay vì so etcd với pod, nó so **Git với cả cluster**.

**✅ Tự chấm** *(đánh dấu khi làm được mà không nhìn tài liệu):*

- [ ] Giải thích khác biệt push vs pull và vì sao pull an toàn hơn về chìa khoá
- [ ] Nói rõ "trôi cấu hình" là gì và vì sao nó nguy hiểm
- [ ] Cài ArgoCD và khai một Application trỏ tới repo Git
- [ ] Đổi Git và chứng minh cluster tự đổi theo, không gõ `kubectl`
- [ ] Sửa tay bằng `kubectl scale` và chứng minh `selfHeal` hoàn tác
- [ ] Rollback bằng `git revert` và nói vì sao cách này tốt hơn hai cách trước
- [ ] Phân biệt `Synced` với `Healthy`
- [ ] Nói được vì sao GitOps bắt buộc phải xử lý bí mật tử tế

✅ **Kết quả đạt được:** Một cluster tự lái bởi Git — mọi thay đổi đều có commit, có review, có đường lui, và không một ai bên ngoài phải giữ chìa khoá vào production.

---

## Ngày 44 — Monitoring: Prometheus & Metrics

> ⏱️ ~90 phút · Loại: Monitoring
>
> 🧭 **Bạn đang ở đâu:** Ngày 43 (GitOps) → **Ngày 44 (Prometheus — thu thập số đo hệ thống)** → Ngày 45 (Grafana vẽ dashboard từ chính stack bạn dựng hôm nay).
>
> ✅ **Chuẩn bị:** máy Linux có `docker` và `docker compose` (Ngày 16–20). Kiểm tra nhanh: `docker compose version`. Cần 3 cổng còn trống: **9090** (Prometheus), **9100** (node-exporter), **9093** (Alertmanager).
>
> 🎁 **Cuối ngày bạn có gì:** một thư mục `lab44-prometheus/` chạy được bằng 1 lệnh, giám sát chính máy bạn, có 3 cảnh báo thật — và bạn sẽ **tự gây sự cố để thấy cảnh báo bắn**.

### 📘 Lý thuyết

#### 1. Vấn đề có thật trước khi có Prometheus

Bạn có 1 server. Nó chậm. Bạn SSH vào gõ `top`, thấy CPU 90% → khởi động lại dịch vụ → hết chậm. Xong.

Giờ bạn có **30 server và 100 container**. Câu hỏi đổi hẳn:

- Lúc 2 giờ sáng CPU máy nào tăng? (bạn đang ngủ, `top` không ai gõ)
- Tuần trước hệ thống chậm — *chậm bao nhiêu*, so với bình thường thì tệ hơn mấy lần?
- Con số nào cho biết "sắp hỏng" **trước khi** khách hàng gọi điện?

`top` không trả lời được, vì nó chỉ cho biết **ngay lúc này, trên đúng máy này**. Thứ bạn cần là một hệ thống **đi đo liên tục, lưu lại theo thời gian, và tự la lên khi vượt ngưỡng**. Đó chính là Prometheus.

#### 2. Metric là gì — nhìn tận mắt cho dễ hiểu

Metric chỉ là **một con số, kèm nhãn, gắn với một mốc thời gian**. Một dịch vụ "có metric" nghĩa là nó mở một trang web `/metrics` trả về text như thế này:

```text
# HELP node_memory_MemAvailable_bytes RAM còn trống (byte)
# TYPE node_memory_MemAvailable_bytes gauge
node_memory_MemAvailable_bytes 3.221225472e+09

# HELP prometheus_http_requests_total Tổng số request HTTP đã nhận
# TYPE prometheus_http_requests_total counter
prometheus_http_requests_total{code="200",handler="/graph"} 14
prometheus_http_requests_total{code="200",handler="/metrics"} 253
```

Đọc dòng cuối: tên metric là `prometheus_http_requests_total`, **nhãn** (label) là `code="200"` và `handler="/metrics"`, giá trị là `253`. Mỗi tổ hợp nhãn khác nhau = **một chuỗi số riêng biệt** được lưu theo thời gian. Nhớ ý này — mục 💡 cuối bài sẽ cho biết vì sao nó làm sập cả hệ thống nếu đặt nhãn ẩu.

#### 3. Pull — Prometheus tự đi hỏi, không ngồi chờ

| | **Push** (dịch vụ tự gửi lên) | **Pull** (Prometheus tự đi lấy) ← Prometheus chọn cái này |
|---|---|---|
| Ai chủ động | Dịch vụ đẩy metric đi | Prometheus gọi `GET /metrics` mỗi 15 giây |
| Dịch vụ chết thì sao | Im lặng — không ai biết là chết hay chỉ *đang rảnh* | Gọi không được → biết ngay là **DOWN** |
| Debug | Phải xem log phía gửi | Mở thẳng `/metrics` bằng `curl` là thấy |

> 🧠 **Hình dung:** Prometheus như **y tá đi từng phòng đo nhịp tim** đúng giờ, thay vì ngồi chờ bệnh nhân tự gọi điện. Vì y tá tự đi, nên **phòng nào không mở cửa là biết ngay có chuyện** — đó chính là lợi thế lớn nhất của pull.

Việc "đi hỏi" gọi là **scrape**. Nơi bị hỏi gọi là **target**.

#### 4. Exporter — cầu nối cho thứ không biết nói metric

Linux không tự mở trang `/metrics`. Nên cần một chương trình nhỏ đứng cạnh, đọc thông tin hệ thống rồi bày ra dạng metric — gọi là **exporter**:

| Exporter | Bày ra metric về | Dùng ở lab hôm nay |
|---|---|---|
| **node-exporter** | CPU, RAM, disk, network của máy Linux | ✅ có |
| **cAdvisor** | Tài nguyên từng container | (Ngày 45) |
| **App tự expose** | Số request, độ trễ, số lỗi của chính ứng dụng | (dùng chính Prometheus làm ví dụ) |

#### 5. Bốn loại metric — chọn sai là đọc ra số vô nghĩa

| Loại | Đặc điểm | Ví dụ | Cách dùng |
|---|---|---|---|
| **Counter** | **Chỉ tăng**, về 0 khi restart | Tổng số request từ lúc khởi động | **Bắt buộc bọc `rate()`** |
| **Gauge** | Lên xuống tự do | RAM còn trống, số kết nối | Đọc thẳng |
| **Histogram** | Chia giá trị vào các "xô" (bucket) | Độ trễ request | `histogram_quantile()` tính p95/p99 |
| **Summary** | Giống histogram nhưng tính sẵn phía app | Ít dùng hơn | — |

**Vì sao counter phải bọc `rate()`:** biết "hệ thống đã phục vụ 3.000.000 request từ hôm khai trương" thì để làm gì? Cái bạn cần là **tốc độ hiện tại** — "đang 120 request/giây, trong khi bình thường là 40". `rate(x[5m])` chính là phép tính "trung bình mỗi giây tăng bao nhiêu, trong 5 phút qua".

#### 6. PromQL tối thiểu đủ dùng hôm nay

| Câu truy vấn | Đọc là |
|---|---|
| `up` | Mỗi target sống (`1`) hay chết (`0`) |
| `node_memory_MemAvailable_bytes` | RAM còn trống, đơn vị byte |
| `rate(prometheus_http_requests_total[1m])` | Số request mỗi giây, tính trên 1 phút qua |
| `sum by (code) (rate(prometheus_http_requests_total[5m]))` | Gộp lại, tách theo mã HTTP |
| `100 - avg(rate(node_cpu_seconds_total{mode="idle"}[5m])) * 100` | % CPU đang bận (lấy 100 trừ đi phần rảnh) |

#### 7. Alert — biến con số thành tiếng chuông

Bạn viết **alert rule** trong Prometheus: "nếu `up == 0` **kéo dài 1 phút** thì báo động". Chữ *kéo dài* (`for: 1m`) rất quan trọng — nó lọc bỏ những cú nhấp nháy 5 giây rồi tự khỏi. Prometheus phát hiện, rồi đẩy sang **Alertmanager** — bộ phận lo việc gom nhóm và gửi đi (Slack, email, điện thoại).

Vòng đời một alert: **Inactive** (bình thường) → **Pending** (đã vượt ngưỡng, đang đếm đủ `for:`) → **Firing** (báo động thật, gửi đi). Lát nữa bạn sẽ thấy tận mắt cả 3 trạng thái này.

### 🧪 LAB — Dựng hệ thống giám sát chạy thật

> **Mục tiêu:** 3 container chạy bằng 1 lệnh, giám sát chính máy bạn, có 3 cảnh báo. Toàn bộ file dưới đây **đầy đủ, copy là chạy** — không cắt khúc.

**Cây thư mục sẽ tạo:**

```text
lab44-prometheus/
├── docker-compose.yml     # khai báo 3 container
├── prometheus.yml         # Prometheus đi hỏi những ai, bao lâu một lần
├── alert.rules.yml        # 3 luật cảnh báo
└── alertmanager.yml       # nhận cảnh báo rồi làm gì
```

#### File 1 — `docker-compose.yml`

```yaml
services:
  prometheus:
    image: prom/prometheus:v3.0.1          # cố định phiên bản để lab luôn tái lập được
    container_name: prometheus
    restart: unless-stopped
    ports:
      - "9090:9090"
    volumes:
      - ./prometheus.yml:/etc/prometheus/prometheus.yml:ro    # :ro = chỉ đọc, container không sửa được
      - ./alert.rules.yml:/etc/prometheus/alert.rules.yml:ro
      - prom-data:/prometheus                                 # dữ liệu metric nằm trong volume, xoá container không mất
    command:
      - '--config.file=/etc/prometheus/prometheus.yml'
      - '--storage.tsdb.path=/prometheus'
      - '--storage.tsdb.retention.time=15d'   # giữ metric 15 ngày rồi tự xoá
      - '--web.enable-lifecycle'              # cho phép nạp lại config không cần restart

  node-exporter:
    image: prom/node-exporter:v1.8.2
    container_name: node-exporter
    restart: unless-stopped
    pid: host                     # nhìn được tiến trình của MÁY THẬT, không phải của container
    ports:
      - "9100:9100"
    volumes:
      - /:/host:ro,rslave         # gắn toàn bộ ổ đĩa máy thật vào /host, chỉ đọc
    command:
      - '--path.rootfs=/host'     # bảo node-exporter: gốc hệ thống thật nằm ở /host

  alertmanager:
    image: prom/alertmanager:v0.27.0
    container_name: alertmanager
    restart: unless-stopped
    ports:
      - "9093:9093"
    volumes:
      - ./alertmanager.yml:/etc/alertmanager/alertmanager.yml:ro

volumes:
  prom-data:
```

#### File 2 — `prometheus.yml`

```yaml
global:
  scrape_interval: 15s        # cứ 15 giây đi hỏi mỗi target một lần
  evaluation_interval: 15s    # cứ 15 giây kiểm tra lại các luật cảnh báo

rule_files:
  - /etc/prometheus/alert.rules.yml

alerting:
  alertmanagers:
    - static_configs:
        - targets: ['alertmanager:9093']    # gọi bằng TÊN SERVICE, Docker tự phân giải thành IP

scrape_configs:
  # Target 1: chính Prometheus tự giám sát mình
  - job_name: 'prometheus'
    static_configs:
      - targets: ['localhost:9090']

  # Target 2: máy Linux của bạn, qua node-exporter
  - job_name: 'node'
    static_configs:
      - targets: ['node-exporter:9100']
        labels:
          may: 'may-cua-toi'      # nhãn tự đặt, sau này lọc theo máy rất tiện
```

#### File 3 — `alert.rules.yml`

```yaml
groups:
  - name: canh-bao-he-thong
    rules:
      # 1) Một target chết quá 1 phút
      - alert: TargetChet
        expr: up == 0
        for: 1m
        labels:
          severity: critical
        annotations:
          tom_tat: "Target {{ $labels.job }} không phản hồi"
          chi_tiet: "{{ $labels.instance }} đã không scrape được hơn 1 phút."

      # 2) RAM còn trống dưới 15%
      - alert: RamSapCan
        expr: (node_memory_MemAvailable_bytes / node_memory_MemTotal_bytes) * 100 < 15
        for: 2m
        labels:
          severity: warning
        annotations:
          tom_tat: "RAM còn dưới 15%"
          chi_tiet: "Chỉ còn ít RAM trống trên {{ $labels.instance }}."

      # 3) CPU bận trên 80% liên tục 5 phút
      - alert: CpuCao
        expr: 100 - (avg by (instance) (rate(node_cpu_seconds_total{mode="idle"}[5m])) * 100) > 80
        for: 5m
        labels:
          severity: warning
        annotations:
          tom_tat: "CPU trên 80%"
          chi_tiet: "CPU {{ $labels.instance }} bận liên tục suốt 5 phút."
```

#### File 4 — `alertmanager.yml`

```yaml
route:
  receiver: 'mac-dinh'
  group_wait: 10s         # gom các alert nổ cùng lúc, chờ 10s rồi gửi 1 lần
  group_interval: 1m
  repeat_interval: 1h     # cùng 1 alert chưa khỏi thì 1 tiếng nhắc lại, không spam

receivers:
  - name: 'mac-dinh'      # lab này chưa gắn Slack/email — alert chỉ hiện trên UI cổng 9093
```

> 📌 **Vì sao chưa gắn Slack ngay:** để bạn tập trung hiểu *alert sinh ra như thế nào* trước. Gắn kênh gửi thật là việc của Ngày 45 — và chỉ là thêm vài dòng vào đúng file này.

### 🧭 Hướng dẫn làm LAB — step by step

> Làm **tuần tự**. Sau mỗi bước, đối chiếu khối *"Bạn sẽ thấy"* rồi mới đi tiếp. Gặp lỗi thì đọc dòng ⚠️ ngay dưới bước đó.

#### Bước 1 — Tạo thư mục và 4 file

```bash
mkdir -p ~/lab44-prometheus && cd ~/lab44-prometheus
```

Tạo lần lượt 4 file ở trên bằng trình soạn thảo (`nano docker-compose.yml`, dán nội dung, `Ctrl+O` → `Enter` → `Ctrl+X`). Rồi kiểm tra:

```bash
ls -1
```

**Bạn sẽ thấy:**
```text
alert.rules.yml
alertmanager.yml
docker-compose.yml
prometheus.yml
```

✅ **Checkpoint:** đủ 4 file, đúng tên (sai một ký tự là container không lên).

⚠️ **Rất hay sai:** YAML **cấm dùng Tab** để thụt dòng — chỉ được dùng dấu cách. Nếu dán từ nơi khác vào rồi lỗi, chạy `cat -A docker-compose.yml | head`; thấy `^I` nghĩa là có Tab, phải thay bằng dấu cách.

#### Bước 2 — Khởi động cả stack bằng 1 lệnh

```bash
docker compose up -d
```

**Bạn sẽ thấy:**
```text
[+] Running 4/4
 ✔ Network lab44-prometheus_default  Created
 ✔ Container node-exporter           Started
 ✔ Container alertmanager            Started
 ✔ Container prometheus              Started
```

✅ **Checkpoint:** 3 container `Started`, không có dòng `Error`.

⚠️ **Nếu báo `port is already allocated`:** cổng đang bị chiếm. Tìm thủ phạm bằng `sudo ss -tlnp | grep 9090`, rồi hoặc tắt nó, hoặc đổi cổng trong `docker-compose.yml` thành `"9091:9090"`.

💡 *`-d` = detached:* chạy nền, trả lại terminal cho bạn. Bỏ `-d` sẽ thấy log chạy thẳng ra màn hình — hữu ích khi debug.

#### Bước 3 — Xác nhận cả 3 container thực sự sống

```bash
docker compose ps
```

**Bạn sẽ thấy:**
```text
NAME            IMAGE                        STATUS         PORTS
alertmanager    prom/alertmanager:v0.27.0    Up 30 seconds  0.0.0.0:9093->9093/tcp
node-exporter   prom/node-exporter:v1.8.2    Up 30 seconds  0.0.0.0:9100->9100/tcp
prometheus      prom/prometheus:v3.0.1       Up 30 seconds  0.0.0.0:9090->9090/tcp
```

✅ **Checkpoint:** cả 3 đều `Up`.

⚠️ **Nếu một container `Restarting` liên tục** — gần như chắc chắn sai cú pháp file config. Xem lý do thật:
```bash
docker compose logs prometheus | tail -20
```
Dòng `error parsing YAML` sẽ chỉ đúng số dòng bị sai.

#### Bước 4 — Nhìn tận mắt metric thô (bước quan trọng nhất để "vỡ ra")

```bash
curl -s localhost:9100/metrics | grep -A2 "^# HELP node_memory_MemAvailable_bytes"
```

**Bạn sẽ thấy:**
```text
# HELP node_memory_MemAvailable_bytes Memory information field MemAvailable_bytes.
# TYPE node_memory_MemAvailable_bytes gauge
node_memory_MemAvailable_bytes 3.221225472e+09
```

✅ **Checkpoint:** thấy đúng 3 dòng: mô tả, kiểu metric, và con số.

💡 **Đây chính là toàn bộ "phép màu":** không có giao thức bí ẩn nào cả — chỉ là một trang text mà Prometheus đi `GET` mỗi 15 giây rồi lưu lại kèm thời điểm. Muốn biết node-exporter bày ra bao nhiêu metric: `curl -s localhost:9100/metrics | grep -c "^node_"`.

#### Bước 5 — Mở giao diện và kiểm tra target

Mở trình duyệt vào **http://localhost:9090** → menu **Status → Target health**.

**Bạn sẽ thấy:** 2 mục `prometheus (1/1 up)` và `node (1/1 up)`, cả hai nền xanh, cột *Last Scrape* nhỏ hơn 15 giây.

✅ **Checkpoint:** cả 2 target đều **UP**.

⚠️ **Nếu target `node` báo DOWN** kèm `connection refused`: bạn đang khai `localhost:9100` thay vì `node-exporter:9100` trong `prometheus.yml`. Bên trong container, `localhost` là **chính container đó**, không phải máy thật — các container phải gọi nhau bằng **tên service**. Sửa xong thì nạp lại config không cần restart:
```bash
curl -X POST localhost:9090/-/reload
```

#### Bước 6 — Truy vấn đầu tiên: ai còn sống?

Vào tab **Query**, gõ `up` rồi bấm **Execute**.

**Bạn sẽ thấy:**
```text
up{instance="localhost:9090", job="prometheus"}                     1
up{instance="node-exporter:9100", job="node", may="may-cua-toi"}    1
```

✅ **Checkpoint:** 2 dòng, đều bằng `1`. Để ý nhãn `may="may-cua-toi"` — đúng cái bạn tự đặt trong `prometheus.yml`.

💡 `up` là metric **Prometheus tự sinh**, không exporter nào cung cấp: `1` = lần scrape vừa rồi thành công, `0` = thất bại.

#### Bước 7 — Thấy tận mắt vì sao counter phải bọc `rate()`

Chạy truy vấn này, ghi lại con số:
```promql
prometheus_http_requests_total{handler="/api/v1/query"}
```
Bấm **Execute** thêm 3–4 lần nữa. Con số **chỉ tăng, không bao giờ giảm** — vì mỗi lần bấm chính là một request.

Giờ đổi sang:
```promql
rate(prometheus_http_requests_total{handler="/api/v1/query"}[1m])
```

**Bạn sẽ thấy:** một số nhỏ có phần thập phân, ví dụ `0.0666`.

✅ **Checkpoint:** hiểu được `0.0666` nghĩa là **~0,067 request mỗi giây** (khoảng 4 request trong 1 phút vừa rồi).

💡 **Chốt lại:** số thô = "tổng từ lúc khởi động" (gần như vô dụng khi trực hệ thống). `rate()` = "**đang** nhanh chậm thế nào" — đây mới là thứ đưa lên dashboard và đặt cảnh báo.

#### Bước 8 — Đọc gauge: RAM còn trống bao nhiêu

```promql
node_memory_MemAvailable_bytes / 1024 / 1024
```

**Bạn sẽ thấy:** ví dụ `3072.5` — tức còn khoảng 3 GB RAM trống.

Rồi đổi sang dạng phần trăm (chính là biểu thức dùng trong alert của bạn):
```promql
(node_memory_MemAvailable_bytes / node_memory_MemTotal_bytes) * 100
```

✅ **Checkpoint:** ra một số trong khoảng 0–100, khớp với `free -h` chạy ở terminal.

💡 Gauge **đọc thẳng được**, không cần `rate()`. Bọc `rate()` vào gauge sẽ ra số vô nghĩa — lỗi kinh điển của người mới.

#### Bước 9 — Xác nhận 3 luật cảnh báo đã được nạp

Vào menu **Alerts** trên giao diện Prometheus.

**Bạn sẽ thấy:** 3 luật `TargetChet`, `RamSapCan`, `CpuCao`, tất cả đang màu xanh **Inactive**.

✅ **Checkpoint:** đủ 3 luật, không luật nào báo lỗi cú pháp.

⚠️ **Nếu trang Alerts trống rỗng:** Prometheus chưa nạp được file rule. Kiểm tra bằng chính công cụ có sẵn trong container:
```bash
docker compose exec prometheus promtool check rules /etc/prometheus/alert.rules.yml
```
Kết quả đúng: `SUCCESS: 3 rules found`.

#### Bước 10 — Tự gây sự cố để thấy cảnh báo bắn thật

Đây là bước đáng giá nhất cả buổi. Giết node-exporter đi:

```bash
docker compose stop node-exporter
```

Bây giờ **quan sát theo mốc thời gian**, mở sẵn tab **Alerts**:

| Sau khoảng | Bạn sẽ thấy |
|---|---|
| ~15 giây | **Status → Target health**: target `node` chuyển đỏ **DOWN** |
| ~15 giây | Query `up` trả về `0` cho `node-exporter:9100` |
| ~30 giây | Trang **Alerts**: `TargetChet` chuyển vàng **PENDING** (đã vượt ngưỡng, đang đếm đủ `for: 1m`) |
| **sau 1 phút** | `TargetChet` chuyển đỏ **FIRING** |
| thêm ~10 giây | Mở **http://localhost:9093** — alert đã sang tới Alertmanager |

✅ **Checkpoint:** bạn nhìn thấy đủ chuỗi **Inactive → Pending → Firing** và alert xuất hiện ở cổng 9093.

💡 **Đây chính là lý do tồn tại của `for:`.** Không có nó, một cú nhấp nháy mạng 5 giây lúc 3 giờ sáng cũng đủ dựng bạn dậy. Có `for: 1m`, sự cố phải *thật sự kéo dài* mới đánh thức người trực.

Hồi sinh lại và xem alert tự tắt:
```bash
docker compose start node-exporter
```
Sau khoảng 30 giây, `TargetChet` tự quay về **Inactive** — không cần ai bấm nút "đã xử lý".

#### Bước 11 — Dọn dẹp (khi đã xong)

```bash
docker compose down        # tắt container, GIỮ lại dữ liệu metric
# docker compose down -v   # thêm -v để xoá luôn volume prom-data (mất sạch metric đã thu)
```

✅ **Checkpoint:** `docker compose ps` không còn container nào.

⚠️ Giữ nguyên thư mục `lab44-prometheus/` — **Ngày 45 sẽ cắm Grafana vào đúng stack này**.

### 💡 Đi làm mới thấm (sách cơ bản hay bỏ quên)

- **Cardinality explosion — thứ thật sự làm sập Prometheus.** Mỗi tổ hợp nhãn khác nhau = 1 chuỗi time-series riêng, nằm trong RAM. Đặt nhãn `user_id`, `request_id` hay `email` → mỗi người dùng đẻ ra một chuỗi mới → vài triệu chuỗi → Prometheus ngốn hết RAM rồi chết. **Quy tắc vàng:** nhãn chỉ dành cho giá trị **hữu hạn và ít** (mã HTTP, tên service, môi trường). Tuyệt đối không nhét ID vào nhãn.
- **Metric không được giữ mãi mãi.** Mặc định ~15 ngày trên đĩa local (chính là `--storage.tsdb.retention.time` trong file bạn vừa viết). Muốn giữ hàng năm hoặc gộp nhiều cụm → gắn thêm **Thanos** hoặc **Mimir**. Rất nhiều người mới đinh ninh metric còn mãi.
- **Recording rule cho truy vấn nặng.** Dashboard có query lồng nhiều `rate()` sẽ tính lại từ đầu mỗi lần ai đó mở trang. **Recording rule** tính sẵn theo chu kỳ và lưu thành metric mới → dashboard nhẹ hẳn.
- **Pushgateway chỉ dành cho job siêu ngắn.** Cronjob chạy 3 giây rồi tắt thì Prometheus không kịp scrape — *chỉ* trường hợp này mới dùng Pushgateway. Dùng cho service thường trực là sai kiến trúc.
- **Khung để nghĩ khi đặt alert:** **RED** (Rate / Errors / Duration — cho service) hoặc **USE** (Utilization / Saturation / Errors — cho tài nguyên). Có khung thì bạn đặt alert theo hệ thống, không theo cảm tính.
- **Cảnh báo về chính cảnh báo — "alert fatigue".** Báo nhiều quá hoá nhờn, đến lúc có sự cố thật thì không ai buồn nhìn nữa. Chỉ alert vào thứ **người dùng thực sự cảm nhận được** (chậm, lỗi, không vào được) — không alert mọi dao động CPU.

### 📝 Tự kiểm tra

> Nghĩ câu trả lời **thành lời** trước khi mở đáp án — nghĩ thầm luôn thấy mình hiểu.

<details>
<summary><b>1. Vì sao Prometheus chọn mô hình pull thay vì push? Lợi ích lớn nhất là gì?</b></summary>

Prometheus **chủ động đi hỏi** (`GET /metrics` mỗi 15 giây) thay vì chờ dịch vụ tự gửi.

Lợi ích lớn nhất: **target chết là biết ngay**. Gọi không được → `up == 0` → cảnh báo. Với push model, dịch vụ im lặng thì không phân biệt được *đã chết* hay *đang rảnh không có gì để gửi*.

Lợi ích phụ: dễ debug (mở thẳng `/metrics` bằng `curl` là thấy), và target không cần biết địa chỉ Prometheus.

</details>

<details>
<summary><b>2. Vì sao counter bắt buộc phải bọc `rate()`? Gauge có cần không?</b></summary>

Counter **chỉ tăng**, nên con số thô gần như vô nghĩa — biết *'đã phục vụ 3 triệu request từ hôm khai trương'* thì để làm gì?

Cái bạn cần là **tốc độ hiện tại**: *'đang 120 request/giây, trong khi bình thường là 40'*. `rate(x[5m])` chính là phép tính 'trung bình mỗi giây tăng bao nhiêu trong 5 phút qua'.

**Gauge thì đọc thẳng** (RAM còn trống, số kết nối) — bọc `rate()` vào gauge sẽ ra kết quả vô nghĩa. Đây là lỗi kinh điển của người mới.

</details>

<details>
<summary><b>3. Cardinality explosion là gì? Cho một ví dụ nhãn KHÔNG được đặt.</b></summary>

Mỗi **tổ hợp nhãn khác nhau** tạo ra một chuỗi time-series riêng nằm trong RAM. Đặt nhãn động thì số chuỗi bùng nổ → Prometheus ngốn hết RAM rồi chết.

Ví dụ nhãn **không được** đặt: `user_id`, `request_id`, `email`, hoặc đường dẫn thật (`/don-hang/12345`). Mỗi người dùng/request lại đẻ một chuỗi mới.

**Quy tắc:** nhãn chỉ dùng cho giá trị **hữu hạn và ít** — mã HTTP, tên service, môi trường. Với đường dẫn thì dùng *mẫu* (`/don-hang/:id`), không dùng giá trị thật.

</details>

### 📚 Thuật ngữ Anh–Việt (ngày này)

| Thuật ngữ | Nghĩa |
|---|---|
| **Metric** | Một con số + nhãn + mốc thời gian, expose ở trang `/metrics` |
| **Scrape / Target** | Việc Prometheus đi hỏi / nơi bị hỏi |
| **Pull vs Push** | Prometheus tự đi lấy (biết ngay khi target chết) vs dịch vụ tự gửi |
| **Exporter** | Chương trình nhỏ bày thông tin hệ thống ra dạng metric (node-exporter, cAdvisor) |
| **Counter** | Chỉ tăng — **bắt buộc bọc `rate()`** |
| **Gauge** | Lên xuống tự do — đọc thẳng, không bọc `rate()` |
| **Histogram** | Chia giá trị vào các 'xô' — dùng `histogram_quantile()` tính p95/p99 |
| **PromQL** | Ngôn ngữ truy vấn metric của Prometheus |
| **`up`** | Metric Prometheus tự sinh: 1 = scrape thành công, 0 = thất bại |
| **`for:`** | Điều kiện phải duy trì bao lâu mới báo động — lọc bỏ nhấp nháy ngắn |
| **Cardinality explosion** | Nhãn động làm số chuỗi bùng nổ và giết Prometheus |
| **Recording rule** | Tính sẵn truy vấn nặng theo chu kỳ, lưu thành metric mới |

### 🎯 Đúc kết Ngày 44

**3 điều phải mang theo:**

1. **Metric chỉ là một trang text** ở `/metrics` gồm tên + nhãn + số. Prometheus đi `GET` nó mỗi 15 giây rồi lưu theo thời gian — không có gì huyền bí.
2. **Pull nên target chết là biết ngay** (`up == 0`). Đây cũng là alert giá trị nhất mà gần như hệ thống nào cũng nên có.
3. **Counter bọc `rate()`, gauge đọc thẳng.** Và nhãn chỉ dùng cho giá trị hữu hạn — nhét ID vào nhãn là con đường ngắn nhất làm sập Prometheus.

> 🧠 **Một câu để nhớ:** con số thô trả lời *"từ trước tới nay bao nhiêu"*, `rate()` trả lời *"ngay lúc này đang thế nào"* — trực hệ thống thì chỉ câu thứ hai mới có ích.

**✅ Tự chấm** *(đánh dấu khi làm được mà không nhìn tài liệu):*

- [ ] Dựng lại được stack 3 container từ đầu bằng `docker compose up -d`
- [ ] Giải thích được pull vs push và vì sao `up == 0` phát hiện được dịch vụ chết
- [ ] Đọc được một dòng metric thô: đâu là tên, đâu là nhãn, đâu là giá trị
- [ ] Viết được `rate(...)` cho counter và nói rõ vì sao không dùng cho gauge
- [ ] Gây sự cố và kể lại đủ chuỗi **Inactive → Pending → Firing**, giải thích tác dụng của `for:`
- [ ] Nói được 1 nguyên nhân làm Prometheus "nổ" (cardinality) và cách tránh

✅ **Kết quả đạt được:** Một hệ thống giám sát chạy thật trên máy bạn — thu metric, truy vấn bằng PromQL, và cảnh báo đã được kiểm chứng bằng sự cố do chính bạn tạo ra.

---

## Ngày 45 — Monitoring: Grafana Dashboard

> ⏱️ ~90 phút · Loại: Monitoring
>
> 🧭 **Bạn đang ở đâu:** Ngày 44 (Prometheus thu số) → **Ngày 45 (Grafana biến số thành hình, và cảnh báo gửi tới nơi người thật đọc được)** → Ngày 46 (Loki gom log). Prometheus có dữ liệu nhưng giao diện của nó chỉ hợp để tra cứu; hôm nay mới là thứ bạn treo lên màn hình phòng làm việc.
>
> ✅ **Chuẩn bị:** thư mục `lab44-prometheus/` từ Ngày 44 (đừng xoá nó). Kiểm tra: `cd ~/lab44-prometheus && ls`.
>
> 🎁 **Cuối ngày bạn có gì:** dashboard **tự dựng lại được từ code** (không phải bấm chuột tạo tay), theo dõi đúng 4 tín hiệu vàng, cộng một cảnh báo gửi ra ngoài mà bạn tự kiểm chứng được.

### 📘 Lý thuyết

#### 1. Vì sao cần Grafana khi Prometheus đã có giao diện

Giao diện Prometheus hợp để **tra cứu một truy vấn**. Nó không hợp để **trực hệ thống**:

| | Giao diện Prometheus | Grafana |
|---|---|---|
| Xem nhiều biểu đồ cùng lúc | Không | Có — cả bảng điều khiển |
| Nhiều nguồn dữ liệu | Chỉ Prometheus | Prometheus + Loki + database + cloud |
| Chia sẻ cho người khác | Gửi link truy vấn | Dashboard có sẵn, ai mở cũng hiểu |
| Cảnh báo tới Slack/email | Qua Alertmanager | Có sẵn, cấu hình bằng giao diện |

> 🔑 Nguyên tắc thực tế: **Prometheus lo thu thập và lưu trữ, Grafana lo hiển thị**. Đừng cố bắt cái này làm việc của cái kia.

#### 2. Bốn tín hiệu vàng — biết nhìn gì thay vì nhìn tất cả

Một exporter bày ra hàng nghìn metric. Nhìn hết là không nhìn gì cả. Google đúc kết lại còn **4 tín hiệu vàng** — đủ để biết một dịch vụ có ổn không:

| Tín hiệu | Câu hỏi | Ví dụ truy vấn |
|---|---|---|
| **Traffic** (lưu lượng) | Có bao nhiêu khách? | `rate(http_requests_total[5m])` |
| **Errors** (lỗi) | Bao nhiêu phần trăm hỏng? | `rate(http_requests_total{code=~"5.."}[5m])` |
| **Latency** (độ trễ) | Khách phải chờ bao lâu? | `histogram_quantile(0.95, ...)` |
| **Saturation** (bão hoà) | Còn dư sức không? | CPU, RAM, hàng đợi |

Một biến thể gọn hơn cho dịch vụ là **RED** (Rate, Errors, Duration); cho tài nguyên thì dùng **USE** (Utilization, Saturation, Errors).

> ⚠️ **Vì sao phải dùng p95 chứ không phải trung bình:** 100 request, 95 cái nhanh 50ms, 5 cái chậm 10 giây → trung bình chỉ khoảng 550ms, nhìn "ổn". Nhưng có 5 khách hàng đang rất bực. **p95 = 95% số request nhanh hơn con số này** — nó cho thấy trải nghiệm của nhóm khách chịu thiệt nhất, thứ mà trung bình luôn che giấu.

#### 3. Dashboard phải sinh ra từ code, không phải từ chuột

Bấm chuột tạo dashboard rất nhanh và rất vui — cho tới khi:

- container Grafana bị xoá → **mất sạch**;
- không ai biết ai đã đổi gì, lúc nào;
- dựng môi trường mới → ngồi bấm lại từ đầu.

**Provisioning** là cách khai báo nguồn dữ liệu và dashboard bằng **file YAML/JSON**, để Grafana tự nạp lúc khởi động. Đây chính là tư duy Infrastructure as Code (Ngày 29) áp vào giám sát.

#### 4. Cảnh báo: Alertmanager hay Grafana?

Cả hai đều gửi được cảnh báo. Khác biệt thực tế:

| | Alertmanager (Ngày 44) | Grafana Alerting |
|---|---|---|
| Luật viết ở đâu | File YAML, hợp với GitOps | Giao diện (xuất được ra file) |
| Nguồn dữ liệu | Chỉ Prometheus | Nhiều nguồn cùng lúc |
| Hợp với | Đội đã quen mọi thứ trong Git | Đội muốn làm nhanh trên giao diện |

Không có lựa chọn nào sai. Hôm nay dùng Grafana Alerting để bạn thấy được cả hai trường phái.

### 🧪 LAB — Dashboard dựng từ code, trên chính stack Ngày 44

**Những gì thêm vào thư mục cũ:**

```text
lab44-prometheus/
├── docker-compose.yml             # SỬA — thêm grafana + cadvisor
├── prometheus.yml                 # SỬA — scrape thêm cadvisor
├── alert.rules.yml                # giữ nguyên
├── alertmanager.yml               # giữ nguyên
└── grafana/
    └── provisioning/
        ├── datasources/
        │   └── prometheus.yml     # THÊM — tự nối tới Prometheus
        └── dashboards/
            ├── dashboard.yml      # THÊM — bảo Grafana tìm dashboard ở đâu
            └── he-thong.json      # THÊM — dashboard viết bằng code
```

#### File 1 — `docker-compose.yml` (thay phần cuối, thêm 2 service)

Giữ nguyên 3 service cũ, **thêm** vào trước mục `volumes:`:

```yaml
  grafana:
    image: grafana/grafana:11.4.0
    container_name: grafana
    restart: unless-stopped
    ports:
      - "3000:3000"
    environment:
      GF_SECURITY_ADMIN_USER: admin
      GF_SECURITY_ADMIN_PASSWORD: admin123        # lab thôi; thật thì dùng secret
      GF_USERS_ALLOW_SIGN_UP: "false"
    volumes:
      - ./grafana/provisioning:/etc/grafana/provisioning:ro   # nạp cấu hình từ code
      - grafana-data:/var/lib/grafana

  cadvisor:
    image: gcr.io/cadvisor/cadvisor:v0.49.1
    container_name: cadvisor
    restart: unless-stopped
    ports:
      - "8081:8080"
    volumes:
      - /:/rootfs:ro
      - /var/run:/var/run:ro
      - /sys:/sys:ro
      - /var/lib/docker/:/var/lib/docker:ro
      - /dev/disk/:/dev/disk:ro
    privileged: true
    devices:
      - /dev/kmsg
```

Và sửa mục `volumes:` cuối file thành:

```yaml
volumes:
  prom-data:
  grafana-data:
```

#### File 2 — `prometheus.yml` (thêm một target)

Thêm vào cuối phần `scrape_configs:`:

```yaml
  # Target 3: metric của từng container
  - job_name: 'cadvisor'
    static_configs:
      - targets: ['cadvisor:8080']
```

#### File 3 — `grafana/provisioning/datasources/prometheus.yml`

```yaml
apiVersion: 1

datasources:
  - name: Prometheus
    type: prometheus
    access: proxy
    url: http://prometheus:9090      # gọi bằng TÊN SERVICE trong mạng Docker
    isDefault: true
    editable: false                  # không cho sửa tay -> buộc mọi thay đổi qua file
```

#### File 4 — `grafana/provisioning/dashboards/dashboard.yml`

```yaml
apiVersion: 1

providers:
  - name: 'dashboard-tu-code'
    orgId: 1
    folder: 'Hệ thống'
    type: file
    disableDeletion: false
    updateIntervalSeconds: 30        # quét lại thư mục mỗi 30 giây
    allowUiUpdates: false
    options:
      path: /etc/grafana/provisioning/dashboards
```

#### File 5 — `grafana/provisioning/dashboards/he-thong.json`

```json
{
  "title": "Sức khoẻ hệ thống",
  "uid": "suc-khoe-he-thong",
  "timezone": "browser",
  "refresh": "10s",
  "time": { "from": "now-30m", "to": "now" },
  "panels": [
    {
      "type": "stat",
      "title": "Số target đang sống",
      "gridPos": { "h": 4, "w": 6, "x": 0, "y": 0 },
      "targets": [{ "expr": "sum(up)", "refId": "A" }],
      "fieldConfig": {
        "defaults": {
          "thresholds": {
            "mode": "absolute",
            "steps": [
              { "color": "red", "value": null },
              { "color": "green", "value": 3 }
            ]
          }
        }
      }
    },
    {
      "type": "gauge",
      "title": "CPU đang bận (%)",
      "gridPos": { "h": 8, "w": 6, "x": 6, "y": 0 },
      "targets": [
        {
          "expr": "100 - (avg(rate(node_cpu_seconds_total{mode=\"idle\"}[5m])) * 100)",
          "refId": "A"
        }
      ],
      "fieldConfig": {
        "defaults": {
          "unit": "percent",
          "min": 0,
          "max": 100,
          "thresholds": {
            "mode": "absolute",
            "steps": [
              { "color": "green", "value": null },
              { "color": "yellow", "value": 70 },
              { "color": "red", "value": 85 }
            ]
          }
        }
      }
    },
    {
      "type": "timeseries",
      "title": "RAM còn trống (%)",
      "gridPos": { "h": 8, "w": 12, "x": 12, "y": 0 },
      "targets": [
        {
          "expr": "(node_memory_MemAvailable_bytes / node_memory_MemTotal_bytes) * 100",
          "legendFormat": "RAM trống",
          "refId": "A"
        }
      ],
      "fieldConfig": { "defaults": { "unit": "percent", "min": 0, "max": 100 } }
    },
    {
      "type": "timeseries",
      "title": "Lưu lượng request vào Prometheus (req/giây)",
      "gridPos": { "h": 8, "w": 12, "x": 0, "y": 8 },
      "targets": [
        {
          "expr": "sum by (handler) (rate(prometheus_http_requests_total[1m]))",
          "legendFormat": "{{handler}}",
          "refId": "A"
        }
      ],
      "fieldConfig": { "defaults": { "unit": "reqps" } }
    },
    {
      "type": "timeseries",
      "title": "RAM từng container (MB)",
      "gridPos": { "h": 8, "w": 12, "x": 12, "y": 8 },
      "targets": [
        {
          "expr": "sum by (name) (container_memory_usage_bytes{name!=\"\"}) / 1024 / 1024",
          "legendFormat": "{{name}}",
          "refId": "A"
        }
      ],
      "fieldConfig": { "defaults": { "unit": "decmbytes" } }
    }
  ]
}
```

### 🧭 Hướng dẫn làm LAB — step by step

#### Bước 1 — Tạo cây thư mục provisioning

```bash
cd ~/lab44-prometheus
mkdir -p grafana/provisioning/datasources grafana/provisioning/dashboards
# tạo 3 file trong grafana/ theo phần LAB
find grafana -type f | sort
```

**Bạn sẽ thấy:**
```text
grafana/provisioning/dashboards/dashboard.yml
grafana/provisioning/dashboards/he-thong.json
grafana/provisioning/datasources/prometheus.yml
```

✅ **Checkpoint:** đủ 3 file, đúng thư mục.

#### Bước 2 — Sửa compose và prometheus.yml, rồi khởi động

```bash
# sửa docker-compose.yml (thêm grafana + cadvisor, thêm volume grafana-data)
# sửa prometheus.yml (thêm job cadvisor)
docker compose up -d
docker compose ps
```

**Bạn sẽ thấy 5 container:**
```text
NAME            STATUS          PORTS
alertmanager    Up 10 seconds   0.0.0.0:9093->9093/tcp
cadvisor        Up 10 seconds   0.0.0.0:8081->8080/tcp
grafana         Up 10 seconds   0.0.0.0:3000->3000/tcp
node-exporter   Up 2 hours      0.0.0.0:9100->9100/tcp
prometheus      Up 10 seconds   0.0.0.0:9090->9090/tcp
```

✅ **Checkpoint:** đủ 5 container `Up`.

⚠️ **Nếu `cadvisor` liên tục restart:** một số bản Linux cần thêm quyền. Xem log: `docker compose logs cadvisor | tail -20`. Không chạy được cũng không sao — 4 panel còn lại vẫn hoạt động, chỉ mất panel RAM container.

Kiểm tra Prometheus đã thấy target mới:
```bash
curl -s localhost:9090/api/v1/targets | grep -o '"job":"[^"]*"' | sort -u
```

**Bạn sẽ thấy:**
```text
"job":"cadvisor"
"job":"node"
"job":"prometheus"
```

#### Bước 3 — Vào Grafana và kiểm tra provisioning đã ăn

Mở **http://localhost:3000** → đăng nhập `admin` / `admin123`.

Vào **Connections → Data sources**.

**Bạn sẽ thấy:** `Prometheus` đã có sẵn, kèm nhãn *Provisioned* và **không sửa được** (vì `editable: false`).

✅ **Checkpoint:** nguồn dữ liệu tự xuất hiện mà bạn **không bấm tạo**.

💡 Đây là điểm mấu chốt của provisioning: xoá container Grafana rồi dựng lại, mọi thứ vẫn y nguyên — vì nó đến từ **file**, không phải từ thao tác chuột.

⚠️ **Nếu không thấy data source:** sai đường dẫn mount. Kiểm tra:
```bash
docker compose exec grafana ls -R /etc/grafana/provisioning
docker compose logs grafana | grep -i "provisioning\|error" | tail -10
```

#### Bước 4 — Mở dashboard

Vào **Dashboards** → thư mục **Hệ thống** → **Sức khoẻ hệ thống**.

**Bạn sẽ thấy** 5 panel có dữ liệu thật:
- *Số target đang sống* — số **3**, nền xanh
- *CPU đang bận* — kim đồng hồ ở vùng xanh
- *RAM còn trống* — đường biểu diễn theo thời gian
- *Lưu lượng request* — nhiều đường tách theo `handler`
- *RAM từng container* — một đường cho mỗi container

✅ **Checkpoint:** panel có dữ liệu, không panel nào báo *No data*.

⚠️ **Nếu panel báo "No data":** mở panel → **Edit** → xem truy vấn, bấm **Run query**. Thường do sai tên metric — đối chiếu bằng cách gõ tên metric ở giao diện Prometheus (có gợi ý tự động).

💡 Để ý panel *Số target đang sống* đổi sang **đỏ** nếu số nhỏ hơn 3 — đó là `thresholds` trong file JSON. Màu sắc có ý nghĩa, không phải trang trí: người trực liếc 2 giây là biết có chuyện.

#### Bước 5 — Kiểm chứng "dashboard là code"

Sửa file JSON trực tiếp:

```bash
sed -i 's/"title": "Sức khoẻ hệ thống"/"title": "Sức khoẻ hệ thống - bản 2"/' \
  grafana/provisioning/dashboards/he-thong.json
sleep 35        # provider quét lại mỗi 30 giây
```

Tải lại trang Grafana.

**Bạn sẽ thấy:** tên dashboard đã đổi thành *Sức khoẻ hệ thống - bản 2*.

✅ **Checkpoint:** sửa file → giao diện đổi theo, **không bấm chuột**.

💡 **Đây là lý do nên làm theo cách này:** file JSON nằm trong Git → mọi thay đổi có review, có lịch sử, có đường lui. Dashboard bấm tay thì không có gì trong số đó. Nếu bạn nhận ra điều này giống hệt tinh thần Ngày 43 (GitOps) thì đúng — cùng một tư duy, áp vào giám sát.

#### Bước 6 — Tạo tải để đồ thị có chuyện để kể

Dashboard phẳng lì thì không dạy bạn được gì. Hãy làm nó nhúc nhích:

```bash
# Đổ request vào Prometheus trong 60 giây
timeout 60 bash -c 'while true; do curl -s "localhost:9090/api/v1/query?query=up" > /dev/null; done' &

# Đồng thời làm CPU bận
timeout 60 bash -c 'while true; do :; done' &
timeout 60 bash -c 'while true; do :; done' &
wait
```

Nhìn dashboard trong lúc chạy.

**Bạn sẽ thấy:** panel *Lưu lượng request* vọt lên vài trăm req/giây, kim CPU nhích sang vàng/đỏ, rồi cả hai hạ xuống sau khi lệnh kết thúc.

✅ **Checkpoint:** đồ thị phản ứng theo thời gian thực với việc bạn vừa làm.

💡 Bây giờ bạn đã thấy được *hình dạng* của tải. Đây chính là thứ giúp trả lời câu hỏi lúc sự cố: *"bình thường nó trông thế nào?"* — không có đường nền để so, mọi con số đều vô nghĩa.

#### Bước 7 — Tạo cảnh báo trong Grafana và tự kiểm chứng

Vào **Alerting → Alert rules → New alert rule**:

1. **Name:** `RAM trống dưới 90%` *(đặt ngưỡng dễ kích hoạt để thấy nó chạy ngay)*
2. **Query A:** chọn Prometheus, dán:
   ```promql
   (node_memory_MemAvailable_bytes / node_memory_MemTotal_bytes) * 100
   ```
3. **Expression:** Threshold → `IS BELOW` → `90`
4. **Evaluation:** tạo folder `Cảnh báo`, evaluation group mới, **Pending period: 1m**
5. **Save rule and exit**

Chờ 1–2 phút rồi vào **Alerting → Alert rules**.

**Bạn sẽ thấy** trạng thái chuyển: `Normal` → `Pending` → **`Firing`** (màu đỏ).

✅ **Checkpoint:** thấy đủ chuỗi chuyển trạng thái.

💡 Giống hệt vòng đời `Inactive → Pending → Firing` của Prometheus ở Ngày 44 — chỉ là giao diện khác. **Pending period** chính là `for:`. Cùng một khái niệm, hai cách gọi.

Muốn gửi ra ngoài thật: **Alerting → Contact points → Add contact point** → chọn *Webhook* (hoặc Slack nếu bạn có). Thử nhanh không cần Slack bằng cách dựng một điểm nhận tạm:

```bash
docker run -d --name bat-webhook --network lab44-prometheus_default -p 8888:8080 \
  mendhak/http-https-echo:34
```
Điền URL contact point: `http://bat-webhook:8080` → **Test**.

```bash
docker logs bat-webhook | tail -20
```

**Bạn sẽ thấy** nội dung JSON của cảnh báo vừa gửi tới.

✅ **Checkpoint:** cảnh báo thật sự đi ra khỏi Grafana.

```bash
docker rm -f bat-webhook
```

#### Bước 8 — Dọn dẹp

```bash
cd ~/lab44-prometheus
docker compose stop        # giữ nguyên để Ngày 46 cắm Loki vào
```

⚠️ Đừng `down -v` — Ngày 46 dùng lại chính stack này.

### 💡 Đi làm mới thấm (sách cơ bản hay bỏ quên)

- **Dashboard đẹp không đồng nghĩa với dashboard hữu ích.** Dashboard 40 panel thì lúc sự cố không ai kịp nhìn. Cách làm tốt: **một dashboard tổng quan đúng 4 tín hiệu vàng** để biết *có chuyện gì không*, rồi mới có các dashboard chi tiết để đào sâu. Trực hệ thống lúc 3 giờ sáng cần câu trả lời trong 5 giây.
- **Đừng tự vẽ lại từ đầu.** [grafana.com/dashboards](https://grafana.com/grafana/dashboards/) có sẵn hàng nghìn dashboard chất lượng. Node Exporter Full là **ID 1860** — nhập ID đó vào *Import* là có ngay bảng đầy đủ cho máy Linux. Lấy về rồi chỉnh, đừng vẽ tay từ số 0.
- **Luôn xuất dashboard ra JSON và commit vào Git.** Bấm chuột tạo cũng được — nhưng xong phải **Share → Export → Save to file** rồi đưa vào repo. Grafana chết là mọi thứ bấm tay biến mất.
- **Cẩn thận `$__rate_interval`.** Grafana có biến này thay cho `[5m]` cố định; nó tự tính theo khoảng thời gian đang xem. Dùng `[5m]` cứng rồi phóng to ra 7 ngày sẽ ra đồ thị sai lệch.
- **Một alert tốt phải kèm hướng dẫn xử lý.** Cảnh báo chỉ nói "CPU cao" thì người bị gọi dậy lúc nửa đêm vẫn không biết làm gì. Đưa vào phần annotation một **runbook**: kiểm tra gì trước, lệnh nào chạy, khi nào thì leo thang. Đây là dấu hiệu rõ nhất phân biệt đội vận hành nghiệp dư với chuyên nghiệp.
- **Alert nên gắn với thứ người dùng cảm nhận được.** "CPU 85%" chưa chắc là vấn đề nếu người dùng vẫn được phục vụ nhanh. "p95 độ trễ vượt 2 giây" hoặc "tỉ lệ lỗi 5xx trên 1%" mới đúng là thứ đáng đánh thức người ta dậy. Ngày 51 (SLO) sẽ hệ thống hoá đúng ý này.

### 📝 Tự kiểm tra

> Nghĩ câu trả lời **thành lời** trước khi mở đáp án — nghĩ thầm luôn thấy mình hiểu.

<details>
<summary><b>1. Bốn tín hiệu vàng là gì? Vì sao cần chúng khi đã có hàng nghìn metric?</b></summary>

**Traffic** (có bao nhiêu khách), **Errors** (bao nhiêu % hỏng), **Latency** (khách chờ bao lâu), **Saturation** (còn dư sức không).

Một exporter bày ra hàng nghìn metric — nhìn hết là không nhìn gì cả. Bốn tín hiệu này là **bộ lọc** giúp biết nhìn gì để trả lời câu *'hệ thống có ổn không?'* trong 5 giây.

Biến thể gọn hơn: **RED** (Rate/Errors/Duration) cho dịch vụ, **USE** (Utilization/Saturation/Errors) cho tài nguyên.

</details>

<details>
<summary><b>2. Vì sao nhìn p95 thay vì giá trị trung bình?</b></summary>

Trung bình **che giấu** trải nghiệm tệ. Ví dụ: 100 request, 95 cái nhanh 50ms, 5 cái chậm 10 giây → trung bình ≈ 550ms, nhìn vào thấy 'ổn'. Nhưng có **5 khách hàng đang rất bực**.

**p95 = 95% số request nhanh hơn con số này** — nó cho thấy trải nghiệm của nhóm chịu thiệt nhất, đúng nhóm sẽ bỏ đi hoặc gọi phàn nàn.

Ở quy mô lớn người ta còn nhìn p99 và p99.9 — 1% của một triệu request vẫn là mười nghìn người.

</details>

<details>
<summary><b>3. Vì sao dashboard phải sinh ra từ file thay vì bấm chuột tạo?</b></summary>

Ba lý do thực tế:
1. Container Grafana bị xoá → **mất sạch** dashboard bấm tay
2. Không ai biết **ai đã đổi gì, lúc nào** — không có lịch sử, không review được
3. Dựng môi trường mới → ngồi bấm lại từ đầu

**Provisioning** bằng file YAML/JSON đưa dashboard vào Git: có review, có đường lui, tái lập được ở bất cứ đâu. Đây chính là tư duy Infrastructure as Code áp cho giám sát — cùng tinh thần với GitOps ở Ngày 43.

</details>

### 📚 Thuật ngữ Anh–Việt (ngày này)

| Thuật ngữ | Nghĩa |
|---|---|
| **4 tín hiệu vàng** | Traffic · Errors · Latency · Saturation — bộ lọc để biết nhìn gì |
| **RED / USE** | Rate-Errors-Duration (dịch vụ) / Utilization-Saturation-Errors (tài nguyên) |
| **p95 / p99** | Phân vị — 95%/99% số request nhanh hơn con số này |
| **Provisioning** | Khai báo datasource và dashboard bằng file để Grafana tự nạp |
| **`$__rate_interval`** | Biến Grafana tự tính khoảng thời gian, thay cho `[5m]` cố định |
| **Threshold** | Ngưỡng màu trên panel — để liếc 2 giây là biết có chuyện |
| **Runbook** | Hướng dẫn xử lý kèm theo cảnh báo — dấu hiệu của đội chuyên nghiệp |
| **Alert fatigue** | Báo nhiều quá hoá nhờn, đến lúc có sự cố thật thì không ai nhìn |

### 🎯 Đúc kết Ngày 45

**3 điều phải mang theo:**

1. **Bốn tín hiệu vàng** (lưu lượng, lỗi, độ trễ, bão hoà) là bộ lọc giúp bạn biết nhìn gì giữa hàng nghìn metric.
2. **Dashboard phải là code.** Provisioning bằng file → có Git, có review, có đường lui, dựng lại được ở bất cứ đâu.
3. **p95 nói sự thật, trung bình che giấu nó.** Luôn nhìn phân vị khi đánh giá trải nghiệm người dùng.

> 🧠 **Một câu để nhớ:** dashboard không phải để *đẹp*, mà để **trả lời trong 5 giây câu hỏi "có chuyện gì không?"** lúc bạn vừa bị đánh thức.

**✅ Tự chấm** *(đánh dấu khi làm được mà không nhìn tài liệu):*

- [ ] Kể đủ 4 tín hiệu vàng và viết được truy vấn cho từng cái
- [ ] Giải thích vì sao dùng p95 thay vì trung bình
- [ ] Provisioning nguồn dữ liệu + dashboard bằng file, không bấm chuột
- [ ] Sửa file JSON và thấy dashboard tự cập nhật
- [ ] Tạo tải và đọc được phản ứng trên đồ thị
- [ ] Tạo alert rule trong Grafana và giải thích Pending period tương ứng với gì
- [ ] Nói được vì sao alert phải kèm runbook

✅ **Kết quả đạt được:** Một dashboard tái lập được từ code, hiển thị đúng những tín hiệu cần nhìn, kèm cảnh báo đã kiểm chứng gửi được ra ngoài.

---

## Ngày 46 — Logging tập trung: Loki

> ⏱️ ~90 phút · Loại: Monitoring
>
> 🧭 **Bạn đang ở đâu:** Ngày 45 (Grafana hiển thị metric) → **Ngày 46 (gom log mọi nơi về một chỗ tra cứu được)** → Ngày 47 (Ansible). Metric cho biết *"có chuyện gì đó sai"*; log cho biết *"sai cái gì"*. Hôm nay bạn lắp trụ cột thứ hai của observability.
>
> ✅ **Chuẩn bị:** stack từ Ngày 44–45 (`cd ~/lab44-prometheus && docker compose start`).
>
> 🎁 **Cuối ngày bạn có gì:** log của **mọi container** chảy về một chỗ, tra cứu bằng câu lệnh thay vì `docker logs` từng cái — và bạn sẽ đi hết một quy trình điều tra sự cố thật: *thấy metric bất thường → nhảy sang log → tìm ra nguyên nhân*.

### 📘 Lý thuyết

#### 1. Vấn đề: `docker logs` không mở rộng được

Một container thì `docker logs -f` là đủ. Nhưng thực tế:

- **20 container trên 5 máy** → SSH vào từng máy, gõ từng lệnh?
- **Container đã chết** → log biến mất cùng nó, đúng lúc bạn cần nhất.
- **Một request lỗi đi qua 4 dịch vụ** → phải mở 4 cửa sổ terminal, tự căn giờ khớp nhau.
- *"Tuần trước có lỗi này không?"* → không có cách nào trả lời.

Cần một chỗ **gom hết log lại, giữ lâu, và tìm kiếm được**.

#### 2. Loki — "Prometheus cho log"

| | **ELK / Elasticsearch** | **Loki** |
|---|---|---|
| Đánh chỉ mục | **Toàn bộ nội dung** log | **Chỉ nhãn** (container, job, mức độ) |
| Tốn tài nguyên | Nhiều (RAM, đĩa) | Ít hơn hẳn |
| Tìm kiếm toàn văn | Rất mạnh | Quét nội dung sau khi lọc nhãn |
| Hợp với | Phân tích log phức tạp | **Vận hành hằng ngày**, đi cặp với Prometheus |

Ý tưởng cốt lõi của Loki: **đừng đánh chỉ mục nội dung log — đắt và phần lớn không dùng đến**. Chỉ đánh chỉ mục vài cái nhãn, phần nội dung nén lại để đó. Khi tìm, lọc theo nhãn trước cho tập nhỏ lại, rồi mới quét nội dung.

Nhờ cách này, Loki dùng **đúng mô hình nhãn như Prometheus** — nên metric và log ghép được với nhau rất tự nhiên trong Grafana.

#### 3. Ba mảnh ghép

```text
  Container  ──> Promtail ──> Loki ──> Grafana
   (sinh log)   (đi gom)    (lưu+tìm)  (hiển thị)
```

| Thành phần | Việc |
|---|---|
| **Promtail** | Chạy trên máy, đọc log container, **gắn nhãn**, đẩy về Loki |
| **Loki** | Nhận, nén, lưu, phục vụ truy vấn |
| **Grafana** | Nơi bạn gõ truy vấn và đọc kết quả (cùng chỗ với metric) |

> 📌 **Ghi chú về phiên bản:** Grafana đang chuyển dần từ Promtail sang **Grafana Alloy** (bộ thu thập hợp nhất cho cả metric lẫn log). Promtail vẫn dùng rộng rãi và dễ hiểu hơn cho người mới, nên lab này dùng Promtail. Khái niệm giống hệt nhau — biết cái này thì đọc cái kia không khó.

#### 4. LogQL — giống PromQL, thêm phần lọc chữ

Một truy vấn LogQL gồm hai phần:

```text
{container="prometheus"}  |= "error"
└─────────┬──────────┘   └────┬────┘
   chọn dòng log nào        lọc nội dung
   (BẮT BUỘC)               (tuỳ chọn)
```

| Toán tử | Nghĩa |
|---|---|
| `\|=` | Có chứa chuỗi này |
| `!=` | Không chứa |
| `\|~` | Khớp biểu thức chính quy |
| `!~` | Không khớp biểu thức chính quy |

Và điều thú vị nhất: **biến log thành số** để vẽ đồ thị như metric:

```promql
sum(rate({container="grafana"} |= "error" [5m]))    # số dòng lỗi mỗi giây
```

> ⚠️ **Phần chọn nhãn là bắt buộc.** Không thể tìm khơi khơi trên toàn bộ log như Google. Phải nói rõ "trong container nào / job nào" trước. Đây là cái giá của việc Loki không đánh chỉ mục nội dung — và cũng là lý do nó rẻ.

### 🧪 LAB — Gom log mọi container về một chỗ

**Những gì thêm vào thư mục cũ:**

```text
lab44-prometheus/
├── docker-compose.yml                      # SỬA — thêm loki + promtail
├── loki-config.yaml                        # THÊM
├── promtail-config.yaml                    # THÊM
└── grafana/provisioning/datasources/
    └── loki.yml                            # THÊM — nối Grafana tới Loki
```

#### File 1 — thêm 2 service vào `docker-compose.yml`

```yaml
  loki:
    image: grafana/loki:3.3.2
    container_name: loki
    restart: unless-stopped
    ports:
      - "3100:3100"
    command: -config.file=/etc/loki/loki-config.yaml
    volumes:
      - ./loki-config.yaml:/etc/loki/loki-config.yaml:ro
      - loki-data:/loki

  promtail:
    image: grafana/promtail:3.3.2
    container_name: promtail
    restart: unless-stopped
    command: -config.file=/etc/promtail/promtail-config.yaml
    volumes:
      - ./promtail-config.yaml:/etc/promtail/promtail-config.yaml:ro
      - /var/run/docker.sock:/var/run/docker.sock:ro   # để tự tìm các container
      - /var/lib/docker/containers:/var/lib/docker/containers:ro
    depends_on:
      - loki
```

Và bổ sung vào mục `volumes:` cuối file:

```yaml
volumes:
  prom-data:
  grafana-data:
  loki-data:
```

#### File 2 — `loki-config.yaml`

```yaml
auth_enabled: false            # lab: không xác thực. Production thì BẮT BUỘC bật.

server:
  http_listen_port: 3100
  log_level: warn

common:
  instance_addr: 127.0.0.1
  path_prefix: /loki
  storage:
    filesystem:                # lab dùng đĩa local; production dùng S3/GCS
      chunks_directory: /loki/chunks
      rules_directory: /loki/rules
  replication_factor: 1
  ring:
    kvstore:
      store: inmemory

schema_config:
  configs:
    - from: 2024-01-01
      store: tsdb
      object_store: filesystem
      schema: v13
      index:
        prefix: index_
        period: 24h

limits_config:
  retention_period: 168h       # giữ log 7 ngày
  allow_structured_metadata: true
  ingestion_rate_mb: 8

compactor:
  working_directory: /loki/compactor
  retention_enabled: true      # phải bật thì retention_period mới có tác dụng
  delete_request_store: filesystem
```

#### File 3 — `promtail-config.yaml`

```yaml
server:
  http_listen_port: 9080
  log_level: warn

positions:
  filename: /tmp/positions.yaml     # nhớ đã đọc tới đâu, khởi động lại không đọc trùng

clients:
  - url: http://loki:3100/loki/api/v1/push

scrape_configs:
  - job_name: docker
    # Tự phát hiện MỌI container đang chạy — không phải khai từng cái
    docker_sd_configs:
      - host: unix:///var/run/docker.sock
        refresh_interval: 10s

    relabel_configs:
      # Tên container: bỏ dấu "/" ở đầu
      - source_labels: ['__meta_docker_container_name']
        regex: '/(.*)'
        target_label: 'container'

      # Tên image, để lọc theo loại dịch vụ
      - source_labels: ['__meta_docker_container_label_com_docker_compose_service']
        target_label: 'service'

      - target_label: 'job'
        replacement: 'docker'
```

#### File 4 — `grafana/provisioning/datasources/loki.yml`

```yaml
apiVersion: 1

datasources:
  - name: Loki
    type: loki
    access: proxy
    url: http://loki:3100
    isDefault: false
    editable: false
```

### 🧭 Hướng dẫn làm LAB — step by step

#### Bước 1 — Tạo file và khởi động

```bash
cd ~/lab44-prometheus
# tạo loki-config.yaml, promtail-config.yaml, grafana/provisioning/datasources/loki.yml
# sửa docker-compose.yml thêm 2 service + volume loki-data
docker compose up -d
docker compose ps
```

**Bạn sẽ thấy 7 container:**
```text
NAME            STATUS
alertmanager    Up
cadvisor        Up
grafana         Up
loki            Up 15 seconds
node-exporter   Up
promtail        Up 12 seconds
prometheus      Up
```

✅ **Checkpoint:** cả `loki` và `promtail` đều `Up`, không `Restarting`.

⚠️ **Nếu `loki` restart liên tục:** gần như luôn là sai cấu hình. Xem lý do:
```bash
docker compose logs loki | grep -i "error\|failed" | tail -10
```
Lỗi hay gặp là `schema` không hợp lệ — phải đúng `v13` + `tsdb` với Loki 3.x.

#### Bước 2 — Kiểm tra Loki đã sống

```bash
curl -s localhost:3100/ready
echo
curl -s "localhost:3100/loki/api/v1/labels" | head -c 200
echo
```

**Bạn sẽ thấy:**
```text
ready
{"status":"success","data":["container","job","service",...]}
```

✅ **Checkpoint:** trả về `ready`, và danh sách nhãn có `container`.

💡 Danh sách nhãn này chính là "mục lục" của Loki. Nó **không** đánh chỉ mục nội dung log — chỉ mấy cái nhãn này thôi. Đó là lý do nó nhẹ.

⚠️ Nếu danh sách nhãn trống: Promtail chưa đẩy được gì. Kiểm tra `docker compose logs promtail | tail -20` — thường do thiếu quyền đọc `docker.sock`.

#### Bước 3 — Tra log đầu tiên trong Grafana

Mở **http://localhost:3000** → **Explore** (biểu tượng la bàn) → chọn nguồn dữ liệu **Loki** ở góc trên.

Dán vào ô truy vấn:

```logql
{job="docker"}
```

Bấm **Run query** (hoặc `Shift+Enter`).

**Bạn sẽ thấy** dòng log từ tất cả container, mới nhất ở trên, kèm nhãn `container` bên cạnh mỗi dòng.

✅ **Checkpoint:** có log hiện ra.

Lọc đúng một container:

```logql
{container="prometheus"}
```

✅ **Checkpoint:** chỉ còn log của Prometheus.

💡 Đây đã là một bước tiến lớn so với `docker logs`: bạn xem log **nhiều container cùng lúc, trên cùng một trục thời gian**, không phải mở 7 cửa sổ terminal.

#### Bước 4 — Lọc nội dung và đếm

```logql
{job="docker"} |= "error"
```

Nếu chưa có lỗi nào, hãy tự tạo ra vài cái:

```bash
docker compose exec prometheus wget -qO- http://localhost:9090/khong-ton-tai || true
curl -s localhost:9090/api/v1/query?query=cu_phap[[[sai > /dev/null
curl -s localhost:3100/loki/api/v1/query?query=cung_sai{{{ > /dev/null
```

Chạy lại truy vấn, và thử thêm các biến thể:

```logql
{job="docker"} |= "error" != "debug"          # có "error" nhưng không có "debug"
{job="docker"} |~ "(?i)(error|warn|fail)"     # regex, (?i) = không phân biệt hoa thường
```

✅ **Checkpoint:** kết quả thu hẹp đúng theo từng bộ lọc.

Giờ **biến log thành đồ thị** — chuyển tab sang **Metrics** hoặc gõ truy vấn dạng số:

```logql
sum by (container) (rate({job="docker"} |~ "(?i)error" [5m]))
```

**Bạn sẽ thấy:** một biểu đồ đường — số dòng lỗi mỗi giây, tách theo container.

✅ **Checkpoint:** log đã biến thành metric vẽ được.

💡 **Đây là điều rất mạnh:** bạn có thể đặt cảnh báo trên *log* y như trên metric — ví dụ "báo động nếu số dòng ERROR vượt 10/giây". Không cần app phải tự expose metric lỗi.

#### Bước 5 — Đi trọn một ca điều tra sự cố thật

Đây là phần đáng giá nhất hôm nay: ghép metric với log đúng như lúc trực hệ thống.

**Tạo sự cố:**
```bash
docker compose stop node-exporter
```

**Bước điều tra 1 — metric báo có chuyện.** Mở dashboard *Sức khoẻ hệ thống* (Ngày 45): panel *Số target đang sống* tụt từ 3 xuống **2** và chuyển **đỏ**.

→ Bạn biết **"có gì đó sai"**, nhưng chưa biết sai cái gì.

**Bước điều tra 2 — nhảy sang log để biết sai cái gì.** Vào **Explore → Loki**:

```logql
{container="prometheus"} |= "node-exporter"
```

**Bạn sẽ thấy** những dòng kiểu:
```text
level=warn ... msg="Error scraping target" target=http://node-exporter:9100/metrics
  err="Get \"http://node-exporter:9100/metrics\": dial tcp ... connect: connection refused"
```

✅ **Checkpoint:** log chỉ thẳng ra nguyên nhân — `connection refused`, tức dịch vụ không còn lắng nghe.

**Bước điều tra 3 — xác nhận và khắc phục:**
```bash
docker compose ps node-exporter        # thấy trạng thái exited
docker compose start node-exporter
```

Chờ khoảng 30 giây, dashboard trở lại **3** và xanh.

💡 **Hãy ghi nhớ đúng trình tự này — nó là quy trình chuẩn khi xử lý sự cố:**

| Bước | Công cụ | Trả lời câu hỏi |
|---|---|---|
| 1 | Metric (Prometheus/Grafana) | *Có chuyện gì không?* |
| 2 | **Log (Loki)** | *Sai cái gì?* |
| 3 | Trace (Module nâng cao NC1) | *Sai ở khúc nào trong chuỗi dịch vụ?* |

Ba trụ cột observability không phải ba thứ song song để chọn một — chúng là **ba bước liên tiếp** của cùng một cuộc điều tra.

#### Bước 6 — Xem mô hình nhãn tiết kiệm thế nào

```bash
curl -s "localhost:3100/loki/api/v1/label/container/values" | head -c 300
echo
```

**Bạn sẽ thấy** danh sách tên container.

✅ **Checkpoint:** chỉ có vài nhãn, mỗi nhãn ít giá trị.

💡 **Đây chính là chỗ Loki tiết kiệm được tiền:** nó chỉ lưu chỉ mục cho vài nhãn này, còn hàng triệu dòng log thì nén lại để nguyên. Nếu bạn lỡ thêm nhãn động (như `request_id`), số chuỗi sẽ bùng nổ và Loki chậm đi trông thấy — **đúng bài học cardinality của Ngày 44**, lặp lại ở tầng log.

#### Bước 7 — Dọn dẹp

```bash
docker compose stop
# docker compose down -v    # chỉ khi muốn xoá sạch cả metric lẫn log đã thu
```

💡 Bạn vừa dựng xong một bộ giám sát hoàn chỉnh: **Prometheus + Alertmanager + Grafana + cAdvisor + Loki + Promtail**, tất cả từ file cấu hình, tái lập được ở bất cứ đâu. Đây là bộ mà rất nhiều công ty đang chạy thật.

### 💡 Đi làm mới thấm (sách cơ bản hay bỏ quên)

- **Log phải có cấu trúc (JSON), đừng để dạng văn xuôi.** `{"muc":"error","ma_don":123,"thong_diep":"thanh toán thất bại"}` cho phép lọc theo trường (`| json | ma_don="123"`). Còn `Loi thanh toan don 123` thì chỉ tìm được bằng cách khớp chuỗi. Đây là việc phải làm **từ phía ứng dụng**, không phải việc của Loki.
- **Nhãn phải ÍT, và phải hữu hạn.** Đừng bao giờ đưa `user_id`, `request_id`, `trace_id` vào **nhãn** — số chuỗi bùng nổ, Loki sập. Những thứ đó thuộc về **nội dung** log (hoặc structured metadata), tìm bằng bộ lọc chữ.
- **Không bao giờ ghi bí mật vào log.** Mật khẩu, token, số thẻ lọt vào log là lộ vĩnh viễn với mọi người có quyền xem log — thường là nhiều người hơn bạn tưởng. Nhiều đội đặt bộ lọc che tự động ở tầng thu thập.
- **Retention là quyết định về tiền, không phải kỹ thuật.** Giữ log 30 ngày nghe hay, nhưng đó là hoá đơn lưu trữ thật. Cách làm phổ biến: giữ đầy đủ 7 ngày, còn thứ cần lâu hơn thì rút thành metric (như ở Bước 4) — metric rẻ hơn log rất nhiều lần.
- **Đồng bộ giờ là điều kiện tiên quyết.** Log từ nhiều máy lệch giờ nhau thì dòng thời gian trở nên vô nghĩa và bạn sẽ suy luận sai nhân quả. `chrony`/`systemd-timesyncd` phải chạy đúng trên mọi máy (Ngày 10).
- **Cùng một `trace_id` trong log là bước đệm sang tracing.** Nếu mọi dịch vụ ghi kèm một mã định danh chung cho mỗi request, bạn có thể lần theo một request qua toàn hệ thống chỉ bằng log — đó là cây cầu dẫn sang distributed tracing (Module nâng cao NC1).

### 📝 Tự kiểm tra

> Nghĩ câu trả lời **thành lời** trước khi mở đáp án — nghĩ thầm luôn thấy mình hiểu.

<details>
<summary><b>1. Loki khác Elasticsearch ở điểm cốt lõi nào? Cái giá phải trả là gì?</b></summary>

Loki **chỉ đánh chỉ mục nhãn**, không đánh chỉ mục nội dung log. Nội dung được nén lại để đó. Khi tìm, nó lọc theo nhãn trước cho tập nhỏ lại, rồi mới quét nội dung.

Nhờ vậy Loki nhẹ hơn ELK rất nhiều về RAM và đĩa.

**Cái giá:** phần chọn nhãn là **bắt buộc** — không thể tìm khơi khơi trên toàn bộ log như Google. Phải nói rõ 'trong container nào / job nào' trước.

</details>

<details>
<summary><b>2. Mô tả quy trình điều tra một sự cố bằng ba trụ cột observability.</b></summary>

Ba trụ cột không phải ba lựa chọn thay thế nhau — chúng là **ba bước liên tiếp** của cùng một cuộc điều tra:

| Bước | Công cụ | Trả lời |
|---|---|---|
| 1 | Metric (Prometheus/Grafana) | *Có chuyện gì không?* |
| 2 | **Log (Loki)** | *Sai cái gì?* |
| 3 | Trace (Jaeger/Tempo) | *Sai ở khúc nào trong chuỗi dịch vụ?* |

Ví dụ thật: dashboard báo target chết → tra log thấy `connection refused` → biết dịch vụ không còn lắng nghe → khởi động lại.

</details>

<details>
<summary><b>3. Vì sao không được đưa `request_id` vào nhãn của Loki? Vậy tìm theo nó bằng cách nào?</b></summary>

Vì đó là **giá trị vô hạn** — mỗi request đẻ một nhãn mới → số chuỗi bùng nổ → Loki chậm đi trông thấy. Đúng bài học cardinality của Ngày 44, lặp lại ở tầng log.

`request_id` thuộc về **nội dung** log, không phải nhãn. Tìm nó bằng bộ lọc chữ:
```logql
{job="docker"} |= "abc-123-def"
```
Hoặc nếu log ở dạng JSON có cấu trúc: `{job="docker"} | json | request_id="abc-123-def"`

</details>

### 📚 Thuật ngữ Anh–Việt (ngày này)

| Thuật ngữ | Nghĩa |
|---|---|
| **Loki** | Hệ gom log 'như Prometheus' — chỉ đánh chỉ mục nhãn, không đánh chỉ mục nội dung |
| **Promtail / Alloy** | Tác nhân đọc log container, gắn nhãn, đẩy về Loki |
| **LogQL** | Ngôn ngữ truy vấn log: `{nhãn} |= "chuỗi"` |
| **`|=` `!=` `|~` `!~`** | Chứa / không chứa / khớp regex / không khớp regex |
| **Structured logging** | Ghi log dạng JSON để lọc được theo trường, không phải khớp chuỗi |
| **Retention** | Thời gian giữ log — quyết định về **tiền**, không phải kỹ thuật |
| **3 trụ cột observability** | Metrics (có sai không) → Logs (sai gì) → Traces (sai ở đâu) |
| **`trace_id`** | Mã định danh chung cho một request qua nhiều dịch vụ — cầu nối sang tracing |

### 🎯 Đúc kết Ngày 46

**3 điều phải mang theo:**

1. **Loki chỉ đánh chỉ mục nhãn, không đánh chỉ mục nội dung.** Rẻ hơn ELK rất nhiều, đổi lại bạn **bắt buộc** phải chọn nhãn trước khi tìm.
2. **Metric → Log → Trace là ba bước của một cuộc điều tra**, không phải ba lựa chọn thay thế nhau.
3. **Log có cấu trúc + ít nhãn** là hai điều kiện để hệ thống log còn dùng được khi quy mô lớn lên.

> 🧠 **Một câu để nhớ:** metric bảo bạn **"có cháy"**, log bảo bạn **"cháy ở bếp, do chập điện"**. Thiếu cái thứ hai thì bạn chỉ biết hoảng.

**✅ Tự chấm** *(đánh dấu khi làm được mà không nhìn tài liệu):*

- [ ] Giải thích Loki khác Elasticsearch ở điểm cốt lõi nào
- [ ] Kể vai trò của Promtail, Loki, Grafana trong đường đi của một dòng log
- [ ] Viết LogQL chọn nhãn + lọc chuỗi + lọc bằng regex
- [ ] Biến log thành đồ thị bằng `rate(...)` và nói ứng dụng của nó
- [ ] Đi trọn quy trình: metric bất thường → tra log → tìm ra nguyên nhân
- [ ] Nói rõ vì sao không được đưa `request_id` vào nhãn
- [ ] Nêu 2 lý do log nên ở dạng JSON

✅ **Kết quả đạt được:** Log của toàn bộ hệ thống chảy về một nơi tra cứu được, ghép chung màn hình với metric — bạn đã có đủ hai trụ cột để tự điều tra một sự cố từ đầu đến cuối.

---

## Ngày 47 — Configuration Management: Ansible

> ⏱️ ~90 phút · Loại: Tự động hoá
>
> 🧭 **Bạn đang ở đâu:** Ngày 46 (giám sát đầy đủ) → **Ngày 47 (Ansible — cấu hình hàng loạt máy bằng code)** → Ngày 48 (Terraform nâng cao). Terraform (Ngày 29) **tạo ra** máy; Ansible **cấu hình bên trong** máy. Hai việc khác nhau, bổ sung cho nhau.
>
> ✅ **Chuẩn bị:** máy Linux có Docker (ta sẽ dựng 3 "server" giả bằng container — **không cần thuê VM nào**), và Python 3.
>
> 🎁 **Cuối ngày bạn có gì:** một playbook cấu hình **3 máy cùng lúc** chỉ bằng một lệnh, chạy lại bao nhiêu lần cũng an toàn, có template sinh cấu hình riêng cho từng máy và một file bí mật được mã hoá thật.

### 📘 Lý thuyết

#### 1. Vấn đề: Bash script không mở rộng được

Ngày 5–6 bạn viết Bash để tự động hoá. Nó tốt cho một máy. Nhưng với 20 máy:

```bash
# Chạy lần 2 thì sao?
apt install nginx -y           # may mà apt biết bỏ qua
echo "..." >> /etc/nginx/x.conf  # ✗ ghi thêm lần nữa -> file hỏng
useradd deploy                   # ✗ báo lỗi "user đã tồn tại"
```

Hai vấn đề cốt lõi của Bash:

1. **Không idempotent** — chạy lại lần hai cho kết quả khác lần một.
2. **Ra lệnh, không mô tả** — script nói *"làm các bước này"*, không nói *"máy phải trông như thế nào"*.

Ansible giải cả hai: bạn **mô tả trạng thái mong muốn**, Ansible tự kiểm tra và chỉ thay đổi những gì chưa khớp. Lại chính là tư duy khai báo của Ngày 36, lần này áp cho máy chủ.

#### 2. Idempotent — khái niệm quan trọng nhất hôm nay

> **Idempotent** = chạy 1 lần hay 100 lần đều cho cùng một kết quả.

```yaml
- name: Đảm bảo nginx đã cài
  apt:
    name: nginx
    state: present      # "phải CÓ" — chưa có thì cài, có rồi thì bỏ qua
```

Chú ý cách diễn đạt: không phải *"hãy cài nginx"* mà là *"nginx phải ở trạng thái đã cài"*. Ansible kiểm tra trước, chỉ hành động khi cần. Nhờ vậy bạn có thể chạy playbook **bất cứ lúc nào** mà không sợ làm hỏng — và đó chính là thứ cho phép dùng nó để *sửa trôi cấu hình*.

#### 3. Vì sao Ansible dễ triển khai: không cần cài gì lên máy đích

| | Ansible | Puppet / Chef |
|---|---|---|
| Trên máy đích | **Không cần cài gì** (chỉ cần SSH + Python) | Phải cài agent |
| Cách hoạt động | Đẩy lệnh qua SSH | Agent tự kéo về theo chu kỳ |
| Ngôn ngữ | YAML | DSL riêng, phải học thêm |

Không cần agent nghĩa là: có SSH vào được máy nào thì quản lý được máy đó, **ngay lập tức**.

#### 4. Bốn khái niệm

| Khái niệm | Là gì |
|---|---|
| **Inventory** | Danh sách máy, chia nhóm (`[web]`, `[db]`) |
| **Playbook** | File YAML mô tả việc cần làm |
| **Module** | Đơn vị việc dựng sẵn (`apt`, `copy`, `service`, `user`...) — có hơn 3000 cái |
| **Role** | Cách đóng gói playbook để dùng lại, như thư viện |

#### 5. Handler — chỉ chạy khi thật sự có thay đổi

```yaml
tasks:
  - name: Đặt file cấu hình nginx
    template:
      src: nginx.conf.j2
      dest: /etc/nginx/conf.d/trang.conf
    notify: khoi dong lai nginx        # CHỈ báo khi file thật sự đổi

handlers:
  - name: khoi dong lai nginx
    service:
      name: nginx
      state: restarted
```

Điểm tinh tế: handler **chỉ chạy khi task báo có thay đổi**. Chạy playbook 10 lần mà cấu hình không đổi thì nginx không bị khởi động lại lần nào. Đây là lý do playbook an toàn để chạy định kỳ.

### 🧪 LAB — Cấu hình 3 "server" cùng lúc

> Ta dựng 3 container Linux có SSH để đóng vai server. Với Ansible, chúng **không khác gì máy thật** — cùng là "cái gì đó SSH vào được".

**Cây thư mục:**

```text
lab47-ansible/
├── docker-compose.yml       # dựng 3 server giả
├── Dockerfile.server        # server giả: Debian + sshd + python3
├── inventory.ini            # danh sách máy
├── playbook.yml             # nội dung chính
├── templates/
│   └── trang-chu.html.j2    # template sinh trang riêng cho từng máy
└── bi-mat.yml               # file bí mật (sẽ mã hoá bằng Ansible Vault)
```

#### File 1 — `Dockerfile.server`

```dockerfile
FROM debian:12-slim

RUN apt-get update && \
    apt-get install -y --no-install-recommends openssh-server python3 sudo && \
    rm -rf /var/lib/apt/lists/* && \
    mkdir -p /run/sshd

# Tạo user để Ansible đăng nhập, cho sudo không cần mật khẩu
RUN useradd -m -s /bin/bash quantri && \
    echo "quantri ALL=(ALL) NOPASSWD:ALL" > /etc/sudoers.d/quantri && \
    mkdir -p /home/quantri/.ssh && chmod 700 /home/quantri/.ssh

COPY khoa_lab.pub /home/quantri/.ssh/authorized_keys
RUN chown -R quantri:quantri /home/quantri/.ssh && \
    chmod 600 /home/quantri/.ssh/authorized_keys

EXPOSE 22
CMD ["/usr/sbin/sshd", "-D"]
```

#### File 2 — `docker-compose.yml`

```yaml
services:
  web1:
    build:
      context: .
      dockerfile: Dockerfile.server
    container_name: may-web1
    ports:
      - "2201:22"

  web2:
    build:
      context: .
      dockerfile: Dockerfile.server
    container_name: may-web2
    ports:
      - "2202:22"

  db1:
    build:
      context: .
      dockerfile: Dockerfile.server
    container_name: may-db1
    ports:
      - "2203:22"
```

#### File 3 — `inventory.ini`

```ini
[web]
web1 ansible_host=127.0.0.1 ansible_port=2201 vai_tro="Máy web số 1"
web2 ansible_host=127.0.0.1 ansible_port=2202 vai_tro="Máy web số 2"

[db]
db1 ansible_host=127.0.0.1 ansible_port=2203 vai_tro="Máy cơ sở dữ liệu"

[all:vars]
ansible_user=quantri
ansible_ssh_private_key_file=./khoa_lab
ansible_ssh_common_args='-o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null'
ansible_python_interpreter=/usr/bin/python3
```

> 📌 Ở lab ta tắt kiểm tra host key cho đỡ vướng. **Production tuyệt đối không làm vậy** — đó là mở cửa cho tấn công xen giữa (nhắc lại cảnh báo ở Ngày 34).

#### File 4 — `templates/trang-chu.html.j2`

```jinja
<!DOCTYPE html>
<html lang="vi">
<head><meta charset="utf-8"><title>{{ inventory_hostname }}</title></head>
<body>
  <h1>Xin chào từ {{ inventory_hostname }}</h1>
  <ul>
    <li>Vai trò: {{ vai_tro }}</li>
    <li>Hệ điều hành: {{ ansible_facts['distribution'] }} {{ ansible_facts['distribution_version'] }}</li>
    <li>Số CPU: {{ ansible_facts['processor_vcpus'] }}</li>
    <li>Thuộc nhóm: {{ group_names | join(', ') }}</li>
  </ul>
  <p>Trang này do Ansible sinh ra — mỗi máy một nội dung khác nhau.</p>
</body>
</html>
```

#### File 5 — `playbook.yml`

```yaml
---
- name: Cấu hình toàn bộ máy chủ
  hosts: all
  become: true                    # chạy bằng quyền sudo

  vars:
    goi_can_thiet:
      - curl
      - vim
      - htop

  tasks:
    - name: Cập nhật danh sách gói (cache 1 giờ)
      apt:
        update_cache: true
        cache_valid_time: 3600

    - name: Đảm bảo các gói cơ bản đã cài
      apt:
        name: "{{ goi_can_thiet }}"
        state: present

    - name: Tạo user triển khai
      user:
        name: trienkhai
        shell: /bin/bash
        state: present

    - name: Tạo thư mục dùng chung
      file:
        path: /opt/ungdung
        state: directory
        owner: trienkhai
        mode: "0755"

# ---- Phần riêng cho nhóm web ----
- name: Cấu hình riêng máy web
  hosts: web
  become: true

  tasks:
    - name: Cài nginx
      apt:
        name: nginx
        state: present

    - name: Sinh trang chủ riêng cho từng máy
      template:
        src: templates/trang-chu.html.j2
        dest: /var/www/html/index.html
        mode: "0644"
      notify: khoi dong lai nginx      # chỉ báo khi file thay đổi

    - name: Đảm bảo nginx đang chạy
      service:
        name: nginx
        state: started

  handlers:
    - name: khoi dong lai nginx
      service:
        name: nginx
        state: restarted

# ---- Phần riêng cho nhóm db ----
- name: Cấu hình riêng máy cơ sở dữ liệu
  hosts: db
  become: true

  tasks:
    - name: Tạo thư mục dữ liệu
      file:
        path: /var/du-lieu
        state: directory
        mode: "0700"

    - name: Ghi ghi chú nhận diện máy
      copy:
        content: "Máy này giữ dữ liệu. Không xoá bừa.\n"
        dest: /var/du-lieu/DOC-TRUOC.txt
        mode: "0644"
```

### 🧭 Hướng dẫn làm LAB — step by step

#### Bước 1 — Cài Ansible

```bash
sudo apt update && sudo apt install -y ansible
# hoặc: python3 -m pip install --user ansible
ansible --version | head -2
```

**Bạn sẽ thấy:**
```text
ansible [core 2.16.x]
  config file = None
```

✅ **Checkpoint:** in ra phiên bản `ansible [core 2.x]`.

#### Bước 2 — Dựng 3 server giả

```bash
mkdir -p ~/lab47-ansible/templates && cd ~/lab47-ansible

# Tạo cặp khoá riêng cho lab (không dùng khoá cá nhân của bạn)
ssh-keygen -t ed25519 -f ./khoa_lab -N "" -C "ansible-lab"

# tạo Dockerfile.server và docker-compose.yml theo phần LAB
docker compose up -d --build
docker compose ps
```

**Bạn sẽ thấy:**
```text
NAME       STATUS         PORTS
may-db1    Up 5 seconds   0.0.0.0:2203->22/tcp
may-web1   Up 5 seconds   0.0.0.0:2201->22/tcp
may-web2   Up 5 seconds   0.0.0.0:2202->22/tcp
```

✅ **Checkpoint:** 3 container `Up`, mở 3 cổng SSH khác nhau.

Kiểm tra SSH vào được:
```bash
ssh -i ./khoa_lab -p 2201 -o StrictHostKeyChecking=no quantri@127.0.0.1 hostname
```

**Bạn sẽ thấy:** một chuỗi mã băm (tên host của container).

⚠️ **Nếu `Permission denied (publickey)`:** file `khoa_lab.pub` chưa có lúc build. Tạo khoá **trước** rồi build lại: `docker compose up -d --build`.

#### Bước 3 — Ansible nhìn thấy các máy chưa?

```bash
# tạo inventory.ini theo phần LAB
ansible all -i inventory.ini -m ping
```

**Bạn sẽ thấy:**
```text
web1 | SUCCESS => {
    "changed": false,
    "ping": "pong"
}
web2 | SUCCESS => { ... "ping": "pong" }
db1  | SUCCESS => { ... "ping": "pong" }
```

✅ **Checkpoint:** cả 3 máy đều `SUCCESS` với `pong`.

💡 `ping` của Ansible **không phải** ICMP ping. Nó thực sự SSH vào, chạy Python ở đó và nhận lời đáp. Nghĩa là `pong` chứng minh cả ba điều: mạng thông, SSH đúng khoá, và Python có sẵn trên máy đích.

Xem cách Ansible nhóm các máy:
```bash
ansible-inventory -i inventory.ini --graph
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

#### Bước 4 — Hỏi thông tin hàng loạt (việc hằng ngày của người vận hành)

Trước khi viết playbook, hãy thấy sức mạnh của lệnh một dòng:

```bash
ansible all -i inventory.ini -m shell -a "uptime" 
ansible web -i inventory.ini -m shell -a "df -h /" 
```

✅ **Checkpoint:** kết quả trả về từ **cả nhóm máy** trong một lần gõ.

💡 Tưởng tượng 50 máy và câu hỏi *"máy nào sắp đầy ổ?"* — một dòng lệnh thay cho 50 lần SSH. Riêng khả năng này đã đủ để Ansible có chỗ đứng.

Xem "facts" — thông tin Ansible tự thu thập về máy:
```bash
ansible web1 -i inventory.ini -m setup -a "filter=ansible_distribution*"
```

**Bạn sẽ thấy:** `ansible_distribution: Debian`, `ansible_distribution_version: 12`...

💡 Chính những biến này được dùng trong template ở Bước 6.

#### Bước 5 — Chạy thử trước khi làm thật

```bash
# tạo playbook.yml và templates/trang-chu.html.j2 theo phần LAB
ansible-playbook -i inventory.ini playbook.yml --check --diff
```

**Bạn sẽ thấy** các dòng `changed` nhưng **không có gì thực sự bị thay đổi**:
```text
TASK [Cài nginx] ******************************
changed: [web1]
changed: [web2]
```

✅ **Checkpoint:** chạy xong mà hệ thống chưa bị đụng tới.

💡 **`--check` là chế độ chạy khô** — Ansible báo *sẽ* làm gì mà không làm thật. Thêm `--diff` để thấy **chính xác từng dòng** file sẽ thay đổi. Đây là thói quen bắt buộc trước khi chạy lên production, giống `helm template` ở Ngày 42 và `terraform plan` ở Ngày 29.

#### Bước 6 — Chạy thật

```bash
ansible-playbook -i inventory.ini playbook.yml
```

**Bạn sẽ thấy** phần tổng kết cuối cùng:
```text
PLAY RECAP *********************************************************
db1   : ok=6    changed=5    unreachable=0    failed=0
web1  : ok=9    changed=8    unreachable=0    failed=0
web2  : ok=9    changed=8    unreachable=0    failed=0
```

✅ **Checkpoint:** `failed=0` ở cả ba máy, và `changed` lớn hơn 0.

Kiểm chứng kết quả:
```bash
docker exec may-web1 curl -s localhost | head -12
echo "=================="
docker exec may-web2 curl -s localhost | grep "<h1>\|Vai trò"
echo "=================="
docker exec may-db1 cat /var/du-lieu/DOC-TRUOC.txt
```

**Bạn sẽ thấy:**
```text
<h1>Xin chào từ web1</h1>
  <li>Vai trò: Máy web số 1</li>
  <li>Hệ điều hành: Debian 12</li>
  ...
==================
<h1>Xin chào từ web2</h1>
  <li>Vai trò: Máy web số 2</li>
==================
Máy này giữ dữ liệu. Không xoá bừa.
```

✅ **Checkpoint:** **cùng một template** nhưng mỗi máy ra một nội dung khác — và máy `db1` không hề bị cài nginx.

💡 Đây là sức mạnh của template kết hợp inventory: một file khuôn, nhiều máy, mỗi máy tự điền thông tin của mình.

#### Bước 7 — Kiểm chứng idempotent (điểm cốt lõi hôm nay)

Chạy lại **y hệt lệnh cũ**:

```bash
ansible-playbook -i inventory.ini playbook.yml
```

**Bạn sẽ thấy:**
```text
PLAY RECAP *********************************************************
db1   : ok=6    changed=0    unreachable=0    failed=0
web1  : ok=9    changed=0    unreachable=0    failed=0
web2  : ok=9    changed=0    unreachable=0    failed=0
```

✅ **Checkpoint:** **`changed=0` ở mọi máy.**

💡 **Hãy dừng lại và ngẫm:** Ansible kiểm tra từng thứ, thấy đã đúng trạng thái mong muốn, nên **không làm gì cả**. Handler cũng không chạy → nginx không bị khởi động lại. Nếu đây là Bash script thì lần chạy thứ hai đã ghi thêm vào file cấu hình và có thể làm hỏng dịch vụ.

Giờ mô phỏng **trôi cấu hình** — ai đó sửa tay lên máy:

```bash
docker exec may-web1 sh -c 'echo "AI ĐÓ SỬA BẬY" > /var/www/html/index.html'
docker exec may-web1 curl -s localhost
```

Chạy lại playbook:

```bash
ansible-playbook -i inventory.ini playbook.yml | grep -A2 "PLAY RECAP"
docker exec may-web1 curl -s localhost | head -3
```

**Bạn sẽ thấy:**
```text
web1  : ok=9    changed=1    ...        ← ĐÚNG MỘT thay đổi: sửa lại file bị phá
web2  : ok=9    changed=0    ...        ← máy không bị phá thì không đụng tới

<!DOCTYPE html>
<html lang="vi">
```

✅ **Checkpoint:** Ansible sửa **đúng cái sai**, không đụng tới phần còn lại.

💡 **Đây chính là GitOps của Ngày 43, nhưng cho máy chủ thay vì cluster.** Cùng một ý tưởng: mô tả trạng thái mong muốn, chạy định kỳ, tự sửa những gì lệch.

#### Bước 8 — Ansible Vault: mã hoá bí mật thật sự

Nhớ Ngày 39: Secret của K8s chỉ là base64. Vault của Ansible thì mã hoá thật.

```bash
ansible-vault create bi-mat.yml
# Nhập mật khẩu 2 lần, trình soạn thảo mở ra -> gõ nội dung:
```

Nội dung file:
```yaml
mat_khau_db: "MatKhauThatSuBiMat"
khoa_api: "sk-that-su-bi-mat-123"
```

Lưu và thoát. Giờ xem file thô:

```bash
head -3 bi-mat.yml
```

**Bạn sẽ thấy:**
```text
$ANSIBLE_VAULT;1.1;AES256
38396164653238623361393661383931363564326266383265393638623831633...
64316562616434306339303436323064323537326638386637663830353965...
```

✅ **Checkpoint:** nội dung là chuỗi mã hoá AES256 — **không phải base64**.

💡 **Khác biệt then chốt so với Ngày 39:** file này **commit vào Git được**. Không có mật khẩu vault thì không ai đọc nổi. Đây là cách xử lý bí mật đúng đắn khi mọi thứ phải nằm trong Git.

Xem và dùng nó:
```bash
ansible-vault view bi-mat.yml            # nhập mật khẩu để xem
ansible-playbook -i inventory.ini playbook.yml -e @bi-mat.yml --ask-vault-pass
```

#### Bước 9 — Dọn dẹp

```bash
cd ~/lab47-ansible
docker compose down
```

💡 Giữ lại thư mục — nó là bộ khung tốt để bạn thử nghiệm thêm về sau.

### 💡 Đi làm mới thấm (sách cơ bản hay bỏ quên)

- **Ansible và Terraform không thay thế nhau.** Terraform **tạo ra** hạ tầng (máy, mạng, ổ đĩa); Ansible **cấu hình bên trong** máy. Quy trình thường thấy: `terraform apply` dựng VM → xuất danh sách IP ra inventory → `ansible-playbook` cấu hình. Dùng Terraform để cài gói phần mềm, hay dùng Ansible để tạo VPC, đều là dùng sai công cụ.
- **`--check` không phải lúc nào cũng chính xác.** Task phụ thuộc vào kết quả của task trước (ví dụ: cấu hình một dịch vụ mà bước cài đặt chưa chạy) có thể báo sai trong chế độ chạy khô. Nó hữu ích, nhưng đừng tin tuyệt đối.
- **`shell`/`command` là cửa thoát hiểm, không phải cửa chính.** Hai module này **không idempotent** — Ansible không biết lệnh của bạn làm gì. Bắt buộc phải dùng thì hãy thêm `creates:` hoặc `changed_when:` để nó biết khi nào cần chạy. Còn lại: luôn ưu tiên module chuyên dụng.
- **Dùng `serial` để khỏi tự sập cả hệ thống.** Playbook mặc định chạy song song trên **mọi** máy. Với dịch vụ đang phục vụ, `serial: 1` (hoặc `serial: "25%"`) sẽ cập nhật lần lượt — giống rolling update của K8s. Không có nó, một cấu hình sai sẽ hạ toàn bộ đội máy cùng lúc.
- **Ansible chậm với số máy lớn.** Đẩy qua SSH nên hàng trăm máy là thấy rõ. Bật `pipelining = True` trong `ansible.cfg` và tăng `forks` là cải thiện đáng kể.
- **Role và Ansible Galaxy để khỏi viết lại.** Cài nginx, Docker, PostgreSQL — đã có người viết sẵn và kiểm thử kỹ trên [Galaxy](https://galaxy.ansible.com). Nhưng nhớ **đọc code trước khi dùng** và ghim phiên bản: bạn đang cho code của người lạ chạy với quyền root trên máy chủ của mình.

### 📝 Tự kiểm tra

> Nghĩ câu trả lời **thành lời** trước khi mở đáp án — nghĩ thầm luôn thấy mình hiểu.

<details>
<summary><b>1. Idempotent nghĩa là gì? Vì sao Bash script thiếu nó lại nguy hiểm?</b></summary>

**Idempotent** = chạy 1 lần hay 100 lần đều cho cùng một kết quả.

Bash script thường không có tính này:
```bash
echo "..." >> /etc/nginx/x.conf   # chạy lần 2 -> ghi thêm lần nữa -> file hỏng
useradd deploy                    # chạy lần 2 -> báo lỗi
```

Ansible mô tả **trạng thái mong muốn** (`state: present`) và tự kiểm tra trước khi hành động. Nhờ vậy playbook chạy lại **bất cứ lúc nào** cũng an toàn — và đó chính là điều cho phép dùng nó để *sửa trôi cấu hình*.

</details>

<details>
<summary><b>2. Handler khác task thường ở điểm nào? Cho ví dụ vì sao nó quan trọng.</b></summary>

Handler **chỉ chạy khi task báo có thay đổi thật sự** (qua `notify`).

Ví dụ: task đặt file cấu hình nginx `notify: khoi dong lai nginx`. Chạy playbook 10 lần mà file không đổi → nginx **không bị khởi động lại lần nào**.

Không có cơ chế này, mỗi lần chạy playbook là một lần gián đoạn dịch vụ vô cớ. Đây là thứ khiến playbook an toàn để chạy định kỳ (ví dụ mỗi giờ để chống trôi cấu hình).

</details>

<details>
<summary><b>3. Khi nào dùng Terraform, khi nào dùng Ansible? Chúng thay thế nhau được không?</b></summary>

**Không thay thế nhau — chúng bổ sung:**
- **Terraform tạo ra** hạ tầng: máy ảo, mạng, ổ đĩa, load balancer
- **Ansible cấu hình bên trong** máy: cài gói, đặt file cấu hình, tạo user

Quy trình thường thấy: `terraform apply` dựng VM → xuất danh sách IP ra inventory → `ansible-playbook` cấu hình.

Dùng Terraform để cài gói phần mềm, hay dùng Ansible để tạo VPC, đều là **dùng sai công cụ** — làm được nhưng rất gượng ép.

</details>

### 📚 Thuật ngữ Anh–Việt (ngày này)

| Thuật ngữ | Nghĩa |
|---|---|
| **Idempotent** | Chạy bao nhiêu lần cũng cho cùng kết quả — khái niệm quan trọng nhất |
| **Inventory** | Danh sách máy cần quản lý, chia theo nhóm |
| **Playbook** | File YAML mô tả trạng thái mong muốn của các máy |
| **Module** | Đơn vị việc dựng sẵn (`apt`, `copy`, `service`) — hơn 3000 cái |
| **Handler** | Task chỉ chạy khi có thay đổi thật sự (qua `notify`) |
| **Role** | Cách đóng gói playbook để dùng lại — như thư viện |
| **Facts** | Thông tin Ansible tự thu thập về máy (OS, CPU, IP...) |
| **Ansible Vault** | Mã hoá **AES256 thật** — khác hẳn base64 của K8s Secret |
| **`--check --diff`** | Chạy khô: báo sẽ đổi gì mà không đổi thật |
| **`serial`** | Cập nhật lần lượt từng nhóm máy thay vì tất cả cùng lúc |
| **Agentless** | Không cần cài gì lên máy đích — chỉ cần SSH + Python |

### 🎯 Đúc kết Ngày 47

**3 điều phải mang theo:**

1. **Idempotent là tất cả.** Mô tả trạng thái mong muốn thay vì liệt kê các bước — nhờ đó playbook chạy lại lúc nào cũng an toàn, và tự sửa được trôi cấu hình.
2. **Không cần agent.** SSH vào được máy nào là quản lý được máy đó ngay, không phải cài thêm gì.
3. **Terraform tạo máy, Ansible cấu hình máy.** Phân vai rõ ràng thì hệ thống mới gọn.

> 🧠 **Một câu để nhớ:** Bash nói *"hãy làm các bước sau"*; Ansible nói *"máy phải trông như thế này"* — và tự kiểm tra xem còn thiếu gì.

**✅ Tự chấm** *(đánh dấu khi làm được mà không nhìn tài liệu):*

- [ ] Giải thích idempotent và vì sao Bash script thiếu nó lại nguy hiểm
- [ ] Viết inventory chia nhóm và chạy lệnh cho riêng một nhóm
- [ ] Dùng `--check --diff` để xem trước thay đổi
- [ ] Viết template Jinja2 sinh nội dung khác nhau cho từng máy
- [ ] Chứng minh `changed=0` khi chạy lại lần hai
- [ ] Phá cấu hình bằng tay rồi chạy playbook và thấy nó sửa đúng chỗ sai
- [ ] Mã hoá bí mật bằng Ansible Vault và nói rõ nó khác Secret của K8s thế nào
- [ ] Nói được khi nào dùng Terraform, khi nào dùng Ansible

✅ **Kết quả đạt được:** Một playbook cấu hình được cả đội máy trong một lệnh, chạy lại an toàn, tự sửa trôi cấu hình — kỹ năng cốt lõi để vận hành hạ tầng không dùng container.

---

## Ngày 48 — Terraform nâng cao: Module, Remote State & Workspace

> ⏱️ ~90 phút · Loại: IaC
>
> 🧭 **Bạn đang ở đâu:** Ngày 47 (Ansible cấu hình máy) → **Ngày 48 (Terraform ở mức dùng được trong đội)** → Ngày 49 (bảo mật pipeline). Ngày 29 bạn đã viết Terraform cho một người dùng một mình. Hôm nay giải ba vấn đề chỉ xuất hiện khi **làm việc theo đội**: lặp code, tranh chấp state, và nhiều môi trường.
>
> ✅ **Chuẩn bị:** Docker đang chạy. **Không cần tài khoản cloud, không tốn một đồng nào** — ta dùng provider Docker để tạo hạ tầng thật trên máy, và MinIO làm kho lưu state tương thích S3.
>
> 🎁 **Cuối ngày bạn có gì:** một module tái sử dụng, state lưu từ xa như đội thật vẫn làm, và hai môi trường dev/prod sinh ra từ **cùng một bộ code**.

### 📘 Lý thuyết

#### 1. Ba vấn đề xuất hiện khi Terraform ra khỏi máy cá nhân

| Vấn đề | Biểu hiện | Lời giải |
|---|---|---|
| **Lặp code** | 3 môi trường = 3 thư mục copy-paste, sửa một chỗ quên hai chỗ | **Module** |
| **State ở máy cá nhân** | File `terraform.tfstate` nằm trên laptop bạn. Đồng nghiệp không có. Hai người chạy cùng lúc là hỏng | **Remote state + khoá** |
| **Nhiều môi trường** | Cần dev và prod giống nhau về cấu trúc nhưng khác về quy mô | **Workspace** hoặc thư mục riêng |

#### 2. State — hiểu đúng thì mọi thứ sáng ra

`terraform.tfstate` là **sổ ghi chép ánh xạ** giữa code và tài nguyên thật:

```text
  Code của bạn              State (sổ ghi)                Thực tế
  resource "web" {...}  ←→  web = id "a3f2c9..."   ←→   container đang chạy
```

Không có state, Terraform **không biết** thứ nào nó đã tạo. Hệ quả rất thực tế:

- Mất state → `terraform apply` tưởng chưa có gì → **tạo trùng toàn bộ hạ tầng**.
- State ở laptop → đồng nghiệp chạy `apply` cũng tạo trùng.
- Hai người chạy cùng lúc → hai bên ghi đè state của nhau → **sổ ghi sai lệch với thực tế**.

> ⚠️ **State chứa bí mật ở dạng chữ thường.** Mật khẩu database, khoá truy cập — tất cả nằm trong đó. Vì vậy: **không bao giờ commit state vào Git**, và kho lưu state phải được mã hoá cùng phân quyền chặt.

#### 3. Remote state + khoá

Chuyển state lên kho dùng chung (S3, GCS, Terraform Cloud) thì cả đội nhìn cùng một sổ. Kèm theo đó là **khoá (lock)**: khi một người đang `apply`, người thứ hai bị chặn lại thay vì ghi đè.

```text
  Chưa có khoá:  A và B cùng apply  →  sổ ghi loạn, tài nguyên mồ côi
  Có khoá:       A apply (giữ khoá) →  B nhận "state đang bị khoá, chờ chút"
```

#### 4. Module — hàm số của hạ tầng

Module chỉ đơn giản là **một thư mục chứa file `.tf`** được dùng lại với tham số khác nhau. Hãy nghĩ nó như một hàm:

```text
  module (hàm)  ──  variables (tham số vào)  ──  outputs (giá trị trả về)
```

```hcl
module "web" {
  source    = "./modules/ung-dung"
  ten       = "web"
  so_ban    = 2
}

module "api" {
  source    = "./modules/ung-dung"   # CÙNG module
  ten       = "api"
  so_ban    = 3                      # khác tham số
}
```

Viết một lần, dùng nhiều nơi — đúng tinh thần Helm chart của Ngày 42, chỉ khác là cho hạ tầng.

#### 5. Workspace — cùng code, nhiều bản state

Một workspace = **một file state riêng** cho cùng một bộ code:

```bash
terraform workspace new dev
terraform workspace new prod
terraform workspace select dev
```

Trong code, đọc workspace đang dùng bằng `terraform.workspace` để đổi quy mô theo môi trường.

> 🔑 **Nhưng hãy biết giới hạn của nó:** workspace hợp khi các môi trường **gần như giống hệt nhau**, chỉ khác quy mô. Khi dev và prod khác nhau về kiến trúc (prod có thêm bản dự phòng, thêm CDN, thêm tài khoản cloud riêng), phần lớn các đội chọn **thư mục riêng cho mỗi môi trường** — rõ ràng và ít rủi ro nhầm lẫn hơn. Nguy cơ lớn nhất của workspace là **quên `select` và lỡ tay apply nhầm lên production**.

### 🧪 LAB — Module, remote state và hai môi trường

**Cây thư mục:**

```text
lab48-terraform/
├── modules/
│   └── ung-dung/
│       ├── main.tf           # module tái sử dụng
│       ├── variables.tf
│       └── outputs.tf
├── main.tf                   # gọi module 2 lần
├── variables.tf
├── outputs.tf
├── backend.tf                # cấu hình remote state (thêm ở Bước 5)
└── minio-compose.yml         # kho S3 giả lập, chạy local
```

#### File 1 — `modules/ung-dung/variables.tf`

```hcl
variable "ten" {
  description = "Tên ứng dụng, dùng để đặt tên container"
  type        = string
}

variable "so_ban" {
  description = "Số bản sao cần chạy"
  type        = number
  default     = 1

  validation {
    condition     = var.so_ban > 0 && var.so_ban <= 10
    error_message = "so_ban phải nằm trong khoảng 1 đến 10."
  }
}

variable "cong_bat_dau" {
  description = "Cổng đầu tiên trên máy chủ; các bản sau tăng dần"
  type        = number
}

variable "moi_truong" {
  description = "Tên môi trường (dev/prod)"
  type        = string
}

variable "id_mang" {
  description = "ID mạng Docker để gắn container vào"
  type        = string
}
```

#### File 2 — `modules/ung-dung/main.tf`

```hcl
terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 3.0"
    }
  }
}

resource "docker_image" "nginx" {
  name         = "nginx:1.27-alpine"
  keep_locally = true          # giữ image lại khi destroy, đỡ phải tải lại
}

resource "docker_container" "ung_dung" {
  count = var.so_ban           # tạo ra đúng số bản sao yêu cầu

  name  = "${var.moi_truong}-${var.ten}-${count.index + 1}"
  image = docker_image.nginx.image_id

  ports {
    internal = 80
    external = var.cong_bat_dau + count.index
  }

  networks_advanced {
    name = var.id_mang
  }

  # Ghi thông tin nhận diện vào trang chủ
  command = [
    "/bin/sh", "-c",
    "echo '<h1>${var.ten} - bản ${count.index + 1} - môi trường ${var.moi_truong}</h1>' > /usr/share/nginx/html/index.html && nginx -g 'daemon off;'"
  ]

  labels {
    label = "moi_truong"
    value = var.moi_truong
  }

  labels {
    label = "quan_ly_boi"
    value = "terraform"
  }
}
```

#### File 3 — `modules/ung-dung/outputs.tf`

```hcl
output "ten_cac_container" {
  description = "Danh sách tên container đã tạo"
  value       = docker_container.ung_dung[*].name
}

output "cac_cong" {
  description = "Danh sách cổng truy cập"
  value       = [for c in docker_container.ung_dung : c.ports[0].external]
}
```

#### File 4 — `main.tf` (thư mục gốc)

```hcl
terraform {
  required_version = ">= 1.5"
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 3.0"
    }
  }
}

provider "docker" {}

locals {
  moi_truong = terraform.workspace        # tên workspace chính là tên môi trường

  # Quy mô khác nhau theo môi trường
  quy_mo = {
    dev  = { web = 1, api = 1 }
    prod = { web = 3, api = 2 }
  }

  cau_hinh = lookup(local.quy_mo, local.moi_truong, local.quy_mo["dev"])
}

resource "docker_network" "mang" {
  name = "mang-${local.moi_truong}"
}

module "web" {
  source       = "./modules/ung-dung"
  ten          = "web"
  so_ban       = local.cau_hinh.web
  cong_bat_dau = local.moi_truong == "prod" ? 8100 : 8000
  moi_truong   = local.moi_truong
  id_mang      = docker_network.mang.id
}

module "api" {
  source       = "./modules/ung-dung"       # CÙNG module, khác tham số
  ten          = "api"
  so_ban       = local.cau_hinh.api
  cong_bat_dau = local.moi_truong == "prod" ? 8150 : 8050
  moi_truong   = local.moi_truong
  id_mang      = docker_network.mang.id
}
```

#### File 5 — `outputs.tf`

```hcl
output "moi_truong_dang_dung" {
  value = terraform.workspace
}

output "container_web" {
  value = module.web.ten_cac_container
}

output "container_api" {
  value = module.api.ten_cac_container
}

output "duong_dan_truy_cap" {
  value = [for p in concat(module.web.cac_cong, module.api.cac_cong) : "http://localhost:${p}"]
}
```

#### File 6 — `minio-compose.yml`

```yaml
services:
  minio:
    image: minio/minio:RELEASE.2024-11-07T00-52-20Z
    container_name: minio-state
    command: server /data --console-address ":9001"
    ports:
      - "9000:9000"      # API tương thích S3
      - "9001:9001"      # giao diện web
    environment:
      MINIO_ROOT_USER: quantri
      MINIO_ROOT_PASSWORD: matkhau123
    volumes:
      - minio-data:/data

volumes:
  minio-data:
```

### 🧭 Hướng dẫn làm LAB — step by step

#### Bước 1 — Cài Terraform (nếu chưa có từ Ngày 29)

```bash
terraform version || {
  wget -O- https://apt.releases.hashicorp.com/gpg | \
    sudo gpg --dearmor -o /usr/share/keyrings/hashicorp.gpg
  echo "deb [signed-by=/usr/share/keyrings/hashicorp.gpg] \
    https://apt.releases.hashicorp.com $(lsb_release -cs) main" | \
    sudo tee /etc/apt/sources.list.d/hashicorp.list
  sudo apt update && sudo apt install -y terraform
}
terraform version
```

**Bạn sẽ thấy:** `Terraform v1.10.x`.

✅ **Checkpoint:** in ra phiên bản `v1.5` trở lên.

#### Bước 2 — Tạo cấu trúc module và khởi tạo

```bash
mkdir -p ~/lab48-terraform/modules/ung-dung && cd ~/lab48-terraform
# tạo 5 file .tf theo phần LAB
terraform init
```

**Bạn sẽ thấy:**
```text
Initializing modules...
- api in modules/ung-dung
- web in modules/ung-dung

Initializing provider plugins...
- Installing kreuzwerker/docker v3.x.x...

Terraform has been successfully initialized!
```

✅ **Checkpoint:** dòng `Initializing modules...` liệt kê **cả `web` và `api`** — hai lần dùng, cùng một thư mục module.

⚠️ **Nếu lỗi `Failed to query available provider packages`:** kiểm tra mạng. Nếu lỗi kết nối Docker, xác nhận `docker ps` chạy được không cần `sudo` (Ngày 34).

#### Bước 3 — Tạo môi trường dev

```bash
terraform workspace new dev
terraform plan
```

**Bạn sẽ thấy** cuối phần plan:
```text
Plan: 5 to add, 0 to change, 0 to destroy.
```

(1 network + 1 web + 1 api + 2 image = 5)

```bash
terraform apply -auto-approve
```

**Bạn sẽ thấy** phần outputs:
```text
Outputs:

container_api = ["dev-api-1"]
container_web = ["dev-web-1"]
duong_dan_truy_cap = ["http://localhost:8000", "http://localhost:8050"]
moi_truong_dang_dung = "dev"
```

Kiểm chứng:
```bash
docker ps --filter "label=moi_truong=dev" --format "table {{.Names}}\t{{.Ports}}"
curl -s localhost:8000
```

**Bạn sẽ thấy:**
```text
NAMES        PORTS
dev-api-1    0.0.0.0:8050->80/tcp
dev-web-1    0.0.0.0:8000->80/tcp

<h1>web - bản 1 - môi trường dev</h1>
```

✅ **Checkpoint:** 2 container chạy thật, tên có tiền tố `dev-`.

#### Bước 4 — Tạo môi trường prod từ CÙNG bộ code

Đây là bước cho thấy giá trị của workspace:

```bash
terraform workspace new prod
terraform workspace list
```

**Bạn sẽ thấy:**
```text
  default
  dev
* prod            ← dấu * là workspace đang dùng
```

```bash
terraform apply -auto-approve
docker ps --filter "label=quan_ly_boi=terraform" --format "table {{.Names}}\t{{.Ports}}"
```

**Bạn sẽ thấy:**
```text
NAMES        PORTS
prod-api-1   0.0.0.0:8150->80/tcp
prod-api-2   0.0.0.0:8151->80/tcp
prod-web-1   0.0.0.0:8100->80/tcp
prod-web-2   0.0.0.0:8101->80/tcp
prod-web-3   0.0.0.0:8102->80/tcp
dev-api-1    0.0.0.0:8050->80/tcp
dev-web-1    0.0.0.0:8000->80/tcp
```

✅ **Checkpoint:** prod có **5 container** (3 web + 2 api), dev vẫn nguyên 2 container — **hai môi trường sống song song từ một bộ code**.

Xem state được tách ra thế nào:
```bash
ls terraform.tfstate.d/
```

**Bạn sẽ thấy:**
```text
dev  prod
```

💡 **Mỗi workspace một file state riêng** — đó là toàn bộ cơ chế. Code chung, sổ ghi riêng.

⚠️ **Và đây cũng là chỗ nguy hiểm:** gõ `terraform destroy` mà quên kiểm tra đang ở workspace nào thì bạn xoá nhầm production. Hãy tạo thói quen chạy `terraform workspace show` **trước mọi lệnh apply/destroy**.

#### Bước 5 — Chuyển state lên kho từ xa

Đến giờ state vẫn nằm trong thư mục của bạn. Hãy chuyển lên kho dùng chung.

Dựng MinIO (đóng vai S3):

```bash
# tạo minio-compose.yml theo phần LAB
docker compose -f minio-compose.yml up -d
sleep 5

# Tạo bucket chứa state
docker run --rm --network host --entrypoint sh minio/mc:latest -c "
  mc alias set local http://127.0.0.1:9000 quantri matkhau123 &&
  mc mb --ignore-existing local/terraform-state &&
  mc ls local"
```

**Bạn sẽ thấy:**
```text
Added `local` successfully.
Bucket created successfully `local/terraform-state`.
[...] terraform-state/
```

✅ **Checkpoint:** bucket `terraform-state` đã tạo.

Tạo `backend.tf`:

```hcl
terraform {
  backend "s3" {
    bucket = "terraform-state"
    key    = "lab48/terraform.tfstate"
    region = "us-east-1"                  # MinIO không dùng, nhưng bắt buộc khai

    endpoints = {
      s3 = "http://127.0.0.1:9000"
    }

    access_key = "quantri"
    secret_key = "matkhau123"

    # Các tuỳ chọn để làm việc được với S3 giả lập
    skip_credentials_validation = true
    skip_metadata_api_check     = true
    skip_region_validation      = true
    skip_requesting_account_id  = true
    use_path_style              = true
  }
}
```

> ⚠️ Ở lab ta viết thẳng khoá vào file cho gọn. **Production tuyệt đối không** — dùng biến môi trường `AWS_ACCESS_KEY_ID` / `AWS_SECRET_ACCESS_KEY` hoặc IAM role.

Chuyển state lên:

```bash
terraform init -migrate-state
# Gõ: yes  khi được hỏi có chuyển state hiện có lên backend mới không
```

**Bạn sẽ thấy:**
```text
Successfully configured the backend "s3"! Terraform will automatically
use this backend unless the backend configuration changes.
```

Kiểm chứng state đã nằm trên kho:

```bash
docker run --rm --network host --entrypoint sh minio/mc:latest -c "
  mc alias set local http://127.0.0.1:9000 quantri matkhau123 >/dev/null &&
  mc ls -r local/terraform-state"
```

**Bạn sẽ thấy:**
```text
[...] 12KiB STANDARD env:prod/lab48/terraform.tfstate
[...]  9KiB STANDARD env:dev/lab48/terraform.tfstate
```

✅ **Checkpoint:** state của **cả hai workspace** đã nằm trên kho dùng chung.

💡 **Ý nghĩa thực tế:** giờ đồng nghiệp chỉ cần `terraform init` là thấy đúng hạ tầng bạn đang quản. Laptop bạn hỏng cũng không mất sổ ghi. Đây là điều kiện tối thiểu để Terraform dùng được trong đội.

#### Bước 6 — Đọc state như một công cụ điều tra

```bash
terraform state list
```

**Bạn sẽ thấy:**
```text
docker_network.mang
module.api.docker_image.nginx
module.api.docker_container.ung_dung[0]
module.api.docker_container.ung_dung[1]
module.web.docker_container.ung_dung[0]
module.web.docker_container.ung_dung[1]
module.web.docker_container.ung_dung[2]
...
```

✅ **Checkpoint:** thấy rõ đường dẫn phân cấp `module.<tên>.<tài nguyên>[chỉ số]`.

Xem chi tiết một tài nguyên:
```bash
terraform state show 'module.web.docker_container.ung_dung[0]' | head -20
```

💡 **Đây là công cụ điều tra chính khi Terraform hành xử khó hiểu.** Câu hỏi *"vì sao nó muốn tạo lại cái này?"* thường được trả lời bằng cách so state với thực tế.

#### Bước 7 — Thấy trôi cấu hình và cách Terraform sửa

Xoá một container bằng tay (giả lập người khác lỡ tay):

```bash
docker rm -f prod-web-2
terraform plan
```

**Bạn sẽ thấy:**
```text
Note: Objects have changed outside of Terraform
  # module.web.docker_container.ung_dung[1] has been deleted

Plan: 1 to add, 0 to change, 0 to destroy.
```

✅ **Checkpoint:** Terraform **phát hiện** thứ bị xoá ngoài luồng và đề nghị tạo lại.

```bash
terraform apply -auto-approve
docker ps --filter "name=prod-web" --format "{{.Names}}"
```

**Bạn sẽ thấy** đủ lại 3 container.

💡 Ba ngày liên tiếp bạn gặp lại đúng một ý tưởng: **ArgoCD (43)**, **Ansible (47)**, **Terraform (48)** — tất cả đều so *mong muốn* với *thực tế* rồi sửa cho khớp. Nắm chắc khuôn tư duy này thì công cụ nào cũng học nhanh.

#### Bước 8 — Dọn dẹp đúng thứ tự

```bash
terraform workspace select prod
terraform destroy -auto-approve

terraform workspace select dev
terraform destroy -auto-approve

terraform workspace select default
terraform workspace delete dev
terraform workspace delete prod

docker compose -f minio-compose.yml down -v
```

✅ **Checkpoint:** `docker ps` không còn container nào của lab.

⚠️ Luôn `destroy` **từng workspace** trước khi xoá nó. Xoá workspace khi tài nguyên còn sống sẽ để lại **hạ tầng mồ côi** — vẫn chạy, vẫn tính tiền, nhưng không còn code nào quản lý. Trên cloud thật thì đây là kiểu lãng phí rất khó phát hiện.

### 💡 Đi làm mới thấm (sách cơ bản hay bỏ quên)

- **Khoá state là bắt buộc, không phải tuỳ chọn.** Hai người cùng `apply` mà không có khoá thì state hỏng, và dọn dẹp rất đau. Trên AWS: dùng `use_lockfile = true` (Terraform 1.10 trở lên) hoặc bảng DynamoDB theo cách cũ. Trên GCS: khoá có sẵn.
- **Ghim phiên bản provider và module.** `version = "~> 3.0"` cho provider, `?ref=v1.2.0` cho module lấy từ Git. Không ghim thì hôm nay `apply` ra một kiểu, tháng sau ra kiểu khác — đúng bài học `latest` của Ngày 33, ở tầng hạ tầng.
- **`terraform plan` phải được đọc, không phải lướt qua.** Chú ý những dòng bắt đầu bằng `-/+` (**huỷ rồi tạo lại**). Với một container thì không sao; với một database production thì đó là mất dữ liệu. Nhiều tài nguyên có `lifecycle { prevent_destroy = true }` chính vì lý do này.
- **State chứa bí mật ở dạng chữ thường.** Mật khẩu database do Terraform tạo ra nằm nguyên trong state. Bật mã hoá cho bucket, siết quyền truy cập, và **không bao giờ** `git add terraform.tfstate`.
- **`terraform import` để tiếp quản hạ tầng có sẵn.** Vào công ty mới, hạ tầng đã dựng tay hết — không cần đập đi xây lại. Viết code mô tả nó rồi `import` vào state, dần dần đưa mọi thứ về IaC.
- **Đừng dùng workspace cho dev/prod khi hai môi trường khác nhau nhiều.** Nghe tiện nhưng rủi ro apply nhầm là có thật, và khi kiến trúc bắt đầu khác nhau thì code sẽ đầy `if`. Đa số đội chọn thư mục riêng cho mỗi môi trường, dùng chung module — rõ ràng hơn và an toàn hơn.

### 📝 Tự kiểm tra

> Nghĩ câu trả lời **thành lời** trước khi mở đáp án — nghĩ thầm luôn thấy mình hiểu.

<details>
<summary><b>1. State của Terraform là gì? Điều gì xảy ra nếu mất nó?</b></summary>

State là **sổ ghi chép ánh xạ** giữa code và tài nguyên thật: `resource "web"` ↔ `id "a3f2c9..."` ↔ container/VM đang chạy.

Mất state thì Terraform **không biết thứ nào nó đã tạo** → `apply` tưởng chưa có gì → **tạo trùng toàn bộ hạ tầng**.

Hệ quả khác: state ở laptop thì đồng nghiệp chạy `apply` cũng tạo trùng; hai người chạy cùng lúc thì ghi đè state của nhau và sổ ghi sai lệch với thực tế.

</details>

<details>
<summary><b>2. Vì sao không bao giờ được commit `terraform.tfstate` vào Git?</b></summary>

Hai lý do:
1. **State chứa bí mật ở dạng chữ thường** — mật khẩu database do Terraform tạo ra nằm nguyên trong đó
2. **Xung đột khi làm nhóm** — hai người sửa state cùng lúc là hỏng, và Git không merge được file này

Cách đúng: remote state (S3/GCS/Terraform Cloud) có **mã hoá** và **khoá**. Khi một người đang `apply`, người thứ hai bị chặn lại thay vì ghi đè.

</details>

<details>
<summary><b>3. Khi nào nên dùng workspace, khi nào nên tách thư mục cho mỗi môi trường?</b></summary>

**Workspace** hợp khi các môi trường **gần như giống hệt nhau**, chỉ khác quy mô — cùng code, khác file state.

**Tách thư mục** hợp hơn khi dev và prod **khác nhau về kiến trúc** (prod có thêm bản dự phòng, CDN, tài khoản cloud riêng). Dùng workspace lúc này sẽ khiến code đầy `if`.

Rủi ro lớn nhất của workspace: **quên `select` và lỡ tay apply nhầm lên production**. Tạo thói quen chạy `terraform workspace show` trước mọi lệnh apply/destroy.

</details>

### 📚 Thuật ngữ Anh–Việt (ngày này)

| Thuật ngữ | Nghĩa |
|---|---|
| **State** | Sổ ghi ánh xạ code ↔ tài nguyên thật; mất nó là Terraform mù |
| **Remote state** | State lưu ở kho dùng chung (S3/GCS) thay vì trên máy cá nhân |
| **State locking** | Khoá state khi đang apply, chặn người thứ hai ghi đè |
| **Module** | Thư mục `.tf` dùng lại được với tham số khác nhau — như hàm số |
| **Workspace** | Nhiều file state cho cùng một bộ code |
| **`terraform plan`** | Xem trước thay đổi; chú ý dòng `-/+` = **huỷ rồi tạo lại** |
| **`terraform import`** | Đưa hạ tầng đã có sẵn vào quản lý của Terraform |
| **`prevent_destroy`** | Chặn xoá nhầm tài nguyên quan trọng |
| **Drift** | Thực tế trôi khỏi state, thường do ai đó sửa tay trên console |

### 🎯 Đúc kết Ngày 48

**3 điều phải mang theo:**

1. **State là sổ ghi chép ánh xạ code ↔ thực tế.** Mất nó thì Terraform mù; để nó ở laptop thì cả đội không dùng chung được; không khoá nó thì hai người là hỏng.
2. **Module là hàm số của hạ tầng** — viết một lần, gọi nhiều nơi với tham số khác nhau. Hết cảnh copy-paste giữa các môi trường.
3. **Workspace tách state cho cùng bộ code**, hợp khi các môi trường gần giống nhau. Khác nhau nhiều thì tách thư mục an toàn hơn.

> 🧠 **Một câu để nhớ:** Terraform không nhìn vào cloud để biết bạn có gì — **nó nhìn vào state**. Hiểu điều đó là hiểu 90% những hành vi kỳ lạ của nó.

**✅ Tự chấm** *(đánh dấu khi làm được mà không nhìn tài liệu):*

- [ ] Giải thích state là gì và điều gì xảy ra khi mất nó
- [ ] Viết module có `variables` + `outputs` và gọi nó hai lần với tham số khác nhau
- [ ] Chuyển state từ local lên remote bằng `init -migrate-state`
- [ ] Nói rõ vì sao cần khoá state và cách bật nó trên AWS
- [ ] Dùng workspace tạo hai môi trường và chỉ ra file state của từng cái
- [ ] Đọc `terraform plan` và nhận ra dấu hiệu tài nguyên sẽ bị huỷ-tạo-lại
- [ ] Phát hiện trôi cấu hình và để Terraform sửa lại
- [ ] Nêu 2 lý do không nên commit state vào Git

✅ **Kết quả đạt được:** Terraform ở mức dùng được trong đội — code không lặp, state dùng chung an toàn, nhiều môi trường sinh ra từ một nguồn duy nhất.

---

## Ngày 49 — Bảo mật DevSecOps & Best Practices

> ⏱️ ~90 phút · Loại: Bảo mật
>
> 🧭 **Bạn đang ở đâu:** Ngày 48 (Terraform trong đội) → **Ngày 49 (gài bảo mật vào chính pipeline)** → Ngày 50 (Milestone ghép toàn bộ). Suốt Giai đoạn 3 bạn đã dựng được dây chuyền tự động; hôm nay dạy nó **tự từ chối** những thứ không an toàn.
>
> ✅ **Chuẩn bị:** repo `ci-demo` (Ngày 31–34) và thư mục `lab48-terraform` (Ngày 48). Docker đang chạy — mọi công cụ hôm nay chạy bằng container, **không cần cài gì lên máy**.
>
> 🎁 **Cuối ngày bạn có gì:** 4 lớp quét tự động chặn được lỗ hổng, bí mật lộ, Dockerfile ẩu và cấu hình hạ tầng nguy hiểm — tất cả chạy ngay trong CI, cộng một lần **tự tay làm lộ mật khẩu rồi tự tìm ra nó**.

### 📘 Lý thuyết

#### 1. Vấn đề: bảo mật kiểm tra cuối cùng thì đã quá muộn

Cách làm cũ: viết code vài tháng → trước khi lên production, đội bảo mật rà soát → tìm ra 50 vấn đề → sửa lại rất tốn kém, và ai cũng bực.

**Shift-left** nghĩa là đẩy việc kiểm tra về **phía trái** của dòng thời gian — càng sớm càng rẻ:

| Phát hiện lúc | Chi phí sửa tương đối |
|---|---|
| Lúc gõ code | **1** |
| Lúc chạy CI | ~5 |
| Trên production | ~50 |
| Sau khi bị tấn công | ~500 và mất uy tín |

Cùng một lỗi. Chỉ khác thời điểm phát hiện. DevSecOps là việc biến bảo mật thành **một bước tự động trong pipeline**, không phải một cuộc họp ở cuối dự án.

#### 2. Bốn lớp cần quét (và công cụ cho từng lớp)

| Lớp | Tìm cái gì | Công cụ dùng hôm nay |
|---|---|---|
| **Bí mật** | Mật khẩu, token lỡ commit vào Git | **Gitleaks** |
| **Thư viện & image** | Lỗ hổng đã biết (CVE) trong gói bạn dùng | **Trivy** |
| **Dockerfile** | Cách viết ẩu, chạy bằng root, tag `latest` | **Hadolint** |
| **Hạ tầng dạng code** | Cổng mở toang, không mã hoá, quyền quá rộng | **Checkov** |

> 🔑 Điểm chung: cả bốn đều **chạy được trong CI và trả về mã lỗi khác 0** khi phát hiện vấn đề. Nhờ vậy chúng chặn được pipeline — đúng như bài học branch protection của Ngày 32.

#### 3. CVE và điểm nghiêm trọng

**CVE** là mã định danh toàn cầu cho một lỗ hổng đã được công bố (ví dụ `CVE-2024-3094`). Mỗi CVE có điểm **CVSS** từ 0 đến 10:

| Mức | Điểm | Ứng xử thực tế |
|---|---|---|
| CRITICAL | 9.0–10 | Sửa ngay, chặn pipeline |
| HIGH | 7.0–8.9 | Sửa ngay, chặn pipeline |
| MEDIUM | 4.0–6.9 | Đưa vào kế hoạch |
| LOW | 0.1–3.9 | Ghi nhận |

> ⚠️ **Đừng đặt ngưỡng chặn ở mức quá thấp ngay từ đầu.** Chặn pipeline vì mọi lỗ hổng LOW sẽ khiến cả đội quen với việc bỏ qua cảnh báo — và rồi họ bỏ qua luôn cái CRITICAL. Bắt đầu bằng **chặn ở HIGH và CRITICAL**, siết dần sau.

#### 4. Bí mật lỡ commit: xoá file là chưa đủ

Đây là hiểu lầm nguy hiểm nhất về Git. Bạn commit nhầm mật khẩu, phát hiện ra, xoá file rồi commit tiếp. Xong chưa?

**Chưa.** Git lưu **toàn bộ lịch sử** — bất kỳ ai clone repo vẫn lấy được mật khẩu đó từ commit cũ. Quy trình xử lý đúng:

1. **Vô hiệu hoá bí mật đó ngay** (đổi mật khẩu, thu hồi token) — đây là bước **quan trọng nhất và phải làm đầu tiên**.
2. Sau đó mới xoá khỏi lịch sử (`git filter-repo` hoặc BFG).
3. Bật quét tự động để không tái diễn.

> 🔑 Ghi nhớ: **bí mật đã lộ thì phải coi như đã bị đánh cắp**, kể cả repo private. Xoá khỏi lịch sử chỉ là dọn dẹp, không phải khắc phục.

#### 5. Nguyên tắc đặc quyền tối thiểu

Xuyên suốt khoá học bạn đã gặp nguyên tắc này nhiều lần mà có thể chưa để ý:

| Ngày | Biểu hiện |
|---|---|
| 33 | Container chạy bằng user thường, không phải root |
| 31, 33 | `permissions:` của `GITHUB_TOKEN` chỉ xin đúng thứ cần |
| 39 | RBAC giới hạn ai đọc được Secret |
| 43 | GitOps: **không ai bên ngoài** giữ chìa khoá cluster |

Một câu duy nhất: **cho đúng quyền cần thiết, không hơn**. Khi có sự cố, đây là thứ quyết định thiệt hại dừng ở một container hay lan ra cả hệ thống.

### 🧪 LAB — Bốn lớp quét, chạy tại máy rồi đưa vào CI

**File sẽ thêm vào repo `ci-demo`:**

```text
ci-demo/
├── .github/workflows/
│   └── bao-mat.yml          # THÊM — quét tự động
├── .gitleaks.toml           # THÊM — cấu hình quét bí mật
└── .hadolint.yaml           # THÊM — cấu hình quét Dockerfile
```

#### File 1 — `.gitleaks.toml`

```toml
title = "Cấu hình quét bí mật cho ci-demo"

[extend]
useDefault = true          # dùng toàn bộ luật mặc định (hơn 100 loại token)

# Thêm luật riêng cho dự án
[[rules]]
id = "mat-khau-trong-code"
description = "Mật khẩu viết thẳng trong code"
regex = '''(?i)(mat_khau|password|passwd|pwd)\s*[:=]\s*["'][^"']{8,}["']'''
tags = ["mat-khau"]

[allowlist]
description = "Bỏ qua các giá trị ví dụ trong tài liệu"
regexes = [
  '''ban@example\.com''',
  '''matkhau123''',              # mật khẩu lab, cố ý công khai
  '''MatKhauSieuBiMat123''',
]
paths = [
  '''(.*?)(md|txt)$''',           # bỏ qua file tài liệu
]
```

#### File 2 — `.hadolint.yaml`

```yaml
failure-threshold: warning       # cảnh báo trở lên là coi như trượt

ignored:
  - DL3008                       # không bắt buộc ghim phiên bản gói apt (gây phiền cho alpine)

trustedRegistries:
  - docker.io
  - ghcr.io
  - registry.k8s.io
```

#### File 3 — `.github/workflows/bao-mat.yml`

```yaml
name: Quét bảo mật

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]
  schedule:
    - cron: '0 2 * * 1'          # 2h sáng thứ Hai hằng tuần

permissions:
  contents: read

jobs:
  # ---------- Lớp 1: bí mật lỡ commit ----------
  quet-bi-mat:
    name: Quét bí mật
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0          # BẮT BUỘC: cần TOÀN BỘ lịch sử mới quét được commit cũ

      - name: Gitleaks
        uses: gitleaks/gitleaks-action@v2
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}

  # ---------- Lớp 2: cách viết Dockerfile ----------
  quet-dockerfile:
    name: Kiểm tra Dockerfile
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Hadolint
        uses: hadolint/hadolint-action@v3.1.0
        with:
          dockerfile: Dockerfile
          config: .hadolint.yaml

  # ---------- Lớp 3: lỗ hổng trong thư viện và image ----------
  quet-lo-hong:
    name: Quét lỗ hổng
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Trivy quét mã nguồn và thư viện
        uses: aquasecurity/trivy-action@0.28.0
        with:
          scan-type: fs
          scan-ref: .
          severity: HIGH,CRITICAL      # chỉ chặn ở mức cao
          exit-code: '1'               # có phát hiện -> pipeline ĐỎ
          ignore-unfixed: true         # bỏ qua lỗ hổng chưa có bản vá

      - name: Build image để quét
        run: docker build -t ci-demo:quet .

      - name: Trivy quét image
        uses: aquasecurity/trivy-action@0.28.0
        with:
          scan-type: image
          image-ref: ci-demo:quet
          severity: HIGH,CRITICAL
          exit-code: '1'
          ignore-unfixed: true

      - name: Tạo SBOM (danh mục thành phần)
        uses: aquasecurity/trivy-action@0.28.0
        with:
          scan-type: image
          image-ref: ci-demo:quet
          format: cyclonedx
          output: sbom.json

      - name: Lưu SBOM
        uses: actions/upload-artifact@v4
        with:
          name: sbom
          path: sbom.json
          retention-days: 30
```

### 🧭 Hướng dẫn làm LAB — step by step

#### Bước 1 — Quét lỗ hổng image bằng Trivy (chạy tại máy)

```bash
cd ~/ci-demo
docker build -t ci-demo:quet .

docker run --rm \
  -v /var/run/docker.sock:/var/run/docker.sock \
  -v "$HOME/.cache/trivy:/root/.cache/trivy" \
  aquasec/trivy:latest image --severity HIGH,CRITICAL ci-demo:quet
```

**Bạn sẽ thấy** (lần đầu mất ~30 giây để tải cơ sở dữ liệu lỗ hổng):
```text
ci-demo:quet (alpine 3.21.x)
============================
Total: 0 (HIGH: 0, CRITICAL: 0)
```

✅ **Checkpoint:** quét xong và có bảng tổng kết.

💡 Nếu ra `0` thì đó là **phần thưởng cho lựa chọn ở Ngày 33**: bạn dùng `node:20-alpine` thay vì `node:20` đầy đủ. Ít phần mềm trong image = ít thứ để khai thác.

Hãy chứng minh điều đó bằng cách quét một image cũ:

```bash
docker run --rm \
  -v "$HOME/.cache/trivy:/root/.cache/trivy" \
  aquasec/trivy:latest image --severity HIGH,CRITICAL node:18
```

**Bạn sẽ thấy** một danh sách dài:
```text
node:18 (debian 12.x)
Total: 87 (HIGH: 79, CRITICAL: 8)

┌──────────────┬────────────────┬──────────┬───────────────┬───────────────┐
│   Library    │ Vulnerability  │ Severity │ Installed Ver │  Fixed Ver    │
├──────────────┼────────────────┼──────────┼───────────────┼───────────────┤
│ libssl3      │ CVE-2024-xxxxx │ CRITICAL │ 3.0.11-1      │ 3.0.13-1      │
...
```

✅ **Checkpoint:** thấy rõ khác biệt giữa image gọn và image đầy đủ, cũ.

💡 **Bài học đắt giá:** phần lớn lỗ hổng trong image **không đến từ code của bạn** — chúng đến từ hệ điều hành nền và thư viện hệ thống. Vì vậy chọn image nền gọn và **cập nhật thường xuyên** là biện pháp bảo mật hiệu quả nhất, rẻ nhất.

#### Bước 2 — Tự làm lộ bí mật rồi tự tìm ra nó

Đây là bước nhớ lâu nhất. Cố tình commit một "mật khẩu":

> 📌 **Vì sao lab này SINH chuỗi lúc chạy thay vì in sẵn trong tài liệu:** một chuỗi giống token thật nằm trong file Markdown sẽ bị **chính GitHub chặn khi push** (tính năng secret scanning). Bản thân việc đó đã là một bài học — và cũng là lý do bạn sẽ tạo chuỗi bằng lệnh ngay dưới đây.

```bash
cd ~/ci-demo

# Sinh các chuỗi CÓ HÌNH DẠNG GIỐNG token thật — nhưng là số ngẫu nhiên, vô giá trị
KHOA_AWS="AKIA$(head -c 32 /dev/urandom | base64 | tr -dc 'A-Z0-9' | head -c 16)"
TOKEN_SLACK="xoxb-$(shuf -i 1000000000-9999999999 -n1)-$(shuf -i 1000000000-9999999999 -n1)-$(head -c 32 /dev/urandom | base64 | tr -dc 'a-z0-9' | head -c 24)"

cat > cau-hinh-tam.js <<EOF
// File này CỐ Ý sai để thấy công cụ bắt được
const cauHinh = {
  duongDanDb: "postgres://admin:SieuMatKhau@db.congty.com:5432/donhang",
  khoaApiAws: "$KHOA_AWS",
  tokenSlack: "$TOKEN_SLACK",
};
module.exports = cauHinh;
EOF

git add cau-hinh-tam.js
git commit -m "Thêm cấu hình (CỐ Ý SAI để thử công cụ)"
```

⚠️ **Tuyệt đối không `git push` nhánh này lên GitHub.** Lab này chỉ làm việc với repo ở máy. Nếu lỡ push, GitHub sẽ chặn — và đó chính xác là điều nên xảy ra.

Giờ quét toàn bộ lịch sử:

```bash
docker run --rm -v "$PWD:/repo" zricethezav/gitleaks:latest \
  detect --source=/repo --verbose --no-banner
```

**Bạn sẽ thấy:**
```text
Finding:     duongDanDb: "postgres://admin:SieuMatKhau@db.congty.com:5432/..."
Secret:      SieuMatKhau
RuleID:      postgres-connection-string
File:        cau-hinh-tam.js
Line:        3
Commit:      8f3a2c9d...

Finding:     khoaApiAws: "AKIAIOSFODNN7EXAMPLE"
RuleID:      aws-access-token
...

3 leaks found
```

✅ **Checkpoint:** tìm ra đủ **3 bí mật**, kèm số dòng và mã commit.

Giờ đến phần quan trọng nhất — **xoá file có đủ không?**

```bash
git rm cau-hinh-tam.js
git commit -m "Xoá file cấu hình"

# Quét lại toàn bộ lịch sử
docker run --rm -v "$PWD:/repo" zricethezav/gitleaks:latest \
  detect --source=/repo --no-banner
```

**Bạn sẽ thấy:**
```text
3 leaks found
```

✅ **Checkpoint:** **vẫn tìm ra 3 bí mật** dù file đã bị xoá.

Tự kiểm chứng bằng Git:
```bash
git log --all --oneline -- cau-hinh-tam.js
git show $(git log --format=%H -n1 --all -- cau-hinh-tam.js):cau-hinh-tam.js | head -5
```

**Bạn sẽ thấy** nội dung mật khẩu vẫn đọc được nguyên vẹn từ lịch sử.

💡 **Đây là điều phải khắc cốt ghi tâm:** `git rm` chỉ xoá ở hiện tại. Lịch sử giữ mọi thứ mãi mãi. Ai clone repo cũng lấy được. Vì vậy quy trình đúng là: **thu hồi bí mật trước** (đổi mật khẩu, revoke token) — rồi mới dọn lịch sử.

Dọn lịch sử cho sạch (lab này chỉ có 2 commit nên reset là đủ):
```bash
git reset --hard HEAD~2
docker run --rm -v "$PWD:/repo" zricethezav/gitleaks:latest \
  detect --source=/repo --no-banner
```

**Bạn sẽ thấy:** `no leaks found`.

⚠️ Với repo thật đã đẩy lên remote thì `reset` không dùng được. Phải dùng `git filter-repo` hoặc **BFG Repo-Cleaner**, và mọi người trong đội phải clone lại. Đó là lý do phòng bệnh (quét tự động) rẻ hơn chữa bệnh rất nhiều.

#### Bước 3 — Soi Dockerfile bằng Hadolint

```bash
docker run --rm -i hadolint/hadolint < Dockerfile
```

**Bạn sẽ thấy** (hoặc không có gì, nếu Dockerfile Ngày 33 của bạn đã tốt):
```text
-:6 DL3018 warning: Pin versions in apk add. Instead of `apk add <package>` use `apk add <package>=<version>`
```

Thử một Dockerfile viết ẩu để thấy nó bắt được gì:

```bash
cat > /tmp/Dockerfile.te <<'EOF'
FROM node:latest
RUN apt-get update
RUN apt-get install -y curl
ADD . /app
WORKDIR /app
RUN npm install
CMD npm start
EOF

docker run --rm -i hadolint/hadolint < /tmp/Dockerfile.te
```

**Bạn sẽ thấy:**
```text
-:1 DL3007 warning: Using latest is prone to errors if the image will ever update.
      Pin the version explicitly to a release tag
-:2 DL3009 info: Delete the apt-get lists after installing something
-:3 DL3008 warning: Pin versions in apt get install
-:4 DL3020 error: Use COPY instead of ADD for files and folders
-:7 DL3025 warning: Use arguments JSON notation for CMD and ENTRYPOINT arguments
```

✅ **Checkpoint:** bắt đúng các lỗi kinh điển, kèm mã luật tra cứu được.

💡 Chú ý `DL3007` — chính là bài học `latest` của Ngày 33, giờ được **tự động cưỡng chế**. Đây là điểm hay của công cụ: biến kinh nghiệm thành luật máy kiểm tra, không phụ thuộc vào việc người review có nhớ hay không.

#### Bước 4 — Quét hạ tầng dạng code bằng Checkov

```bash
cd ~/lab48-terraform
docker run --rm -v "$PWD:/tf" bridgecrew/checkov:latest \
  -d /tf --compact --quiet --framework terraform
```

**Bạn sẽ thấy:**
```text
terraform scan results:
Passed checks: 8, Failed checks: 3, Skipped checks: 0

Check: CKV_DOCKER_3: "Ensure that a user for the container has been created"
	FAILED for resource: docker_container.ung_dung
...
```

✅ **Checkpoint:** có bảng tổng kết passed/failed.

Thử với một cấu hình thật sự nguy hiểm:

```bash
mkdir -p /tmp/tf-te && cat > /tmp/tf-te/main.tf <<'EOF'
resource "aws_s3_bucket" "du_lieu" {
  bucket = "du-lieu-cong-ty"
}

resource "aws_security_group" "mo_toang" {
  name = "cho-phep-tat-ca"
  ingress {
    from_port   = 0
    to_port     = 65535
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]     # MỞ TOÀN BỘ CỔNG RA INTERNET
  }
}
EOF

docker run --rm -v /tmp/tf-te:/tf bridgecrew/checkov:latest -d /tf --compact --quiet
```

**Bạn sẽ thấy:**
```text
Check: CKV_AWS_260: "Ensure no security groups allow ingress from 0.0.0.0:0 to port 80"
	FAILED
Check: CKV_AWS_19: "Ensure all data stored in the S3 bucket is securely encrypted at rest"
	FAILED
Check: CKV_AWS_21: "Ensure all data stored in the S3 bucket have versioning enabled"
	FAILED
...
```

✅ **Checkpoint:** bắt được nhóm bảo mật mở toang và bucket không mã hoá.

💡 **Đây là loại lỗi gây rò rỉ dữ liệu nhiều nhất ngoài đời thật** — không phải kỹ thuật tấn công tinh vi, mà chỉ là một bucket cấu hình sai. Checkov bắt được nó **trước khi** `terraform apply`, tức trước khi nó tồn tại.

#### Bước 5 — Đưa tất cả vào CI

```bash
cd ~/ci-demo
# tạo .gitleaks.toml, .hadolint.yaml, .github/workflows/bao-mat.yml theo phần LAB
git add .gitleaks.toml .hadolint.yaml .github/workflows/bao-mat.yml
git commit -m "Thêm quét bảo mật tự động vào CI"
git push
```

Mở tab **Actions** → workflow **Quét bảo mật**.

**Bạn sẽ thấy 3 job chạy song song:**
```text
Quét bí mật          ✅
Kiểm tra Dockerfile  ✅
Quét lỗ hổng         ✅
```

✅ **Checkpoint:** cả 3 job xanh.

⚠️ **Nếu job quét bí mật báo lỗi thiếu lịch sử:** kiểm tra đã có `fetch-depth: 0` chưa. Mặc định `checkout` chỉ lấy **một** commit — quét như vậy sẽ bỏ sót toàn bộ lịch sử.

#### Bước 6 — Chứng minh CI thật sự chặn được

```bash
cd ~/ci-demo
git checkout -b thu-bao-mat
cat > lo-bi-mat.js <<'EOF'
const ketNoi = {
  password: "P4ssw0rd-Production-That-2026",   // luật "mat-khau-trong-code" sẽ bắt
};
module.exports = ketNoi;
EOF
git add lo-bi-mat.js
git commit -m "Thử: cố ý để lộ mật khẩu"
git push -u origin thu-bao-mat
```

> 📌 **Vì sao ở đây dùng mật khẩu chứ không dùng token của nhà cung cấp:** GitHub có **push protection** — chuỗi giống token AWS/Slack/GitHub thật sẽ bị chặn **ngay lúc `git push`**, trước cả khi workflow kịp chạy. Bạn sẽ không thấy được CI chặn PR. Dùng mật khẩu trong code thì push được, và bạn quan sát được đúng thứ cần quan sát.
>
> Nhân tiện, đây là **hai lớp bảo vệ khác nhau** và bạn nên biết cả hai: push protection của nền tảng chặn ở cổng vào; gitleaks trong CI là lớp của riêng bạn, bắt được cả những thứ nền tảng không biết (mật khẩu nội bộ, khoá riêng của công ty).

Mở Pull Request trên GitHub.

**Bạn sẽ thấy:**
```text
❌ Quét bí mật — Failing after 25s
🔒 Merging is blocked
```

✅ **Checkpoint:** PR bị chặn, không merge được (nhờ branch protection Ngày 32).

💡 **Đây là toàn bộ ý nghĩa của DevSecOps gói trong một màn hình:** bảo mật không còn là một cuộc họp ở cuối dự án, mà là **một cánh cửa tự động khoá lại** ngay khi có vấn đề — 25 giây sau khi bạn push.

Dọn dẹp:
```bash
git checkout main
git branch -D thu-bao-mat
git push origin --delete thu-bao-mat
```

#### Bước 7 — SBOM: biết mình đang dùng những gì

```bash
docker run --rm \
  -v /var/run/docker.sock:/var/run/docker.sock \
  aquasec/trivy:latest image --format cyclonedx --quiet ci-demo:quet \
  > /tmp/sbom.json

python -c "
import json
d = json.load(open('/tmp/sbom.json'))
tp = d.get('components', [])
print(f'Tổng số thành phần: {len(tp)}')
for c in tp[:8]:
    print(' -', c.get('name'), c.get('version'))
"
```

**Bạn sẽ thấy:**
```text
Tổng số thành phần: 42
 - alpine-baselayout 3.6.x
 - busybox 1.37.x
 - musl 1.2.x
 - nodejs 20.x.x
 ...
```

✅ **Checkpoint:** liệt kê được toàn bộ thành phần trong image.

💡 **SBOM (Software Bill of Materials)** là "danh mục thành phần" của phần mềm. Khi một lỗ hổng lớn được công bố (như Log4Shell năm 2021), câu hỏi đầu tiên của mọi công ty là *"chúng ta có dùng thư viện đó không, ở những đâu?"*. Có SBOM thì trả lời trong 5 phút; không có thì mất nhiều ngày rà soát. Nhiều nơi giờ đã **bắt buộc** nhà cung cấp phải nộp SBOM.

### 💡 Đi làm mới thấm (sách cơ bản hay bỏ quên)

- **Cảnh báo quá nhiều thì không ai đọc.** Bật quét ở mọi mức nghiêm trọng sẽ cho ra hàng trăm phát hiện ngày đầu tiên, cả đội nản và bắt đầu bỏ qua — kể cả cái thật sự nguy hiểm. Bắt đầu bằng **CRITICAL + HIGH, và chỉ những cái đã có bản vá** (`ignore-unfixed`), rồi siết dần. Đây đúng là bài học *alert fatigue* của Ngày 44, áp cho bảo mật.
- **`ignore-unfixed` là lựa chọn thực dụng.** Lỗ hổng chưa có bản vá thì chặn pipeline cũng chẳng giải quyết được gì — bạn không thể sửa. Ghi nhận, theo dõi, nhưng đừng để nó làm tê liệt việc phát hành.
- **Quét theo lịch quan trọng ngang quét theo commit.** Image bạn build hôm nay sạch sẽ; ba tuần nữa có CVE mới công bố cho một thư viện trong đó. Không quét lại định kỳ thì bạn chạy hàng tháng trời với một lỗ hổng đã biết mà không hay. Đó là lý do workflow ở trên có `schedule`.
- **Dependabot / Renovate lo phần nâng cấp.** Quét chỉ cho biết có vấn đề; hai công cụ này **tự mở Pull Request** nâng phiên bản thư viện. Kết hợp với CI đầy đủ (Ngày 32), bạn có được vòng lặp cập nhật gần như tự động.
- **Người là lớp phòng thủ cuối, không phải lớp đầu.** Công cụ bắt được cái đã biết; còn logic phân quyền sai (người dùng A xem được đơn hàng của người dùng B) thì không công cụ nào phát hiện. Quét tự động để giải phóng thời gian con người cho những thứ chỉ con người thấy được.
- **Đừng để quá trình build tự tải mã lạ về chạy.** `curl | bash` trong Dockerfile, action GitHub ghim `@main`, thư viện không khoá phiên bản — đó là những cánh cửa của tấn công chuỗi cung ứng. Ghim phiên bản (lý tưởng là ghim SHA) ở mọi tầng: image nền, thư viện, action, module Terraform.

### 📝 Tự kiểm tra

> Nghĩ câu trả lời **thành lời** trước khi mở đáp án — nghĩ thầm luôn thấy mình hiểu.

<details>
<summary><b>1. Shift-left nghĩa là gì? Minh hoạ bằng chi phí sửa lỗi.</b></summary>

**Đẩy việc kiểm tra về phía trái** của dòng thời gian — càng sớm càng rẻ:

| Phát hiện lúc | Chi phí tương đối |
|---|---|
| Gõ code | 1 |
| Chạy CI | ~5 |
| Trên production | ~50 |
| Sau khi bị tấn công | ~500 và mất uy tín |

Cùng một lỗi, chỉ khác thời điểm phát hiện. DevSecOps là biến bảo mật thành **một bước tự động trong pipeline**, không phải một cuộc họp ở cuối dự án.

</details>

<details>
<summary><b>2. Bạn `git rm` file chứa mật khẩu rồi commit. Vấn đề đã xong chưa?</b></summary>

**Chưa.** Git lưu **toàn bộ lịch sử** — bất kỳ ai clone repo vẫn lấy được mật khẩu từ commit cũ. `git rm` chỉ xoá ở hiện tại.

Quy trình đúng, **theo đúng thứ tự này**:
1. **Vô hiệu hoá bí mật ngay** (đổi mật khẩu, thu hồi token) — quan trọng nhất, làm đầu tiên
2. Xoá khỏi lịch sử (`git filter-repo` hoặc BFG)
3. Bật quét tự động để không tái diễn

Ghi nhớ: **bí mật đã lộ thì phải coi như đã bị đánh cắp**, kể cả repo private.

</details>

<details>
<summary><b>3. Vì sao không nên đặt ngưỡng chặn pipeline ở mọi mức nghiêm trọng ngay từ đầu?</b></summary>

Vì bật quét ở mọi mức sẽ cho ra **hàng trăm phát hiện ngày đầu tiên**. Cả đội nản, rồi bắt đầu bỏ qua cảnh báo — **kể cả cái CRITICAL thật sự nguy hiểm**.

Đây chính là *alert fatigue* của Ngày 44, áp cho bảo mật.

Cách làm đúng: bắt đầu bằng **CRITICAL + HIGH**, và chỉ những cái **đã có bản vá** (`ignore-unfixed` — lỗ hổng chưa có bản vá thì chặn cũng không giải quyết được gì). Rồi siết dần khi đội đã quen.

</details>

### 📚 Thuật ngữ Anh–Việt (ngày này)

| Thuật ngữ | Nghĩa |
|---|---|
| **Shift-left** | Đẩy kiểm tra về sớm trong vòng đời — càng sớm càng rẻ |
| **CVE / CVSS** | Mã định danh lỗ hổng công bố / điểm nghiêm trọng 0–10 |
| **Gitleaks** | Quét bí mật lỡ commit — quét **cả lịch sử**, cần `fetch-depth: 0` |
| **Trivy** | Quét lỗ hổng trong thư viện và image |
| **Hadolint** | Kiểm tra cách viết Dockerfile |
| **Checkov** | Quét cấu hình hạ tầng dạng code (Terraform, K8s) |
| **SBOM** | Danh mục thành phần — trả lời 'ta có dùng thư viện dính CVE không?' |
| **`ignore-unfixed`** | Bỏ qua lỗ hổng chưa có bản vá — thực dụng, tránh chặn vô ích |
| **Supply chain attack** | Tấn công qua thư viện/action/image bên thứ ba |
| **Dependabot / Renovate** | Tự mở PR nâng phiên bản thư viện có lỗ hổng |

### 🎯 Đúc kết Ngày 49

**3 điều phải mang theo:**

1. **Shift-left: phát hiện càng sớm càng rẻ.** Bảo mật phải là một bước tự động trong pipeline, không phải một cuộc rà soát ở cuối.
2. **Bí mật đã commit là bí mật đã lộ** — kể cả khi bạn đã xoá file. Thu hồi trước, dọn lịch sử sau.
3. **Bốn lớp quét, bốn loại rủi ro khác nhau:** bí mật (Gitleaks), lỗ hổng (Trivy), cách viết Dockerfile (Hadolint), cấu hình hạ tầng (Checkov). Không cái nào thay thế cái nào.

> 🧠 **Một câu để nhớ:** bảo mật không phải một bước cuối cùng trước khi phát hành — nó là **một cánh cửa tự động khoá** đứng ngay trong dây chuyền.

**✅ Tự chấm** *(đánh dấu khi làm được mà không nhìn tài liệu):*

- [ ] Giải thích shift-left và vì sao phát hiện sớm rẻ hơn nhiều lần
- [ ] Quét image bằng Trivy và giải thích vì sao image alpine ít lỗ hổng hơn
- [ ] Chứng minh `git rm` không xoá được bí mật khỏi lịch sử
- [ ] Nói đúng thứ tự xử lý khi lỡ commit bí mật
- [ ] Dùng Hadolint và giải thích ít nhất 3 mã luật nó báo
- [ ] Dùng Checkov bắt được security group mở toang
- [ ] Đưa quét vào CI với `exit-code: 1` và chứng minh PR bị chặn
- [ ] Nói được SBOM là gì và vì sao nó quan trọng lúc có CVE lớn

✅ **Kết quả đạt được:** Pipeline có bốn lớp phòng thủ tự động — bí mật, lỗ hổng, Dockerfile và hạ tầng đều được soi trước khi vào `main`, và bạn đã tự kiểm chứng rằng nó thật sự chặn được.

---

## Ngày 50 — MILESTONE: LAB tổng hợp Giai đoạn 3

> ⏱️ ~180 phút · Loại: LAB Final
>
> 🧭 **Bạn đang ở đâu:** Ngày 31–49 (CI/CD, Kubernetes, Helm, GitOps, giám sát, Ansible, Terraform, bảo mật) → **Ngày 50 (nối tất cả thành một vòng khép kín)** → Giai đoạn 4 (SRE & dự án tốt nghiệp).
>
> ✅ **Chuẩn bị:** cluster đang chạy, repo mã nguồn và repo cấu hình, stack giám sát.
>
> 🎯 **Đây là bài lớn nhất từ đầu khoá.** Nó ghép 19 ngày kiến thức vào một hệ thống duy nhất. Hãy chia thành 2–3 buổi nếu cần.

### 📋 Đề bài — "Vòng DevOps khép kín"

> Xây một hệ thống mà từ lúc bạn `git push` tới lúc **nhìn thấy thay đổi đó trên dashboard giám sát**, không ai chạm tay vào bất cứ đâu.

```text
   git push
      ↓
   [CI]  lint → test → quét bảo mật
      ↓
   [Image]  build → tag SHA → registry
      ↓
   [Repo cấu hình]  CI tự cập nhật tag
      ↓
   [ArgoCD]  phát hiện Git đổi → tự đồng bộ
      ↓
   [Kubernetes]  rolling update · probe · HPA · nhiều bản
      ↓
   [Giám sát]  Prometheus + Grafana + Loki → dashboard đổi theo
      ↓
   [Cảnh báo]  có vấn đề → báo ngay
      ↓
   quay lại đầu: sửa code → push
```

### ✅ Yêu cầu

#### Bắt buộc

| # | Yêu cầu | Kiến thức từ |
|---|---|---|
| 1 | CI đủ tầng + 3 lớp quét bảo mật, chặn được | Ngày 32, 49 |
| 2 | Image tag SHA trên registry | Ngày 33 |
| 3 | **Helm chart** cho ứng dụng, values tách theo môi trường | Ngày 42 |
| 4 | **GitOps**: ArgoCD tự đồng bộ từ repo cấu hình | Ngày 43 |
| 5 | Ứng dụng có probe, nhiều bản, HPA | Ngày 41 |
| 6 | **Prometheus + Grafana** với dashboard provisioning từ file | Ngày 44, 45 |
| 7 | **Loki** gom log toàn hệ thống | Ngày 46 |
| 8 | Ít nhất 3 cảnh báo có ý nghĩa | Ngày 44, 45 |
| 9 | Hạ tầng/namespace bằng **Terraform** | Ngày 48 |
| 10 | Quay lui bằng `git revert`, dưới 3 phút | Ngày 43 |
| 11 | Monorepo có cấu trúc rõ + README có sơ đồ | — |

#### Nâng cao

| # | Yêu cầu |
|---|---|
| 12 | CI **tự cập nhật tag** vào repo cấu hình (khép kín hoàn toàn) |
| 13 | Ansible cấu hình node hoặc máy chủ phụ trợ |
| 14 | `NetworkPolicy` giới hạn luồng mạng giữa các tầng |
| 15 | Cảnh báo gửi tới kênh chat thật |
| 16 | Triển khai canary hoặc blue-green |

### 📐 Tiêu chí chấm (100 điểm)

| Hạng mục | Điểm | Đạt tối đa khi |
|---|---:|---|
| CI & bảo mật | 15 | Nhiều tầng, 3 lớp quét chặn thật, dưới 5 phút |
| Đóng gói & registry | 10 | Tag bất biến, truy ngược được |
| Helm | 10 | Tham số hoá tốt, nhiều môi trường, `lint` sạch |
| GitOps | 15 | Tự đồng bộ, selfHeal hoạt động, quay lui bằng Git |
| Kubernetes | 15 | Probe, HPA, nhiều bản, requests đầy đủ |
| Giám sát | 20 | Metric + log + dashboard từ file + cảnh báo tới nơi thật |
| Hạ tầng bằng code | 10 | Terraform dựng được, có remote state |
| Tài liệu | 5 | README có sơ đồ, người lạ hiểu được |

> 🎯 **Từ 80 điểm** là đủ năng lực của một DevOps Engineer. Đây cũng chính là bộ khung cho dự án tốt nghiệp ở Ngày 56–59.

### 🔥 Phép thử lớn — "Một vòng trọn vẹn"

Đây là bài kiểm tra duy nhất thật sự quan trọng hôm nay. Làm liền mạch, ghi lại thời gian từng chặng.

```bash
# ── CHẶNG 1: Thay đổi code ─────────────────────
cd ~/cloudnote
sed -i 's/phiên bản cũ/PHIÊN BẢN MỚI/' app/backend/app.js
T0=$(date +%s)
git commit -am "Đo một vòng khép kín" && git push

# ── CHẶNG 2: theo dõi từng chặng ───────────────
# (mở song song các cửa sổ này)
#  a) tab Actions trên GitHub        → CI xanh lúc nào?
#  b) kubectl get application -n argocd -w  → Synced lúc nào?
#  c) kubectl get pods -w            → pod mới lên lúc nào?
#  d) dashboard Grafana              → đồ thị phản ánh lúc nào?

# ── CHẶNG 3: xác nhận ──────────────────────────
curl -s http://<dia-chi>/api/version
echo "Tổng thời gian một vòng: $(( $(date +%s) - T0 )) giây"
```

Ghi lại **bảng thời gian từng chặng** — nó cho bạn biết chỗ nghẽn nằm ở đâu:

| Chặng | Thời gian của bạn | Mốc tham khảo |
|---|---|---|
| push → CI xanh | ___ | dưới 3 phút |
| CI xanh → image trên registry | ___ | dưới 2 phút |
| image → ArgoCD phát hiện | ___ | dưới 3 phút (có webhook thì vài giây) |
| ArgoCD → pod mới chạy | ___ | dưới 1 phút |
| pod mới → dashboard phản ánh | ___ | dưới 1 phút |
| **Tổng** | ___ | **dưới 10 phút** |

### 🔥 Bốn phép thử phụ

**1. Tự phục hồi.** `kubectl delete pod -l app=api` → dịch vụ không gián đoạn, pod mới lên trong vài giây.

**2. Chống trôi cấu hình.** `kubectl scale deploy/api --replicas=9` → ArgoCD đưa về đúng số trong Git sau khoảng 30 giây.

**3. Quay lui.** `git revert` trên repo cấu hình → hệ thống về bản cũ. Bấm giờ.

**4. Phát hiện sự cố.** Dừng database → cảnh báo phải bắn **và** bạn phải tìm ra nguyên nhân bằng log trong vòng 5 phút.

### 🧪 Bộ kiểm chứng

```bash
#!/usr/bin/env bash
NS=cua-hang
diem=0
kiem() { if eval "$2" &>/dev/null; then echo "  ✅ $1 (+$3)"; diem=$((diem+$3)); else echo "  ❌ $1"; fi; }

echo "▸ CI & bảo mật"
for t in gitleaks trivy hadolint; do
  kiem "Quét bằng $t" "grep -rqi '$t' .github/workflows/" 4
done
kiem "CI nhiều tầng"              "grep -rq 'needs:' .github/workflows/" 3

echo "▸ Đóng gói"
kiem "Tag theo SHA"               "grep -rq 'github.sha' .github/workflows/" 5
kiem "Không deploy latest"        "! grep -rq 'tag:.*latest' ../cloudnote-config/ 2>/dev/null" 5

echo "▸ Helm"
kiem "Chart hợp lệ"               "helm lint ./helm/* 2>/dev/null | grep -q '0 chart(s) failed'" 5
kiem "Values theo môi trường"     "ls helm/*/values-*.yaml 2>/dev/null | grep -q ." 5

echo "▸ GitOps"
kiem "ArgoCD có Application"      "kubectl get application -n argocd | grep -qv NAME" 5
kiem "Trạng thái Synced"          "kubectl get application -n argocd -o jsonpath='{.items[0].status.sync.status}' | grep -q Synced" 5
kiem "Bật tự đồng bộ + selfHeal"  "kubectl get application -n argocd -o yaml | grep -q selfHeal" 5

echo "▸ Kubernetes"
kiem "Có readinessProbe"          "kubectl -n $NS get deploy -o yaml | grep -q readinessProbe" 5
kiem "Có livenessProbe"           "kubectl -n $NS get deploy -o yaml | grep -q livenessProbe" 4
kiem "Có HPA"                     "kubectl -n $NS get hpa | grep -qv NAME" 3
kiem "Nhiều bản cho app không trạng thái" "[ \$(kubectl -n $NS get deploy api -o jsonpath='{.spec.replicas}') -ge 2 ]" 3

echo "▸ Giám sát"
kiem "Prometheus đang chạy"       "kubectl get pods -A | grep -q prometheus" 5
kiem "Grafana đang chạy"          "kubectl get pods -A | grep -q grafana" 5
kiem "Loki đang chạy"             "kubectl get pods -A | grep -q loki" 5
kiem "Dashboard trong Git"        "ls **/dashboards/*.json 2>/dev/null | grep -q ." 5

echo "▸ Hạ tầng bằng code"
kiem "Terraform hợp lệ"           "terraform -chdir=terraform validate" 5
kiem "Không commit state"         "! git ls-files | grep -q tfstate" 5

echo "▸ Tài liệu"
kiem "README có sơ đồ"            "grep -qE 'mermaid|!\[' README.md" 5

echo ""
echo "  ĐIỂM (tự động): $diem / 92"
```

### ⚠️ Những cái bẫy hay gặp

| Bẫy | Hậu quả | Cách tránh |
|---|---|---|
| CI có kubeconfig của cluster | Lộ CI là lộ cluster | GitOps — CI chỉ ghi vào repo cấu hình |
| Gộp mã nguồn và cấu hình một repo | Lịch sử code ngập commit "đổi tag" | Tách hai repo |
| Dashboard bấm tay | Mất khi Grafana dựng lại | Provisioning từ file |
| Bật `selfHeal` khi chưa quen | Sửa tay bị hoàn tác, gây bực bội | Hiểu rõ trước khi bật (Ngày 43) |
| Alert ngưỡng CPU | Đánh thức người vô ích | Alert theo triệu chứng người dùng thấy |
| Không đo từng chặng | Không biết nghẽn ở đâu | Bảng thời gian ở phép thử lớn |

### 💬 Gợi ý khi bí

<details>
<summary><b>Monorepo hay nhiều repo? Tổ chức thế nào?</b></summary>

Cấu trúc dùng phổ biến — **hai repo**:

```text
cloudnote/                    ← repo mã nguồn (lập trình viên sửa)
├── app/{backend,frontend}/
├── helm/cloudnote/           ← chart (khuôn)
├── terraform/
├── .github/workflows/
└── docs/

cloudnote-config/             ← repo cấu hình (CI và người vận hành sửa)
└── ung-dung/
    ├── dev/values.yaml       ← tag image nằm ở đây
    └── prod/values.yaml
```

Vì sao tách: mỗi lần deploy là một commit vào repo cấu hình. Gộp chung thì lịch sử code ngập commit "cập nhật tag", và mỗi lần đổi cấu hình lại kích hoạt chạy lại toàn bộ CI một cách vô nghĩa.
</details>

<details>
<summary><b>Làm sao khép kín vòng mà không sửa tag bằng tay?</b></summary>

Thêm một job cuối vào workflow build image: clone repo cấu hình, sửa tag, commit ngược lại (xem chi tiết ở gợi ý Ngày 57). Cần một PAT có quyền ghi repo cấu hình, cất trong Secrets.

Sau đó ArgoCD thấy Git đổi và tự đồng bộ — **vòng khép kín hoàn toàn**: bạn chỉ push code, không chạm vào cluster, và mọi thay đổi đều có commit ghi lại.
</details>

<details>
<summary><b>Ba cảnh báo nào nên đặt cho hệ thống này?</b></summary>

1. **Dịch vụ không phản hồi** — `up == 0` hoặc probe thất bại, `for: 2m`
2. **Tỉ lệ lỗi 5xx vượt 5%** trong 5 phút
3. **Pod liên tục restart** — `rate(kube_pod_container_status_restarts_total[15m]) > 0`

Ba cái này bắt được phần lớn sự cố thật. Đừng đặt cảnh báo CPU/RAM trừ khi bạn có lý do cụ thể — chúng gây nhiễu nhiều hơn giúp ích. Ngày 51 sẽ cho bạn cách tốt hơn nữa: cảnh báo theo tốc độ đốt ngân sách lỗi.
</details>

### 🎯 Đúc kết Ngày 50 — Tổng kết Giai đoạn 3

**3 điều phải mang theo:**

1. **Giá trị nằm ở chỗ các công cụ nối vào nhau**, không ở từng công cụ riêng lẻ. Mỗi cái chỉ là một mắt xích; điều đáng học là **cách chúng ghép thành một vòng**.
2. **Không ai bên ngoài cần giữ chìa khoá cluster.** CI ghi vào Git, tác nhân trong cluster tự kéo về. Đây là khác biệt lớn nhất về bảo mật so với cách deploy ở Ngày 34.
3. **Vòng chỉ khép kín khi có giám sát.** Không có phần đo lường và cảnh báo, bạn chỉ có một dây chuyền đẩy code — không phải một hệ thống vận hành được.

> 🧠 **Một câu để nhớ:** hết Giai đoạn 3, thứ bạn xây không phải "một hệ thống chạy trên Kubernetes" — mà là **một vòng tự động: code đổi → hệ thống đổi → bạn nhìn thấy nó đổi**.

**✅ Tự chấm Milestone Giai đoạn 3:**

- [ ] Đạt từ 80 điểm
- [ ] Phép thử lớn: một vòng trọn vẹn dưới 10 phút, có bảng thời gian từng chặng
- [ ] Bốn phép thử phụ đều đạt
- [ ] Không hệ thống nào bên ngoài giữ kubeconfig của cluster
- [ ] README có sơ đồ toàn bộ vòng

✅ **Kết quả đạt được:** Một vòng DevOps khép kín và đo được — cũng chính là bộ khung bạn sẽ dùng lại cho dự án tốt nghiệp ở Ngày 56–59.

---

## Phụ lục A — Lỗi thường gặp (CI/CD · K8s · Monitoring)

| Lỗi kinh điển | Hậu quả | Cách làm đúng |
|---|---|---|
| Deploy bằng tag `latest` | Không biết đang chạy gì, rollback sai | Tag bất biến (SHA/semver) |
| Hard-code secret trong workflow YAML | Lộ secret vĩnh viễn | GitHub Secrets/Environments |
| Liveness probe quá gắt | CrashLoopBackOff (restart vô tận) | Readiness để ngừng traffic; liveness nới lỏng |
| Pod không có resource limits | 1 pod ngốn RAM giết cả node | Luôn đặt requests + limits |
| Tưởng K8s Secret là mã hóa | Lộ secret (chỉ base64) | RBAC + encryption-at-rest + Vault |
| Sửa tay trên cluster (`kubectl edit`) | Drift, mất đồng bộ với Git | Mọi thay đổi qua Git (GitOps) |
| HPA không scale | Quên cài Metrics Server | Cài metrics-server trước |
| Database dùng Deployment | Mất dữ liệu/danh tính | StatefulSet + PVC |
| Alert mọi dao động nhỏ | Alert fatigue → bỏ qua cả alert thật | Alert theo golden signals/SLO |
| NodePort/LoadBalancer cho mọi service | Tốn kém, khó quản | ClusterIP + Ingress |

## Phụ lục B — Playbook xử lý sự cố

**🔴 "Pod không lên / CrashLoopBackOff"**
```bash
kubectl get pods                       # trạng thái: Pending? CrashLoop? ImagePullBackOff?
kubectl describe pod <pod>             # Events ở cuối — lý do thật
kubectl logs <pod> --previous          # log của lần crash trước
# Pending → thiếu tài nguyên/không có node phù hợp
# ImagePullBackOff → sai tên image / thiếu credential registry
# CrashLoop → app lỗi khi khởi động hoặc liveness probe sai
```

**🔴 "Không truy cập được service"**
```bash
kubectl get svc,endpoints              # Service có endpoint không? (không = selector sai)
kubectl get pods --show-labels         # label pod khớp selector của Service?
kubectl port-forward svc/<name> 8080:80  # test trực tiếp, bỏ qua Ingress
kubectl describe ingress <name>        # Ingress route đúng chưa
```

**🔴 "Pipeline CI/CD fail"**
- Đọc log job — bước nào đỏ? (lint? test? build? deploy?)
- `ImagePullBackOff` khi deploy → registry credential / tag sai.
- Deploy SSH fail → kiểm tra Secret (key/host), quyền key.
- Build chậm/hết cache → kiểm tra cấu hình cache layer.

**🔴 "Metric/dashboard không có dữ liệu"**
- Prometheus: Status > Targets — target có UP không? (DOWN = scrape fail)
- App đã expose `/metrics` chưa? `curl pod:port/metrics`
- Grafana: data source Test có "working"? Time range đúng chưa?

**🔴 "ArgoCD OutOfSync / Degraded"**
- `OutOfSync` → có drift hoặc commit mới chưa sync → xem diff trong UI.
- `Degraded` → tài nguyên K8s lỗi (pod CrashLoop...) → đào vào pod.
- `Unknown` → ArgoCD không truy cập được repo/cluster.

## Phụ lục C — Cheat sheet

```text
# KUBECTL HÀNG NGÀY
kubectl get pods -A                    # mọi pod, mọi namespace
kubectl describe pod <p>               # điều tra (Events ở cuối)
kubectl logs -f <p> [--previous]       # log (lần crash trước)
kubectl exec -it <p> -- sh             # vào trong pod
kubectl apply -f . / -k ./overlay      # declarative apply
kubectl rollout undo deploy/<d>        # rollback
kubectl port-forward svc/<s> 8080:80   # test service nội bộ
kubectl get events --sort-by=.lastTimestamp

# HELM
helm install <name> <chart> -f values-prod.yaml
helm diff upgrade <name> <chart>       # xem trước (plugin)
helm rollback <name> <revision>

# CI/CD (GitHub Actions)
# - tag image theo SHA, KHÔNG latest
# - secret trong Secrets/Environments
# - CI mọi PR; CD khi merge main (production có approval)

# MONITORING (PromQL)
rate(http_requests_total[5m])          # request/s
histogram_quantile(0.95, rate(http_duration_bucket[5m]))  # p95
sum(rate(http_requests_total{status=~"5.."}[5m]))         # lỗi 5xx

# TERRAFORM (team)
terraform fmt && terraform validate
terraform plan -out=tfplan             # review trong CI/PR
# remote state + locking BẮT BUỘC khi làm nhóm

# BẢO MẬT (shift-left, chạy trong CI)
trivy image --severity CRITICAL --exit-code 1 <img>
tfsec ./infra ; gitleaks detect
```

> 💬 **Lời khuyên cuối Giai đoạn 3:** Bạn vừa lắp ráp toàn bộ "dây chuyền" DevOps hiện đại: code tự test → tự build → tự deploy → tự giám sát → tự phục hồi. Điểm mấu chốt không phải biết từng công cụ, mà hiểu **chúng ghép vào nhau như thế nào** để tạo một vòng đời khép kín. Giai đoạn 4 sẽ nâng tư duy lên mức **độ tin cậy** (SRE): không chỉ "chạy được" mà "chạy đáng tin ở quy mô lớn", tối ưu chi phí, và gói tất cả vào một dự án tốt nghiệp.

> ➡️ **Tiếp theo — Giai đoạn 4 (Ngày 51–60):** SRE, HA/DR, FinOps, Service Mesh & Dự án tốt nghiệp.
