# T0.24: Bruno collection scaffold

**Status:** ✅ Done

## Roadmap

- **Ticket:** [T0.24](../../specs/00-vision/roadmap/phases/01-p0-foundations.md#s04) in [🛣️ P0: Foundations](../../specs/00-vision/roadmap/phases/01-p0-foundations.md)
- **Phase:** [🛣️ P0: Foundations](../../specs/00-vision/roadmap/phases/01-p0-foundations.md)
- **Sprint:** [S04](../../specs/00-vision/roadmap/phases/01-p0-foundations.md#s04), 1 to 12 February 2027: Foundations ready
- **Epic:** [E0.4 First service and contracts](../../specs/00-vision/roadmap/phases/01-p0-foundations.md#epics): `backend/services/platform`, its image, its OpenAPI, the contract check, the typed client and the Bruno collection

## What it delivers

- `bruno/platform/`, a Bruno collection generated from the OpenAPI of `platform`, as [D406](../../specs/06-decisions/technical/d406-back-end.md) decides (the Bruno collection generated from the contract).
- Bruno tests on the health call and on one refused call, which answers problem+json with its code, as [REQ-T05-03](../../specs/03-technical/t05-api-and-webhooks/requirements/req-t05-03-problem-json.md) asks.
- No credential in any committed file of the collection (TEST-1 of [D426](../../specs/06-decisions/technical/d426-testing-strategy.md)).
- A run of the collection, headless, by `stage.yml` on dev, keeping its JUnit and JSON reports, as [CI/CD and stages](../../technical/delivery/ci-cd-and-stages.md#stages-dev-and-qa) describes.
- A CI check that fails when the committed collection is stale against the OpenAPI.

## Features, use cases and business rules

- [📌 REQ-T05-03 problem+json errors](../../specs/03-technical/t05-api-and-webhooks/requirements/req-t05-03-problem-json.md): a refused call returns a problem+json body with its code, and no secret is in an error.
- [📌 REQ-T05-01 REST with OpenAPI behind one gateway](../../specs/03-technical/t05-api-and-webhooks/requirements/req-t05-01-rest-openapi.md): the OpenAPI a service serves, which the collection is generated from.
- [📌 REQ-T05-05 Contracts tested](../../specs/03-technical/t05-api-and-webhooks/requirements/req-t05-05-contract-tests.md): contract tests run in CI and catch breaking changes.
- [📜 D406 Back end](../../specs/06-decisions/technical/d406-back-end.md): OpenAPI generated from the code, with the Bruno collection generated from it.
- [📜 D426 Testing strategy](../../specs/06-decisions/technical/d426-testing-strategy.md): the testing levels, synthetic data only.

## Technical pages it builds on

- [🏗️ Back end](../../technical/architecture/backend.md): the Bruno collection is generated from each service's OpenAPI, so that one change updates all.
- [🏗️ CI/CD and stages](../../technical/delivery/ci-cd-and-stages.md#stages-dev-and-qa): the dev stage runs the smoke test, unit tests, Bruno and Playwright `@smoke`.
- [🏗️ Tests and traceability](../../technical/delivery/tests-and-traceability.md): the API level is the Bruno collection in `bruno/`, run headless on dev and QA.
- [🏗️ API](../../technical/interfaces/api.md): each endpoint's requests are kept in the Bruno collection `bruno/`.

## Screens touched

- ➖ No screen: the ticket builds a Bruno collection, its tests and CI steps, and changes no front end.

## Budgets touched

- The ticket touches no budget: neither the roadmap row nor the specifications give it a measure of `docs/specs/05-non-functional/`.

## Acceptance criteria

1. **Given** the OpenAPI of `platform`, **when** the generator runs, **then** `bruno/platform/` holds the collection generated from it. ([📜 D406](../../specs/06-decisions/technical/d406-back-end.md))
2. **Given** the collection, **when** it runs headless against `platform`, **then** its test on the health call passes. ([📌 REQ-T05-01](../../specs/03-technical/t05-api-and-webhooks/requirements/req-t05-01-rest-openapi.md))
3. **Given** a refused call, **when** the collection runs its test on it, **then** the body is problem+json with its code and holds no secret. ([📌 REQ-T05-03](../../specs/03-technical/t05-api-and-webhooks/requirements/req-t05-03-problem-json.md))
4. **Given** the files of `bruno/`, **when** they are searched, **then** no credential is committed in any of them (TEST-1, [📜 D426](../../specs/06-decisions/technical/d426-testing-strategy.md)).
5. **Given** a run of `stage.yml` on dev, **when** it reaches the Bruno step, **then** it runs the collection headless and keeps its JUnit and JSON reports. ([CI/CD and stages](../../technical/delivery/ci-cd-and-stages.md#stages-dev-and-qa))
6. **Given** a collection that no longer matches the OpenAPI of `platform`, **when** CI runs, **then** it fails. ([📌 REQ-T05-05](../../specs/03-technical/t05-api-and-webhooks/requirements/req-t05-05-contract-tests.md))

## Out of scope

- The OpenAPI generation and its contract check, see [T0.18](../../specs/00-vision/roadmap/phases/01-p0-foundations.md#s03).
- The typed API client generated from the same document, see [T0.20](../../specs/00-vision/roadmap/phases/01-p0-foundations.md#s03).
- `compose.e2e.yaml`, which starts the real images, see [T0.21](../../specs/00-vision/roadmap/phases/01-p0-foundations.md#s04).
- The Playwright scaffold, see [T0.22](../../specs/00-vision/roadmap/phases/01-p0-foundations.md#s04).
- The collections of the other services, which come with their own tickets in later phases.

## Assumptions

- TEST-1 is cited by the roadmap row and by D426 ("TEST-1 to TEST-9 apply") but no page of `docs/specs/` or `docs/technical/` defines it; the ticket reads it as the roadmap row does, no credential in a committed file, and takes the most conservative form (no secret, token or password value anywhere in `bruno/`).
- The roadmap row gives `stage.yml` as the runner and names no Bruno CLI; the choice of tool to run headless and to write the reports is left to the plan.
- `tests-and-traceability.md` marks `bruno/` as "to come": the collection is created by this ticket.
- The ticket anchor of the roadmap link is the sprint anchor `s04`, because the row has no anchor of its own.
