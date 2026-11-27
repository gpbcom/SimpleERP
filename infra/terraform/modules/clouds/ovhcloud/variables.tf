variable "region" {
  type        = string
  description = "The region of the OVHcloud account in which the deployment is created."

  validation {
    condition     = trimspace(var.region) != ""
    error_message = "Invalid region. Must not be empty."
  }
}
