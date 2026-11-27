# T0.01: Mono-repo folders and workspaces

**Status:** ✅ Done

## Roadmap

- **Ticket:** [T0.01](../../specs/00-vision/roadmap/phases/01-p0-foundations.md#s01) in [🛣️ P0: Foundations](../../specs/00-vision/roadmap/phases/01-p0-foundations.md)
- **Phase:** [🛣️ P0: Foundations](../../specs/00-vision/roadmap/phases/01-p0-foundations.md)
- **Sprint:** [S01](../../specs/00-vision/roadmap/phases/01-p0-foundations.md#s01), 7 to 18 December 2026: The layout, its rules and the first shared code.
- **Epic:** [E0.1 Layout and conventions](../../specs/00-vision/roadmap/phases/01-p0-foundations.md#epics): The folders and workspaces of D438; the convention tests and front-end lint rules extended to them (T0.01 and T0.02).

## What it delivers

- Every folder of the D438 layout, each with a README saying what it holds, as [Repository layout](../../technical/architecture/repository-layout.md): `backend/models`, `backend/shared`, `backend/services`, `frontend/backoffice`, `frontend/mobile`, `frontend/packages`, `plugins`, `sdk`, `infra/compose`, `infra/helm`, `infra/terraform`, `packs/countries`, `packs/sectors`.
- The uv workspace members (Python 3.13), as [D406 Back end](../../specs/06-decisions/technical/d406-back-end.md) and the "Mono-repo" section of AGENT.md.
- The pnpm workspace (`package.json`, `pnpm-workspace.yaml`, `pnpm-lock.yaml`, Node 22), as [D407 Front end](../../specs/06-decisions/technical/d407-front-end.md).
- [Configuration](../../technical/architecture/configuration.md) and the README updated.

## Features, use cases and business rules

- [📜 D438 Repository layout](../../specs/06-decisions/technical/d438-repository-layout.md): the mono-repo with the back end and the front end apart, shared models under `backend/models/`, libraries under `backend/shared/`, `plugins/` and `sdk/` separate, `infra/` for Compose, Helm and Terraform.
- [📜 D406 Back end](../../specs/06-decisions/technical/d406-back-end.md)
- [📜 D407 Front end](../../specs/06-decisions/technical/d407-front-end.md)
- [📜 D415 Supply chain controls](../../specs/06-decisions/technical/d415-supply-chain-controls.md): both locks pinned.

## Technical pages it builds on

- [🏗️ Repository layout](../../technical/architecture/repository-layout.md): the target tree of folders and the rules between them; its "first tickets of phase P0 create its folders".
- [🏗️ Configuration](../../technical/architecture/configuration.md): updated by this ticket, as the roadmap row says.
- [🏗️ Supply chain and licences](../../technical/security/supply-chain-and-licences.md): pinned dependencies in both locks.

## Screens touched

- ➖ No screen: the ticket creates empty folders, workspaces and READMEs, and builds no screen of `frontend/backoffice` or `frontend/mobile`.

## Budgets touched

- The ticket touches no budget.

## Acceptance criteria

1. **Given** a clean clone, **when** `uv sync --locked` runs, **then** it passes with the workspace members pinned in one `uv.lock`. ([📜 D415](../../specs/06-decisions/technical/d415-supply-chain-controls.md))
2. **Given** a clean clone, **when** `pnpm install --frozen-lockfile` runs, **then** it passes with `pnpm-lock.yaml` pinned. ([📜 D415](../../specs/06-decisions/technical/d415-supply-chain-controls.md))
3. **Given** the new folders, **when** CI's change detection runs, **then** it lists them. ([📜 D438](../../specs/06-decisions/technical/d438-repository-layout.md))
4. **Given** every folder of the D438 layout, **when** it is opened, **then** it has a README saying what it holds. ([📜 D438](../../specs/06-decisions/technical/d438-repository-layout.md))
5. **Given** the README, **when** its quick start is followed, **then** it works.

## Out of scope

- The convention tests and the front-end lint settings for the new packages, see [T0.02](../../specs/00-vision/roadmap/phases/01-p0-foundations.md#s01).
- The shared models and enums, see [T0.03](../../specs/00-vision/roadmap/phases/01-p0-foundations.md#s01).

## Assumptions

- The roadmap row names no use case, business rule, entity, flow or requirement for this ticket: the decisions D438, D406, D407 and D415 and the design pages above settle what it builds.
- The roadmap row names no budget, so none is listed.
- The pages `docs/technical/architecture/configuration.md` and the README are only said to be "updated"; what changes in them is not stated, so only what the new layout requires is changed.
- The folders of `backend/shared/` libraries and `frontend/packages/` are named by later tickets; this ticket creates their parent folders only.
