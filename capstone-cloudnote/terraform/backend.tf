# Remote state — BẮT BUỘC khi làm việc nhóm (tránh mất/xung đột state).
# Bỏ comment và điền bucket/table của bạn. Local state chỉ ổn khi học 1 mình.
#
# terraform {
#   backend "s3" {
#     bucket         = "my-tfstate-bucket"          # 🔧 TODO: bucket S3 của bạn
#     key            = "cloudnote/dev/terraform.tfstate"
#     region         = "ap-southeast-1"
#     dynamodb_table = "terraform-locks"            # khóa state, tránh apply đè nhau
#     encrypt        = true
#   }
# }
