resource "aws_vpc" "app_vpc" {
 cidr_block = var.vpc_cidr_block
 enable_dns_hostnames = var.enable_dns_hostnames
}