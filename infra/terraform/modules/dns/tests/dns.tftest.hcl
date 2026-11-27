variables {
  cloud  = { name = "ovhcloud", region = "test-region" }
  name   = "simple-erp"
  domain = "erp.example.org"
}

run "the_dns_output_carries_every_field" {
  command = plan

  assert {
    condition     = output.dns.cloud == "ovhcloud"
    error_message = "The dns output must carry the expected cloud."
  }

  assert {
    condition     = output.dns.name == "simple-erp"
    error_message = "The dns output must carry the expected name."
  }

  assert {
    condition     = output.dns.domain == "erp.example.org"
    error_message = "The dns output must carry the expected domain."
  }
}

run "the_dns_output_follows_the_scaleway_cloud" {
  command = plan

  variables {
    cloud = { name = "scaleway", region = "test-region" }
  }

  assert {
    condition     = output.dns.cloud == "scaleway"
    error_message = "The dns output must carry the expected cloud."
  }

  assert {
    condition     = output.dns.name == "simple-erp"
    error_message = "The dns output must carry the expected name."
  }

  assert {
    condition     = output.dns.domain == "erp.example.org"
    error_message = "The dns output must carry the expected domain."
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

run "a_domain_with_no_dot_is_refused" {
  command = plan

  variables {
    domain = "localhost"
  }

  expect_failures = [var.domain]
}

run "a_domain_with_capitals_is_refused" {
  command = plan

  variables {
    domain = "Erp.Example.org"
  }

  expect_failures = [var.domain]
}
