# T0.13: Test helpers library, progress

**Status:** 🟡 Planned

<!-- ticket:specs -->
## 📚 Specifications

The specification and design pages of [TICKET.md](TICKET.md), copied by `python3 .claude/scripts/tickets/ticket_refs.py sync`.

- [Back end, shared code](../../technical/architecture/backend.md#target-design-specified-in-gh-2-not-built-yet)
- [Tests and traceability](../../technical/delivery/tests-and-traceability.md#target-design-specified-in-gh-2-not-built-yet)
- [📜 D426 Testing strategy](../../specs/06-decisions/technical/d426-testing-strategy.md)
- [📜 D438 Repository layout](../../specs/06-decisions/technical/d438-repository-layout.md)
- [🏗️ Tests and traceability](../../technical/delivery/tests-and-traceability.md)
- [🏗️ Back end](../../technical/architecture/backend.md)
- [🏗️ Repository layout](../../technical/architecture/repository-layout.md)
<!-- /ticket:specs -->

## 📝 Events

| Time | Event | By | Result |
| --- | --- | --- | --- |
| 2026-11-27 18:19 | Plan written: 19 tasks, 5 waves, awaiting approval | planner | ⏳ |
| 2026-11-27 18:28 | Plan approved by the person (group approval) | 👤 person | 🟢 Approved |
| 2026-11-27 23:44 | Wave 1: 7 of 8 tasks done | workers | ❌ |
| 2026-11-27 23:44 | Integrate (Waves) | integrator | ✅ 7 integrated, 0 blocked, not committed |
| 2026-11-27 23:44 | Stopped in wave 1: K05 not done | workflow | ❌ |
| 2026-11-27 23:47 | Plan change: new task K20 (test and .gitignore, wave 1) keeps a logs package of src/ or tests/ tracked; K05 is retried once K20 is integrated (its hand-off was empty twice: .gitignore line 36 `logs/` hid backend/shared/testing/tests/logs/) | 👤 person (P0 standing order) | 🟢 Approved |
| 2026-11-28 00:08 | Wave 1: 2 of 2 tasks done | workers | ✅ |
| 2026-11-28 00:08 | Integrate (Waves) | integrator | ✅ 2 integrated, 1 blocked, not committed |
| 2026-11-28 00:08 | Wave 2: 1 of 1 tasks done | workers | ✅ |
| 2026-11-28 00:08 | Integrate (Waves) | integrator | ✅ 1 integrated, 1 blocked, not committed |
| 2026-11-28 00:08 | Wave 3: 5 of 5 tasks done | workers | ✅ |
| 2026-11-28 00:08 | Integrate (Waves) | integrator | ✅ 5 integrated, 1 blocked, not committed |
| 2026-11-28 00:08 | Wave 4: 4 blocking file(s) sent to their owners: backend/shared/testing/tests/synthetic/test_company_builder.py, backend/shared/testing/tests/synthetic/test_user_builder.py, backend/shared/testing/src/erp_testing/models/synthetic/__init__.py, backend/shared/testing/tests/context/test_synthetic_company_context.py | workers | 🔁 |
| 2026-11-28 00:08 | Integrate (Waves) | integrator | ✅ 3 integrated, 0 blocked, not committed |
| 2026-11-28 00:08 | Wave 4: 4 of 4 tasks done | workers | ✅ |
| 2026-11-28 00:08 | Integrate (Waves) | integrator | ✅ 4 integrated, 0 blocked, not committed |
| 2026-11-28 00:08 | Wave 5: 1 blocking file(s) sent to their owners: backend/shared/testing/tests/plugin/test_testing_plugin.py | workers | 🔁 |
| 2026-11-28 00:08 | Integrate (Waves) | integrator | ✅ 1 integrated, 0 blocked, not committed |
| 2026-11-28 00:08 | Wave 5: 0 of 1 tasks done | workers | ❌ |
| 2026-11-28 00:08 | Stopped in wave 5: K19 not done | workflow | ❌ |
| 2026-11-28 00:12 | Plan change: new task K21 fixes line 15 of tests/plugin/test_testing_plugin.py (SyntheticCatalog imported from a package that does not re-export it); K19 now depends on K21 (it was blocked by that import twice, its plugin is done) | 👤 person (P0 standing order) | 🟢 Approved |
| 2026-11-28 00:17 | K21: blocked only by files later waves write, counted as done | workers | ✅ |
| 2026-11-28 00:17 | Wave 2: 1 of 1 tasks done | workers | ✅ |
| 2026-11-28 00:17 | Integrate (Waves) | integrator | ✅ 1 integrated, 0 blocked, not committed |
| 2026-11-28 00:17 | Wave 5: 1 of 1 tasks done | workers | ✅ |
| 2026-11-28 00:17 | Integrate (Waves) | integrator | ✅ 1 integrated, 0 blocked, not committed |
| 2026-11-28 00:17 | Verify 1 (3 not applicable) | verifier | ✅ passed |
| 2026-11-28 00:17 | Review 1 (full) | reviewer | ⚠️ 1 blocking, 8 follow-ups |
| 2026-11-28 00:17 | Integrate (Review) | integrator | ✅ 1 integrated, 0 blocked, not committed |
| 2026-11-28 00:17 | Review 2 (confirm fixes) | reviewer | ✅ 0 blocking, 1 follow-ups |
| 2026-11-28 00:17 | Waiting for the person's code review: nothing is committed or pushed until PLAN.md says **Push:** 🟢 Approved (TKT-18) | workflow | 👀 |
| 2026-11-28 00:23 | Push approved after the code review | 👤 person | 🟢 |
| 2026-11-28 00:23 | Verify 1 (3 not applicable) | verifier | ❌ 1 failures |
| 2026-11-28 00:23 | Stopped: checks failing. Open failures: [{"check":"pytest","file":"tests","detail":"FAILED tests/ci/release/test_automerge.py::TestAutomerge::test_a_hotfix_takes_the_version_at_the_start_of_its_name; FAILED tests/ci/release/test_automerge.py::TestAutomerge::test_a_hotfix_without_a_version_is_left_to_a_person; FAILED tests/ci/release_notes/test_release_notes.py::TestReleaseNotes::test_the_changelog_lists_each_commit_of_each_pull_request_by_kind; FAILED tests/ci/release_notes/test_release_notes.py::TestReleaseNotes::test_a_new_release_goes_on_top_of_the_previous_ones; FAILED tests/ci/release_notes/test_release_notes.py::TestReleaseNotes::test_the_unreleased_section_stays_on_top; FAILED tests/ci/release_notes/test_release_notes.py::TestReleaseNotes::test_the_release_notes_name_the_tickets_delivered_and_what_they_deliver; FAILED tests/ci/release_notes/test_release_notes.py::TestReleaseNotes::test_the_test_report_sums_every_suite_of_ci; FAILED tests/ci/release_notes/test_release_notes.py::TestReleaseNotes::test_a_failed_test_shows_in_the_report; FAILED tests/ci/release_notes/test_release_notes.py::TestReleaseNotes::test_no_release_without_its_test_reports; FAILED tests/ci/release_notes/test_release_notes.py::TestReleaseNotes::test_the_first_release_starts_after_master; FAILED tests/ci/release_notes/test_release_notes.py::TestReleaseNotes::test_a_gh_ticket_commit_is_filed_under_the_tickets; 15 failed, 1292 passed, 3 skipped in 41.16s","environment":false}] | workflow | ❌ |
| 2026-11-28 00:23 | Work left uncommitted in /home/guillaume/Documents/Projects/Others/simple-erp on feature/tickets; `/ticket-run T0.13` continues it | workflow | ⚠️ |
| 2026-11-28 00:26 | Push approved after the code review | 👤 person | 🟢 |
| 2026-11-28 00:26 | Verify 1 (3 not applicable) | verifier | ✅ passed |

## 🔜 Follow-ups

| File | What to change |
| --- | --- |
| backend/shared/testing/src/erp_testing/context/synthetic_company_context.py backend/shared/testing/tests/context/test_synthetic_company_context.py | `SyntheticCompanyContext.__init__` accepts a user whose `company_id` is not the company's id. Refusing that pair with an `SE` error, logged at ERROR, would make the mismatch above impossible by construction. Add a test for the refusal. Owners: K18 and K04. |
| backend/shared/testing/src/erp_testing/plugin/testing_plugin.py | The session-scoped fixtures `postgres_server` and `synthetic_catalog` are instance methods, and pytest emits PytestRemovedIn10Warning for both (see tests-evidences/pytest-backend-shared-testing.txt). Pytest 10 removes this, which would break every consumer. Plan a move to `@classmethod` fixtures with a class-level logger, or a module-free alternative, before pytest 10. Owner: K19. |
| backend/shared/testing/src/erp_testing/stand_in/stand_in_server.py backend/shared/testing/src/erp_testing/postgres/postgres_test_server.py backend/shared/testing/src/erp_testing/context/synthetic_company_context.py | The import group comments are wrong or inconsistent. stand_in_server.py:8-13 puts `# First-party imports` over erp_lifecycle, then `# Third-party imports` over pydantic, then erp_testing with no comment. postgres_test_server.py:14 labels erp_lifecycle as first-party. synthetic_company_context.py labels erp_context as third-party. Use one convention: workspace libraries other than erp_testing are third-party, and erp_testing is first-party. Owners: K15, K16 and K18. |
| backend/shared/testing/src/erp_testing/models/synthetic/synthetic_company.py backend/shared/testing/src/erp_testing/models/synthetic/synthetic_user.py | The validators annotate `JsonValue | CompanyId` and `JsonValue | RecordId` (synthetic_company.py:41, synthetic_user.py:40 and :60). Use `Union[JsonValue, CompanyId]`. Owner: K12. |
| backend/shared/testing/src/erp_testing/stand_in/stand_in_handler.py | Line 40 raises a bare `TypeError` with no ERROR log before it. Building `StandInRequest` at line 92 can raise a validation error on a malformed request path, which would end the handler thread with no answer. Use an SE server error with a log, and answer 400 to an invalid request. Owner: K15. |
| backend/shared/testing/src/erp_testing/models/synthetic/synthetic_catalog.py | `DEFAULT_PATH` is `Path(__file__).parents[4]/conf/catalogs/synthetic.yaml`. That path exists only in an editable workspace install: a built wheel of erp-testing does not ship `conf/`. Ship the catalogue as package data, or document that the library is used editable only. Owner: K12. |
| docs/technical/delivery/tests-and-traceability.md backend/shared/testing/tests/plugin/conftest.py | The documentation registers the plugin under the name `"erp_testing"`, while the conftest and the plugin docstring use `"erp-testing"`. Pick one name. Owners: K14 and K08. |
| .github/workflows/python.yml | The 4 skipped tests in the evidence are the real PostgreSQL ones, so the per-session server was never started in the verifier's environment. Confirm that CI runners have the PostgreSQL binaries (GitHub's Ubuntu images do, under /usr/lib/postgresql), or install them, so the session server is exercised at least in CI. This is outside this ticket's area. |

<!-- timings -->
## ⏱️ Timings

Measured from the agents' transcripts by `python3 .claude/scripts/reports/progress.py timings --ticket T0.13` (TKT-10).

| Measure | Value |
| --- | --- |
| 🕒 Ticket started | 2026-11-27 18:07:05 |
| 🕒 Last activity | 2026-11-28 00:27:08 |
| ⏱️ **Overall ticket time** (first start to last activity) | **6h20m02s** |
| 🤖 Time with agents working (sum of runs) | 56m39s |
| ⏸️ Time between runs (approvals, fixes) | 5h23m22s |
| 🔁 Workflow runs | 6 |
| 🪙 **Tokens consumed** (input, output, cache write, cache read) | **52.54M** |

#### 🪙 Tokens by model

| Model | Input | Output | Cache write | Cache read | Total |
| --- | --- | --- | --- | --- | --- |
| 🟢 haiku | 0k | 211k | 1.74M | 5.96M | **7.91M** |
| 🔵 sonnet | 1k | 738k | 3.22M | 32.74M | **36.69M** |
| 🟣 opus | 0k | 177k | 543k | 7.22M | **7.94M** |
| **All models** | 1k | 1.13M | 5.50M | 45.91M | **52.54M** |

### 1. ticket-plan · 2026-11-27 18:07:05 to 18:19:51 · ⏱️ 12m45s

| Phase | Start | End | Elapsed | Steps |
| --- | --- | --- | --- | --- |
| Ticket | 18:07:05 | 18:07:52 | 0m46s | 2 |
| Check | 18:07:52 | 18:07:56 | 0m03s | 1 |
| Plan | 18:07:56 | 18:17:43 | 9m46s | 1 |
| Write | 18:17:44 | 18:19:51 | 2m07s | 2 |

Tokens of this run: 0k · 238k · 700k · 6.78M · **7.72M** (input · output · cache write · cache read · total)

| Step | Model | Start | End | Elapsed | Input | Output | Cache write | Cache read | Total |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ done check T0.13 | 🟢 haiku | 18:07:05 | 18:07:12 | 0m06s | 0k | 0k | 37k | 73k | **112k** |
| ✅ ticket-writer T0.13 | 🔵 sonnet | 18:07:12 | 18:07:52 | 0m39s | 0k | 20k | 180k | 1.23M | **1.43M** |
| ✅ check TICKET.md T0.13 | 🟢 haiku | 18:07:52 | 18:07:56 | 0m03s | 0k | 0k | 35k | 38k | **73k** |
| ✅ planner T0.13 | 🟣 opus | 18:07:56 | 18:17:43 | 9m46s | 0k | 147k | 207k | 4.07M | **4.42M** |
| ✅ scribe T0.13 | 🟢 haiku | 18:17:44 | 18:19:45 | 2m01s | 0k | 70k | 204k | 1.33M | **1.61M** |
| ✅ check PLAN.md T0.13 | 🟢 haiku | 18:19:46 | 18:19:51 | 0m05s | 0k | 0k | 35k | 38k | **73k** |

### 2. ticket-run · 2026-11-27 23:39:20 to 23:44:57 · ⏱️ 5m36s

| Phase | Start | End | Elapsed | Steps |
| --- | --- | --- | --- | --- |
| Gate | 23:39:20 | 23:40:13 | 0m53s | 4 |
| Waves | 23:40:18 | 23:44:57 | 4m38s | 11 |
| Verify | | | not run | 0 |
| Review | | | not run | 0 |
| Finish | | | not run | 0 |

Tokens of this run: 0k · 272k · 922k · 8.26M · **9.45M** (input · output · cache write · cache read · total)

| Step | Model | Start | End | Elapsed | Input | Output | Cache write | Cache read | Total |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ gate T0.13 | 🟢 haiku | 23:39:20 | 23:39:45 | 0m25s | 0k | 15k | 57k | 206k | **279k** |
| ✅ plan check T0.13 | 🟢 haiku | 23:39:45 | 23:39:48 | 0m02s | 0k | 0k | 36k | 39k | **76k** |
| ✅ start rule T0.13 | 🟢 haiku | 23:39:49 | 23:39:58 | 0m09s | 0k | 0k | 36k | 39k | **76k** |
| ✅ integrator prepare T0.13 | 🔵 sonnet | 23:39:58 | 23:40:13 | 0m15s | 0k | 0k | 37k | 84k | **122k** |
| ✅ K01 test-writer | 🔵 sonnet | 23:40:18 | 23:41:42 | 1m23s | 0k | 35k | 82k | 779k | **897k** |
| ✅ K02 test-writer | 🔵 sonnet | 23:40:21 | 23:41:49 | 1m27s | 0k | 21k | 67k | 823k | **912k** |
| ✅ K03 test-writer | 🔵 sonnet | 23:40:28 | 23:42:27 | 1m59s | 0k | 65k | 78k | 1.19M | **1.33M** |
| ✅ K04 test-writer | 🔵 sonnet | 23:40:34 | 23:41:22 | 0m47s | 0k | 7k | 55k | 480k | **542k** |
| ❌ K05 test-writer | 🔵 sonnet | 23:40:38 | 23:42:00 | 1m22s | 0k | 15k | 56k | 791k | **862k** |
| ✅ K06 test-writer | 🔵 sonnet | 23:40:43 | 23:43:05 | 2m21s | 0k | 61k | 114k | 975k | **1.15M** |
| ✅ K07 test-writer | 🔵 sonnet | 23:40:46 | 23:41:50 | 1m03s | 0k | 18k | 58k | 512k | **588k** |
| ✅ K08 test-writer | 🔵 sonnet | 23:40:49 | 23:42:12 | 1m22s | 0k | 14k | 89k | 1.21M | **1.31M** |
| ❌ K05 test-writer | 🔵 sonnet | 23:43:16 | 23:44:20 | 1m03s | 0k | 13k | 46k | 658k | **719k** |
| ✅ integrator Waves | 🔵 sonnet | 23:44:24 | 23:44:47 | 0m23s | 0k | 1k | 46k | 211k | **258k** |
| ✅ scribe T0.13 | 🟢 haiku | 23:44:48 | 23:44:57 | 0m08s | 0k | 2k | 60k | 254k | **318k** |

### 3. ticket-run · 2026-11-27 23:46:44 to 00:08:09 · ⏱️ 21m24s

| Phase | Start | End | Elapsed | Steps |
| --- | --- | --- | --- | --- |
| Gate | 23:46:44 | 23:47:48 | 1m03s | 4 |
| Waves | 23:47:49 | 00:08:09 | 20m19s | 28 |
| Verify | | | not run | 0 |
| Review | | | not run | 0 |
| Finish | | | not run | 0 |

Tokens of this run: 0k · 460k · 2.00M · 22.49M · **24.94M** (input · output · cache write · cache read · total)

| Step | Model | Start | End | Elapsed | Input | Output | Cache write | Cache read | Total |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ gate T0.13 | 🟢 haiku | 23:46:44 | 23:47:11 | 0m26s | 0k | 16k | 65k | 205k | **288k** |
| ✅ plan check T0.13 | 🟢 haiku | 23:47:11 | 23:47:14 | 0m02s | 0k | 0k | 39k | 37k | **77k** |
| ✅ start rule T0.13 | 🟢 haiku | 23:47:14 | 23:47:30 | 0m15s | 0k | 0k | 37k | 79k | **117k** |
| ✅ integrator prepare T0.13 | 🔵 sonnet | 23:47:33 | 23:47:48 | 0m14s | 0k | 0k | 38k | 86k | **125k** |
| ❌ K05 test-writer | 🔵 sonnet | 23:47:49 | 23:49:09 | 1m19s | 0k | 11k | 55k | 757k | **824k** |
| ✅ K20 test-writer | 🔵 sonnet | 23:47:51 | 23:48:18 | 0m27s | 0k | 3k | 43k | 405k | **452k** |
| ✅ K05 test-writer | 🔵 sonnet | 23:49:11 | 23:50:22 | 1m10s | 0k | 14k | 59k | 642k | **715k** |
| ✅ integrator Waves | 🔵 sonnet | 23:50:23 | 23:50:35 | 0m11s | 0k | 1k | 42k | 212k | **256k** |
| ✅ K09 implementer | 🔵 sonnet | 23:50:36 | 23:51:37 | 1m01s | 0k | 5k | 47k | 420k | **474k** |
| ✅ integrator Waves | 🔵 sonnet | 23:51:40 | 23:51:53 | 0m13s | 0k | 1k | 44k | 261k | **306k** |
| ✅ K10 implementer | 🔵 sonnet | 23:51:56 | 23:53:58 | 2m01s | 0k | 44k | 109k | 1.77M | **1.92M** |
| ✅ K11 implementer | 🔵 sonnet | 23:51:59 | 23:53:48 | 1m49s | 0k | 27k | 86k | 1.37M | **1.49M** |
| ✅ K12 implementer | 🔵 sonnet | 23:52:02 | 23:55:22 | 3m20s | 0k | 82k | 168k | 4.17M | **4.42M** |
| ✅ K13 implementer | 🔵 sonnet | 23:52:03 | 23:53:15 | 1m11s | 0k | 6k | 49k | 273k | **328k** |
| ✅ K14 doc-writer | 🟢 haiku | 23:52:05 | 23:53:03 | 0m57s | 0k | 10k | 56k | 400k | **467k** |
| ✅ integrator Waves | 🔵 sonnet | 23:55:23 | 23:55:42 | 0m18s | 0k | 1k | 46k | 270k | **318k** |
| ✅ K15 implementer | 🔵 sonnet | 23:55:44 | 23:58:38 | 2m54s | 0k | 81k | 109k | 2.69M | **2.88M** |
| ✅ K16 implementer | 🔵 sonnet | 23:55:45 | 23:58:16 | 2m31s | 0k | 63k | 113k | 1.36M | **1.53M** |
| ❌ K17 implementer | 🔵 sonnet | 23:55:47 | 23:56:54 | 1m07s | 0k | 11k | 62k | 727k | **801k** |
| ❌ K18 implementer | 🔵 sonnet | 23:55:50 | 23:57:14 | 1m24s | 0k | 7k | 58k | 705k | **771k** |
| ✅ K07 test-writer (fix) | 🔵 sonnet | 23:58:47 | 23:59:00 | 0m12s | 0k | 0k | 41k | 87k | **129k** |
| ✅ K12 implementer (fix) | 🔵 sonnet | 23:58:48 | 23:59:42 | 0m53s | 0k | 1k | 45k | 316k | **364k** |
| ✅ K04 test-writer (fix) | 🔵 sonnet | 23:58:50 | 23:59:14 | 0m23s | 0k | 2k | 45k | 313k | **361k** |
| ✅ integrator Waves | 🔵 sonnet | 23:59:55 | 00:00:10 | 0m14s | 0k | 1k | 47k | 268k | **317k** |
| ✅ K17 implementer | 🔵 sonnet | 00:00:11 | 00:01:42 | 1m30s | 0k | 11k | 76k | 592k | **681k** |
| ✅ K18 implementer | 🔵 sonnet | 00:00:13 | 00:01:11 | 0m57s | 0k | 11k | 67k | 862k | **941k** |
| ✅ integrator Waves | 🔵 sonnet | 00:01:43 | 00:02:05 | 0m21s | 0k | 1k | 48k | 414k | **464k** |
| ❌ K19 implementer | 🔵 sonnet | 00:02:07 | 00:03:20 | 1m13s | 0k | 10k | 64k | 771k | **846k** |
| ✅ K08 test-writer (fix) | 🔵 sonnet | 00:03:25 | 00:04:02 | 0m36s | 0k | 1k | 40k | 131k | **174k** |
| ✅ integrator Waves | 🔵 sonnet | 00:04:11 | 00:04:24 | 0m12s | 0k | 1k | 54k | 365k | **421k** |
| ❌ K19 implementer | 🔵 sonnet | 00:04:27 | 00:05:43 | 1m15s | 0k | 14k | 78k | 870k | **963k** |
| ✅ scribe T0.13 | 🟢 haiku | 00:05:45 | 00:08:09 | 2m24s | 0k | 10k | 53k | 640k | **704k** |

### 4. ticket-run · 2026-11-28 00:08:51 to 00:20:32 · ⏱️ 11m41s

| Phase | Start | End | Elapsed | Steps |
| --- | --- | --- | --- | --- |
| Gate | 00:08:51 | 00:09:47 | 0m56s | 4 |
| Waves | 00:09:49 | 00:11:39 | 1m49s | 4 |
| Verify | 00:11:39 | 00:12:52 | 1m12s | 1 |
| Review | 00:12:52 | 00:17:38 | 4m45s | 5 |
| Finish | 00:17:38 | 00:20:32 | 2m54s | 4 |

Tokens of this run: 0k · 110k · 1.22M · 7.02M · **8.35M** (input · output · cache write · cache read · total)

| Step | Model | Start | End | Elapsed | Input | Output | Cache write | Cache read | Total |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ gate T0.13 | 🟢 haiku | 00:08:51 | 00:09:17 | 0m26s | 0k | 15k | 64k | 167k | **247k** |
| ✅ plan check T0.13 | 🟢 haiku | 00:09:17 | 00:09:22 | 0m04s | 0k | 0k | 36k | 78k | **115k** |
| ✅ start rule T0.13 | 🟢 haiku | 00:09:23 | 00:09:33 | 0m09s | 0k | 0k | 36k | 39k | **76k** |
| ✅ integrator prepare T0.13 | 🔵 sonnet | 00:09:33 | 00:09:47 | 0m13s | 0k | 0k | 42k | 89k | **132k** |
| ❌ K21 implementer | 🔵 sonnet | 00:09:49 | 00:10:10 | 0m20s | 0k | 2k | 41k | 265k | **309k** |
| ✅ integrator Waves | 🔵 sonnet | 00:10:13 | 00:10:23 | 0m10s | 0k | 0k | 50k | 212k | **264k** |
| ✅ K19 implementer | 🔵 sonnet | 00:10:25 | 00:11:25 | 0m59s | 0k | 9k | 66k | 520k | **596k** |
| ✅ integrator Waves | 🔵 sonnet | 00:11:28 | 00:11:39 | 0m10s | 0k | 0k | 48k | 174k | **224k** |
| ✅ verifier round 1 | 🟢 haiku | 00:11:39 | 00:12:52 | 1m12s | 0k | 0k | 37k | 122k | **161k** |
| ✅ reviewer round 1 | 🟣 opus | 00:12:52 | 00:15:13 | 2m20s | 0k | 25k | 255k | 2.77M | **3.05M** |
| ✅ FIX-K19+K08+K21 implementer (fix) | 🔵 sonnet | 00:15:15 | 00:15:39 | 0m23s | 0k | 1k | 46k | 224k | **272k** |
| ✅ integrator Review | 🔵 sonnet | 00:15:44 | 00:15:55 | 0m11s | 0k | 0k | 59k | 216k | **277k** |
| ✅ verifier after review 1 | 🟢 haiku | 00:15:55 | 00:17:08 | 1m12s | 0k | 0k | 37k | 122k | **161k** |
| ✅ reviewer round 2 | 🟣 opus | 00:17:09 | 00:17:38 | 0m29s | 0k | 4k | 80k | 381k | **465k** |
| ✅ scribe T0.13 | 🟢 haiku | 00:17:38 | 00:20:22 | 2m43s | 0k | 21k | 119k | 732k | **874k** |
| ✅ explainer T0.13 | 🔵 sonnet | 00:17:38 | 00:18:54 | 1m15s | 0k | 23k | 120k | 782k | **925k** |
| ✅ docs check T0.13 1 | 🟢 haiku | 00:20:24 | 00:20:27 | 0m03s | 0k | 0k | 36k | 39k | **76k** |
| ✅ scribe T0.13 (timings) | 🟢 haiku | 00:20:28 | 00:20:32 | 0m04s | 0k | 0k | 39k | 83k | **123k** |

### 5. ticket-run · 2026-11-28 00:20:47 to 00:23:15 · ⏱️ 2m28s

| Phase | Start | End | Elapsed | Steps |
| --- | --- | --- | --- | --- |
| Gate | 00:20:47 | 00:21:46 | 0m59s | 4 |
| Waves | | | not run | 0 |
| Verify | 00:21:47 | 00:23:02 | 1m15s | 1 |
| Review | | | not run | 0 |
| Finish | 00:23:02 | 00:23:15 | 0m12s | 1 |

Tokens of this run: 0k · 24k · 298k · 724k · **1.05M** (input · output · cache write · cache read · total)

| Step | Model | Start | End | Elapsed | Input | Output | Cache write | Cache read | Total |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ gate T0.13 | 🟢 haiku | 00:20:47 | 00:21:12 | 0m25s | 0k | 15k | 65k | 178k | **258k** |
| ✅ plan check T0.13 | 🟢 haiku | 00:21:13 | 00:21:17 | 0m04s | 0k | 0k | 37k | 78k | **116k** |
| ✅ start rule T0.13 | 🟢 haiku | 00:21:20 | 00:21:32 | 0m12s | 0k | 0k | 39k | 76k | **116k** |
| ✅ integrator prepare T0.13 | 🔵 sonnet | 00:21:32 | 00:21:46 | 0m14s | 0k | 0k | 42k | 90k | **132k** |
| ✅ verifier round 1 | 🟢 haiku | 00:21:47 | 00:23:02 | 1m15s | 0k | 2k | 39k | 122k | **164k** |
| ✅ scribe T0.13 | 🟢 haiku | 00:23:02 | 00:23:15 | 0m12s | 0k | 5k | 75k | 178k | **260k** |

### 6. ticket-run · 2026-11-28 00:24:24 to 00:27:08 · ⏱️ 2m43s

| Phase | Start | End | Elapsed | Steps |
| --- | --- | --- | --- | --- |
| Gate | 00:24:24 | 00:25:24 | 0m59s | 4 |
| Waves | | | not run | 0 |
| Verify | 00:25:24 | 00:26:37 | 1m12s | 1 |
| Review | | | not run | 0 |
| Finish | 00:26:37 | 00:27:08 | 0m30s | 3 |

Tokens of this run: 0k · 19k · 354k · 640k · **1.01M** (input · output · cache write · cache read · total)

| Step | Model | Start | End | Elapsed | Input | Output | Cache write | Cache read | Total |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ gate T0.13 | 🟢 haiku | 00:24:24 | 00:24:50 | 0m26s | 0k | 15k | 99k | 172k | **288k** |
| ✅ plan check T0.13 | 🟢 haiku | 00:24:51 | 00:24:54 | 0m03s | 0k | 0k | 36k | 39k | **76k** |
| ✅ start rule T0.13 | 🟢 haiku | 00:24:55 | 00:25:08 | 0m13s | 0k | 0k | 37k | 78k | **116k** |
| ✅ integrator prepare T0.13 | 🔵 sonnet | 00:25:11 | 00:25:24 | 0m13s | 0k | 0k | 42k | 90k | **133k** |
| ✅ verifier round 1 | 🟢 haiku | 00:25:24 | 00:26:37 | 1m12s | 0k | 0k | 37k | 82k | **120k** |
| ✅ scribe T0.13 | 🟢 haiku | 00:26:37 | 00:26:44 | 0m07s | 0k | 1k | 64k | 137k | **203k** |
| ✅ docs check T0.13 1 | 🟢 haiku | 00:27:03 | 00:27:07 | 0m03s | 0k | 0k | 36k | 39k | **76k** |
| 🔄 integrator finish T0.13 | 🔵 sonnet | 00:27:07 | 00:27:08 | 0m00s | 0k | 0k | 0k | 0k | **0k** |
<!-- /timings -->
