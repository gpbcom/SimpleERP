variable "cloud" {
  type = object({
    name   = string
    region = string
  })
  description = "The cloud the resources belong to: its name (ovhcloud or scaleway) and its region."

  validation {
    condition     = contains(["ovhcloud", "scaleway"], var.cloud.name)
    error_message = "Invalid cloud name. Must be ovhcloud or scaleway."
  }

  validation {
    condition     = trimspace(var.cloud.region) != ""
    error_message = "Invalid cloud region. Must not be blank."
  }
}

variable "name" {
  type        = string
  description = "The name of the resource, in lower case letters, digits and hyphens, starting with a letter."

  validation {
    condition     = can(regex("^[a-z]([a-z0-9-]{0,61}[a-z0-9])?$", var.name))
    error_message = "Invalid name. Must start with a lower case letter, use only lower case letters, digits and hyphens, end with a letter or a digit, and hold at most 63 characters."
  }
}
