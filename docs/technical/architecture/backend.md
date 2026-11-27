# Back end

The back-end services: language, frameworks, service boundaries, data access, jobs and workers, events. Nothing of the
target is built yet.

## Today

The back end today is the Python 3.13 code under `src/`, described in [Architecture](architecture.md).

## Target design (specified in GH-2, not built yet)

**Language and framework (D406).** Python 3.13 with uv, Pydantic models and the api → service → storage layers
(`AGENT.md`); FastAPI for the HTTP services.

**Contracts (TC-07).** Each service publishes its OpenAPI generated from its Pydantic models; the MCP tools, A2A skills,
typed clients between services and the Bruno collection are generated from it, so that one change updates all; breaking
changes are caught in CI.

**Shared code.** `packages/` is a service kit with no business rules: the lifecycle base classes, logging, configuration
loading, the company-context and rights middleware, the event outbox, the metering client, the country-pack rules
library, test helpers.

**Business rules (TC-22).** Each service's rules (pricing, stock, planning, payroll, accounting) are pure functions over
the data they read, so that the same code runs on live data and on a what-if scenario overlay (F23); storage and side
effects stay at the edges.

Decided in [D406](../../specs/06-decisions/technical/d406-back-end.md).

Last reviewed: 2026-11-12 (GH-2)
