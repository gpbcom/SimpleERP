# T0.24: Implementation choices

**Ticket:** [TICKET.md](TICKET.md) · **How it works:** [EXPLAIN.md](EXPLAIN.md) · **Review:** [REVIEW.md](REVIEW.md)

## 🎯 Constraints

- The collection is generated from the OpenAPI of `platform`, as [D406](../../specs/06-decisions/technical/d406-back-end.md) decides (criterion 1 of [TICKET.md](TICKET.md)).
- A refused call answers problem+json with its code and no secret ([REQ-T05-03](../../specs/03-technical/t05-api-and-webhooks/requirements/req-t05-03-problem-json.md)).
- No credential in `bruno/` (TEST-1 of [D426](../../specs/06-decisions/technical/d426-testing-strategy.md)), read in the most conservative form, as the ticket's assumptions say.
- CI fails when the collection is stale ([REQ-T05-05](../../specs/03-technical/t05-api-and-webhooks/requirements/req-t05-05-contract-tests.md)).
- The dev stage runs it headless and keeps JUnit and JSON reports ([CI/CD and stages](../../technical/delivery/ci-cd-and-stages.md)).
- A class per file and the other Python rules of [`AGENT.md`](../../../AGENT.md) hold in `tests/`. They do not hold in `.github/scripts`.

## ⚖️ Choices at a glance

