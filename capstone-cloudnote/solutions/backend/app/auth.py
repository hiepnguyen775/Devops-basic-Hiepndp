"""Xác thực: hash mật khẩu (bcrypt) + tạo/giải mã JWT.

Nguyên tắc:
  - KHÔNG lưu mật khẩu plaintext — chỉ lưu hash (bcrypt tự sinh salt).
  - JWT có chữ ký (HS256) + hạn dùng (exp). Secret đọc từ biến môi trường.
"""
import os
from datetime import datetime, timedelta, timezone

from jose import jwt, JWTError
from passlib.context import CryptContext

# 🔐 Production: đặt JWT_SECRET qua Secret/biến môi trường, KHÔNG để default này.
SECRET_KEY = os.environ.get("JWT_SECRET", "doi-secret-nay-trong-production")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(plain: str, hashed: str) -> bool:
    return pwd_context.verify(plain, hashed)


def create_access_token(username: str) -> str:
    """Tạo JWT với subject = username và hạn dùng."""
    expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    payload = {"sub": username, "exp": expire}
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)


def decode_token(token: str) -> str | None:
    """Trả về username nếu token hợp lệ, None nếu sai/hết hạn."""
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload.get("sub")
    except JWTError:
        return None
