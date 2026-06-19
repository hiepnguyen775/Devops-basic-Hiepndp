"""Kết nối PostgreSQL + khởi tạo schema.

Cấu hình đọc từ BIẾN MÔI TRƯỜNG (không hard-code secret):
  - Ưu tiên DATABASE_URL (dùng ở docker-compose).
  - Nếu không có, ghép từ POSTGRES_HOST/USER/PASSWORD/DB (dùng ở Kubernetes).
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
    """Tạo 1 kết nối mới.
    TODO nâng cao: dùng connection pool (psycopg_pool / PgBouncer) thay vì mở kết nối mỗi request.
    """
    return psycopg2.connect(DATABASE_URL, cursor_factory=RealDictCursor)


def init_db():
    """Tạo bảng nếu chưa có (idempotent).
    Production thật nên dùng migration tool (Alembic/Flyway) thay vì CREATE TABLE IF NOT EXISTS.
    """
    with get_conn() as conn, conn.cursor() as cur:
        cur.execute(
            """
            CREATE TABLE IF NOT EXISTS notes (
                id          SERIAL PRIMARY KEY,
                title       VARCHAR(200) NOT NULL,
                content     TEXT NOT NULL DEFAULT '',
                created_at  TIMESTAMPTZ NOT NULL DEFAULT now()
            );
            """
        )
        conn.commit()
    log.info("Khởi tạo schema xong")


def check_db() -> bool:
    """Dùng cho readiness probe: DB có sẵn sàng nhận kết nối không?"""
    try:
        with get_conn() as conn, conn.cursor() as cur:
            cur.execute("SELECT 1;")
        return True
    except Exception as e:  # noqa: BLE001
        log.warning("DB chưa sẵn sàng: %s", e)
        return False
