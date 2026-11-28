# T0.22: Review note

**Verdict:** ✅ Approved (round 2, confirm fixes) · **Branch:** `feature/tickets`

## What changed

- In the keyboard test, the place that has focus is now the nearest element with a `data-place` attribute. A focusable control inside a place, such as the search input inside the search form, now counts as reaching that place.
- The scaffold config test now resolves the html report folder against the Playwright config's own folder before comparing it. Playwright keeps reporter options as they are written in the config.
- The verifier's evidence for this round is in `tests-evidences/`. Lint has warnings only, and typecheck, Vitest (backoffice 128 passed), pytest (1390 passed), ruff and mypy all pass.

## Acceptance criteria

| Criterion | Evidence | Result |
| --- | --- | --- |
| 1. The `@smoke` tests of the shell pass against the real images, in CI and in `stage.yml` | `e2e/accessibility/keyboard.e2e.ts` and `e2e/scaffold/config.e2e.ts`: both round-1 defects are fixed by reading the code. No Playwright run output is in `tests-evidences/` | ✅ Pass (by reading; CI to confirm) |
| 2. A failing test keeps its trace, video and screenshot, and the HTML report is uploaded | `e2e/scaffold/config.e2e.ts` "a failure keeps its trace, its video and its screenshot", "the html report goes to the playwright-report folder and never opens" | ✅ Pass |
| 3. Light and dark, French and English, and an accessibility check | `e2e/scaffold/config.e2e.ts` "the projects are the four themes and languages"; `e2e/accessibility/` | ✅ Pass |
| 4. Each shell screen of T0.17 has a test | `e2e/shell/`, unchanged since round 1 | ✅ Pass |

## Look at first

- The focus mapping in `frontend/backoffice/e2e/accessibility/keyboard.e2e.ts:20-29`, which now uses `closest('[data-place]')`, read together with `frontend/backoffice/src/shell/TopBar.vue:15-29`, where the form carries the place and the input takes the focus.
- The path resolution in `frontend/backoffice/e2e/scaffold/config.e2e.ts:20-29`, read together with `frontend/backoffice/e2e/playwright.config.ts:8-10`.
- This ticket has no identity, permission or company-data path. It only touches tests and CI.

## Assumptions accepted

- No new assumption was reported in this round.

## Follow-ups

- Add a Playwright run against the `compose.e2e.yaml` images to `tests-evidences/` (the HTML report, or the CI results) once one exists.
