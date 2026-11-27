# T0.03: Shared base model and enums

**Status:** ✅ Done

## Roadmap

- **Ticket:** [T0.03](../../specs/00-vision/roadmap/phases/01-p0-foundations.md#s01) in [🛣️ P0 Foundations](../../specs/00-vision/roadmap/phases/01-p0-foundations.md)
- **Phase:** [🛣️ P0 Foundations](../../specs/00-vision/roadmap/phases/01-p0-foundations.md)
- **Sprint:** [S01](../../specs/00-vision/roadmap/phases/01-p0-foundations.md#s01), 7 to 18 December 2026: the layout, its rules and the first shared code
- **Epic:** [E0.2 Shared models](../../specs/00-vision/roadmap/phases/01-p0-foundations.md#epics): `erp_models`: base model, money, ids and times, enums, `SE` exceptions and the error codes of D122

## What it delivers

In `backend/models` (the `erp_models` package):

- The base model: extra fields forbidden, frozen where it must not change, as [Repository layout](../../technical/architecture/repository-layout.md) makes `backend/models/` the one shared Pydantic models library.
- Ids and UTC times.
- The company id of [E-T01-01](../../specs/03-technical/t01-companies-and-data-isolation/data/e-t01-01-company.md) as an opaque type.
- Money as an exact decimal with its currency, following [REQ-T10-03](../../specs/03-technical/t10-translations-and-notifications/requirements/req-t10-03-money-decimals.md).
- The cursor page and idempotency key models of [REQ-T05-02](../../specs/03-technical/t05-api-and-webhooks/requirements/req-t05-02-paging-and-idempotency.md).
- The `StrEnum` conventions and `YamlCatalog`, the base of the catalogues loaded from `conf/catalogs/` ([Configuration](../../technical/architecture/configuration.md)).

## Features, use cases and business rules

- [🗃️ E-T01-01 Company](../../specs/03-technical/t01-companies-and-data-isolation/data/e-t01-01-company.md): the company id, taken as an opaque type.
- [📌 REQ-T10-03 Money as exact decimals](../../specs/03-technical/t10-translations-and-notifications/requirements/req-t10-03-money-decimals.md): money is an exact decimal with its currency.
- [📌 REQ-T05-02 Paging, filters, idempotency](../../specs/03-technical/t05-api-and-webhooks/requirements/req-t05-02-paging-and-idempotency.md): cursor paging and the idempotency key.
- [📜 D438 Repository layout](../../specs/06-decisions/technical/d438-repository-layout.md): `backend/models/` holds the shared models.
- [📜 D406 Back end](../../specs/06-decisions/technical/d406-back-end.md): Python 3.13 with uv and Pydantic models.

## Technical pages it builds on

- [🏗️ Repository layout](../../technical/architecture/repository-layout.md): `backend/models/` is the one shared Pydantic models library, so that every public contract is defined once.
- [🏗️ Back end](../../technical/architecture/backend.md): Pydantic models and the layers of `AGENT.md`.
- [🏗️ Configuration](../../technical/architecture/configuration.md): `conf/catalogs/` data is loaded by `YamlCatalog` models.

## Screens touched

- ➖ No screen: the ticket adds shared Python models in `backend/models` and changes no front end.

## Budgets touched

- The ticket touches no budget.

## Acceptance criteria

1. **Given** each model of `erp_models` delivered here, **when** its tests run, **then** it has the six model tests of AGENT.md (defaults, full valid construction, `None` becomes the default, bad values rejected, unknown keys rejected, round trip).
2. **Given** money lines in the same currency, **when** they are summed, **then** the result has no float error. ([📌 REQ-T10-03](../../specs/03-technical/t10-translations-and-notifications/requirements/req-t10-03-money-decimals.md), criterion 2)
3. **Given** a write repeated with its idempotency key, **when** the model of the key is used, **then** it carries the key that makes the write be done once, and a list is paged by a cursor. ([📌 REQ-T05-02](../../specs/03-technical/t05-api-and-webhooks/requirements/req-t05-02-paging-and-idempotency.md))
4. **Given** the models and enums of `backend/models`, **when** `tests/conventions/` runs, **then** it passes.

## Out of scope

- The `SE` exceptions and the error code catalogue, see [T0.04](../../specs/00-vision/roadmap/phases/01-p0-foundations.md#s01).
- Rounding and conversion rules of a country pack, see [📜 D293](../../specs/06-decisions/country-packs/d293-capabilities-take-legal-rules-from-the-pack.md).
- The lifecycle library, see [T0.05](../../specs/00-vision/roadmap/phases/01-p0-foundations.md#s01).

## Assumptions

- The roadmap names no use case, business rule or screen for this ticket, so none is linked.
- The names of the models and of the money currency type are not fixed by the specifications. They follow `AGENT.md` and are chosen in the plan.
- Criterion 3 states only what REQ-T05-02 says (cursor paging, idempotency key); the fields of the models are left to the plan.
- The ticket is read as having no budget: neither the roadmap row nor the specifications give it a measure.
