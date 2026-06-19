"""CloudNote API — PHIÊN BẢN ĐẦY ĐỦ (đã giải hết TODO).

Tính năng:
  - Đăng ký / đăng nhập (JWT)
  - CRUD notes scope theo user (mỗi người chỉ thấy note của mình)
  - /metrics cho Prometheus
  - /health /ready cho K8s probe
"""
import time
import logging
from contextlib import asynccontextmanager

from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel, Field
from prometheus_fastapi_instrumentator import Instrumentator

from . import db, auth

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
log = logging.getLogger("cloudnote")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/login")


@asynccontextmanager
async def lifespan(app: FastAPI):
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
    version="1.0.0",
    docs_url="/api/docs",
    openapi_url="/api/openapi.json",
    lifespan=lifespan,
)

# /metrics tự sinh cho Prometheus
Instrumentator().instrument(app).expose(app, endpoint="/metrics", include_in_schema=False)


# ---------- Models ----------
class UserIn(BaseModel):
    username: str = Field(min_length=3, max_length=50)
    password: str = Field(min_length=6, max_length=128)


class NoteIn(BaseModel):
    title: str = Field(min_length=1, max_length=200)
    content: str = ""


# ---------- Dependency: lấy user hiện tại từ JWT ----------
def get_current_user(token: str = Depends(oauth2_scheme)) -> dict:
    username = auth.decode_token(token)
    if not username:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token không hợp lệ")
    user = db.get_user_by_username(username)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="User không tồn tại")
    return user


# ---------- Health / Ready ----------
@app.get("/health")
@app.get("/api/health")
def health():
    return {"status": "ok"}


@app.get("/ready")
@app.get("/api/ready")
def ready():
    if db.check_db():
        return {"status": "ready"}
    raise HTTPException(status_code=503, detail="database not ready")


# ---------- Auth ----------
@app.post("/api/register", status_code=201)
def register(user: UserIn):
    if db.get_user_by_username(user.username):
        raise HTTPException(status_code=409, detail="Username đã tồn tại")
    row = db.create_user(user.username, auth.hash_password(user.password))
    log.info("Đăng ký user=%s", row["username"])
    return {"id": row["id"], "username": row["username"]}


@app.post("/api/login")
def login(form: OAuth2PasswordRequestForm = Depends()):
    user = db.get_user_by_username(form.username)
    if not user or not auth.verify_password(form.password, user["password_hash"]):
        raise HTTPException(status_code=401, detail="Sai username hoặc mật khẩu")
    token = auth.create_access_token(user["username"])
    return {"access_token": token, "token_type": "bearer"}


# ---------- CRUD notes (yêu cầu đăng nhập) ----------
@app.get("/api/notes")
def list_notes(current=Depends(get_current_user)):
    return db.list_notes(current["id"])


@app.post("/api/notes", status_code=201)
def create_note(note: NoteIn, current=Depends(get_current_user)):
    return db.create_note(current["id"], note.title, note.content)


@app.put("/api/notes/{note_id}")
def update_note(note_id: int, note: NoteIn, current=Depends(get_current_user)):
    row = db.update_note(current["id"], note_id, note.title, note.content)
    if not row:
        raise HTTPException(status_code=404, detail="Không tìm thấy note")
    return row


@app.delete("/api/notes/{note_id}", status_code=204)
def delete_note(note_id: int, current=Depends(get_current_user)):
    if not db.delete_note(current["id"], note_id):
        raise HTTPException(status_code=404, detail="Không tìm thấy note")
    return None
