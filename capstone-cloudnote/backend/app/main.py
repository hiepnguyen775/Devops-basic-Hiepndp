"""CloudNote API — FastAPI.

Endpoint:
  GET    /health      | /api/health   -> liveness (app còn sống?)
  GET    /ready       | /api/ready    -> readiness (DB sẵn sàng?)
  GET    /api/notes                   -> liệt kê note
  POST   /api/notes                   -> tạo note
  DELETE /api/notes/{id}              -> TODO (bạn tự làm)

Swagger UI: /api/docs  (truy cập local: http://localhost:8080/api/docs)

Lưu ý routing:
  - /health & /ready để ở ROOT cho Kubernetes probe gọi thẳng vào pod (cổng 8000).
  - Bản /api/* để truy cập qua nginx/Ingress (vì nginx chuyển tiếp /api → backend).
"""
import time
import logging
from contextlib import asynccontextmanager

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

from . import db

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
log = logging.getLogger("cloudnote")


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Khi khởi động: tạo schema. Retry vì DB có thể lên chậm hơn app.
    for attempt in range(1, 11):
        try:
            db.init_db()
            break
        except Exception as e:  # noqa: BLE001
            log.warning("Chờ DB (%d/10): %s", attempt, e)
            time.sleep(3)
    yield


app = FastAPI(
    title="CloudNote API",
    version="0.1.0",
    docs_url="/api/docs",
    openapi_url="/api/openapi.json",
    lifespan=lifespan,
)


class NoteIn(BaseModel):
    title: str = Field(min_length=1, max_length=200)
    content: str = ""


# ---------- Health / Readiness ----------
@app.get("/health")
@app.get("/api/health")
def health():
    """Liveness: tiến trình còn chạy là ok."""
    return {"status": "ok"}


@app.get("/ready")
@app.get("/api/ready")
def ready():
    """Readiness: chỉ sẵn sàng khi kết nối được DB."""
    if db.check_db():
        return {"status": "ready"}
    raise HTTPException(status_code=503, detail="database not ready")


# ---------- CRUD notes ----------
@app.get("/api/notes")
def list_notes():
    with db.get_conn() as conn, conn.cursor() as cur:
        cur.execute("SELECT id, title, content, created_at FROM notes ORDER BY id DESC;")
        return cur.fetchall()


@app.post("/api/notes", status_code=201)
def create_note(note: NoteIn):
    with db.get_conn() as conn, conn.cursor() as cur:
        cur.execute(
            "INSERT INTO notes (title, content) VALUES (%s, %s) "
            "RETURNING id, title, content, created_at;",
            (note.title, note.content),
        )
        row = cur.fetchone()
        conn.commit()
    log.info("Tạo note id=%s", row["id"])
    return row


# ============================================================
# 📝 TODO — bài tập cho bạn (học bằng cách làm):
#   1. DELETE /api/notes/{id}  -> xóa note theo id; trả 404 nếu không tồn tại.
#        gợi ý: cur.execute("DELETE FROM notes WHERE id=%s RETURNING id;", (id,))
#   2. PUT /api/notes/{id}     -> cập nhật title/content.
#   3. GET  /metrics           -> expose metric cho Prometheus
#        gợi ý: pip install prometheus-fastapi-instrumentator
#   4. (Nâng cao) Đăng nhập user bằng JWT -> note gắn với user_id (thêm bảng users).
# ============================================================
