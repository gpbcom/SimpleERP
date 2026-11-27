variable "cloud" {
  type = object({
    name   = string
    region = string
  })
  description = "The cloud the container registry is built on: its provider name and its region."

  validation {
    condition     = contains(["ovhcloud", "scaleway"], var.cloud.name)
    error_message = "Invalid cloud name. It must be ovhcloud or scaleway."
  }

  validation {
    condition     = trimspace(var.cloud.region) != ""
    error_message = "Invalid cloud region. It must not be empty."
  }
}

variable "name" {
  type        = string
  description = "The name of the container registry, in lower case letters, digits and hyphens, starting with a letter."

  validation {
    condition     = can(regex("^[a-z]([a-z0-9-]{0,61}[a-z0-9])?$", var.name))
    error_message = "Invalid name. It must start with a lower case letter and hold at most 63 lower case letters, digits and hyphens, without ending in a hyphen."
  }
}
