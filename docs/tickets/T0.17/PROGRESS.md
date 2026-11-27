# T0.17: Progress

**Status:** 🟡 Planned

<!-- ticket:specs -->
## 📚 Specifications

The specification and design pages of [TICKET.md](TICKET.md), copied by `python3 .claude/scripts/tickets/ticket_refs.py sync`.

- [Front end](../../technical/architecture/frontend.md#target-design-specified-in-gh-2-not-built-yet)
- [D43](../../specs/06-decisions/ux/d43-light-and-dark.md)
- [D46](../../specs/06-decisions/ux/d46-accessibility-standard.md)
- [D438](../../specs/06-decisions/technical/d438-repository-layout.md)
- [📜 D407 Front end](../../specs/06-decisions/technical/d407-front-end.md)
- [📜 D47 App shell](../../specs/06-decisions/ux/d47-app-shell.md)
- [📜 D49 Assistant side panel](../../specs/06-decisions/ux/d49-assistant-side-panel.md)
- [📜 D21 Languages](../../specs/06-decisions/foundations/d21-languages.md)
- [🏗️ Front end](../../technical/architecture/frontend.md)
- [🏗️ Repository layout](../../technical/architecture/repository-layout.md)
- [♿ Accessibility](../../specs/05-non-functional/accessibility.md#requirement)
- [🌍 Localisation](../../specs/05-non-functional/localisation.md)
<!-- /ticket:specs -->

## 📝 Events

| Time | Event | By | Result |
| --- | --- | --- | --- |
| 2026-11-27 18:19 | Plan written: 18 tasks, 6 waves | scribe | ⏳ Awaiting approval |
| 2026-11-27 18:19 | Plan check failed: 1 problems | scribe | ⚠️ |
| 2026-11-27 18:28 | Plan approved by the person (group approval) | 👤 person | 🟢 Approved |
| 2026-11-27 21:10 | Wave 1: 8 of 8 tasks done | workers | ✅ |
| 2026-11-27 21:10 | Integrate (Waves) | integrator | ✅ 8 integrated, 0 blocked, not committed |
| 2026-11-27 21:10 | Wave 2: 1 of 1 tasks done | workers | ✅ |
| 2026-11-27 21:10 | Integrate (Waves) | integrator | ✅ 1 integrated, 0 blocked, not committed |
| 2026-11-27 21:10 | Wave 3: 3 of 3 tasks done | workers | ✅ |
| 2026-11-27 21:10 | Integrate (Waves) | integrator | ✅ 3 integrated, 1 blocked, not committed |
| 2026-11-27 21:10 | Wave 4: 2 blocking file(s) sent to their owners: frontend/backoffice/tests/assets/symbol.spec.ts, frontend/backoffice/tests/shell/BottomTabBar.spec.ts | workers | 🔁 |
| 2026-11-27 21:10 | Integrate (Waves) | integrator | ✅ 2 integrated, 0 blocked, not committed |
| 2026-11-27 21:10 | Wave 4: 3 of 3 tasks done | workers | ✅ |
| 2026-11-27 21:10 | Integrate (Waves) | integrator | ✅ 3 integrated, 0 blocked, not committed |
| 2026-11-27 21:10 | Wave 5: 2 blocking file(s) sent to their owners: frontend/backoffice/package.json (or frontend/backoffice/tsconfig.vitest.json), frontend/backoffice/tests/setup.ts | workers | 🔁 |
| 2026-11-27 21:10 | Integrate (Waves) | integrator | ✅ 2 integrated, 1 blocked, not committed |
| 2026-11-27 21:10 | Wave 5: 0 of 1 tasks done | workers | ❌ |
| 2026-11-27 21:10 | Stopped in wave 5: K16 not done | workflow | ❌ |
| 2026-11-27 21:26 | Wave 5: 2 blocking file(s) sent to their owners: frontend/backoffice/tests/helpers/mountComponent.ts, frontend/backoffice/tests/shell/BottomTabBar.spec.ts | workers | 🔁 |
| 2026-11-27 21:26 | Integrate (Waves) | integrator | ✅ 2 integrated, 1 blocked, not committed |
| 2026-11-27 21:26 | Wave 5: 1 of 1 tasks done | workers | ✅ |
| 2026-11-27 21:26 | Integrate (Waves) | integrator | ✅ 1 integrated, 0 blocked, not committed |
| 2026-11-27 21:26 | Wave 6: 2 of 2 tasks done | workers | ✅ |
| 2026-11-27 21:26 | Integrate (Waves) | integrator | ✅ 2 integrated, 0 blocked, not committed |
| 2026-11-27 21:26 | Verify 1 (3 not applicable) | verifier | ✅ passed |
| 2026-11-27 21:26 | Review 1 (full) | reviewer | ✅ 0 blocking, 8 follow-ups |
| 2026-11-27 21:26 | Waiting for the person's code review: nothing is committed or pushed until PLAN.md says **Push:** 🟢 Approved (TKT-18) | scribe | 👀 |
| 2026-11-27 21:28 | Push approved after the code review | 👤 person | 🟢 |
| 2026-11-27 21:28 | Verify 1 (3 not applicable) | verifier | ✅ passed |


## 🔜 Follow-ups

| File | What to change |
| --- | --- |
| frontend/backoffice/README.md docs/technical/architecture/frontend.md | K18: README.md:64-71 says the Dockerfile is not part of this ticket and the image is not built yet, and frontend.md:12 says the image is not built yet. Both are wrong, because K17 ships frontend/backoffice/Dockerfile, Dockerfile.dockerignore and nginx.conf, and CI builds the image (detect_changes.py finds the Dockerfile). Describe the image as it is: a multi-stage build from the repository root, non-root nginx-unprivileged on port 8080, the wget healthcheck, and `docker build -f frontend/backoffice/Dockerfile .`. Also point the T0.22 link at frontend.md:13 to the #s04 anchor. |
| frontend/backoffice/src/shell/BottomTabBar.vue | K15: BottomTabBar.vue:32 sets `position: fixed`, but AppShell puts the tab bar in a grid row of its own and makes it sticky. Only the higher specificity of AppShell's :deep selector stops it from covering main. Remove the fixed positioning (and `inset-inline`, `bottom`, `z-index`) so the grid alone places the bar. Also split the attributes one per line to clear the 13 vue/max-attributes-per-line warnings in tests-evidences/lint.txt, as the other shell components do. |
| frontend/backoffice/src/shell/AppSidebar.vue frontend/backoffice/tests/shell/AppSidebar.spec.ts | K13 with K04: AppSidebar.vue:6 and :11 import the symbol with `?no-inline` and then strip that query with a regex, only so that the test's `/symbol\.svg$/` matches. Use a plain `import symbolUrl from '../assets/symbol.svg'`. Change the test to check that the src is set: a hashed URL or a data URI. |
| frontend/backoffice/src/shell/ThemeSwitch.vue frontend/backoffice/tests/shell/TopBar.spec.ts frontend/backoffice/src/locales/en.json frontend/backoffice/src/locales/fr.json frontend/backoffice/tests/locales/catalogues.spec.ts | K14: the switch only goes between light and dark. Once a person clicks it, nothing in the UI gets them back to 'follow the device', but the store (setPreference('system')) and the README support it. Add a third choice that calls setPreference('system'), with its labels in both catalogues and a test. Or say in the README that it can only be undone by clearing storage. |
| frontend/backoffice/index.html | K16/K09: data-theme is set only when the Pinia store is created, after the bundle loads. A user on a dark device, or with a stored dark choice, sees the light theme for a moment before the app mounts. Add a small inline script in <head> that reads `simpleerp.theme` and prefers-color-scheme and sets data-theme before the first paint. The future Playwright tests (T0.22) can cover it. |
| frontend/backoffice/Dockerfile frontend/backoffice/nginx.conf | K17: the base images `node:22-alpine` and `nginxinc/nginx-unprivileged:alpine` (mainline, a moving tag) are not pinned by digest, so two builds of the same commit can differ. Pin both by @sha256 and let Renovate/Dependabot move them. nginx.conf sends no security headers. Add at least X-Content-Type-Options nosniff, Referrer-Policy and a frame-ancestors/X-Frame-Options policy once the specification names them. |
| docs/tickets/T0.17/tests-evidences/docker-build.txt | Verifier/K17: acceptance criterion 8 has no evidence file. K17 reports a local build and a Trivy scan, but tests-evidences/ holds no output of `docker build`, of the healthcheck or of Trivy. Add the output, or rely explicitly on the images job of CI on the pull request. |
| frontend/backoffice/src/shell/AppSidebar.vue frontend/backoffice/src/shell/BottomTabBar.vue | K13/K15: the sidebar and the tab bar build their own nav items and do not use UiNavItem from @simpleerp/ui. UiNavItem takes a plain href and cannot do router navigation, so this was a reasonable choice. A later ticket should give UiNavItem a RouterLink mode, then move the shell onto it, so the item states of C-08 (including the count badge) live in one place. |

<!-- timings -->
## ⏱️ Timings

Measured from the agents' transcripts by `python3 .claude/scripts/reports/progress.py timings --ticket T0.17` (TKT-10).

| Measure | Value |
| --- | --- |
| 🕒 Ticket started | 2026-11-27 18:07:05 |
| 🕒 Last activity | 2026-11-27 21:29:22 |
| ⏱️ **Overall ticket time** (first start to last activity) | **3h22m17s** |
| 🤖 Time with agents working (sum of runs) | 47m57s |
| ⏸️ Time between runs (approvals, fixes) | 2h34m19s |
| 🔁 Workflow runs | 4 |
| 🪙 **Tokens consumed** (input, output, cache write, cache read) | **46.63M** |

#### 🪙 Tokens by model

| Model | Input | Output | Cache write | Cache read | Total |
| --- | --- | --- | --- | --- | --- |
| 🟢 haiku | 0k | 156k | 1.30M | 3.75M | **5.21M** |
| 🔵 sonnet | 1k | 477k | 2.49M | 27.33M | **30.30M** |
| 🟣 opus | 0k | 190k | 566k | 10.36M | **11.12M** |
| **All models** | 1k | 824k | 4.36M | 41.45M | **46.63M** |

### 1. ticket-plan · 2026-11-27 18:07:05 to 18:19:32 · ⏱️ 12m27s

| Phase | Start | End | Elapsed | Steps |
| --- | --- | --- | --- | --- |
| Ticket | 18:07:05 | 18:07:56 | 0m50s | 2 |
| Check | 18:07:56 | 18:08:15 | 0m19s | 3 |
| Plan | 18:08:16 | 18:17:43 | 9m27s | 1 |
| Write | 18:17:44 | 18:19:32 | 1m48s | 3 |

Tokens of this run: 0k · 267k · 921k · 6.93M · **8.11M** (input · output · cache write · cache read · total)

| Step | Model | Start | End | Elapsed | Input | Output | Cache write | Cache read | Total |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ done check T0.17 | 🟢 haiku | 18:07:05 | 18:07:12 | 0m06s | 0k | 0k | 35k | 38k | **73k** |
| ✅ ticket-writer T0.17 | 🔵 sonnet | 18:07:13 | 18:07:56 | 0m42s | 0k | 23k | 186k | 1.34M | **1.55M** |
| ✅ check TICKET.md T0.17 | 🟢 haiku | 18:07:56 | 18:08:01 | 0m04s | 0k | 1k | 38k | 73k | **113k** |
| ✅ ticket-writer fix T0.17 | 🔵 sonnet | 18:08:01 | 18:08:11 | 0m10s | 0k | 2k | 48k | 164k | **215k** |
| ✅ check TICKET.md T0.17 | 🟢 haiku | 18:08:11 | 18:08:15 | 0m03s | 0k | 0k | 2k | 71k | **73k** |
| ✅ planner T0.17 | 🟣 opus | 18:08:16 | 18:17:43 | 9m27s | 0k | 151k | 248k | 4.58M | **4.98M** |
| ✅ scribe T0.17 | 🟢 haiku | 18:17:44 | 18:19:18 | 1m34s | 0k | 85k | 186k | 529k | **800k** |
| ✅ check PLAN.md T0.17 | 🟢 haiku | 18:19:18 | 18:19:21 | 0m02s | 0k | 0k | 99k | 7k | **107k** |
| ✅ scribe plan check T0.17 | 🟢 haiku | 18:19:24 | 18:19:32 | 0m08s | 0k | 1k | 75k | 126k | **203k** |

### 2. ticket-run · 2026-11-27 20:53:15 to 21:10:40 · ⏱️ 17m24s

| Phase | Start | End | Elapsed | Steps |
| --- | --- | --- | --- | --- |
| Gate | 20:53:15 | 20:53:51 | 0m36s | 4 |
| Waves | 20:53:53 | 21:10:40 | 16m46s | 30 |
| Verify | | | not run | 0 |
| Review | | | not run | 0 |
| Finish | | | not run | 0 |

Tokens of this run: 0k · 360k · 1.80M · 19.52M · **21.68M** (input · output · cache write · cache read · total)

| Step | Model | Start | End | Elapsed | Input | Output | Cache write | Cache read | Total |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ gate T0.17 | 🟢 haiku | 20:53:15 | 20:53:26 | 0m11s | 0k | 5k | 42k | 79k | **127k** |
| ✅ plan check T0.17 | 🟢 haiku | 20:53:26 | 20:53:30 | 0m03s | 0k | 0k | 36k | 72k | **109k** |
| ✅ start rule T0.17 | 🟢 haiku | 20:53:30 | 20:53:37 | 0m06s | 0k | 0k | 34k | 37k | **72k** |
| ✅ integrator prepare T0.17 | 🔵 sonnet | 20:53:38 | 20:53:51 | 0m13s | 0k | 0k | 35k | 80k | **116k** |
| ✅ K01 test-writer | 🔵 sonnet | 20:53:53 | 20:55:26 | 1m32s | 0k | 28k | 55k | 575k | **658k** |
| ✅ K02 test-writer | 🔵 sonnet | 20:53:55 | 20:55:18 | 1m23s | 0k | 8k | 42k | 337k | **388k** |
| ✅ K03 test-writer | 🔵 sonnet | 20:53:56 | 20:54:46 | 0m50s | 0k | 6k | 42k | 380k | **428k** |
| ✅ K04 test-writer | 🔵 sonnet | 20:53:57 | 20:55:33 | 1m35s | 0k | 18k | 50k | 543k | **612k** |
| ✅ K05 test-writer | 🔵 sonnet | 20:54:00 | 20:54:49 | 0m48s | 0k | 12k | 48k | 425k | **486k** |
| ✅ K06 test-writer | 🔵 sonnet | 20:54:04 | 20:54:35 | 0m31s | 0k | 8k | 43k | 291k | **342k** |
| ✅ K07 test-writer | 🔵 sonnet | 20:54:07 | 20:55:02 | 0m55s | 0k | 8k | 52k | 488k | **550k** |
| ✅ K08 test-writer | 🔵 sonnet | 20:54:09 | 20:55:37 | 1m28s | 0k | 18k | 63k | 662k | **744k** |
| ✅ integrator Waves | 🔵 sonnet | 20:55:47 | 20:56:06 | 0m19s | 0k | 1k | 40k | 157k | **198k** |
| ✅ K09 frontend-implementer | 🔵 sonnet | 20:56:08 | 20:58:11 | 2m02s | 0k | 80k | 115k | 1.54M | **1.74M** |
| ✅ integrator Waves | 🔵 sonnet | 20:58:15 | 20:58:27 | 0m11s | 0k | 0k | 41k | 201k | **244k** |
| ✅ K10 frontend-implementer | 🔵 sonnet | 20:58:29 | 20:59:31 | 1m02s | 0k | 20k | 60k | 998k | **1.08M** |
| ✅ K11 frontend-implementer | 🔵 sonnet | 20:58:30 | 20:59:39 | 1m09s | 0k | 8k | 51k | 662k | **722k** |
| ✅ K12 frontend-implementer | 🔵 sonnet | 20:58:32 | 20:59:09 | 0m37s | 0k | 4k | 43k | 519k | **567k** |
| ✅ integrator Waves | 🔵 sonnet | 20:59:51 | 21:00:06 | 0m15s | 0k | 1k | 42k | 203k | **246k** |
| ❌ K13 frontend-implementer | 🔵 sonnet | 21:00:08 | 21:01:53 | 1m45s | 0k | 20k | 75k | 1.68M | **1.78M** |
| ✅ K14 frontend-implementer | 🔵 sonnet | 21:00:09 | 21:02:25 | 2m16s | 0k | 29k | 82k | 2.06M | **2.18M** |
| ❌ K15 frontend-implementer | 🔵 sonnet | 21:00:11 | 21:01:36 | 1m25s | 0k | 11k | 57k | 1.43M | **1.50M** |
| ✅ K04 test-writer (fix) | 🔵 sonnet | 21:02:37 | 21:03:11 | 0m33s | 0k | 1k | 37k | 162k | **201k** |
| ✅ K06 test-writer (fix) | 🔵 sonnet | 21:02:39 | 21:02:55 | 0m16s | 0k | 1k | 39k | 124k | **164k** |
| ✅ integrator Waves | 🔵 sonnet | 21:03:20 | 21:03:31 | 0m11s | 0k | 0k | 42k | 202k | **245k** |
| ✅ K13 frontend-implementer | 🔵 sonnet | 21:03:32 | 21:04:36 | 1m03s | 0k | 4k | 59k | 500k | **564k** |
| ✅ K15 frontend-implementer | 🔵 sonnet | 21:03:34 | 21:04:53 | 1m18s | 0k | 8k | 53k | 830k | **892k** |
| ✅ integrator Waves | 🔵 sonnet | 21:05:02 | 21:05:15 | 0m12s | 0k | 0k | 43k | 204k | **249k** |
| ❌ K16 frontend-implementer | 🔵 sonnet | 21:05:17 | 21:06:59 | 1m41s | 0k | 31k | 101k | 1.90M | **2.03M** |
| ✅ K09 frontend-implementer (fix) | 🔵 sonnet | 21:07:05 | 21:07:42 | 0m36s | 0k | 2k | 43k | 374k | **420k** |
| ✅ K01 test-writer (fix) | 🔵 sonnet | 21:07:06 | 21:07:56 | 0m49s | 0k | 2k | 38k | 206k | **247k** |
| ✅ integrator Waves | 🔵 sonnet | 21:08:29 | 21:08:45 | 0m15s | 0k | 1k | 41k | 201k | **244k** |
| ❌ K16 frontend-implementer | 🔵 sonnet | 21:08:47 | 21:10:22 | 1m34s | 0k | 5k | 58k | 1.13M | **1.19M** |
| ✅ scribe T0.17 | 🟢 haiku | 21:10:27 | 21:10:40 | 0m12s | 0k | 4k | 79k | 250k | **333k** |

### 3. ticket-run · 2026-11-27 21:11:06 to 21:27:38 · ⏱️ 16m32s

| Phase | Start | End | Elapsed | Steps |
| --- | --- | --- | --- | --- |
| Gate | 21:11:06 | 21:11:53 | 0m47s | 4 |
| Waves | 21:11:55 | 21:22:01 | 10m06s | 9 |
| Verify | 21:22:02 | 21:22:25 | 0m23s | 1 |
| Review | 21:22:26 | 21:26:24 | 3m58s | 1 |
| Finish | 21:26:24 | 21:27:38 | 1m14s | 4 |

Tokens of this run: 0k · 185k · 1.31M · 14.22M · **15.72M** (input · output · cache write · cache read · total)

| Step | Model | Start | End | Elapsed | Input | Output | Cache write | Cache read | Total |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ gate T0.17 | 🟢 haiku | 21:11:06 | 21:11:21 | 0m15s | 0k | 7k | 48k | 195k | **252k** |
| ✅ plan check T0.17 | 🟢 haiku | 21:11:21 | 21:11:26 | 0m04s | 0k | 0k | 34k | 74k | **109k** |
| ✅ start rule T0.17 | 🟢 haiku | 21:11:28 | 21:11:37 | 0m08s | 0k | 0k | 36k | 72k | **109k** |
| ✅ integrator prepare T0.17 | 🔵 sonnet | 21:11:37 | 21:11:53 | 0m15s | 0k | 0k | 36k | 81k | **117k** |
| ❌ K16 frontend-implementer | 🔵 sonnet | 21:11:55 | 21:13:36 | 1m40s | 0k | 26k | 85k | 1.67M | **1.79M** |
| ✅ K01 test-writer (fix) | 🔵 sonnet | 21:13:43 | 21:13:53 | 0m10s | 0k | 0k | 35k | 83k | **119k** |
| ✅ K06 test-writer (fix) | 🔵 sonnet | 21:13:44 | 21:14:37 | 0m52s | 0k | 0k | 36k | 83k | **121k** |
| ✅ integrator Waves | 🔵 sonnet | 21:14:45 | 21:15:01 | 0m15s | 0k | 1k | 41k | 202k | **245k** |
| ✅ K16 frontend-implementer | 🔵 sonnet | 21:15:05 | 21:16:35 | 1m29s | 0k | 32k | 94k | 1.71M | **1.84M** |
| ✅ integrator Waves | 🔵 sonnet | 21:16:39 | 21:16:51 | 0m12s | 0k | 1k | 45k | 243k | **289k** |
| ✅ K17 frontend-implementer | 🔵 sonnet | 21:16:53 | 21:21:38 | 4m44s | 0k | 15k | 73k | 1.99M | **2.08M** |
| ✅ K18 doc-writer | 🟢 haiku | 21:16:56 | 21:17:41 | 0m45s | 0k | 16k | 77k | 1.03M | **1.12M** |
| ✅ integrator Waves | 🔵 sonnet | 21:21:49 | 21:22:01 | 0m12s | 0k | 1k | 41k | 202k | **245k** |
| ✅ verifier round 1 | 🟢 haiku | 21:22:02 | 21:22:25 | 0m23s | 0k | 0k | 37k | 75k | **113k** |
| ✅ reviewer round 1 | 🟣 opus | 21:22:26 | 21:26:24 | 3m58s | 0k | 39k | 317k | 5.78M | **6.14M** |
| ✅ scribe T0.17 | 🟢 haiku | 21:26:24 | 21:27:02 | 0m37s | 0k | 19k | 109k | 253k | **382k** |
| ✅ explainer T0.17 | 🔵 sonnet | 21:26:24 | 21:27:31 | 1m06s | 0k | 21k | 91k | 396k | **508k** |
| ✅ docs check T0.17 1 | 🟢 haiku | 21:27:31 | 21:27:34 | 0m03s | 0k | 0k | 34k | 37k | **72k** |
| ✅ scribe T0.17 (timings) | 🟢 haiku | 21:27:34 | 21:27:38 | 0m03s | 0k | 0k | 35k | 41k | **77k** |

### 4. ticket-run · 2026-11-27 21:27:48 to 21:29:22 · ⏱️ 1m33s

| Phase | Start | End | Elapsed | Steps |
| --- | --- | --- | --- | --- |
| Gate | 21:27:48 | 21:28:30 | 0m41s | 4 |
| Waves | | | not run | 0 |
| Verify | 21:28:30 | 21:28:54 | 0m24s | 1 |
| Review | | | not run | 0 |
| Finish | 21:28:55 | 21:29:22 | 0m27s | 3 |

Tokens of this run: 0k · 11k · 325k · 773k · **1.11M** (input · output · cache write · cache read · total)

| Step | Model | Start | End | Elapsed | Input | Output | Cache write | Cache read | Total |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ gate T0.17 | 🟢 haiku | 21:27:48 | 21:28:02 | 0m13s | 0k | 6k | 47k | 158k | **212k** |
| ✅ plan check T0.17 | 🟢 haiku | 21:28:02 | 21:28:05 | 0m02s | 0k | 0k | 34k | 37k | **72k** |
| ✅ start rule T0.17 | 🟢 haiku | 21:28:05 | 21:28:15 | 0m09s | 0k | 0k | 34k | 74k | **109k** |
| ✅ integrator prepare T0.17 | 🔵 sonnet | 21:28:17 | 21:28:30 | 0m12s | 0k | 0k | 36k | 81k | **118k** |
| ✅ verifier round 1 | 🟢 haiku | 21:28:30 | 21:28:54 | 0m24s | 0k | 0k | 35k | 116k | **152k** |
| ✅ scribe T0.17 | 🟢 haiku | 21:28:55 | 21:29:12 | 0m16s | 0k | 2k | 70k | 263k | **336k** |
| ✅ docs check T0.17 1 | 🟢 haiku | 21:29:13 | 21:29:19 | 0m06s | 0k | 0k | 34k | 37k | **72k** |
| 🔄 integrator finish T0.17 | 🔵 sonnet | 21:29:20 | 21:29:22 | 0m02s | 0k | 0k | 32k | 4k | **37k** |
<!-- /timings -->
