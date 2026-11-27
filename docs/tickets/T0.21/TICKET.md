# T0.21: Compose stack and its profiles

**Status:** ✅ Done

## Roadmap

- **Ticket:** [T0.21](../../specs/00-vision/roadmap/phases/01-p0-foundations.md#s04) in [🛣️ P0: Foundations](../../specs/00-vision/roadmap/phases/01-p0-foundations.md)
- **Phase:** [🛣️ P0: Foundations](../../specs/00-vision/roadmap/phases/01-p0-foundations.md)
- **Sprint:** [S04](../../specs/00-vision/roadmap/phases/01-p0-foundations.md#s04), 1 to 12 Feb 2027: Foundations ready
- **Epic:** [E0.5 Run anywhere](../../specs/00-vision/roadmap/phases/01-p0-foundations.md#epics): `compose.e2e.yaml`, the Compose profiles, the laptop check, the Helm and Terraform skeletons

## What it delivers

- `compose.e2e.yaml` at the repository root, starting the real images (`platform`, `backoffice`, PostgreSQL) for Playwright and the stages, as [CI/CD and stages](../../technical/delivery/ci-cd-and-stages.md#stages-dev-and-qa).
- The laptop and one-server Compose profiles in `infra/compose/`, built from the same images, as [Deployment](../../technical/infrastructure/deployment.md).

## Features, use cases and business rules

- [📌 REQ-T09-02](../../specs/03-technical/t09-install-backups-and-updates/requirements/req-t09-02-compose-and-helm.md): Compose and Helm are both supported, from the same images (criterion 1: one server, Compose installs it).
- [📜 D408](../../specs/06-decisions/technical/d408-performance-and-profiles.md): the laptop profile and the cloud profiles on the same images.
- [📜 D421](../../specs/06-decisions/technical/d421-infrastructure-cncf.md): fully CNCF compatible infrastructure.
- [📜 D18](../../specs/06-decisions/foundations/d18-installation.md): installation, one Docker Compose command for one company.

## Technical pages it builds on

- [🏗️ CI/CD and stages](../../technical/delivery/ci-cd-and-stages.md#stages-dev-and-qa): a stage starts its images with `compose.e2e.yaml`; `images.yml` runs Playwright against it.
- [🏗️ Deployment](../../technical/infrastructure/deployment.md): Compose for one server and the laptop profile, from the same images as Helm.

## Screens touched

- ➖ No screen: the ticket builds Compose files in `infra/compose` and at the root, and changes no front end.

## Budgets touched

- [📦 Installation](../../specs/05-non-functional/installation.md): the one-server profile starts with one Docker Compose command, from the same images as Helm.

## Acceptance criteria

1. **Given** a clean checkout and the built images, **when** `docker compose -f compose.e2e.yaml up --wait` runs in CI's images job and in `stage.yml`, **then** `platform`, `backoffice` and PostgreSQL start and are healthy. ([📌 REQ-T09-02](../../specs/03-technical/t09-install-backups-and-updates/requirements/req-t09-02-compose-and-helm.md))
2. **Given** one server, **when** the one-server profile of `infra/compose/` is started, **then** one command installs it, from the same images. ([📌 REQ-T09-02](../../specs/03-technical/t09-install-backups-and-updates/requirements/req-t09-02-compose-and-helm.md) criterion 1, [📦 Installation](../../specs/05-non-functional/installation.md))
3. **Given** the laptop profile, **when** it is started, **then** it uses the same images as the one-server profile. ([📜 D408](../../specs/06-decisions/technical/d408-performance-and-profiles.md), [📜 D421](../../specs/06-decisions/technical/d421-infrastructure-cncf.md))

## Out of scope

- The Playwright scaffold run against the stack, see [T0.22](../../specs/00-vision/roadmap/phases/01-p0-foundations.md#s04).
- The installer's machine check and the memory measure of the laptop profile, see [T0.25](../../specs/00-vision/roadmap/phases/01-p0-foundations.md#s04).
- The Helm umbrella chart, see [T0.19](../../specs/00-vision/roadmap/phases/01-p0-foundations.md#s03).
- The full install, backups and upgrades, built in P2 (T9).

## Assumptions

- The roadmap row gives no anchor for the ticket: the link uses the sprint anchor `#s04`, and the epic link uses `#epics`, as the page has no per-epic anchor.
- Criterion 3 is derived from "the laptop and one-server profiles from the same images" of the roadmap row; the specifications give no further measure for the laptop profile before T0.25.
- Criterion 1 reads "healthy" as what `up --wait` waits for; the services' health checks are the ones their own tickets deliver (T0.14, T0.17).
