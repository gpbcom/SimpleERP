locals {
  cluster = {
    cloud   = var.cloud.name
    region  = var.cloud.region
    name    = var.name
    network = var.network.name
  }
}
