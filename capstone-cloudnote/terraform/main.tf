# =====================================================================
# CloudNote — Hạ tầng bằng code (SKELETON để bạn hoàn thiện)
#
# Đây là bộ khung dùng AWS EC2 làm ví dụ (phổ biến nhất). Bạn có thể đổi
# sang nhà cung cấp khác (GCP/Azure) hoặc dùng k3s trên 1 VM để tiết kiệm.
# Mục tiêu: tạo 1 server có Docker để chạy app (hoặc 1 cluster k3s).
#
# Quy trình: terraform init -> plan -> apply ; xong demo thì terraform destroy
# =====================================================================

terraform {
  required_version = ">= 1.6"
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region = var.region
}

# Security Group: chỉ mở cổng cần thiết (least privilege)
resource "aws_security_group" "cloudnote" {
  name        = "${var.project}-sg"
  description = "CloudNote inbound rules"

  ingress {
    description = "SSH"
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = [var.my_ip_cidr] # 🔧 TODO: chỉ IP của bạn, KHÔNG 0.0.0.0/0
  }
  ingress {
    description = "HTTP"
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = local.tags
}

# Máy ảo chạy app (cài Docker tự động qua user_data)
resource "aws_instance" "cloudnote" {
  ami                    = var.ami_id # 🔧 TODO: AMI Ubuntu ở region của bạn
  instance_type          = var.instance_type
  key_name               = var.key_name
  vpc_security_group_ids = [aws_security_group.cloudnote.id]

  user_data = <<-EOF
    #!/bin/bash
    set -euo pipefail
    apt-get update && apt-get install -y docker.io docker-compose-plugin git
    systemctl enable --now docker
    # 🔧 TODO: clone repo & docker compose up, hoặc cài k3s rồi kubectl apply -f k8s/
  EOF

  tags = merge(local.tags, { Name = "${var.project}-app" })
}

locals {
  tags = {
    Project     = var.project
    Environment = var.environment
    ManagedBy   = "terraform"
  }
}
