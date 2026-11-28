# T0.22: Implementation choices

**Ticket:** [TICKET.md](TICKET.md) · **How it works:** [EXPLAIN.md](EXPLAIN.md) · **Review:** [REVIEW.md](REVIEW.md)

## 🎯 Constraints

- The tests run against the real images started by [`compose.e2e.yaml`](../../../compose.e2e.yaml), never a development server, and live in the app's `e2e/` folder ([`AGENT.md`](../../../AGENT.md), front ends).
- A failure keeps its trace, video and screenshot, and the HTML report is uploaded (acceptance criterion 2 of [TICKET.md](TICKET.md), [D426](../../specs/06-decisions/technical/d426-testing-strategy.md)).
- Light and dark, French and English, and an accessibility check are covered ([D43](../../specs/06-decisions/ux/d43-light-and-dark.md), [D21](../../specs/06-decisions/foundations/d21-languages.md), [D46](../../specs/06-decisions/ux/d46-accessibility-standard.md)).
- Each shell screen of T0.17 has a test (TKT-21, [`.claude/rules/tickets.md`](../../../.claude/rules/tickets.md)).
- The lint, typecheck and Vitest checks of `checks.py` must keep passing with the new suite.
- The runner script is shared by CI and [`stage.yml`](../../../.github/workflows/stage.yml), so it must keep working for front ends with and without a config.
- Several files of the ticket belong to different tasks, so choices made by one task could not change another task's file (TKT-4).

## ⚖️ Choices at a glance

