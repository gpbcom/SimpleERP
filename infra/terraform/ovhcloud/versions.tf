terraform {
  required_version = "1.17.2"

  # No backend block: the state is never kept in the repository, and the operator chooses where it lives.
  required_providers {
    ovh = {
      source  = "ovh/ovh"
      version = "2.26.0"
    }
  }
}
