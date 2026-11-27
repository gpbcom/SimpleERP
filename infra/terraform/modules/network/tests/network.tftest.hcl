variables {
  cloud = { name = "ovhcloud", region = "test-region" }
  name  = "simple-erp"
  cidr  = "10.0.0.0/16"
}

run "the_output_carries_every_field_for_ovhcloud" {
  command = plan

  assert {
    condition     = output.network.cloud == "ovhcloud"
    error_message = "The network output must carry the cloud ovhcloud."
  }

  assert {
    condition     = output.network.region == "test-region"
    error_message = "The network output must carry the region test-region."
  }

  assert {
    condition     = output.network.name == "simple-erp"
    error_message = "The network output must carry the name simple-erp."
  }

  assert {
    condition     = output.network.cidr == "10.0.0.0/16"
    error_message = "The network output must carry the cidr 10.0.0.0/16."
  }
}

run "the_same_interface_serves_scaleway" {
  command = plan

  variables {
    cloud = { name = "scaleway", region = "fr-par" }
  }

  assert {
    condition     = output.network.cloud == "scaleway"
    error_message = "The network output must carry the cloud scaleway."
  }

  assert {
    condition     = output.network.region == "fr-par"
    error_message = "The network output must carry the region fr-par."
  }

  assert {
    condition     = output.network.name == "simple-erp"
    error_message = "The network output must carry the name simple-erp."
  }

  assert {
    condition     = output.network.cidr == "10.0.0.0/16"
    error_message = "The network output must carry the cidr 10.0.0.0/16."
  }
}

run "an_unknown_cloud_is_refused" {
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
    name = "1simple"
  }

  expect_failures = [var.name]
}

run "a_cidr_that_is_not_a_cidr_is_refused" {
  command = plan

  variables {
    cidr = "not-a-cidr"
  }

  expect_failures = [var.cidr]
}
