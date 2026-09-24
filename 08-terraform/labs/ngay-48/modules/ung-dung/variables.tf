variable "ten" {
  description = "Tên ứng dụng, dùng để đặt tên container"
  type        = string
}

variable "so_ban" {
  description = "Số bản sao cần chạy"
  type        = number
  default     = 1

  validation {
    condition     = var.so_ban > 0 && var.so_ban <= 10
    error_message = "so_ban phải nằm trong khoảng 1 đến 10."
  }
}

variable "cong_bat_dau" {
  description = "Cổng đầu tiên trên máy chủ; các bản sau tăng dần"
  type        = number
}

variable "moi_truong" {
  description = "Tên môi trường (dev/prod)"
  type        = string
}

variable "id_mang" {
  description = "ID mạng Docker để gắn container vào"
  type        = string
}
