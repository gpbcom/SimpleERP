# This module has no provider block and no credential: the ovh provider reads its credentials from its own
# environment variables at apply time.
locals {
  cloud = {
    name   = "ovhcloud"
    region = var.region
  }
}
