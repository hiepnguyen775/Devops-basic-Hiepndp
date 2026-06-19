# ---- Stage 1: build — cài dependency vào venv riêng ----
FROM python:3.12-slim AS build
WORKDIR /app
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# ---- Stage 2: runtime — base nhỏ, chạy non-root ----
FROM python:3.12-slim
# Tạo user thường (không chạy root — best practice bảo mật)
RUN useradd -r -u 1001 appuser
# Chỉ copy venv đã build sang (image cuối nhẹ, không có toolchain build)
COPY --from=build /opt/venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH" \
    PYTHONUNBUFFERED=1
WORKDIR /app
COPY app/ ./app/
USER appuser
EXPOSE 8000
# HEALTHCHECK để Docker/orchestrator biết container có thực sự khỏe
HEALTHCHECK --interval=30s --timeout=3s --start-period=10s --retries=3 \
  CMD python -c "import urllib.request,sys; sys.exit(0 if urllib.request.urlopen('http://localhost:8000/health').status==200 else 1)"
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
