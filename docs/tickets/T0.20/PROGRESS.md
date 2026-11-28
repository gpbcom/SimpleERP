# T0.20: Typed API client package: progress

**Status:** 🟡 Planned

<!-- ticket:specs -->
## 📚 Specifications

The specification and design pages of [TICKET.md](TICKET.md), copied by `python3 .claude/scripts/tickets/ticket_refs.py sync`.

- [Back end](../../technical/architecture/backend.md)
- [📜 D406](../../specs/06-decisions/technical/d406-back-end.md)
- [📌 REQ-T05-03](../../specs/03-technical/t05-api-and-webhooks/requirements/req-t05-03-problem-json.md)
- [📜 D122](../../specs/06-decisions/ux/d122-error-message-standard.md)
- [📜 D438: Repository layout](../../specs/06-decisions/technical/d438-repository-layout.md)
- [📜 D407: Front end](../../specs/06-decisions/technical/d407-front-end.md)
- [📌 REQ-T05-01: REST with OpenAPI behind one gateway](../../specs/03-technical/t05-api-and-webhooks/requirements/req-t05-01-rest-openapi.md)
- [📌 REQ-T05-05: Contracts tested](../../specs/03-technical/t05-api-and-webhooks/requirements/req-t05-05-contract-tests.md)
- [🔌 I-T05-02: OpenAPI registry](../../specs/03-technical/t05-api-and-webhooks/interfaces/i-t05-02-openapi-registry.md)
- [🏗️ Front end](../../technical/architecture/frontend.md)
- [🏗️ API](../../technical/interfaces/api.md)
<!-- /ticket:specs -->

## 📝 Events

| Time | Event | By | Result |
| --- | --- | --- | --- |
| 2026-11-27 18:14 | Plan written: 12 tasks, 5 waves | ⏳ | Awaiting approval |
| 2026-11-27 18:29 | Plan approved by the person (group approval) | 👤 person | 🟢 Approved |
| 2026-11-28 01:27 | Wave 1: 5 of 5 tasks done | workers | ✅ |
| 2026-11-28 01:27 | Integrate (Waves) | integrator | ✅ 5 integrated, 0 blocked, not committed |
| 2026-11-28 01:27 | Wave 2: 2 of 2 tasks done | workers | ✅ |
| 2026-11-28 01:27 | Integrate (Waves) | integrator | ✅ 2 integrated, 0 blocked, not committed |
| 2026-11-28 01:27 | Wave 3: 2 blocking file(s) sent to their owners: frontend/packages/api-client/tests/helpers/problem-server.ts, frontend/packages/api-client/package.json | workers | 🔁 |
| 2026-11-28 01:27 | Integrate (Waves) | integrator | ✅ 2 integrated, 0 blocked, not committed |
| 2026-11-28 01:27 | Wave 3: 3 of 3 tasks done | workers | ✅ |
| 2026-11-28 01:27 | Integrate (Waves) | integrator | ✅ 3 integrated, 0 blocked, not committed |
| 2026-11-28 01:27 | Wave 4: 1 of 1 tasks done | workers | ✅ |
| 2026-11-28 01:27 | Integrate (Waves) | integrator | ✅ 1 integrated, 0 blocked, not committed |
| 2026-11-28 01:27 | Wave 5: 1 of 1 tasks done | workers | ✅ |
| 2026-11-28 01:27 | Integrate (Waves) | integrator | ✅ 1 integrated, 0 blocked, not committed |
| 2026-11-28 01:27 | Verify 1 (2 not applicable) | verifier | ✅ passed |
| 2026-11-28 01:27 | Review 1 (full) | reviewer | ✅ 0 blocking, 8 follow-ups |
| 2026-11-28 01:27 | Waiting for the person's code review: nothing is committed or pushed until PLAN.md says **Push:** 🟢 Approved (TKT-18) | scribe | 👀 |
| 2026-11-28 01:31 | Push approved after the code review | 👤 person | 🟢 |
| 2026-11-28 01:31 | Verify 1 (2 not applicable) | verifier | ✅ passed |

## 🔜 Follow-ups

