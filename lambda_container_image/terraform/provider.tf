terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 3.27"
    }
  }
}

provider "aws" {
  region                  = var.default_region
  shared_credentials_file = var.credentials_file
  assume_role {
    role_arn     = var.user_role
    session_name = var.session_name
  }
}

