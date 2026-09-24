output "moi_truong_dang_dung" {
  value = terraform.workspace
}

output "container_web" {
  value = module.web.ten_cac_container
}

output "container_api" {
  value = module.api.ten_cac_container
}

output "duong_dan_truy_cap" {
  value = [for p in concat(module.web.cac_cong, module.api.cac_cong) : "http://localhost:${p}"]
}
