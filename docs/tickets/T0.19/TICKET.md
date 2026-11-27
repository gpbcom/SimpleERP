# T0.19: Helm umbrella chart skeleton

**Status:** ✅ Done

## Roadmap

- **Ticket:** [T0.19](../../specs/00-vision/roadmap/phases/01-p0-foundations.md#s03) in [🛣️ P0: Foundations](../../specs/00-vision/roadmap/phases/01-p0-foundations.md)
- **Phase:** [🛣️ P0: Foundations](../../specs/00-vision/roadmap/phases/01-p0-foundations.md)
- **Sprint:** [S03](../../specs/00-vision/roadmap/phases/01-p0-foundations.md#s03), 18 to 29 January 2027: The contracts and the shell
- **Epic:** [E0.5 Run anywhere](../../specs/00-vision/roadmap/phases/01-p0-foundations.md#epics): `compose.e2e.yaml`, the Compose profiles, the laptop check, the Helm and Terraform skeletons

## What it delivers

- In `infra/helm`, an umbrella chart and one chart per image (`platform`, `backoffice`), as [Deployment](../../technical/infrastructure/deployment.md): Helm for every Kubernetes, with the same images as Compose.
- Values with every default written out, the image tag taken from the commit, and no secret in values.
- A CI check where `helm lint` and `helm template` pass and the rendered manifests validate against the Kubernetes schemas.

## Features, use cases and business rules

- [📌 REQ-T09-02: Compose and Helm everywhere](../../specs/03-technical/t09-install-backups-and-updates/requirements/req-t09-02-compose-and-helm.md): "Given a cluster, Helm installs it", from the same images as Compose.
- [📜 D421: Infrastructure: fully CNCF compatible](../../specs/06-decisions/technical/d421-infrastructure-cncf.md): "Compose and Helm supported everywhere".
- [📜 D438: Repository layout](../../specs/06-decisions/technical/d438-repository-layout.md): "infra/ for Compose, Helm and Terraform".

## Technical pages it builds on

- [Deployment](../../technical/infrastructure/deployment.md): Compose for one server and the laptop profile, Helm for every Kubernetes, with the same images.
- [Repository layout](../../technical/architecture/repository-layout.md): `helm/` holds "an umbrella chart and a chart per service".

## Screens touched

- ➖ No screen: the ticket adds Helm charts under `infra/helm` and changes no front end.

## Budgets touched

- The ticket touches no budget: the [Installation](../../specs/05-non-functional/installation.md) page has its measures still to be specified.

## Acceptance criteria

1. **Given** the charts of `infra/helm`, **when** `helm lint` runs in CI, **then** it passes. ([📌 REQ-T09-02](../../specs/03-technical/t09-install-backups-and-updates/requirements/req-t09-02-compose-and-helm.md))
2. **Given** the umbrella chart and its values, **when** `helm template` runs in CI, **then** it renders and the manifests validate against the Kubernetes schemas. ([📌 REQ-T09-02](../../specs/03-technical/t09-install-backups-and-updates/requirements/req-t09-02-compose-and-helm.md))
3. **Given** the umbrella chart, **when** its charts are read, **then** there is one chart per image, `platform` and `backoffice`, and they use the same images as Compose. ([📌 REQ-T09-02](../../specs/03-technical/t09-install-backups-and-updates/requirements/req-t09-02-compose-and-helm.md))
4. **Given** the values files, **when** they are read, **then** every default is written out, the image tag comes from the commit and no secret is in them. ([📜 D421](../../specs/06-decisions/technical/d421-infrastructure-cncf.md))

## Out of scope

- The Terraform modules, see [T0.08](../../specs/00-vision/roadmap/phases/01-p0-foundations.md#s01).
- The Compose stack and its profiles, see [T0.21](../../specs/00-vision/roadmap/phases/01-p0-foundations.md#s04).
- The other services' charts, which come with the phases that build them.

## Assumptions

- The roadmap anchors only sprints, so the ticket links point to the sprint and epic sections of the phase page.
- The Installation page's measures are "To be specified", so no budget is taken from it.
- Charts for services other than `platform` and `backoffice` are not part of this ticket, as the roadmap row names only these two.
- The roadmap row names no business rule, use case or entity, so the requirement and decisions above are the specification this ticket builds on.
