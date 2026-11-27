locals {
  network = {
    cloud  = var.cloud.name
    region = var.cloud.region
    name   = var.name
    cidr   = var.cidr
  }
}
