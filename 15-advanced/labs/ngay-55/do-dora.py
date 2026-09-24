#!/usr/bin/env python3
"""Ước lượng 4 chỉ số DORA từ lịch sử Git của một repo."""

import subprocess
import sys
import datetime
import statistics

REPO = sys.argv[1] if len(sys.argv) > 1 else "."
SO_NGAY = int(sys.argv[2]) if len(sys.argv) > 2 else 90


def git(*args):
    r = subprocess.run(["git", "-C", REPO, *args],
                       capture_output=True, text=True)
    return r.stdout.strip()


tu_ngay = (datetime.date.today() - datetime.timedelta(days=SO_NGAY)).isoformat()

# --- 1. Tần suất triển khai: đếm commit vào main (xấp xỉ số lần deploy) ---
commits = [l for l in git("log", "--oneline", f"--since={tu_ngay}", "main").split("\n") if l]
so_lan = len(commits)
moi_tuan = so_lan / (SO_NGAY / 7) if SO_NGAY else 0

# --- 2. Thời gian từ commit tới main: đo qua khoảng cách giữa các commit ---
raw = git("log", f"--since={tu_ngay}", "--format=%ct", "main")
moc = sorted(int(x) for x in raw.split("\n") if x.strip())
khoang = [(b - a) / 3600 for a, b in zip(moc, moc[1:])] if len(moc) > 1 else []
trung_vi_gio = statistics.median(khoang) if khoang else 0

# --- 3. Tỉ lệ thay đổi gây lỗi: đếm commit sửa lỗi / revert ---
tu_khoa = ["fix", "sửa", "hotfix", "revert", "khắc phục", "bug"]
loi = [c for c in commits if any(k in c.lower() for k in tu_khoa)]
ty_le_loi = len(loi) / so_lan * 100 if so_lan else 0

print("═" * 58)
print(f"  CHỈ SỐ DORA — {SO_NGAY} ngày gần nhất")
print("═" * 58)


def xep_hang(ten, gia_tri, don_vi, moc_tot, moc_kha, nho_hon_tot=False):
    if nho_hon_tot:
        hang = "🟢 Dẫn đầu" if gia_tri <= moc_tot else ("🟡 Khá" if gia_tri <= moc_kha else "🔴 Cần cải thiện")
    else:
        hang = "🟢 Dẫn đầu" if gia_tri >= moc_tot else ("🟡 Khá" if gia_tri >= moc_kha else "🔴 Cần cải thiện")
    print(f"\n{ten}")
    print(f"  Giá trị: {gia_tri:.1f} {don_vi}")
    print(f"  Xếp hạng: {hang}")


xep_hang("1. Tần suất triển khai", moi_tuan, "lần/tuần", 7, 1)
xep_hang("2. Khoảng cách giữa các thay đổi", trung_vi_gio, "giờ (trung vị)", 24, 168, nho_hon_tot=True)
xep_hang("3. Tỉ lệ thay đổi gây lỗi (ước lượng)", ty_le_loi, "%", 5, 15, nho_hon_tot=True)

print("\n4. Thời gian khôi phục")
print("  Không suy ra được từ Git — cần dữ liệu sự cố")
print("  (lấy từ hệ thống cảnh báo, hoặc thống kê postmortem — Ngày 51)")

print("\n" + "═" * 58)
print(f"Tổng: {so_lan} thay đổi, trong đó {len(loi)} là sửa lỗi")
print("\n📌 Lưu ý: đây là ƯỚC LƯỢNG từ Git. Số liệu chính xác cần lấy")
print("   từ hệ thống CI/CD (thời điểm deploy) và hệ thống sự cố.")
