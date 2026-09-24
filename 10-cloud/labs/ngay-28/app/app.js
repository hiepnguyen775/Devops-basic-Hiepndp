const http = require('node:http');
const os = require('node:os');

const PORT = process.env.PORT || 3000;
const PHIEN_BAN = process.env.PHIEN_BAN || 'chua-ro';

const server = http.createServer((req, res) => {
  if (req.url === '/health') {
    res.writeHead(200, { 'Content-Type': 'application/json' });
    return res.end(JSON.stringify({ trangThai: 'ok' }));
  }
  res.writeHead(200, { 'Content-Type': 'application/json' });
  res.end(JSON.stringify({
    thongDiep: 'Ứng dụng đang chạy trên máy chủ',
    phienBan: PHIEN_BAN,
    may: os.hostname(),
    thoiGianChay: Math.round(process.uptime()) + 's',
  }, null, 2));
});

server.listen(PORT, () => console.log(`Đang nghe cổng ${PORT}, phiên bản ${PHIEN_BAN}`));
