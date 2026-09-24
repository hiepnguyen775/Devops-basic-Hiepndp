#!/usr/bin/env python3
"""So sánh tài nguyên ĐẶT CHỖ với tài nguyên THỰC DÙNG, quy ra tiền."""

import json
import urllib.request
import urllib.parse
import pathlib

PROMETHEUS = "http://localhost:9090"
GIO_MOI_THANG = 730

gia = json.loads(pathlib.Path("bang-gia.json").read_text(encoding="utf-8"))["gia"]


def hoi_prometheus(truy_van):
    url = f"{PROMETHEUS}/api/v1/query?" + urllib.parse.urlencode({"query": truy_van})
    with urllib.request.urlopen(url, timeout=10) as r:
        return json.load(r)["data"]["result"]


def tien_moi_thang(cpu_core, ram_gb):
    return (cpu_core * gia["cpu_moi_core_moi_gio"]
            + ram_gb * gia["ram_moi_gb_moi_gio"]) * GIO_MOI_THANG


# ---- Thực dùng: lấy từ cAdvisor (Ngày 45) ----
cpu_thuc = {r["metric"].get("name", "?"): float(r["value"][1])
            for r in hoi_prometheus(
                'sum by (name) (rate(container_cpu_usage_seconds_total{name!=""}[5m]))')}

ram_thuc = {r["metric"].get("name", "?"): float(r["value"][1]) / (1024 ** 3)
            for r in hoi_prometheus(
                'sum by (name) (container_memory_working_set_bytes{name!=""})')}

# ---- Đặt chỗ: giả định mức người ta HAY xin cho một dịch vụ nhỏ ----
DAT_CHO_CPU = 1.0     # 1 core
DAT_CHO_RAM = 2.0     # 2 GB

print(f"{'Container':<22} {'CPU dùng':>10} {'RAM dùng':>10} "
      f"{'Tiền thực':>11} {'Tiền đặt chỗ':>13} {'Lãng phí':>10}")
print("-" * 82)

tong_thuc = tong_dat = 0.0
for ten in sorted(set(cpu_thuc) | set(ram_thuc)):
    c, m = cpu_thuc.get(ten, 0.0), ram_thuc.get(ten, 0.0)
    t_thuc = tien_moi_thang(c, m)
    t_dat = tien_moi_thang(DAT_CHO_CPU, DAT_CHO_RAM)
    tong_thuc += t_thuc
    tong_dat += t_dat
    print(f"{ten[:22]:<22} {c:>9.3f}c {m:>9.3f}G "
          f"${t_thuc:>10.2f} ${t_dat:>12.2f} ${t_dat - t_thuc:>9.2f}")

print("-" * 82)
print(f"{'TỔNG':<22} {'':>10} {'':>10} ${tong_thuc:>10.2f} ${tong_dat:>12.2f} "
      f"${tong_dat - tong_thuc:>9.2f}")

if tong_dat > 0:
    ty_le = (tong_dat - tong_thuc) / tong_dat * 100
    print(f"\n💸 Lãng phí: {ty_le:.1f}% ngân sách — ${tong_dat - tong_thuc:.2f}/tháng "
          f"(${(tong_dat - tong_thuc) * 12:.2f}/năm)")

# ---- Gợi ý mức đặt chỗ hợp lý ----
print("\n📐 Gợi ý điều chỉnh (thực dùng + 30% dự phòng):")
for ten in sorted(cpu_thuc):
    c = cpu_thuc.get(ten, 0.0) * 1.3
    m = ram_thuc.get(ten, 0.0) * 1.3
    print(f"  {ten[:22]:<22} requests: cpu={max(c, 0.01):.3f}  memory={max(m, 0.032):.3f}Gi")
