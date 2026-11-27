mock_provider "ovh" {}

run "a_valid_region_gives_the_ovhcloud_cloud_object" {
  command = plan

  variables {
    region = "GRA11"
  }

  assert {
    condition     = output.cloud.name == "ovhcloud"
    error_message = "The cloud name must be ovhcloud."
  }

  assert {
    condition     = output.cloud.region == "GRA11"
    error_message = "The cloud region must be the region given."
  }
}

run "a_blank_region_is_refused" {
  command = plan

  variables {
    region = "   "
  }

  expect_failures = [var.region]
}
