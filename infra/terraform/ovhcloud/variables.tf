variable "name" {
  type        = string
  description = "The name that prefixes every resource of the deployment."
}

variable "region" {
  type        = string
  description = "The region of the cloud where the deployment runs."
}

variable "domain" {
  type        = string
  description = "The domain name that the DNS zone serves."
}

variable "network_cidr" {
  type        = string
  description = "The address range of the private network, in CIDR notation."
}
