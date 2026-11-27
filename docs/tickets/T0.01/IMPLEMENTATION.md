# T0.01: Implementation choices

**Ticket:** [TICKET.md](TICKET.md) · **How it works:** [EXPLAIN.md](EXPLAIN.md) · **Review:** [REVIEW.md](REVIEW.md)

## 🎯 Constraints

- Both locks are pinned and install on a clean clone, with `uv sync --locked` and `pnpm install --frozen-lockfile` ([D415](../../specs/06-decisions/technical/d415-supply-chain-controls.md), acceptance criteria 1 and 2 of [TICKET.md](TICKET.md)).
- The layout, folder names and READMEs follow [D438](../../specs/06-decisions/technical/d438-repository-layout.md) and the [layout page](../../technical/architecture/repository-layout.md).
- Python 3.13 and Node 22 ([D406](../../specs/06-decisions/technical/d406-back-end.md), [D407](../../specs/06-decisions/technical/d407-front-end.md)).
- The code rules of [AGENT.md](../../../AGENT.md): nothing at module level, one class per file, at most five Python files per folder, no `Any`, and a change in `backend/models/`, `frontend/packages/`, [`uv.lock`](../../../uv.lock) or [`pnpm-lock.yaml`](../../../pnpm-lock.yaml) runs all of CI.
- The repository CI job has no Node, and the layout tests must run there ([`tests/layout/`](../../../tests/layout/test_folder_readmes.py)).
- The SDK package name and the shared libraries belong to later tickets ([TICKET.md](TICKET.md), assumptions and out of scope).

## ⚖️ Choices at a glance

