variable "default_region" {
  type    = string
  default = "ap-northeast-1"
}

variable "credentials_file" {
  type    = string
  default = ".credentials"
}

variable "session_name" {
  type    = string
  default = "terraform"
}

variable "user_role" {
  type = string
}

variable "slack_webhook_url" {
  type = string
}


variable "default_tags" {
  type = map(string)

  default = {
    ManagedBy = "https://github.com/sandbox/lambda_container_image/terraform"
  }
}
