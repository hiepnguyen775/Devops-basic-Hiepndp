output "public_ip" {
  description = "IP công khai của server — SSH và mở app qua IP này"
  value       = aws_instance.cloudnote.public_ip
}

output "ssh_command" {
  description = "Lệnh SSH vào server"
  value       = "ssh -i ${var.key_name}.pem ubuntu@${aws_instance.cloudnote.public_ip}"
}