| # | Decision | Chosen | Main alternative | Trade-off accepted |
| --- | --- | --- | --- | --- |
| [D1](#d1) | Which request makes the refused call | `GET /v1/anything` with no company header, asserting 400 ... | Unknown route with a company header: 404 and `PLATFORM-ROUTE-01` | The test covers the shared refusal, not the platform's routing errors. |
| [D2](#d2) | How the refused body is checked for secrets | One case-insensitive regex over the whole JSON body, plus... | Walk keys and values separately | A failure says only that a word was found. |
| [D3](#d3) | How the collection is produced and checked | A standard-library script that reads the committed JSON O... | The Bruno CLI importer | Features of OpenAPI the platform does not use are not mapped. |
| [D4](#d4) | What `check` compares | Generated files in memory, and any extra file under `requ... | Diff the whole collection folder | Only the generated part is guarded. |
| [D5](#d5) | Numbering of `seq` | Numbered per folder and path | Per folder by sorted path and method, as the brief says | The brief and the tests disagree, and the tests won. |
| [D6](#d6) | How arguments are read | `parse_args` returns None on any bad argument, and `main`... | argparse subparsers with their own exit behaviour | Plain usage line only. |
| [D7](#d7) | How the credential scan reads a file | A line scanner with block tracking, and an allow-list of ... | A full `.bru` parser | False positives on non-secret keys are accepted to avoid missing a secret. |
| [D8](#d8) | Which files the scan reads | git's file list only when git's top level is the scanned ... | Always `git ls-files` | Two code paths. |
| [D9](#d9) | How change detection treats `bruno/` | An explicit block in the path loop, mapping `bruno/<name>... | Add `bruno/` to `REPOSITORY_PREFIXES` with an owner lookup | More code in the loop. |
| [D10](#d10) | Where the freshness check runs | In the `services` job of `python.yml`, after the contract... | Before the contract check | A cheap step for services with no collection. |
| [D11](#d11) | How Node 22 is set up for Bruno | A separate `setup-node` step with no cache, before the Br... | Move the pnpm and setup-node pair before Bruno | A second setup call. |
| [D12](#d12) | How the stage tests read the workflow | Each Bruno flag as a substring of the run script, and the... | Parse the command into tokens | A reordered or renamed flag value is not caught. |
| [D13](#d13) | How the python workflow test finds the step | A `bruno_step()` method and a `BRUNO_STEP` ClassVar on th... | A helper in [`tests/ci/workflows/helpers.py`](../../../tests/ci/workflows/helpers.py) | A local helper. |
| [D14](#d14) | How the generator tests run | A subprocess on a fake service in `tmp_path`, with `--roo... | Import the script | A small speed cost. |
| [D15](#d15) | What proves the generator did not leak | Unique marker secrets in the fixture, asserted absent fro... | Golden files | Not every leak is covered. |
| [D16](#d16) | What the detection tests cover | Three parametrised behaviours in one class | One test per path | Fewer tests. |
| [D17](#d17) | Where the docs say it | A bold-led paragraph in the HTTP chapter of `api.md`, a s... | A separate section in `api.md` | Detail lives on the CI page only. |
| [D18](#d18) | `baseUrl` of the `stage` environment | The literal default port 8000 | The `ERP_PLATFORM_PORT` environment variable | Manual edit if the port changes. |
| [D19](#d19) | No recursive flag on `bru run` | Leave the command as it is | Add `-r` and assert it | Relies on the pinned CLI's default. |

## <a id="d1"></a>D1: Which request makes the refused call

**Chosen:** `GET /v1/anything` with no company header, asserting 400 and a non-empty code · **Where:** [`bruno/platform/tests/refused-call.bru:7-11`](../../../bruno/platform/tests/refused-call.bru#L7-L11) · **Source:** K01

| Option | For | Against |
| --- | --- | --- |
| ✅ No company header, 400 | Needs no header, so no credential or company id is in the file. It exercises the shared company-context refusal | It does not exercise the platform's own 404 handler |
| Unknown route with a company header: 404 and `PLATFORM-ROUTE-01` | Tests the platform's own handler | Needs a company header in the committed file |
| A wrong method: 405 | Simple | Named by the worker, no reason to prefer it recorded |

**Trade-off:** The test covers the shared refusal, not the platform's routing errors.

**Revisit when:** a second refused call is wanted for the platform's own handler.

## <a id="d2"></a>D2: How the refused body is checked for secrets

**Chosen:** One case-insensitive regex over the whole JSON body, plus a `Traceback` check · **Where:** [`bruno/platform/tests/refused-call.bru:29-33`](../../../bruno/platform/tests/refused-call.bru#L29-L33) · **Source:** K01

| Option | For | Against |
| --- | --- | --- |
| ✅ One regex over `JSON.stringify` of the body | Covers keys and values, short, stays in Bruno's sandbox | It cannot say which word matched |
| Walk keys and values separately | Reports the match | Longer |
| A Chai string-contains assertion per word | Explicit | One assertion per word, longer |

**Trade-off:** A failure says only that a word was found.

**Revisit when:** the list of words grows or the message needs to name the match.

## <a id="d3"></a>D3: How the collection is produced and checked

**Chosen:** A standard-library script that reads the committed JSON OpenAPI and compares bytes in memory · **Where:** [`.github/scripts/bruno_collection.py:155`](../../../.github/scripts/bruno_collection.py#L155) · **Source:** K09, D406

| Option | For | Against |
| --- | --- | --- |
| ✅ Own script | Output is deterministic so a byte comparison finds a stale collection, and CI runs it without Node. The Python rules of [`AGENT.md`](../../../AGENT.md) do not apply to `.github/scripts` | It maps only the OpenAPI features the tests and the specification need |
| The Bruno CLI importer | The tool's own conversion | Needs Node in the Python job, and the worker gave no determinism guarantee |
| PyYAML | Reads YAML OpenAPI | The committed document is JSON, so it adds a dependency for nothing |

**Trade-off:** Features of OpenAPI the platform does not use are not mapped.

**Revisit when:** a service uses OpenAPI features the generator ignores.

## <a id="d4"></a>D4: What `check` compares

**Chosen:** Generated files in memory, and any extra file under `requests/` is unexpected · **Where:** [`.github/scripts/bruno_collection.py:214`](../../../.github/scripts/bruno_collection.py#L214) · **Source:** K09

| Option | For | Against |
| --- | --- | --- |
| ✅ In-memory comparison of generated files | Hand-written `tests/`, `environments/` and the ignore file stay free to change. No temporary folder | Hand-edited generated files are caught only by byte difference |
| Diff the whole collection folder | Simple | Would flag every hand-written test |
| Generate into a temporary folder and compare | Reuses `generate` | Needs temporary files |

**Trade-off:** Only the generated part is guarded.

**Revisit when:** hand-written files must be kept in step with the OpenAPI too.

## <a id="d5"></a>D5: Numbering of `seq`

**Chosen:** Numbered per folder and path · **Where:** [`.github/scripts/bruno_collection.py:155`](../../../.github/scripts/bruno_collection.py#L155) · **Source:** K09, read from the diff

| Option | For | Against |
| --- | --- | --- |
| ✅ Per (folder, path) | The only numbering that satisfies the tests | Gives no global order in a folder, and Bruno orders by `seq` only |
| Per folder by sorted path and method, as the brief says | What the brief states | The tests of K03 disagree with it |

**Trade-off:** The brief and the tests disagree, and the tests won.

**Revisit when:** the first service has several paths in one folder. It is listed as a follow-up.

## <a id="d6"></a>D6: How arguments are read

**Chosen:** `parse_args` returns None on any bad argument, and `main` prints the usage and exits 2 · **Where:** [`.github/scripts/bruno_collection.py:235`](../../../.github/scripts/bruno_collection.py#L235) · **Source:** K09

| Option | For | Against |
| --- | --- | --- |
| ✅ Catch the error and return None | Every bad argument gives exit code 2 and a usage line, as `detect_changes.py` does | Less rich messages than argparse's own |
| argparse subparsers with their own exit behaviour | Richer messages | Exit behaviour not tied to the existing script's |

**Trade-off:** Plain usage line only.

**Revisit when:** users ask for help text.

## <a id="d7"></a>D7: How the credential scan reads a file

**Chosen:** A line scanner with block tracking, and an allow-list of structural auth keys · **Where:** [`tests/ci/bruno_credentials/helpers.py:110`](../../../tests/ci/bruno_credentials/helpers.py#L110) · **Source:** K02

| Option | For | Against |
| --- | --- | --- |
| ✅ Line scanner, allow-list | No new dependency, findings read `file:line`. Stricter, so it fits the conservative reading of TEST-1 | A key such as `client_id` must be a placeholder. Multi-line values may be missed |
| A full `.bru` parser | Exact | A new dependency |
| Whole-file regexes only | Simple | No line numbers |
| Flag only known secret key names | Fewer false positives | Misses names not on the list |

**Trade-off:** False positives on non-secret keys are accepted to avoid missing a secret.

**Revisit when:** the collections use an auth mode whose keys the allow-list does not know.

## <a id="d8"></a>D8: Which files the scan reads

**Chosen:** git's file list only when git's top level is the scanned root, else a recursive walk · **Where:** [`tests/ci/bruno_credentials/helpers.py:66`](../../../tests/ci/bruno_credentials/helpers.py#L66) · **Source:** K02

| Option | For | Against |
| --- | --- | --- |
| ✅ Conditional git list | A `tmp_path` inside another repository is never scanned through that repository. The real repository honours the ignore rules | Two code paths |
| Always `git ls-files` | One path | Wrong inside a nested temporary folder |
| Always walk | One path | Would scan ignored files such as `.env` |

**Trade-off:** Two code paths.

**Revisit when:** the test layout stops using temporary folders.

## <a id="d9"></a>D9: How change detection treats `bruno/`

**Chosen:** An explicit block in the path loop, mapping `bruno/<name>` to the service only when it exists · **Where:** [`.github/scripts/detect_changes.py:212-216`](../../../.github/scripts/detect_changes.py#L212-L216) · **Source:** K10

| Option | For | Against |
| --- | --- | --- |
| ✅ Explicit block with a `BRUNO` constant | Selects exactly the one service and no image, as the tests require | A little longer |
| Add `bruno/` to `REPOSITORY_PREFIXES` with an owner lookup | Reuses the existing mechanism | Named by the worker, not chosen |
| Treat `bruno/` as a shared path | Simple | Selects everything |

**Trade-off:** More code in the loop.

**Revisit when:** several path families need the same mapping.

## <a id="d10"></a>D10: Where the freshness check runs

**Chosen:** In the `services` job of `python.yml`, after the contract check, with no extra `if` · **Where:** [`.github/workflows/python.yml:61-62`](../../../.github/workflows/python.yml#L61-L62) · **Source:** K11

| Option | For | Against |
| --- | --- | --- |
| ✅ Beside the contract check | The script skips a service with no collection, so an `if` would repeat it. The contract checks stay together | The step runs for every service |
| Before the contract check | Fails earlier | Splits the contract checks |
| An `if` on the collection folder | Explicit | Duplicates the script's own skip |

**Trade-off:** A cheap step for services with no collection.

**Revisit when:** the step becomes slow.

## <a id="d11"></a>D11: How Node 22 is set up for Bruno

**Chosen:** A separate `setup-node` step with no cache, before the Bruno step · **Where:** [`.github/workflows/stage.yml:123-126`](../../../.github/workflows/stage.yml#L123-L126) · **Source:** K12

| Option | For | Against |
| --- | --- | --- |
| ✅ Separate step | The pnpm-cached one stays after Bruno so Playwright is unaffected. The repository has no pnpm lock yet, so a cache would fail | A second `setup-node` call |
| Move the pnpm and setup-node pair before Bruno | One call | Moves the Playwright setup |
| Add `cache: pnpm` to the new step | Faster | Fails without a pnpm lock |

**Trade-off:** A second setup call.

**Revisit when:** a pnpm lock exists and the step time matters.

## <a id="d12"></a>D12: How the stage tests read the workflow

**Chosen:** Each Bruno flag as a substring of the run script, and the Node setup located by position before the Bruno step · **Where:** [`tests/ci/workflows/test_stage_workflow.py:73-108`](../../../tests/ci/workflows/test_stage_workflow.py#L73-L108) · **Source:** K06

| Option | For | Against |
| --- | --- | --- |
| ✅ Substrings and an index lookup | Ignore flag order and line breaks, and check the ordering the brief requires | Less strict than a parsed command |
| Parse the command into tokens | Strict | Ties the test to the layout |
| Compare the whole script | Strict | Breaks on any edit |
| Only check that a `setup-node` exists | Simple | Does not check the order |

**Trade-off:** A reordered or renamed flag value is not caught.

**Revisit when:** a flag's value matters.

## <a id="d13"></a>D13: How the python workflow test finds the step

**Chosen:** A `bruno_step()` method and a `BRUNO_STEP` ClassVar on the test class · **Where:** [`tests/ci/workflows/checks/test_python_workflow.py:17-24`](../../../tests/ci/workflows/checks/test_python_workflow.py#L17-L24) · **Source:** K05

| Option | For | Against |
| --- | --- | --- |
| ✅ A helper method on the class | Keeps one class per file and shares the lookup, with a clear message when the step is missing | The lookup is local to this file |
| A helper in [`tests/ci/workflows/helpers.py`](../../../tests/ci/workflows/helpers.py) | Shared | Not among the task's files |
| Repeat the lookup in each test | Simple | Repeated |

**Trade-off:** A local helper.

**Revisit when:** other workflow tests need the same lookup.

## <a id="d14"></a>D14: How the generator tests run

**Chosen:** A subprocess on a fake service in `tmp_path`, with `--root`, and a first assertion that `generate` exits 0 · **Where:** [`tests/ci/bruno_collection/helpers.py:96`](../../../tests/ci/bruno_collection/helpers.py#L96) · **Source:** K03

| Option | For | Against |
| --- | --- | --- |
| ✅ Subprocess | Tests the real command line and exit codes, independent of the real OpenAPI, and fails now for the missing script | A little slower |
| Import the script | Faster | Skips the command line |
| Run against `backend/services/platform` | Real data | Breaks when the OpenAPI changes |

**Trade-off:** A small speed cost.

**Revisit when:** the suite becomes slow.

## <a id="d15"></a>D15: What proves the generator did not leak

**Chosen:** Unique marker secrets in the fixture, asserted absent from every generated file · **Where:** [`tests/ci/bruno_collection/helpers.py:12`](../../../tests/ci/bruno_collection/helpers.py#L12) · **Source:** K03

| Option | For | Against |
| --- | --- | --- |
| ✅ Marker strings | Robust to formatting changes in the generator | Cannot catch every possible leak |
| Golden files | Exact | Break on any formatting change |
| Check only the password | Simple | Misses the token, email and query default |

**Trade-off:** Not every leak is covered.

**Revisit when:** the generator maps more of the document.

## <a id="d16"></a>D16: What the detection tests cover

**Chosen:** Three parametrised behaviours in one class · **Where:** [`tests/ci/detect_changes/bruno/test_bruno_changes.py:23`](../../../tests/ci/detect_changes/bruno/test_bruno_changes.py#L23) · **Source:** K04

| Option | For | Against |
| --- | --- | --- |
| ✅ Service match, no match, beside a front end | Each behaviour stated once, and a failure names the path | Fewer tests |
| One test per path | Granular | More repetition |

**Trade-off:** Fewer tests.

**Revisit when:** a new path family is added.

## <a id="d17"></a>D17: Where the docs say it

**Chosen:** A bold-led paragraph in the HTTP chapter of `api.md`, a section in the testing page that links the CI page, and a paragraph in Stages · **Where:** [`docs/technical/interfaces/api.md:44-62`](../../../docs/technical/interfaces/api.md#L44-L62) · **Source:** K07, K08

| Option | For | Against |
| --- | --- | --- |
| ✅ Paragraphs beside the OpenAPI text, one source for CI detail | Keeps the chapter's pattern and avoids repeating the workflow table | A cross-page link, and a paragraph is less scannable than a table cell |
| A separate section in `api.md` | Easier to find | Breaks the flow |
| A bulleted list | Scannable | Not the pattern of that chapter |
| Duplicate the workflow description | No link to follow | Two places to keep in step |
| A row in the stage table | Scannable | A list of report files does not fit a cell |

**Trade-off:** Detail lives on the CI page only.

**Revisit when:** the pages diverge.

## <a id="d18"></a>D18: `baseUrl` of the `stage` environment

**Chosen:** The literal default port 8000 · **Where:** [`bruno/platform/environments/stage.bru:2`](../../../bruno/platform/environments/stage.bru#L2) · **Source:** K13

| Option | For | Against |
| --- | --- | --- |
| ✅ Literal | Matches the brief | A changed `ERP_PLATFORM_PORT` needs a manual edit |
| The `ERP_PLATFORM_PORT` environment variable | Follows the port | Not chosen: the brief asks for a literal |

**Trade-off:** Manual edit if the port changes.

**Revisit when:** the compose port becomes configurable in CI.

## <a id="d19"></a>D19: No recursive flag on `bru run`

**Chosen:** Leave the command as it is, with no `-r` · **Where:** [`.github/workflows/stage.yml:127-137`](../../../.github/workflows/stage.yml#L127-L137) · **Source:** FIX-K12+K06+K14

| Option | For | Against |
| --- | --- | --- |
| ✅ No flag | The run from the collection root executed both tests, so CLI 4.2.1 recurses by default. A flag would be dead weight | A CLI upgrade could change this unnoticed |
| Add `-r` and assert it | Safe against an upgrade | Dead weight with the pinned version |

**Trade-off:** Relies on the pinned CLI's default.

**Revisit when:** the CLI version is raised. A zero-test failure is a follow-up.

## 📝 Assumptions behind the choices

- Bruno CLI 4.2.1 recurses into subfolders when run from the collection root: supports [D19](#d19).
