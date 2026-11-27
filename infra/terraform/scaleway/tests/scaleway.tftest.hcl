mock_provider "scaleway" {}

variables {
  name         = "simple-erp"
  region       = "test-region"
  domain       = "erp.example.org"
  network_cidr = "10.0.0.0/16"
}

run "wiring" {
  command = plan

  assert {
    condition     = output.cloud.name == "scaleway"
    error_message = "The root must call the scaleway cloud module."
  }

  assert {
    condition     = output.network.cloud == output.cloud.name && output.network.region == var.region
    error_message = "The network must belong to the root's cloud and region."
  }

  assert {
    condition     = output.cluster.cloud == output.cloud.name && output.cluster.region == var.region
    error_message = "The cluster must belong to the root's cloud and region."
  }

  assert {
    condition     = output.storage.cloud == output.cloud.name && output.storage.region == var.region
    error_message = "The storage must belong to the root's cloud and region."
  }

  assert {
    condition     = output.registry.cloud == output.cloud.name && output.registry.region == var.region
    error_message = "The registry must belong to the root's cloud and region."
  }

  assert {
    condition     = output.dns.cloud == output.cloud.name && output.release.cloud == output.cloud.name
    error_message = "The DNS zone and the release must belong to the root's cloud."
  }

  assert {
    condition     = output.cluster.network == output.network.name
    error_message = "The cluster must sit on the network."
  }

  assert {
    condition     = output.release.cluster == output.cluster.name
    error_message = "The release must be installed on the cluster."
  }

  assert {
    condition     = output.dns.domain == var.domain
    error_message = "The DNS zone must serve the domain."
  }

  assert {
    condition     = output.network.cidr == var.network_cidr
    error_message = "The network must use the given CIDR."
  }
}
