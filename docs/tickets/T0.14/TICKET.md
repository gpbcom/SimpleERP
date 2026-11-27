# T0.14: Platform service skeleton and image

**Status:** ✅ Done

## Roadmap

- **Ticket:** [T0.14](../../specs/00-vision/roadmap/phases/01-p0-foundations.md#s02) in [🛣️ P0: Foundations](../../specs/00-vision/roadmap/phases/01-p0-foundations.md)
- **Phase:** [🛣️ P0: Foundations](../../specs/00-vision/roadmap/phases/01-p0-foundations.md)
- **Sprint:** [S02](../../specs/00-vision/roadmap/phases/01-p0-foundations.md#s02), 4 to 15 January 2027: the service kit and the first service
- **Epic:** [E0.4 First service and contracts](../../specs/00-vision/roadmap/phases/01-p0-foundations.md#epics): `backend/services/platform`, its image, its OpenAPI, the contract check, the typed client and the Bruno collection

## What it delivers

- `backend/services/platform` as an AGENT.md service: `api`, `service`, `storage` and `models` under its own package, factories and `conf/app.yaml`, as [Repository layout](../../technical/architecture/repository-layout.md#target-design-specified-in-gh-2-not-built-yet).
- A FastAPI application under `/v1` with a health endpoint, as [Back end](../../technical/architecture/backend.md#target-design-specified-in-gh-2-not-built-yet).
- The problem+json handler of [REQ-T05-03](../../specs/03-technical/t05-api-and-webhooks/requirements/req-t05-03-problem-json.md), with the [D122](../../specs/06-decisions/ux/d122-error-message-standard.md) error codes.
- The company-context middleware of the shared library (T0.09), mounted on the service.
- A multi-stage `Dockerfile` with the repository root as build context ([D419](../../specs/06-decisions/technical/d419-ci-cd-and-registry.md)).

## Features, use cases and business rules

- [📌 REQ-T05-03: problem+json errors](../../specs/03-technical/t05-api-and-webhooks/requirements/req-t05-03-problem-json.md)
- [📌 REQ-T01-02: The company context at every layer](../../specs/03-technical/t01-companies-and-data-isolation/requirements/req-t01-02-company-context-everywhere.md)
- [📜 D406: Back end](../../specs/06-decisions/technical/d406-back-end.md): every service is a regular FastAPI application, served by uvicorn, with no command line (owner, 2026-11-27).
- [📜 D438: Repository layout](../../specs/06-decisions/technical/d438-repository-layout.md)
- [📜 D419: CI/CD and the image registry](../../specs/06-decisions/technical/d419-ci-cd-and-registry.md)
- [📜 D122: Error message standard](../../specs/06-decisions/ux/d122-error-message-standard.md)

## Technical pages it builds on

- [Repository layout](../../technical/architecture/repository-layout.md): the service holds `Dockerfile`, `pyproject.toml`, `conf/`, `tests/` and `src/<service>/` with `models`, `storage`, `service` and `api`; each layer calls only the one below.
- [Back end](../../technical/architecture/backend.md): Python 3.13 with uv, Pydantic models, the api, service, storage layers and FastAPI for the HTTP services.

## Screens touched

- ➖ No screen: a back-end service and its image, with no front end.

## Budgets touched

- The ticket touches no budget: the roadmap row and the specifications give it no measure.

## Acceptance criteria

1. **Given** the image built from the repository root, **when** CI builds it and starts it, **then** it builds and starts. (T0.14 done when)
2. **Given** the running service, **when** the health endpoint under `/v1` is called, **then** it answers. (T0.14 done when)
3. **Given** a refused call, **when** the service answers, **then** the body is problem+json with its D122 error code. ([📌 REQ-T05-03](../../specs/03-technical/t05-api-and-webhooks/requirements/req-t05-03-problem-json.md) criterion 1, [📜 D122](../../specs/06-decisions/ux/d122-error-message-standard.md))
4. **Given** an error, **when** the service answers, **then** no secret is in the body. ([📌 REQ-T05-03](../../specs/03-technical/t05-api-and-webhooks/requirements/req-t05-03-problem-json.md) criterion 2)
5. **Given** a request without a company, **when** it reaches the service, **then** it is refused. ([📌 REQ-T01-02](../../specs/03-technical/t01-companies-and-data-isolation/requirements/req-t01-02-company-context-everywhere.md) criterion 1)
6. **Given** the new service, **when** `tests/conventions/` runs, **then** it passes with no change to the conventions. ([📜 D438](../../specs/06-decisions/technical/d438-repository-layout.md))

## Out of scope

- The OpenAPI document and the contract check, see [T0.18](../../specs/00-vision/roadmap/phases/01-p0-foundations.md#s03).
- The typed API client, see [T0.20](../../specs/00-vision/roadmap/phases/01-p0-foundations.md#s03).
- The Bruno collection, see [T0.24](../../specs/00-vision/roadmap/phases/01-p0-foundations.md#s04).
- The Compose stack and the Helm chart for the image, see [T0.21](../../specs/00-vision/roadmap/phases/01-p0-foundations.md#s04) and [T0.19](../../specs/00-vision/roadmap/phases/01-p0-foundations.md#s03).

## Assumptions

- The company-context middleware and the rights library come from T0.09 (`backend/shared/context`), the lifecycle base from T0.05 and the logging and configuration from T0.06: the roadmap row says "the context middleware" without naming the library, so it is assumed to be the one of T0.09.
- The service's Python package name is not given by the specifications: `platform` is assumed, adjusted if it collides with the standard library module of that name.
- The health endpoint path (for example `/v1/health`) is not specified: the most conservative option is taken.
- The roadmap sets no budget for the ticket, so none is listed.
- The "factories" of the roadmap row are the application factory of the FastAPI application, `AppFactory` ([D406](../../specs/06-decisions/technical/d406-back-end.md), AGENT.md "Layout"): the service has no command line and the skeleton has no runnable of its own.
