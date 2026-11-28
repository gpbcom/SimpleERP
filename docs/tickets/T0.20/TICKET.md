# T0.20: Typed API client package

**Status:** ✅ Done

## Roadmap

- **Ticket:** [T0.20](../../specs/00-vision/roadmap/phases/01-p0-foundations.md#s03) in [🛣️ P0: Foundations](../../specs/00-vision/roadmap/phases/01-p0-foundations.md)
- **Phase:** [🛣️ P0: Foundations](../../specs/00-vision/roadmap/phases/01-p0-foundations.md)
- **Sprint:** [S03](../../specs/00-vision/roadmap/phases/01-p0-foundations.md#s03), 18 to 29 Jan 2027: The contracts and the shell
- **Epic:** [E0.4 First service and contracts](../../specs/00-vision/roadmap/phases/01-p0-foundations.md#epics): `backend/services/platform`, its image, its OpenAPI, the contract check, the typed client and the Bruno collection

## What it delivers

- `frontend/packages/api-client`, a typed client generated from the OpenAPI document of T0.18 (clients generated from the contract), as [Back end](../../technical/architecture/backend.md) (Contracts) and [📜 D406](../../specs/06-decisions/technical/d406-back-end.md) state.
- problem+json errors mapped to a typed error that carries its error code of the error message standard, as [📌 REQ-T05-03](../../specs/03-technical/t05-api-and-webhooks/requirements/req-t05-03-problem-json.md) and [📜 D122](../../specs/06-decisions/ux/d122-error-message-standard.md) state.
- A check that the generated client is up to date: CI, or the build, fails when it is stale.

## Features, use cases and business rules

- [📜 D406: Back end](../../specs/06-decisions/technical/d406-back-end.md): "OpenAPI generated from the code, with MCP tools, A2A skills, clients and the Bruno collection generated from it".
- [📜 D122: Error message standard](../../specs/06-decisions/ux/d122-error-message-standard.md): every error has a title, a why, an action and a small support reference.
- [📜 D438: Repository layout](../../specs/06-decisions/technical/d438-repository-layout.md): the shared TypeScript packages live under `frontend/packages/<pkg>`.
- [📜 D407: Front end](../../specs/06-decisions/technical/d407-front-end.md): Vue 3 with TypeScript and Vite, the front-end stack the client serves.
- [📌 REQ-T05-01: REST with OpenAPI behind one gateway](../../specs/03-technical/t05-api-and-webhooks/requirements/req-t05-01-rest-openapi.md): each service publishes an OpenAPI generated from its code, the source of the client.
- [📌 REQ-T05-03: problem+json errors](../../specs/03-technical/t05-api-and-webhooks/requirements/req-t05-03-problem-json.md): errors are problem+json with the error codes of the error pattern, no secret in them.
- [📌 REQ-T05-05: Contracts tested](../../specs/03-technical/t05-api-and-webhooks/requirements/req-t05-05-contract-tests.md): a removed field fails CI, so the client follows a contract that is checked.
- [🔌 I-T05-02: OpenAPI registry](../../specs/03-technical/t05-api-and-webhooks/interfaces/i-t05-02-openapi-registry.md): where the OpenAPI documents are published.

## Technical pages it builds on

- [🏗️ Back end](../../technical/architecture/backend.md): "Each service publishes its OpenAPI generated from its Pydantic models; ... typed clients ... are generated from it, so that one change updates all".
- [🏗️ Front end](../../technical/architecture/frontend.md): Vue 3, TypeScript and Vite, the stack of the package.
- [🏗️ API](../../technical/interfaces/api.md): `/v1` and `application/problem+json` errors carrying the codes of D122.

## Screens touched

- ➖ No screen: the package is a generated library with no user interface. The error on screen is built by T0.23.

## Budgets touched

- The ticket touches no budget.

## Acceptance criteria

1. **Given** the OpenAPI document of `platform` committed by T0.18 and the generated client in `frontend/packages/api-client`, **when** the document changes and the client is not regenerated, **then** CI or the build fails. ([📌 REQ-T05-01](../../specs/03-technical/t05-api-and-webhooks/requirements/req-t05-01-rest-openapi.md), [📌 REQ-T05-05](../../specs/03-technical/t05-api-and-webhooks/requirements/req-t05-05-contract-tests.md))
2. **Given** a field renamed in the OpenAPI document and the client regenerated, **when** a caller still uses the old name, **then** the type check fails. ([📌 REQ-T05-05](../../specs/03-technical/t05-api-and-webhooks/requirements/req-t05-05-contract-tests.md))
3. **Given** a call refused with a problem+json body, **when** the client receives it, **then** it gives the caller a typed error with the error code of the body. ([📌 REQ-T05-03](../../specs/03-technical/t05-api-and-webhooks/requirements/req-t05-03-problem-json.md), [📜 D122](../../specs/06-decisions/ux/d122-error-message-standard.md))
4. **Given** an error, **when** the client maps it, **then** no secret appears in the typed error. ([📌 REQ-T05-03](../../specs/03-technical/t05-api-and-webhooks/requirements/req-t05-03-problem-json.md))

## Out of scope

- The OpenAPI generation and the contract check, see [T0.18](../../specs/00-vision/roadmap/phases/01-p0-foundations.md#s03).
- The error shown on screen with its title, why and action, see [T0.23](../../specs/00-vision/roadmap/phases/01-p0-foundations.md#s04).
- The Bruno collection generated from the same document, see [T0.24](../../specs/00-vision/roadmap/phases/01-p0-foundations.md#s04).

## Assumptions

- The roadmap row names no generator tool, so the plan chooses one that respects D406 and the licences of the supply-chain page; the ticket fixes none.
- The roadmap row says "typed error with its D122 code" and no field name: the field of the problem+json body that carries the code is taken from T0.14 and T0.18, and is not invented here.
- Criterion 4 reads REQ-T05-03 criterion 2 (no secret in an error) as applying to the typed error the client builds from the body.
- The roadmap lists no use case, business rule or entity for this ticket, so its criteria cite requirements.
