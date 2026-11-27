terraform {
  required_version = ">= 1.11"

  required_providers {
    ovh = {
      source  = "ovh/ovh"
      version = "2.26.0"
    }
  }
}
