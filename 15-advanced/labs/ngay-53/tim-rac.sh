#!/usr/bin/env bash
# Tìm tài nguyên mồ côi — thứ vẫn tính tiền mà không ai dùng
set -uo pipefail

echo "════════════════════════════════════════════════════"
echo "  TÌM TÀI NGUYÊN MỒ CÔI"
echo "════════════════════════════════════════════════════"

echo ""
echo "▸ Volume không gắn với container nào:"
docker volume ls -qf dangling=true | while read -r v; do
  kich_thuoc=$(docker run --rm -v "$v":/v alpine:3.21 du -sh /v 2>/dev/null | cut -f1)
  echo "   - $v  (${kich_thuoc:-?})"
done
SO_VOL=$(docker volume ls -qf dangling=true | wc -l)
echo "   => $SO_VOL volume mồ côi"

echo ""
echo "▸ Image không được container nào dùng:"
docker images -qf dangling=true | wc -l | xargs echo "   =>" "image lơ lửng"
echo "   Tổng dung lượng có thể thu hồi:"
docker system df --format "   {{.Type}}: {{.Reclaimable}}" 2>/dev/null

echo ""
echo "▸ Container đã dừng (vẫn chiếm đĩa):"
docker ps -aq --filter "status=exited" | wc -l | xargs echo "   =>" "container đã thoát"

echo ""
echo "▸ Container KHÔNG có nhãn chủ sở hữu (không quy được trách nhiệm chi phí):"
docker ps --format '{{.Names}}' | while read -r c; do
  nhan=$(docker inspect "$c" --format '{{index .Config.Labels "chu_so_huu"}}' 2>/dev/null)
  [ -z "$nhan" ] || [ "$nhan" = "<no value>" ] && echo "   - $c"
done

echo ""
echo "════════════════════════════════════════════════════"
echo "Dọn dẹp (XEM KỸ danh sách trên trước khi chạy):"
echo "  docker system prune -af --volumes"
echo "════════════════════════════════════════════════════"
