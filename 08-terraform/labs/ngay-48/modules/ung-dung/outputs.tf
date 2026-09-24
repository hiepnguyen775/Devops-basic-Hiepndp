output "ten_cac_container" {
  description = "Danh sách tên container đã tạo"
  value       = docker_container.ung_dung[*].name
}

output "cac_cong" {
  description = "Danh sách cổng truy cập"
  value       = [for c in docker_container.ung_dung : c.ports[0].external]
}
