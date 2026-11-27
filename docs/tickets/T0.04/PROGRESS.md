# T0.04: SE exceptions and error codes: progress

**Status:** 🟡 Planned

<!-- ticket:specs -->
## 📚 Specifications

The specification and design pages of [TICKET.md](TICKET.md), copied by `python3 .claude/scripts/tickets/ticket_refs.py sync`.

- [🏗️ Back end](../../technical/architecture/backend.md)
- [📜 D122 Error message standard](../../specs/06-decisions/ux/d122-error-message-standard.md)
- [📌 REQ-T05-03 problem+json errors](../../specs/03-technical/t05-api-and-webhooks/requirements/req-t05-03-problem-json.md)
- [📜 D406 Back end](../../specs/06-decisions/technical/d406-back-end.md)
- [📜 D438 Repository layout](../../specs/06-decisions/technical/d438-repository-layout.md)
- [🏗️ Repository layout](../../technical/architecture/repository-layout.md)
- [🏗️ Configuration](../../technical/architecture/configuration.md)
- [🏗️ API](../../technical/interfaces/api.md)
- [REQ-T10-01](../../specs/03-technical/t10-translations-and-notifications/requirements/req-t10-01-translation-catalogues.md)
<!-- /ticket:specs -->

## 📝 Events

| Time | Event | By | Result |
| --- | --- | --- | --- |
| 2026-11-27 18:13 | Plan written: 10 tasks, 5 waves | scribe | ⏳ Awaiting approval |
| 2026-11-27 18:27 | Plan approved by the person (group approval) | 👤 person | 🟢 Approved |
| 2026-11-27 21:19 | Wave 1: 5 of 5 tasks done | workers | ✅ |
| 2026-11-27 21:19 | Integrate (Waves) | integrator | ✅ 5 integrated, 0 blocked, not committed |
| 2026-11-27 21:19 | Wave 2: 2 of 2 tasks done | workers | ✅ |
| 2026-11-27 21:19 | Integrate (Waves) | integrator | ✅ 2 integrated, 0 blocked, not committed |
| 2026-11-27 21:19 | Wave 3: 1 of 1 tasks done | workers | ✅ |
| 2026-11-27 21:19 | Integrate (Waves) | integrator | ✅ 1 integrated, 0 blocked, not committed |
| 2026-11-27 21:19 | Wave 4: 1 of 1 tasks done | workers | ✅ |
| 2026-11-27 21:19 | Integrate (Waves) | integrator | ✅ 1 integrated, 1 blocked, not committed |
| 2026-11-27 21:19 | Wave 5: 1 of 1 tasks done | workers | ✅ |
| 2026-11-27 21:19 | Integrate (Waves) | integrator | ✅ 1 integrated, 0 blocked, not committed |
| 2026-11-27 21:19 | Verify 1 | verifier | ✅ passed |
| 2026-11-27 21:19 | Review 1 (full) | reviewer | ✅ 0 blocking, 7 follow-ups |
| 2026-11-27 21:19 | Waiting for the person's code review: nothing is committed or pushed until PLAN.md says **Push:** 🟢 Approved (TKT-18) | scribe | 👀 |
| 2026-11-27 21:22 | Push approved after the code review | 👤 person | 🟢 |
| 2026-11-27 21:22 | Verify 1 (3 not applicable) | verifier | ✅ passed |

## 🔜 Follow-ups

