# T0.18: Implementation choices

**Ticket:** [TICKET.md](TICKET.md) · **How it works:** [EXPLAIN.md](EXPLAIN.md) · **Review:** [REVIEW.md](REVIEW.md)

## 🎯 Constraints

- A removed field fails CI, an added one passes, and a stale committed document fails CI ([TICKET.md](TICKET.md) criteria 2 to 4, [REQ-T05-05](../../specs/03-technical/t05-api-and-webhooks/requirements/req-t05-05-contract-tests.md)).
- The committed document is the one served by `platform` (criteria 1 and 5, [I-T05-02](../../specs/03-technical/t05-api-and-webhooks/interfaces/i-t05-02-openapi-registry.md)).
- No package of `backend/` has a command line: exporting is a script of `.github/scripts/` and the check is a test ([`AGENT.md`](../../../AGENT.md), "Layout").
- One class per file, at most five Python files per folder, no module-level code, no nested function, no `Any`, no mocks ([`AGENT.md`](../../../AGENT.md), "Rules a test enforces" and "Tests").
- Services keep layers: `api`, `service`, `storage`, `models` ([`AGENT.md`](../../../AGENT.md)).
- A message or log never quotes a value read from a file ([`AGENT.md`](../../../AGENT.md), "Logging").

## ⚖️ Choices at a glance

