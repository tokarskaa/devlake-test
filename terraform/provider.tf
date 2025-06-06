terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.16"
    }
  }
  required_version = ">= 1.2.0"
}

provider "aws" {
  region     = var.aws_region
  profile = "SystemAdministrator-619071311446"
#   access_key = var.aws_access_key
#   secret_key = var.aws_secret_key
}