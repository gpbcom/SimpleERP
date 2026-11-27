# T0.08: Review note

**Verdict:** ✅ Approved · **Branch:** `feature/tickets`

## What changed

- Six interface modules that work on any cloud: network, kubernetes-cluster, storage, registry, dns and helm-release. Each takes the same `cloud` object (`ovhcloud` or `scaleway`, plus a region) and a `name`, checks its inputs, and holds no resource yet. Running apply creates nothing.
- Two provider modules, `modules/clouds/ovhcloud` and `modules/clouds/scaleway`, are the only code tied to one cloud. Each pins its provider exactly and has no provider block, so credentials come only from the `OVH_*` and `SCW_*` environment variables.
- Two roots, `ovhcloud/` and `scaleway/`, are line-for-line identical except for the cloud module source and the provider pin. Both pin Terraform 1.17.2 and commit their lock files. They declare no backend, and `.gitignore` keeps state, tfvars, overrides and caches out of git.
- A new reusable `terraform.yml` runs fmt -check, init -backend=false, validate and `terraform test` (with a JUnit report) on each Terraform folder, one folder per matrix entry. `ci.yml` and `release.yml` call it, and `images`, `result` and `prepare` wait for it.
- `detect_changes.py` has a sixth output, `terraform`. Any change under `infra/terraform/` selects every Terraform folder and the repository tests.

## Acceptance criteria

| Criterion | Evidence | Result |
| --- | --- | --- |
| 1. The ovhcloud root passes fmt -check and validate in CI | `tests-evidences/terraform-fmt.txt`, `tests-evidences/terraform-validate-infra-terraform-ovhcloud.txt`, `tests-evidences/terraform-test-infra-terraform-ovhcloud.txt`; `TestTerraformWorkflow::test_the_scripts_run_each_terraform_command`, `TestCiWorkflow::test_the_terraform_job_receives_the_folders_to_check` | ✅ Pass |
| 2. The scaleway root passes fmt -check and validate in CI | `tests-evidences/terraform-fmt.txt`, `tests-evidences/terraform-validate-infra-terraform-scaleway.txt`, `tests-evidences/terraform-test-infra-terraform-scaleway.txt`; same workflow tests | ✅ Pass |
| 3. The roots differ only in their provider module and call the same six modules | `TestTerraformRoots::test_the_roots_are_identical_once_the_provider_module_is_normalised`, `::test_only_the_cloud_source_and_the_provider_entry_differ_between_the_roots`, `::test_a_root_calls_its_own_cloud_and_the_interface_once_each_and_nothing_else`; `tests-evidences/pytest.txt` (998 passed) | ✅ Pass |
| 4. No credential in a file and the state kept outside the repository | `TestTerraformStateAndCredentials` (no backend, state, tfvars and caches ignored, no literal credential, no sensitive default); `tests-evidences/pytest.txt` | ✅ Pass |

## Look at first

- **How the roots compare (criterion 3):** `infra/terraform/ovhcloud/main.tf` against `infra/terraform/scaleway/main.tf`, and the two `versions.tf`. `tests/infra/terraform/test_terraform_roots.py` pins the 4 lines that differ.
- **Credentials and state (criterion 4):** `infra/terraform/.gitignore`, `infra/terraform/modules/clouds/*/main.tf` (no provider block), and `tests/infra/terraform/test_terraform_state_and_credentials.py`. This ticket touches no company data, identity or permissions.
- **CI wiring:** `.github/workflows/terraform.yml` passes the folder through `env` only (no `${{ inputs }}` in a script), checks out with `persist-credentials: false`, and pins each action to a SHA. In `.github/workflows/ci.yml` and `release.yml`, a skipped terraform job still lets `images`, `result` and `prepare` run.
- **Change detection:** `.github/scripts/detect_changes.py` `discover_terraform`. It skips hidden folders, `_` folders and `tests` folders. A change to `infra/terraform/README.md` now selects every Terraform folder, and the old "selects nothing" cases were removed from the tests to match.

## Assumptions accepted

- Versions pinned and the CI step added to the existing pipeline: accepted (D415).
- No backend, and the operator chooses where state lives: accepted, because the specifications only ask for state outside the repository.
- Ticket link to sprint S01: accepted, because the roadmap has no per-ticket anchor.
- "Differ only in their provider module" means the cloud module source plus the provider pin: accepted, and tested at exactly 4 lines.
- A minimal interface (cloud, name, plus one input per module): accepted, because no specification gives one, and P2 extends it.
- No provider block, credentials from environment variables only: accepted (D421, criterion 4).
- Repository tests in `tests/infra/terraform/`: accepted, because `pytest tests` in python.yml collects them.
- The release runs the terraform suite: accepted (TKT-26).
- K16, the moved detector test needed no import edit: accepted, checked.

## Follow-ups

- Two pages make claims the roadmap does not. The README says later P0 tickets fill in the modules, and both pages call T9 a "ticket". The roadmap gives the work to T2.74 and T2.81 in P2, under capability T9 (K15).
- The validation messages use two styles across the six modules. Use the AGENT.md form in all of them (K08, K09).
- `test_repository_layout.py` now builds its expected front-end list from disk, which weakens the test and is outside the ticket's scope (K06).
- Add Dependabot entries for the Terraform providers and version (D415).
