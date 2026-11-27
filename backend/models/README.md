# Shared models

The shared Pydantic models of every public contract: API resources, events, plugin and connector contracts, enums and
their `SE` exceptions. Each is defined once here. The package is `erp_models`, imported by the services, `plugins/` and
`sdk/`.

See [D438 Repository layout](../../docs/specs/06-decisions/technical/d438-repository-layout.md), the
[Repository layout](../../docs/technical/architecture/repository-layout.md) page, and the
[Backend](../../docs/technical/architecture/backend.md) page.

## Sub-packages

`erp_models` imports no service and no library of `backend/shared/`. Each sub-package holds the models of one concern.

| Sub-package | Models | Import path | Specification |
|---|---|---|---|
| `base` | `ErpModel`, a Pydantic model that forbids unknown keys; `FrozenErpModel`, the same and also frozen; `OpaqueId`, the base of opaque texts | `erp_models.base.erp_model`, `erp_models.base.frozen_erp_model`, `erp_models.base.opaque_id` | [D406 Back end](../../docs/specs/06-decisions/technical/d406-back-end.md) |
| `ids` | `RecordId`, the id of a record; `CompanyId`, the opaque id of a company | `erp_models.ids.record_id`, `erp_models.ids.company_id` | [E-T01-01 Company](../../docs/specs/03-technical/t01-companies-and-data-isolation/data/e-t01-01-company.md) |
| `times` | `UtcTimestamp`, an aware instant converted to UTC; naive times are refused | `erp_models.times.utc_timestamp` | [D406 Back end](../../docs/specs/06-decisions/technical/d406-back-end.md) |
| `money` | `Money`, an exact `Decimal` with an ISO 4217 alphabetic currency code; floats are refused and nothing is rounded (the country pack rounds, D293); with `zero`, `add` and `total`; sums in different currencies are refused | `erp_models.money.money` | [REQ-T10-03 Money decimals](../../docs/specs/03-technical/t10-translations-and-notifications/requirements/req-t10-03-money-decimals.md) |
| `paging` | `CursorPage[ItemT]`, with `items`, `next_cursor` and `has_more` | `erp_models.paging.cursor_page` | [REQ-T05-02 Paging and idempotency](../../docs/specs/03-technical/t05-api-and-webhooks/requirements/req-t05-02-paging-and-idempotency.md) |
| `idempotency` | `IdempotencyKey`, equal and hashable by value | `erp_models.idempotency.idempotency_key` | [REQ-T05-02 Paging and idempotency](../../docs/specs/03-technical/t05-api-and-webhooks/requirements/req-t05-02-paging-and-idempotency.md) |
| `catalogs` | `YamlCatalog`, with `load(path)`, which reads a UTF-8 YAML mapping; the `UNREADABLE` exception that each catalogue sets | `erp_models.catalogs.yaml_catalog` | [Configuration](../../docs/technical/architecture/configuration.md) |

## Exceptions

The `SE` exceptions of a model live in its sub-package's `exceptions/` folder, and the folder's `__init__.py` re-exports
them through a sorted `__all__`, so callers import from the package (`erp_models.money.exceptions`). The shared `SE`
base classes and the error codes are added by T0.04.

## StrEnum conventions

`backend/models/tests/test_str_enum_conventions.py` enforces these rules on every `StrEnum` of the package:

- the class carries `@unique`;
- each enum is in its own file, named after it in snake case (`PaymentStatus` in `payment_status.py`);
- its members are listed under `Attributes:` in the docstring;
- the `enums/` package's `__init__.py` re-exports it.

## Checks

Run the package's tests and type checks from the repository root:

```bash
uv run pytest backend/models/tests -n 2
uv run mypy backend/models/src
```