| # | Decision | Chosen | Main alternative | Trade-off accepted |
| --- | --- | --- | --- | --- |
| [D1](#d1) | The pnpm version to pin | `pnpm@10.34.9` | `pnpm@12.21.0`, the local version | Developers on pnpm 12 are switched to 10 |
| [D2](#d2) | How to write the Node range | `^22` | `>=22 <23` | The test must reject digits, not ranges |
| [D3](#d3) | Build backend of `erp-models` | `uv_build` with a range | `hatchling` | The upper bound needs a bump with uv minors |
| [D4](#d4) | The SDK member | Virtual, no build system | A placeholder package | The SDK cannot be imported yet |
| [D5](#d5) | How the workspace tests check installs | Static parsing, no tool call | Run `uv sync` and `pnpm install` in the test | Lock consistency is not proved by the tests |
| [D6](#d6) | pnpm workspace globs | Two apps by path, the rest by wildcard | Wildcards for everything | Apps must be added to the file |
| [D7](#d7) | Helpers of the layout tests | Instance methods and `ClassVar`s | Module functions or a helpers file | Helpers sit in the test class |
| [D8](#d8) | Reading README links and sections | Split and line scan | Regex or a Markdown parser | Reference-style links and fenceless setups are missed |
| [D9](#d9) | The detector test's target | The real repository root | A fixture repository | Tests depend on the repository state |
| [D10](#d10) | A change to `frontend/packages/` | Selects both front ends | Selects nothing, as the brief listed | Departs from the brief |
| [D11](#d11) | The pnpm version in the README | Point to the `packageManager` pin | Write the number | One more click for the reader |
| [D12](#d12) | Configuration page | A Workspaces table and per-service `conf/` paths | A bullet list, or keep bare `conf/` paths | Longer table cells |
| [D13](#d13) | Layout page, Today section | Bullets of links, only the members on disk | A paragraph, a diagram, or every glob member | The page needs an update when folders appear |

## <a id="d1"></a>D1: The pnpm version to pin

**Chosen:** `pnpm@10.34.9` · **Where:** [`package.json:8`](../../../package.json#L8) · **Source:** K10, accepted by the reviewer

| Option | For | Against |
| --- | --- | --- |
| ✅ `pnpm@10.34.9` | Writes a single-document lock that [`tests/layout/test_pnpm_workspace.py`](../../../tests/layout/test_pnpm_workspace.py#L56) parses; `pnpm/action-setup` reads the field in CI; no specification pins a version | Not the version installed locally |
| `pnpm@12.21.0` (the brief) | The local version | Its lock has a second YAML document, which breaks the done-when test |
| Edit the 12.x lock by hand | Keeps pnpm 12 | `--frozen-lockfile` then fails |

**Trade-off:** developers on pnpm 12 are switched to 10.34.9 by `packageManager`, in exchange for a lock the test and CI both accept.

**Revisit when:** the layout test reads multi-document YAML, or CI moves to pnpm 11 or later.

## <a id="d2"></a>D2: How to write the Node range

**Chosen:** `"^22"` · **Where:** [`package.json:5-7`](../../../package.json#L5-L7) · **Source:** K10

| Option | For | Against |
| --- | --- | --- |
| ✅ `^22` | Means `>=22.0.0 <23.0.0`, and passes the test that rejects the digits 23 | Less explicit than two bounds |
| `>=22 <23` (the brief) | Explicit | Its `23` is rejected by [`test_the_engines_allow_node_22_only`](../../../tests/layout/test_pnpm_workspace.py#L42) |

**Trade-off:** the same meaning, written to suit the test. The test itself is over strict (a follow-up in [EXPLAIN.md](EXPLAIN.md)).

**Revisit when:** the test compares major numbers only.

## <a id="d3"></a>D3: Build backend of `erp-models`

**Chosen:** `uv_build>=0.12.21,<0.13` with `module-name = "erp_models"` · **Where:** [`backend/models/pyproject.toml:10-15`](../../../backend/models/pyproject.toml#L10-L15) · **Source:** K06

| Option | For | Against |
| --- | --- | --- |
| ✅ `uv_build` | The uv-native backend, the default of `uv init --lib`; no extra tool in the supply chain ([D415](../../specs/06-decisions/technical/d415-supply-chain-controls.md)) | The upper bound needs a bump with each uv minor; a range is not locked by [`uv.lock`](../../../uv.lock) |
| `hatchling` | More widespread | A third-party tool added to the supply chain |

**Trade-off:** a bounded range rather than an exact pin. The reviewer asks to pin it exactly (follow-up).

**Revisit when:** uv 0.13 is adopted, or builds of `erp_models` must be reproducible.

## <a id="d4"></a>D4: The SDK member

**Chosen:** a virtual member, with no `[build-system]` and no source package · **Where:** [`sdk/pyproject.toml:1-8`](../../../sdk/pyproject.toml#L1-L8) · **Source:** K06

| Option | For | Against |
| --- | --- | --- |
| ✅ Virtual member | Does not invent the SDK package name, which belongs to the ticket of D425 | The SDK cannot be imported yet |
| A placeholder package now | Importable at once | Fixes a name nobody has decided |

**Trade-off:** the member is locked ([`uv.lock:74-83`](../../../uv.lock#L74-L83)) but empty.

**Revisit when:** the SDK ticket adds its build system.

## <a id="d5"></a>D5: How the workspace tests check installs

**Chosen:** static parsing of the TOML, JSON and YAML files, with no uv or pnpm call · **Where:** [`tests/layout/test_uv_workspace.py`](../../../tests/layout/test_uv_workspace.py), [`tests/layout/test_pnpm_workspace.py`](../../../tests/layout/test_pnpm_workspace.py) · **Source:** K02, K03

| Option | For | Against |
| --- | --- | --- |
| ✅ Static parsing | Fast, no network; the repository CI job has no Node | Only shows that the lock lists the member (`[manifest].members`), not that it matches the manifests |
| `uv sync --locked` or `pnpm install --frozen-lockfile` in a subprocess | Proves the real install | Needs network and tools; `pnpm` fails in the repository CI job |

**Trade-off:** the real installs are left to the verifier and to the CI jobs. The pnpm one is recorded in [`pnpm-install.txt`](tests-evidences/pnpm-install.txt); the uv one is not (follow-up).

**Revisit when:** the verifier's `checks.py` runs `uv sync --locked`.

## <a id="d6"></a>D6: pnpm workspace globs

**Chosen:** the two apps by path, `portals/*` and `packages/*` by wildcard · **Where:** [`pnpm-workspace.yaml:1-5`](../../../pnpm-workspace.yaml#L1-L5) · **Source:** K10

| Option | For | Against |
| --- | --- | --- |
| ✅ Mixed | Follows D438: a portal or a package joins with no change here | A new app needs a line |
| Wildcards for everything | No edit ever | Not what the layout names: the two apps are fixed |

**Trade-off:** a line to add per new app, which is rare.

**Revisit when:** more apps are planned.

## <a id="d7"></a>D7: Helpers of the layout tests

**Chosen:** instance methods of the test class and `ClassVar` constants · **Where:** [`tests/layout/test_folder_readmes.py:32-35`](../../../tests/layout/test_folder_readmes.py#L32-L35), [`tests/layout/test_pnpm_workspace.py:24-32`](../../../tests/layout/test_pnpm_workspace.py#L24-L32), [`tests/layout/test_uv_workspace.py:12-27`](../../../tests/layout/test_uv_workspace.py#L12-L27) · **Source:** K01, K02, K03

| Option | For | Against |
| --- | --- | --- |
| ✅ Methods and `ClassVar`s | [AGENT.md](../../../AGENT.md) allows nothing else at module level; one place reads each file, with a clear message when it is missing | Helpers sit in the test class |
| Module functions or a `helpers.py` | Shared across files | Module-level functions are refused; two small readers do not justify a file |
| A pytest fixture (K01) | Idiomatic | A plain method is enough for one read |

**Trade-off:** each test class carries its own reader.

**Revisit when:** three or more layout tests need the same reader, which would justify a `helpers.py` in the folder.

## <a id="d8"></a>D8: Reading README links and sections

**Chosen:** split on `](` for links, and scan lines for headings, the first `bash` block and table rows · **Where:** [`tests/layout/test_folder_readmes.py:54-63`](../../../tests/layout/test_folder_readmes.py#L54-L63), [`tests/layout/test_readme_quick_start.py`](../../../tests/layout/test_readme_quick_start.py#L15-L29) · **Source:** K01, K05

| Option | For | Against |
| --- | --- | --- |
| ✅ Split and line scan | No dependency; enough for inline links | Misses reference-style links; depends on `#` headings and a `bash` fence |
| A regex | Compact | Not chosen by the worker; the reasons are not recorded |
| `markdown-it` or a Markdown library | Complete | A new dependency for five checks |

**Trade-off:** simple code that fits the READMEs of today.

**Revisit when:** a README uses reference-style links.

## <a id="d9"></a>D9: The detector test's target

**Chosen:** run the detector on the real repository root, held in a `ClassVar` · **Where:** [`tests/ci/detect_changes/test_repository_layout.py:20-30`](../../../tests/ci/detect_changes/test_repository_layout.py#L20-L30) · **Source:** K04

| Option | For | Against |
| --- | --- | --- |
| ✅ The real root | Proves criterion 3 on the folders that exist | The tests depend on the repository's state, which is the intent |
| The `detect()` helper with a fixture repository | Isolated | It writes a fixture repository, so it cannot see the real folders |

**Trade-off:** a layout change breaks these tests, on purpose.

**Revisit when:** the detector is tested on its own rules elsewhere and this file only needs the layout.

## <a id="d10"></a>D10: A change to `frontend/packages/`

**Chosen:** its README selects both front ends, with its own test · **Where:** [`tests/ci/detect_changes/test_repository_layout.py:55-70`](../../../tests/ci/detect_changes/test_repository_layout.py#L55-L70) · **Source:** K04, accepted by the reviewer

| Option | For | Against |
| --- | --- | --- |
| ✅ Selects both front ends | [AGENT.md](../../../AGENT.md) (CI/CD, step 1) says a change in `frontend/packages/` runs all of them | Departs from the brief's list of eight paths |
| Keep it in "selects nothing" and change the detector | Matches the brief | Contradicts AGENT.md |
| Drop the case | Simplest | Leaves the path uncovered |

**Trade-off:** the test follows the rule rather than the brief.

**Revisit when:** the detector treats a README-only change differently.

## <a id="d11"></a>D11: The pnpm version in the README

**Chosen:** a pointer to the `packageManager` pin · **Where:** [`README.md:194`](../../../README.md#L194) · **Source:** K12

| Option | For | Against |
| --- | --- | --- |
| ✅ Point to [`package.json`](../../../package.json) | One source of truth, correct when the pin moves | One click for the reader |
| Write the number | Visible at once | A second place to update, and D1 may change it |
| Leave it out | Shortest | The reader does not know the version exists |

**Trade-off:** the number is one link away.

**Revisit when:** D1 settles on a long-lived version.

## <a id="d12"></a>D12: Configuration page

**Chosen:** a Workspaces table of the six root files, between the first table and the target design, and per-service `conf/` paths · **Where:** [`docs/technical/architecture/configuration.md:7-28`](../../../docs/technical/architecture/configuration.md#L7-L28) · **Source:** K13

| Option | For | Against |
| --- | --- | --- |
| ✅ A table, full paths | Easy to scan for six files of one kind; explicit about where each file sits | Longer cells |
| A bullet list | Matches the first list of the page | Harder to scan |
| After the target design, or bare `conf/` paths with a note | Smaller diff | The target design would no longer be last; bare paths are wrong under D438 |

**Trade-off:** the Planned rows keep their wording, so the page mixes what exists and what is planned. The root [`conf/logger.yaml`](../../../conf/logger.yaml) is not mentioned (follow-up).

**Revisit when:** the first service exists.

## <a id="d13"></a>D13: Layout page, Today section

**Chosen:** bullets of links to each README, and the members that exist on disk · **Where:** [`docs/technical/architecture/repository-layout.md:8-26`](../../../docs/technical/architecture/repository-layout.md#L8-L26) · **Source:** K14

| Option | For | Against |
| --- | --- | --- |
| ✅ Links, members on disk only | Links resolve against the disk and can be checked; matches the state of the repository | The page needs an update when portals, packages and services appear |
| A prose paragraph without links | Shorter | Not checkable |
| A Mermaid tree | Visual | Would duplicate the target design |
| Every glob member | Complete | Names members that do not exist |

**Trade-off:** a longer section that needs maintenance.

**Revisit when:** the next ticket adds a folder or a member.

## 📝 Assumptions behind the choices

- `packageManager` is `pnpm@10.34.9`, and no specification pins a version: supports [D1](#d1) and [D11](#d11).
- `^22` means the same as `>=22 <23`: supports [D2](#d2).
- The root pyproject already declared the members and Python version, so only its comment changed: supports [D3](#d3), [D4](#d4).
- A change under `frontend/packages/` selects every front end (AGENT.md CI/CD step 1): supports [D10](#d10).
- A README fragment on the D438 link is ignored, and prose is any non-blank line that does not start with `#`: supports [D8](#d8).
- The Today section describes only what exists on disk: supports [D13](#d13).
