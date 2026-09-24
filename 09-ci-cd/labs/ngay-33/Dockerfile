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
