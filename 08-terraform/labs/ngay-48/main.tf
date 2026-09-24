terraform {
  required_version = ">= 1.5"
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 3.0"
    }
  }
}

provider "docker" {}

locals {
  moi_truong = terraform.workspace        # tên workspace chính là tên môi trường

  # Quy mô khác nhau theo môi trường
  quy_mo = {
    dev  = { web = 1, api = 1 }
    prod = { web = 3, api = 2 }
  }

  cau_hinh = lookup(local.quy_mo, local.moi_truong, local.quy_mo["dev"])
}

resource "docker_network" "mang" {
  name = "mang-${local.moi_truong}"
}

module "web" {
  source       = "./modules/ung-dung"
  ten          = "web"
  so_ban       = local.cau_hinh.web
  cong_bat_dau = local.moi_truong == "prod" ? 8100 : 8000
  moi_truong   = local.moi_truong
  id_mang      = docker_network.mang.id
}

module "api" {
  source       = "./modules/ung-dung"       # CÙNG module, khác tham số
  ten          = "api"
  so_ban       = local.cau_hinh.api
  cong_bat_dau = local.moi_truong == "prod" ? 8150 : 8050
  moi_truong   = local.moi_truong
  id_mang      = docker_network.mang.id
}