| # | Decision | Chosen | Main alternative | Trade-off accepted |
| --- | --- | --- | --- | --- |
| [D1](#d1) | Where the expected labels come from | The real catalogue JSON, by the language of the project | Hard-coded English and French text | Tests depend on the shell's file layout, and three loading styles coexist |
| [D2](#d2) | How elements are located | Roles and accessible names, `data-shell` only where none exists | CSS classes or `data-testid` everywhere | Tests also check accessible names, and are tied to a few data attributes |
| [D3](#d3) | How accessibility is checked | An automatic fixture running axe after every test, plus explicit scans of three states | An explicit call in each test | Some states are scanned twice |
| [D4](#d4) | The projects | Four Chromium projects sharing one viewport | Repeating the viewport, or Playwright device presets | One viewport of 1440 x 900 only |
| [D5](#d5) | How the theme is tested | Compare the background before and after the manual switch | Emulate the colour scheme in a second page | Tests the switch rather than a second device setting |
| [D6](#d6) | The scaffold contract | Seven separate `@smoke` tests that read the loaded config | One large test | More test entries per project |
| [D7](#d7) | The keyboard test | One Tab loop with a cap, the place taken as the nearest `data-place` | One test per item, or a fixed Tab count | Tied to the shell's markup, a cap of 40 presses |
| [D8](#d8) | How the report folder is checked | Resolve it against the config's folder, then match the path | Assert the literal relative string | Needs the config file path at run time |
| [D9](#d9) | How the runner passes the config | A bash array, empty or `--config ...` | Two full branches, or an unquoted string | Needs bash 4.4 or newer |
| [D10](#d10) | How the runner is tested | A bash stand-in `pnpm` first on `PATH` | A Python stand-in, as for the release tests | A second style of stand-in in the repository |
| [D11](#d11) | How lint reaches `e2e/` | `--ignore-pattern '!e2e/**'` in the script | Edit the ESLint config, or a second lint script | The un-ignore lives in the script, not the config |
| [D12](#d12) | Package versions | Exact pins | Caret ranges | Manual bumps |
| [D13](#d13) | Where the documentation goes | One Playwright section in the tests page, linked from the others | A separate page, or the README alone | A longer section in an existing page |

## <a id="d1"></a>D1: Where the expected labels come from

**Chosen:** read the catalogue JSON by the project's locale · **Where:** [`frontend/backoffice/e2e/shell/sidebar.e2e.ts:1-7`](../../../frontend/backoffice/e2e/shell/sidebar.e2e.ts#L1-L7), [`frontend/backoffice/e2e/preferences/language.e2e.ts:16-19`](../../../frontend/backoffice/e2e/preferences/language.e2e.ts#L16-L19), [`frontend/backoffice/e2e/accessibility/keyboard.e2e.ts:14-18`](../../../frontend/backoffice/e2e/accessibility/keyboard.e2e.ts#L14-L18) · **Source:** K01, K02, K03

| Option | For | Against |
| --- | --- | --- |
| ✅ Read the catalogue | The tests follow the real translations in all four projects, and a changed label does not break them (K01) | They depend on the file layout of `src/locales` |
| Hard-code English and French | Independent of the shell's files | A wording change breaks every project, and the text is written twice |
| Read the label from the page | No file read | It would test the page against itself |
| `data-shell` and `data-nav-item` only | Language independent | Does not prove that the right text shows in each language (D21) |

K01 used JSON import attributes (needs Node 22 and the `resolveJsonModule` of [`frontend/backoffice/e2e/tsconfig.json`](../../../frontend/backoffice/e2e/tsconfig.json)), K02 used `readFileSync` from the working folder (it depends on the folder the run starts in), and K03 used `readFileSync` from the test folder. The three tasks worked in parallel, and each avoided files it did not own, so the three styles coexist.

**Trade-off:** correct translations are tested, at the price of three ways of loading them.

**Revisit when:** the next ticket adds an e2e test. The review follow-up asks for one shared helper in `e2e/fixtures/`.

## <a id="d2"></a>D2: How elements are located

**Chosen:** roles and accessible names, `data-shell` only for the symbol, the tab bar and the sidebar · **Where:** [`frontend/backoffice/e2e/shell/phone.e2e.ts:13-20`](../../../frontend/backoffice/e2e/shell/phone.e2e.ts#L13-L20) · **Source:** K01, K03

| Option | For | Against |
| --- | --- | --- |
| ✅ Roles and names | The tests also check that elements are named for assistive technology ([D46](../../specs/06-decisions/ux/d46-accessibility-standard.md)) | The symbol has an empty alt text and the sidebar is an `aside` whose role depends on context, so three elements need `data-shell` |
| CSS classes | Simple | Break on a style refactor and prove nothing about accessibility |
| `data-testid` on every element | Stable | Adds markup everywhere, and hides a missing accessible name |

K03 also located the shell through its `data-shell` and `data-place` attributes for the keyboard and scan tests, because they are language independent and one test serves all four projects.

**Trade-off:** the tests are tied to a few data attributes of the shell.

**Revisit when:** the shell changes its markup, or gives the three elements roles.

## <a id="d3"></a>D3: How accessibility is checked

**Chosen:** an automatic fixture that runs axe after each test, and explicit scans of the sidebar expanded, collapsed and the phone tab bar · **Where:** [`frontend/backoffice/e2e/fixtures/test.ts:4-13`](../../../frontend/backoffice/e2e/fixtures/test.ts#L4-L13), [`frontend/backoffice/e2e/accessibility/axe.e2e.ts:5-28`](../../../frontend/backoffice/e2e/accessibility/axe.e2e.ts#L5-L28) · **Source:** K06, K03

| Option | For | Against |
| --- | --- | --- |
| ✅ Automatic fixture | Every test is checked with no code per test (D46) | A test that stays on `about:blank` is skipped |
| An explicit call in each test | Visible in each test | Forgotten in the next test |
| An `afterEach` hook | Same effect | Named by K06 as an alternative, with no reason given against it (open point) |

**Trade-off:** the explicit scans of [`frontend/backoffice/e2e/accessibility/axe.e2e.ts`](../../../frontend/backoffice/e2e/accessibility/axe.e2e.ts) repeat what the fixture does, so each of those states is scanned twice. Both were kept because the explicit tests give the criterion a named test per state.

**Revisit when:** the scan time matters. The follow-up asks to keep one of the two for these states.

## <a id="d4"></a>D4: The projects

**Chosen:** four Chromium projects sharing one `VIEWPORT` constant · **Where:** [`frontend/backoffice/e2e/playwright.config.ts:3-21`](../../../frontend/backoffice/e2e/playwright.config.ts#L3-L21) · **Source:** K06

| Option | For | Against |
| --- | --- | --- |
| ✅ One constant, four projects | One place to change the viewport, and the 1440 x 900 of D121 | Chromium only |
| Repeat the viewport per project | No constant | Four places to change |
| `devices` presets | Ready made | Impose another viewport than 1440 x 900 |

The phone size is set only in the phone tests, with `test.use`.

**Trade-off:** one browser, one desktop size. The ticket asks for themes and languages, not browsers.

**Revisit when:** a browser or a device matrix is required.

## <a id="d5"></a>D5: How the theme is tested

**Chosen:** compare the computed body background before and after the manual switch · **Where:** [`frontend/backoffice/e2e/preferences/theme.e2e.ts:15-23`](../../../frontend/backoffice/e2e/preferences/theme.e2e.ts#L15-L23) · **Source:** K02

| Option | For | Against |
| --- | --- | --- |
| ✅ Compare through the switch | One page, and the real switch | Does not test two device settings in one test |
| Emulate the colour scheme in a second page | Tests the device setting directly | Needs a second page, and the four projects already set the scheme |

**Trade-off:** each project tests its own device setting, and the switch tests the other theme.

**Revisit when:** the theme logic grows beyond the device setting and the switch.

## <a id="d6"></a>D6: The scaffold contract

**Chosen:** separate `@smoke` tests that read the loaded config; the scheme, locale and viewport together in one test · **Where:** [`frontend/backoffice/e2e/scaffold/config.e2e.ts:8-52`](../../../frontend/backoffice/e2e/scaffold/config.e2e.ts#L8-L52) · **Source:** K04

| Option | For | Against |
| --- | --- | --- |
| ✅ One test per contract point | A failure names the broken setting | A few more entries per project |
| One large test | Fewer entries | A failure hides the other points |

The tests read the config through `test.info()`, which proves the retained trace, video and screenshot of criterion 2 without having to fail a test.

**Trade-off:** the contract is checked, not a real failing run. Nothing yet proves that a failure keeps its artefacts and that the report is uploaded.

**Revisit when:** a Playwright run is added to the evidence, see the follow-up.

## <a id="d7"></a>D7: The keyboard test

**Chosen:** one Tab loop, capped at 40 presses, that collects the focused place and checks its visible focus · **Where:** [`frontend/backoffice/e2e/accessibility/keyboard.e2e.ts:66-97`](../../../frontend/backoffice/e2e/accessibility/keyboard.e2e.ts#L66-L97) · **Source:** K03, review round 2

| Option | For | Against |
| --- | --- | --- |
| ✅ One loop | One test whatever the number of items, stops once all are reached, and a cap makes an unreachable item fail instead of hang | A shared failure message |
| One test per item | Names the item | Grows with each item |
| A fixed Tab count | Simple | Breaks as soon as an item is added |

The place is the nearest `data-place` ancestor of the focused element ([`frontend/backoffice/e2e/accessibility/keyboard.e2e.ts:20-29`](../../../frontend/backoffice/e2e/accessibility/keyboard.e2e.ts#L20-L29)), K03's choice over special-casing the search input or adding `data-place` to the input (a file K03 did not own). The review round 2 found the first version missed the search input and fixed it this way.

**Trade-off:** generic for any wrapper place, but tied to `data-place`.

**Revisit when:** the shell holds more than about 40 tab stops.

## <a id="d8"></a>D8: How the report folder is checked

**Chosen:** resolve `outputFolder` against the folder of the config file, then match `frontend/backoffice/playwright-report` · **Where:** [`frontend/backoffice/e2e/scaffold/config.e2e.ts:20-29`](../../../frontend/backoffice/e2e/scaffold/config.e2e.ts#L20-L29) · **Source:** K04, review round 2

| Option | For | Against |
| --- | --- | --- |
| ✅ Resolve, then match | Checks the real destination and survives a different relative spelling | Needs the config file path at run time |
| Assert the literal `../playwright-report` | No path logic | Ties the test to one spelling |

The reporter options are read through a narrow cast to `{ outputFolder?: string; open?: string }` ([`frontend/backoffice/e2e/scaffold/config.e2e.ts:22`](../../../frontend/backoffice/e2e/scaffold/config.e2e.ts#L22)), rather than Playwright's reporter types or `any`, to keep strict typing with no new import. It trusts the shape of the html reporter's second tuple element.

**Trade-off:** a little path logic in a test.

**Revisit when:** Playwright changes how it reports reporter options.

## <a id="d9"></a>D9: How the runner passes the config

**Chosen:** an array that is empty or holds `--config e2e/playwright.config.ts`, expanded before the extra arguments · **Where:** [`.github/scripts/playwright.sh:16-21`](../../../.github/scripts/playwright.sh#L16-L21) · **Source:** K07

| Option | For | Against |
| --- | --- | --- |
| ✅ An array | One command line, no word splitting | Needs bash 4.4 or newer for an empty array under `set -u` |
| Two `if`/`else` branches with a full command each | Works on any bash | Duplicates the command |
| A string expanded unquoted | Short | Word splitting |

**Trade-off:** requires bash 4.4 or newer. The script's tests ([`tests/ci/playwright/test_playwright_script.py:9-43`](../../../tests/ci/playwright/test_playwright_script.py#L9-L43)) run it under the local bash.

**Revisit when:** the script must run on macOS's default bash 3.2. That is an open point: nobody reported checking it.

## <a id="d10"></a>D10: How the runner is tested

**Chosen:** a bash stand-in `pnpm` written to the test folder and put first on `PATH`, logging `cwd|args` and failing when a `fail` marker file exists · **Where:** [`tests/ci/playwright/helpers.py:10-14`](../../../tests/ci/playwright/helpers.py#L10-L14) · **Source:** K05

| Option | For | Against |
| --- | --- | --- |
| ✅ A bash stand-in | Needs no interpreter lookup, and is the language of the script under test | Differs from the Python `FAKE_GH` of the release tests |
| A Python stand-in, as in [`tests/ci/release/helpers.py`](../../../tests/ci/release/helpers.py) | Same style as the release tests | Not chosen by K05 for the reason in the first row |
| An exported shell function | No file | A function is not what the real script finds on `PATH` |

[`AGENT.md`](../../../AGENT.md) prefers real things to mocks, and a stand-in executable is the style of the release tests. Only `playwright test` calls are read from the log, and `install` calls are ignored ([`tests/ci/playwright/helpers.py:41`](../../../tests/ci/playwright/helpers.py#L41)).

**Trade-off:** one more stand-in style.

**Revisit when:** the repository gathers its stand-ins into one helper.

## <a id="d11"></a>D11: How lint reaches `e2e/`

**Chosen:** `eslint . --ignore-pattern '!e2e/**'` · **Where:** [`frontend/backoffice/package.json:14`](../../../frontend/backoffice/package.json#L14) · **Source:** K06

| Option | For | Against |
| --- | --- | --- |
| ✅ Un-ignore in the script | Lint covers `e2e/` without touching a file the task did not own | The config and the script disagree, and the editor's ESLint still ignores `e2e/` |
| Remove `e2e/**` from the ignores of [`frontend/backoffice/eslint.config.js`](../../../frontend/backoffice/eslint.config.js) | One place | That file belongs to another task |
| A second `eslint e2e` script | Explicit | A second lint command for CI to run |

**Trade-off:** accepted for ownership reasons. The lint evidence names no e2e file, so it is not shown that the e2e files are linted.

**Revisit when:** the config's owner allows it. This is the follow-up.

## <a id="d12"></a>D12: Package versions

**Chosen:** `@playwright/test` 1.65.1 and `@axe-core/playwright` 4.14.1, with no caret · **Where:** [`frontend/backoffice/package.json:28-29`](../../../frontend/backoffice/package.json#L28-L29) · **Source:** K06

| Option | For | Against |
| --- | --- | --- |
| ✅ Exact pins | Matches the pinned style of the lock (D415), no drift. 4.14.1 is the version of the axe-core already used | Manual bumps |
| Caret ranges | Automatic patches | Browser and library may drift between runs |

**Trade-off:** manual bumps for repeatable runs.

**Revisit when:** the dependency policy changes.

## <a id="d13"></a>D13: Where the documentation goes

**Chosen:** a Playwright section in [`docs/technical/delivery/tests-and-traceability.md`](../../../docs/technical/delivery/tests-and-traceability.md) (lines 20-50), linked from [`docs/technical/architecture/frontend.md`](../../../docs/technical/architecture/frontend.md) and [`frontend/backoffice/README.md`](../../../frontend/backoffice/README.md) · **Where:** [`docs/technical/delivery/tests-and-traceability.md:20`](../../../docs/technical/delivery/tests-and-traceability.md#L20) · **Source:** K08

| Option | For | Against |
| --- | --- | --- |
| ✅ One section between Levels and Test helpers | The test levels stay in one page, and the other two stay short | A longer page |
| A separate Playwright page | Focused | A fourth place to keep current |
| Everything in the README | Next to the code | The levels are then split from the page that defines them |

K08 named the config and test folders as plain text, because links to files not yet there would have failed the check; they exist now, and linking them is a follow-up.

**Trade-off:** plain-text names that do not click.

**Revisit when:** the next edit of the page.

## 📝 Assumptions behind the choices

None.
