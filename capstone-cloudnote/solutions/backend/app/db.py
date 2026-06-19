"""Truy cập DB — phiên bản đầy đủ: bảng users + notes (gắn user_id).

Đặt các hàm truy cập dữ liệu ở đây để main.py gọn (tách tầng).
"""
import os
import logging
import psycopg2
from psycopg2.extras import RealDictCursor

log = logging.getLogger("cloudnote.db")

DATABASE_URL = os.environ.get("DATABASE_URL")
if not DATABASE_URL:
    host = os.environ.get("POSTGRES_HOST", "db")
    user = os.environ.get("POSTGRES_USER", "cloudnote")
    pwd = os.environ.get("POSTGRES_PASSWORD", "change_me_please_123")
    name = os.environ.get("POSTGRES_DB", "cloudnote")
    DATABASE_URL = f"postgresql://{user}:{pwd}@{host}:5432/{name}"


def get_conn():
    return psycopg2.connect(DATABASE_URL, cursor_factory=RealDictCursor)


def init_db():
    """Tạo bảng users + notes (idempotent). Production: dùng migration tool."""
    with get_conn() as conn, conn.cursor() as cur:
        cur.execute(
            """
            CREATE TABLE IF NOT EXISTS users (
                id            SERIAL PRIMARY KEY,
                username      VARCHAR(50) UNIQUE NOT NULL,
                password_hash TEXT NOT NULL,
                created_at    TIMESTAMPTZ NOT NULL DEFAULT now()
            );
            CREATE TABLE IF NOT EXISTS notes (
                id          SERIAL PRIMARY KEY,
                title       VARCHAR(200) NOT NULL,
                content     TEXT NOT NULL DEFAULT '',
                user_id     INTEGER REFERENCES users(id) ON DELETE CASCADE,
                created_at  TIMESTAMPTZ NOT NULL DEFAULT now()
            );
            """
        )
        conn.commit()
    log.info("Khởi tạo schema (users + notes) xong")


def check_db() -> bool:
    try:
        with get_conn() as conn, conn.cursor() as cur:
            cur.execute("SELECT 1;")
        return True
    except Exception as e:  # noqa: BLE001
        log.warning("DB chưa sẵn sàng: %s", e)
        return False


# ---------- Users ----------
def create_user(username: str, password_hash: str):
    with get_conn() as conn, conn.cursor() as cur:
        cur.execute(
            "INSERT INTO users (username, password_hash) VALUES (%s, %s) RETURNING id, username;",
            (username, password_hash),
        )
        row = cur.fetchone()
        conn.commit()
        return row


def get_user_by_username(username: str):
    with get_conn() as conn, conn.cursor() as cur:
        cur.execute("SELECT id, username, password_hash FROM users WHERE username=%s;", (username,))
        return cur.fetchone()


# ---------- Notes (luôn scope theo user_id) ----------
def list_notes(user_id: int):
    with get_conn() as conn, conn.cursor() as cur:
        cur.execute(
            "SELECT id, title, content, created_at FROM notes WHERE user_id=%s ORDER BY id DESC;",
            (user_id,),
        )
        return cur.fetchall()


def create_note(user_id: int, title: str, content: str):
    with get_conn() as conn, conn.cursor() as cur:
        cur.execute(
            "INSERT INTO notes (title, content, user_id) VALUES (%s, %s, %s) "
            "RETURNING id, title, content, created_at;",
            (title, content, user_id),
        )
        row = cur.fetchone()
        conn.commit()
        return row


def update_note(user_id: int, note_id: int, title: str, content: str):
    """Chỉ cập nhật note CỦA user đó (tránh sửa note người khác)."""
    with get_conn() as conn, conn.cursor() as cur:
        cur.execute(
            "UPDATE notes SET title=%s, content=%s WHERE id=%s AND user_id=%s "
            "RETURNING id, title, content, created_at;",
            (title, content, note_id, user_id),
        )
        row = cur.fetchone()
        conn.commit()
        return row  # None nếu không tồn tại / không thuộc user


def delete_note(user_id: int, note_id: int) -> bool:
    with get_conn() as conn, conn.cursor() as cur:
        cur.execute("DELETE FROM notes WHERE id=%s AND user_id=%s RETURNING id;", (note_id, user_id))
        row = cur.fetchone()
        conn.commit()
        return row is not None
