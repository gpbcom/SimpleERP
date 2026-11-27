# T0.03: Shared base model and enums

**Status:** ✅ Done · **Ticket:** [TICKET.md](TICKET.md) · **Choices and trade-offs:** [IMPLEMENTATION.md](IMPLEMENTATION.md) · **Review:** [REVIEW.md](REVIEW.md)

## 🔭 What it does

- Gives every service one base model that refuses unknown keys, and a frozen variant for values that must not change.
- Provides opaque ids (record, company, idempotency key), a UTC timestamp and an exact money value with its currency.
- Provides a generic cursor page and `YamlCatalog`, the base of the catalogues loaded from `conf/catalogs/`.
- Adds the `StrEnum` conventions test, and the dependencies (pydantic, pyyaml) of `erp_models`.

## ⚙️ How it works

1. **Base models:** [`ErpModel`](../../../backend/models/src/erp_models/base/erp_model.py#L14) sets `extra="forbid"`. [`FrozenErpModel`](../../../backend/models/src/erp_models/base/frozen_erp_model.py#L17) adds `frozen=True`, which also makes instances hashable. Every value type below is frozen.
2. **Opaque ids:** [`OpaqueId.validate_value`](../../../backend/models/src/erp_models/base/opaque_id.py#L29-L47) refuses a non-text or empty value and strips the rest, raising the subclass's `INVALID_VALUE` exception ([`opaque_id.py:25`](../../../backend/models/src/erp_models/base/opaque_id.py#L25)). The text is wrapped in a `value` field.
3. **Typed ids:** [`RecordId`](../../../backend/models/src/erp_models/ids/record_id.py#L19), [`CompanyId`](../../../backend/models/src/erp_models/ids/company_id.py#L24) and [`IdempotencyKey`](../../../backend/models/src/erp_models/idempotency/idempotency_key.py#L25) only set their own exception. Pydantic equality compares the model type too, so a `CompanyId` never equals a `RecordId` of the same text.
4. **Time:** [`UtcTimestamp.validate_instant`](../../../backend/models/src/erp_models/times/utc_timestamp.py#L29-L70) parses an ISO 8601 text, refuses naive times and anything that is not a datetime, and converts to UTC. [`now`](../../../backend/models/src/erp_models/times/utc_timestamp.py#L73) builds the current instant.
5. **Money amount:** [`validate_amount`](../../../backend/models/src/erp_models/money/money.py#L36) refuses floats, booleans, NaN and Infinity, and accepts a decimal text, an `int` or a `Decimal`. Nothing is rounded and the scale is kept.
6. **Money currency:** [`validate_currency`](../../../backend/models/src/erp_models/money/money.py#L82) requires three upper-case letters (`CURRENCY_PATTERN`, [line 31](../../../backend/models/src/erp_models/money/money.py#L31)).
7. **Money sums:** [`zero`](../../../backend/models/src/erp_models/money/money.py#L112), [`add`](../../../backend/models/src/erp_models/money/money.py#L124) (raises `SEMoneyCurrencyMismatch` across currencies) and [`total`](../../../backend/models/src/erp_models/money/money.py#L143), which starts from zero and adds line by line, so there is no float error (REQ-T10-03).
8. **Paging:** [`CursorPage`](../../../backend/models/src/erp_models/paging/cursor_page.py#L14) holds `items` ([validator](../../../backend/models/src/erp_models/paging/cursor_page.py#L31)) and an opaque `next_cursor`, stripped and never empty ([validator](../../../backend/models/src/erp_models/paging/cursor_page.py#L53)). [`has_more`](../../../backend/models/src/erp_models/paging/cursor_page.py#L79) is true when a cursor is set.
9. **Catalogues:** [`YamlCatalog.load`](../../../backend/models/src/erp_models/catalogs/yaml_catalog.py#L34) opens the file as UTF-8, reads it with `yaml.safe_load`, requires a mapping and validates it. Any failure raises the catalogue's `UNREADABLE` ([line 28](../../../backend/models/src/erp_models/catalogs/yaml_catalog.py#L28)) without quoting the file's content.
10. **Enum conventions:** [`TestStrEnumConventions`](../../../backend/models/tests/test_str_enum_conventions.py#L11) checks every `StrEnum` of `erp_models` (see the README).

## 🧱 Files and lines changed

<!-- changes -->
| File | Change | Lines in the new version | Added | Removed |
| --- | --- | --- | --- | --- |
| [`backend/models/README.md`](../../../backend/models/README.md) | Modified | [7-47](../../../backend/models/README.md#L7) | +41 | −2 |
| [`backend/models/pyproject.toml`](../../../backend/models/pyproject.toml) | Modified | [8](../../../backend/models/pyproject.toml#L8), [16-21](../../../backend/models/pyproject.toml#L16) | +7 | −1 |
| [`backend/models/src/erp_models/base/__init__.py`](../../../backend/models/src/erp_models/base/__init__.py) | Added | ➖ | +0 | −0 |
| [`backend/models/src/erp_models/base/erp_model.py`](../../../backend/models/src/erp_models/base/erp_model.py) | Added | [1-14](../../../backend/models/src/erp_models/base/erp_model.py#L1) | +14 | −0 |
| [`backend/models/src/erp_models/base/exceptions/__init__.py`](../../../backend/models/src/erp_models/base/exceptions/__init__.py) | Added | [1-4](../../../backend/models/src/erp_models/base/exceptions/__init__.py#L1) | +4 | −0 |
| [`backend/models/src/erp_models/base/exceptions/se_invalid_opaque_id_exception.py`](../../../backend/models/src/erp_models/base/exceptions/se_invalid_opaque_id_exception.py) | Added | [1-10](../../../backend/models/src/erp_models/base/exceptions/se_invalid_opaque_id_exception.py#L1) | +10 | −0 |
| [`backend/models/src/erp_models/base/exceptions/se_opaque_id_invalid_value.py`](../../../backend/models/src/erp_models/base/exceptions/se_opaque_id_invalid_value.py) | Added | [1-7](../../../backend/models/src/erp_models/base/exceptions/se_opaque_id_invalid_value.py#L1) | +7 | −0 |
| [`backend/models/src/erp_models/base/frozen_erp_model.py`](../../../backend/models/src/erp_models/base/frozen_erp_model.py) | Added | [1-17](../../../backend/models/src/erp_models/base/frozen_erp_model.py#L1) | +17 | −0 |
| [`backend/models/src/erp_models/base/opaque_id.py`](../../../backend/models/src/erp_models/base/opaque_id.py) | Added | [1-53](../../../backend/models/src/erp_models/base/opaque_id.py#L1) | +53 | −0 |
| [`backend/models/src/erp_models/catalogs/__init__.py`](../../../backend/models/src/erp_models/catalogs/__init__.py) | Added | ➖ | +0 | −0 |
| [`backend/models/src/erp_models/catalogs/exceptions/__init__.py`](../../../backend/models/src/erp_models/catalogs/exceptions/__init__.py) | Added | [1-4](../../../backend/models/src/erp_models/catalogs/exceptions/__init__.py#L1) | +4 | −0 |
| [`backend/models/src/erp_models/catalogs/exceptions/se_invalid_yaml_catalog_exception.py`](../../../backend/models/src/erp_models/catalogs/exceptions/se_invalid_yaml_catalog_exception.py) | Added | [1-10](../../../backend/models/src/erp_models/catalogs/exceptions/se_invalid_yaml_catalog_exception.py#L1) | +10 | −0 |
| [`backend/models/src/erp_models/catalogs/exceptions/se_yaml_catalog_unreadable.py`](../../../backend/models/src/erp_models/catalogs/exceptions/se_yaml_catalog_unreadable.py) | Added | [1-8](../../../backend/models/src/erp_models/catalogs/exceptions/se_yaml_catalog_unreadable.py#L1) | +8 | −0 |
| [`backend/models/src/erp_models/catalogs/yaml_catalog.py`](../../../backend/models/src/erp_models/catalogs/yaml_catalog.py) | Added | [1-60](../../../backend/models/src/erp_models/catalogs/yaml_catalog.py#L1) | +60 | −0 |
| [`backend/models/src/erp_models/idempotency/__init__.py`](../../../backend/models/src/erp_models/idempotency/__init__.py) | Added | ➖ | +0 | −0 |
| [`backend/models/src/erp_models/idempotency/exceptions/__init__.py`](../../../backend/models/src/erp_models/idempotency/exceptions/__init__.py) | Added | [1-4](../../../backend/models/src/erp_models/idempotency/exceptions/__init__.py#L1) | +4 | −0 |
| [`backend/models/src/erp_models/idempotency/exceptions/se_idempotency_key_invalid_value.py`](../../../backend/models/src/erp_models/idempotency/exceptions/se_idempotency_key_invalid_value.py) | Added | [1-7](../../../backend/models/src/erp_models/idempotency/exceptions/se_idempotency_key_invalid_value.py#L1) | +7 | −0 |
| [`backend/models/src/erp_models/idempotency/exceptions/se_invalid_idempotency_key_exception.py`](../../../backend/models/src/erp_models/idempotency/exceptions/se_invalid_idempotency_key_exception.py) | Added | [1-10](../../../backend/models/src/erp_models/idempotency/exceptions/se_invalid_idempotency_key_exception.py#L1) | +10 | −0 |
| [`backend/models/src/erp_models/idempotency/idempotency_key.py`](../../../backend/models/src/erp_models/idempotency/idempotency_key.py) | Added | [1-25](../../../backend/models/src/erp_models/idempotency/idempotency_key.py#L1) | +25 | −0 |
| [`backend/models/src/erp_models/ids/__init__.py`](../../../backend/models/src/erp_models/ids/__init__.py) | Added | ➖ | +0 | −0 |
| [`backend/models/src/erp_models/ids/company_id.py`](../../../backend/models/src/erp_models/ids/company_id.py) | Added | [1-24](../../../backend/models/src/erp_models/ids/company_id.py#L1) | +24 | −0 |
| [`backend/models/src/erp_models/ids/exceptions/__init__.py`](../../../backend/models/src/erp_models/ids/exceptions/__init__.py) | Added | [1-11](../../../backend/models/src/erp_models/ids/exceptions/__init__.py#L1) | +11 | −0 |
| [`backend/models/src/erp_models/ids/exceptions/se_company_id_invalid_value.py`](../../../backend/models/src/erp_models/ids/exceptions/se_company_id_invalid_value.py) | Added | [1-7](../../../backend/models/src/erp_models/ids/exceptions/se_company_id_invalid_value.py#L1) | +7 | −0 |
| [`backend/models/src/erp_models/ids/exceptions/se_invalid_company_id_exception.py`](../../../backend/models/src/erp_models/ids/exceptions/se_invalid_company_id_exception.py) | Added | [1-10](../../../backend/models/src/erp_models/ids/exceptions/se_invalid_company_id_exception.py#L1) | +10 | −0 |
| [`backend/models/src/erp_models/ids/exceptions/se_invalid_record_id_exception.py`](../../../backend/models/src/erp_models/ids/exceptions/se_invalid_record_id_exception.py) | Added | [1-10](../../../backend/models/src/erp_models/ids/exceptions/se_invalid_record_id_exception.py#L1) | +10 | −0 |
| [`backend/models/src/erp_models/ids/exceptions/se_record_id_invalid_value.py`](../../../backend/models/src/erp_models/ids/exceptions/se_record_id_invalid_value.py) | Added | [1-7](../../../backend/models/src/erp_models/ids/exceptions/se_record_id_invalid_value.py#L1) | +7 | −0 |
| [`backend/models/src/erp_models/ids/record_id.py`](../../../backend/models/src/erp_models/ids/record_id.py) | Added | [1-19](../../../backend/models/src/erp_models/ids/record_id.py#L1) | +19 | −0 |
| [`backend/models/src/erp_models/money/__init__.py`](../../../backend/models/src/erp_models/money/__init__.py) | Added | ➖ | +0 | −0 |
| [`backend/models/src/erp_models/money/exceptions/__init__.py`](../../../backend/models/src/erp_models/money/exceptions/__init__.py) | Added | [1-6](../../../backend/models/src/erp_models/money/exceptions/__init__.py#L1) | +6 | −0 |
| [`backend/models/src/erp_models/money/exceptions/se_invalid_money_exception.py`](../../../backend/models/src/erp_models/money/exceptions/se_invalid_money_exception.py) | Added | [1-10](../../../backend/models/src/erp_models/money/exceptions/se_invalid_money_exception.py#L1) | +10 | −0 |
| [`backend/models/src/erp_models/money/exceptions/se_money_currency_mismatch.py`](../../../backend/models/src/erp_models/money/exceptions/se_money_currency_mismatch.py) | Added | [1-7](../../../backend/models/src/erp_models/money/exceptions/se_money_currency_mismatch.py#L1) | +7 | −0 |
| [`backend/models/src/erp_models/money/exceptions/se_money_invalid_amount.py`](../../../backend/models/src/erp_models/money/exceptions/se_money_invalid_amount.py) | Added | [1-7](../../../backend/models/src/erp_models/money/exceptions/se_money_invalid_amount.py#L1) | +7 | −0 |
| [`backend/models/src/erp_models/money/exceptions/se_money_invalid_currency.py`](../../../backend/models/src/erp_models/money/exceptions/se_money_invalid_currency.py) | Added | [1-7](../../../backend/models/src/erp_models/money/exceptions/se_money_invalid_currency.py#L1) | +7 | −0 |
| [`backend/models/src/erp_models/money/money.py`](../../../backend/models/src/erp_models/money/money.py) | Added | [1-160](../../../backend/models/src/erp_models/money/money.py#L1) | +160 | −0 |
| [`backend/models/src/erp_models/paging/__init__.py`](../../../backend/models/src/erp_models/paging/__init__.py) | Added | ➖ | +0 | −0 |
| [`backend/models/src/erp_models/paging/cursor_page.py`](../../../backend/models/src/erp_models/paging/cursor_page.py) | Added | [1-86](../../../backend/models/src/erp_models/paging/cursor_page.py#L1) | +86 | −0 |
| [`backend/models/src/erp_models/paging/exceptions/__init__.py`](../../../backend/models/src/erp_models/paging/exceptions/__init__.py) | Added | [1-5](../../../backend/models/src/erp_models/paging/exceptions/__init__.py#L1) | +5 | −0 |
| [`backend/models/src/erp_models/paging/exceptions/se_cursor_page_invalid_items.py`](../../../backend/models/src/erp_models/paging/exceptions/se_cursor_page_invalid_items.py) | Added | [1-7](../../../backend/models/src/erp_models/paging/exceptions/se_cursor_page_invalid_items.py#L1) | +7 | −0 |
| [`backend/models/src/erp_models/paging/exceptions/se_cursor_page_invalid_next_cursor.py`](../../../backend/models/src/erp_models/paging/exceptions/se_cursor_page_invalid_next_cursor.py) | Added | [1-7](../../../backend/models/src/erp_models/paging/exceptions/se_cursor_page_invalid_next_cursor.py#L1) | +7 | −0 |
| [`backend/models/src/erp_models/paging/exceptions/se_invalid_cursor_page_exception.py`](../../../backend/models/src/erp_models/paging/exceptions/se_invalid_cursor_page_exception.py) | Added | [1-10](../../../backend/models/src/erp_models/paging/exceptions/se_invalid_cursor_page_exception.py#L1) | +10 | −0 |
| [`backend/models/src/erp_models/py.typed`](../../../backend/models/src/erp_models/py.typed) | Added | ➖ | +0 | −0 |
| [`backend/models/src/erp_models/times/__init__.py`](../../../backend/models/src/erp_models/times/__init__.py) | Added | ➖ | +0 | −0 |
| [`backend/models/src/erp_models/times/exceptions/__init__.py`](../../../backend/models/src/erp_models/times/exceptions/__init__.py) | Added | [1-4](../../../backend/models/src/erp_models/times/exceptions/__init__.py#L1) | +4 | −0 |
| [`backend/models/src/erp_models/times/exceptions/se_invalid_utc_timestamp_exception.py`](../../../backend/models/src/erp_models/times/exceptions/se_invalid_utc_timestamp_exception.py) | Added | [1-10](../../../backend/models/src/erp_models/times/exceptions/se_invalid_utc_timestamp_exception.py#L1) | +10 | −0 |
| [`backend/models/src/erp_models/times/exceptions/se_utc_timestamp_invalid_instant.py`](../../../backend/models/src/erp_models/times/exceptions/se_utc_timestamp_invalid_instant.py) | Added | [1-7](../../../backend/models/src/erp_models/times/exceptions/se_utc_timestamp_invalid_instant.py#L1) | +7 | −0 |
| [`backend/models/src/erp_models/times/utc_timestamp.py`](../../../backend/models/src/erp_models/times/utc_timestamp.py) | Added | [1-80](../../../backend/models/src/erp_models/times/utc_timestamp.py#L1) | +80 | −0 |
| [`backend/models/tests/base/test_erp_model.py`](../../../backend/models/tests/base/test_erp_model.py) | Added | [1-53](../../../backend/models/tests/base/test_erp_model.py#L1) | +53 | −0 |
| [`backend/models/tests/base/test_frozen_erp_model.py`](../../../backend/models/tests/base/test_frozen_erp_model.py) | Added | [1-58](../../../backend/models/tests/base/test_frozen_erp_model.py#L1) | +58 | −0 |
| [`backend/models/tests/base/test_opaque_id.py`](../../../backend/models/tests/base/test_opaque_id.py) | Added | [1-52](../../../backend/models/tests/base/test_opaque_id.py#L1) | +52 | −0 |
| [`backend/models/tests/catalogs/yaml_catalog/sample_catalog.py`](../../../backend/models/tests/catalogs/yaml_catalog/sample_catalog.py) | Added | [1-46](../../../backend/models/tests/catalogs/yaml_catalog/sample_catalog.py#L1) | +46 | −0 |
| [`backend/models/tests/catalogs/yaml_catalog/se_sample_catalog_invalid_names.py`](../../../backend/models/tests/catalogs/yaml_catalog/se_sample_catalog_invalid_names.py) | Added | [1-5](../../../backend/models/tests/catalogs/yaml_catalog/se_sample_catalog_invalid_names.py#L1) | +5 | −0 |
| [`backend/models/tests/catalogs/yaml_catalog/se_sample_catalog_unreadable.py`](../../../backend/models/tests/catalogs/yaml_catalog/se_sample_catalog_unreadable.py) | Added | [1-7](../../../backend/models/tests/catalogs/yaml_catalog/se_sample_catalog_unreadable.py#L1) | +7 | −0 |
| [`backend/models/tests/catalogs/yaml_catalog/test_yaml_catalog.py`](../../../backend/models/tests/catalogs/yaml_catalog/test_yaml_catalog.py) | Added | [1-100](../../../backend/models/tests/catalogs/yaml_catalog/test_yaml_catalog.py#L1) | +100 | −0 |
| [`backend/models/tests/idempotency/test_idempotency_key.py`](../../../backend/models/tests/idempotency/test_idempotency_key.py) | Added | [1-66](../../../backend/models/tests/idempotency/test_idempotency_key.py#L1) | +66 | −0 |
| [`backend/models/tests/ids/test_company_id.py`](../../../backend/models/tests/ids/test_company_id.py) | Added | [1-66](../../../backend/models/tests/ids/test_company_id.py#L1) | +66 | −0 |
| [`backend/models/tests/ids/test_record_id.py`](../../../backend/models/tests/ids/test_record_id.py) | Added | [1-45](../../../backend/models/tests/ids/test_record_id.py#L1) | +45 | −0 |
| [`backend/models/tests/money/money/test_money.py`](../../../backend/models/tests/money/money/test_money.py) | Added | [1-125](../../../backend/models/tests/money/money/test_money.py#L1) | +125 | −0 |
| [`backend/models/tests/money/money/test_money_sums.py`](../../../backend/models/tests/money/money/test_money_sums.py) | Added | [1-68](../../../backend/models/tests/money/money/test_money_sums.py#L1) | +68 | −0 |
| [`backend/models/tests/paging/test_cursor_page.py`](../../../backend/models/tests/paging/test_cursor_page.py) | Added | [1-96](../../../backend/models/tests/paging/test_cursor_page.py#L1) | +96 | −0 |
| [`backend/models/tests/test_str_enum_conventions.py`](../../../backend/models/tests/test_str_enum_conventions.py) | Added | [1-129](../../../backend/models/tests/test_str_enum_conventions.py#L1) | +129 | −0 |
| [`backend/models/tests/times/test_utc_timestamp.py`](../../../backend/models/tests/times/test_utc_timestamp.py) | Added | [1-99](../../../backend/models/tests/times/test_utc_timestamp.py#L1) | +99 | −0 |
| [`docs/technical/architecture/configuration.md`](../../../docs/technical/architecture/configuration.md) | Modified | [9](../../../docs/technical/architecture/configuration.md#L9), [49](../../../docs/technical/architecture/configuration.md#L49) | +2 | −2 |
| [`uv.lock`](../../../uv.lock) | Modified | [84-93](../../../uv.lock#L84) | +10 | −0 |
| **63 files** | | | **+1809** | **−5** |
<!-- /changes -->

- [`backend/models/src/erp_models/base/`](../../../backend/models/src/erp_models/base/): the two base models, `OpaqueId` and its two exceptions.
- [`backend/models/src/erp_models/ids/`](../../../backend/models/src/erp_models/ids/), [`idempotency/`](../../../backend/models/src/erp_models/idempotency/): the typed ids and the idempotency key, each with its exceptions.
- [`backend/models/src/erp_models/times/`](../../../backend/models/src/erp_models/times/), [`money/`](../../../backend/models/src/erp_models/money/), [`paging/`](../../../backend/models/src/erp_models/paging/), [`catalogs/`](../../../backend/models/src/erp_models/catalogs/): the value types and the catalogue base, each with its `SE` exceptions in `exceptions/`.
- [`backend/models/src/erp_models/py.typed`](../../../backend/models/src/erp_models/py.typed): marks the package as typed for mypy.
- [`backend/models/tests/`](../../../backend/models/tests/): the tests mirror the source, with the six model tests of AGENT.md per model, [money sums](../../../backend/models/tests/money/money/test_money_sums.py) and the [StrEnum conventions](../../../backend/models/tests/test_str_enum_conventions.py).
- [`backend/models/pyproject.toml`](../../../backend/models/pyproject.toml), lines [`8-21`](../../../backend/models/pyproject.toml#L8-L21): adds the pydantic and pyyaml dependencies and a pytest section so that `tests.*` imports resolve.
- [`uv.lock`](../../../uv.lock): only the `erp-models` entry gains its dependencies.
- [`backend/models/README.md`](../../../backend/models/README.md): lists the sub-packages, the exceptions and the enum conventions.
- [`docs/technical/architecture/configuration.md`](../../technical/architecture/configuration.md), lines [`9`](../../technical/architecture/configuration.md#L9) and [`49`](../../technical/architecture/configuration.md#L49): says that `YamlCatalog` now exists.

## 🧪 How to test it

```bash
uv run pytest backend/models/tests -n 2
uv run mypy backend/models/src
uv run ruff check backend
uv run pytest tests/conventions -n 2
```

## 🔗 Evidence

- [Models tests](tests-evidences/pytest-backend-models.txt): 215 passed.
- [Repository tests](tests-evidences/pytest.txt): 1156 passed.
- [Ruff check](tests-evidences/ruff-check.txt), [ruff format](tests-evidences/ruff-format.txt) and [mypy](tests-evidences/mypy.txt): clean.
- [Lock check](tests-evidences/uv-lock-check.txt), [lifecycle tests](tests-evidences/pytest-backend-shared-lifecycle.txt), [ticket references](tests-evidences/ticket-refs.txt) and [plan view](tests-evidences/plan-view.txt).

## 📝 Assumptions accepted

- K17: pydantic 2.14.4 and pyyaml 6.0.4 were already pinned in [`uv.lock`](../../../uv.lock) as dev dependencies of the root package, so only the `erp-models` entry changes (D415).
- No use case, business rule or screen is linked, because the roadmap names none. E-T01-01, REQ-T10-03 and REQ-T05-02 settle the work.
- Model names and the currency type are chosen in the plan under AGENT.md. Currency is a plain ISO 4217 alphabetic text, with no invented catalogue.
- Criterion 3 states only what REQ-T05-02 says. `CursorPage` and `IdempotencyKey` add no rule beyond it, and storing keys is left to the services.
- No budget is touched.

## 🔜 Follow-ups

| File | What to change |
| --- | --- |
| [`money.py`](../../../backend/models/src/erp_models/money/money.py#L3) | K12: move the `# Standard library imports` comment above `import re`, so that `re` and `decimal` are in the same group. |
| [`opaque_id.py`](../../../backend/models/src/erp_models/base/opaque_id.py), [`company_id.py`](../../../backend/models/src/erp_models/ids/company_id.py), [`record_id.py`](../../../backend/models/src/erp_models/ids/record_id.py), [`idempotency_key.py`](../../../backend/models/src/erp_models/idempotency/idempotency_key.py), [`IMPLEMENTATION.md`](IMPLEMENTATION.md) | K09/K10/K14: ids and keys wrap a `value` field, so `company_id: CompanyId` serialises as `{"company_id": {"value": "C-12"}}`. Alternatives and the SE exceptions on `Exception` are recorded in IMPLEMENTATION.md. Revisit before the first API resource uses them. |
| [`cursor_page.py`](../../../backend/models/src/erp_models/paging/cursor_page.py#L79), [`README.md`](../../../backend/models/README.md) | K13/K16: `has_more` is a plain `@property`, so it is missing from `model_dump` and the JSON schema. Make it a `@computed_field` when the API resources are built, or describe it in the README as derived. |
| [`test_erp_model.py`](../../../backend/models/tests/base/test_erp_model.py), [`test_frozen_erp_model.py`](../../../backend/models/tests/base/test_frozen_erp_model.py) | K01: `test_none_becomes_the_default` asserts that `None` raises `ValidationError`, the opposite of its name. Rename it or give the sample model a validator that maps None to the default. |
| [`sample_catalog.py`](../../../backend/models/tests/catalogs/yaml_catalog/sample_catalog.py) | K07: split the two `SESampleCatalogInvalidNames` messages onto two lines each, with `# noqa: E501` on the first. |
| The `exceptions/__init__.py` of [`base`](../../../backend/models/src/erp_models/base/exceptions/__init__.py), [`catalogs`](../../../backend/models/src/erp_models/catalogs/exceptions/__init__.py), [`idempotency`](../../../backend/models/src/erp_models/idempotency/exceptions/__init__.py), [`ids`](../../../backend/models/src/erp_models/ids/exceptions/__init__.py), [`money`](../../../backend/models/src/erp_models/money/exceptions/__init__.py), [`paging`](../../../backend/models/src/erp_models/paging/exceptions/__init__.py), [`times`](../../../backend/models/src/erp_models/times/exceptions/__init__.py) | K09 to K15: add `from __future__ import annotations` at the top of each non-empty file. |
| [`utc_timestamp.py`](../../../backend/models/src/erp_models/times/utc_timestamp.py#L29) | K11: type the intermediate value as `Union[JsonValue, datetime]` rather than `object`, then drop the `cast`. |
| [`test_str_enum_conventions.py`](../../../backend/models/tests/test_str_enum_conventions.py) | K08: the StrEnum check covers only `erp_models`. Move it into `tests/conventions/` in a later ticket. |
| [`uv-lock-check.txt`](tests-evidences/uv-lock-check.txt), [`PROGRESS.md`](PROGRESS.md) | Verifier/scribe: rerun `uv lock --check` and `uv sync --locked --all-packages` in the clean tree, with the `cwd` line. In PROGRESS.md fix the task ids: Money is K12, UtcTimestamp K11, CursorPage K13. |