| # | Decision | Chosen | Main alternative | Trade-off accepted |
| --- | --- | --- | --- | --- |
| [D1](#d1) | Where the check runs | Tests of the service, run by a CI script | A command in the service | Needs a script and a test folder, no command line |
| [D2](#d2) | Which document is the baseline | The base commit's document, with `fetch-depth: 0` | A shallow checkout, or fetching the base later | Slower checkout |
| [D3](#d3) | What counts as stale | Parsed JSON equality | Text or hash comparison | Key order never matters |
| [D4](#d4) | Baseline compared with | The committed document | The generated document | A stale document is reported on its own |
| [D5](#d5) | How the comparator walks | Recursive walk of two dicts | Flatten to pointer maps, or a diff library | Longer code, explicit rules |
| [D6](#d6) | Parameter identity | Escaped `<in>/<name>` key | List position, or name only | A moved parameter counts as removed |
| [D7](#d7) | `passed` | Derived property | A stored field | A property on the model |
| [D8](#d8) | Reading a document | One `except (OSError, ValueError)`, cause kept, no content | Own branch per error, or a Pydantic model | Less detail in messages |
| [D9](#d9) | Exceptions layout | Three sub-folders with re-exports | One flat folder | One more import level |
| [D10](#d10) | Export script errors | `sys.argv` and one broad `except` | `argparse`, narrow `except` | Programming errors also read as export failures |
| [D11](#d11) | Script exit code and baseline variable | `|| status=$?`, `unset` first | Bare pytest under `set -e` | A few more lines |
| [D12](#d12) | Documents in `/openapi.json` access | Tests send the company headers | Make the path public | Does not test anonymous access |
| [D13](#d13) | Fixtures and helpers in tests | Plain dicts, real app, real git, stand-in `uv` | JSON files, mocks, nested functions | Some repetition, depends on bash |
| [D14](#d14) | Where the documentation goes | The `python.yml` row and the HTTP section of `api.md` | A new page, or the service README | A long table row |
| [D15](#d15) | Hardening the runtime image | `apt-get upgrade` and pip removal in one `RUN`, with a text test | Pin `libzstd1`, a trivy ignore file, another base image | Not reproducible, needs the network |

## <a id="d1"></a>D1: Where the contract check runs

**Chosen:** pytest tests in `tests/contracts/`, run by [`.github/scripts/check_contract.sh`](../../../.github/scripts/check_contract.sh) · **Where:** [`.github/workflows/python.yml:57-60`](../../../.github/workflows/python.yml#L57-L60) · **Source:** plan, read from the diff

| Option | For | Against |
| --- | --- | --- |
| ✅ Tests plus a CI script | The [`AGENT.md`](../../../AGENT.md) table says a contract check is "a test in the service's `tests/`" and a CI step is a script of `.github/scripts/` | Two layers to read |
| A command line of the service | Simple to call | Forbidden by [`AGENT.md`](../../../AGENT.md) and `tests/conventions/` |

**Trade-off:** the check needs a script and an environment variable to reach the baseline.

**Revisit when:** a second service commits an OpenAPI document (see the follow-up on a shared library in [EXPLAIN.md](EXPLAIN.md)).

## <a id="d2"></a>D2: The baseline is the base commit's document

**Chosen:** `fetch-depth: 0` on the services job, base SHA passed through `env` · **Where:** [`.github/workflows/python.yml:44`](../../../.github/workflows/python.yml#L44), [`.github/workflows/python.yml:57-60`](../../../.github/workflows/python.yml#L57-L60) · **Source:** K09

| Option | For | Against |
| --- | --- | --- |
| ✅ Full clone, `git show <base>:<file>` | Works with `persist-credentials: false`; the env value avoids script injection | A full clone is slower |
| Fetch the base later | Faster checkout | Impossible with `persist-credentials: false` (K09) |
| `git show` against a shallow clone | No change to checkout | The base commit is not there |

**Trade-off:** a slower checkout of the services job. No measurement of the cost was made.

**Revisit when:** the checkout time becomes a problem, which nobody has measured yet (open point).

## <a id="d3"></a>D3: Staleness is parsed JSON equality

**Chosen:** `committed != generated` after both are parsed · **Where:** [`contract_service.py:72`](../../../backend/services/platform/src/erp_platform/service/contracts/contract_service.py#L72) · **Source:** K12

| Option | For | Against |
| --- | --- | --- |
| ✅ Dict equality | Indentation and key order never make a document stale; no extra code | A text diff is not shown |
| Serialised text | Catches formatting drift | Fails on harmless changes |
| Hashes | Compact | Same flaw as text, and hides the difference |

**Trade-off:** formatting is not checked. **Revisit when:** a rule asks for a canonical file format.

## <a id="d4"></a>D4: The baseline is compared with the committed document

**Chosen:** `comparator.compare(baseline, committed)` · **Where:** [`contract_service.py:78`](../../../backend/services/platform/src/erp_platform/service/contracts/contract_service.py#L78) · **Source:** K12

| Option | For | Against |
| --- | --- | --- |
| ✅ Baseline against committed | The brief says so; breaking changes describe what is committed; a stale document is reported separately | A stale document can hide a change not yet exported |
| Baseline against generated | Sees the code as it is | Mixes the two failures |

**Trade-off:** the two failures are reported apart. **Revisit when:** a change must be judged before it is exported.

## <a id="d5"></a>D5: A recursive walk of the two documents

**Chosen:** `_compare_node` and its helpers · **Where:** [`contract_comparator.py:171`](../../../backend/services/platform/src/erp_platform/service/contracts/contract_comparator.py#L171) · **Source:** K11

| Option | For | Against |
| --- | --- | --- |
| ✅ Recursive walk | Pointer building and per-node rules are explicit; no dependency | Only `properties` and `items` are followed |
| Flatten to pointer maps | Shorter | Blurs which keywords count as a change |
| Third-party diff library | Less code | A new dependency for a rule set of six kinds |

**Trade-off:** `anyOf`/`oneOf`/`allOf`, `enum`, responses and required fields are not compared yet (follow-up in [EXPLAIN.md](EXPLAIN.md)); the ticket's criteria are met. **Revisit when:** a second endpoint arrives.

## <a id="d6"></a>D6: Parameters are keyed by `<in>/<name>`

**Chosen:** an escaped key · **Where:** [`contract_comparator.py:93`](../../../backend/services/platform/src/erp_platform/service/contracts/contract_comparator.py#L93) · **Source:** K11

| Option | For | Against |
| --- | --- | --- |
| ✅ `<in>/<name>` | Survives reordering; the same name elsewhere is another parameter | A parameter moved to another place counts as removed (conservative, REQ-T05-05) |
| List position | Simple | Breaks on reordering |
| Name only | Simple | Confuses the same name in path and query |

**Trade-off:** it may report more. **Revisit when:** a move of a parameter must be allowed.

## <a id="d7"></a>D7: `passed` is derived

**Chosen:** a property over `stale` and `breaking_changes` · **Where:** [`contract_report.py:79`](../../../backend/services/platform/src/erp_platform/models/contracts/contract_report.py#L79) · **Source:** K08

| Option | For | Against |
| --- | --- | --- |
| ✅ Property | Cannot disagree with its data; clean round trip | Not a serialised field |
| Stored field | Visible in dumps | Can contradict the others |

**Trade-off:** none that is known. **Revisit when:** a consumer needs `passed` in a dump.

## <a id="d8"></a>D8: One error path to read a document

**Chosen:** one `try` over `(OSError, ValueError)`, then an `isinstance(dict)` check; only the path and `type(error).__name__` in messages · **Where:** [`open_api_document_repository.py:55-63`](../../../backend/services/platform/src/erp_platform/storage/contracts/open_api_document_repository.py#L55-L63) · **Source:** K10, K04

| Option | For | Against |
| --- | --- | --- |
| ✅ One path, no content | One message shape; storage holds no rule; follows "never log a value" and "keep the cause" | The non-object case has no cause; less detail |
| One branch per error | More precise | Duplicated messages |
| Validate with a Pydantic model | Strict | A rule in storage, and a model for a free-form document |
| Quote the decoder's message | More detail | It may quote content |

**Trade-off:** less detail in messages. **Revisit when:** debugging a broken document needs the decoder's position.

## <a id="d9"></a>D9: Exceptions in sub-folders

**Chosen:** `contract_change/`, `contract_report/` and `document/`, re-exported by the package `__init__` · **Where:** [`models/contracts/exceptions/__init__.py`](../../../backend/services/platform/src/erp_platform/models/contracts/exceptions/__init__.py) · **Source:** K08

| Option | For | Against |
| --- | --- | --- |
| ✅ Sub-folders | A flat folder would hold 8 files, past the limit of five | One more import level; callers still import from the package |
| One flat folder | Simpler | Fails `tests/conventions/` |

The document exceptions sit in `models`, not in storage, because the tests and the brief import them from there. `SEOpenApiDocumentError` derives from `Exception`, as existing storage bases do. **Trade-off:** more folders. **Revisit when:** the folder count grows.

## <a id="d10"></a>D10: The export script reads `sys.argv` and catches broadly

**Chosen:** manual argument check and one `except Exception` · **Where:** [`.github/scripts/export_openapi.py:41-55`](../../../.github/scripts/export_openapi.py#L41-L55) · **Source:** K13

| Option | For | Against |
| --- | --- | --- |
| ✅ `sys.argv` and a broad `except` | The test needs exactly one stderr line and exit 2; a factory can raise anything. CI scripts may use a command line | A programming error in the script also reads as an export failure |
| `argparse` | Standard | Multi-line usage errors and its own exit paths |
| Narrow `except` list | More precise | A traceback could escape |

**Trade-off:** accepted by the reviewer. **Open point:** nobody gave the reason for `sys.path.insert(0, os.getcwd())` at [line 50](../../../.github/scripts/export_openapi.py#L50); the review asks to drop or explain it. **Revisit when:** the script takes more than one argument.

## <a id="d11"></a>D11: The shell script keeps the exit code and clears the variable

**Chosen:** `status=0 ... || status=$?`, `unset ERP_CONTRACT_BASELINE` before any `export` · **Where:** [`check_contract.sh:17`](../../../.github/scripts/check_contract.sh#L17), [`check_contract.sh:32-35`](../../../.github/scripts/check_contract.sh#L32-L35) · **Source:** K09

| Option | For | Against |
| --- | --- | --- |
| ✅ Capture, close the group, exit | The log group always closes; an inherited baseline never leaks into a stale-only run | A few more lines |
| Bare pytest under `set -e` | Shorter | The group stays open on failure |
| Inline variable per case | No `unset` | Cannot clear an inherited value |

The script also checks the base with `git cat-file -e <base>^{commit}` ([line 20](../../../.github/scripts/check_contract.sh#L20)) so a zero or unknown SHA means stale-only. **Revisit when:** the `uv run --package` invocation is aligned with `check_python_project.sh` (follow-up).

## <a id="d12"></a>D12: The tests send the company headers

**Chosen:** a `client` fixture with the headers · **Where:** [`backend/services/platform/tests/contracts/conftest.py:42-45`](../../../backend/services/platform/tests/contracts/conftest.py#L42-L45) · **Source:** K06, K14

| Option | For | Against |
| --- | --- | --- |
| ✅ Headers in a fixture | Stays in the ticket's files; I-T05-02 lists Rights, so not making the document public is conservative | Does not test anonymous access |
| Add `/openapi.json` to `public_paths` | Simpler tests | `conf/app.yaml` belongs to T0.14, and it would loosen access |
| Headers inline in each test | No fixture | Repetition |

**Revisit when:** the specifications say whether the document is public.

## <a id="d13"></a>D13: Test helpers without mocks or module-level code

**Chosen:** plain dict fixtures, the real application built by `AppFactory.create()`, real temporary git repositories, a bash stand-in `uv`, helper classes in `conftest.py` · **Where:** [`tests/ci/check_contract/conftest.py:62`](../../../tests/ci/check_contract/conftest.py#L62), [`tests/ci/check_contract/conftest.py:74`](../../../tests/ci/check_contract/conftest.py#L74), [`backend/services/platform/tests/contracts/conftest.py:17-39`](../../../backend/services/platform/tests/contracts/conftest.py#L17-L39) · **Source:** K02, K03, K05, K06, K07

| Option | For | Against |
| --- | --- | --- |
| ✅ Dicts, real app, real git, bash stand-in | No mocks ([`AGENT.md`](../../../AGENT.md)); each case is readable; a missing-base commit is a `git commit-tree` of the empty tree, so the repository keeps two commits | Duplicated literals; depends on bash; the app is rebuilt per test |
| JSON or YAML fixture files | Short tests | Needs a loader |
| `unittest.mock` or a Python stand-in | No bash | Mocks are not used here |
| Nested functions or module constants | Concise | Banned by `tests/conventions/` |

Other test choices: asserting `(kind, location)` pairs so tests do not depend on added `ContractChange` fields ([`test_contract_comparator.py:36`](../../../backend/services/platform/tests/service/contracts/contract_comparator/test_contract_comparator.py#L36)); the baseline skip sits in the body ([`test_contract_baseline.py:20-21`](../../../backend/services/platform/tests/contracts/test_contract_baseline.py#L20-L21)) so import errors still fail; the real-document tests pick the first schema with properties at run time. **Revisit when:** the stand-in grows beyond what bash can hold.

## <a id="d14"></a>D14: Where the documentation goes

**Chosen:** the `python.yml` row of [`docs/technical/delivery/ci-cd-and-stages.md:50`](../../../docs/technical/delivery/ci-cd-and-stages.md#L50), and the OpenAPI paragraph of [`docs/technical/interfaces/api.md`](../../../docs/technical/interfaces/api.md) · **Source:** K15

| Option | For | Against |
| --- | --- | --- |
| ✅ Workflows table and API page | One table of CI steps; readers look in the API page for the document | A long row; the export command appears twice |
| A new page | Room | Splits CI steps |
| The service README | Close to the code | Not where the API is described |

**Revisit when:** the contract check grows past one row.

## <a id="d15"></a>D15: How the runtime image is hardened against the Trivy findings

**Chosen:** upgrade apt packages and uninstall system pip in the single runtime-stage `RUN` that creates the user, guarded by a text test · **Where:** [`backend/services/platform/Dockerfile:20-24`](../../../backend/services/platform/Dockerfile#L20-L24), [`backend/services/platform/tests/image/test_dockerfile.py:9-35`](../../../backend/services/platform/tests/image/test_dockerfile.py#L9-L35) · **Source:** K17 (image) and K16 (test), a plan change approved after the plan

| Option | For | Against |
| --- | --- | --- |
| ✅ `apt-get upgrade` and pip uninstall in one `RUN` | One layer; no version pinned; the venv needs no pip | The build needs network access to apt; the upgrade is not reproducible between builds |
| Pin `libzstd1` to the fixed version | Reproducible | Named by the worker as an alternative; the reason it lost is not recorded (open point) |
| Add a trivy ignore file | No image change | Named by the worker as an alternative; it hides the finding instead of fixing it (open point: not confirmed by the worker) |
| Use a distroless or other base image | Smaller surface | A change of base for a skeleton image; the reason it lost is not recorded (open point) |

For the test (K16): substring and index checks on the runtime stage text, one parametrised test for the "before `USER`" order, against parsing the `RUN` lines or building the image as `test_image.py` does. The substring checks need no Docker and no mock, but depend on the exact spelling and cannot tell a command in a comment from a real one. Building the image would be exact but slow and needs Docker.

**Trade-off:** the apt upgrade is not reproducible and the build needs the network, in exchange for one layer and no pinned versions. With the GHA layer cache of [`.github/workflows/images.yml:88-89`](../../../.github/workflows/images.yml#L88-L89), the upgrade layer is reused until the base image changes.

**Revisit when:** a later HIGH CVE fails Trivy because of the cached layer (add `no-cache-filters` or `pull: true`), or the Dockerfile grows past what substring checks can read.

## 📝 Assumptions behind the choices

- `/openapi.json` stays behind the company context: supports [D12](#d12).
- A blank baseline or an unknown or zero base means stale-only: supports [D2](#d2) and [D11](#d11).
- Conservative comparator rules (a parameter moved, a type added): supports [D5](#d5) and [D6](#d6).
- `SEOpenApiDocumentUnreadableError` with the cause kept: supports [D8](#d8).
- Package `erp_platform` and the `/v1/health` path: supports [D13](#d13).
- K16: the runtime stage is the text after the last `FROM `, with literal substring checks: supports [D15](#d15).
- K17: the `RUN` runs before `/opt/venv` exists, so it removes the base image's pip: supports [D15](#d15).