| File | What to change |
| --- | --- |
| frontend/packages/api-client/src/problem/api-problem-error.ts frontend/packages/api-client/src/problem/to-api-error.ts frontend/packages/api-client/tests/problem/to-api-error.test.ts frontend/packages/api-client/tests/client/create-api-client.test.ts frontend/packages/api-client/README.md | The allow-list keeps only `code` and `status`. The `Problem` model (backend/shared/context/src/erp_context/models/refusals/problem.py:36-39) also has `reference`, "the small support reference" of D122, which is a code and never a secret. T0.23 criterion 1 must show "its support reference". Before or within T0.23, add `reference` to ApiProblemError, checked against Problem.CODE_PATTERN, and extend the leak tests to cover it. Owner: K09/K11 (or T0.23). |
| frontend/packages/api-client/README.md frontend/packages/api-client/src/problem/api-problem-error.ts frontend/packages/api-client/src/problem/to-api-error.ts docs/technical/interfaces/api.md | The README and the doc comments call `code` "the D122 support code". The Problem model calls `code` "the code of the error pattern" and `reference` "the small support reference" (D122). Call `code` "the code of the error pattern (D122)" so it is not confused with the support reference. Owner: K12/K09. |
| frontend/packages/api-client/src/problem/to-api-error.ts frontend/packages/api-client/tests/problem/to-api-error.test.ts | Any non-empty string is accepted as the code. A proxy or a misbehaving service could answer problem+json with free text in `code`, and that text would go into the error and its message. Accept only values that match the error-pattern code shape (Problem.CODE_PATTERN, `^[A-Z][A-Z0-9]*(-[A-Z0-9]+)*-[0-9]{2}$`), map anything else to ApiUnexpectedResponseError, and add a test case for it. Owner: K09. |
| docs/technical/interfaces/api.md | The page says the client is "generated from each service's committed OpenAPI document". Only `backend/services/platform/openapi.json` is generated today. Change it to say that, and that other services are added the same way later. Owner: K12. |
| docs/technical/delivery/ci-cd-and-stages.md | The new sentence at line 55 puts a line of about 400 characters inside a paragraph wrapped at 120. Re-wrap the paragraph. Owner: K10. |
| frontend/packages/api-client/src/client/create-api-client.ts | An error answer that is not problem+json leaves its body unread before the throw. Call `response.body?.cancel()` when the body is not read, so the connection is released at once. Owner: K11. |
| frontend/packages/api-client/tests/generate/renamed-field.test.ts | This test spawns `node` from PATH, while check-generated.test.ts uses `process.execPath`. Use `process.execPath` in both places so the tests run on the same Node as Vitest. Owner: K04. |
| frontend/packages/api-client/package.json | The package has no prettier config. Prettier defaults (double quotes, semicolons) format the generated file and some tests, while the hand-written sources use single quotes and no semicolons. Generator stability depends on the editor hook and generate.mjs resolving the same config. Pin one shared prettier config, for example from @simpleerp/config, so both always agree. Owner: K06. |

<!-- timings -->
## ⏱️ Timings

Measured from the agents' transcripts by `python3 .claude/scripts/reports/progress.py timings --ticket T0.20` (TKT-10).

| Measure | Value |
| --- | --- |
| 🕒 Ticket started | 2026-11-27 18:07:05 |
| 🕒 Last activity | 2026-11-28 01:31:21 |
| ⏱️ **Overall ticket time** (first start to last activity) | **7h24m15s** |
| 🤖 Time with agents working (sum of runs) | 24m14s |
| ⏸️ Time between runs (approvals, fixes) | 7h00m00s |
| 🔁 Workflow runs | 3 |
| 🪙 **Tokens consumed** (input, output, cache write, cache read) | **23.16M** |

#### 🪙 Tokens by model

| Model | Input | Output | Cache write | Cache read | Total |
| --- | --- | --- | --- | --- | --- |
| 🟢 haiku | 0k | 105k | 964k | 3.41M | **4.48M** |
| 🔵 sonnet | 0k | 183k | 1.43M | 10.99M | **12.61M** |
| 🟣 opus | 0k | 93k | 401k | 5.58M | **6.07M** |
| **All models** | 0k | 382k | 2.80M | 19.98M | **23.16M** |

### 1. ticket-plan · 2026-11-27 18:07:05 to 18:14:22 · ⏱️ 7m16s

| Phase | Start | End | Elapsed | Steps |
| --- | --- | --- | --- | --- |
| Ticket | 18:07:05 | 18:07:57 | 0m51s | 2 |
| Check | 18:07:57 | 18:08:01 | 0m03s | 1 |
| Plan | 18:08:02 | 18:13:17 | 5m15s | 1 |
| Write | 18:13:17 | 18:14:22 | 1m05s | 2 |

Tokens of this run: 0k · 145k · 646k · 5.64M · **6.43M** (input · output · cache write · cache read · total)

