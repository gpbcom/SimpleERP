# T0.10: Event outbox library

**Status:** ✅ Done

## Roadmap

- **Ticket:** [T0.10](../../specs/00-vision/roadmap/phases/01-p0-foundations.md#s02) in [🛣️ P0: Foundations](../../specs/00-vision/roadmap/phases/01-p0-foundations.md)
- **Phase:** [🛣️ P0: Foundations](../../specs/00-vision/roadmap/phases/01-p0-foundations.md)
- **Sprint:** [S02](../../specs/00-vision/roadmap/phases/01-p0-foundations.md#s02), 4 to 15 January 2027: the service kit and the first service
- **Epic:** [E0.3 Service kit](../../specs/00-vision/roadmap/phases/01-p0-foundations.md#epics): the libraries of the back-end design page: lifecycle, logging, configuration, company context and rights, outbox, metering client, country-pack rules, test helpers, in `backend/shared/<lib>`, with no business rules

## What it delivers

- The outbox library in `backend/shared/outbox`: an event written in the same transaction as the change, as [Architecture](../../technical/architecture/architecture.md) ("Messaging") describes it: "fed through an outbox in each service so that no event is lost".
- A relay that publishes each event at least once behind a publisher interface, with a test publisher that stands in for the event bus, which is chosen in P2.
- An event envelope in `erp_models` (`backend/models`), the public contract of an event, as the shared models of [Repository layout](../../technical/architecture/repository-layout.md).
- A library that the audit writer of [I-T03-01](../../specs/03-technical/t03-audit-trail/interfaces/i-t03-01-audit-writer.md) will use ("Every service appends entries through its event outbox"); the audit writer itself is not built here.

## Features, use cases and business rules

- [📜 D405 Architecture and scalability](../../specs/06-decisions/technical/d405-architecture-and-scalability.md): "HTTP for reads and commands and an event bus with an outbox for what happened".
- [📜 D406 Back end](../../specs/06-decisions/technical/d406-back-end.md): "`packages/` as a service kit without business rules", which the outbox library is part of (see [Back end](../../technical/architecture/backend.md)).
- [📜 D438 Repository layout](../../specs/06-decisions/technical/d438-repository-layout.md): the library lives in `backend/shared/<lib>` and the envelope in `backend/models`.
- [📜 D426 Testing strategy](../../specs/06-decisions/technical/d426-testing-strategy.md): the testing strategy the library's tests follow, with a test publisher standing in for the bus (roadmap row).
- [🔌 I-T03-01 Audit writer](../../specs/03-technical/t03-audit-trail/interfaces/i-t03-01-audit-writer.md): the later user of the outbox.

## Technical pages it builds on

- [🏗️ Architecture](../../technical/architecture/architecture.md): the outbox per service that feeds the event bus, so that no event is lost.
- [🏗️ Back end](../../technical/architecture/backend.md): the service kit of `backend/shared/` that lists the event outbox, with no business rules.
- [🏗️ Repository layout](../../technical/architecture/repository-layout.md): where `backend/shared/` and `backend/models/` sit, and what they may import.
- [🏗️ Tests and traceability](../../technical/delivery/tests-and-traceability.md): the way the library's tests are written.

## Screens touched

- ➖ No screen: a back-end library with no front end.

## Budgets touched

- The roadmap row and the specifications give this ticket no non-functional measure, so it touches no budget.

## Acceptance criteria

1. **Given** an event written with a change and the process stopped before it was published, **when** the process restarts, **then** the event is published. ([📜 D405](../../specs/06-decisions/technical/d405-architecture-and-scalability.md))
2. **Given** a change that is rolled back, **when** the relay runs, **then** nothing is published for it. ([📜 D405](../../specs/06-decisions/technical/d405-architecture-and-scalability.md))
3. **Given** a test publisher in place of the bus, **when** the relay runs, **then** it publishes every written event at least once through the publisher interface. ([📜 D405](../../specs/06-decisions/technical/d405-architecture-and-scalability.md))
4. **Given** the library and the envelope, **when** the conventions tests of `tests/conventions/` run, **then** they pass: the library imports `erp_models` and no service, and the envelope is a model of `backend/models`. ([📜 D438](../../specs/06-decisions/technical/d438-repository-layout.md))
5. **Given** the library's own tests, **when** they run, **then** they pass, with no mock library. ([📜 D426](../../specs/06-decisions/technical/d426-testing-strategy.md))

## Out of scope

- The event bus itself, chosen in P2 (Phase P0 "Out of scope"), see [P0: Foundations](../../specs/00-vision/roadmap/phases/01-p0-foundations.md#scope).
- The audit writer that uses the outbox, see [I-T03-01](../../specs/03-technical/t03-audit-trail/interfaces/i-t03-01-audit-writer.md).
- The metering client that emits its usage event through the outbox, see [T0.11](../../specs/00-vision/roadmap/phases/01-p0-foundations.md#s02).

## Assumptions

- The roadmap does not say which storage holds the outbox table. The library takes the transaction of the caller's storage layer behind an interface, and the PostgreSQL test server of T0.13 is not a prerequisite named by the roadmap; the plan decides the test storage.
- The folder name `backend/shared/outbox` is the one the roadmap row gives ("Where"), confirmed as D572 in the epics section of the phase page.
- The roadmap states no retry, ordering or event size rule; none is built beyond "at least once".
