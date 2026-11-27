# T0.08: Implementation choices

**Ticket:** [TICKET.md](TICKET.md) · **How it works:** [EXPLAIN.md](EXPLAIN.md) · **Review:** [REVIEW.md](REVIEW.md)

## 🎯 Constraints

- The two roots differ only in their provider module, and call the same six modules (acceptance criterion 3 of [TICKET.md](TICKET.md); [REQ-T09-08](../../specs/03-technical/t09-install-backups-and-updates/requirements/req-t09-08-terraform-ovhcloud-scaleway.md)).
- No credential in a file, and state kept outside the repository (criterion 4; [D421](../../specs/06-decisions/technical/d421-infrastructure-cncf.md)).
- Versions are pinned, and the roots pass fmt -check and validate in CI (criteria 1 and 2; D415).
- A Terraform change must run CI jobs for the folders it touches, and a release runs every CI suite with its reports (AGENT.md "CI/CD", TKT-26).
- The code stays in the layout of [D438](../../specs/06-decisions/technical/d438-repository-layout.md), and a test folder holds at most five Python files (AGENT.md).

## ⚖️ Choices at a glance

| # | Decision | Chosen | Main alternative | Trade-off accepted |
| --- | --- | --- | --- | --- |
| [D1](#d1) | Where the cloud-specific code lives | One provider module per cloud, no provider block | A provider block in each root | Credentials stay in the environment, at the cost of one extra module per cloud |
| [D2](#d2) | State backend | None declared, state ignored by git | A fixed remote backend | The operator must choose a backend, but no choice is invented |
| [D3](#d3) | Interface modules | Minimal interface, no resource | Real resources now | P2 may have to extend the inputs |
| [D4](#d4) | CI layout | Reusable `terraform.yml`, one matrix entry per folder, also called from the release | Steps inside `python.yml`, or the root folders only | Every folder is checked on any Terraform change |
| [D5](#d5) | Tests for criteria 3 and 4 | Python tests in `tests/infra/terraform/` | `terraform test` alone | A new test folder that AGENT.md does not list yet |

## <a id="d1"></a>D1: Where the cloud-specific code lives

**Chosen:** a provider module per cloud with no provider block · **Where:** [`infra/terraform/modules/clouds/ovhcloud/main.tf:1-8`](../../../infra/terraform/modules/clouds/ovhcloud/main.tf#L1-L8), [`infra/terraform/ovhcloud/versions.tf:5-10`](../../../infra/terraform/ovhcloud/versions.tf#L5-L10) · **Source:** PLAN

| Option | For | Against |
| --- | --- | --- |
| ✅ A cloud module plus the provider pin in each root | The four lines that differ between the roots are the module source and the provider entry, which a test pins down. Providers read credentials from environment variables, which meets criterion 4. | Adds a module per cloud, and the lock files and tftest files must name their cloud. |
| A provider block in each root | Familiar layout. | A provider block invites a credential or a variable for it, and the roots would differ in more than their provider module. |

**Trade-off:** the roots are not byte-identical, only identical to 4 lines. That is the reading of "differ only in their provider module" the reviewer accepted.

**Revisit when:** P2 (T2.74, T2.81) adds the real resources and a provider needs an option that environment variables cannot carry.

## <a id="d2"></a>D2: State backend

**Chosen:** no backend block, plus an ignore file · **Where:** [`infra/terraform/ovhcloud/versions.tf:4`](../../../infra/terraform/ovhcloud/versions.tf#L4), [`infra/terraform/.gitignore:1-12`](../../../infra/terraform/.gitignore#L1-L12) · **Source:** TICKET and PLAN

| Option | For | Against |
| --- | --- | --- |
| ✅ No backend, operator's choice | REQ-T09-08 and the roadmap only say "state kept outside the repository". Nothing is invented, and a test checks that no file declares a backend. | The operator must configure one before a real apply. |
| A named remote backend | State would be shared at once. | No specification names one. |

**Trade-off:** the skeleton leaves one setup step to the operator.

**Revisit when:** a specification or a P2 ticket names the state store.

## <a id="d3"></a>D3: Interface modules

**Chosen:** `cloud` and `name` for all, plus one input each (`cidr`, `network`, `domain`, `cluster`), no resource · **Where:** [`infra/terraform/modules/network/variables.tf:1-37`](../../../infra/terraform/modules/network/variables.tf#L1-L37) · **Source:** PLAN

| Option | For | Against |
| --- | --- | --- |
| ✅ A minimal interface | The specifications name the six modules but not their inputs, so nothing more can be justified. Running apply creates nothing. | P2 may have to extend or rename inputs. |
| Real resources now | Closer to a working deployment. | Out of the ticket's scope, and the specifications give no resource list. |

**Trade-off:** a thin interface now, in exchange for no guessed resources.

**Revisit when:** T2.74 and T2.81 build the resources.

## <a id="d4"></a>D4: CI layout

**Chosen:** a reusable `terraform.yml` called from `ci.yml` and `release.yml` · **Where:** [`.github/workflows/terraform.yml:19-62`](../../../.github/workflows/terraform.yml#L19-L62), [`.github/workflows/ci.yml:84-89`](../../../.github/workflows/ci.yml#L84-L89) · **Source:** PLAN

| Option | For | Against |
| --- | --- | --- |
| ✅ A reusable workflow, a matrix of folders | Matches how `python.yml` and `typescript.yml` are built. A failing folder does not hide the others (`fail-fast: false`). The release can call it (TKT-26). | A sixth detector output, and any change under `infra/terraform/` runs every folder, even [`infra/terraform/README.md`](../../../infra/terraform/README.md). |
| Only the two roots | Fewer jobs. | The modules would not be validated or tested on their own. |

**Trade-off:** more CI minutes for simple selection rules.

**Revisit when:** the folders are many enough that selecting only the changed ones saves real time. The reason for selecting everything is not recorded beyond "the modules are shared" (open point).

## <a id="d5"></a>D5: Tests for criteria 3 and 4

**Chosen:** Python tests in `tests/infra/terraform/` · **Where:** [`tests/infra/terraform/test_terraform_roots.py:39-51`](../../../tests/infra/terraform/test_terraform_roots.py#L39-L51) · **Source:** PLAN

| Option | For | Against |
| --- | --- | --- |
| ✅ A new pytest folder | Criteria 3 and 4 are about files, which pytest compares well. `pytest tests` in python.yml collects it, and a Terraform change sets `repository`. | AGENT.md does not list `tests/infra/` yet. |
| `terraform test` only | One tool. | It cannot compare two roots or scan for a literal credential. |

**Trade-off:** one folder AGENT.md does not name, accepted by the reviewer.

**Revisit when:** AGENT.md lists the folder.

## 📝 Assumptions behind the choices

- "Differ only in their provider module" means the cloud module source plus the provider pin: supports [D1](#d1).
- No backend, the operator chooses: supports [D2](#d2).
- A minimal interface, because no specification gives one: supports [D3](#d3).
- Versions pinned and the step added to the existing pipeline, also called from the release: supports [D4](#d4).
- Repository tests in `tests/infra/terraform/`: supports [D5](#d5).
