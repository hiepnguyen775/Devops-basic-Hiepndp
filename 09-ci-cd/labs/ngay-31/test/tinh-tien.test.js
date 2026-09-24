const test = require('node:test');
const assert = require('node:assert');
const { tinhTien } = require('../src/tinh-tien');

test('cộng đúng tiền nhiều món', () => {
  const gioHang = [
    { gia: 20000, soLuong: 2 },
    { gia: 15000, soLuong: 1 },
  ];
  assert.strictEqual(tinhTien(gioHang), 55000);
});

test('áp dụng giảm giá 10%', () => {
  const gioHang = [{ gia: 100000, soLuong: 1 }];
  assert.strictEqual(tinhTien(gioHang, 10), 90000);
});

test('giỏ rỗng thì trả 0', () => {
  assert.strictEqual(tinhTien([]), 0);
});

test('truyền sai kiểu thì báo lỗi', () => {
  assert.throws(() => tinhTien('không phải mảng'));
});
