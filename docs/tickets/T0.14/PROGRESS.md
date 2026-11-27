# T0.14: Progress

**Status:** 🟡 Planned

<!-- ticket:specs -->
## 📚 Specifications

The specification and design pages of [TICKET.md](TICKET.md), copied by `python3 .claude/scripts/tickets/ticket_refs.py sync`.

- [Repository layout](../../technical/architecture/repository-layout.md#target-design-specified-in-gh-2-not-built-yet)
- [Back end](../../technical/architecture/backend.md#target-design-specified-in-gh-2-not-built-yet)
- [REQ-T05-03](../../specs/03-technical/t05-api-and-webhooks/requirements/req-t05-03-problem-json.md)
- [D122](../../specs/06-decisions/ux/d122-error-message-standard.md)
- [D419](../../specs/06-decisions/technical/d419-ci-cd-and-registry.md)
- [📌 REQ-T01-02: The company context at every layer](../../specs/03-technical/t01-companies-and-data-isolation/requirements/req-t01-02-company-context-everywhere.md)
- [📜 D406: Back end](../../specs/06-decisions/technical/d406-back-end.md)
- [📜 D438: Repository layout](../../specs/06-decisions/technical/d438-repository-layout.md)
- [Repository layout](../../technical/architecture/repository-layout.md)
- [Back end](../../technical/architecture/backend.md)
<!-- /ticket:specs -->

## 📝 Events

| Time | Event | By | Result |
| --- | --- | --- | --- |
| 2026-11-27 18:17 | Plan written: 19 tasks, 6 waves | ⏳ planner | ⏳ Awaiting approval |
| 2026-11-27 18:28 | Plan approved by the person (group approval) | 👤 person | 🟢 Approved |
| 2026-11-27 19:40 | Plan change: no cli module, regular FastAPI application (owner decision) | 👤 person | 🟢 Approved |
| 2026-11-27 23:29 | Wave 1: 8 of 8 tasks done | workers | ✅ |
| 2026-11-27 23:29 | Integrate (Waves) | integrator | ✅ 8 integrated, 0 blocked, not committed |
| 2026-11-27 23:29 | Wave 2: 3 of 3 tasks done | workers | ✅ |
| 2026-11-27 23:29 | Integrate (Waves) | integrator | ✅ 3 integrated, 0 blocked, not committed |
| 2026-11-27 23:29 | Wave 3: 4 of 4 tasks done | workers | ✅ |
| 2026-11-27 23:29 | Integrate (Waves) | integrator | ✅ 4 integrated, 0 blocked, not committed |
| 2026-11-27 23:29 | Wave 4: 2 of 2 tasks done | workers | ✅ |
| 2026-11-27 23:29 | Integrate (Waves) | integrator | ✅ 2 integrated, 0 blocked, not committed |
| 2026-11-27 23:29 | Wave 5: 1 of 1 tasks done | workers | ✅ |
| 2026-11-27 23:29 | Integrate (Waves) | integrator | ✅ 1 integrated, 0 blocked, not committed |
| 2026-11-27 23:29 | Wave 6: 2 blocking file(s) sent to their owners: backend/services/platform/src/erp_platform/api/http/app_builder.py, backend/services/platform/tests/api/test_app_factory.py | workers | 🔁 |
| 2026-11-27 23:29 | Integrate (Waves) | integrator | ✅ 1 integrated, 0 blocked, not committed |
| 2026-11-27 23:29 | Wave 6: 1 of 1 tasks done | workers | ✅ |
| 2026-11-27 23:29 | Integrate (Waves) | integrator | ✅ 1 integrated, 0 blocked, not committed |
| 2026-11-27 23:29 | Verify 1 | verifier | ❌ 2 failures |
| 2026-11-27 23:29 | Verify 2 (3 not applicable) | verifier | ❌ 2 failures |
| 2026-11-27 23:29 | Verify 3 (3 not applicable) | verifier | ❌ 2 failures |
| 2026-11-27 23:29 | Stopped: checks failing. Open failures: pytest backend/services/platform in backend/services/platform/tests/image/test_image.py (3 failed: test_a_call_without_a_company_is_refused_as_problem_json, test_the_health_call_answers_ok_after_the_start, test_the_container_is_still_running_after_the_calls; AssertionError at test_image.py:44, class-scoped fixture set as instance attribute); pytest backend/services/platform in uv.lock (the image build failed at COPY pyproject.toml uv.lock .python-version, the same 3 failures reported) | verifier | ❌ |
| 2026-11-27 23:29 | Work left uncommitted in /home/guillaume/Documents/Projects/Others/simple-erp on feature/tickets; /ticket-run T0.14 continues it | scribe | ⚠️ |
| 2026-11-27 23:33 | Plan change: new task K20 copies erp_context's refusal catalogue into the image (the service exited at startup on SERefusalCatalogUnreadable, so every image test timed out; the fix rounds went to the test and to uv.lock, which are right) | 👤 person (P0 standing order) | 🟢 Approved |
| 2026-11-27 23:34 | Wave 7: 1 of 1 tasks done | workers | ✅ |
| 2026-11-27 23:34 | Integrate (Waves) | integrator | ✅ 1 integrated, 0 blocked, not committed |
| 2026-11-27 23:34 | Verify 1 (3 not applicable) | verifier | ✅ passed |
| 2026-11-27 23:34 | Review 1 (full) | reviewer | ✅ 0 blocking, 9 follow-ups |
| 2026-11-27 23:34 | Waiting for the person's code review: nothing is committed or pushed until PLAN.md says **Push:** 🟢 Approved (TKT-18) | scribe | 👀 |
| 2026-11-27 23:37 | Push approved after the code review | 👤 person | 🟢 |
| 2026-11-27 23:37 | Verify 1 (3 not applicable) | verifier | ✅ passed |

## 🔜 Follow-ups

| File | What to change |
| --- | --- |
| backend/services/platform/src/erp_platform/service/problems/problem_service.py backend/services/platform/src/erp_platform/models/problems/problem_details.py backend/services/platform/tests/service/problems/test_problem_service.py backend/services/platform/tests/models/problems/test_problem_details.py | problem_service.py:64 builds ProblemDetails from title and why only. The catalogue's action and reference keys are dropped, but the context refusals of erp_context do return action and reference. Add action and reference to ProblemDetails, fill them from the catalogue entry, and test them. AC3 is still met, because the D122 code is in the body. Owner: the models and service tasks. |
| backend/services/platform/src/erp_platform/api/http/problem_handler.py backend/services/platform/tests/api/http/test_problem_handler.py | problem_handler.py:101 maps every HTTP status other than 404 and 405 (400, 401, 403, 409...) to PLATFORM-INTERNAL-01 while keeping the 4xx status. That mislabels a client error as an internal one. No route raises such an HTTPException yet. Add a generic client-error code, or one code per status, when the first route needs it. |
| backend/services/platform/src/erp_platform/api/http/problem_handler.py | The Notes at problem_handler.py:32 claim that no exception message reaches a log. Under uvicorn, Starlette's ServerErrorMiddleware re-raises the error after the 500 handler, so uvicorn.error logs the full traceback, message included. The ASGITransport test with raise_app_exceptions=False cannot see this. The body is clean, so AC4 holds. Either fix the claim or keep uvicorn from logging the message, with a test under real uvicorn. |
| backend/services/platform/src/erp_platform/api/http/app_builder.py backend/shared/context/pyproject.toml | app_builder.py:70 falls back to Path(erp_context.__file__).parents[2]/conf/catalogs, which exists only in the source tree. The image works only because of the extra Dockerfile COPY at line 24. Ship refusal_codes.yaml as package data of erp_context, or give it a config key, so that every next service does not have to repeat the COPY. |
| backend/services/platform/src/erp_platform/api/http/problem_handler.py | Notes line 34 says the erp_context refusals keep their own handler, registered by the application factory. No RefusalHandler is registered. Middleware refusals answer directly, and a RightsGuard refusal would reach the 500 handler. Register RefusalHandler when the first guarded route arrives, or correct the note. |
| backend/services/platform/src/erp_platform/models/config/platform_config.py | Lines 22 and 30 describe public_paths as paths served without a bearer token. They are the paths served without a company (the company-context middleware). Reword them. |
| backend/services/platform/tests/api/http/test_app_builder.py | Lines 14 to 19 define module-level constants. Move them into the TestAppBuilder class as ClassVars, as test_problem_handler.py does. |
| backend/services/platform/tests/image/test_image.py | The class-scoped container fixture at line 46 is an instance method, which triggers PytestRemovedIn10Warning. Make it a @classmethod fixture. |
| backend/services/platform/src/erp_platform/storage/catalogs/error_code_repository.py backend/services/platform/src/erp_platform/models/config/platform_config.py backend/services/platform/src/erp_platform/models/health/health_status.py backend/services/platform/src/erp_platform/models/problems/problem_details.py | The import-group comments do not match the imports. erp_models and erp_config sit under 'First-party imports', pydantic under 'Third-party imports' after them, and the erp_platform imports have no comment. Group them as Standard library, Third-party (pydantic, erp_* libraries), then First-party (erp_platform), as app_builder.py does. |

<!-- timings -->
## ⏱️ Timings

Measured from the agents' transcripts by `python3 .claude/scripts/reports/progress.py timings --ticket T0.14` (TKT-10).

| Measure | Value |
| --- | --- |
| 🕒 Ticket started | 2026-11-27 18:07:05 |
| 🕒 Last activity | 2026-11-27 23:38:12 |
| ⏱️ **Overall ticket time** (first start to last activity) | **5h31m06s** |
| 🤖 Time with agents working (sum of runs) | 1h08m34s |
| ⏸️ Time between runs (approvals, fixes) | 4h22m31s |
| 🔁 Workflow runs | 4 |
| 🪙 **Tokens consumed** (input, output, cache write, cache read) | **36.88M** |

#### 🪙 Tokens by model

| Model | Input | Output | Cache write | Cache read | Total |
| --- | --- | --- | --- | --- | --- |
| 🟢 haiku | 0k | 155k | 1.42M | 4.28M | **5.86M** |
| 🔵 sonnet | 0k | 315k | 2.44M | 21.83M | **24.59M** |
| 🟣 opus | 0k | 140k | 476k | 5.81M | **6.43M** |
| **All models** | 1k | 612k | 4.34M | 31.93M | **36.88M** |

### 1. ticket-plan · 2026-11-27 18:07:05 to 18:17:45 · ⏱️ 10m39s

| Phase | Start | End | Elapsed | Steps |
| --- | --- | --- | --- | --- |
| Ticket | 18:07:05 | 18:07:53 | 0m47s | 2 |
| Check | 18:07:53 | 18:07:56 | 0m03s | 1 |
| Plan | 18:07:57 | 18:16:18 | 8m21s | 1 |
| Write | 18:16:19 | 18:17:45 | 1m26s | 2 |

Tokens of this run: 0k · 225k · 820k · 6.11M · **7.15M** (input · output · cache write · cache read · total)

| Step | Model | Start | End | Elapsed | Input | Output | Cache write | Cache read | Total |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ done check T0.14 | 🟢 haiku | 18:07:05 | 18:07:12 | 0m06s | 0k | 0k | 37k | 73k | **112k** |
| ✅ ticket-writer T0.14 | 🔵 sonnet | 18:07:12 | 18:07:53 | 0m40s | 0k | 26k | 193k | 1.42M | **1.64M** |
| ✅ check TICKET.md T0.14 | 🟢 haiku | 18:07:53 | 18:07:56 | 0m03s | 0k | 0k | 35k | 38k | **73k** |
| ✅ planner T0.14 | 🟣 opus | 18:07:57 | 18:16:18 | 8m21s | 0k | 123k | 346k | 4.05M | **4.52M** |
| ✅ scribe T0.14 | 🟢 haiku | 18:16:19 | 18:17:41 | 1m22s | 0k | 74k | 171k | 492k | **738k** |
| ✅ check PLAN.md T0.14 | 🟢 haiku | 18:17:41 | 18:17:45 | 0m03s | 0k | 0k | 35k | 38k | **73k** |

### 2. ticket-run · 2026-11-27 22:39:32 to 23:29:21 · ⏱️ 49m48s

| Phase | Start | End | Elapsed | Steps |
| --- | --- | --- | --- | --- |
| Gate | 22:39:32 | 22:40:15 | 0m42s | 4 |
| Waves | 22:40:16 | 22:57:18 | 17m01s | 29 |
| Verify | 22:57:18 | 23:29:06 | 31m48s | 7 |
| Review | | | not run | 0 |
| Finish | 23:29:06 | 23:29:21 | 0m14s | 1 |

Tokens of this run: 0k · 294k · 2.46M · 21.27M · **24.03M** (input · output · cache write · cache read · total)

| Step | Model | Start | End | Elapsed | Input | Output | Cache write | Cache read | Total |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ gate T0.14 | 🟢 haiku | 22:39:32 | 22:39:47 | 0m15s | 0k | 7k | 49k | 167k | **223k** |
| ✅ plan check T0.14 | 🟢 haiku | 22:39:48 | 22:39:51 | 0m03s | 0k | 0k | 36k | 39k | **76k** |
| ✅ start rule T0.14 | 🟢 haiku | 22:39:51 | 22:40:01 | 0m09s | 0k | 0k | 36k | 39k | **76k** |
| ✅ integrator prepare T0.14 | 🔵 sonnet | 22:40:01 | 22:40:15 | 0m13s | 0k | 0k | 37k | 84k | **122k** |
| ✅ K01 test-writer | 🔵 sonnet | 22:40:16 | 22:42:20 | 2m04s | 0k | 45k | 99k | 1.41M | **1.55M** |
| ✅ K02 test-writer | 🔵 sonnet | 22:40:17 | 22:41:15 | 0m57s | 0k | 5k | 44k | 530k | **579k** |
| ✅ K03 test-writer | 🔵 sonnet | 22:40:19 | 22:41:41 | 1m22s | 0k | 19k | 88k | 859k | **967k** |
| ✅ K04 test-writer | 🔵 sonnet | 22:40:20 | 22:41:17 | 0m56s | 0k | 4k | 47k | 548k | **600k** |
| ✅ K05 test-writer | 🔵 sonnet | 22:40:22 | 22:41:22 | 0m59s | 0k | 10k | 60k | 731k | **802k** |
| ✅ K06 test-writer | 🔵 sonnet | 22:40:25 | 22:41:40 | 1m15s | 0k | 17k | 84k | 1.10M | **1.20M** |
| ✅ K07 test-writer | 🔵 sonnet | 22:40:27 | 22:41:28 | 1m01s | 0k | 12k | 76k | 967k | **1.06M** |
| ✅ K08 test-writer | 🔵 sonnet | 22:40:29 | 22:41:19 | 0m50s | 0k | 11k | 48k | 691k | **750k** |
| ✅ integrator Waves | 🔵 sonnet | 22:42:26 | 22:42:44 | 0m17s | 0k | 1k | 41k | 250k | **293k** |
| ✅ K09 implementer | 🔵 sonnet | 22:42:46 | 22:43:13 | 0m27s | 0k | 3k | 47k | 276k | **327k** |
| ✅ K10 implementer | 🔵 sonnet | 22:42:47 | 22:44:47 | 1m59s | 0k | 38k | 101k | 1.72M | **1.86M** |
| ✅ K11 implementer | 🔵 sonnet | 22:42:48 | 22:43:50 | 1m01s | 0k | 8k | 58k | 737k | **804k** |
| ✅ integrator Waves | 🔵 sonnet | 22:44:52 | 22:45:09 | 0m17s | 0k | 1k | 43k | 341k | **386k** |
| ✅ K12 implementer | 🔵 sonnet | 22:45:11 | 22:45:33 | 0m22s | 0k | 1k | 43k | 225k | **270k** |
| ✅ K13 implementer | 🔵 sonnet | 22:45:12 | 22:45:55 | 0m43s | 0k | 3k | 52k | 327k | **384k** |
| ✅ K14 implementer | 🔵 sonnet | 22:45:13 | 22:45:58 | 0m45s | 0k | 4k | 44k | 270k | **318k** |
| ✅ K15 doc-writer | 🟢 haiku | 22:45:16 | 22:45:53 | 0m37s | 0k | 12k | 66k | 663k | **742k** |
| ✅ integrator Waves | 🔵 sonnet | 22:46:06 | 22:46:19 | 0m12s | 0k | 0k | 44k | 170k | **215k** |
| ✅ K16 implementer | 🔵 sonnet | 22:46:20 | 22:47:02 | 0m41s | 0k | 3k | 41k | 266k | **311k** |
| ✅ K17 implementer | 🔵 sonnet | 22:46:22 | 22:47:01 | 0m39s | 0k | 6k | 50k | 426k | **483k** |
| ✅ integrator Waves | 🔵 sonnet | 22:47:09 | 22:47:21 | 0m11s | 0k | 0k | 41k | 167k | **210k** |
| ✅ K18 implementer | 🔵 sonnet | 22:47:22 | 22:48:53 | 1m30s | 0k | 14k | 89k | 1.29M | **1.39M** |
| ✅ integrator Waves | 🔵 sonnet | 22:49:02 | 22:49:12 | 0m10s | 0k | 0k | 42k | 168k | **211k** |
| ❌ K19 implementer | 🔵 sonnet | 22:49:14 | 22:55:26 | 6m12s | 0k | 13k | 70k | 1.86M | **1.95M** |
| ❌ K18 implementer (fix) | 🔵 sonnet | 22:55:30 | 22:55:51 | 0m21s | 0k | 2k | 46k | 221k | **270k** |
| ✅ K07 test-writer (fix) | 🔵 sonnet | 22:55:31 | 22:56:02 | 0m30s | 0k | 1k | 41k | 215k | **258k** |
| ✅ integrator Waves | 🔵 sonnet | 22:56:09 | 22:56:19 | 0m10s | 0k | 0k | 87k | 121k | **210k** |
| ✅ K19 implementer | 🔵 sonnet | 22:56:20 | 22:57:05 | 0m45s | 0k | 3k | 50k | 461k | **515k** |
| ✅ integrator Waves | 🔵 sonnet | 22:57:08 | 22:57:18 | 0m09s | 0k | 0k | 42k | 167k | **210k** |
| ✅ verifier round 1 | 🟢 haiku | 22:57:18 | 23:08:42 | 11m24s | 0k | 5k | 177k | 199k | **382k** |
| ❌ K08 test-writer (fix) | 🔵 sonnet | 23:08:44 | 23:11:37 | 2m53s | 0k | 4k | 96k | 516k | **617k** |
| ❌ FIX-uv.lock implementer (fix) | 🔵 sonnet | 23:08:45 | 23:11:58 | 3m12s | 0k | 4k | 56k | 793k | **853k** |
| ✅ verifier round 2 | 🟢 haiku | 23:11:59 | 23:15:10 | 3m11s | 0k | 3k | 11k | 411k | **426k** |
| ❌ K08 test-writer (fix) | 🔵 sonnet | 23:15:12 | 23:15:48 | 0m36s | 0k | 3k | 54k | 409k | **467k** |
| ❌ FIX-uv.lock implementer (fix) | 🔵 sonnet | 23:15:13 | 23:19:22 | 4m09s | 0k | 5k | 58k | 963k | **1.03M** |
| ✅ verifier round 3 | 🟢 haiku | 23:19:23 | 23:29:06 | 9m43s | 0k | 4k | 94k | 152k | **251k** |
| ✅ scribe T0.14 | 🟢 haiku | 23:29:06 | 23:29:21 | 0m14s | 0k | 4k | 53k | 308k | **365k** |

### 3. ticket-run · 2026-11-27 23:29:54 to 23:35:56 · ⏱️ 6m02s

| Phase | Start | End | Elapsed | Steps |
| --- | --- | --- | --- | --- |
| Gate | 23:29:54 | 23:30:39 | 0m44s | 4 |
| Waves | 23:30:40 | 23:31:37 | 0m56s | 2 |
| Verify | 23:31:37 | 23:32:39 | 1m02s | 1 |
| Review | 23:32:40 | 23:34:41 | 2m00s | 1 |
| Finish | 23:34:41 | 23:35:56 | 1m15s | 4 |

Tokens of this run: 0k · 78k · 783k · 3.75M · **4.61M** (input · output · cache write · cache read · total)

| Step | Model | Start | End | Elapsed | Input | Output | Cache write | Cache read | Total |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ gate T0.14 | 🟢 haiku | 23:29:54 | 23:30:08 | 0m13s | 0k | 8k | 94k | 78k | **181k** |
| ✅ plan check T0.14 | 🟢 haiku | 23:30:08 | 23:30:11 | 0m03s | 0k | 0k | 39k | 36k | **76k** |
| ✅ start rule T0.14 | 🟢 haiku | 23:30:11 | 23:30:23 | 0m11s | 0k | 0k | 36k | 78k | **115k** |
| ✅ integrator prepare T0.14 | 🔵 sonnet | 23:30:25 | 23:30:39 | 0m13s | 0k | 0k | 43k | 82k | **126k** |
| ✅ K20 implementer | 🔵 sonnet | 23:30:40 | 23:31:21 | 0m41s | 0k | 1k | 48k | 169k | **219k** |
| ✅ integrator Waves | 🔵 sonnet | 23:31:28 | 23:31:37 | 0m09s | 0k | 0k | 42k | 168k | **211k** |
| ✅ verifier round 1 | 🟢 haiku | 23:31:37 | 23:32:39 | 1m02s | 0k | 0k | 5k | 114k | **119k** |
| ✅ reviewer round 1 | 🟣 opus | 23:32:40 | 23:34:41 | 2m00s | 0k | 17k | 129k | 1.76M | **1.91M** |
| ✅ scribe T0.14 | 🟢 haiku | 23:34:41 | 23:35:12 | 0m31s | 0k | 18k | 128k | 474k | **621k** |
| ✅ explainer T0.14 | 🔵 sonnet | 23:34:41 | 23:35:48 | 1m07s | 0k | 29k | 132k | 626k | **788k** |
| ✅ docs check T0.14 1 | 🟢 haiku | 23:35:48 | 23:35:52 | 0m03s | 0k | 0k | 41k | 73k | **115k** |
| ✅ scribe T0.14 (timings) | 🟢 haiku | 23:35:52 | 23:35:56 | 0m04s | 0k | 0k | 39k | 83k | **123k** |

### 4. ticket-run · 2026-11-27 23:36:08 to 23:38:12 · ⏱️ 2m04s

| Phase | Start | End | Elapsed | Steps |
| --- | --- | --- | --- | --- |
| Gate | 23:36:08 | 23:36:53 | 0m45s | 4 |
| Waves | | | not run | 0 |
| Verify | 23:36:53 | 23:37:57 | 1m03s | 1 |
| Review | | | not run | 0 |
| Finish | 23:37:57 | 23:38:12 | 0m14s | 3 |

Tokens of this run: 0k · 13k · 273k · 802k · **1.09M** (input · output · cache write · cache read · total)

| Step | Model | Start | End | Elapsed | Input | Output | Cache write | Cache read | Total |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ gate T0.14 | 🟢 haiku | 23:36:08 | 23:36:23 | 0m15s | 0k | 9k | 59k | 201k | **270k** |
| ✅ plan check T0.14 | 🟢 haiku | 23:36:24 | 23:36:27 | 0m03s | 0k | 0k | 39k | 76k | **115k** |
| ✅ start rule T0.14 | 🟢 haiku | 23:36:28 | 23:36:39 | 0m11s | 0k | 0k | 36k | 39k | **76k** |
| ✅ integrator prepare T0.14 | 🔵 sonnet | 23:36:39 | 23:36:53 | 0m13s | 0k | 0k | 43k | 82k | **126k** |
| ✅ verifier round 1 | 🟢 haiku | 23:36:53 | 23:37:57 | 1m03s | 0k | 0k | 5k | 114k | **119k** |
| ✅ scribe T0.14 | 🟢 haiku | 23:37:57 | 23:38:05 | 0m07s | 0k | 2k | 89k | 172k | **264k** |
| ✅ docs check T0.14 1 | 🟢 haiku | 23:38:05 | 23:38:09 | 0m04s | 0k | 0k | 0k | 115k | **116k** |
| 🔄 integrator finish T0.14 | 🔵 sonnet | 23:38:12 | 23:38:12 | 0m00s | 0k | 0k | 0k | 0k | **0k** |
<!-- /timings -->
