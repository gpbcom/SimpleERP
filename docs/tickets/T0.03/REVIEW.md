# T0.03: Review note

**Verdict:** ✅ Approved · **Branch:** `feature/tickets`

## What changed

- `erp_models` gets two base models: `ErpModel`, which refuses unknown keys, and `FrozenErpModel`, which also refuses assignment and is hashable. Every value type built in this ticket is frozen.
- Ids are opaque, frozen wrappers of a stripped, non-empty text (`OpaqueId`, then `RecordId`, `CompanyId` and `IdempotencyKey`). A `CompanyId` never equals a `RecordId` with the same text, and a service never parses it (E-T01-01).
- `Money` holds an exact `Decimal` and an ISO 4217 alphabetic code. Floats, booleans, NaN and Infinity are refused, nothing is rounded (D293 leaves rounding to the pack), and adding two currencies raises `SEMoneyCurrencyMismatch`. `UtcTimestamp` refuses naive times and epoch numbers and converts every instant to UTC.
- `CursorPage[ItemT]` (PEP 695 generic) holds `items` and an opaque `next_cursor`. `YamlCatalog.load(path)` reads a UTF-8 YAML mapping with `safe_load` and raises the catalogue's own `UNREADABLE`, without quoting the file's content.
- `uv.lock` is now part of the ticket. It pins only the erp-models dependencies, which closes the blocking finding of the previous run.

## Acceptance criteria

| Criterion | Evidence | Result |
| --- | --- | --- |
| 1. Each model has the six AGENT.md model tests | `tests-evidences/pytest-backend-models.txt` (215 passed). `test_defaults`, `test_full_valid_construction`, `test_none_becomes_the_default`, `test_rejects_bad_values`, `test_rejects_unknown_keys` and `test_round_trip` are present in each of `tests/base/*`, `tests/ids/*`, `tests/times/*`, `tests/money/money/test_money.py`, `tests/paging/*`, `tests/idempotency/*` and `tests/catalogs/yaml_catalog/*` | ✅ Pass |
| 2. Money lines in one currency sum with no float error (REQ-T10-03, 2) | `TestMoneySums.test_ten_lines_of_ten_cents_total_exactly_one`, `test_a_decimal_sum_has_no_float_error`, `test_large_amounts_sum_exactly` | ✅ Pass |
| 3. A repeated write carries the key that makes it done once, and a list is paged by a cursor (REQ-T05-02) | `TestIdempotencyKey.test_the_keys_of_repeated_writes_make_one_key`, `test_a_write_repeated_with_its_key_carries_an_equal_key`; `TestCursorPage.test_a_page_in_the_middle_of_a_list_has_a_next_cursor`, `test_the_last_page_has_no_next_cursor` | ✅ Pass |
| 4. `tests/conventions/` passes on the models and enums | `tests-evidences/pytest.txt` (`tests`, 1156 passed), `ruff-check.txt`, `ruff-format.txt`, `mypy.txt` | ✅ Pass |

## Look at first

- **Company data isolation: the opaque company id.** Read `backend/models/src/erp_models/base/opaque_id.py` and `backend/models/src/erp_models/ids/company_id.py` line by line. The text is only stripped and is kept case-sensitive as given. Equality is by model type and value, so a `CompanyId` cannot be swapped for a `RecordId`. The id is wrapped as `{"value": ...}` and is not a bare string. That choice will show in every API contract, so decide it before the first resource uses it (follow-up).
- **Exceptions outside `ValueError`.** Every model exception subclasses `Exception`, so Pydantic raises it as it is and does not collect it into a `ValidationError`. A missing required field still raises `ValidationError`. T0.04 adds the shared SE bases and error codes on top: `backend/models/src/erp_models/*/exceptions/`.
- **Money semantics:** `backend/models/src/erp_models/money/money.py`. The scale is kept (`1.0` and `1.00` are equal). JSON round-trips the amount as a string. `total` starts from `zero(currency)` and adds lines one by one.
- **The lock:** the `uv.lock` hunk of the ticket touches only the `erp-models` entry. `backend/models/pyproject.toml` also adds a pytest section, so that `tests.catalogs...` imports resolve from `backend/models`.

## Assumptions accepted

- K17, pydantic and pyyaml already pinned in uv.lock: accepted. HEAD pins pydantic 2.14.4 and pyyaml 6.0.4 as root dev dependencies, so only the erp-models entry changes (D415).
- TICKET.md, no use case, rule or screen linked: accepted. The roadmap names none, and E-T01-01, REQ-T10-03 and REQ-T05-02 settle the work.
- TICKET.md, model and currency names chosen in the plan: accepted. The specifications fix no name, and the currency is an ISO 4217 text, with no invented catalogue.
- TICKET.md, criterion 3 limited to what REQ-T05-02 says: accepted. Storing the keys belongs to the services that write.
- TICKET.md, no budget: accepted. No non-functional measure applies yet.

## Follow-ups

- K09, K10, K14 and the explainer: record in IMPLEMENTATION.md the decisions no agent reported. These are the `value` wrapper for ids against `RootModel[str]` or `Annotated[str, ...]`, the exceptions based on `Exception` and not `ValueError`, and the behaviour on value objects (`Money.add/total`, `UtcTimestamp.now`).
- K13 and K16: `CursorPage.has_more` is a plain property, missing from `model_dump` and the JSON schema. Make it a `@computed_field` or describe it as derived.
- K12: in `money.py`, `import re` sits above the `# Standard library imports` comment.
- K01: `test_none_becomes_the_default` in `test_erp_model.py` and `test_frozen_erp_model.py` asserts the opposite of its name.
- K07: the `SESampleCatalogInvalidNames` messages in `sample_catalog.py` put two sentences on one line.
- K09 to K15: the non-empty `exceptions/__init__.py` files lack `from __future__ import annotations`.
- K11: `utc_timestamp.py` types its intermediate value as `object` and needs a `cast`.
- K08: the StrEnum check covers only `erp_models`. Move it into `tests/conventions/` later, so that every package is covered.
- Verifier and scribe: rerun `uv-lock-check.txt` in the clean tree, with its `cwd` line. Fix the task ids in the 🔜 Follow-ups table of PROGRESS.md (Money is K12, UtcTimestamp K11, CursorPage K13).
