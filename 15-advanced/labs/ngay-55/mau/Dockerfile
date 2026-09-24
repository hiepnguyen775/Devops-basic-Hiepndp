# Golden path: đã áp dụng mọi bài học từ Ngày 18, 33, 49
FROM node:20-alpine AS deps
WORKDIR /app
COPY package.json package-lock.json* ./
RUN npm ci --omit=dev 2>/dev/null || npm install --omit=dev

FROM node:20-alpine
WORKDIR /app
ENV NODE_ENV=production

RUN addgroup -S nhom && adduser -S ungdung -G nhom

COPY --from=deps /app/node_modules ./node_modules
COPY --chown=ungdung:nhom . .

USER ungdung
EXPOSE 3000

HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
  CMD wget -qO- http://127.0.0.1:3000/health || exit 1

CMD ["node", "app.js"]
