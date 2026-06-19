# Module bổ sung — Python cho DevOps

> **3 ngày** · Lấp khoảng trống quan trọng nhất so với roadmap chuẩn: roadmap.sh xếp **Python** là kỹ năng cốt lõi của DevOps (automation, cloud SDK, xử lý dữ liệu) — bên cạnh Bash.
>
> 🗓️ **Học khi nào?** Sau khi xong **Bash (Ngày 5–6)** hoặc song song Giai đoạn 2. Bash hợp cho lệnh hệ thống ngắn; Python hợp cho logic phức tạp, gọi API, xử lý JSON/YAML, SDK cloud.
>
> **Khuôn mỗi ngày:** 📘 Lý thuyết → 🧪 Lab cơ bản → 🚀 Lab nâng cao (best-practice) → 💡 Bổ sung thực tế → 📝 Bài ôn tập.
>
> 📚 Docs: [Python](https://docs.python.org/3/) · [Real Python](https://realpython.com/) · [boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html) · [requests](https://requests.readthedocs.io/) · [PyYAML](https://pyyaml.org/)

---

## Mục lục

| Ngày | Chủ đề |
|------|--------|
| [P1](#ngày-p1--python-cơ-bản-cho-automation) | Python cơ bản cho automation |
| [P2](#ngày-p2--xử-lý-dữ-liệu-jsonyaml--gọi-api) | Xử lý dữ liệu (JSON/YAML) & gọi API |
| [P3](#ngày-p3--tự-động-hóa-hệ-thống--cloud-sdk) | Tự động hóa hệ thống & Cloud SDK |

---

## Ngày P1 — Python cơ bản cho automation

> ⏱️ ~90 phút · Loại: Python

### 📘 Lý thuyết

- **Vì sao DevOps cần Python (ngoài Bash):** Bash tuyệt cho lệnh hệ thống ngắn, nhưng đuối khi logic phức tạp, xử lý JSON/API, hay code dài. Python dễ đọc, thư viện khổng lồ, là ngôn ngữ của hầu hết SDK cloud (boto3) và công cụ DevOps (Ansible viết bằng Python).
- **Cú pháp nền tảng:** biến (không khai báo kiểu), `print()`, thụt lề **bằng space** để định khối (như YAML — không có `{}`).
- **Kiểu dữ liệu:** `str`, `int`, `float`, `bool`, `list` (`[]`), `dict` (`{}`), `tuple`.
- **Điều kiện & vòng lặp:** `if/elif/else`, `for x in ...`, `while`.
- **Hàm:** `def ten(thamso):` ... `return`.
- **Đọc/ghi file:** `with open('file') as f:` (tự đóng file).
- **Tham số dòng lệnh:** `sys.argv`, hoặc `argparse` (chuẩn hơn).
- **Môi trường ảo (venv):** mỗi project 1 môi trường riêng để không xung đột thư viện.

### 🧪 Lab cơ bản

1. Cài Python 3 (`python3 --version`), tạo venv:
   ```bash
   python3 -m venv .venv && source .venv/bin/activate    # Windows: .venv\Scripts\activate
   ```
2. Viết `hello.py` in `Hello DevOps`, chạy `python3 hello.py`.
3. Viết script nhận tên qua `input()` và chào.
4. Viết script dùng `for` tạo 5 file `file1.txt`..`file5.txt`.
5. Viết script đọc 1 file text và đếm số dòng.

### 🚀 Lab nâng cao (best-practice)

> Mục tiêu: viết script Python "chạy thật được" — có venv, requirements, xử lý lỗi, CLI chuẩn.

1. **Luôn dùng venv + `requirements.txt`** (tái lập môi trường, không cài bừa vào hệ thống):
   ```bash
   pip install requests pyyaml
   pip freeze > requirements.txt        # ghi lại version chính xác
   # máy khác: pip install -r requirements.txt
   ```
2. **CLI chuẩn với `argparse`** thay vì `sys.argv` thô:
   ```python
   import argparse
   p = argparse.ArgumentParser(description="Kiểm tra sức khỏe dịch vụ")
   p.add_argument("--url", required=True)
   p.add_argument("--timeout", type=int, default=5)
   args = p.parse_args()
   print(args.url, args.timeout)
   ```
3. **Xử lý lỗi đúng cách** (`try/except`) + **logging** thay vì `print` bừa:
   ```python
   import logging
   logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
   try:
       risky()
   except Exception as e:
       logging.error("Thất bại: %s", e)
   ```
4. **Type hints** giúp đọc + bắt lỗi sớm: `def check(url: str, timeout: int = 5) -> bool:`.

### 💡 Bổ sung thực tế: Bash hay Python — chọn cái nào?

| Tình huống | Nên dùng |
|---|---|
| Gọi vài lệnh hệ thống, glue ngắn (< 20 dòng) | **Bash** |
| Logic phức tạp, vòng lặp lồng, nhiều điều kiện | **Python** |
| Xử lý JSON/YAML, gọi REST API | **Python** (Bash + jq cũng được nhưng đuối) |
| Tương tác cloud (AWS/GCP/Azure) qua SDK | **Python** (boto3...) |
| Script khởi động/cron đơn giản trên server | **Bash** |

- **Quy tắc:** Bash khi "dán lệnh lại với nhau"; Python khi "có logic thật sự". Nhiều DevOps senior: Bash cho < 50 dòng, vượt thì chuyển Python.
- **`with open(...)` luôn dùng** — tự đóng file kể cả khi lỗi (tránh rò rỉ file handle).
- **venv là bắt buộc** — cài thẳng `pip install` vào hệ thống gây xung đột version giữa các project (giống "dependency hell").

### 📝 Bài ôn tập & Demo đối chiếu

- **Bài ôn:** viết script nhận 1 số qua `argparse`, in "Chẵn"/"Lẻ".
- Khi nào chọn Python thay vì Bash?
- Vì sao nên dùng venv cho mỗi project?

| Demo đối chiếu | Kết quả mong đợi |
|---|---|
| `python3 hello.py` | In `Hello DevOps` |
| Kích hoạt venv | Prompt hiện `(.venv)` |
| `pip freeze` | Liệt kê thư viện đã cài kèm version |

✅ **Kết quả đạt được:** Viết được script Python cơ bản với cấu trúc chuẩn (venv, argparse, logging).

---

## Ngày P2 — Xử lý dữ liệu (JSON/YAML) & gọi API

> ⏱️ ~90 phút · Loại: Python

### 📘 Lý thuyết

- **JSON:** định dạng API trả về; Python xử lý bằng module `json` (`json.loads`, `json.dumps`).
- **YAML:** định dạng cấu hình DevOps (K8s, Compose, Ansible); xử lý bằng `pyyaml` (`yaml.safe_load`).
- **dict ↔ JSON/YAML:** đọc JSON/YAML thành `dict` Python để thao tác, rồi ghi ngược lại.
- **Gọi HTTP API:** thư viện `requests` (`requests.get/post`), đọc status code, `.json()`.
- **Xử lý lỗi mạng:** timeout, retry, kiểm tra status code (đừng giả định API luôn thành công).
- **Biến môi trường:** `os.environ` đọc config/secret (không hard-code).
- **f-string:** `f"User {name} có {count} note"` — cách format chuỗi hiện đại.

### 🧪 Lab cơ bản

1. Đọc 1 file JSON thành dict và in 1 trường:
   ```python
   import json
   data = json.load(open("config.json"))
   print(data["database"]["host"])
   ```
2. Đọc 1 file YAML (vd `docker-compose.yml`) bằng `yaml.safe_load` và in danh sách service.
3. Gọi API công khai và in kết quả:
   ```python
   import requests
   r = requests.get("https://api.github.com")
   print(r.status_code, r.json()["current_user_url"])
   ```
4. Đọc 1 biến môi trường bằng `os.environ.get("MY_VAR", "mặc định")`.
5. Chuyển 1 dict Python thành JSON đẹp: `json.dumps(d, indent=2)`.

### 🚀 Lab nâng cao (best-practice)

> Mục tiêu: gọi API và xử lý dữ liệu như script production — có timeout, retry, kiểm tra lỗi.

1. **Gọi API an toàn** (timeout + kiểm status, không treo vô hạn):
   ```python
   import requests
   try:
       r = requests.get(url, timeout=5)
       r.raise_for_status()             # ném lỗi nếu 4xx/5xx
       data = r.json()
   except requests.RequestException as e:
       logging.error("Gọi API lỗi: %s", e)
   ```
2. **Retry có backoff** cho API hay chập chờn (dùng `urllib3.Retry` / `tenacity`).
3. **`yaml.safe_load`** (KHÔNG dùng `yaml.load` thuần — lỗ hổng thực thi code tùy ý).
4. **Secret qua biến môi trường**, không hard-code token trong code:
   ```python
   token = os.environ["API_TOKEN"]      # ném lỗi rõ ràng nếu thiếu
   ```

### 💡 Bổ sung thực tế: đây là kỹ năng dùng HÀNG NGÀY của DevOps

- **Vì sao quan trọng:** gần như mọi công cụ DevOps trả JSON (`docker inspect`, `kubectl -o json`, `aws ... --output json`, mọi REST API). Biết parse JSON bằng Python = tự động hóa được rất nhiều việc mà Bash + jq làm vất vả.
- **`json` vs `jq`:** việc nhanh trên terminal → `jq` (Ngày 22). Logic phức tạp, nhiều bước, gọi nhiều API → Python `json` gọn hơn.
- **`raise_for_status()` là thói quen sống còn:** không có nó, script "chạy thành công" nhưng thực ra API trả 500 và bạn xử lý dữ liệu rác.
- **CẢNH BÁO `yaml.load`:** luôn dùng `yaml.safe_load`. `yaml.load` thuần có thể thực thi code tùy ý từ file YAML độc hại — lỗ hổng bảo mật thật.
- **Idempotent + dry-run:** script tự động hóa nên hỗ trợ `--dry-run` (in ra sẽ làm gì mà không làm thật) — giống `terraform plan`.

### 📝 Bài ôn tập & Demo đối chiếu

- **Bài ôn:** viết script gọi 1 API, nếu status ≠ 200 thì in cảnh báo.
- Phân biệt `json.loads` (chuỗi → dict) và `json.load` (file → dict).
- Vì sao phải dùng `yaml.safe_load` thay vì `yaml.load`?

| Demo đối chiếu | Kết quả mong đợi |
|---|---|
| Parse JSON từ file | In đúng trường lồng nhau |
| Gọi API có timeout | Trả status 200 + dữ liệu, hoặc báo lỗi gọn |
| Đọc YAML | Liệt kê đúng các service |

✅ **Kết quả đạt được:** Xử lý JSON/YAML và gọi API bằng Python — kỹ năng glue automation cốt lõi.

---

## Ngày P3 — Tự động hóa hệ thống & Cloud SDK

> ⏱️ ~90 phút · Loại: Python

### 📘 Lý thuyết

- **Gọi lệnh hệ thống từ Python:** `subprocess.run([...], capture_output=True, text=True)` — chạy lệnh shell, lấy output, kiểm tra exit code.
- **Thao tác file/thư mục:** module `os`, `pathlib`, `shutil`.
- **Cloud SDK:** `boto3` (AWS), `google-cloud-*` (GCP), `azure-sdk` (Azure) — quản lý tài nguyên cloud bằng code.
- **Lập lịch:** script Python chạy qua cron / systemd timer (Ngày 6).
- **Đóng gói script:** `requirements.txt`, có thể đóng vào Docker image để chạy ở bất kỳ đâu.
- **Logging + báo cáo:** ghi log có cấu trúc, gửi cảnh báo (Slack/email) khi bất thường.

### 🧪 Lab cơ bản

1. Gọi lệnh hệ thống và đọc output:
   ```python
   import subprocess
   r = subprocess.run(["df", "-h", "/"], capture_output=True, text=True)
   print(r.stdout)
   ```
2. Viết script kiểm tra dung lượng đĩa, in cảnh báo nếu > 85% (parse output `df`).
3. (Nếu có AWS) Cài `boto3`, liệt kê các S3 bucket:
   ```python
   import boto3
   for b in boto3.client("s3").list_buckets()["Buckets"]:
       print(b["Name"])
   ```
4. Dùng `pathlib` tìm tất cả file `.log` trong 1 thư mục.
5. Viết script gửi nội dung ra 1 webhook (Slack/Discord) bằng `requests.post`.

### 🚀 Lab nâng cao (best-practice)

> Mục tiêu: viết một công cụ tự động hóa hoàn chỉnh — như công cụ nội bộ thật.

1. **Script health-check production-grade** (kết hợp P1+P2+P3): kiểm tra đĩa/RAM/dịch vụ → ghi log → gửi cảnh báo webhook nếu vượt ngưỡng → hỗ trợ `--dry-run` và `argparse`.
2. **`subprocess` an toàn** — dùng list `["cmd", "arg"]` (KHÔNG `shell=True` với input từ ngoài → lỗ hổng command injection):
   ```python
   subprocess.run(["systemctl", "is-active", svc], check=True)   # check=True: lỗi → ném exception
   ```
3. **boto3 least privilege** — dùng IAM role/credential quyền tối thiểu, không hard-code access key (lấy từ `~/.aws/credentials` hoặc biến môi trường).
4. **Đóng script vào Docker image** để chạy nhất quán trong CI/cron/K8s CronJob.

### 💡 Bổ sung thực tế: Python là "keo dán" của toàn bộ DevOps

- **Đây là nơi mọi thứ kết nối:** Python gọi được shell (`subprocess`), API (`requests`), cloud (`boto3`), parse mọi định dạng (json/yaml) → là công cụ tự động hóa vạn năng khi Bash đuối.
- **CẢNH BÁO `shell=True`:** `subprocess.run(f"rm {user_input}", shell=True)` với input từ ngoài = lỗ hổng **command injection** nghiêm trọng. Luôn truyền list, không truyền chuỗi shell.
- **boto3 = chìa khóa automation AWS:** mọi việc trên AWS Console đều làm được bằng boto3 — tạo/xóa EC2, đọc CloudWatch, quản lý S3... Đây là cách viết công cụ vận hành cloud tự động.
- **Khi nào dùng Python vs Terraform/Ansible:** Terraform để **tạo hạ tầng** (khai báo), Ansible để **cấu hình** (khai báo). Python cho **logic động/glue** mà 2 cái kia không làm gọn (vd: "quét tất cả tài khoản, tìm volume mồ côi > 30 ngày, gửi báo cáo").
- **CronJob trong K8s** thường chính là 1 Docker image chạy script Python theo lịch — đóng gói script là kỹ năng thật.

### 📝 Bài ôn tập & Demo đối chiếu

- **Bài ôn:** viết script kiểm tra 1 dịch vụ systemd có chạy không, in trạng thái.
- Vì sao `shell=True` với input từ ngoài là nguy hiểm?
- Khi nào dùng Python thay vì Terraform/Ansible?

| Demo đối chiếu | Kết quả mong đợi |
|---|---|
| Gọi lệnh hệ thống | `subprocess` trả về output đúng |
| Script health-check | In CPU/RAM/Disk, cảnh báo khi vượt ngưỡng |
| (AWS) boto3 liệt kê tài nguyên | In danh sách bucket/instance |

✅ **Kết quả đạt được:** Tự động hóa hệ thống và cloud bằng Python — bổ trợ Bash, lấp đúng khoảng trống roadmap chuẩn.

---

> 🔗 **Sau module này:** quay lại lộ trình chính. Python sẽ phát huy mạnh ở **Giai đoạn 3** (script trong CI/CD pipeline, K8s CronJob) và **Giai đoạn 4** (công cụ tự động hóa SRE, FinOps scripts).
>
> 📚 Đào sâu: [Python docs](https://docs.python.org/3/) · [Real Python](https://realpython.com/) · [Automate the Boring Stuff (miễn phí)](https://automatetheboringstuff.com/) · [boto3 docs](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)
