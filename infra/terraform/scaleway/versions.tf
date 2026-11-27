terraform {
  required_version = "1.17.2"

  # No backend block: the state is never kept in the repository, and the operator chooses where it lives.
  required_providers {
    scaleway = {
      source  = "scaleway/scaleway"
      version = "2.93.0"
    }
  }
}
