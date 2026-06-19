# 📐 CloudNote — Kiến trúc chi tiết & Quyết định thiết kế

Tài liệu này mô tả kiến trúc, luồng dữ liệu, và các quyết định thiết kế (ADR) của CloudNote. Vẽ lại các sơ đồ này vào portfolio/CV của bạn.

---

## 1. Sơ đồ thành phần (Component diagram)

```mermaid
flowchart TB
    User(("👤 Người dùng")) -->|"HTTP(S)"| ENTRY
    subgraph ENTRY["Điểm vào"]
        direction LR
        IngOrProxy["🚪 Ingress (K8s)<br/>hoặc nginx (local)"]
    end
    IngOrProxy -->|"/"| FE["🖼️ Frontend<br/>HTML/JS + nginx"]
    IngOrProxy -->|"/api/*"| BE["⚙️ Backend API<br/>FastAPI (Python)"]
    BE -->|"SQL :5432"| DB[("🗄️ PostgreSQL")]
    BE -.->|"đọc cấu hình"| CM["⚙️ ConfigMap / .env"]
    BE -.->|"đọc mật khẩu DB"| SEC["🔐 Secret"]
    classDef pub fill:#e3f2fd,stroke:#1976d2;
    classDef app fill:#e8f5e9,stroke:#2e7d32;
    classDef data fill:#fff3e0,stroke:#f57c00;
    class IngOrProxy,FE pub;
    class BE app;
    class DB data;
```

## 2. Luồng một request "tạo note" (Sequence)

```mermaid
sequenceDiagram
    actor U as 👤 Người dùng
    participant F as 🖼️ Frontend (nginx)
    participant B as ⚙️ Backend (FastAPI)
    participant D as 🗄️ PostgreSQL
    U->>F: Mở web, nhập note, bấm "Lưu"
    F->>B: POST /api/notes {title, content}
    B->>B: Validate dữ liệu (TODO: kiểm tra rỗng)
    B->>D: INSERT INTO notes (...)
    D-->>B: trả về id + created_at
    B-->>F: 201 Created {note}
    F-->>U: Hiển thị note mới trong danh sách
    Note over B,D: /ready kiểm tra kết nối DB trước khi nhận traffic
```

## 3. Luồng CI/CD (từ commit đến production)

```mermaid
flowchart LR
    C(("commit")) --> PR{"Pull Request?"}
    PR -->|"có"| CI["🧪 CI: lint + test + Trivy scan"]
    CI -->|"fail ❌"| Block["chặn merge"]
    CI -->|"pass ✅"| Merge["merge vào main"]
    Merge --> Build["🏗️ build image (tag = git SHA)"]
    Build --> Push["📦 push → GHCR"]
    Push --> Deploy["🚀 kubectl/helm apply"]
    Deploy --> Health{"health check?"}
    Health -->|"ok ✅"| Live(("🌍 Live"))
    Health -->|"fail ❌"| RB["↩️ rollback"]
    classDef ci fill:#e3f2fd,stroke:#1976d2;
    class CI,Build,Push,Deploy ci;
```

## 4. Topology trên Kubernetes

```mermaid
flowchart TB
    Net(("🌐 Internet")) --> ING["🚪 Ingress · cloudnote.local"]
    ING -->|"path: /"| FSVC["Service: frontend (ClusterIP)"]
    ING -->|"path: /api"| BSVC["Service: backend (ClusterIP)"]
    FSVC --> FP1["Pod frontend"]
    FSVC --> FP2["Pod frontend"]
    BSVC --> BP1["Pod backend"]
    BSVC --> BP2["Pod backend (HPA 2→5)"]
    BP1 -->|"db-svc"| DSVC["Service: db (headless)"]
    BP2 --> DSVC
    DSVC --> DB[("Pod postgres-0<br/>StatefulSet + PVC")]
    subgraph NS["Namespace: cloudnote"]
        ING
        FSVC
        BSVC
        DSVC
        FP1
        FP2
        BP1
        BP2
        DB
    end
    classDef svc fill:#e3f2fd,stroke:#1976d2;
    classDef data fill:#fff3e0,stroke:#f57c00;
    class FSVC,BSVC,DSVC svc;
    class DB data;
```

