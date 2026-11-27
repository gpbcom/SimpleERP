# T0.13: Test helpers library

**Status:** ✅ Done

## Roadmap

- **Ticket:** [T0.13](../../specs/00-vision/roadmap/phases/01-p0-foundations.md#s02) in [🛣️ P0: Foundations](../../specs/00-vision/roadmap/phases/01-p0-foundations.md)
- **Phase:** [🛣️ P0: Foundations](../../specs/00-vision/roadmap/phases/01-p0-foundations.md)
- **Sprint:** [S02](../../specs/00-vision/roadmap/phases/01-p0-foundations.md#s02), 4 to 15 January 2027: the service kit and the first service
- **Epic:** [E0.3 Service kit](../../specs/00-vision/roadmap/phases/01-p0-foundations.md#epics): the libraries of the back end (lifecycle, logging, configuration, company context and rights, outbox, metering client, country-pack rules, test helpers), one library per agent, each with its own folder, tests and pyproject

## What it delivers

- The test helpers library in `backend/shared/testing`, with no business rules, as [Back end, shared code](../../technical/architecture/backend.md#target-design-specified-in-gh-2-not-built-yet): "test helpers" are part of the service kit.
- A local HTTP stand-in server.
- A PostgreSQL test server started per session.
- A company-context fixture.
- Log capture.
- Synthetic data builders, and no mock library, as [Tests and traceability](../../technical/delivery/tests-and-traceability.md#target-design-specified-in-gh-2-not-built-yet): "Only synthetic data", and tests use real stand-ins rather than mocks.
- The kit's own tests use these helpers.

## Features, use cases and business rules

- [📜 D426 Testing strategy](../../specs/06-decisions/technical/d426-testing-strategy.md): synthetic data, seeded by sector, and full coverage of errors and edge cases.
- [📜 D438 Repository layout](../../specs/06-decisions/technical/d438-repository-layout.md): `backend/shared/<lib>` holds the libraries the services share, with no business rules.

## Technical pages it builds on

- [🏗️ Tests and traceability](../../technical/delivery/tests-and-traceability.md): "they use real stand-ins rather than mocks (a local server, a git sandbox, a fake executable)", and "Only synthetic data ... never production data in tests".
- [🏗️ Back end](../../technical/architecture/backend.md): the shared code is "a service kit with no business rules", test helpers included.
- [🏗️ Repository layout](../../technical/architecture/repository-layout.md): the place of `backend/shared` and its test helpers.

## Screens touched

- ➖ No screen: the ticket builds a Python library under `backend/shared/testing` and changes no front end.

## Budgets touched

- The ticket touches no budget.

## Acceptance criteria

1. **Given** the library `backend/shared/testing`, **when** its own tests run, **then** they use its helpers: the local HTTP stand-in server, the PostgreSQL test server started per session, the company-context fixture, log capture and the synthetic data builders. ([📜 D426](../../specs/06-decisions/technical/d426-testing-strategy.md))
2. **Given** a stand-in server with no answer configured, **when** it is called, **then** its default answer is a valid empty value of the real model (TEST-2). ([📜 D426](../../specs/06-decisions/technical/d426-testing-strategy.md))
3. **Given** every fixture and builder of the library, **when** they are read, **then** none holds production data: all data is synthetic. ([📜 D426](../../specs/06-decisions/technical/d426-testing-strategy.md))
4. **Given** the library, **when** its dependencies are read, **then** it uses no mock library. ([🏗️ Tests and traceability](../../technical/delivery/tests-and-traceability.md))
5. **Given** the repository, **when** `tests/conventions/` runs, **then** the new library passes with no change to the conventions. ([📜 D438](../../specs/06-decisions/technical/d438-repository-layout.md))

## Out of scope

- The company context and rights middleware that the company-context fixture stands for, see [T0.09](../../specs/00-vision/roadmap/phases/01-p0-foundations.md#s02).
- The Playwright scaffold, see [S04](../../specs/00-vision/roadmap/phases/01-p0-foundations.md#s04).
- The Bruno collection, see [S04](../../specs/00-vision/roadmap/phases/01-p0-foundations.md#s04).
- The platform service that will use the helpers, see [T0.14](../../specs/00-vision/roadmap/phases/01-p0-foundations.md#s02).

## Assumptions

- TEST-2 is cited by the roadmap row but no page of `docs/specs/` defines it; its wording is taken from the row: a stand-in's default answer is a valid empty value of the real model.
- The ticket graph gives T0.13 the prerequisite T0.09 (area `backend/shared/testing`); the roadmap row does not say why, so the company-context fixture is assumed to build on T0.09's company context.
- No page of `docs/specs/03-technical/` or `05-non-functional/` gives this ticket a requirement or a measure, so none is linked.
- The ticket rows of the phase page have no anchor of their own, so the sprint and epic anchors (`#s02`, `#epics`) are used.
