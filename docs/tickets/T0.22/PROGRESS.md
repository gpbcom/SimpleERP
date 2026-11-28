# T0.22: Playwright scaffold against the real images, progress

**Status:** 🟡 Planned

<!-- ticket:specs -->
## 📚 Specifications

The specification and design pages of [TICKET.md](TICKET.md), copied by `python3 .claude/scripts/tickets/ticket_refs.py sync`.

- [🏗️ Tests and traceability](../../technical/delivery/tests-and-traceability.md#levels)
- [🏗️ CI/CD and stages](../../technical/delivery/ci-cd-and-stages.md#stages-dev-and-qa)
- [🏗️ CI/CD and stages](../../technical/delivery/ci-cd-and-stages.md#workflows)
- [📜 D426 Testing strategy](../../specs/06-decisions/technical/d426-testing-strategy.md)
- [📜 D47 App shell](../../specs/06-decisions/ux/d47-app-shell.md)
- [📜 D43 Light and dark modes](../../specs/06-decisions/ux/d43-light-and-dark.md)
- [📜 D21 Languages](../../specs/06-decisions/foundations/d21-languages.md)
- [📜 D46 Accessibility standard](../../specs/06-decisions/ux/d46-accessibility-standard.md)
- [🏗️ Tests and traceability](../../technical/delivery/tests-and-traceability.md)
- [🏗️ CI/CD and stages](../../technical/delivery/ci-cd-and-stages.md)
- [🏗️ Front end](../../technical/architecture/frontend.md)
- [♿ Accessibility](../../specs/05-non-functional/accessibility.md)
<!-- /ticket:specs -->

## 📝 Events

| Time | Event | By | Result |
| --- | --- | --- | --- |
| 2026-11-27 18:13 | Plan written: 8 tasks, 2 waves | scribe | ⏳ Awaiting approval |
| 2026-11-27 18:29 | Plan approved by the person (group approval) | 👤 person | 🟢 Approved |
| 2026-11-28 01:09 | Wave 1: 6 of 6 tasks done | workers | ✅ |
| 2026-11-28 01:09 | Integrate (Waves) | integrator | ✅ 6 integrated, 0 blocked, not committed |
| 2026-11-28 01:09 | Wave 2: 3 blocking file(s) sent to their owners: frontend/backoffice/e2e/shell/top-bar.e2e.ts, frontend/backoffice/e2e/shell/phone.e2e.ts, frontend/backoffice/e2e/shell/sidebar.e2e.ts | workers | 🔁 |
| 2026-11-28 01:09 | Integrate (Waves) | integrator | ✅ 1 integrated, 0 blocked, not committed |
| 2026-11-28 01:09 | Wave 2: 2 of 2 tasks done | workers | ✅ |
| 2026-11-28 01:09 | Integrate (Waves) | integrator | ✅ 2 integrated, 0 blocked, not committed |
| 2026-11-28 01:09 | Verify 1 (2 not applicable) | verifier | ✅ passed |
| 2026-11-28 01:09 | Review 1 (full) | reviewer | ⚠️ 2 blocking, 5 follow-ups |
| 2026-11-28 01:09 | Integrate (Review) | integrator | ✅ 2 integrated, 0 blocked, not committed |
| 2026-11-28 01:09 | Review 2 (confirm fixes) | reviewer | ✅ 0 blocking, 1 follow-ups |
| 2026-11-28 01:09 | Waiting for the person's code review: nothing is committed or pushed until PLAN.md says **Push:** 🟢 Approved (TKT-18) | scribe | 👀 Awaiting code review |
| 2026-11-28 01:13 | Push approved after the code review | 👤 person | 🟢 |
| 2026-11-28 01:13 | Verify 1 (2 not applicable) | verifier | ✅ passed |

## 🔜 Follow-ups

| File | What to change |
| --- | --- |
| docs/tickets/T0.22/tests-evidences/ | No Playwright run is recorded. checks.py runs lint, typecheck, Vitest and pytest, but never `playwright test` against compose.e2e.yaml, which is why the two failures above were not caught. Once the fixes land, run `docker compose -f compose.e2e.yaml up --detach --wait && bash .github/scripts/playwright.sh --grep @smoke` and keep its output (and `--list`) in tests-evidences/. |
| docs/technical/delivery/tests-and-traceability.md | D121 has a page, docs/specs/06-decisions/ux/d121-mockup-sizes.md. Link it instead of writing the plain ID. Now that the scaffold exists, also link frontend/backoffice/e2e/playwright.config.ts and the e2e folders, which are now plain text. |
| frontend/backoffice/package.json frontend/backoffice/eslint.config.js | e2e/ is un-ignored through `--ignore-pattern '!e2e/**'` in the lint script, while eslint.config.js ignores it. Remove 'e2e/**' from the ignores of eslint.config.js and go back to `eslint .`, so that the editor's ESLint and CI agree. Also check that ESLint really lints e2e/: the lint evidence names no e2e file. |
| frontend/backoffice/e2e/shell/sidebar.e2e.ts frontend/backoffice/e2e/shell/top-bar.e2e.ts frontend/backoffice/e2e/shell/phone.e2e.ts frontend/backoffice/e2e/preferences/language.e2e.ts frontend/backoffice/e2e/accessibility/keyboard.e2e.ts | The catalogues are read three ways: JSON import attributes (K01), readFileSync from process.cwd() (K02), and readFileSync from testInfo.project.testDir (K03). Share one helper in e2e/fixtures/ (for example `labels()`), so that one way holds and nothing depends on the cwd. |
| frontend/backoffice/e2e/accessibility/axe.e2e.ts | The automatic fixture already runs axe after every test, so the explicit `expectNoAccessibilityViolations` calls scan each state twice. Keep the explicit scan or the fixture for these states, not both. The comment about the user menu can go once the menu exists. |
| docs/tickets/T0.22/tests-evidences/ | The evidence folder has lint, typecheck, Vitest, pytest, ruff and mypy, but no output of a Playwright run against the compose.e2e.yaml images. AC1 to AC4 can only be confirmed by reading the tests until CI runs them. Attach the Playwright report or the CI run's results when one exists. |

<!-- timings -->
## ⏱️ Timings

Measured from the agents' transcripts by `python3 .claude/scripts/reports/progress.py timings --ticket T0.22` (TKT-10).

| Measure | Value |
| --- | --- |
| 🕒 Ticket started | 2026-11-27 18:07:05 |
| 🕒 Last activity | 2026-11-28 01:13:49 |
| ⏱️ **Overall ticket time** (first start to last activity) | **7h06m44s** |
| 🤖 Time with agents working (sum of runs) | 25m02s |
| ⏸️ Time between runs (approvals, fixes) | 6h41m41s |
| 🔁 Workflow runs | 3 |
| 🪙 **Tokens consumed** (input, output, cache write, cache read) | **23.31M** |

#### 🪙 Tokens by model

| Model | Input | Output | Cache write | Cache read | Total |
| --- | --- | --- | --- | --- | --- |
| 🟢 haiku | 0k | 73k | 920k | 3.26M | **4.26M** |
| 🔵 sonnet | 0k | 189k | 1.20M | 10.33M | **11.72M** |
| 🟣 opus | 0k | 115k | 558k | 6.66M | **7.33M** |
| **All models** | 0k | 378k | 2.68M | 20.25M | **23.31M** |

### 1. ticket-plan · 2026-11-27 18:07:05 to 18:14:13 · ⏱️ 7m07s

| Phase | Start | End | Elapsed | Steps |
| --- | --- | --- | --- | --- |
| Ticket | 18:07:05 | 18:08:11 | 1m05s | 2 |
| Check | 18:08:11 | 18:08:15 | 0m03s | 1 |
| Plan | 18:08:15 | 18:13:13 | 4m57s | 1 |
| Write | 18:13:13 | 18:14:13 | 0m59s | 2 |

Tokens of this run: 0k · 153k · 678k · 6.51M · **7.34M** (input · output · cache write · cache read · total)

| Step | Model | Start | End | Elapsed | Input | Output | Cache write | Cache read | Total |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ done check T0.22 | 🟢 haiku | 18:07:05 | 18:07:12 | 0m06s | 0k | 0k | 37k | 73k | **112k** |
| ✅ ticket-writer T0.22 | 🔵 sonnet | 18:07:12 | 18:08:11 | 0m58s | 0k | 36k | 193k | 2.19M | **2.42M** |
| ✅ check TICKET.md T0.22 | 🟢 haiku | 18:08:11 | 18:08:15 | 0m03s | 0k | 0k | 35k | 38k | **73k** |
| ✅ planner T0.22 | 🟣 opus | 18:08:15 | 18:13:13 | 4m57s | 0k | 79k | 253k | 3.72M | **4.05M** |
| ✅ scribe T0.22 | 🟢 haiku | 18:13:13 | 18:14:10 | 0m56s | 0k | 37k | 123k | 450k | **610k** |
| ✅ check PLAN.md T0.22 | 🟢 haiku | 18:14:10 | 18:14:13 | 0m03s | 0k | 0k | 35k | 38k | **73k** |

### 2. ticket-run · 2026-11-28 00:55:46 to 01:11:31 · ⏱️ 15m45s

| Phase | Start | End | Elapsed | Steps |
| --- | --- | --- | --- | --- |
| Gate | 00:55:46 | 00:56:30 | 0m43s | 4 |
| Waves | 00:56:32 | 01:02:26 | 5m53s | 13 |
| Verify | 01:02:26 | 01:03:39 | 1m12s | 1 |
| Review | 01:03:39 | 01:09:20 | 5m40s | 6 |
| Finish | 01:09:20 | 01:11:31 | 2m10s | 4 |

Tokens of this run: 0k · 219k · 1.72M · 13.00M · **14.94M** (input · output · cache write · cache read · total)

| Step | Model | Start | End | Elapsed | Input | Output | Cache write | Cache read | Total |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ gate T0.22 | 🟢 haiku | 00:55:46 | 00:55:56 | 0m10s | 0k | 2k | 41k | 169k | **213k** |
| ✅ plan check T0.22 | 🟢 haiku | 00:55:57 | 00:56:01 | 0m04s | 0k | 0k | 36k | 78k | **116k** |
| ✅ start rule T0.22 | 🟢 haiku | 00:56:04 | 00:56:15 | 0m10s | 0k | 0k | 36k | 39k | **76k** |
| ✅ integrator prepare T0.22 | 🔵 sonnet | 00:56:15 | 00:56:30 | 0m14s | 0k | 0k | 37k | 84k | **122k** |
| ✅ K01 test-writer | 🔵 sonnet | 00:56:32 | 00:58:11 | 1m38s | 0k | 18k | 66k | 700k | **786k** |
| ✅ K02 test-writer | 🔵 sonnet | 00:56:35 | 00:58:06 | 1m31s | 0k | 10k | 55k | 953k | **1.02M** |
| ✅ K03 test-writer | 🔵 sonnet | 00:56:38 | 00:57:39 | 1m01s | 0k | 16k | 78k | 814k | **909k** |
| ✅ K04 test-writer | 🔵 sonnet | 00:56:39 | 00:57:46 | 1m06s | 0k | 7k | 47k | 400k | **455k** |
| ✅ K05 test-writer | 🔵 sonnet | 00:56:42 | 00:57:59 | 1m16s | 0k | 13k | 58k | 560k | **632k** |
| ✅ K08 doc-writer | 🟢 haiku | 00:56:44 | 00:57:37 | 0m53s | 0k | 12k | 76k | 1.14M | **1.23M** |
| ✅ integrator Waves | 🔵 sonnet | 00:58:20 | 00:58:35 | 0m14s | 0k | 1k | 75k | 129k | **206k** |
| ❌ K06 frontend-implementer | 🔵 sonnet | 00:58:37 | 01:00:00 | 1m23s | 0k | 20k | 69k | 1.15M | **1.24M** |
| ✅ K07 implementer | 🔵 sonnet | 00:58:38 | 00:59:18 | 0m39s | 0k | 1k | 40k | 178k | **219k** |
| ✅ K01 test-writer (fix) | 🔵 sonnet | 01:00:07 | 01:00:42 | 0m34s | 0k | 0k | 38k | 89k | **128k** |
| ✅ integrator Waves | 🔵 sonnet | 01:00:51 | 01:01:01 | 0m09s | 0k | 0k | 43k | 209k | **253k** |
| ✅ K06 frontend-implementer | 🔵 sonnet | 01:01:03 | 01:02:09 | 1m06s | 0k | 19k | 68k | 948k | **1.04M** |
| ✅ integrator Waves | 🔵 sonnet | 01:02:14 | 01:02:26 | 0m11s | 0k | 0k | 39k | 169k | **209k** |
| ✅ verifier round 1 | 🟢 haiku | 01:02:26 | 01:03:39 | 1m12s | 0k | 0k | 39k | 80k | **120k** |
| ✅ reviewer round 1 | 🟣 opus | 01:03:39 | 01:07:01 | 3m22s | 0k | 30k | 226k | 2.39M | **2.64M** |
| ✅ K03 test-writer (fix) | 🔵 sonnet | 01:07:03 | 01:07:19 | 0m15s | 0k | 0k | 41k | 88k | **130k** |
| ✅ K04 test-writer (fix) | 🔵 sonnet | 01:07:05 | 01:07:19 | 0m14s | 0k | 1k | 42k | 87k | **131k** |
| ✅ integrator Review | 🔵 sonnet | 01:07:22 | 01:07:32 | 0m09s | 0k | 0k | 42k | 166k | **209k** |
| ✅ verifier after review 1 | 🟢 haiku | 01:07:32 | 01:08:43 | 1m10s | 0k | 0k | 37k | 82k | **120k** |
| ✅ reviewer round 2 | 🟣 opus | 01:08:43 | 01:09:20 | 0m36s | 0k | 5k | 78k | 555k | **640k** |
| ✅ scribe T0.22 | 🟢 haiku | 01:09:20 | 01:09:46 | 0m25s | 0k | 13k | 99k | 288k | **401k** |
| ✅ explainer T0.22 | 🔵 sonnet | 01:09:20 | 01:11:20 | 2m00s | 0k | 37k | 127k | 1.32M | **1.49M** |
| ✅ docs check T0.22 1 | 🟢 haiku | 01:11:20 | 01:11:25 | 0m04s | 0k | 0k | 39k | 76k | **117k** |
| ✅ scribe T0.22 (timings) | 🟢 haiku | 01:11:28 | 01:11:31 | 0m03s | 0k | 0k | 37k | 44k | **81k** |

### 3. ticket-run · 2026-11-28 01:11:40 to 01:13:49 · ⏱️ 2m09s

| Phase | Start | End | Elapsed | Steps |
| --- | --- | --- | --- | --- |
| Gate | 01:11:40 | 01:12:22 | 0m42s | 4 |
| Waves | | | not run | 0 |
| Verify | 01:12:23 | 01:13:33 | 1m10s | 1 |
| Review | | | not run | 0 |
| Finish | 01:13:33 | 01:13:49 | 0m16s | 3 |

Tokens of this run: 0k · 5k · 281k · 740k · **1.03M** (input · output · cache write · cache read · total)

| Step | Model | Start | End | Elapsed | Input | Output | Cache write | Cache read | Total |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ gate T0.22 | 🟢 haiku | 01:11:40 | 01:11:45 | 0m05s | 0k | 1k | 46k | 122k | **169k** |
| ✅ plan check T0.22 | 🟢 haiku | 01:11:47 | 01:11:51 | 0m04s | 0k | 0k | 37k | 79k | **116k** |
| ✅ start rule T0.22 | 🟢 haiku | 01:11:53 | 01:12:06 | 0m13s | 0k | 0k | 37k | 79k | **116k** |
| ✅ integrator prepare T0.22 | 🔵 sonnet | 01:12:09 | 01:12:22 | 0m13s | 0k | 0k | 37k | 85k | **124k** |
| ✅ verifier round 1 | 🟢 haiku | 01:12:23 | 01:13:33 | 1m10s | 0k | 0k | 39k | 80k | **120k** |
| ✅ scribe T0.22 | 🟢 haiku | 01:13:33 | 01:13:42 | 0m09s | 0k | 1k | 45k | 213k | **261k** |
| ✅ docs check T0.22 1 | 🟢 haiku | 01:13:42 | 01:13:47 | 0m04s | 0k | 0k | 37k | 79k | **117k** |
| 🔄 integrator finish T0.22 | 🔵 sonnet | 01:13:49 | 01:13:49 | 0m00s | 0k | 0k | 0k | 0k | **0k** |
<!-- /timings -->
