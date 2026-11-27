module "cloud" {
  source = "../modules/clouds/ovhcloud"

  region = var.region
}

module "network" {
  source = "../modules/network"

  cloud = module.cloud.cloud
  name  = var.name
  cidr  = var.network_cidr
}

module "kubernetes_cluster" {
  source = "../modules/kubernetes-cluster"

  cloud   = module.cloud.cloud
  name    = var.name
  network = module.network.network
}

module "storage" {
  source = "../modules/storage"

  cloud = module.cloud.cloud
  name  = var.name
}

module "registry" {
  source = "../modules/registry"

  cloud = module.cloud.cloud
  name  = var.name
}

module "dns" {
  source = "../modules/dns"

  cloud  = module.cloud.cloud
  name   = var.name
  domain = var.domain
}

module "helm_release" {
  source = "../modules/helm-release"

  cloud   = module.cloud.cloud
  name    = var.name
  cluster = module.kubernetes_cluster.cluster
}
