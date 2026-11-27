output "cluster" {
  description = "The managed Kubernetes cluster: its cloud, region, name and the name of its network."
  value       = local.cluster
}
