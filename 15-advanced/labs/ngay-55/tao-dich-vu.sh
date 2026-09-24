#!/usr/bin/env bash
# Bộ khởi tạo dịch vụ — golden path của tổ chức
set -euo pipefail

TEN="${1:-}"
CHU_SO_HUU="${2:-chua-ro}"

if [ -z "$TEN" ]; then
  echo "Dùng: $0 <ten-dich-vu> [doi-so-huu]"
  echo "Ví dụ: $0 dich-vu-thanh-toan doi-backend"
  exit 1
fi

if ! echo "$TEN" | grep -qE '^[a-z][a-z0-9-]{2,29}$'; then
  echo "❌ Tên phải viết thường, chỉ gồm chữ/số/gạch ngang, dài 3-30 ký tự."
  exit 1
fi

if [ -d "$TEN" ]; then
  echo "❌ Thư mục '$TEN' đã tồn tại."
  exit 1
fi

MAU="$(cd "$(dirname "$0")" && pwd)/mau"

echo "🚀 Đang tạo dịch vụ '$TEN' (chủ sở hữu: $CHU_SO_HUU)..."

mkdir -p "$TEN"/{src,test,.github/workflows}
cd "$TEN"

# ---- Mã nguồn khởi đầu ----
cat > app.js <<'EOF'
const http = require('node:http');
const PORT = process.env.PORT || 3000;

const server = http.createServer((req, res) => {
  if (req.url === '/health') {
    res.writeHead(200, { 'Content-Type': 'application/json' });
    return res.end(JSON.stringify({ trangThai: 'ok' }));
  }
  res.writeHead(200, { 'Content-Type': 'application/json' });
  res.end(JSON.stringify({ dichVu: process.env.TEN_DICH_VU || 'chua-dat-ten' }));
});

server.listen(PORT, () => console.log(`Đang nghe cổng ${PORT}`));
EOF

cat > test/app.test.js <<'EOF'
const test = require('node:test');
const assert = require('node:assert');

test('ví dụ: thay bằng test thật của bạn', () => {
  assert.strictEqual(1 + 1, 2);
});
EOF

cat > package.json <<EOF
{
  "name": "$TEN",
  "version": "0.1.0",
  "main": "app.js",
  "scripts": {
    "start": "node app.js",
    "test": "node --test test/"
  },
  "license": "UNLICENSED"
}
EOF

# ---- Golden path: copy khuôn đã chuẩn hoá ----
cp "$MAU/Dockerfile" .
cp "$MAU/Makefile" .
cp "$MAU/ci.yml" .github/workflows/ci.yml

printf 'node_modules/\n.env\ndist/\n' > .gitignore
printf 'node_modules\n.git\n.github\ntest\n*.md\n' > .dockerignore

# ---- Tài liệu sinh sẵn ----
cat > README.md <<EOF
# $TEN

> Chủ sở hữu: **$CHU_SO_HUU**
> Sinh bởi bộ khởi tạo dịch vụ (golden path)

## Bắt đầu nhanh

\`\`\`bash
make cai      # cài thư viện
make test     # chạy test
make chay     # build và chạy bằng Docker
make help     # xem tất cả lệnh
\`\`\`

## Dịch vụ đã có sẵn những gì

- ✅ Dockerfile nhiều tầng, chạy bằng user thường, có HEALTHCHECK
- ✅ CI: lint + test + quét bí mật
- ✅ Điểm kiểm tra sức khoẻ tại \`/health\`
- ✅ Makefile với bộ lệnh chuẩn dùng chung toàn tổ chức

## Điểm truy cập

| Đường dẫn | Mô tả |
|---|---|
| \`/\` | Thông tin dịch vụ |
| \`/health\` | Kiểm tra sức khoẻ (dùng cho probe) |
EOF

# ---- Siêu dữ liệu để quy trách nhiệm (Ngày 53) ----
cat > dich-vu.yaml <<EOF
ten: $TEN
chu_so_huu: $CHU_SO_HUU
tang: 3
kenh_lien_he: "#$CHU_SO_HUU"
slo:
  kha_dung: 99.5
  p95_do_tre_ms: 300
EOF

git init -q -b main
git add .
git commit -q -m "Khởi tạo $TEN từ golden path"

echo ""
echo "✅ Xong! Dịch vụ '$TEN' đã sẵn sàng."
echo ""
echo "   cd $TEN && make help"
echo ""
echo "Đã có sẵn: Dockerfile · CI · quét bảo mật · health check · README · Makefile"
