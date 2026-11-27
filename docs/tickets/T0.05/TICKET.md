# T0.05: Lifecycle and factories library

**Status:** ✅ Done

## Roadmap

- **Ticket:** [T0.05](../../specs/00-vision/roadmap/phases/01-p0-foundations.md#s01) in [🛣️ P0: Foundations](../../specs/00-vision/roadmap/phases/01-p0-foundations.md)
- **Phase:** [🛣️ P0: Foundations](../../specs/00-vision/roadmap/phases/01-p0-foundations.md)
- **Sprint:** [S01](../../specs/00-vision/roadmap/phases/01-p0-foundations.md#s01), 7 to 18 Dec 2026: The layout, its rules and the first shared code
- **Epic:** [E0.3 Service kit](../../specs/00-vision/roadmap/phases/01-p0-foundations.md#epics): The libraries of Back end: lifecycle, logging, configuration, company context and rights, outbox, metering client, country-pack rules, test helpers

## What it delivers

- `Runnable` and `AsyncRunnable`, with `initialize`, `run`, `close` and `execute`, in `backend/shared/lifecycle`, as the lifecycle of [Architecture](../../technical/architecture/architecture.md): every runnable class has the `initialize()`, `run()`, `close()` lifecycle.
- The abstract factory base of AGENT.md ("Lifecycle and factories"), in `backend/shared/lifecycle`, as the service kit of [Back end](../../technical/architecture/backend.md): a kit with no business rules, holding the lifecycle base classes.

## Features, use cases and business rules

- [📜 D406 Back end](../../specs/06-decisions/technical/d406-back-end.md): the back-end decision that sets the service kit.
- [📜 D438 Repository layout](../../specs/06-decisions/technical/d438-repository-layout.md): `backend/shared/<lib>` holds the libraries the services share.

## Technical pages it builds on

- [🏗️ Architecture](../../technical/architecture/architecture.md): "Every runnable class has the `initialize()`, `run()`, `close()` lifecycle and is built by a factory".
- [🏗️ Back end](../../technical/architecture/backend.md): the shared code is a service kit with no business rules, with the lifecycle base classes first.
- [🏗️ Repository layout](../../technical/architecture/repository-layout.md): `shared/` holds the libraries imported by the services, lifecycle among them.

## Screens touched

- ➖ No screen: a Python library of `backend/shared/lifecycle`, with no front end.

## Budgets touched

- The ticket touches no budget.

## Acceptance criteria

1. **Given** a `Runnable` whose `initialize()` fails, **when** `execute()` runs, **then** `close()` is still called. ([📜 D406](../../specs/06-decisions/technical/d406-back-end.md))
2. **Given** an `AsyncRunnable` whose `initialize()` fails, **when** `execute()` is awaited, **then** `close()` is still called. ([📜 D406](../../specs/06-decisions/technical/d406-back-end.md))
3. **Given** a class that subclasses `Runnable` or `AsyncRunnable`, **when** the convention test that requires a lifecycle base for a class with `run` runs, **then** it accepts the class. ([📜 D438](../../specs/06-decisions/technical/d438-repository-layout.md))
4. **Given** the abstract factory base, **when** a concrete factory builds a runnable, **then** the runnable is created by the factory and not by a direct constructor call. ([📜 D406](../../specs/06-decisions/technical/d406-back-end.md))
5. **Given** the library, **when** its tests, ruff and mypy run, **then** they pass.

## Out of scope

- Logging and configuration, see [T0.06](../../specs/00-vision/roadmap/phases/01-p0-foundations.md#s01).
- The first service and its factories, see [T0.14](../../specs/00-vision/roadmap/phases/01-p0-foundations.md#s02).

## Assumptions

- The roadmap gives no use case, business rule or requirement for this ticket: the specifications that settle it are decisions D406 and D438 and the design pages above, so the criteria come from the roadmap's "done when" and AGENT.md.
- Criteria 2 and 4 are taken from AGENT.md ("Lifecycle and factories"), which says `execute()` closes whatever happens and runnables are created by factories.
- The roadmap rows carry no ticket anchor, so the links use the sprint anchor `#s01` and the epic table anchor `#epics`.
- The folder `backend/shared/lifecycle` is the name confirmed in the phase page (D572).
