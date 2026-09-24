terraform {
  required_providers {
    aws = { source = "hashicorp/aws", version = "~> 5.0" }
  }
}
provider "aws" {
  region = "ap-southeast-1"
}
resource "aws_instance" "web" {
  ami           = "ami-xxxxxxxx"   # thay bằng AMI Ubuntu của region bạn
  instance_type = "t2.micro"
  tags = { Name = "tf-lab-web" }
}
output "public_ip" {
  value = aws_instance.web.public_ip
}