| File | What to change |
| --- | --- |
| `backend/models/README.md`, `backend/models/src/erp_models/base/exceptions/se_invalid_opaque_id_exception.py`, `backend/models/src/erp_models/ids/exceptions/se_invalid_company_id_exception.py`, `backend/models/src/erp_models/ids/exceptions/se_invalid_record_id_exception.py`, `backend/models/src/erp_models/money/exceptions/se_invalid_money_exception.py`, `backend/models/src/erp_models/paging/exceptions/se_invalid_cursor_page_exception.py`, `backend/models/src/erp_models/times/exceptions/se_invalid_utc_timestamp_exception.py`, `backend/models/src/erp_models/idempotency/exceptions/se_invalid_idempotency_key_exception.py`, `backend/models/src/erp_models/catalogs/exceptions/se_invalid_yaml_catalog_exception.py` | In a later ticket, rebase the existing T0.03 model bases on SEInvalidModelException so they inherit a CODE the T0.14 problem+json handler can resolve. Add a convention rule that every SE exception derives from SEException. Until then, change the README sentence to say that new exceptions derive from the bases. |
| `tests/conventions/exceptions/exception_scanner.py`, `tests/conventions/exceptions/test_exception_scanner.py` | Add the built-in exception names (for example every name in builtins that subclasses BaseException) to the roots, and add a broken-tree case for a non-SE class based on ValueError. |
| `backend/models/tests/errors/catalogs/test_error_codes_data.py` | Add a data test that checks entry.reference == code for every code, and that each message key starts with errors.<code in snake case>. This keeps the catalogue consistent as later tickets add codes. |
| `backend/models/README.md` | Drop the clause, or say only that the reference is the support code shown as 'ref. SITE-CLOSE-01' by the D122 pattern. |
| `backend/models/src/erp_models/errors/catalogs/error_catalog.py`, `backend/models/src/erp_models/errors/entries/error_code_entry.py` | Have ErrorCatalog reuse ErrorCodeEntry.REFERENCE_PATTERN, or keep both in one catalogue constant. Consider a read-only mapping for codes, so callers cannot add entries at run time. |
| `backend/models/tests/errors/entries/test_error_code_entry.py` | Rename it test_none_is_refused_because_no_field_has_a_default, as test_error_catalog.py already does. |
| `backend/models/README.md` | Record in the README, or in the T0.14 ticket, how a service image finds the catalogue (copied into its conf/ or packaged as data). |

<!-- timings -->
## ⏱️ Timings

Measured from the agents' transcripts by `python3 .claude/scripts/reports/progress.py timings --ticket T0.04` (TKT-10).

| Measure | Value |
| --- | --- |
| 🕒 Ticket started | 2026-11-27 18:07:05 |
| 🕒 Last activity | 2026-11-27 21:22:57 |
| ⏱️ **Overall ticket time** (first start to last activity) | **3h15m51s** |
| 🤖 Time with agents working (sum of runs) | 22m52s |
| ⏸️ Time between runs (approvals, fixes) | 2h52m59s |
| 🔁 Workflow runs | 3 |
| 🪙 **Tokens consumed** (input, output, cache write, cache read) | **19.14M** |

#### 🪙 Tokens by model

| Model | Input | Output | Cache write | Cache read | Total |
| --- | --- | --- | --- | --- | --- |
| 🟢 haiku | 0k | 107k | 914k | 3.45M | **4.47M** |
| 🔵 sonnet | 0k | 184k | 1.12M | 9.66M | **10.96M** |
| 🟣 opus | 0k | 94k | 387k | 3.23M | **3.72M** |
| **All models** | 0k | 385k | 2.42M | 16.34M | **19.14M** |

### 1. ticket-plan · 2026-11-27 18:07:05 to 18:14:18 · ⏱️ 7m12s

| Phase | Start | End | Elapsed | Steps |
| --- | --- | --- | --- | --- |
| Ticket | 18:07:05 | 18:07:53 | 0m47s | 2 |
| Check | 18:07:53 | 18:08:10 | 0m16s | 3 |
| Plan | 18:08:10 | 18:13:15 | 5m04s | 1 |
| Write | 18:13:15 | 18:14:18 | 1m02s | 2 |

Tokens of this run: 0k · 145k · 691k · 4.34M · **5.17M** (input · output · cache write · cache read · total)

