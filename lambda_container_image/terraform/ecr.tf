resource "aws_ecr_repository" "sandbox_container_lambda_image" {
  name                 = "sandbox_container_lambda_image"
  image_tag_mutability = "MUTABLE"

  image_scanning_configuration {
    scan_on_push = true
  }

  tags = var.default_tags
}

resource "aws_ecr_lifecycle_policy" "sandbox_container_lambda_image_policy" {
  repository = aws_ecr_repository.sandbox_container_lambda_image.name
  policy     = <<EOF
{
    "rules": [
        {
        "rulePriority": 1,
        "description": "For not prod env, keep latest 3",
        "selection": {
            "tagStatus": "any",
            "countType": "imageCountMoreThan",
            "countNumber": 3
        },
        "action": {
            "type": "expire"
        }
        }
    ]
}
EOF
}