#!/usr/bin/env bash
# Kiểm chứng máy đã được dựng đúng chuẩn
set -uo pipefail
MAY="${1:-may-web}"

echo "═══════════════════════════════════════════"
echo "  KIỂM TRA MÁY: $MAY"
echo "═══════════════════════════════════════════"

chay() { multipass exec "$MAY" -- bash -c "$1" 2>/dev/null; }

kiem() {
  local mo_ta="$1" lenh="$2" mong_doi="$3"
  local kq; kq=$(chay "$lenh")
  if echo "$kq" | grep -q "$mong_doi"; then
    echo "  ✅ $mo_ta"
  else
    echo "  ❌ $mo_ta  (nhận được: ${kq:-rỗng})"
  fi
}

echo ""
echo "▸ Người dùng và quyền"
kiem "User quantri tồn tại"        "id quantri"                    "quantri"
kiem "quantri có quyền sudo"       "groups quantri"                "sudo"
kiem "quantri thuộc nhóm docker"   "groups quantri"                "docker"

echo ""
echo "▸ Hardening SSH"
kiem "Cấm đăng nhập bằng root"     "sshd -T | grep permitrootlogin" "permitrootlogin no"
kiem "Cấm đăng nhập bằng mật khẩu" "sshd -T | grep passwordauth"    "passwordauthentication no"

echo ""
echo "▸ Tường lửa"
kiem "UFW đang bật"                "sudo ufw status | head -1"      "active"
kiem "Cổng 22 đã mở"               "sudo ufw status"                "22/tcp"
kiem "Cổng 80 đã mở"               "sudo ufw status"                "80/tcp"

echo ""
echo "▸ Dịch vụ"
kiem "fail2ban đang chạy"          "systemctl is-active fail2ban"   "active"
kiem "Docker đã cài"               "docker --version"               "Docker version"

echo ""
echo "▸ cloud-init"
kiem "cloud-init hoàn tất"         "cat /var/log/cloud-init-xong.txt" "20"
echo ""
