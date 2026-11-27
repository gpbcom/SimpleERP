mock_provider "scaleway" {}

run "a_valid_region_gives_the_scaleway_cloud_object" {
  command = plan

  variables {
    region = "fr-par"
  }

  assert {
    condition     = output.cloud.name == "scaleway"
    error_message = "The cloud name must be scaleway."
  }

  assert {
    condition     = output.cloud.region == "fr-par"
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
