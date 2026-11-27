# T0.04: Review note

**Verdict:** ✅ Approved · **Branch:** `feature/tickets`

## What changed

- Three `SE` bases now sit in `erp_models.exceptions`: the root `SEException`, the layer base `SEError` and the model base `SEInvalidModelException`. Each carries a `CODE` class constant that subclasses inherit or override. None of them subclasses `ValueError`, so Pydantic never wraps them in a `ValidationError`.
- The D122 error code catalogue is data in `backend/models/conf/catalogs/error_codes.yaml`. It holds the three base codes and the D122 sample `SITE-CLOSE-01`, each with a title, why and action translation key and a support reference.
- `ErrorCatalog`, a `YamlCatalog`, and `ErrorCodeEntry`, a frozen model, validate the file. Codes and keys follow strict patterns, so no free text (and no secret) fits in them. `resolve(code)` refuses an unknown code with `SEErrorCatalogUnknownCode`.
- A new convention check, `tests/conventions/exceptions/`, enforces the AGENT.md exception rules on every Python package. The rules are: the name starts with `SE`, the file is named after the class and sits inside an `exceptions/` folder, and the class is listed in a sorted `__all__`. It reads the code with `ast` only and is tested on broken trees.
- `backend/models/README.md` documents the bases, the catalogue and how to add a code. `configuration.md` names the first catalogue.

## Acceptance criteria

| Criterion | Evidence | Result |
| --- | --- | --- |
| 1. Given any code of the catalogue, when it is resolved, then it gives its title key, why key, action key and support reference | `test_error_codes_data.py::test_every_code_has_a_title_a_why_an_action_and_a_reference`, `test_error_catalog.py::test_a_known_code_resolves_to_its_four_values`; tests-evidences/pytest-backend-models.txt (361 passed) | ✅ Pass |
| 2. Given a code not in the catalogue, when the model is asked for it, then it is refused | `test_error_catalog.py::test_an_unknown_code_is_refused` (unknown, empty and lower-case codes) | ✅ Pass |
| 3. Given every message of the catalogue, when it is read, then none holds a secret | `test_error_codes_data.py::test_no_key_or_reference_holds_a_secret_word` and `test_every_message_key_is_a_lower_case_dotted_key`, plus the strict patterns of `ErrorCodeEntry` | ✅ Pass |
| 4. Given the `SE` bases, when `tests/conventions/` runs, then they follow AGENT.md (one per file, `SE...`, sorted `__all__`) | `tests/conventions/exceptions/test_exception_conventions.py`, `test_exception_scanner.py`; tests-evidences/pytest.txt (1174 passed) | ✅ Pass |

## Look at first

- **Exception hierarchy and codes**: `backend/models/src/erp_models/exceptions/se_exception.py`, `se_error.py`, `se_invalid_model_exception.py`. This is the contract the T0.14 problem+json handler will read through `CODE`.
- **Validation of the catalogue**: `backend/models/src/erp_models/errors/entries/error_code_entry.py` (one validator per field, each with its own exception) and `backend/models/src/erp_models/errors/catalogs/error_catalog.py` (`validate_codes` checks the keys, `resolve` refuses an unknown code).
- **Convention scanner**: `tests/conventions/exceptions/exception_scanner.py`. It finds exceptions by base name, followed through other exceptions, so a class based on another built-in exception (such as `ValueError`) is not seen yet (see the follow-ups).
- **Identity, permissions and company data isolation**: the ticket has none. It adds no route, no store and no company data. Error messages are translation keys only, which keeps secrets out of errors (REQ-T05-03, criterion 2).

## Assumptions accepted

- The `SEException` root and the three base codes are the "codes the bases need" of TICKET.md. Accepted: no specification fixes them.
- The code format `WORD-WORD-NN` is inferred from the D122 sample, and the key format `errors.<code>.<part>` is the plan's choice. Accepted: the strict formats are what make criterion 3 checkable.
- The fields are `title`, `why`, `action` and `reference`, not `*_key`. Accepted: AGENT.md reserves `_key` for secret store entries.
- `SEErrorCatalogUnreadable` is the model's own exception, not a subclass of `SEYamlCatalogUnreadable`. Accepted: this is the `UNREADABLE` contract of AGENT.md.
- Workers ran the main checkout's .venv because other tickets' packages broke `uv run`. Accepted: the verifier re-ran every check in a clean tree holding only T0.04.
- Every other worker assumption (pytest names, ValidationError for missing or unknown keys and frozen assignment, the file location, the README names) was checked against the built code and accepted.

## Follow-ups

- The T0.03 model bases (`SEInvalidMoneyException` and the others) still subclass plain `Exception`, so they carry no `CODE`. The README claims every shared error derives from the bases. Rebase them in a later ticket, before T0.14, or soften the sentence.
- The scanner's roots should include every built-in exception, so that a `ValueError`-based class cannot slip through.
- Add a data test that `reference == code` and that the message keys match the code.
- Drop the invented README clause that the reference "points to the specification".
- The code pattern is written twice, and the frozen catalogue still exposes a mutable `codes` dict.
- Rename `test_none_becomes_the_default` in `test_error_code_entry.py`: it asserts a refusal.
- The installed `erp_models` package does not ship `backend/models/conf/`. T0.14 must decide how a service image finds the catalogue.
