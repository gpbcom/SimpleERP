# T0.08: Terraform module skeletons

**Status:** ✅ Done

## Roadmap

- **Ticket:** [T0.08](../../specs/00-vision/roadmap/phases/01-p0-foundations.md#s01) in [🛣️ P0: Foundations](../../specs/00-vision/roadmap/phases/01-p0-foundations.md)
- **Phase:** [🛣️ P0: Foundations](../../specs/00-vision/roadmap/phases/01-p0-foundations.md)
- **Sprint:** [S01](../../specs/00-vision/roadmap/phases/01-p0-foundations.md#s01), 7 to 18 December 2026: The layout, its rules and the first shared code
- **Epic:** [E0.5 Run anywhere](../../specs/00-vision/roadmap/phases/01-p0-foundations.md#epics): `compose.e2e.yaml`, the Compose profiles, the laptop check, the Helm and Terraform skeletons

## What it delivers

- `infra/terraform/modules/` with the modules network, Kubernetes cluster, storage, registry, DNS and Helm release, behind one interface, as [Infrastructure deployment](../../technical/infrastructure/infrastructure.md) ("Terraform modules per cloud behind one interface").
- The roots `infra/terraform/ovhcloud/` and `infra/terraform/scaleway/` calling those modules, as [Repository layout](../../technical/architecture/repository-layout.md) ("modules/, ovhcloud/ and scaleway/").
- Terraform state kept outside the repository, and no credential in any file.
- `terraform fmt -check` and `terraform validate` on both roots in CI.

## Features, use cases and business rules

- [📌 REQ-T09-08: A Terraform project for OVHcloud and Scaleway](../../specs/03-technical/t09-install-backups-and-updates/requirements/req-t09-08-terraform-ovhcloud-scaleway.md): "network, managed Kubernetes, storage, registry, DNS and the Helm release"; P0 builds the skeleton, P2 (T9) closes it.
- [📜 D421: Infrastructure: fully CNCF compatible](../../specs/06-decisions/technical/d421-infrastructure-cncf.md): works on managed Kubernetes of European clouds, a cloud's managed services optional by configuration, never required.
- [📜 D438: Repository layout](../../specs/06-decisions/technical/d438-repository-layout.md): `infra/terraform` is part of the layout.

## Technical pages it builds on

- [🏗️ Infrastructure deployment](../../technical/infrastructure/infrastructure.md): "Terraform modules per cloud behind one interface".
- [🏗️ Repository layout](../../technical/architecture/repository-layout.md): `terraform/` holds `modules/`, `ovhcloud/` and `scaleway/`.

## Screens touched

- ➖ No screen: the ticket adds infrastructure code only and changes no front end.

## Budgets touched

- The ticket touches no budget.

## Acceptance criteria

1. **Given** the root `infra/terraform/ovhcloud`, **when** `terraform fmt -check` and `terraform validate` run in CI, **then** both pass. ([📌 REQ-T09-08](../../specs/03-technical/t09-install-backups-and-updates/requirements/req-t09-08-terraform-ovhcloud-scaleway.md))
2. **Given** the root `infra/terraform/scaleway`, **when** `terraform fmt -check` and `terraform validate` run in CI, **then** both pass. ([📌 REQ-T09-08](../../specs/03-technical/t09-install-backups-and-updates/requirements/req-t09-08-terraform-ovhcloud-scaleway.md))
3. **Given** the two roots, **when** they are compared, **then** they differ only in their provider module and both call the same modules network, Kubernetes cluster, storage, registry, DNS and Helm release behind one interface. ([📜 D421](../../specs/06-decisions/technical/d421-infrastructure-cncf.md))
4. **Given** the repository, **when** its files are searched, **then** no credential is in a file and the Terraform state is kept outside the repository. ([📌 REQ-T09-08](../../specs/03-technical/t09-install-backups-and-updates/requirements/req-t09-08-terraform-ovhcloud-scaleway.md))

## Out of scope

- A fully working deployment from an empty account to a signed-in company, and its apply on each release, see [P0: Foundations](../../specs/00-vision/roadmap/phases/01-p0-foundations.md#scope) (closed in P2, T9).
- The Helm umbrella chart skeleton, see [T0.19](../../specs/00-vision/roadmap/phases/01-p0-foundations.md#s03).
- The Compose stack and its profiles, see [T0.21](../../specs/00-vision/roadmap/phases/01-p0-foundations.md#s04).

## Assumptions

- The roadmap row names no tool version and no CI job layout; the CI step is added to the existing pipeline of `.github/` and the Terraform and provider versions are pinned, as D415 asks of dependencies.
- The roadmap row does not name where state is kept; the skeleton declares no state backend inside the repository and leaves its choice to the operator.
- The roadmap anchors no ticket row, so the ticket link points to the sprint section S01.
- "Differ only in their provider module" is read as: each root selects its cloud's provider module and nothing else.