| Step | Model | Start | End | Elapsed | Input | Output | Cache write | Cache read | Total |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ done check T0.20 | 🟢 haiku | 18:07:05 | 18:07:12 | 0m06s | 0k | 0k | 37k | 73k | **112k** |
| ✅ ticket-writer T0.20 | 🔵 sonnet | 18:07:12 | 18:07:57 | 0m44s | 0k | 26k | 228k | 1.44M | **1.70M** |
| ✅ check TICKET.md T0.20 | 🟢 haiku | 18:07:57 | 18:08:01 | 0m03s | 0k | 0k | 35k | 38k | **73k** |
| ✅ planner T0.20 | 🟣 opus | 18:08:02 | 18:13:17 | 5m15s | 0k | 69k | 181k | 3.44M | **3.69M** |
| ✅ scribe T0.20 | 🟢 haiku | 18:13:17 | 18:14:18 | 1m00s | 0k | 47k | 125k | 568k | **742k** |
| ✅ check PLAN.md T0.20 | 🟢 haiku | 18:14:18 | 18:14:22 | 0m04s | 0k | 0k | 37k | 73k | **112k** |

### 2. ticket-run · 2026-11-28 01:14:15 to 01:29:00 · ⏱️ 14m44s

| Phase | Start | End | Elapsed | Steps |
| --- | --- | --- | --- | --- |
| Gate | 01:14:15 | 01:14:58 | 0m42s | 4 |
| Waves | 01:14:59 | 01:24:13 | 9m13s | 21 |
| Verify | 01:24:13 | 01:25:28 | 1m15s | 1 |
| Review | 01:25:28 | 01:27:31 | 2m02s | 1 |
| Finish | 01:27:31 | 01:29:00 | 1m28s | 4 |

Tokens of this run: 0k · 228k · 1.86M · 13.68M · **15.77M** (input · output · cache write · cache read · total)

| Step | Model | Start | End | Elapsed | Input | Output | Cache write | Cache read | Total |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ gate T0.20 | 🟢 haiku | 01:14:15 | 01:14:26 | 0m11s | 0k | 5k | 47k | 207k | **260k** |
| ✅ plan check T0.20 | 🟢 haiku | 01:14:27 | 01:14:30 | 0m03s | 0k | 0k | 36k | 39k | **76k** |
| ✅ start rule T0.20 | 🟢 haiku | 01:14:30 | 01:14:42 | 0m11s | 0k | 0k | 39k | 76k | **116k** |
| ✅ integrator prepare T0.20 | 🔵 sonnet | 01:14:42 | 01:14:58 | 0m15s | 0k | 0k | 37k | 85k | **122k** |
| ✅ K01 test-writer | 🔵 sonnet | 01:14:59 | 01:16:12 | 1m12s | 0k | 13k | 63k | 551k | **628k** |
| ✅ K02 test-writer | 🔵 sonnet | 01:15:01 | 01:15:53 | 0m52s | 0k | 11k | 58k | 721k | **792k** |
| ✅ K03 test-writer | 🔵 sonnet | 01:15:02 | 01:16:01 | 0m58s | 0k | 11k | 48k | 506k | **565k** |
| ✅ K04 test-writer | 🔵 sonnet | 01:15:03 | 01:16:05 | 1m01s | 0k | 12k | 47k | 500k | **559k** |
| ✅ K05 test-writer | 🔵 sonnet | 01:15:06 | 01:16:08 | 1m02s | 0k | 6k | 52k | 532k | **592k** |
| ✅ integrator Waves | 🔵 sonnet | 01:16:21 | 01:16:36 | 0m15s | 0k | 1k | 41k | 250k | **293k** |
| ✅ K06 frontend-implementer | 🔵 sonnet | 01:16:38 | 01:17:25 | 0m47s | 0k | 14k | 61k | 760k | **835k** |
| ✅ K07 implementer | 🔵 sonnet | 01:16:39 | 01:17:18 | 0m39s | 0k | 2k | 49k | 178k | **230k** |
| ✅ integrator Waves | 🔵 sonnet | 01:17:29 | 01:17:41 | 0m12s | 0k | 1k | 48k | 257k | **306k** |
| ❌ K08 frontend-implementer | 🔵 sonnet | 01:17:43 | 01:18:47 | 1m04s | 0k | 13k | 67k | 995k | **1.08M** |
| ✅ K09 frontend-implementer | 🔵 sonnet | 01:17:44 | 01:18:51 | 1m07s | 0k | 12k | 62k | 1.07M | **1.15M** |
| ✅ K10 doc-writer | 🟢 haiku | 01:17:45 | 01:18:28 | 0m42s | 0k | 4k | 54k | 406k | **465k** |
| ✅ K02 test-writer (fix) | 🔵 sonnet | 01:19:03 | 01:19:20 | 0m17s | 0k | 2k | 41k | 304k | **349k** |
| ✅ K06 frontend-implementer (fix) | 🔵 sonnet | 01:19:04 | 01:19:43 | 0m38s | 0k | 1k | 40k | 180k | **222k** |
| ✅ integrator Waves | 🔵 sonnet | 01:19:46 | 01:19:59 | 0m12s | 0k | 0k | 47k | 210k | **259k** |
| ✅ K08 frontend-implementer | 🔵 sonnet | 01:20:00 | 01:21:09 | 1m08s | 0k | 10k | 54k | 655k | **720k** |
| ✅ integrator Waves | 🔵 sonnet | 01:21:16 | 01:21:30 | 0m13s | 0k | 1k | 43k | 212k | **256k** |
| ✅ K11 frontend-implementer | 🔵 sonnet | 01:21:31 | 01:22:38 | 1m06s | 0k | 8k | 53k | 622k | **684k** |
| ✅ integrator Waves | 🔵 sonnet | 01:22:53 | 01:23:05 | 0m12s | 0k | 1k | 49k | 257k | **308k** |
| ✅ K12 doc-writer | 🟢 haiku | 01:23:07 | 01:23:54 | 0m47s | 0k | 10k | 56k | 581k | **648k** |
| ✅ integrator Waves | 🔵 sonnet | 01:24:03 | 01:24:13 | 0m10s | 0k | 1k | 48k | 256k | **305k** |
| ✅ verifier round 1 | 🟢 haiku | 01:24:13 | 01:25:28 | 1m15s | 0k | 0k | 41k | 119k | **161k** |
| ✅ reviewer round 1 | 🟣 opus | 01:25:28 | 01:27:31 | 2m02s | 0k | 24k | 220k | 2.14M | **2.38M** |
| ✅ scribe T0.20 | 🟢 haiku | 01:27:31 | 01:28:00 | 0m28s | 0k | 24k | 117k | 530k | **672k** |
| ✅ explainer T0.20 | 🔵 sonnet | 01:27:31 | 01:28:52 | 1m21s | 0k | 26k | 144k | 354k | **525k** |
| ✅ docs check T0.20 1 | 🟢 haiku | 01:28:53 | 01:28:56 | 0m03s | 0k | 0k | 39k | 36k | **76k** |
| ✅ scribe T0.20 (timings) | 🟢 haiku | 01:28:56 | 01:29:00 | 0m04s | 0k | 0k | 39k | 83k | **123k** |

