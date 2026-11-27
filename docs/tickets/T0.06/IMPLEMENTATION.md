# T0.06: Implementation choices

**Ticket:** [TICKET.md](TICKET.md) · **How it works:** [EXPLAIN.md](EXPLAIN.md) · **Review:** [REVIEW.md](REVIEW.md)

## 🎯 Constraints

- Every default is written in the service's `app.yaml`, and an environment variable overrides it (D413, acceptance criterion 1 of [TICKET.md](TICKET.md)).
- A `_key` field names a vault entry, and its value never appears in a log line or a `repr` (D240, criterion 2).
- Every log line carries the service, the company as an opaque id and the request, and one company's id never leaks to another request (D416, criterion 3).
- The two libraries live in `backend/shared/logging` and `backend/shared/config`, as uv workspace members (D438, criterion 4).
- [AGENT.md](../../../AGENT.md): one class per file, no module-level code, no `Any`, at most five files per folder, no underscore attributes, a log line per method, never a typed value in a log.

## ⚖️ Choices at a glance

| # | Decision | Chosen | Main alternative | Trade-off accepted |
| --- | --- | --- | --- | --- |
| [D1](#d1) | How the company and request reach the log | Two `ContextVar`s read by a filter | One `ContextVar` holding a pair, or tokens | `bind` has no reset, so T0.09 must bind once per task |
| [D2](#d2) | What the JSON line holds | A fixed whitelist of keys | Copy `record.__dict__` | A new field needs a code change |
| [D3](#d3) | When the `_key` check runs | `mode="before"` model validator | `mode="after"` | Reads raw keys, would miss aliases |
| [D4](#d4) | How `_key` values are hidden | Mask in `__repr_args__` | `Field(repr=False)` or `SecretStr` | Defaults on a subclass are not checked |
| [D5](#d5) | When missing defaults are detected | On the raw file, before overrides | After the overrides | Only direct sections are recursed into |
| [D6](#d6) | How override values are typed | `yaml.safe_load`, raw text on failure | Keep every value a string | YAML 1.1 coercions (`no`, `on`) |
| [D7](#d7) | How overrides are applied | Walk a deep copy and replace | Rebuild recursively | Copies all data |
| [D8](#d8) | What gets logged on errors | Only `type(error).__name__` | The error text | Less to debug with |
| [D9](#d9) | The service and file locations in logging | Injected into the reference file | One file per service | `disable_existing_loggers` forced to default `False` |
| [D10](#d10) | Time format in JSON | `datetime` in UTC, truncated to ms | `strftime` or `formatTime` | A string replace of `+00:00` |
| [D11](#d11) | Exception layout and base | Two sub-packages, deriving from `Exception` | One flat folder, or `ValueError` | Not catchable as `ValueError` |
| [D12](#d12) | Loader generics and method name | PEP 695 `AppConfigLoader[T]` with `read()` | Module `TypeVar`, `load` | None beyond syntax |
| [D13](#d13) | Test helpers and fixtures | Methods of the test class, autouse clean-up fixtures | Module functions, a `helpers.py` | Helpers sit among the tests |
| [D14](#d14) | Root workspace wiring | Root dependencies and sources | Rely on the `backend/shared/*` glob | Two more root dependencies |
| [D15](#d15) | Where the library design is documented | Existing pages plus READMEs | New section in `configuration.md` | `configuration.md` unchanged for now |

## <a id="d1"></a>D1: How the company and request reach the log

**Chosen:** two `ClassVar` `ContextVar`s, read through accessors by the filter · **Where:** [`backend/shared/logging/src/erp_logging/context/log_context.py:22-23`](../../../backend/shared/logging/src/erp_logging/context/log_context.py#L22-L23) and [`context_filter.py:54`](../../../backend/shared/logging/src/erp_logging/filters/context_filter.py#L54) · **Source:** K12, K16

| Option | For | Against |
| --- | --- | --- |
| ✅ Two `ContextVar`s, set by `bind` and `clear` | Match the company and request contract of the brief. Each async task has its own value, which D416 needs. `bind` stays simple | No previous binding is restored |
| One `ContextVar` with a frozen pair | One variable to manage | Not chosen by the worker beyond the brief's two-variable contract |
| Tokens or a context manager | Restores the previous binding | The brief and tests ask only for `bind` and `clear` |
| Read the `ContextVar`s directly in the filter | Fewer calls | Ties the filter to `LogContext` internals (K16) |

**Trade-off:** no reset handling. `or` also turns an empty string into `-`, the safer log tag.

**Revisit when:** T0.09's middleware needs to nest bindings in one task.

## <a id="d2"></a>D2: What the JSON line holds

**Chosen:** build a dict from the `FIELDS` keys and `json.dumps(ensure_ascii=False)` · **Where:** [`json_lines_formatter.py:31-51`](../../../backend/shared/logging/src/erp_logging/formatters/json_lines_formatter.py#L31-L51) · **Source:** K13

| Option | For | Against |
| --- | --- | --- |
| ✅ Explicit whitelist | An extra such as `password_key` can never leak (D240). `json` escaping guarantees one line | A new field needs a code change |
| Copy and filter `record.__dict__` | New extras appear for free | A secret attribute would need to be filtered out each time |
| A third-party JSON logging library | Less code | Adds a dependency, and its field rules are not ours (named by the worker, no further reason given) |

**Trade-off:** rigidity for safety, matching criterion 2.

**Revisit when:** a service needs structured extras in its lines: add them to `FIELDS` with a test.

## <a id="d3"></a>D3: When the `_key` check runs

**Chosen:** a `model_validator(mode="before")` on the raw input · **Where:** [`config_section.py:38`](../../../backend/shared/config/src/erp_config/models/config_section.py#L38) · **Source:** K14

| Option | For | Against |
| --- | --- | --- |
| ✅ `mode="before"` | `42` and `True` raise `SEConfigSectionInvalidKey`, as the tests expect | Reads dict keys, so it misses field aliases (the section has none) |
| `mode="after"` (the brief) | Sees typed fields | Pydantic's own `str` check refuses a bool or int first, as a `ValidationError` |

**Trade-off:** a gap for aliases, which no section uses.

**Revisit when:** a section declares an alias on a `_key` field.

## <a id="d4"></a>D4: How `_key` values are hidden

**Chosen:** wrap `__repr_args__` and replace each `_key` value with `***` · **Where:** [`config_section.py:73`](../../../backend/shared/config/src/erp_config/models/config_section.py#L73) · **Source:** K14

| Option | For | Against |
| --- | --- | --- |
| ✅ Mask in `__repr_args__` | Automatic for every subclass, no per-field setup | A `_key` default on a subclass is not checked (review follow-up) |
| `Field(repr=False)` per field | Built in | Each field must remember it |
| `SecretStr` | Built in | Would change the field type from a vault entry name |

**Trade-off:** convenience over a check of defaults.

**Revisit when:** the follow-up on `_key` defaults is taken.

## <a id="d5"></a>D5: When missing defaults are detected

**Chosen:** check the raw file data before the overrides · **Where:** [`app_config_loader.py:134`](../../../backend/shared/config/src/erp_config/loading/app_config_loader.py#L134) and [`app_config_loader.py:83`](../../../backend/shared/config/src/erp_config/loading/app_config_loader.py#L83) · **Source:** K17

| Option | For | Against |
| --- | --- | --- |
| ✅ Raw data, before overrides | An override can never hide a missing default (D413). Simple | Recurses only into fields annotated directly as a `ConfigSection` |
| After the overrides | Sees the final data | An override could fill a field the file lacks |
| Compare model defaults with the file | Direct | Not chosen by the worker beyond the brief |

**Trade-off:** `Optional`, list and dict sections are not checked (follow-up).

**Revisit when:** a service declares such a section.

## <a id="d6"></a>D6: How override values are typed

**Chosen:** `yaml.safe_load`, the raw string on a `YAMLError` · **Where:** [`environment_overrides.py:48`](../../../backend/shared/config/src/erp_config/loading/environment_overrides.py#L48) · **Source:** K15

| Option | For | Against |
| --- | --- | --- |
| ✅ YAML parse | Typed ints and booleans, as the brief says | YAML 1.1: `no` becomes `False`, `0755` an octal, a numeric vault name an int |
| Every value a string | Predictable | Pydantic lax mode would still need to convert, and lists and maps are lost |
| JSON parse | Stricter | Plain words would need quotes (named by the worker, no further reason given) |

**Trade-off:** surprising coercions of a few strings, listed as a follow-up.

**Revisit when:** a variable meets one of them, or the loader parses against the field type.

## <a id="d7"></a>D7: How overrides are applied

**Chosen:** walk each path iteratively on a deep copy and replace in place · **Where:** [`environment_overrides.py:79`](../../../backend/shared/config/src/erp_config/loading/environment_overrides.py#L79) and [`:113`](../../../backend/shared/config/src/erp_config/loading/environment_overrides.py#L113) · **Source:** K15

| Option | For | Against |
| --- | --- | --- |
| ✅ Deep copy and replace | The input stays untouched, which a test checks | Copies all data even when no variable applies |
| Rebuild the dict recursively | No mutation | More code |
| Flatten to dotted keys | Simple lookup | Needs to be unflattened again |

**Trade-off:** a small copy at start-up. The failure is built by [`environment_overrides.py:64`](../../../backend/shared/config/src/erp_config/loading/environment_overrides.py#L64), which logs once and sets the cause, though the cause is rarely present.

**Revisit when:** configuration becomes large enough for the copy to show.

## <a id="d8"></a>D8: What gets logged on errors

**Chosen:** only `type(error).__name__`, with the cause chained · **Where:** [`app_config_loader.py:106`](../../../backend/shared/config/src/erp_config/loading/app_config_loader.py#L106) and [`logging_setup.py:118`](../../../backend/shared/logging/src/erp_logging/setup/logging_setup.py#L118) · **Source:** K17, K18

| Option | For | Against |
| --- | --- | --- |
| ✅ Type name only, `raise ... from error` | A pydantic error can quote the input, which may name a vault entry (D240). AGENT.md says never to log a typed value | Less to debug with, though the chain keeps the cause |
| Log `str(error)` | Detailed | May leak a value |

**Trade-off:** debugging detail for safety.

**Revisit when:** never for values: add detail only through the exception chain.

## <a id="d9"></a>D9: Service and file locations in logging

**Chosen:** one reference file, with the service injected and every file moved into `logs_dir` · **Where:** [`logging_setup.py:83`](../../../backend/shared/logging/src/erp_logging/setup/logging_setup.py#L83) and [`:104`](../../../backend/shared/logging/src/erp_logging/setup/logging_setup.py#L104) · **Source:** K18, K11, K19

| Option | For | Against |
| --- | --- | --- |
| ✅ Inject into the reference [`logger.yaml`](../../../backend/shared/logging/conf/logger.yaml) | One file for every service, kept correct in one place | The page of the design no longer lists a per-service file |
| A `logger.yaml` per service | Free to differ | Copies drift |
| Leave `disable_existing_loggers` at the `dictConfig` default `True` | No code | Loggers created earlier would go silent, and a test fails depending on order |

**Trade-off:** `setdefault(False)` lets a file still set it.

**Revisit when:** a service needs its own handlers: allow an override file.

## <a id="d10"></a>D10: Time format in JSON

**Chosen:** `datetime.fromtimestamp(created, tz=UTC)` with `isoformat(timespec="milliseconds")` and `Z` · **Where:** [`json_lines_formatter.py:40-42`](../../../backend/shared/logging/src/erp_logging/formatters/json_lines_formatter.py#L40-L42) · **Source:** K13

| Option | For | Against |
| --- | --- | --- |
| ✅ `datetime` | Exact, truncates to milliseconds, independent of the local timezone | The `+00:00` to `Z` replace is a small trick |
| `time.strftime` plus manual ms | Familiar | More code |
| `Formatter.formatTime` | Built in | Uses the local time zone by default (named by the worker, no further reason given) |

**Trade-off:** one string replace.

**Revisit when:** a consumer needs microseconds.

## <a id="d11"></a>D11: Exception layout and base

**Chosen:** `sections/` and `loading/` sub-packages re-exported by a sorted `__all__`, deriving from `Exception` · **Where:** [`backend/shared/config/src/erp_config/models/exceptions/__init__.py`](../../../backend/shared/config/src/erp_config/models/exceptions/__init__.py) and [`se_app_config_error.py:5`](../../../backend/shared/config/src/erp_config/models/exceptions/loading/se_app_config_error.py#L5) · **Source:** K10

| Option | For | Against |
| --- | --- | --- |
| ✅ Sub-packages, `Exception` base | Respects the five-file limit. Pydantic does not wrap them, so tests assert the specific type | Two packages for seven classes. Not catchable as `ValueError` |
| One flat folder | One package | Breaks the five-file limit |
| `ValueError` base | Catchable generically | Pydantic would wrap it in a `ValidationError` |

**Trade-off:** callers catch the `SE` types.

**Revisit when:** a caller needs a generic catch.

## <a id="d12"></a>D12: Loader generics and method name

**Chosen:** `class AppConfigLoader[T: ConfigSection]` with `read()` · **Where:** [`app_config_loader.py:23`](../../../backend/shared/config/src/erp_config/loading/app_config_loader.py#L23) · **Source:** K17

| Option | For | Against |
| --- | --- | --- |
| ✅ PEP 695 and `read` | No module-level code, and no clash with `YamlCatalog.load` | Python 3.13 syntax (the repository requires it) |
| Module `TypeVar` | Familiar | Breaks the no-module-level rule |
| A method `load` | Usual name | Clashes with `YamlCatalog.load` |

**Trade-off:** none worth noting.

**Revisit when:** the loader and `YamlCatalog` share a base.

## <a id="d13"></a>D13: Test helpers and fixtures

**Chosen:** helpers as methods of the test class, autouse fixtures that clear shared state before and after, indirect parametrised `environ` for the loader tests · **Where:** [`test_log_context.py:11`](../../../backend/shared/logging/tests/context/test_log_context.py#L11), [`conftest.py:12`](../../../backend/shared/logging/tests/context/conftest.py#L12), [`app_config_loader/conftest.py:30`](../../../backend/shared/config/tests/loading/app_config_loader/conftest.py#L30), [`test_environment_overrides.py:12`](../../../backend/shared/config/tests/loading/test_environment_overrides.py#L12) · **Source:** K01, K02, K06, K07

| Option | For | Against |
| --- | --- | --- |
| ✅ Methods and flat fixtures | Meets the one-class and no-module-code rules, and nested functions are banned by `tests/conventions`. Clearing before and after protects against a failing test | Helpers sit among the tests. Long inline YAML strings |
| Module-level helper functions | Short | Forbidden by AGENT.md (the review also rejected K03's `make_record`, see follow-up) |
| A separate `helpers.py` | Allowed by AGENT.md | One more file per folder. Not chosen by the workers |
| Fixture files on disk | Readable YAML | The cases would sit away from their assertions |

Other test choices: [`test_json_lines_formatter.py:12`](../../../backend/shared/logging/tests/formatters/test_json_lines_formatter.py#L12) builds real `LogRecord` objects, which tests the formatter alone, where a logger with a handler would also cover wiring. [`test_logging_setup.py:51`](../../../backend/shared/logging/tests/setup/test_logging_setup.py#L51) checks the tags in the JSON values, so it does not depend on the key names. [`test_config_section.py:47`](../../../backend/shared/config/tests/models/config_section/test_config_section.py#L47) expects pydantic's `ValidationError` on assigning to a frozen model.

**Trade-off:** readability against strict conventions.

**Revisit when:** the convention tests allow a `helpers.py` more often.

## <a id="d14"></a>D14: Root workspace wiring

**Chosen:** add both libraries to the root dependencies and `[tool.uv.sources]` · **Where:** [`pyproject.toml:8-15`](../../../pyproject.toml#L8-L15) · **Source:** K08

| Option | For | Against |
| --- | --- | --- |
| ✅ Explicit sources, like `erp-lifecycle` | The root can import them for the tests run from the root | Two more root dependencies |
| Rely on the `backend/shared/*` glob | No root change | The root would not import them |

Dependency floors: `colorlog>=6.12.0` equals the locked version, as the brief says, and pydantic and pyyaml take the floors of `erp_models`. A looser floor would admit older releases, at the risk of untested ones.

**Trade-off:** a tight floor.

**Revisit when:** a service needs an older `colorlog`.

## <a id="d15"></a>D15: Where the library design is documented

**Chosen:** edit [`backend.md`](../../../docs/technical/architecture/backend.md) and [`observability.md`](../../../docs/technical/operations/observability.md), and write a README per library · **Where:** [`observability.md:7`](../../../docs/technical/operations/observability.md#L7), [`README.md`](../../../backend/shared/logging/README.md) and [`README.md`](../../../backend/shared/config/README.md) · **Source:** K19, K20, review

| Option | For | Against |
| --- | --- | --- |
| ✅ Existing pages plus short READMEs with relative links | Links resolve locally and are checked | Break if a folder moves |
| A new "Shared configuration library" section in `configuration.md` (K19's plan) | Rules next to the file table | T0.04 holds that file uncommitted (TKT-16), so it is not in this diff, and [`backend.md:15`](../../../docs/technical/architecture/backend.md#L15) links an anchor that does not exist |
| One README for both | Fewer files | The brief asks for one each. Not chosen beyond that |
| A Mermaid diagram of the three outputs | Shows where the tags go | Draws them from `LogContext` instead of the filter on the handlers (follow-up) |

**Trade-off:** the documentation is incomplete until T0.04 merges.

**Revisit when:** T0.04 has merged: add the section and fix the link.

## 📝 Assumptions behind the choices

- K12: the `ContextVar` names and a `bind` without tokens, so T0.09 binds once per request task: supports [D1](#d1).
- K14: the `_key` check runs before field validation: supports [D3](#d3) and [D4](#d4).
- K15: the last path segment must already exist, and messages never quote a value: supports [D6](#d6), [D7](#d7).
- K17: nested non-mapping sections are left to model validation: supports [D5](#d5).
- K09, K10: the exceptions subclass `Exception`: supports [D11](#d11).
- K08: workspace sources like `erp-lifecycle`: supports [D14](#d14).
- K18: `disable_existing_loggers` defaults to `False`: supports [D9](#d9).
- K19: the observability page says only the logging library is built: supports [D15](#d15).
