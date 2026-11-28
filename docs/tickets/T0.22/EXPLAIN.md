# T0.22: Playwright scaffold against the real images

**Status:** ✅ Done · **Ticket:** [TICKET.md](TICKET.md) · **Choices and trade-offs:** [IMPLEMENTATION.md](IMPLEMENTATION.md) · **Review:** [REVIEW.md](REVIEW.md)

## 🔭 What it does

- The back office has a Playwright suite that runs against the real images, never a development server, in four projects: light and dark, English and French.
- A failing test keeps its trace, video and screenshot, and the HTML report is written to a folder that CI uploads.
- Each part of the T0.17 shell has `@smoke` tests: the sidebar, the top bar, the phone tab bar, the theme, the language and keyboard navigation.
- An accessibility check (axe-core, WCAG 2.2 AA) runs after every test.
- The runner script passes the suite's configuration to Playwright, and tests of the script itself prove how it does so.

## ⚙️ How it works

1. **The runner finds the suite:** for each front end with an `e2e/` folder, the script builds an optional `--config` argument when `playwright.config.ts` exists, in [`.github/scripts/playwright.sh:16-19`](../../../.github/scripts/playwright.sh#L16-L19). It installs Chromium and runs `playwright test` from the front end's folder, forwarding extra arguments such as `--grep @smoke`, in [`.github/scripts/playwright.sh:21`](../../../.github/scripts/playwright.sh#L21). A failure marks the run failed, and the other front ends still run.
2. **The configuration sets the contract:** one viewport of 1440 x 900 at [`frontend/backoffice/e2e/playwright.config.ts:3`](../../../frontend/backoffice/e2e/playwright.config.ts#L3), the base URL from `ERP_E2E_BASE_URL` at [`frontend/backoffice/e2e/playwright.config.ts:12`](../../../frontend/backoffice/e2e/playwright.config.ts#L12), trace, video and screenshot kept on failure at [`frontend/backoffice/e2e/playwright.config.ts:13-15`](../../../frontend/backoffice/e2e/playwright.config.ts#L13-L15), and the list and HTML reporters at [`frontend/backoffice/e2e/playwright.config.ts:10`](../../../frontend/backoffice/e2e/playwright.config.ts#L10). No web server is started.
3. **Four projects:** `light-en`, `dark-en`, `light-fr` and `dark-fr`, each a Chromium project with its colour scheme and locale, in [`frontend/backoffice/e2e/playwright.config.ts:18-21`](../../../frontend/backoffice/e2e/playwright.config.ts#L18-L21). Every test runs once per project.
4. **Every test is also an accessibility test:** the automatic fixture waits for the test body, then, if the page left `about:blank`, runs axe, in [`frontend/backoffice/e2e/fixtures/test.ts:4-13`](../../../frontend/backoffice/e2e/fixtures/test.ts#L4-L13). The scan uses the WCAG tags of [`frontend/backoffice/e2e/fixtures/accessibility.ts:4`](../../../frontend/backoffice/e2e/fixtures/accessibility.ts#L4) and throws a list of violations at [`frontend/backoffice/e2e/fixtures/accessibility.ts:13`](../../../frontend/backoffice/e2e/fixtures/accessibility.ts#L13).
5. **The shell tests find the text in the catalogues:** they load `en.json` or `fr.json` according to the project's locale, so a label is never written twice. The sidebar tests do it with JSON import attributes at [`frontend/backoffice/e2e/shell/sidebar.e2e.ts:1-7`](../../../frontend/backoffice/e2e/shell/sidebar.e2e.ts#L1-L7), the language tests with `readFileSync` at [`frontend/backoffice/e2e/preferences/language.e2e.ts:16-19`](../../../frontend/backoffice/e2e/preferences/language.e2e.ts#L16-L19), and the keyboard tests at [`frontend/backoffice/e2e/accessibility/keyboard.e2e.ts:14-18`](../../../frontend/backoffice/e2e/accessibility/keyboard.e2e.ts#L14-L18).
6. **The shell screens:** the expanded and collapsed sidebar, in [`frontend/backoffice/e2e/shell/sidebar.e2e.ts:11`](../../../frontend/backoffice/e2e/shell/sidebar.e2e.ts#L11) and [`frontend/backoffice/e2e/shell/sidebar.e2e.ts:32`](../../../frontend/backoffice/e2e/shell/sidebar.e2e.ts#L32); the top bar's places, in [`frontend/backoffice/e2e/shell/top-bar.e2e.ts:11`](../../../frontend/backoffice/e2e/shell/top-bar.e2e.ts#L11); and the phone tab bar at 390 x 844, in [`frontend/backoffice/e2e/shell/phone.e2e.ts:13`](../../../frontend/backoffice/e2e/shell/phone.e2e.ts#L13) and [`frontend/backoffice/e2e/shell/phone.e2e.ts:22`](../../../frontend/backoffice/e2e/shell/phone.e2e.ts#L22). Locators use roles and accessible names, and `data-shell` only where no role exists.
7. **Theme and language:** the active theme must follow the device setting, the two themes must paint different backgrounds, and the manual switch overrides the device, in [`frontend/backoffice/e2e/preferences/theme.e2e.ts:10-30`](../../../frontend/backoffice/e2e/preferences/theme.e2e.ts#L10-L30). The page declares the project's language and shows no raw catalogue key, in [`frontend/backoffice/e2e/preferences/language.e2e.ts:21-38`](../../../frontend/backoffice/e2e/preferences/language.e2e.ts#L21-L38).
8. **Keyboard:** the first Tab focuses the skip link and Enter moves focus to `main`, in [`frontend/backoffice/e2e/accessibility/keyboard.e2e.ts:44-57`](../../../frontend/backoffice/e2e/accessibility/keyboard.e2e.ts#L44-L57). A loop of at most 40 Tab presses collects the focused place, taken as the nearest `data-place` ancestor ([`frontend/backoffice/e2e/accessibility/keyboard.e2e.ts:20-29`](../../../frontend/backoffice/e2e/accessibility/keyboard.e2e.ts#L20-L29)), checks a visible focus on each ([`frontend/backoffice/e2e/accessibility/keyboard.e2e.ts:31-41`](../../../frontend/backoffice/e2e/accessibility/keyboard.e2e.ts#L31-L41)), and compares them with every sidebar item and top bar place, in [`frontend/backoffice/e2e/accessibility/keyboard.e2e.ts:66-97`](../../../frontend/backoffice/e2e/accessibility/keyboard.e2e.ts#L66-L97).
9. **Explicit accessibility scans of three states:** expanded sidebar, collapsed sidebar and phone tab bar, in [`frontend/backoffice/e2e/accessibility/axe.e2e.ts:5-28`](../../../frontend/backoffice/e2e/accessibility/axe.e2e.ts#L5-L28).
10. **The scaffold guards itself:** tests read the loaded configuration and check the retained artefacts, the absence of a web server, the report folder resolved against the config's own folder, the four projects and the base URL, in [`frontend/backoffice/e2e/scaffold/config.e2e.ts:8-52`](../../../frontend/backoffice/e2e/scaffold/config.e2e.ts#L8-L52).
11. **Tooling:** the two packages are pinned at [`frontend/backoffice/package.json:28-29`](../../../frontend/backoffice/package.json#L28-L29); lint now covers `e2e/` and typecheck adds the e2e project, at [`frontend/backoffice/package.json:14-15`](../../../frontend/backoffice/package.json#L14-L15), with the e2e project's own settings in [`frontend/backoffice/e2e/tsconfig.json`](../../../frontend/backoffice/e2e/tsconfig.json).
12. **The script is tested:** a stand-in `pnpm` logs its working folder and arguments ([`tests/ci/playwright/helpers.py:10-14`](../../../tests/ci/playwright/helpers.py#L10-L14)), the real script runs against it ([`tests/ci/playwright/helpers.py:28`](../../../tests/ci/playwright/helpers.py#L28)), and the cases are in [`tests/ci/playwright/test_playwright_script.py:9-43`](../../../tests/ci/playwright/test_playwright_script.py#L9-L43).

## 🧱 Files and lines changed

<!-- changes -->
| File | Change | Lines in the new version | Added | Removed |
| --- | --- | --- | --- | --- |
| [`.github/scripts/playwright.sh`](../../../.github/scripts/playwright.sh) | Modified | [4-5](../../../.github/scripts/playwright.sh#L4), [16-19](../../../.github/scripts/playwright.sh#L16), [21](../../../.github/scripts/playwright.sh#L21) | +7 | −2 |
| [`docs/technical/architecture/frontend.md`](../../../docs/technical/architecture/frontend.md) | Modified | [13-15](../../../docs/technical/architecture/frontend.md#L13), [46](../../../docs/technical/architecture/frontend.md#L46) | +4 | −3 |
| [`docs/technical/delivery/tests-and-traceability.md`](../../../docs/technical/delivery/tests-and-traceability.md) | Modified | [20-50](../../../docs/technical/delivery/tests-and-traceability.md#L20), [139](../../../docs/technical/delivery/tests-and-traceability.md#L139) | +32 | −1 |
| [`frontend/backoffice/.gitignore`](../../../frontend/backoffice/.gitignore) | Added | [1-2](../../../frontend/backoffice/.gitignore#L1) | +2 | −0 |
| [`frontend/backoffice/README.md`](../../../frontend/backoffice/README.md) | Modified | [64-70](../../../frontend/backoffice/README.md#L64) | +7 | −0 |
| [`frontend/backoffice/e2e/accessibility/axe.e2e.ts`](../../../frontend/backoffice/e2e/accessibility/axe.e2e.ts) | Added | [1-29](../../../frontend/backoffice/e2e/accessibility/axe.e2e.ts#L1) | +29 | −0 |
| [`frontend/backoffice/e2e/accessibility/keyboard.e2e.ts`](../../../frontend/backoffice/e2e/accessibility/keyboard.e2e.ts) | Added | [1-98](../../../frontend/backoffice/e2e/accessibility/keyboard.e2e.ts#L1) | +98 | −0 |
| [`frontend/backoffice/e2e/fixtures/accessibility.ts`](../../../frontend/backoffice/e2e/fixtures/accessibility.ts) | Added | [1-14](../../../frontend/backoffice/e2e/fixtures/accessibility.ts#L1) | +14 | −0 |
| [`frontend/backoffice/e2e/fixtures/test.ts`](../../../frontend/backoffice/e2e/fixtures/test.ts) | Added | [1-16](../../../frontend/backoffice/e2e/fixtures/test.ts#L1) | +16 | −0 |
| [`frontend/backoffice/e2e/playwright.config.ts`](../../../frontend/backoffice/e2e/playwright.config.ts) | Added | [1-23](../../../frontend/backoffice/e2e/playwright.config.ts#L1) | +23 | −0 |
| [`frontend/backoffice/e2e/preferences/language.e2e.ts`](../../../frontend/backoffice/e2e/preferences/language.e2e.ts) | Added | [1-39](../../../frontend/backoffice/e2e/preferences/language.e2e.ts#L1) | +39 | −0 |
| [`frontend/backoffice/e2e/preferences/theme.e2e.ts`](../../../frontend/backoffice/e2e/preferences/theme.e2e.ts) | Added | [1-31](../../../frontend/backoffice/e2e/preferences/theme.e2e.ts#L1) | +31 | −0 |
| [`frontend/backoffice/e2e/scaffold/config.e2e.ts`](../../../frontend/backoffice/e2e/scaffold/config.e2e.ts) | Added | [1-53](../../../frontend/backoffice/e2e/scaffold/config.e2e.ts#L1) | +53 | −0 |
| [`frontend/backoffice/e2e/shell/phone.e2e.ts`](../../../frontend/backoffice/e2e/shell/phone.e2e.ts) | Added | [1-32](../../../frontend/backoffice/e2e/shell/phone.e2e.ts#L1) | +32 | −0 |
| [`frontend/backoffice/e2e/shell/sidebar.e2e.ts`](../../../frontend/backoffice/e2e/shell/sidebar.e2e.ts) | Added | [1-55](../../../frontend/backoffice/e2e/shell/sidebar.e2e.ts#L1) | +55 | −0 |
| [`frontend/backoffice/e2e/shell/top-bar.e2e.ts`](../../../frontend/backoffice/e2e/shell/top-bar.e2e.ts) | Added | [1-28](../../../frontend/backoffice/e2e/shell/top-bar.e2e.ts#L1) | +28 | −0 |
| [`frontend/backoffice/e2e/tsconfig.json`](../../../frontend/backoffice/e2e/tsconfig.json) | Added | [1-9](../../../frontend/backoffice/e2e/tsconfig.json#L1) | +9 | −0 |
| [`frontend/backoffice/package.json`](../../../frontend/backoffice/package.json) | Modified | [14-15](../../../frontend/backoffice/package.json#L14), [28-29](../../../frontend/backoffice/package.json#L28) | +4 | −2 |
| [`pnpm-lock.yaml`](../../../pnpm-lock.yaml) | Modified | [39-44](../../../pnpm-lock.yaml#L39), [238-243](../../../pnpm-lock.yaml#L238), [559-563](../../../pnpm-lock.yaml#L559), [1685-1694](../../../pnpm-lock.yaml#L1685), [2138-2142](../../../pnpm-lock.yaml#L2138), [2358-2361](../../../pnpm-lock.yaml#L2358), [3530-3535](../../../pnpm-lock.yaml#L3530) | +42 | −0 |
| [`tests/ci/playwright/helpers.py`](../../../tests/ci/playwright/helpers.py) | Added | [1-52](../../../tests/ci/playwright/helpers.py#L1) | +52 | −0 |
| [`tests/ci/playwright/test_playwright_script.py`](../../../tests/ci/playwright/test_playwright_script.py) | Added | [1-50](../../../tests/ci/playwright/test_playwright_script.py#L1) | +50 | −0 |
| **21 files** | | | **+627** | **−8** |
<!-- /changes -->

- [`.github/scripts/playwright.sh`](../../../.github/scripts/playwright.sh), lines [`13-19`](../../../.github/scripts/playwright.sh#L13-L19): passes `--config e2e/playwright.config.ts` when the front end has one, through an array so that nothing is word-split.
- [`frontend/backoffice/e2e/playwright.config.ts`](../../../frontend/backoffice/e2e/playwright.config.ts) and [`frontend/backoffice/e2e/tsconfig.json`](../../../frontend/backoffice/e2e/tsconfig.json): the configuration, the four projects and the type settings of the suite.
- [`frontend/backoffice/e2e/fixtures/test.ts`](../../../frontend/backoffice/e2e/fixtures/test.ts) and [`frontend/backoffice/e2e/fixtures/accessibility.ts`](../../../frontend/backoffice/e2e/fixtures/accessibility.ts): the automatic axe fixture and its scan.
- [`frontend/backoffice/e2e/shell/sidebar.e2e.ts`](../../../frontend/backoffice/e2e/shell/sidebar.e2e.ts), [`frontend/backoffice/e2e/shell/top-bar.e2e.ts`](../../../frontend/backoffice/e2e/shell/top-bar.e2e.ts), [`frontend/backoffice/e2e/shell/phone.e2e.ts`](../../../frontend/backoffice/e2e/shell/phone.e2e.ts): one test file per shell screen of T0.17.
- [`frontend/backoffice/e2e/preferences/theme.e2e.ts`](../../../frontend/backoffice/e2e/preferences/theme.e2e.ts) and [`frontend/backoffice/e2e/preferences/language.e2e.ts`](../../../frontend/backoffice/e2e/preferences/language.e2e.ts): the two themes and the two languages.
- [`frontend/backoffice/e2e/accessibility/keyboard.e2e.ts`](../../../frontend/backoffice/e2e/accessibility/keyboard.e2e.ts) and [`frontend/backoffice/e2e/accessibility/axe.e2e.ts`](../../../frontend/backoffice/e2e/accessibility/axe.e2e.ts): keyboard reach and explicit scans.
- [`frontend/backoffice/e2e/scaffold/config.e2e.ts`](../../../frontend/backoffice/e2e/scaffold/config.e2e.ts): the configuration contract of acceptance criteria 2 and 3.
- [`frontend/backoffice/package.json`](../../../frontend/backoffice/package.json), [`pnpm-lock.yaml`](../../../pnpm-lock.yaml): the two Playwright packages, the lint and typecheck scripts.
- [`frontend/backoffice/.gitignore`](../../../frontend/backoffice/.gitignore): keeps the report and results folders out of git.
- [`tests/ci/playwright/helpers.py`](../../../tests/ci/playwright/helpers.py), [`tests/ci/playwright/test_playwright_script.py`](../../../tests/ci/playwright/test_playwright_script.py): tests of the runner script with a stand-in `pnpm`.
- [`docs/technical/delivery/tests-and-traceability.md`](../../../docs/technical/delivery/tests-and-traceability.md), lines [`20-50`](../../../docs/technical/delivery/tests-and-traceability.md#L20-L50): the new Playwright section (projects, tags, reports, runner, local commands).
- [`docs/technical/architecture/frontend.md`](../../../docs/technical/architecture/frontend.md), lines [`14-16`](../../../docs/technical/architecture/frontend.md#L14-L16), and [`frontend/backoffice/README.md`](../../../frontend/backoffice/README.md), lines [`64-70`](../../../frontend/backoffice/README.md#L64-L70): short statements that link to that section.

## 🧪 How to test it

```bash
python3 .claude/scripts/tickets/ticket_tree.py diff --ticket T0.22 --name-only
uv run pytest tests/ci/playwright -n 2
pnpm --filter ./frontend/backoffice run lint
pnpm --filter ./frontend/backoffice run typecheck
docker compose -f compose.e2e.yaml up --detach --wait
bash .github/scripts/playwright.sh --grep @smoke
pnpm --filter ./frontend/backoffice exec playwright show-report playwright-report
```

The first four show the checks recorded below. The last three need Docker and run the suite against the real images, as CI and [`.github/workflows/stage.yml`](../../../.github/workflows/stage.yml) do. The stack is described in [`compose.e2e.yaml`](../../../compose.e2e.yaml).

## 🔗 Evidence

- [Lint](tests-evidences/lint.txt): warnings only.
- [Type check](tests-evidences/typecheck.txt): passes.
- [Vitest](tests-evidences/test.txt): backoffice 128 tests passed.
- [pytest](tests-evidences/pytest.txt): 1390 passed.
- [ruff check](tests-evidences/ruff-check.txt), [ruff format](tests-evidences/ruff-format.txt) and [mypy](tests-evidences/mypy.txt): pass.
- [pnpm install](tests-evidences/pnpm-install.txt), [plan view](tests-evidences/plan-view.txt) and [ticket references](tests-evidences/ticket-refs.txt): the plan and install checks.
- No Playwright run against the real images is recorded: the criteria are confirmed by reading until CI runs them (see the follow-ups).

## 📝 Assumptions accepted

None.

## 🔜 Follow-ups

| File | What to change |
| --- | --- |
| [`docs/tickets/T0.22/tests-evidences/`](tests-evidences/) | No Playwright run is recorded. `checks.py` runs lint, typecheck, Vitest and pytest, never `playwright test` against [`compose.e2e.yaml`](../../../compose.e2e.yaml). Once the stack is up, run the last three commands of "How to test it" and keep its output (and `--list`). |
| [`docs/technical/delivery/tests-and-traceability.md`](../../../docs/technical/delivery/tests-and-traceability.md) | Link [D121](../../../docs/specs/06-decisions/ux/d121-mockup-sizes.md) instead of the plain ID, and link the config and e2e folders, now that they exist. |
| [`frontend/backoffice/package.json`](../../../frontend/backoffice/package.json), [`frontend/backoffice/eslint.config.js`](../../../frontend/backoffice/eslint.config.js) | `e2e/` is un-ignored by `--ignore-pattern '!e2e/**'` in the lint script while the config ignores it. Remove `e2e/**` from the config's ignores and go back to `eslint .`, so the editor and CI agree. Also check that ESLint really lints `e2e/`: the lint evidence names no e2e file. |
| [`frontend/backoffice/e2e/shell/sidebar.e2e.ts`](../../../frontend/backoffice/e2e/shell/sidebar.e2e.ts), [`frontend/backoffice/e2e/shell/top-bar.e2e.ts`](../../../frontend/backoffice/e2e/shell/top-bar.e2e.ts), [`frontend/backoffice/e2e/shell/phone.e2e.ts`](../../../frontend/backoffice/e2e/shell/phone.e2e.ts), [`frontend/backoffice/e2e/preferences/language.e2e.ts`](../../../frontend/backoffice/e2e/preferences/language.e2e.ts), [`frontend/backoffice/e2e/accessibility/keyboard.e2e.ts`](../../../frontend/backoffice/e2e/accessibility/keyboard.e2e.ts) | The catalogues are read three ways (import attributes, `readFileSync` from the working folder, `readFileSync` from the test folder). Share one helper in `e2e/fixtures/` such as `labels()`, so one way holds and nothing depends on the working folder. |
| [`frontend/backoffice/e2e/accessibility/axe.e2e.ts`](../../../frontend/backoffice/e2e/accessibility/axe.e2e.ts) | The automatic fixture already runs axe after every test, so the explicit calls scan each state twice. Keep one of them. The comment about the user menu can go once the menu exists. |
