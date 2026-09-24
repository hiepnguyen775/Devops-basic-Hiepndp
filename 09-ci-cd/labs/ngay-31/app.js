const http = require('node:http');
const { tinhTien } = require('./src/tinh-tien');

const PORT = process.env.PORT || 3000;

const server = http.createServer((req, res) => {
  if (req.url === '/health') {
    res.writeHead(200, { 'Content-Type': 'application/json' });
    return res.end(JSON.stringify({ trangThai: 'ok' }));
  }
  const demo = tinhTien([{ gia: 20000, soLuong: 2 }], 10);
  res.writeHead(200, { 'Content-Type': 'application/json' });
  res.end(JSON.stringify({ thongDiep: 'ci-demo đang chạy', donHangMau: demo }));
});

server.listen(PORT, () => console.log(`Đang nghe ở cổng ${PORT}`));
