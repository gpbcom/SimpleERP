# T0.04: SE exceptions and error codes

**Status:** ✅ Done · **Ticket:** [TICKET.md](TICKET.md) · **Choices and trade-offs:** [IMPLEMENTATION.md](IMPLEMENTATION.md) · **Review:** [REVIEW.md](REVIEW.md)

## 🔭 What it does

- Gives every shared error three `SE` bases (`SEException`, `SEError`, `SEInvalidModelException`), each with a `CODE` that subclasses inherit or override.
- Holds the D122 error code catalogue as data: each code has a title, why and action translation key and a support reference.
- Refuses an unknown code, and keeps free text and secrets out of the catalogue through strict patterns.
- Adds a convention check that enforces the AGENT.md exception rules (name, file, sorted `__all__`) on every Python package.

## ⚙️ How it works

1. **The bases:** `SEException` is the root with `CODE = "UNEXPECTED-ERROR-01"`, in [`backend/models/src/erp_models/exceptions/se_exception.py:17`](../../../backend/models/src/erp_models/exceptions/se_exception.py#L17). `SEError` overrides it with `SERVICE-FAILURE-01` in [`backend/models/src/erp_models/exceptions/se_error.py:19`](../../../backend/models/src/erp_models/exceptions/se_error.py#L19), and `SEInvalidModelException` with `INVALID-INPUT-01` in [`backend/models/src/erp_models/exceptions/se_invalid_model_exception.py:19`](../../../backend/models/src/erp_models/exceptions/se_invalid_model_exception.py#L19). None subclasses `ValueError`, so Pydantic never wraps them.
2. **The data:** the four codes are in [`backend/models/conf/catalogs/error_codes.yaml:3-23`](../../../backend/models/conf/catalogs/error_codes.yaml#L3-L23), the three base codes and the D122 sample `SITE-CLOSE-01`.
3. **Loading:** `ErrorCatalog` is a `YamlCatalog` ([`backend/models/src/erp_models/errors/catalogs/error_catalog.py:20`](../../../backend/models/src/erp_models/errors/catalogs/error_catalog.py#L20)). An unreadable file raises its own `UNREADABLE`, set at [line 35](../../../backend/models/src/erp_models/errors/catalogs/error_catalog.py#L35).
4. **Checking the keys:** `validate_codes` refuses anything but a non-empty mapping whose keys match `CODE_PATTERN` ([`error_catalog.py:40-64`](../../../backend/models/src/erp_models/errors/catalogs/error_catalog.py#L40-L64)).
5. **Checking each entry:** every value becomes an `ErrorCodeEntry`, a frozen model ([`backend/models/src/erp_models/errors/entries/error_code_entry.py:20`](../../../backend/models/src/erp_models/errors/entries/error_code_entry.py#L20)). One validator per field, each with its own exception, tests the value against a strict pattern ([`error_code_entry.py:45-123`](../../../backend/models/src/erp_models/errors/entries/error_code_entry.py#L45-L123)), the patterns being at [lines 37-38](../../../backend/models/src/erp_models/errors/entries/error_code_entry.py#L37-L38).
6. **Resolving:** `resolve(code)` returns the entry or raises `SEErrorCatalogUnknownCode` ([`error_catalog.py:70-88`](../../../backend/models/src/erp_models/errors/catalogs/error_catalog.py#L70-L88)).
7. **The convention scan:** `ExceptionScanner` reads every source file with `ast` and grows the set of exception names from `Exception` and `BaseException` ([`tests/conventions/exceptions/exception_scanner.py:55-70`](../../../tests/conventions/exceptions/exception_scanner.py#L55-L70)). It derives the expected file name from the class name ([`exception_scanner.py:72-74`](../../../tests/conventions/exceptions/exception_scanner.py#L72-L74)), then reports misnamed (`SE` prefix), misplaced and unexported exceptions ([`exception_scanner.py:104-135`](../../../tests/conventions/exceptions/exception_scanner.py#L104-L135)). The three checks run on the repository in [`tests/conventions/exceptions/test_exception_conventions.py:10-16`](../../../tests/conventions/exceptions/test_exception_conventions.py#L10-L16).

## 🧱 Files and lines changed

<!-- changes -->
| File | Change | Lines in the new version | Added | Removed |
| --- | --- | --- | --- | --- |
| [`backend/models/README.md`](../../../backend/models/README.md) | Modified | [29-92](../../../backend/models/README.md#L29) | +64 | −1 |
| [`backend/models/conf/catalogs/error_codes.yaml`](../../../backend/models/conf/catalogs/error_codes.yaml) | Added | [1-23](../../../backend/models/conf/catalogs/error_codes.yaml#L1) | +23 | −0 |
| [`backend/models/src/erp_models/errors/__init__.py`](../../../backend/models/src/erp_models/errors/__init__.py) | Added | ➖ | +0 | −0 |
| [`backend/models/src/erp_models/errors/catalogs/__init__.py`](../../../backend/models/src/erp_models/errors/catalogs/__init__.py) | Added | ➖ | +0 | −0 |
| [`backend/models/src/erp_models/errors/catalogs/error_catalog.py`](../../../backend/models/src/erp_models/errors/catalogs/error_catalog.py) | Added | [1-88](../../../backend/models/src/erp_models/errors/catalogs/error_catalog.py#L1) | +88 | −0 |
| [`backend/models/src/erp_models/errors/catalogs/exceptions/__init__.py`](../../../backend/models/src/erp_models/errors/catalogs/exceptions/__init__.py) | Added | [1-11](../../../backend/models/src/erp_models/errors/catalogs/exceptions/__init__.py#L1) | +11 | −0 |
| [`backend/models/src/erp_models/errors/catalogs/exceptions/se_error_catalog_invalid_codes.py`](../../../backend/models/src/erp_models/errors/catalogs/exceptions/se_error_catalog_invalid_codes.py) | Added | [1-7](../../../backend/models/src/erp_models/errors/catalogs/exceptions/se_error_catalog_invalid_codes.py#L1) | +7 | −0 |
| [`backend/models/src/erp_models/errors/catalogs/exceptions/se_error_catalog_unknown_code.py`](../../../backend/models/src/erp_models/errors/catalogs/exceptions/se_error_catalog_unknown_code.py) | Added | [1-7](../../../backend/models/src/erp_models/errors/catalogs/exceptions/se_error_catalog_unknown_code.py#L1) | +7 | −0 |
| [`backend/models/src/erp_models/errors/catalogs/exceptions/se_error_catalog_unreadable.py`](../../../backend/models/src/erp_models/errors/catalogs/exceptions/se_error_catalog_unreadable.py) | Added | [1-7](../../../backend/models/src/erp_models/errors/catalogs/exceptions/se_error_catalog_unreadable.py#L1) | +7 | −0 |
| [`backend/models/src/erp_models/errors/catalogs/exceptions/se_invalid_error_catalog_exception.py`](../../../backend/models/src/erp_models/errors/catalogs/exceptions/se_invalid_error_catalog_exception.py) | Added | [1-11](../../../backend/models/src/erp_models/errors/catalogs/exceptions/se_invalid_error_catalog_exception.py#L1) | +11 | −0 |
| [`backend/models/src/erp_models/errors/entries/__init__.py`](../../../backend/models/src/erp_models/errors/entries/__init__.py) | Added | ➖ | +0 | −0 |
| [`backend/models/src/erp_models/errors/entries/error_code_entry.py`](../../../backend/models/src/erp_models/errors/entries/error_code_entry.py) | Added | [1-123](../../../backend/models/src/erp_models/errors/entries/error_code_entry.py#L1) | +123 | −0 |
| [`backend/models/src/erp_models/errors/entries/exceptions/__init__.py`](../../../backend/models/src/erp_models/errors/entries/exceptions/__init__.py) | Added | [1-13](../../../backend/models/src/erp_models/errors/entries/exceptions/__init__.py#L1) | +13 | −0 |
| [`backend/models/src/erp_models/errors/entries/exceptions/se_error_code_entry_invalid_action.py`](../../../backend/models/src/erp_models/errors/entries/exceptions/se_error_code_entry_invalid_action.py) | Added | [1-7](../../../backend/models/src/erp_models/errors/entries/exceptions/se_error_code_entry_invalid_action.py#L1) | +7 | −0 |
| [`backend/models/src/erp_models/errors/entries/exceptions/se_error_code_entry_invalid_reference.py`](../../../backend/models/src/erp_models/errors/entries/exceptions/se_error_code_entry_invalid_reference.py) | Added | [1-7](../../../backend/models/src/erp_models/errors/entries/exceptions/se_error_code_entry_invalid_reference.py#L1) | +7 | −0 |
| [`backend/models/src/erp_models/errors/entries/exceptions/se_error_code_entry_invalid_title.py`](../../../backend/models/src/erp_models/errors/entries/exceptions/se_error_code_entry_invalid_title.py) | Added | [1-7](../../../backend/models/src/erp_models/errors/entries/exceptions/se_error_code_entry_invalid_title.py#L1) | +7 | −0 |
| [`backend/models/src/erp_models/errors/entries/exceptions/se_error_code_entry_invalid_why.py`](../../../backend/models/src/erp_models/errors/entries/exceptions/se_error_code_entry_invalid_why.py) | Added | [1-7](../../../backend/models/src/erp_models/errors/entries/exceptions/se_error_code_entry_invalid_why.py#L1) | +7 | −0 |
| [`backend/models/src/erp_models/errors/entries/exceptions/se_invalid_error_code_entry_exception.py`](../../../backend/models/src/erp_models/errors/entries/exceptions/se_invalid_error_code_entry_exception.py) | Added | [1-11](../../../backend/models/src/erp_models/errors/entries/exceptions/se_invalid_error_code_entry_exception.py#L1) | +11 | −0 |
| [`backend/models/src/erp_models/exceptions/__init__.py`](../../../backend/models/src/erp_models/exceptions/__init__.py) | Added | [1-7](../../../backend/models/src/erp_models/exceptions/__init__.py#L1) | +7 | −0 |
| [`backend/models/src/erp_models/exceptions/se_error.py`](../../../backend/models/src/erp_models/exceptions/se_error.py) | Added | [1-19](../../../backend/models/src/erp_models/exceptions/se_error.py#L1) | +19 | −0 |
| [`backend/models/src/erp_models/exceptions/se_exception.py`](../../../backend/models/src/erp_models/exceptions/se_exception.py) | Added | [1-17](../../../backend/models/src/erp_models/exceptions/se_exception.py#L1) | +17 | −0 |
| [`backend/models/src/erp_models/exceptions/se_invalid_model_exception.py`](../../../backend/models/src/erp_models/exceptions/se_invalid_model_exception.py) | Added | [1-19](../../../backend/models/src/erp_models/exceptions/se_invalid_model_exception.py#L1) | +19 | −0 |
| [`backend/models/tests/errors/catalogs/test_error_catalog.py`](../../../backend/models/tests/errors/catalogs/test_error_catalog.py) | Added | [1-123](../../../backend/models/tests/errors/catalogs/test_error_catalog.py#L1) | +123 | −0 |
| [`backend/models/tests/errors/catalogs/test_error_codes_data.py`](../../../backend/models/tests/errors/catalogs/test_error_codes_data.py) | Added | [1-52](../../../backend/models/tests/errors/catalogs/test_error_codes_data.py#L1) | +52 | −0 |
| [`backend/models/tests/errors/entries/test_error_code_entry.py`](../../../backend/models/tests/errors/entries/test_error_code_entry.py) | Added | [1-139](../../../backend/models/tests/errors/entries/test_error_code_entry.py#L1) | +139 | −0 |
| [`backend/models/tests/exceptions/test_se_error.py`](../../../backend/models/tests/exceptions/test_se_error.py) | Added | [1-52](../../../backend/models/tests/exceptions/test_se_error.py#L1) | +52 | −0 |
| [`backend/models/tests/exceptions/test_se_exception.py`](../../../backend/models/tests/exceptions/test_se_exception.py) | Added | [1-47](../../../backend/models/tests/exceptions/test_se_exception.py#L1) | +47 | −0 |
| [`backend/models/tests/exceptions/test_se_invalid_model_exception.py`](../../../backend/models/tests/exceptions/test_se_invalid_model_exception.py) | Added | [1-51](../../../backend/models/tests/exceptions/test_se_invalid_model_exception.py#L1) | +51 | −0 |
| [`docs/technical/architecture/configuration.md`](../../../docs/technical/architecture/configuration.md) | Modified | [9](../../../docs/technical/architecture/configuration.md#L9) | +1 | −1 |
| [`tests/conventions/exceptions/exception_scanner.py`](../../../tests/conventions/exceptions/exception_scanner.py) | Added | [1-137](../../../tests/conventions/exceptions/exception_scanner.py#L1) | +137 | −0 |
| [`tests/conventions/exceptions/test_exception_conventions.py`](../../../tests/conventions/exceptions/test_exception_conventions.py) | Added | [1-17](../../../tests/conventions/exceptions/test_exception_conventions.py#L1) | +17 | −0 |
| [`tests/conventions/exceptions/test_exception_scanner.py`](../../../tests/conventions/exceptions/test_exception_scanner.py) | Added | [1-101](../../../tests/conventions/exceptions/test_exception_scanner.py#L1) | +101 | −0 |
| **32 files** | | | **+1175** | **−2** |
<!-- /changes -->

- [`backend/models/src/erp_models/exceptions/`](../../../backend/models/src/erp_models/exceptions/__init__.py): the three bases and their re-export. They are the contract the T0.14 problem+json handler reads through `CODE`.
- [`backend/models/src/erp_models/errors/entries/`](../../../backend/models/src/erp_models/errors/entries/error_code_entry.py): the entry model and its four field exceptions plus a model base.
- [`backend/models/src/erp_models/errors/catalogs/`](../../../backend/models/src/erp_models/errors/catalogs/error_catalog.py): the catalogue model and its four exceptions (unreadable, invalid codes, unknown code, base).
- [`backend/models/conf/catalogs/error_codes.yaml`](../../../backend/models/conf/catalogs/error_codes.yaml): the catalogue data, kept out of Python as AGENT.md requires.
- [`backend/models/tests/`](../../../backend/models/tests/errors/catalogs/test_error_catalog.py): tests of the bases, the entry, the catalogue and its data, written before the code.
- [`tests/conventions/exceptions/`](../../../tests/conventions/exceptions/exception_scanner.py): the scanner, the check on the repository, and tests on broken trees.
- [`backend/models/README.md`](../../../backend/models/README.md), lines [`25-93`](../../../backend/models/README.md#L25-L93): the bases, the catalogue flow and how to add a code.
- [`docs/technical/architecture/configuration.md`](../../../docs/technical/architecture/configuration.md): names the error catalogue as the first catalogue.

## 🧪 How to test it

```bash
uv run --all-packages pytest backend/models/tests -q -n 2
uv run --all-packages pytest tests/conventions/exceptions -q -n 2
uv run ruff check backend/models tests/conventions/exceptions
uv run mypy backend/models/src
```

The first runs the bases, the entry and the catalogue; the second runs the convention scan on the whole repository and on broken trees.

## 🔗 Evidence

- [pytest, backend/models](tests-evidences/pytest-backend-models.txt): 361 passed.
- [pytest, whole tests folder](tests-evidences/pytest.txt): 1174 passed.
- [pytest, lifecycle library](tests-evidences/pytest-backend-shared-lifecycle.txt): run to confirm nothing else broke.
- [ruff check](tests-evidences/ruff-check.txt), [ruff format](tests-evidences/ruff-format.txt) and [mypy](tests-evidences/mypy.txt): the checks on the ticket's files.
- [Plan view](tests-evidences/plan-view.txt) and [ticket references](tests-evidences/ticket-refs.txt): the plan and the specification links are up to date.

## 📝 Assumptions accepted

- The pytest project name is `erp-models`, as [`backend/models/pyproject.toml`](../../../backend/models/pyproject.toml) declares.
- `SEInvalidModelException` comes from K06 in the same ticket, so the import of the entry tests resolves.
- A bad value of any type is refused with the field's own exception. A missing field or an unknown key raises `ValidationError`, and assigning to a frozen model raises `ValidationError`.
- `codes` has no default: a missing one raises `ValidationError`, `None` raises `SEErrorCatalogInvalidCodes`, and an empty model is refused.
- A bad entry (empty title) raises `SEErrorCodeEntryInvalidTitle`, because `ErrorCodeEntry` validates the entries.
- The catalogue lives at [`backend/models/conf/catalogs/error_codes.yaml`](../../../backend/models/conf/catalogs/error_codes.yaml), mirroring a service's `conf/catalogs/`.
- The entry exposes `title`, `why`, `action` and `reference`, and `erp_models.exceptions` exports the three bases, each with a `CODE`.
- The scanner finds no offender on the repository tree. It reports one offender per problem, counts a missing `__init__.py` as a missing `__all__`, reads only top-level classes and resolves bases by name only.
- The workers ran the main checkout's `.venv` because other tickets' uncommitted packages broke `uv run`. The verifier re-ran every check in a clean tree holding only T0.04, so the evidence is valid.
- Each base lists `CODE` under Attributes and has a Notes section on D122. Exception files carry no import-group comments.
- Patterns are matched with `re.fullmatch` on the stripped value, so the anchors are redundant but harmless.
- `SEErrorCatalogUnreadable` subclasses `SEInvalidErrorCatalogException`, not `SEYamlCatalogUnreadable`, as AGENT.md asks for the model's own `UNREADABLE`. Non-string keys are refused with `SEErrorCatalogInvalidCodes`.
- Message keys follow `errors.<code in snake case>.title|why|action`: the plan's choice, since the specifications fix no key format.
- The README names (`ErrorCatalog`, `resolve`, `load`, `SEErrorCatalogUnknownCode`, `SEErrorCatalogUnreadable`, the `SITE-CLOSE-01` sample) match the built code. The P2 translation catalogues are named only as the future home of the texts, as TICKET.md puts REQ-T10-01 out of scope.
- `SEException` is a root above the two AGENT.md bases, with the codes `UNEXPECTED-ERROR-01`, `SERVICE-FAILURE-01` and `INVALID-INPUT-01`: the "codes the bases need" of TICKET.md.
- The fields are not named `*_key`, because AGENT.md reserves `_key` for secret store entries. The strict code and key patterns are inferred from D122 and make criterion 3 checkable.

## 🔜 Follow-ups

| File | What to change |
| --- | --- |
| [`backend/models/README.md`](../../../backend/models/README.md), the T0.03 exceptions such as [`se_invalid_money_exception.py`](../../../backend/models/src/erp_models/money/exceptions/se_invalid_money_exception.py) and [`se_invalid_opaque_id_exception.py`](../../../backend/models/src/erp_models/base/exceptions/se_invalid_opaque_id_exception.py) | In a later ticket, rebase the T0.03 model bases on `SEInvalidModelException` so they inherit a `CODE` the T0.14 handler can resolve, and add a rule that every `SE` exception derives from `SEException`. Until then, say in the README that new exceptions derive from the bases. |
| [`tests/conventions/exceptions/exception_scanner.py`](../../../tests/conventions/exceptions/exception_scanner.py), [`test_exception_scanner.py`](../../../tests/conventions/exceptions/test_exception_scanner.py) | Add every built-in exception name to the roots, and a broken-tree case for a non-`SE` class based on `ValueError`. |
| [`backend/models/tests/errors/catalogs/test_error_codes_data.py`](../../../backend/models/tests/errors/catalogs/test_error_codes_data.py) | Test that `reference == code` and that each message key starts with `errors.<code in snake case>`. |
| [`backend/models/README.md`](../../../backend/models/README.md) | Drop the clause that the reference points to the specification, or say only that it is the support code shown as `ref. SITE-CLOSE-01` by D122. |
| [`error_catalog.py`](../../../backend/models/src/erp_models/errors/catalogs/error_catalog.py), [`error_code_entry.py`](../../../backend/models/src/erp_models/errors/entries/error_code_entry.py) | Reuse `ErrorCodeEntry.REFERENCE_PATTERN` in `ErrorCatalog`, and consider a read-only mapping for `codes`. |
| [`backend/models/tests/errors/entries/test_error_code_entry.py`](../../../backend/models/tests/errors/entries/test_error_code_entry.py) | Rename `test_none_becomes_the_default` to `test_none_is_refused_because_no_field_has_a_default`. |
| [`backend/models/README.md`](../../../backend/models/README.md) | Record how a service image finds the catalogue (copied into its `conf/` or packaged as data), or leave it to T0.14. |
