# T0.18: OpenAPI generation and contract check

**Status:** ✅ Done

## Roadmap

- **Ticket:** [T0.18](../../specs/00-vision/roadmap/phases/01-p0-foundations.md#s03) in [🛣️ P0: Foundations](../../specs/00-vision/roadmap/phases/01-p0-foundations.md)
- **Phase:** [🛣️ P0: Foundations](../../specs/00-vision/roadmap/phases/01-p0-foundations.md)
- **Sprint:** [S03](../../specs/00-vision/roadmap/phases/01-p0-foundations.md#s03), 18 to 29 Jan 2027: The contracts and the shell
- **Epic:** [E0.4 First service and contracts](../../specs/00-vision/roadmap/phases/01-p0-foundations.md#epics): `backend/services/platform`, its image, its OpenAPI, the contract check, the typed client and the Bruno collection

## What it delivers

- The OpenAPI document of `platform` generated from its code and served by it, committed to the repository, as [REQ-T05-01](../../specs/03-technical/t05-api-and-webhooks/requirements/req-t05-01-rest-openapi.md) criterion 1 and [I-T05-02](../../specs/03-technical/t05-api-and-webhooks/interfaces/i-t05-02-openapi-registry.md) ask.
- A CI check that fails when the committed document is stale or when a change breaks it, as [REQ-T05-05](../../specs/03-technical/t05-api-and-webhooks/requirements/req-t05-05-contract-tests.md) asks (a removed field fails, an added field passes).

Done when: a removed field fails CI and an added one passes ([REQ-T05-05](../../specs/03-technical/t05-api-and-webhooks/requirements/req-t05-05-contract-tests.md) criteria 1 and 2); a stale document fails CI.

Where: `backend/services/platform`, `.github`.

## Features, use cases and business rules

- [📌 REQ-T05-01: REST with OpenAPI behind one gateway](../../specs/03-technical/t05-api-and-webhooks/requirements/req-t05-01-rest-openapi.md)
- [📌 REQ-T05-05: Contracts tested](../../specs/03-technical/t05-api-and-webhooks/requirements/req-t05-05-contract-tests.md)
- [🔌 I-T05-02: OpenAPI registry](../../specs/03-technical/t05-api-and-webhooks/interfaces/i-t05-02-openapi-registry.md)
- [📜 D406: Back end](../../specs/06-decisions/technical/d406-back-end.md)
- [📜 D426: Testing strategy](../../specs/06-decisions/technical/d426-testing-strategy.md)
- [📜 D419: CI/CD and the image registry](../../specs/06-decisions/technical/d419-ci-cd-and-registry.md): the pipeline in `.github` that runs the check.

## Technical pages it builds on

- [🏗️ Back end](../../technical/architecture/backend.md): "Each service publishes its OpenAPI generated from its Pydantic models ... breaking changes are caught in CI."
- [🏗️ API](../../technical/interfaces/api.md): an OpenAPI per service, the version in the path (`/v1`); the chapter lists each endpoint with its OpenAPI definition.
- [🏗️ Tests and traceability](../../technical/delivery/tests-and-traceability.md): "contract tests generated from each OpenAPI".

## Screens touched

- ➖ No screen: the ticket changes `backend/services/platform` and `.github` only, no front end.

## Budgets touched

- The ticket touches no budget: neither the roadmap row nor the specifications give it a measure.

## Acceptance criteria

1. **Given** `platform` starts, **when** its OpenAPI is requested, **then** the document generated from its code is served. ([REQ-T05-01](../../specs/03-technical/t05-api-and-webhooks/requirements/req-t05-01-rest-openapi.md) criterion 1)
2. **Given** a field removed from the API of `platform`, **when** the contract check runs in CI, **then** CI fails. ([REQ-T05-05](../../specs/03-technical/t05-api-and-webhooks/requirements/req-t05-05-contract-tests.md) criterion 1)
3. **Given** a field added to the API of `platform`, **when** the contract check runs in CI, **then** CI passes. ([REQ-T05-05](../../specs/03-technical/t05-api-and-webhooks/requirements/req-t05-05-contract-tests.md) criterion 2)
4. **Given** the committed OpenAPI document differs from the one generated from the code, **when** CI runs, **then** it fails. (roadmap "done when")
5. **Given** the OpenAPI document is generated, **when** it is committed, **then** it is the one served by `platform` ([I-T05-02](../../specs/03-technical/t05-api-and-webhooks/interfaces/i-t05-02-openapi-registry.md)).

## Out of scope

- The typed API client generated from this document, see [T0.20](../../specs/00-vision/roadmap/phases/01-p0-foundations.md#s03).
- The Bruno collection generated from it, see [T0.24](../../specs/00-vision/roadmap/phases/01-p0-foundations.md#s04).
- The gateway and routing of `/v1` to services ([REQ-T05-01](../../specs/03-technical/t05-api-and-webhooks/requirements/req-t05-01-rest-openapi.md) criterion 2), see the P2 closing of T5 in [P0 scope](../../specs/00-vision/roadmap/phases/01-p0-foundations.md#scope).
- The `platform` skeleton and its image, see [T0.14](../../specs/00-vision/roadmap/phases/01-p0-foundations.md#s02).

## Assumptions

- The roadmap gives no anchor per ticket, so the ticket links point to the sprint anchor of its table.
- Criteria 4 and 5 restate the roadmap's "done when" and the "committed and served" wording; the specifications name no tool or file path for the document or the check, so the plan chooses them within `backend/services/platform` and `.github`.
- REQ-T05-01 criterion 2 (routing behind the gateway) is taken as closed in P2, as the P0 scope table says.
- T0.14 (the `platform` skeleton) is taken as a prerequisite, since the ticket generates the document from its code.
