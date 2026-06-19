variable "project" {
  type    = string
  default = "cloudnote"
}

variable "environment" {
  type    = string
  default = "dev"
}

variable "region" {
  type    = string
  default = "ap-southeast-1" # Singapore — đổi theo nhu cầu
}

variable "instance_type" {
  type    = string
  default = "t3.micro" # free-tier-ish; right-size theo tải thật
}

variable "ami_id" {
  type        = string
  description = "AMI Ubuntu 22.04/24.04 ở region của bạn (tra trong EC2 console)"
  # 🔧 TODO: không có default — bắt buộc truyền qua terraform.tfvars
}

variable "key_name" {
  type        = string
  description = "Tên SSH key pair đã tạo trên AWS để SSH vào instance"
}

variable "my_ip_cidr" {
  type        = string
  description = "IP của bạn dạng CIDR để mở SSH, vd 1.2.3.4/32"
  default     = "0.0.0.0/0" # 🔧 TODO: ĐỔI thành IP thật của bạn cho an toàn
}
