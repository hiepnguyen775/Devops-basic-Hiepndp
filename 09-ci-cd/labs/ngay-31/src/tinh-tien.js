// Tính tiền đơn hàng: cộng tiền các món rồi áp mã giảm giá (nếu có).
function tinhTien(cacMon, phanTramGiam = 0) {
  if (!Array.isArray(cacMon)) {
    throw new Error('cacMon phải là một mảng');
  }
  const tongTho = cacMon.reduce((tong, mon) => tong + mon.gia * mon.soLuong, 0);
  return Math.round(tongTho * (1 - phanTramGiam / 100));
}

module.exports = { tinhTien };
