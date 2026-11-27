# T0.16: Progress

**Status:** 🟡 Planned

<!-- ticket:specs -->
## 📚 Specifications

The specification and design pages of [TICKET.md](TICKET.md), copied by `python3 .claude/scripts/tickets/ticket_refs.py sync`.

- [D21](../../specs/06-decisions/foundations/d21-languages.md)
- [Localisation](../../specs/05-non-functional/localisation.md)
- [REQ-T10-03](../../specs/03-technical/t10-translations-and-notifications/requirements/req-t10-03-money-decimals.md)
- [REQ-T10-01](../../specs/03-technical/t10-translations-and-notifications/requirements/req-t10-01-translation-catalogues.md)
- [📜 D407 Front end](../../specs/06-decisions/technical/d407-front-end.md)
- [🏗️ Front end](../../technical/architecture/frontend.md)
- [🌐 Localisation](../../specs/05-non-functional/localisation.md#measures)
<!-- /ticket:specs -->

## 📝 Events

| Time | Event | By | Result |
| --- | --- | --- | --- |
| 2026-11-27 18:13 | Plan written: 18 tasks, 4 waves | scribe | ⏳ Awaiting approval |
| 2026-11-27 18:28 | Plan approved by the person (group approval) | 👤 person | 🟢 Approved |
| 2026-11-27 20:09 | Wave 1: 8 of 8 tasks done | workers | ✅ |
| 2026-11-27 20:09 | Integrate (Waves) | integrator | ✅ 8 integrated, 0 blocked, not committed |
| 2026-11-27 20:09 | Wave 2: 1 of 1 tasks done | workers | ✅ |
| 2026-11-27 20:09 | Integrate (Waves) | integrator | ✅ 1 integrated, 0 blocked, not committed |
| 2026-11-27 20:09 | Wave 3: 8 of 8 tasks done | workers | ✅ |
| 2026-11-27 20:09 | Integrate (Waves) | integrator | ✅ 8 integrated, 0 blocked, not committed |
| 2026-11-27 20:09 | Wave 4: 3 blocking file(s) sent to their owners: frontend/packages/i18n/tests/format/formatDate.test.ts, frontend/packages/i18n/tests/format/formatMoney.test.ts, frontend/packages/i18n/tests/format/formatNumber.test.ts | workers | 🔁 |
| 2026-11-27 20:09 | Integrate (Waves) | integrator | ✅ 3 integrated, 0 blocked, not committed |
| 2026-11-27 20:09 | Wave 4: 1 of 1 tasks done | workers | ✅ |
| 2026-11-27 20:09 | Integrate (Waves) | integrator | ✅ 1 integrated, 1 blocked, not committed |
| 2026-11-27 20:09 | Verify 1 | verifier | ✅ passed |
| 2026-11-27 20:09 | Review 1 (full) | reviewer | ✅ 0 blocking, 5 follow-ups |
| 2026-11-27 20:09 | Waiting for the person's code review: nothing is committed or pushed until PLAN.md says **Push:** 🟢 Approved (TKT-18) | scribe | 👀 |
| 2026-11-27 20:17 | Push approved after the code review | 👤 person | 🟢 |
| 2026-11-27 20:17 | Verify 1 | verifier | ✅ passed |


## 🔜 Follow-ups

| File | What to change |
| --- | --- |
| frontend/packages/i18n/src/format/formatNumber.ts frontend/packages/i18n/tests/format/formatNumber.test.ts | Line 6 of the doc comment says a decimal string 'stays exact'. With the default options, Intl.NumberFormat still rounds it to 3 fraction digits, so formatNumber('1.23456', 'en-GB') gives '1.235'. Either say in the comment that rounding follows the options (maximumFractionDigits), or default maximumFractionDigits to the string's own decimals the way formatMoney does, and add a test for the default case. Owner: K13. |
| frontend/packages/i18n/src/check/findMissingKeys.ts frontend/packages/i18n/tests/check/findMissingKeys.test.ts | flatten (lines 3-12) recurses into any value that is not a string. A number or array leaf in a JSON catalogue is silently dropped, so it is never reported, and a null leaf throws a TypeError. Report a value that is neither a string nor a plain object as missing in its language, and add a test for it. Owner: K11 (K01 for the test). |
| frontend/packages/i18n/README.md | The 'Where it sits' section says the package is 'built on the design system's tokens', but it does not depend on @simpleerp/tokens. Drop that clause or reword it. The list of consumers (backoffice, portals, mobile) is an assumption (K17). Mark it as the target until T0.17 wires the first app. Owner: K17. |
| frontend/packages/i18n/src frontend/packages/i18n/tests | Files mix single and double quotes and use semicolons in some files but not others: formatNumber.ts and index.ts have none, formatMoney.ts and createI18n.ts have them. Lint passes, so add a formatter rule to @simpleerp/config, or align the files in a later ticket. Owners: K10 to K16. |
| frontend/packages/i18n/src/check/findMissingKeys.ts frontend/packages/i18n/src/translate/createI18n.ts | The helpers flatten and compare have no doc comment, and pickCatalog and resolveKey have only a one-line summary. The other functions have full TSDoc with params, returns and throws. Add the same to these helpers for consistency. Owners: K11 and K15. |

<!-- timings -->
## ⏱️ Timings

Measured from the agents' transcripts by `python3 .claude/scripts/reports/progress.py timings --ticket T0.16` (TKT-10).

| Measure | Value |
| --- | --- |
| 🕒 Ticket started | 2026-11-27 18:07:05 |
| 🕒 Last activity | 2026-11-27 20:17:18 |
| ⏱️ **Overall ticket time** (first start to last activity) | **2h10m12s** |
| 🤖 Time with agents working (sum of runs) | 23m29s |
| ⏸️ Time between runs (approvals, fixes) | 1h46m43s |
| 🔁 Workflow runs | 3 |
| 🪙 **Tokens consumed** (input, output, cache write, cache read) | **23.91M** |

#### 🪙 Tokens by model

| Model | Input | Output | Cache write | Cache read | Total |
| --- | --- | --- | --- | --- | --- |
| 🟢 haiku | 0k | 116k | 1.53M | 3.75M | **5.39M** |
| 🔵 sonnet | 0k | 168k | 1.51M | 12.93M | **14.60M** |
| 🟣 opus | 0k | 90k | 365k | 3.46M | **3.91M** |
| **All models** | 0k | 375k | 3.40M | 20.13M | **23.91M** |

### 1. ticket-plan · 2026-11-27 18:07:05 to 18:14:49 · ⏱️ 7m43s

| Phase | Start | End | Elapsed | Steps |
| --- | --- | --- | --- | --- |
| Ticket | 18:07:05 | 18:08:03 | 0m57s | 2 |
| Check | 18:08:03 | 18:08:18 | 0m15s | 3 |
| Plan | 18:08:19 | 18:13:30 | 5m11s | 1 |
| Write | 18:13:31 | 18:14:49 | 1m17s | 2 |

Tokens of this run: 0k · 142k · 652k · 5.24M · **6.03M** (input · output · cache write · cache read · total)

| Step | Model | Start | End | Elapsed | Input | Output | Cache write | Cache read | Total |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ done check T0.16 | 🟢 haiku | 18:07:05 | 18:07:12 | 0m06s | 0k | 0k | 37k | 73k | **112k** |
| ✅ ticket-writer T0.16 | 🔵 sonnet | 18:07:12 | 18:08:03 | 0m50s | 0k | 25k | 159k | 1.87M | **2.05M** |
| ✅ check TICKET.md T0.16 | 🟢 haiku | 18:08:03 | 18:08:07 | 0m03s | 0k | 0k | 37k | 73k | **112k** |
| ✅ ticket-writer fix T0.16 | 🔵 sonnet | 18:08:07 | 18:08:15 | 0m07s | 0k | 1k | 41k | 124k | **167k** |
| ✅ check TICKET.md T0.16 | 🟢 haiku | 18:08:15 | 18:08:18 | 0m03s | 0k | 0k | 2k | 71k | **73k** |
| ✅ planner T0.16 | 🟣 opus | 18:08:19 | 18:13:30 | 5m11s | 0k | 72k | 183k | 2.27M | **2.53M** |
| ✅ scribe T0.16 | 🟢 haiku | 18:13:31 | 18:14:45 | 1m14s | 0k | 41k | 154k | 713k | **909k** |
| ✅ check PLAN.md T0.16 | 🟢 haiku | 18:14:45 | 18:14:49 | 0m03s | 0k | 0k | 35k | 38k | **73k** |

### 2. ticket-run · 2026-11-27 19:56:28 to 20:10:52 · ⏱️ 14m23s

| Phase | Start | End | Elapsed | Steps |
| --- | --- | --- | --- | --- |
| Gate | 19:56:28 | 19:57:08 | 0m40s | 4 |
| Waves | 19:57:09 | 20:07:23 | 10m13s | 28 |
| Verify | 20:07:23 | 20:07:44 | 0m20s | 1 |
| Review | 20:07:45 | 20:09:23 | 1m38s | 1 |
| Finish | 20:09:23 | 20:10:52 | 1m28s | 4 |

Tokens of this run: 0k · 214k · 2.19M · 14.22M · **16.63M** (input · output · cache write · cache read · total)

| Step | Model | Start | End | Elapsed | Input | Output | Cache write | Cache read | Total |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ gate T0.16 | 🟢 haiku | 19:56:28 | 19:56:41 | 0m13s | 0k | 6k | 76k | 166k | **249k** |
| ✅ plan check T0.16 | 🟢 haiku | 19:56:42 | 19:56:46 | 0m04s | 0k | 0k | 68k | 40k | **109k** |
| ✅ start rule T0.16 | 🟢 haiku | 19:56:47 | 19:56:53 | 0m06s | 0k | 0k | 37k | 73k | **111k** |
| ✅ integrator prepare T0.16 | 🔵 sonnet | 19:56:54 | 19:57:08 | 0m14s | 0k | 0k | 35k | 81k | **117k** |
| ✅ K01 test-writer | 🔵 sonnet | 19:57:09 | 19:58:22 | 1m13s | 0k | 6k | 48k | 205k | **261k** |
| ✅ K02 test-writer | 🔵 sonnet | 19:57:11 | 19:57:59 | 0m48s | 0k | 6k | 50k | 343k | **400k** |
| ✅ K03 test-writer | 🔵 sonnet | 19:57:13 | 19:57:50 | 0m37s | 0k | 4k | 41k | 253k | **300k** |
| ✅ K04 test-writer | 🔵 sonnet | 19:57:15 | 19:57:43 | 0m28s | 0k | 2k | 37k | 166k | **207k** |
| ✅ K05 test-writer | 🔵 sonnet | 19:57:18 | 19:57:55 | 0m36s | 0k | 3k | 40k | 210k | **253k** |
| ✅ K06 test-writer | 🔵 sonnet | 19:57:23 | 19:58:12 | 0m48s | 0k | 4k | 41k | 211k | **258k** |
| ✅ K07 test-writer | 🔵 sonnet | 19:57:27 | 19:58:14 | 0m47s | 0k | 6k | 43k | 294k | **343k** |
| ✅ K08 test-writer | 🔵 sonnet | 19:57:32 | 19:58:18 | 0m45s | 0k | 4k | 40k | 251k | **296k** |
| ✅ integrator Waves | 🔵 sonnet | 19:58:35 | 19:58:56 | 0m21s | 0k | 1k | 41k | 241k | **284k** |
| ✅ K09 frontend-implementer | 🔵 sonnet | 19:58:58 | 20:00:08 | 1m09s | 0k | 16k | 57k | 684k | **758k** |
| ✅ integrator Waves | 🔵 sonnet | 20:00:18 | 20:00:30 | 0m12s | 0k | 0k | 40k | 201k | **242k** |
| ✅ K10 frontend-implementer | 🔵 sonnet | 20:00:32 | 20:01:17 | 0m45s | 0k | 5k | 45k | 703k | **753k** |
| ✅ K11 frontend-implementer | 🔵 sonnet | 20:00:34 | 20:01:21 | 0m47s | 0k | 6k | 46k | 578k | **631k** |
| ✅ K12 frontend-implementer | 🔵 sonnet | 20:00:37 | 20:01:47 | 1m10s | 0k | 6k | 45k | 520k | **572k** |
| ✅ K13 frontend-implementer | 🔵 sonnet | 20:00:40 | 20:01:31 | 0m50s | 0k | 5k | 45k | 699k | **750k** |
| ✅ K14 frontend-implementer | 🔵 sonnet | 20:00:42 | 20:01:33 | 0m50s | 0k | 4k | 43k | 560k | **608k** |
| ✅ K15 frontend-implementer | 🔵 sonnet | 20:00:44 | 20:02:04 | 1m19s | 0k | 9k | 52k | 637k | **699k** |
| ✅ K17 doc-writer | 🟢 haiku | 20:00:47 | 20:01:33 | 0m46s | 0k | 10k | 95k | 533k | **640k** |
| ❌ K18 doc-writer | 🟢 haiku | 20:00:50 | 20:01:50 | 0m59s | 0k | 8k | 78k | 433k | **519k** |
| ✅ K18 doc-writer | 🟢 haiku | 20:02:22 | 20:02:46 | 0m24s | 0k | 4k | 74k | 384k | **463k** |
| ✅ integrator Waves | 🔵 sonnet | 20:02:47 | 20:03:09 | 0m21s | 0k | 1k | 44k | 208k | **253k** |
| ❌ K16 frontend-implementer | 🔵 sonnet | 20:03:10 | 20:04:30 | 1m20s | 0k | 7k | 53k | 1.13M | **1.19M** |
| ✅ K05 test-writer (fix) | 🔵 sonnet | 20:04:37 | 20:04:59 | 0m22s | 0k | 1k | 39k | 288k | **329k** |
| ✅ K03 test-writer (fix) | 🔵 sonnet | 20:04:38 | 20:05:51 | 1m12s | 0k | 2k | 38k | 249k | **289k** |
| ✅ K04 test-writer (fix) | 🔵 sonnet | 20:04:40 | 20:05:16 | 0m35s | 0k | 2k | 39k | 499k | **541k** |
| ✅ integrator Waves | 🔵 sonnet | 20:06:05 | 20:06:20 | 0m14s | 0k | 0k | 43k | 208k | **253k** |
| ✅ K16 frontend-implementer | 🔵 sonnet | 20:06:22 | 20:07:06 | 0m44s | 0k | 3k | 47k | 665k | **716k** |
| ✅ integrator Waves | 🔵 sonnet | 20:07:11 | 20:07:23 | 0m12s | 0k | 1k | 41k | 202k | **245k** |
| ✅ verifier round 1 | 🟢 haiku | 20:07:23 | 20:07:44 | 0m20s | 0k | 3k | 116k | 73k | **192k** |
| ✅ reviewer round 1 | 🟣 opus | 20:07:45 | 20:09:23 | 1m38s | 0k | 17k | 182k | 1.19M | **1.39M** |
| ✅ scribe T0.16 | 🟢 haiku | 20:09:23 | 20:09:49 | 0m25s | 0k | 19k | 114k | 365k | **498k** |
| ✅ explainer T0.16 | 🔵 sonnet | 20:09:23 | 20:10:40 | 1m17s | 0k | 23k | 94k | 544k | **662k** |
| ✅ docs check T0.16 1 | 🟢 haiku | 20:10:40 | 20:10:44 | 0m03s | 0k | 0k | 37k | 35k | **73k** |
| ✅ scribe T0.16 (timings) | 🟢 haiku | 20:10:45 | 20:10:52 | 0m07s | 0k | 1k | 72k | 84k | **159k** |

### 3. ticket-run · 2026-11-27 20:15:56 to 20:17:18 · ⏱️ 1m21s

| Phase | Start | End | Elapsed | Steps |
| --- | --- | --- | --- | --- |
| Gate | 20:15:56 | 20:16:42 | 0m46s | 4 |
| Waves | | | not run | 0 |
| Verify | 20:16:42 | 20:16:58 | 0m16s | 1 |
| Review | | | not run | 0 |
| Finish | 20:16:59 | 20:17:18 | 0m18s | 3 |

Tokens of this run: 0k · 18k · 557k · 675k · **1.25M** (input · output · cache write · cache read · total)

| Step | Model | Start | End | Elapsed | Input | Output | Cache write | Cache read | Total |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ gate T0.16 | 🟢 haiku | 20:15:56 | 20:16:12 | 0m16s | 0k | 8k | 126k | 75k | **211k** |
| ✅ plan check T0.16 | 🟢 haiku | 20:16:12 | 20:16:18 | 0m05s | 0k | 0k | 73k | 73k | **147k** |
| ✅ start rule T0.16 | 🟢 haiku | 20:16:20 | 20:16:28 | 0m07s | 0k | 0k | 37k | 73k | **111k** |
| ✅ integrator prepare T0.16 | 🔵 sonnet | 20:16:28 | 20:16:42 | 0m13s | 0k | 0k | 36k | 82k | **119k** |
| ✅ verifier round 1 | 🟢 haiku | 20:16:42 | 20:16:58 | 0m16s | 0k | 2k | 107k | 120k | **230k** |
| ✅ scribe T0.16 | 🟢 haiku | 20:16:59 | 20:17:11 | 0m12s | 0k | 5k | 107k | 207k | **320k** |
| ✅ docs check T0.16 1 | 🟢 haiku | 20:17:11 | 20:17:15 | 0m03s | 0k | 0k | 35k | 37k | **73k** |
| 🔄 integrator finish T0.16 | 🔵 sonnet | 20:17:16 | 20:17:18 | 0m01s | 0k | 0k | 33k | 4k | **37k** |
<!-- /timings -->
