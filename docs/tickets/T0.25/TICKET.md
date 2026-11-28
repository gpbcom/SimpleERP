# T0.25: Laptop profile check and memory measure

**Status:** ✅ Done

## Roadmap

- **Ticket:** [T0.25](../../specs/00-vision/roadmap/phases/01-p0-foundations.md#s04) in [🛣️ P0: Foundations](../../specs/00-vision/roadmap/phases/01-p0-foundations.md)
- **Phase:** [🛣️ P0: Foundations](../../specs/00-vision/roadmap/phases/01-p0-foundations.md)
- **Sprint:** [S04](../../specs/00-vision/roadmap/phases/01-p0-foundations.md#s04), 1 to 12 February 2027: end to end
- **Epic:** [E0.5 Run anywhere](../../specs/00-vision/roadmap/phases/01-p0-foundations.md#epics): `compose.e2e.yaml`, the Compose profiles, the laptop check, the Helm and Terraform skeletons

## What it delivers

- The installer's machine check (memory, cores, disk against the 8 GB budget), in `infra/compose`, as [REQ-T09-03](../../specs/03-technical/t09-install-backups-and-updates/requirements/req-t09-03-laptop-profile.md) states: "the installer checks the machine".
- A measure of the memory at rest of the P0 stack on the laptop profile, written with its date to [Performance and capacity](../../technical/infrastructure/performance-and-capacity.md).
- Milvus left out of the laptop profile when the AI is off, as [REQ-T08-01](../../specs/03-technical/t08-rag-platform/requirements/req-t08-01-milvus-collections.md) and [D22](../../specs/06-decisions/foundations/d22-no-graphics-card-needed.md) state.

## Features, use cases and business rules

- [📌 REQ-T09-03: The laptop profile within 8 GB](../../specs/03-technical/t09-install-backups-and-updates/requirements/req-t09-03-laptop-profile.md)
- [📌 REQ-T08-01: Milvus collections](../../specs/03-technical/t08-rag-platform/requirements/req-t08-01-milvus-collections.md)
- [📜 D408: Performance targets and resource profiles](../../specs/06-decisions/technical/d408-performance-and-profiles.md)
- [📜 D22: No graphics card needed](../../specs/06-decisions/foundations/d22-no-graphics-card-needed.md)

## Technical pages it builds on

- [🏗️ Performance and capacity](../../technical/infrastructure/performance-and-capacity.md): the laptop profile "within 8 GB of RAM and 4 cores at normal load, to be proved by a measured prototype before it is promised"; the page receives the measure.
- [📌 REQ-T09-02: Compose and Helm everywhere](../../specs/03-technical/t09-install-backups-and-updates/requirements/req-t09-02-compose-and-helm.md): the Compose profiles of T0.21 that the check and the measure run on.

## Screens touched

- ➖ No screen: the ticket changes `infra/compose` and a design page, no front end.

## Budgets touched

- [📦 Installation](../../specs/05-non-functional/installation.md): the laptop profile within 8 GB of RAM, proved by a measured prototype.

## Acceptance criteria

1. **Given** a machine under the budget, **when** the installer checks it, **then** it installs. ([📌 REQ-T09-03](../../specs/03-technical/t09-install-backups-and-updates/requirements/req-t09-03-laptop-profile.md), criterion 1, with a simulated machine)
2. **Given** a machine too small, **when** the installer checks it, **then** it tells so. ([📌 REQ-T09-03](../../specs/03-technical/t09-install-backups-and-updates/requirements/req-t09-03-laptop-profile.md), criterion 2, with a simulated machine)
3. **Given** the P0 stack on the laptop profile, **when** it is at rest, **then** its measured memory is recorded with its date in [Performance and capacity](../../technical/infrastructure/performance-and-capacity.md).
4. **Given** the AI is off, **when** the laptop profile starts, **then** Milvus is not installed. ([📌 REQ-T08-01](../../specs/03-technical/t08-rag-platform/requirements/req-t08-01-milvus-collections.md), [📜 D22](../../specs/06-decisions/foundations/d22-no-graphics-card-needed.md))

## Out of scope

- The 8 GB promise itself: it waits for the whole stack in P2, see [P0 risks](../../specs/00-vision/roadmap/phases/01-p0-foundations.md#risks).
- The Compose stack and its profiles, see [T0.21](../../specs/00-vision/roadmap/phases/01-p0-foundations.md#s04).

## Assumptions

- The roadmap row cites no check for the "cores" and "disk" thresholds; none is stated in the specifications, so the thresholds are left to the plan and recorded there as assumptions.
- The roadmap and D408 give 8 GB of RAM and, in the design page, 4 cores at normal load; no disk size is specified.
