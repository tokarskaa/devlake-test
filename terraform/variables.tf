variable "aws_region" {
 type = string
 description = "AWS region to use for resources."
 default = "us-east-1"
}

variable "aws_azs" {
 type = string
 description = "AWS Availability Zones"
 default = "us-east-1a"
}

variable "enable_dns_hostnames" {
 type = bool
 description = "Enable DNS hostnames in VPC"
 default = true
}

variable "vpc_cidr_block" {
 type = string
 description = "Base CIDR Block for VPC"
 default = "10.0.0.0/16"
}

variable "vpc_public_subnets_cidr_block" {
 type = string
 description = "CIDR Block for Public Subnets in VPC"
 default = "10.0.0.0/24"
}

variable "instance_type" {
 type = string
 description = "Type for EC2 Instance"
 default = "t2.micro"
}

variable "instance_key" {
 default = "MyKeyPair"
}