## 5. Mô hình dữ liệu (ERD đơn giản)

```mermaid
erDiagram
    NOTES {
        int id PK
        string title
        text content
        timestamp created_at
    }
    USERS ||--o{ NOTES : "sở hữu (TODO nâng cao)"
    USERS {
        int id PK
        string username
        string password_hash
    }
```

> Bộ khung khởi đầu chỉ có bảng `notes`. Bảng `users` + quan hệ là **thử thách nâng cao** (thêm đăng nhập đa người dùng).

---

## 6. Quyết định thiết kế (ADR — Architecture Decision Records)

> ADR ghi lại "vì sao chọn cái này" — câu hỏi phỏng vấn kinh điển. Mỗi quyết định: bối cảnh → lựa chọn → lý do → đánh đổi.

### ADR-001: FastAPI cho backend
- **Bối cảnh:** cần REST API nhẹ, dễ học, gắn với module Python.
- **Quyết định:** FastAPI.
- **Lý do:** nhanh, tự sinh docs (`/docs`), type hint sẵn, cộng đồng lớn.
- **Đánh đổi:** nếu team quen Node/Go thì có thể chọn Express/Gin — kiến trúc không đổi.

### ADR-002: PostgreSQL thay vì NoSQL
- **Lý do:** dữ liệu note có cấu trúc + quan hệ (user→note), cần ACID. Postgres là mặc định an toàn.
- **Đánh đổi:** nếu cần cache/session tốc độ cao → thêm Redis (không thay Postgres).

### ADR-003: nginx frontend kiêm reverse proxy `/api` (ở local)
- **Lý do:** tránh lỗi CORS, 1 origin duy nhất; ở K8s thì Ingress đảm nhiệm routing.
- **Đánh đổi:** local và K8s định tuyến hơi khác nhau — đã tách rõ trong tài liệu.

### ADR-004: Kubernetes thay vì chỉ Docker Compose ở production
- **Lý do:** cần self-healing, auto-scale (HPA), rolling update không downtime — Compose không có.
- **Đánh đổi:** phức tạp hơn; với app nhỏ/nội bộ thì Compose + 1 VM là đủ (đừng over-engineer).

### ADR-005: Backend Postgres dùng StatefulSet + PVC
- **Lý do:** database là stateful, cần danh tính + storage ổn định; Deployment sẽ mất dữ liệu.
- **Đánh đổi:** vận hành DB trên K8s khó hơn managed DB (RDS/Cloud SQL) — cân nhắc cho production thật.

### ADR-006: Tag image theo git SHA, không dùng `latest`
- **Lý do:** truy vết chính xác phiên bản đang chạy, rollback đúng.
- **Đánh đổi:** không có, đây là best practice nên theo.

---

## 7. Bảo mật (Security checklist)

- [ ] Mật khẩu DB qua **Secret/biến môi trường**, không hard-code.
- [ ] Image quét **Trivy** trong CI, chặn nếu có lỗ hổng nghiêm trọng.
- [ ] Container chạy **non-root** (`USER` trong Dockerfile).
- [ ] Backend dùng **least privilege** với DB (user riêng, không superuser).
- [ ] DB **không expose** ra ngoài (chỉ network nội bộ / ClusterIP).
- [ ] (Nâng cao) NetworkPolicy: chỉ backend được nói chuyện với DB.
- [ ] `.env` và Secret thật nằm trong `.gitignore`, không commit.

## 8. Độ tin cậy (Reliability)

- **Liveness probe** `/health` — pod treo → K8s restart.
- **Readiness probe** `/ready` — chỉ nhận traffic khi DB sẵn sàng.
- **Resource requests/limits** — tránh 1 pod ngốn hết tài nguyên node.
- **HPA** — backend tự scale 2→5 theo CPU.
- **SLO gợi ý:** 99% request < 300ms, uptime 99.5% → error budget ~3.6h/tháng.
