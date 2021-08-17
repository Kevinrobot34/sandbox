data "aws_iam_policy_document" "sandbox_container_lambda_role_assume_role_policy" {
  statement {
    actions = ["sts:AssumeRole"]
    effect  = "Allow"
    principals {
      type        = "Service"
      identifiers = ["lambda.amazonaws.com"]
    }
  }
}

data "aws_iam_policy_document" "sandbox_container_lambda_role_policy" {
  statement {
    effect    = "Allow"
    actions   = ["logs:CreateLogStream", "logs:PutLogEvents"]
    resources = ["arn:aws:logs:*:*:log-group:/aws/lambda/*"]
  }
  statement {
    effect    = "Allow"
    actions   = ["logs:CreateLogGroup"]
    resources = ["*"]
  }
}

resource "aws_iam_role" "sandbox_container_lambda_role" {
  name = "sandbox_container_lambda_role"
  tags = var.default_tags

  assume_role_policy = data.aws_iam_policy_document.sandbox_container_lambda_role_assume_role_policy.json
}

resource "aws_iam_role_policy" "sandbox_container_lambda_role_policy" {
  name   = "sandbox_container_lambda_role_policy"
  role   = aws_iam_role.sandbox_container_lambda_role.id
  policy = data.aws_iam_policy_document.sandbox_container_lambda_role_policy.json
}