| Step | Model | Start | End | Elapsed | Input | Output | Cache write | Cache read | Total |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ done check T0.04 | 🟢 haiku | 18:07:05 | 18:07:11 | 0m05s | 0k | 0k | 35k | 38k | **73k** |
| ✅ ticket-writer T0.04 | 🔵 sonnet | 18:07:11 | 18:07:53 | 0m41s | 0k | 22k | 202k | 1.32M | **1.54M** |
| ✅ check TICKET.md T0.04 | 🟢 haiku | 18:07:53 | 18:07:57 | 0m04s | 0k | 0k | 38k | 73k | **112k** |
| ✅ ticket-writer fix T0.04 | 🔵 sonnet | 18:07:57 | 18:08:05 | 0m07s | 0k | 1k | 47k | 162k | **211k** |
| ✅ check TICKET.md T0.04 | 🟢 haiku | 18:08:06 | 18:08:10 | 0m04s | 0k | 0k | 4k | 106k | **112k** |
| ✅ planner T0.04 | 🟣 opus | 18:08:10 | 18:13:15 | 5m04s | 0k | 71k | 191k | 2.14M | **2.40M** |
| ✅ scribe T0.04 | 🟢 haiku | 18:13:15 | 18:14:13 | 0m58s | 0k | 47k | 136k | 417k | **601k** |
| ✅ check PLAN.md T0.04 | 🟢 haiku | 18:14:14 | 18:14:18 | 0m04s | 0k | 0k | 35k | 76k | **112k** |

### 2. ticket-run · 2026-11-27 21:07:07 to 21:21:05 · ⏱️ 13m58s

| Phase | Start | End | Elapsed | Steps |
| --- | --- | --- | --- | --- |
| Gate | 21:07:07 | 21:07:48 | 0m41s | 4 |
| Waves | 21:07:49 | 21:16:48 | 8m58s | 15 |
| Verify | 21:16:48 | 21:17:49 | 1m00s | 1 |
| Review | 21:17:49 | 21:19:46 | 1m56s | 1 |
| Finish | 21:19:46 | 21:21:05 | 1m19s | 4 |

Tokens of this run: 0k · 231k · 1.46M · 11.27M · **12.95M** (input · output · cache write · cache read · total)

| Step | Model | Start | End | Elapsed | Input | Output | Cache write | Cache read | Total |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ gate T0.04 | 🟢 haiku | 21:07:07 | 21:07:21 | 0m13s | 0k | 3k | 45k | 237k | **287k** |
| ✅ plan check T0.04 | 🟢 haiku | 21:07:21 | 21:07:24 | 0m03s | 0k | 0k | 34k | 37k | **71k** |
| ✅ start rule T0.04 | 🟢 haiku | 21:07:25 | 21:07:33 | 0m08s | 0k | 0k | 36k | 71k | **109k** |
| ✅ integrator prepare T0.04 | 🔵 sonnet | 21:07:33 | 21:07:48 | 0m14s | 0k | 0k | 34k | 80k | **115k** |
| ✅ K01 test-writer | 🔵 sonnet | 21:07:49 | 21:09:41 | 1m51s | 0k | 17k | 60k | 580k | **658k** |
| ✅ K02 test-writer | 🔵 sonnet | 21:07:51 | 21:09:28 | 1m37s | 0k | 13k | 52k | 554k | **619k** |
| ✅ K03 test-writer | 🔵 sonnet | 21:07:53 | 21:09:00 | 1m07s | 0k | 10k | 58k | 607k | **675k** |
| ✅ K04 test-writer | 🔵 sonnet | 21:07:55 | 21:08:48 | 0m52s | 0k | 6k | 49k | 444k | **501k** |
| ✅ K05 test-writer | 🔵 sonnet | 21:07:58 | 21:10:24 | 2m26s | 0k | 25k | 68k | 898k | **992k** |
| ✅ integrator Waves | 🔵 sonnet | 21:10:36 | 21:10:58 | 0m21s | 0k | 1k | 40k | 398k | **440k** |
| ✅ K06 implementer | 🔵 sonnet | 21:11:01 | 21:11:48 | 0m47s | 0k | 9k | 49k | 654k | **713k** |
| ✅ K10 doc-writer | 🟢 haiku | 21:11:03 | 21:11:57 | 0m53s | 0k | 22k | 91k | 1.17M | **1.28M** |
| ✅ integrator Waves | 🔵 sonnet | 21:12:00 | 21:12:16 | 0m16s | 0k | 1k | 40k | 282k | **323k** |
| ✅ K07 implementer | 🔵 sonnet | 21:12:18 | 21:13:48 | 1m29s | 0k | 12k | 55k | 764k | **832k** |
| ✅ integrator Waves | 🔵 sonnet | 21:13:49 | 21:14:02 | 0m13s | 0k | 1k | 43k | 326k | **371k** |
| ✅ K08 implementer | 🔵 sonnet | 21:14:04 | 21:15:41 | 1m36s | 0k | 32k | 65k | 1.17M | **1.27M** |
| ✅ integrator Waves | 🔵 sonnet | 21:15:57 | 21:16:13 | 0m16s | 0k | 1k | 43k | 378k | **424k** |
| ✅ K09 implementer | 🔵 sonnet | 21:16:15 | 21:16:34 | 0m18s | 0k | 1k | 37k | 211k | **251k** |
| ✅ integrator Waves | 🔵 sonnet | 21:16:36 | 21:16:48 | 0m12s | 0k | 1k | 42k | 290k | **334k** |
| ✅ verifier round 1 | 🟢 haiku | 21:16:48 | 21:17:49 | 1m00s | 0k | 0k | 39k | 112k | **152k** |
| ✅ reviewer round 1 | 🟣 opus | 21:17:49 | 21:19:46 | 1m56s | 0k | 22k | 195k | 1.09M | **1.31M** |
| ✅ scribe T0.04 | 🟢 haiku | 21:19:46 | 21:20:18 | 0m31s | 0k | 21k | 109k | 372k | **503k** |
| ✅ explainer T0.04 | 🔵 sonnet | 21:19:46 | 21:20:58 | 1m11s | 0k | 22k | 86k | 449k | **558k** |
| ✅ docs check T0.04 1 | 🟢 haiku | 21:20:58 | 21:21:01 | 0m03s | 0k | 0k | 37k | 34k | **72k** |
| ✅ scribe T0.04 (timings) | 🟢 haiku | 21:21:01 | 21:21:05 | 0m03s | 0k | 0k | 35k | 41k | **77k** |

