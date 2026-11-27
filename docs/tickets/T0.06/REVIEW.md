# T0.06: Review note

**Verdict:** ✅ Approved · **Branch:** `feature/tickets`

## What changed

- `erp_logging` (`backend/shared/logging`) applies a service's `conf/logger.yaml` from one reference file. The output goes to a coloured console, a coloured rotating `logs/simpleerp.log` and `logs/simpleerp.jsonl`. `LoggingSetup` injects the service name and moves every handler file into the service's `logs/` folder.
- `ContextFilter`, on every handler, tags each record with `service`, `company` and `request`. The company and the request are read from `LogContext` (contextvars, so each task has its own values) and are written as `-` when unbound. `JsonLinesFormatter` writes a fixed whitelist of keys only, so an extra such as `password_key` never reaches the JSON lines (D240, D416).
- `erp_config` (`backend/shared/config`) has `AppConfigLoader[T].read()`. It refuses a `conf/app.yaml` that leaves out any default (D413), checks this before the overrides, then applies `ERP__SECTION__FIELD` variables through `EnvironmentOverrides`, parsed as YAML and never logged.
- `ConfigSection` is frozen, refuses unknown keys, accepts a `_key` value only as a vault entry name (`[A-Za-z0-9][A-Za-z0-9._/-]*`, at most 128 characters), and masks it as `***` in `repr` and `str` (D240).
- Both libraries are their own uv packages, wired into the root workspace (D438), with READMEs. The back-end and observability design pages now describe them.

## Acceptance criteria

| Criterion | Evidence | Result |
| --- | --- | --- |
| 1. Given a default in `conf/app.yaml`, when the matching environment variable is set, then the loaded configuration holds the environment value | `test_an_environment_variable_overrides_a_default`, `test_an_environment_value_replaces_the_default`; tests-evidences/pytest-backend-shared-config.txt (43 passed) | ✅ Pass |
| 2. Given a configuration with a `_key` field, when it is loaded and logged, then the `_key` value never appears in a log line, and the field only names a vault entry | `test_a_key_value_never_appears_in_a_log_line`, `test_a_key_that_is_not_an_entry_name_is_refused`, `test_repr_and_str_mask_the_vault_entry_name`, `test_an_extra_attribute_ending_in_key_is_not_written`; tests-evidences/pytest-backend-shared-config.txt, pytest-backend-shared-logging.txt | ✅ Pass |
| 3. Given the logging set up from `conf/logger.yaml`, when a line is written, then it carries the service, the company as an opaque id and the request | `test_every_line_carries_the_service_the_company_and_the_request` (console, text file, JSON lines); tests-evidences/pytest-backend-shared-logging.txt (40 passed) | ✅ Pass |
| 4. Given the two libraries, when the tests and the convention tests run, then they pass, with the libraries in `backend/shared/logging` and `backend/shared/config` | tests-evidences/pytest.txt (1156 passed, `tests/conventions` included), ruff-check.txt, ruff-format.txt, mypy.txt | ✅ Pass |

## Look at first

- **Secrets out of logs and repr (D240):** read line by line `backend/shared/config/src/erp_config/models/config_section.py` (the before-validator and `__repr_args__`), `backend/shared/config/src/erp_config/loading/app_config_loader.py` (only `type(error).__name__` is logged, never a value) and `backend/shared/logging/src/erp_logging/formatters/json_lines_formatter.py` (the key whitelist). The `_key` check covers input values only, not class defaults (follow-up).
- **Company tag isolation (D416):** `backend/shared/logging/src/erp_logging/context/log_context.py` and `filters/context_filter.py`. Values live in contextvars and a child task's binding does not leak (`test_a_value_bound_in_a_task_does_not_leak_to_the_caller`). `bind` sets the variables with no token reset, so T0.09's middleware must bind once in each request's own task.
- **Logging setup:** `backend/shared/logging/src/erp_logging/setup/logging_setup.py`. The service is injected, every handler file is rewritten into `logs_dir`, `disable_existing_loggers` defaults to False, and `dictConfig` errors are wrapped.
- **Override parsing:** `backend/shared/config/src/erp_config/loading/environment_overrides.py`. YAML 1.1 parsing turns `no`/`on` into booleans and turns numeric strings into numbers (follow-up).
- **Docs:** `docs/technical/architecture/backend.md` links an anchor in `configuration.md` that the delivered diff does not contain. K19's configuration.md change is missing, because T0.04 holds that file uncommitted.

## Assumptions accepted

- All worker assumptions K01 to K20 are accepted, except the two below. Each is consistent with D413, D416, D240 and D438 and with the brief (see the structured list).
- K19 "The erp_config section was added as a new heading in configuration.md": **rejected**. No such section is in the ticket's diff (follow-up).
- K03 "make_record is a module-level function, as other test files do": **rejected** as a rule reading, because AGENT.md allows no module-level helper outside helpers.py. It is not blocking (follow-up).
- TICKET.md assumptions (decisions linked in place of use cases, folder names from D572, tag names, logger.yaml shape): accepted.

## Follow-ups

- Link backend.md to configuration.md without the missing anchor. After T0.04 merges, add the erp_config section to configuration.md and mark `conf/app.yaml` as built (K19).
- Move `make_record` into the test class or a helpers.py (K03).
- Fix or remove the misplaced import group comments in the four sample section files (K05/K07).
- Make override parsing type-aware, or document YAML 1.1 coercions (`no`, `on`, octal, numeric vault names) (K15/K06).
- Check `_key` defaults declared on a subclass, not only input values (K14/K05).
- Check written defaults for Optional, list and dict sections, or document the limit (K17/K07).
- Redraw the observability diagram with ContextFilter on the handlers, and say `-` rather than "empty" (K19).
- The convention scanner sees only direct `BaseModel` subclasses: decide on test-only model subclasses (conventions, outside this ticket).
</content>
