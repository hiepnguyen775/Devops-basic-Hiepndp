terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 3.0"
    }
  }
}

resource "docker_image" "nginx" {
  name         = "nginx:1.27-alpine"
  keep_locally = true          # giữ image lại khi destroy, đỡ phải tải lại
}

resource "docker_container" "ung_dung" {
  count = var.so_ban           # tạo ra đúng số bản sao yêu cầu

  name  = "${var.moi_truong}-${var.ten}-${count.index + 1}"
  image = docker_image.nginx.image_id

  ports {
    internal = 80
    external = var.cong_bat_dau + count.index
  }

  networks_advanced {
    name = var.id_mang
  }

  # Ghi thông tin nhận diện vào trang chủ
  command = [
    "/bin/sh", "-c",
    "echo '<h1>${var.ten} - bản ${count.index + 1} - môi trường ${var.moi_truong}</h1>' > /usr/share/nginx/html/index.html && nginx -g 'daemon off;'"
  ]

  labels {
    label = "moi_truong"
    value = var.moi_truong
  }

  labels {
    label = "quan_ly_boi"
    value = "terraform"
  }
}
