resource "aws_lambda_function" "sandbox_container_lambda" {
  function_name = "sandbox_container_lambda"
  description   = "Sandbox function to test container image lambda"
  role          = aws_iam_role.sandbox_container_lambda_role.arn
  tags          = var.default_tags

  package_type = "Image"
  image_uri    = "${aws_ecr_repository.sandbox_container_lambda_image.repository_url}:latest"

  timeout = 120

  environment {
    variables = {
      SLACK_WEBHOOK_URL    = var.slack_webhook_url
      LAMBDA_FUNCTION_NAME = "sandbox_container_lambda"
    }
  }
}
