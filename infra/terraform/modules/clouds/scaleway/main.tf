# This module has no provider block and no credential: the scaleway provider reads its credentials from its own
# environment variables at apply time.
locals {
  cloud = {
    name   = "scaleway"
    region = var.region
  }
}
