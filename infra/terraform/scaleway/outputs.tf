output "cloud" {
  description = "The cloud the deployment runs on."
  value       = module.cloud.cloud
}

output "network" {
  description = "The private network."
  value       = module.network.network
}

output "cluster" {
  description = "The Kubernetes cluster."
  value       = module.kubernetes_cluster.cluster
}

output "storage" {
  description = "The object storage."
  value       = module.storage.storage
}

output "registry" {
  description = "The container registry."
  value       = module.registry.registry
}

output "dns" {
  description = "The DNS zone."
  value       = module.dns.dns
}

output "release" {
  description = "The SimpleERP release installed on the cluster."
  value       = module.helm_release.release
}