### 3. ticket-run · 2026-11-28 01:29:08 to 01:31:21 · ⏱️ 2m12s

| Phase | Start | End | Elapsed | Steps |
| --- | --- | --- | --- | --- |
| Gate | 01:29:08 | 01:29:53 | 0m45s | 4 |
| Waves | | | not run | 0 |
| Verify | 01:29:53 | 01:31:07 | 1m13s | 1 |
| Review | | | not run | 0 |
| Finish | 01:31:07 | 01:31:21 | 0m13s | 3 |

Tokens of this run: 0k · 8k · 298k · 651k · **958k** (input · output · cache write · cache read · total)

| Step | Model | Start | End | Elapsed | Input | Output | Cache write | Cache read | Total |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ gate T0.20 | 🟢 haiku | 01:29:08 | 01:29:19 | 0m10s | 0k | 5k | 50k | 162k | **218k** |
| ✅ plan check T0.20 | 🟢 haiku | 01:29:19 | 01:29:22 | 0m02s | 0k | 0k | 36k | 39k | **76k** |
| ✅ start rule T0.20 | 🟢 haiku | 01:29:22 | 01:29:37 | 0m14s | 0k | 0k | 36k | 78k | **116k** |
| ✅ integrator prepare T0.20 | 🔵 sonnet | 01:29:39 | 01:29:53 | 0m13s | 0k | 0k | 42k | 81k | **124k** |
| ✅ verifier round 1 | 🟢 haiku | 01:29:53 | 01:31:07 | 1m13s | 0k | 0k | 39k | 80k | **119k** |
| ✅ scribe T0.20 | 🟢 haiku | 01:31:07 | 01:31:16 | 0m08s | 0k | 1k | 53k | 131k | **186k** |
| ✅ docs check T0.20 1 | 🟢 haiku | 01:31:16 | 01:31:20 | 0m04s | 0k | 0k | 39k | 76k | **116k** |
| 🔄 integrator finish T0.20 | 🔵 sonnet | 01:31:20 | 01:31:21 | 0m00s | 0k | 0k | 0k | 0k | **0k** |
<!-- /timings -->
