variables {
  cloud = { name = "ovhcloud", region = "test-region" }
  name  = "simple-erp"
}

run "the_registry_output_carries_every_field" {
  command = plan

  assert {
    condition     = output.registry.cloud == "ovhcloud"
    error_message = "The registry output must carry the expected cloud."
  }

  assert {
    condition     = output.registry.region == "test-region"
    error_message = "The registry output must carry the expected region."
  }

  assert {
    condition     = output.registry.name == "simple-erp"
    error_message = "The registry output must carry the expected name."
  }
}

run "the_registry_output_follows_the_scaleway_cloud" {
  command = plan

  variables {
    cloud = { name = "scaleway", region = "test-region" }
  }

  assert {
    condition     = output.registry.cloud == "scaleway"
    error_message = "The registry output must carry the expected cloud."
  }

  assert {
    condition     = output.registry.region == "test-region"
    error_message = "The registry output must carry the expected region."
  }

  assert {
    condition     = output.registry.name == "simple-erp"
    error_message = "The registry output must carry the expected name."
  }
}

run "an_unknown_cloud_name_is_refused" {
  command = plan

  variables {
    cloud = { name = "aws", region = "test-region" }
  }

  expect_failures = [var.cloud]
}

run "a_blank_region_is_refused" {
  command = plan

  variables {
    cloud = { name = "ovhcloud", region = "  " }
  }

  expect_failures = [var.cloud]
}

run "a_name_with_capitals_is_refused" {
  command = plan

  variables {
    name = "Simple-ERP"
  }

  expect_failures = [var.name]
}

run "a_name_starting_with_a_digit_is_refused" {
  command = plan

  variables {
    name = "1simple-erp"
  }

  expect_failures = [var.name]
}
