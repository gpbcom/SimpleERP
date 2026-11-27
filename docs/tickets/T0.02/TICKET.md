# T0.02: Conventions for the shared libraries and the front ends

**Status:** ✅ Done

## Roadmap

- **Ticket:** [T0.02](../../specs/00-vision/roadmap/phases/01-p0-foundations.md#s01) in [🛣️ P0: Foundations](../../specs/00-vision/roadmap/phases/01-p0-foundations.md)
- **Phase:** [🛣️ P0: Foundations](../../specs/00-vision/roadmap/phases/01-p0-foundations.md)
- **Sprint:** [S01](../../specs/00-vision/roadmap/phases/01-p0-foundations.md#s01), 7 to 18 December 2026: The layout, its rules and the first shared code
- **Epic:** [E0.1 Layout and conventions](../../specs/00-vision/roadmap/phases/01-p0-foundations.md#epics): the folders and workspaces of D438; the convention tests and front-end lint rules extended to them

## What it delivers

- `tests/conventions/` extended to the D438 rules a test can enforce: `erp_models` imports no library or service, `backend/shared` imports `erp_models` and other libraries but never a service, `plugins/` and `sdk/` import only `erp_models`, as [Repository layout](../../technical/architecture/repository-layout.md).
- The front ends' shared eslint and strict TypeScript settings in `frontend/packages/config`, as [D407](../../specs/06-decisions/technical/d407-front-end.md).
- A deliberately broken fixture that fails each new rule once.

## Features, use cases and business rules

- [📜 D438 Repository layout](../../specs/06-decisions/technical/d438-repository-layout.md): "AGENT.md and the conventions tests follow in a harness ticket".
- [📜 D407 Front end](../../specs/06-decisions/technical/d407-front-end.md): Vue 3 with TypeScript, the front ends the shared settings apply to.

## Technical pages it builds on

- [🏗️ Repository layout](../../technical/architecture/repository-layout.md): the rules on `backend/models/`, `backend/shared/`, `plugins/` and `sdk/` imports, and the conventions tests of `tests/conventions/` that follow the layout.

## Screens touched

- ➖ No screen: the ticket adds convention tests and the shared lint and TypeScript settings of `frontend/packages/config`, and builds no screen.

## Budgets touched

- The ticket touches no budget.

## Acceptance criteria

1. **Given** a deliberately broken fixture in `erp_models` that imports a library or a service, **when** the conventions run, **then** the rule fails once for it. ([📜 D438](../../specs/06-decisions/technical/d438-repository-layout.md))
2. **Given** a deliberately broken fixture in `backend/shared` that imports a service, **when** the conventions run, **then** the rule fails once for it. ([📜 D438](../../specs/06-decisions/technical/d438-repository-layout.md))
3. **Given** a deliberately broken fixture in `plugins/` or `sdk/` that imports anything but `erp_models`, **when** the conventions run, **then** the rule fails once for it. ([📜 D438](../../specs/06-decisions/technical/d438-repository-layout.md))
4. **Given** an empty library or front-end package is added, **when** the conventions run, **then** no change to the tests is needed. ([📜 D438](../../specs/06-decisions/technical/d438-repository-layout.md))
5. **Given** the shared eslint and strict TypeScript settings of `frontend/packages/config`, **when** a front end uses them, **then** they apply to it. ([📜 D407](../../specs/06-decisions/technical/d407-front-end.md))

## Out of scope

- The folders, uv members and pnpm workspace, see [T0.01](../../specs/00-vision/roadmap/phases/01-p0-foundations.md#s01).
- The shared base model and enums, see [T0.03](../../specs/00-vision/roadmap/phases/01-p0-foundations.md#s01).

## Assumptions

- The roadmap row has no anchor of its own, so the ticket links to the sprint anchor `#s01`.
- The criteria are derived from the roadmap row's "Done when" and "Delivers" text, as no use case or business rule applies.