### 3. ticket-run · 2026-11-27 21:21:16 to 21:22:57 · ⏱️ 1m41s

| Phase | Start | End | Elapsed | Steps |
| --- | --- | --- | --- | --- |
| Gate | 21:21:16 | 21:21:52 | 0m36s | 4 |
| Waves | | | not run | 0 |
| Verify | 21:21:52 | 21:22:43 | 0m51s | 1 |
| Review | | | not run | 0 |
| Finish | 21:22:44 | 21:22:57 | 0m12s | 3 |

Tokens of this run: 0k · 9k · 271k · 738k · **1.02M** (input · output · cache write · cache read · total)

| Step | Model | Start | End | Elapsed | Input | Output | Cache write | Cache read | Total |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ gate T0.04 | 🟢 haiku | 21:21:16 | 21:21:28 | 0m11s | 0k | 5k | 51k | 191k | **248k** |
| ✅ plan check T0.04 | 🟢 haiku | 21:21:28 | 21:21:31 | 0m02s | 0k | 0k | 34k | 37k | **72k** |
| ✅ start rule T0.04 | 🟢 haiku | 21:21:31 | 21:21:39 | 0m07s | 0k | 0k | 37k | 72k | **109k** |
| ✅ integrator prepare T0.04 | 🔵 sonnet | 21:21:39 | 21:21:52 | 0m12s | 0k | 0k | 36k | 81k | **118k** |
| ✅ verifier round 1 | 🟢 haiku | 21:21:52 | 21:22:43 | 0m51s | 0k | 0k | 35k | 116k | **152k** |
| ✅ scribe T0.04 | 🟢 haiku | 21:22:44 | 21:22:52 | 0m08s | 0k | 1k | 41k | 201k | **243k** |
| ✅ docs check T0.04 1 | 🟢 haiku | 21:22:53 | 21:22:56 | 0m03s | 0k | 0k | 34k | 37k | **72k** |
| 🔄 integrator finish T0.04 | 🔵 sonnet | 21:22:57 | 21:22:57 | 0m00s | 0k | 0k | 0k | 0k | **0k** |
<!-- /timings -->
