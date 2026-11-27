# T0.04: Implementation choices

**Ticket:** [TICKET.md](TICKET.md) · **How it works:** [EXPLAIN.md](EXPLAIN.md) · **Review:** [REVIEW.md](REVIEW.md)

## 🎯 Constraints

- One class per file, no module constants, one exception per file with a sorted `__all__`, no `_key` field names and no `Any`: the rules of [`AGENT.md`](../../../AGENT.md).
- Data is not hard-coded in Python: it goes in `conf/catalogs/*.yaml`, loaded by a `YamlCatalog` ([`AGENT.md`](../../../AGENT.md), [`backend/models/src/erp_models/catalogs/yaml_catalog.py`](../../../backend/models/src/erp_models/catalogs/yaml_catalog.py)).
- Every message is a translation key and never holds a secret: criteria 2 and 3 of [TICKET.md](TICKET.md) (REQ-T05-03).
- The shared bases must not make Pydantic wrap them in a `ValidationError`, so they cannot subclass `ValueError`.
- Models follow the T0.03 pattern ([`backend/models/src/erp_models/base/frozen_erp_model.py`](../../../backend/models/src/erp_models/base/frozen_erp_model.py)).

## ⚖️ Choices at a glance

| # | Decision | Chosen | Main alternative | Trade-off accepted |
| --- | --- | --- | --- | --- |
| [D1](#d1) | Where the `CODE` lives | A `ClassVar` on a root `SEException` | A code table outside the classes | Older T0.03 exceptions carry no code yet |
| [D2](#d2) | How the entry is validated | One validator per field, strict patterns | A shared validator | Some repetition |
| [D3](#d3) | Who validates the entries | `ErrorCodeEntry`, not `validate_codes` | Validate inside `validate_codes` | A bad entry is not reported by the catalogue exception |
| [D4](#d4) | Entry base class | `FrozenErpModel` | Plain `BaseModel` | Depends on `erp_models.base` |
| [D5](#d5) | Unknown code lookup | `dict.get`, then raise | Catch `KeyError` | No chained cause |
| [D6](#d6) | How the scanner reads code | `ast`, bases by name | Import and `issubclass` | Same-named classes are confused, built-in bases missed |
| [D7](#d7) | Expected file name | Regex on word boundaries | Underscore before every capital | Odd acronyms may split unexpectedly |
| [D8](#d8) | Scanner tests | One table of broken trees | One test per tree | A failure needs a tuple to read |
| [D9](#d9) | Test data and subclasses | Class attributes, `type(...)` subclasses, inline helpers | Module constants, nested or extra classes | Less readable, a little repeated data |
| [D10](#d10) | Data test loop | A loop in one test | Parametrise over codes | One test reports many codes |
| [D11](#d11) | Where it is documented | A section of the models README | A page in `docs/technical/` | One README to keep current |

## <a id="d1"></a>D1: Where the `CODE` lives

**Chosen:** a `CODE` `ClassVar` on a root `SEException`, overridden by the two AGENT.md bases · **Where:** [`backend/models/src/erp_models/exceptions/se_exception.py:17`](../../../backend/models/src/erp_models/exceptions/se_exception.py#L17) · **Source:** TICKET and PLAN

| Option | For | Against |
| --- | --- | --- |
| ✅ `ClassVar` on the class | Subclasses inherit or override it ([`test_se_exception.py:22-28`](../../../backend/models/tests/exceptions/test_se_exception.py#L22-L28)), and constants are `ClassVar`s under AGENT.md | The three base codes are an inference: no specification names them |
| A code table keyed by class | Keeps the classes free of data | Not named by any worker or specification (open point) |

**Trade-off:** the T0.03 model exceptions still derive from `Exception`, so they carry no code (see the follow-ups of [EXPLAIN.md](EXPLAIN.md)).

**Revisit when:** T0.14 builds the problem+json handler and needs every `SE` exception to answer to `CODE`.

## <a id="d2"></a>D2: How the entry is validated

**Chosen:** one validator per field, each raising its own exception, with one `fullmatch` test for every case · **Where:** [`backend/models/src/erp_models/errors/entries/error_code_entry.py:45-123`](../../../backend/models/src/erp_models/errors/entries/error_code_entry.py#L45-L123) · **Source:** K07

| Option | For | Against |
| --- | --- | --- |
| ✅ One validator per field | AGENT.md wants each field to raise its own exception, and has no module-level helpers | The four validators repeat |
| One shared validator choosing the exception by field name | Less code | Needs a lookup of exception types |
| Separate checks for None, bool, empty and pattern | A precise message | Longer. The pattern already refuses them, so the message does not say which case failed |

**Trade-off:** repetition and a general message, in return for explicit exceptions and strict formats that make criterion 3 checkable.

**Revisit when:** a fifth field with the same rule appears, since AGENT.md lets fields with the same rule share a validator.

## <a id="d3"></a>D3: Who validates the entries

**Chosen:** `validate_codes` checks the mapping and its keys only · **Where:** [`backend/models/src/erp_models/errors/catalogs/error_catalog.py:40-64`](../../../backend/models/src/erp_models/errors/catalogs/error_catalog.py#L40-L64) · **Source:** K08

| Option | For | Against |
| --- | --- | --- |
| ✅ Leave entries to `ErrorCodeEntry` | The tests expect the entry's own exceptions, and no rule is written twice | A bad entry under a valid key is not reported by `SEErrorCatalogInvalidCodes` |
| Validate each entry in `validate_codes` | One exception for the catalogue | Duplicates the entry rules |

**Trade-off:** the reference pattern is written in both classes (follow-up).

**Revisit when:** callers need one exception for any catalogue error.

## <a id="d4"></a>D4: Entry base class

**Chosen:** `FrozenErpModel`, giving `extra="forbid"` and `frozen=True` · **Where:** [`error_code_entry.py:20`](../../../backend/models/src/erp_models/errors/entries/error_code_entry.py#L20) · **Source:** K07

| Option | For | Against |
| --- | --- | --- |
| ✅ `FrozenErpModel` | One shared config, the `OpaqueId` pattern of T0.03 | Depends on `erp_models.base` |
| Plain `BaseModel` with its own `ConfigDict` | No dependency | Repeats the config |

**Trade-off:** the catalogue itself is frozen but exposes a mutable `codes` dict (follow-up).

**Revisit when:** a read-only mapping type is adopted.

## <a id="d5"></a>D5: Unknown code lookup

**Chosen:** `dict.get` and a raise on a miss · **Where:** [`error_catalog.py:82-87`](../../../backend/models/src/erp_models/errors/catalogs/error_catalog.py#L82-L87) · **Source:** K08

| Option | For | Against |
| --- | --- | --- |
| ✅ `get` then raise | Shorter, no try block | No `KeyError` cause |
| Catch `KeyError` and re-raise | Keeps the cause | The cause carries nothing here |

**Trade-off:** none that matters. The code is refused, never replaced by a generic message (REQ-T05-03).

**Revisit when:** a lookup can fail for another reason.

## <a id="d6"></a>D6: How the scanner reads code

**Chosen:** `ast`, resolving bases by name until nothing new is found · **Where:** [`tests/conventions/exceptions/exception_scanner.py:55-70`](../../../tests/conventions/exceptions/exception_scanner.py#L55-L70) · **Source:** K05

| Option | For | Against |
| --- | --- | --- |
| ✅ `ast` | No imports and no side effects, follows inheritance across files | Name matching only, so two classes with one name are confused |
| Import and `issubclass` | Exact | Imports every package, with side effects |
| A regex on class lines | Simple | Cannot follow inheritance (reason not recorded by the worker, an open point) |

**Trade-off:** the roots are only `Exception` and `BaseException` ([line 27](../../../tests/conventions/exceptions/exception_scanner.py#L27)), so a class based on `ValueError` is missed. The review lists this as a follow-up.

**Revisit when:** a built-in-based exception is added to the repository.

## <a id="d7"></a>D7: Expected file name

**Chosen:** a regex that cuts on lower-to-upper boundaries and before an acronym's last capital · **Where:** [`exception_scanner.py:30`](../../../tests/conventions/exceptions/exception_scanner.py#L30) · **Source:** K05

| Option | For | Against |
| --- | --- | --- |
| ✅ The regex | `SEDatabase` gives `se_database`, as in the AGENT.md examples, and no dependency | An unusual acronym may split unexpectedly |
| An underscore before every capital | Simplest | Would give `s_e_database` |
| An inflection library | Tested splitting | A new dependency |

**Trade-off:** one regex to understand in return for no dependency.

**Revisit when:** a class name is split differently from what a person expects.

## <a id="d8"></a>D8: Scanner tests

**Chosen:** one parametrised test over a table of broken trees, each case proving that only its own rule fires, once · **Where:** [`tests/conventions/exceptions/test_exception_scanner.py`](../../../tests/conventions/exceptions/test_exception_scanner.py) · **Source:** K05

| Option | For | Against |
| --- | --- | --- |
| ✅ One table | Shorter, and proves the rules do not overlap | A failure needs the (case, rule) tuple to be read |
| One test per tree | Names each case | Longer |

**Trade-off:** terse reports for a shorter table.

**Revisit when:** the table grows past what one reader can scan.

## <a id="d9"></a>D9: Test data and subclasses

**Chosen:** class attributes for shared data, `type(name, (Base,), {...})` for subclasses, inline builder methods per file · **Where:** [`test_se_exception.py:22-28`](../../../backend/models/tests/exceptions/test_se_exception.py#L22-L28), [`test_error_code_entry.py`](../../../backend/models/tests/errors/entries/test_error_code_entry.py), [`test_error_catalog.py`](../../../backend/models/tests/errors/catalogs/test_error_catalog.py) · **Source:** K01 to K04

| Option | For | Against |
| --- | --- | --- |
| ✅ Class attributes and `type(...)` | AGENT.md forbids module constants and a second class per file | The subclasses are less readable |
| Module constants, nested classes | Readable | Forbidden by AGENT.md |
| A `helpers.py`, `conftest.py` or fixture YAML shared with other tasks | No repetition | Ties a task to another's files (TKT-4) |

The cause test uses a `wrap()` helper raising with `raise from` inside a single-statement `pytest.raises`, which satisfies ruff PT012 and PT017 without `noqa`, at the cost of one method. The entry tests stack field-by-value parametrisation, which gives more than six tests and adds positive cases the brief did not list.

**Trade-off:** a few lines of data are repeated across files.

**Revisit when:** a third test file needs the same data, which warrants a `helpers.py`.

## <a id="d10"></a>D10: Data test loop

**Chosen:** a loop over every code inside one test, with the code in the assertion message · **Where:** [`backend/models/tests/errors/catalogs/test_error_codes_data.py:23-30`](../../../backend/models/tests/errors/catalogs/test_error_codes_data.py#L23-L30) · **Source:** K04

| Option | For | Against |
| --- | --- | --- |
| ✅ Loop | Collection works while the data is missing (tests come first) | One test reports many codes |
| Parametrise over codes | One report per code | Needs the file at import time |

**Trade-off:** the failing code is named in the message instead of in the test id.

**Revisit when:** the catalogue is large enough that one failure should not hide others.

## <a id="d11"></a>D11: Where it is documented

**Chosen:** a new section of the models README, linked from the Exceptions paragraph · **Where:** [`backend/models/README.md:31-93`](../../../backend/models/README.md#L31-L93) · **Source:** K10

| Option | For | Against |
| --- | --- | --- |
| ✅ The models README | The first place a developer of a shared contract looks, with a Mermaid flowchart that renders on the host | One more file to keep current |
| A page in `docs/technical/` | Next to other design pages | One more link to keep in sync |
| A link only to the specifications | Nothing to maintain | Leaves how to add a code unwritten |

**Trade-off:** the README holds a clause the review calls invented (the reference "points to the specification"): see the follow-ups.

**Revisit when:** T0.14 documents how a service image finds the catalogue.

## 📝 Assumptions behind the choices

- The three base codes `UNEXPECTED-ERROR-01`, `SERVICE-FAILURE-01` and `INVALID-INPUT-01` are inferred, with no specification naming them: supports [D1](#d1).
- The fields are not named `*_key`, and the strict patterns are inferred from D122: supports [D2](#d2).
- Entries are validated by `ErrorCodeEntry` and a bad entry raises its own exception: supports [D3](#d3).
- `SEErrorCatalogUnreadable` is the model's own `UNREADABLE`, and non-string keys are refused with `SEErrorCatalogInvalidCodes`: supports [D3](#d3).
- Bases are resolved by name only and only top-level classes are read: supports [D6](#d6).
- Message keys follow `errors.<code in snake case>.<part>`, the plan's choice: supports [D2](#d2).
