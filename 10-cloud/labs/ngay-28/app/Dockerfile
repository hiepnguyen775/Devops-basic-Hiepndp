FROM node:20-alpine
WORKDIR /app

ENV NODE_ENV=production

RUN addgroup -S nhom && adduser -S ungdung -G nhom

COPY package.json ./
COPY app.js ./

USER ungdung
EXPOSE 3000

HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
  CMD wget -qO- http://127.0.0.1:3000/health || exit 1

CMD ["node", "app.js"]
