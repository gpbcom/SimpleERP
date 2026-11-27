# T0.08: Terraform module skeletons

**Status:** ✅ Done · **Ticket:** [TICKET.md](TICKET.md) · **Choices and trade-offs:** [IMPLEMENTATION.md](IMPLEMENTATION.md) · **Review:** [REVIEW.md](REVIEW.md)

## 🔭 What it does

- Six cloud-neutral Terraform modules (network, kubernetes-cluster, storage, registry, dns, helm-release) share one interface: a `cloud` object and a `name`. They check their inputs and hold no resource yet, so an apply creates nothing.
- Two provider modules, one for OVHcloud and one for Scaleway, are the only code tied to a cloud. Each pins its provider and holds no credential.
- Two roots, `ovhcloud` and `scaleway`, call the same six modules and differ only in their cloud module and provider pin. No backend is declared, and state and variable files are ignored by git.
- CI checks every Terraform folder (format, init without backend, validate, test) in a new reusable workflow that the CI and the release both call.

## ⚙️ How it works

1. **A root selects its cloud:** `module "cloud"` points at the provider module of that cloud and passes the region, in [`infra/terraform/ovhcloud/main.tf:1-5`](../../../infra/terraform/ovhcloud/main.tf#L1-L5). The Scaleway root is the same file with another source.
2. **The provider module builds the `cloud` object:** a local holds the cloud name and region, in [`infra/terraform/modules/clouds/ovhcloud/main.tf:3-8`](../../../infra/terraform/modules/clouds/ovhcloud/main.tf#L3-L8). It has no provider block, so the provider reads its credentials from environment variables. The region is validated in [`infra/terraform/modules/clouds/ovhcloud/variables.tf:1-9`](../../../infra/terraform/modules/clouds/ovhcloud/variables.tf#L1-L9) and the object is output in [`infra/terraform/modules/clouds/ovhcloud/outputs.tf:1-4`](../../../infra/terraform/modules/clouds/ovhcloud/outputs.tf#L1-L4).
3. **The root wires the six interface modules:** each receives `module.cloud.cloud` and `var.name`, and the network, cluster and helm-release modules chain their outputs, in [`infra/terraform/ovhcloud/main.tf:7-51`](../../../infra/terraform/ovhcloud/main.tf#L7-L51).
4. **An interface module validates its inputs:** the cloud must be `ovhcloud` or `scaleway` with a non-blank region, the name an RFC 1123 label, the CIDR an IPv4 range, in [`infra/terraform/modules/network/variables.tf:1-37`](../../../infra/terraform/modules/network/variables.tf#L1-L37). It then returns one object in [`infra/terraform/modules/network/main.tf:1-8`](../../../infra/terraform/modules/network/main.tf#L1-L8).
5. **Versions are pinned and state stays out:** the root pins Terraform and the provider exactly and declares no backend, in [`infra/terraform/ovhcloud/versions.tf:1-11`](../../../infra/terraform/ovhcloud/versions.tf#L1-L11). The lock file is committed; state, tfvars, overrides and caches are ignored in [`infra/terraform/.gitignore:1-12`](../../../infra/terraform/.gitignore#L1-L12).
6. **Change detection lists the folders:** [`.github/scripts/detect_changes.py:101-110`](../../../.github/scripts/detect_changes.py#L101-L110) finds every folder holding a `*.tf` file, skipping hidden, `_` and `tests` folders. A change under `infra/terraform/` selects them all and sets `repository` ([`.github/scripts/detect_changes.py:183-184`](../../../.github/scripts/detect_changes.py#L183-L184), [`.github/scripts/detect_changes.py:198`](../../../.github/scripts/detect_changes.py#L198)). It prints them as the sixth output ([`.github/scripts/detect_changes.py:210`](../../../.github/scripts/detect_changes.py#L210)).
7. **CI calls the reusable workflow:** the `terraform` job runs when the list is not empty, in [`.github/workflows/ci.yml:84-89`](../../../.github/workflows/ci.yml#L84-L89), and `result` and `images` wait for it ([`.github/workflows/ci.yml:92`](../../../.github/workflows/ci.yml#L92), [`.github/workflows/ci.yml:104`](../../../.github/workflows/ci.yml#L104)). The release does the same in [`.github/workflows/release.yml:97-103`](../../../.github/workflows/release.yml#L97-L103).
8. **One matrix entry per folder:** [`.github/workflows/terraform.yml:24-62`](../../../.github/workflows/terraform.yml#L24-L62) runs `fmt -check` (line 39), `init -backend=false` (line 41), `validate` (line 43) and `terraform test` with a JUnit report (line 54) when the folder has a `tests/` folder. The folder goes through `env`, never into the script text, and the report is uploaded even on failure.

## 🧱 Files and lines changed

<!-- changes -->
| File | Change | Lines in the new version | Added | Removed |
| --- | --- | --- | --- | --- |
| [`.github/scripts/detect_changes.py`](../../../.github/scripts/detect_changes.py) | Modified | [7](../../../.github/scripts/detect_changes.py#L7), [16-19](../../../.github/scripts/detect_changes.py#L16), [22-24](../../../.github/scripts/detect_changes.py#L22), [37-38](../../../.github/scripts/detect_changes.py#L37), [59](../../../.github/scripts/detect_changes.py#L59), [98-110](../../../.github/scripts/detect_changes.py#L98), [168](../../../.github/scripts/detect_changes.py#L168), [175](../../../.github/scripts/detect_changes.py#L175), [181-182](../../../.github/scripts/detect_changes.py#L181), [195](../../../.github/scripts/detect_changes.py#L195), [199](../../../.github/scripts/detect_changes.py#L199), [207](../../../.github/scripts/detect_changes.py#L207) | +31 | −6 |
| [`.github/workflows/ci.yml`](../../../.github/workflows/ci.yml) | Modified | [4-5](../../../.github/workflows/ci.yml#L4), [36](../../../.github/workflows/ci.yml#L36), [84-90](../../../.github/workflows/ci.yml#L84), [92](../../../.github/workflows/ci.yml#L92), [104](../../../.github/workflows/ci.yml#L104) | +12 | −4 |
| [`.github/workflows/release.yml`](../../../.github/workflows/release.yml) | Modified | [69](../../../.github/workflows/release.yml#L69), [97-103](../../../.github/workflows/release.yml#L97), [105](../../../.github/workflows/release.yml#L105) | +9 | −1 |
| [`.github/workflows/terraform.yml`](../../../.github/workflows/terraform.yml) | Added | [1-62](../../../.github/workflows/terraform.yml#L1) | +62 | −0 |
| [`docs/technical/delivery/ci-cd-and-stages.md`](../../../docs/technical/delivery/ci-cd-and-stages.md) | Modified | [49](../../../docs/technical/delivery/ci-cd-and-stages.md#L49), [52](../../../docs/technical/delivery/ci-cd-and-stages.md#L52), [60-61](../../../docs/technical/delivery/ci-cd-and-stages.md#L60) | +4 | −2 |
| [`docs/technical/infrastructure/infrastructure.md`](../../../docs/technical/infrastructure/infrastructure.md) | Modified | [8-12](../../../docs/technical/infrastructure/infrastructure.md#L8), [55](../../../docs/technical/infrastructure/infrastructure.md#L55) | +6 | −2 |
| [`infra/terraform/.gitignore`](../../../infra/terraform/.gitignore) | Added | [1-12](../../../infra/terraform/.gitignore#L1) | +12 | −0 |
| [`infra/terraform/README.md`](../../../infra/terraform/README.md) | Modified | [3-7](../../../infra/terraform/README.md#L3), [9-83](../../../infra/terraform/README.md#L9) | +80 | −4 |
| [`infra/terraform/modules/clouds/ovhcloud/main.tf`](../../../infra/terraform/modules/clouds/ovhcloud/main.tf) | Added | [1-8](../../../infra/terraform/modules/clouds/ovhcloud/main.tf#L1) | +8 | −0 |
| [`infra/terraform/modules/clouds/ovhcloud/outputs.tf`](../../../infra/terraform/modules/clouds/ovhcloud/outputs.tf) | Added | [1-4](../../../infra/terraform/modules/clouds/ovhcloud/outputs.tf#L1) | +4 | −0 |
| [`infra/terraform/modules/clouds/ovhcloud/tests/ovhcloud.tftest.hcl`](../../../infra/terraform/modules/clouds/ovhcloud/tests/ovhcloud.tftest.hcl) | Added | [1-29](../../../infra/terraform/modules/clouds/ovhcloud/tests/ovhcloud.tftest.hcl#L1) | +29 | −0 |
| [`infra/terraform/modules/clouds/ovhcloud/variables.tf`](../../../infra/terraform/modules/clouds/ovhcloud/variables.tf) | Added | [1-9](../../../infra/terraform/modules/clouds/ovhcloud/variables.tf#L1) | +9 | −0 |
| [`infra/terraform/modules/clouds/ovhcloud/versions.tf`](../../../infra/terraform/modules/clouds/ovhcloud/versions.tf) | Added | [1-10](../../../infra/terraform/modules/clouds/ovhcloud/versions.tf#L1) | +10 | −0 |
| [`infra/terraform/modules/clouds/scaleway/main.tf`](../../../infra/terraform/modules/clouds/scaleway/main.tf) | Added | [1-8](../../../infra/terraform/modules/clouds/scaleway/main.tf#L1) | +8 | −0 |
| [`infra/terraform/modules/clouds/scaleway/outputs.tf`](../../../infra/terraform/modules/clouds/scaleway/outputs.tf) | Added | [1-4](../../../infra/terraform/modules/clouds/scaleway/outputs.tf#L1) | +4 | −0 |
| [`infra/terraform/modules/clouds/scaleway/tests/scaleway.tftest.hcl`](../../../infra/terraform/modules/clouds/scaleway/tests/scaleway.tftest.hcl) | Added | [1-29](../../../infra/terraform/modules/clouds/scaleway/tests/scaleway.tftest.hcl#L1) | +29 | −0 |
| [`infra/terraform/modules/clouds/scaleway/variables.tf`](../../../infra/terraform/modules/clouds/scaleway/variables.tf) | Added | [1-9](../../../infra/terraform/modules/clouds/scaleway/variables.tf#L1) | +9 | −0 |
| [`infra/terraform/modules/clouds/scaleway/versions.tf`](../../../infra/terraform/modules/clouds/scaleway/versions.tf) | Added | [1-10](../../../infra/terraform/modules/clouds/scaleway/versions.tf#L1) | +10 | −0 |
| [`infra/terraform/modules/dns/main.tf`](../../../infra/terraform/modules/dns/main.tf) | Added | [1-7](../../../infra/terraform/modules/dns/main.tf#L1) | +7 | −0 |
| [`infra/terraform/modules/dns/outputs.tf`](../../../infra/terraform/modules/dns/outputs.tf) | Added | [1-4](../../../infra/terraform/modules/dns/outputs.tf#L1) | +4 | −0 |
| [`infra/terraform/modules/dns/tests/dns.tftest.hcl`](../../../infra/terraform/modules/dns/tests/dns.tftest.hcl) | Added | [1-107](../../../infra/terraform/modules/dns/tests/dns.tftest.hcl#L1) | +107 | −0 |
| [`infra/terraform/modules/dns/variables.tf`](../../../infra/terraform/modules/dns/variables.tf) | Added | [1-37](../../../infra/terraform/modules/dns/variables.tf#L1) | +37 | −0 |
| [`infra/terraform/modules/dns/versions.tf`](../../../infra/terraform/modules/dns/versions.tf) | Added | [1-3](../../../infra/terraform/modules/dns/versions.tf#L1) | +3 | −0 |
| [`infra/terraform/modules/helm-release/main.tf`](../../../infra/terraform/modules/helm-release/main.tf) | Added | [1-7](../../../infra/terraform/modules/helm-release/main.tf#L1) | +7 | −0 |
| [`infra/terraform/modules/helm-release/outputs.tf`](../../../infra/terraform/modules/helm-release/outputs.tf) | Added | [1-4](../../../infra/terraform/modules/helm-release/outputs.tf#L1) | +4 | −0 |
| [`infra/terraform/modules/helm-release/tests/helm-release.tftest.hcl`](../../../infra/terraform/modules/helm-release/tests/helm-release.tftest.hcl) | Added | [1-87](../../../infra/terraform/modules/helm-release/tests/helm-release.tftest.hcl#L1) | +87 | −0 |
| [`infra/terraform/modules/helm-release/variables.tf`](../../../infra/terraform/modules/helm-release/variables.tf) | Added | [1-37](../../../infra/terraform/modules/helm-release/variables.tf#L1) | +37 | −0 |
| [`infra/terraform/modules/helm-release/versions.tf`](../../../infra/terraform/modules/helm-release/versions.tf) | Added | [1-3](../../../infra/terraform/modules/helm-release/versions.tf#L1) | +3 | −0 |
| [`infra/terraform/modules/kubernetes-cluster/main.tf`](../../../infra/terraform/modules/kubernetes-cluster/main.tf) | Added | [1-8](../../../infra/terraform/modules/kubernetes-cluster/main.tf#L1) | +8 | −0 |
| [`infra/terraform/modules/kubernetes-cluster/outputs.tf`](../../../infra/terraform/modules/kubernetes-cluster/outputs.tf) | Added | [1-4](../../../infra/terraform/modules/kubernetes-cluster/outputs.tf#L1) | +4 | −0 |
| [`infra/terraform/modules/kubernetes-cluster/tests/kubernetes-cluster.tftest.hcl`](../../../infra/terraform/modules/kubernetes-cluster/tests/kubernetes-cluster.tftest.hcl) | Added | [1-97](../../../infra/terraform/modules/kubernetes-cluster/tests/kubernetes-cluster.tftest.hcl#L1) | +97 | −0 |
| [`infra/terraform/modules/kubernetes-cluster/variables.tf`](../../../infra/terraform/modules/kubernetes-cluster/variables.tf) | Added | [1-37](../../../infra/terraform/modules/kubernetes-cluster/variables.tf#L1) | +37 | −0 |
| [`infra/terraform/modules/kubernetes-cluster/versions.tf`](../../../infra/terraform/modules/kubernetes-cluster/versions.tf) | Added | [1-3](../../../infra/terraform/modules/kubernetes-cluster/versions.tf#L1) | +3 | −0 |
| [`infra/terraform/modules/network/main.tf`](../../../infra/terraform/modules/network/main.tf) | Added | [1-8](../../../infra/terraform/modules/network/main.tf#L1) | +8 | −0 |
| [`infra/terraform/modules/network/outputs.tf`](../../../infra/terraform/modules/network/outputs.tf) | Added | [1-4](../../../infra/terraform/modules/network/outputs.tf#L1) | +4 | −0 |
| [`infra/terraform/modules/network/tests/network.tftest.hcl`](../../../infra/terraform/modules/network/tests/network.tftest.hcl) | Added | [1-107](../../../infra/terraform/modules/network/tests/network.tftest.hcl#L1) | +107 | −0 |
| [`infra/terraform/modules/network/variables.tf`](../../../infra/terraform/modules/network/variables.tf) | Added | [1-37](../../../infra/terraform/modules/network/variables.tf#L1) | +37 | −0 |
| [`infra/terraform/modules/network/versions.tf`](../../../infra/terraform/modules/network/versions.tf) | Added | [1-3](../../../infra/terraform/modules/network/versions.tf#L1) | +3 | −0 |
| [`infra/terraform/modules/registry/main.tf`](../../../infra/terraform/modules/registry/main.tf) | Added | [1-7](../../../infra/terraform/modules/registry/main.tf#L1) | +7 | −0 |
| [`infra/terraform/modules/registry/outputs.tf`](../../../infra/terraform/modules/registry/outputs.tf) | Added | [1-4](../../../infra/terraform/modules/registry/outputs.tf#L1) | +4 | −0 |
| [`infra/terraform/modules/registry/tests/registry.tftest.hcl`](../../../infra/terraform/modules/registry/tests/registry.tftest.hcl) | Added | [1-86](../../../infra/terraform/modules/registry/tests/registry.tftest.hcl#L1) | +86 | −0 |
| [`infra/terraform/modules/registry/variables.tf`](../../../infra/terraform/modules/registry/variables.tf) | Added | [1-27](../../../infra/terraform/modules/registry/variables.tf#L1) | +27 | −0 |
| [`infra/terraform/modules/registry/versions.tf`](../../../infra/terraform/modules/registry/versions.tf) | Added | [1-3](../../../infra/terraform/modules/registry/versions.tf#L1) | +3 | −0 |
| [`infra/terraform/modules/storage/main.tf`](../../../infra/terraform/modules/storage/main.tf) | Added | [1-7](../../../infra/terraform/modules/storage/main.tf#L1) | +7 | −0 |
| [`infra/terraform/modules/storage/outputs.tf`](../../../infra/terraform/modules/storage/outputs.tf) | Added | [1-4](../../../infra/terraform/modules/storage/outputs.tf#L1) | +4 | −0 |
| [`infra/terraform/modules/storage/tests/storage.tftest.hcl`](../../../infra/terraform/modules/storage/tests/storage.tftest.hcl) | Added | [1-86](../../../infra/terraform/modules/storage/tests/storage.tftest.hcl#L1) | +86 | −0 |
| [`infra/terraform/modules/storage/variables.tf`](../../../infra/terraform/modules/storage/variables.tf) | Added | [1-27](../../../infra/terraform/modules/storage/variables.tf#L1) | +27 | −0 |
| [`infra/terraform/modules/storage/versions.tf`](../../../infra/terraform/modules/storage/versions.tf) | Added | [1-3](../../../infra/terraform/modules/storage/versions.tf#L1) | +3 | −0 |
| [`infra/terraform/ovhcloud/.terraform.lock.hcl`](../../../infra/terraform/ovhcloud/.terraform.lock.hcl) | Added | [1-26](../../../infra/terraform/ovhcloud/.terraform.lock.hcl#L1) | +26 | −0 |
| [`infra/terraform/ovhcloud/main.tf`](../../../infra/terraform/ovhcloud/main.tf) | Added | [1-51](../../../infra/terraform/ovhcloud/main.tf#L1) | +51 | −0 |
| [`infra/terraform/ovhcloud/outputs.tf`](../../../infra/terraform/ovhcloud/outputs.tf) | Added | [1-34](../../../infra/terraform/ovhcloud/outputs.tf#L1) | +34 | −0 |
| [`infra/terraform/ovhcloud/tests/ovhcloud.tftest.hcl`](../../../infra/terraform/ovhcloud/tests/ovhcloud.tftest.hcl) | Added | [1-62](../../../infra/terraform/ovhcloud/tests/ovhcloud.tftest.hcl#L1) | +62 | −0 |
| [`infra/terraform/ovhcloud/variables.tf`](../../../infra/terraform/ovhcloud/variables.tf) | Added | [1-19](../../../infra/terraform/ovhcloud/variables.tf#L1) | +19 | −0 |
| [`infra/terraform/ovhcloud/versions.tf`](../../../infra/terraform/ovhcloud/versions.tf) | Added | [1-11](../../../infra/terraform/ovhcloud/versions.tf#L1) | +11 | −0 |
| [`infra/terraform/scaleway/.terraform.lock.hcl`](../../../infra/terraform/scaleway/.terraform.lock.hcl) | Added | [1-26](../../../infra/terraform/scaleway/.terraform.lock.hcl#L1) | +26 | −0 |
| [`infra/terraform/scaleway/main.tf`](../../../infra/terraform/scaleway/main.tf) | Added | [1-51](../../../infra/terraform/scaleway/main.tf#L1) | +51 | −0 |
| [`infra/terraform/scaleway/outputs.tf`](../../../infra/terraform/scaleway/outputs.tf) | Added | [1-34](../../../infra/terraform/scaleway/outputs.tf#L1) | +34 | −0 |
| [`infra/terraform/scaleway/tests/scaleway.tftest.hcl`](../../../infra/terraform/scaleway/tests/scaleway.tftest.hcl) | Added | [1-62](../../../infra/terraform/scaleway/tests/scaleway.tftest.hcl#L1) | +62 | −0 |
| [`infra/terraform/scaleway/variables.tf`](../../../infra/terraform/scaleway/variables.tf) | Added | [1-19](../../../infra/terraform/scaleway/variables.tf#L1) | +19 | −0 |
| [`infra/terraform/scaleway/versions.tf`](../../../infra/terraform/scaleway/versions.tf) | Added | [1-11](../../../infra/terraform/scaleway/versions.tf#L1) | +11 | −0 |
| [`tests/ci/detect_changes/helpers.py`](../../../tests/ci/detect_changes/helpers.py) | Modified | [15-16](../../../tests/ci/detect_changes/helpers.py#L15), [25-30](../../../tests/ci/detect_changes/helpers.py#L25), [54-60](../../../tests/ci/detect_changes/helpers.py#L54), [94-101](../../../tests/ci/detect_changes/helpers.py#L94), [111](../../../tests/ci/detect_changes/helpers.py#L111) | +24 | −2 |
| [`tests/ci/detect_changes/terraform/test_terraform.py`](../../../tests/ci/detect_changes/terraform/test_terraform.py) | Added | [1-58](../../../tests/ci/detect_changes/terraform/test_terraform.py#L1) | +58 | −0 |
| [`tests/ci/detect_changes/test_detect_changes.py`](../../../tests/ci/detect_changes/test_detect_changes.py) | Modified | [32](../../../tests/ci/detect_changes/test_detect_changes.py#L32), [removed after 112](../../../tests/ci/detect_changes/test_detect_changes.py#L112) | +1 | −2 |
| [`tests/ci/detect_changes/test_repository_layout.py`](../../../tests/ci/detect_changes/test_repository_layout.py) | Modified | [5](../../../tests/ci/detect_changes/test_repository_layout.py#L5), [7](../../../tests/ci/detect_changes/test_repository_layout.py#L7), [27-39](../../../tests/ci/detect_changes/test_repository_layout.py#L27), [49-50](../../../tests/ci/detect_changes/test_repository_layout.py#L49), [64-65](../../../tests/ci/detect_changes/test_repository_layout.py#L64), [81](../../../tests/ci/detect_changes/test_repository_layout.py#L81), [86-87](../../../tests/ci/detect_changes/test_repository_layout.py#L86), [removed after 71](../../../tests/ci/detect_changes/test_repository_layout.py#L71) | +22 | −5 |
| [`tests/ci/detect_changes/test_shared_changes.py`](../../../tests/ci/detect_changes/test_shared_changes.py) | Modified | [46](../../../tests/ci/detect_changes/test_shared_changes.py#L46) | +1 | −0 |
| [`tests/ci/release/test_release_workflow.py`](../../../tests/ci/release/test_release_workflow.py) | Modified | [16](../../../tests/ci/release/test_release_workflow.py#L16), [22](../../../tests/ci/release/test_release_workflow.py#L22), [69-76](../../../tests/ci/release/test_release_workflow.py#L69) | +10 | −1 |
| [`tests/ci/workflows/checks/test_terraform_workflow.py`](../../../tests/ci/workflows/checks/test_terraform_workflow.py) | Added | [1-82](../../../tests/ci/workflows/checks/test_terraform_workflow.py#L1) | +82 | −0 |
| [`tests/ci/workflows/test_ci_workflow.py`](../../../tests/ci/workflows/test_ci_workflow.py) | Modified | [19-20](../../../tests/ci/workflows/test_ci_workflow.py#L19), [23](../../../tests/ci/workflows/test_ci_workflow.py#L23), [84](../../../tests/ci/workflows/test_ci_workflow.py#L84), [101-103](../../../tests/ci/workflows/test_ci_workflow.py#L101) | +7 | −3 |
| [`tests/ci/workflows/test_workflow_security.py`](../../../tests/ci/workflows/test_workflow_security.py) | Modified | [30](../../../tests/ci/workflows/test_workflow_security.py#L30) | +1 | −0 |
| [`tests/infra/terraform/helpers.py`](../../../tests/infra/terraform/helpers.py) | Added | [1-30](../../../tests/infra/terraform/helpers.py#L1) | +30 | −0 |
| [`tests/infra/terraform/test_terraform_roots.py`](../../../tests/infra/terraform/test_terraform_roots.py) | Added | [1-67](../../../tests/infra/terraform/test_terraform_roots.py#L1) | +67 | −0 |
| [`tests/infra/terraform/test_terraform_state_and_credentials.py`](../../../tests/infra/terraform/test_terraform_state_and_credentials.py) | Added | [1-65](../../../tests/infra/terraform/test_terraform_state_and_credentials.py#L1) | +65 | −0 |
| **72 files** | | | **+1968** | **−32** |
<!-- /changes -->

- [`infra/terraform/modules/`](../../../infra/terraform/modules/network/main.tf): six interface modules (`network`, `kubernetes-cluster`, `storage`, `registry`, `dns`, `helm-release`), each with `main.tf`, `variables.tf`, `outputs.tf`, `versions.tf` and a `tests/*.tftest.hcl`. They give the P2 tickets a fixed interface and hold no resource.
- [`infra/terraform/modules/clouds/ovhcloud/versions.tf`](../../../infra/terraform/modules/clouds/ovhcloud/versions.tf) and [`infra/terraform/modules/clouds/scaleway/versions.tf`](../../../infra/terraform/modules/clouds/scaleway/versions.tf): the two cloud modules, each pinning its provider exactly (lines 4-9).
- [`infra/terraform/ovhcloud/main.tf`](../../../infra/terraform/ovhcloud/main.tf) and [`infra/terraform/scaleway/main.tf`](../../../infra/terraform/scaleway/main.tf), with their `variables.tf`, `outputs.tf`, `versions.tf`, lock files and tests: the two roots, kept identical but for the cloud source and the provider pin.
- [`infra/terraform/.gitignore`](../../../infra/terraform/.gitignore): keeps state, tfvars, overrides and caches out of git (criterion 4).
- [`infra/terraform/README.md`](../../../infra/terraform/README.md) and [`docs/technical/infrastructure/infrastructure.md`](../../../docs/technical/infrastructure/infrastructure.md), [`docs/technical/delivery/ci-cd-and-stages.md`](../../../docs/technical/delivery/ci-cd-and-stages.md): describe the skeleton and the new CI suite.
- [`.github/workflows/terraform.yml`](../../../.github/workflows/terraform.yml): the new reusable workflow described in step 8.
- [`.github/workflows/ci.yml`](../../../.github/workflows/ci.yml) and [`.github/workflows/release.yml`](../../../.github/workflows/release.yml): the `terraform` job and the `needs` lists that wait for it.
- [`.github/scripts/detect_changes.py`](../../../.github/scripts/detect_changes.py): `discover_terraform` and the sixth `terraform` output.
- [`tests/infra/terraform/test_terraform_roots.py`](../../../tests/infra/terraform/test_terraform_roots.py) and [`tests/infra/terraform/test_terraform_state_and_credentials.py`](../../../tests/infra/terraform/test_terraform_state_and_credentials.py), with [`tests/infra/terraform/helpers.py`](../../../tests/infra/terraform/helpers.py): pin the identical roots (4 lines differ), the six modules, no backend, ignored state and no literal credential.
- [`tests/ci/detect_changes/terraform/test_terraform.py`](../../../tests/ci/detect_changes/terraform/test_terraform.py), [`tests/ci/detect_changes/helpers.py`](../../../tests/ci/detect_changes/helpers.py), [`tests/ci/detect_changes/test_detect_changes.py`](../../../tests/ci/detect_changes/test_detect_changes.py), [`tests/ci/detect_changes/test_shared_changes.py`](../../../tests/ci/detect_changes/test_shared_changes.py), [`tests/ci/detect_changes/test_repository_layout.py`](../../../tests/ci/detect_changes/test_repository_layout.py): the detector tests for the sixth output. The Terraform ones sit in their own folder to keep `tests/ci/detect_changes` at five Python files.
- [`tests/ci/workflows/checks/test_terraform_workflow.py`](../../../tests/ci/workflows/checks/test_terraform_workflow.py), [`tests/ci/workflows/test_ci_workflow.py`](../../../tests/ci/workflows/test_ci_workflow.py), [`tests/ci/workflows/test_workflow_security.py`](../../../tests/ci/workflows/test_workflow_security.py), [`tests/ci/release/test_release_workflow.py`](../../../tests/ci/release/test_release_workflow.py): the workflow tests for the new job, the pinned actions and the release.

## 🧪 How to test it

```bash
uv run pytest tests/infra/terraform -n 2
uv run pytest tests/ci/detect_changes -n 2
uv run pytest tests/ci/workflows -n 2
uv run pytest tests/ci/release -n 2
terraform fmt -check -recursive infra/terraform
terraform -chdir=infra/terraform/ovhcloud init -backend=false && terraform -chdir=infra/terraform/ovhcloud validate && terraform -chdir=infra/terraform/ovhcloud test
terraform -chdir=infra/terraform/scaleway init -backend=false && terraform -chdir=infra/terraform/scaleway validate && terraform -chdir=infra/terraform/scaleway test
```

The pytest runs check the roots, the state rules, the detector and the workflows. The Terraform commands are what `terraform.yml` runs for each folder.

## 🔗 Evidence

- [pytest](tests-evidences/pytest.txt): 998 passed.
- [terraform fmt](tests-evidences/terraform-fmt.txt): format check of every folder.
- [OVHcloud root, validate](tests-evidences/terraform-validate-infra-terraform-ovhcloud.txt), [test](tests-evidences/terraform-test-infra-terraform-ovhcloud.txt) and [init](tests-evidences/terraform-init-infra-terraform-ovhcloud.txt).
- [Scaleway root, validate](tests-evidences/terraform-validate-infra-terraform-scaleway.txt), [test](tests-evidences/terraform-test-infra-terraform-scaleway.txt) and [init](tests-evidences/terraform-init-infra-terraform-scaleway.txt).
- [Network module, validate](tests-evidences/terraform-validate-infra-terraform-modules-network.txt) and [test](tests-evidences/terraform-test-infra-terraform-modules-network.txt); the other modules have the same three files in the same folder.
- [ruff check](tests-evidences/ruff-check.txt), [ruff format](tests-evidences/ruff-format.txt), [mypy](tests-evidences/mypy.txt), [ticket references](tests-evidences/ticket-refs.txt) and [plan view](tests-evidences/plan-view.txt).

## 📝 Assumptions accepted

- No Terraform or provider version and no CI layout are named, so a reusable step is added to the existing pipeline with every version pinned (D415).
- No state backend is declared and the operator chooses one: REQ-T09-08 only says "state kept outside the repository".
- The ticket link points to sprint S01, because the roadmap has no per-ticket anchor.
- "Differ only in their provider module" means the cloud module source plus the provider pin: exactly 4 lines, pinned by a test.
- The specifications name the six modules but not their inputs, so a minimal interface (cloud, name, plus one input per module) is fixed for P2 to extend.
- No provider block is written, and providers read credentials from environment variables (D421).
- The repository tests go in `tests/infra/terraform/`, which `pytest tests` in python.yml collects.
- `terraform.yml` is also called from the release, because TKT-26 says a release runs every CI suite.
- K16: the moved detector test needed no import edit, because it already used full paths.

## 🔜 Follow-ups

| File | What to change |
| --- | --- |
| [`infra/terraform/README.md`](../../../infra/terraform/README.md), [`docs/technical/infrastructure/infrastructure.md`](../../../docs/technical/infrastructure/infrastructure.md) | The README says later P0 tickets fill in the modules, and both pages call T9 a "ticket". In the roadmap, no later P0 ticket touches `infra/terraform`: the resources come in P2 with T2.74 (OVHcloud) and T2.81 (Scaleway), under capability T9. Change both pages to say that. |
| The `variables.tf` of [`network`](../../../infra/terraform/modules/network/variables.tf), [`kubernetes-cluster`](../../../infra/terraform/modules/kubernetes-cluster/variables.tf), [`storage`](../../../infra/terraform/modules/storage/variables.tf), [`registry`](../../../infra/terraform/modules/registry/variables.tf), [`dns`](../../../infra/terraform/modules/dns/variables.tf) and [`helm-release`](../../../infra/terraform/modules/helm-release/variables.tf) | Two message styles: "Must be ..." and "Must not be blank." in the first three, "It must be ..." and "It must not be empty." in the last three. Use the AGENT.md form `Invalid <field>: ... Must be ...` in all six. |
| [`tests/ci/detect_changes/test_repository_layout.py`](../../../tests/ci/detect_changes/test_repository_layout.py) | The test of the shared front-end packages builds its expected list from the `frontend/` folders on disk, so it can no longer catch a missing project. Go back to a fixed list, or record why it is dynamic. |
| [`.github/dependabot.yml`](../../../.github/dependabot.yml) | The providers and the Terraform version are pinned but nothing proposes updates. Add a Dependabot `terraform` entry for both roots in a later ticket. |
