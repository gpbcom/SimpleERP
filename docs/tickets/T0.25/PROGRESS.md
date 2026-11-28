# T0.25: Progress

**Status:** 🟡 Planned

<!-- ticket:specs -->
## 📚 Specifications

The specification and design pages of [TICKET.md](TICKET.md), copied by `python3 .claude/scripts/tickets/ticket_refs.py sync`.

- [REQ-T09-03](../../specs/03-technical/t09-install-backups-and-updates/requirements/req-t09-03-laptop-profile.md)
- [Performance and capacity](../../technical/infrastructure/performance-and-capacity.md)
- [REQ-T08-01](../../specs/03-technical/t08-rag-platform/requirements/req-t08-01-milvus-collections.md)
- [D22](../../specs/06-decisions/foundations/d22-no-graphics-card-needed.md)
- [📜 D408: Performance targets and resource profiles](../../specs/06-decisions/technical/d408-performance-and-profiles.md)
- [📌 REQ-T09-02: Compose and Helm everywhere](../../specs/03-technical/t09-install-backups-and-updates/requirements/req-t09-02-compose-and-helm.md)
- [📦 Installation](../../specs/05-non-functional/installation.md)
<!-- /ticket:specs -->

## 📝 Events

| Time | Event | By | Result |
| --- | --- | --- | --- |
| 2026-11-27 18:14 | Plan written: 10 tasks, 4 waves | scribe | ⏳ Awaiting approval |
| 2026-11-27 18:29 | Plan approved by the person (group approval) | 👤 person | 🟢 Approved |
| 2026-11-28 01:04 | Wave 1: 5 of 5 tasks done | workers | ✅ |
| 2026-11-28 01:04 | Integrate (Waves) | integrator | ✅ 5 integrated, 0 blocked, not committed |
| 2026-11-28 01:04 | Wave 2: 1 of 1 tasks done | workers | ✅ |
| 2026-11-28 01:04 | Integrate (Waves) | integrator | ✅ 1 integrated, 0 blocked, not committed |
| 2026-11-28 01:04 | Wave 3: 1 blocking file(s) sent to their owners: infra/compose/compose.laptop.yaml | workers | 🔁 |
| 2026-11-28 01:04 | Integrate (Waves) | integrator | ✅ 1 integrated, 0 blocked, not committed |
| 2026-11-28 01:04 | Wave 3: 2 of 2 tasks done | workers | ✅ |
| 2026-11-28 01:04 | Integrate (Waves) | integrator | ✅ 2 integrated, 0 blocked, not committed |
| 2026-11-28 01:04 | Wave 4: 1 of 2 tasks done | workers | ❌ |
| 2026-11-28 01:04 | Integrate (Waves) | integrator | ✅ 1 integrated, 0 blocked, not committed |
| 2026-11-28 01:04 | Stopped in wave 4: K10 not done | workflow | ❌ |
| 2026-11-28 01:08 | Plan change: new tasks K11 (tests), K12 (settings), K13 (measure) and K14 (installer) start the laptop profile as compose.yaml plus the compose.laptop.yaml overlay, not the overlay alone, which Compose refused; K10 now depends on K13 and may build the two images locally for the measure, removing them afterwards (TKT-27) | 👤 person (P0 standing order) | 🟢 Approved |
| 2026-11-28 01:15 | Wave 2: 1 of 1 tasks done | workers | ✅ |
| 2026-11-28 01:15 | Integrate (Waves) | integrator | ✅ 1 integrated, 0 blocked, not committed |
| 2026-11-28 01:15 | Wave 3: 1 of 1 tasks done | workers | ✅ |
| 2026-11-28 01:15 | Integrate (Waves) | integrator | ✅ 1 integrated, 0 blocked, not committed |
| 2026-11-28 01:15 | Wave 4: 2 of 2 tasks done | workers | ✅ |
| 2026-11-28 01:15 | Integrate (Waves) | integrator | ✅ 2 integrated, 0 blocked, not committed |
| 2026-11-28 01:15 | Wave 5: 1 of 1 tasks done | workers | ✅ |
| 2026-11-28 01:15 | Integrate (Waves) | integrator | ✅ 1 integrated, 0 blocked, not committed |
| 2026-11-28 01:15 | Verify 1 (3 not applicable) | verifier | ✅ passed |
| 2026-11-28 01:15 | Review 1 (full) | reviewer | ✅ 0 blocking, 4 follow-ups |
| 2026-11-28 01:15 | Waiting for the person's code review: nothing is committed or pushed until PLAN.md says **Push:** 🟢 Approved (TKT-18) | scribe | 👀 |
| 2026-11-28 01:17 | Push approved after the code review | 👤 person | 🟢 |
| 2026-11-28 01:17 | Verify 1 (3 not applicable) | verifier | ✅ passed |

## 🔜 Follow-ups

| File | What to change |
| --- | --- |
| `infra/compose/README.md` | Under 'Installing the laptop profile', say that install.sh still needs ERP_IMAGE_TAG (and optionally ERP_IMAGE_PREFIX) and the secrets/postgres_password file of the one-server section. Without them, compose.yaml refuses to start and install.sh only reports 'The laptop profile did not start.' Also update the stale line in the 'Laptop' section, 'The memory budget of D408 is measured later, by ticket T0.25', to point at the measure now in performance-and-capacity.md. Owner: K-task of the README (doc-writer). |
| `infra/compose/measure-memory.sh`, `infra/compose/README.md` | The script runs under the same Compose project name (simpleerp) as an installed laptop profile, and its EXIT trap runs 'docker compose down'. Run on a machine where the profile is installed, it stops that install. Either refuse when the project is already running or use a separate project name (-p simpleerp-measure), and document it. Also guard against an empty ids array: 'docker stats' with no id would measure every container on the host. Owner: K13 (measure-memory.sh), with a test in tests/infra/compose/measure_memory/test_measure_memory.py. |
| `tests/infra/compose/measure_memory/test_measure_memory.py` | Move VERBS and THREE into TestMeasureMemory as ClassVar constants, or into tests/infra/compose/helpers.py, which may hold shared constants. tests/conventions does not flag them today. Owner: K04 (test-writer of measure_memory). |
| `infra/compose/check-machine.sh`, `tests/infra/compose/check_machine/test_check_machine.py` | 'read -r memory_bytes cpus docker_root' splits on spaces, so a DockerRootDir containing a space is cut short. It then falls back to the script folder for the disk check. Read the docker root as the rest of the line (it already is, since it is the last read variable), or add a test with a spaced path to prove it. When the fallback is taken, as on Docker Desktop where the root is inside the VM, log on stderr that the disk was checked on the script folder instead. Owner: K06. |


<!-- timings -->
## ⏱️ Timings

Measured from the agents' transcripts by `python3 .claude/scripts/reports/progress.py timings --ticket T0.25` (TKT-10).

| Measure | Value |
| --- | --- |
| 🕒 Ticket started | 2026-11-27 18:07:05 |
| 🕒 Last activity | 2026-11-28 01:17:53 |
| ⏱️ **Overall ticket time** (first start to last activity) | **7h10m47s** |
| 🤖 Time with agents working (sum of runs) | 28m51s |
| ⏸️ Time between runs (approvals, fixes) | 6h41m55s |
| 🔁 Workflow runs | 4 |
| 🪙 **Tokens consumed** (input, output, cache write, cache read) | **21.99M** |

#### 🪙 Tokens by model

| Model | Input | Output | Cache write | Cache read | Total |
| --- | --- | --- | --- | --- | --- |
| 🟢 haiku | 0k | 120k | 1.26M | 5.69M | **7.07M** |
| 🔵 sonnet | 0k | 121k | 1.44M | 8.70M | **10.26M** |
| 🟣 opus | 0k | 96k | 316k | 4.24M | **4.65M** |
| **All models** | 0k | 338k | 3.01M | 18.64M | **21.99M** |

### 1. ticket-plan · 2026-11-27 18:07:05 to 18:15:07 · ⏱️ 8m01s

| Phase | Start | End | Elapsed | Steps |
| --- | --- | --- | --- | --- |
| Ticket | 18:07:05 | 18:07:47 | 0m42s | 2 |
| Check | 18:07:48 | 18:07:51 | 0m03s | 1 |
| Plan | 18:07:52 | 18:14:08 | 6m16s | 1 |
| Write | 18:14:08 | 18:15:07 | 0m59s | 2 |

Tokens of this run: 0k · 148k · 577k · 5.03M · **5.75M** (input · output · cache write · cache read · total)

| Step | Model | Start | End | Elapsed | Input | Output | Cache write | Cache read | Total |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ done check T0.25 | 🟢 haiku | 18:07:05 | 18:07:11 | 0m05s | 0k | 0k | 37k | 73k | **112k** |
| ✅ ticket-writer T0.25 | 🔵 sonnet | 18:07:12 | 18:07:47 | 0m35s | 0k | 18k | 144k | 1.08M | **1.25M** |
| ✅ check TICKET.md T0.25 | 🟢 haiku | 18:07:48 | 18:07:51 | 0m03s | 0k | 0k | 35k | 38k | **73k** |
| ✅ planner T0.25 | 🟣 opus | 18:07:52 | 18:14:08 | 6m16s | 0k | 84k | 205k | 3.43M | **3.72M** |
| ✅ scribe T0.25 | 🟢 haiku | 18:14:08 | 18:15:04 | 0m55s | 0k | 44k | 119k | 357k | **521k** |
| ✅ check PLAN.md T0.25 | 🟢 haiku | 18:15:04 | 18:15:07 | 0m03s | 0k | 0k | 35k | 38k | **73k** |

### 2. ticket-run · 2026-11-28 00:55:46 to 01:04:26 · ⏱️ 8m40s

| Phase | Start | End | Elapsed | Steps |
| --- | --- | --- | --- | --- |
| Gate | 00:55:46 | 00:56:25 | 0m39s | 4 |
| Waves | 00:56:27 | 01:04:26 | 7m59s | 19 |
| Verify | | | not run | 0 |
| Review | | | not run | 0 |
| Finish | | | not run | 0 |

Tokens of this run: 0k · 110k · 1.15M · 7.50M · **8.77M** (input · output · cache write · cache read · total)

| Step | Model | Start | End | Elapsed | Input | Output | Cache write | Cache read | Total |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ gate T0.25 | 🟢 haiku | 00:55:46 | 00:55:55 | 0m09s | 0k | 3k | 42k | 169k | **215k** |
| ✅ plan check T0.25 | 🟢 haiku | 00:55:55 | 00:55:58 | 0m02s | 0k | 0k | 36k | 39k | **76k** |
| ✅ start rule T0.25 | 🟢 haiku | 00:55:58 | 00:56:10 | 0m11s | 0k | 0k | 36k | 39k | **76k** |
| ✅ integrator prepare T0.25 | 🔵 sonnet | 00:56:10 | 00:56:25 | 0m15s | 0k | 0k | 37k | 84k | **122k** |
| ✅ K01 test-writer | 🔵 sonnet | 00:56:27 | 00:57:06 | 0m39s | 0k | 11k | 59k | 403k | **474k** |
| ✅ K02 test-writer | 🔵 sonnet | 00:56:28 | 00:57:55 | 1m27s | 0k | 9k | 49k | 589k | **648k** |
| ✅ K03 test-writer | 🔵 sonnet | 00:56:29 | 00:57:56 | 1m26s | 0k | 11k | 61k | 647k | **719k** |
| ✅ K04 test-writer | 🔵 sonnet | 00:56:32 | 00:57:00 | 0m28s | 0k | 3k | 44k | 308k | **356k** |
| ✅ K05 test-writer | 🔵 sonnet | 00:56:35 | 00:57:25 | 0m50s | 0k | 12k | 56k | 516k | **586k** |
| ✅ integrator Waves | 🔵 sonnet | 00:58:08 | 00:58:22 | 0m13s | 0k | 0k | 75k | 129k | **205k** |
| ✅ K06 implementer | 🔵 sonnet | 00:58:24 | 00:59:06 | 0m42s | 0k | 4k | 48k | 227k | **280k** |
| ✅ integrator Waves | 🔵 sonnet | 00:59:14 | 00:59:24 | 0m10s | 0k | 0k | 40k | 167k | **208k** |
| ✅ K07 implementer | 🔵 sonnet | 00:59:26 | 01:00:32 | 1m05s | 0k | 8k | 58k | 635k | **702k** |
| ❌ K08 implementer | 🔵 sonnet | 00:59:28 | 01:00:04 | 0m36s | 0k | 5k | 45k | 511k | **562k** |
| ✅ K04 test-writer (fix) | 🔵 sonnet | 01:00:42 | 01:01:04 | 0m22s | 0k | 3k | 45k | 222k | **271k** |
| ✅ integrator Waves | 🔵 sonnet | 01:01:05 | 01:01:15 | 0m09s | 0k | 1k | 41k | 166k | **208k** |
| ✅ K08 implementer | 🔵 sonnet | 01:01:18 | 01:02:14 | 0m56s | 0k | 6k | 55k | 609k | **671k** |
| ✅ integrator Waves | 🔵 sonnet | 01:02:15 | 01:02:27 | 0m12s | 0k | 0k | 40k | 167k | **208k** |
| ✅ K09 doc-writer | 🟢 haiku | 01:02:29 | 01:03:00 | 0m31s | 0k | 10k | 67k | 641k | **719k** |
| ❌ K10 doc-writer | 🟢 haiku | 01:02:30 | 01:03:11 | 0m41s | 0k | 7k | 46k | 574k | **628k** |
| ❌ K10 doc-writer | 🟢 haiku | 01:03:20 | 01:03:58 | 0m38s | 0k | 3k | 41k | 265k | **310k** |
| ✅ integrator Waves | 🔵 sonnet | 01:04:06 | 01:04:16 | 0m10s | 0k | 0k | 42k | 209k | **252k** |
| ✅ scribe T0.25 | 🟢 haiku | 01:04:17 | 01:04:26 | 0m09s | 0k | 3k | 81k | 178k | **262k** |

### 3. ticket-run · 2026-11-28 01:05:31 to 01:15:46 · ⏱️ 10m14s

| Phase | Start | End | Elapsed | Steps |
| --- | --- | --- | --- | --- |
| Gate | 01:05:31 | 01:06:11 | 0m40s | 4 |
| Waves | 01:06:13 | 01:12:22 | 6m08s | 9 |
| Verify | 01:12:24 | 01:13:20 | 0m55s | 1 |
| Review | 01:13:20 | 01:14:48 | 1m28s | 1 |
| Finish | 01:14:49 | 01:15:46 | 0m57s | 4 |

Tokens of this run: 0k · 69k · 989k · 5.32M · **6.38M** (input · output · cache write · cache read · total)

| Step | Model | Start | End | Elapsed | Input | Output | Cache write | Cache read | Total |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ gate T0.25 | 🟢 haiku | 01:05:31 | 01:05:41 | 0m09s | 0k | 4k | 49k | 164k | **217k** |
| ✅ plan check T0.25 | 🟢 haiku | 01:05:41 | 01:05:44 | 0m03s | 0k | 0k | 39k | 37k | **77k** |
| ✅ start rule T0.25 | 🟢 haiku | 01:05:45 | 01:05:56 | 0m11s | 0k | 0k | 39k | 77k | **116k** |
| ✅ integrator prepare T0.25 | 🔵 sonnet | 01:05:56 | 01:06:11 | 0m14s | 0k | 0k | 37k | 85k | **123k** |
| ✅ K11 implementer | 🔵 sonnet | 01:06:13 | 01:07:06 | 0m52s | 0k | 4k | 47k | 281k | **332k** |
| ✅ integrator Waves | 🔵 sonnet | 01:07:16 | 01:07:25 | 0m09s | 0k | 0k | 41k | 167k | **209k** |
| ✅ K12 implementer | 🔵 sonnet | 01:07:27 | 01:07:44 | 0m17s | 0k | 1k | 40k | 176k | **217k** |
| ✅ integrator Waves | 🔵 sonnet | 01:07:45 | 01:07:55 | 0m09s | 0k | 0k | 41k | 167k | **209k** |
| ✅ K13 implementer | 🔵 sonnet | 01:07:56 | 01:08:35 | 0m38s | 0k | 1k | 42k | 221k | **265k** |
| ✅ K14 implementer | 🔵 sonnet | 01:07:58 | 01:08:15 | 0m17s | 0k | 1k | 40k | 178k | **220k** |
| ✅ integrator Waves | 🔵 sonnet | 01:08:45 | 01:08:55 | 0m10s | 0k | 0k | 40k | 167k | **209k** |
| ✅ K10 doc-writer | 🟢 haiku | 01:08:56 | 01:12:13 | 3m16s | 0k | 18k | 78k | 1.73M | **1.83M** |
| ✅ integrator Waves | 🔵 sonnet | 01:12:13 | 01:12:22 | 0m09s | 0k | 1k | 43k | 208k | **253k** |
| ✅ verifier round 1 | 🟢 haiku | 01:12:24 | 01:13:20 | 0m55s | 0k | 0k | 39k | 80k | **120k** |
| ✅ reviewer round 1 | 🟣 opus | 01:13:20 | 01:14:48 | 1m28s | 0k | 12k | 111k | 806k | **930k** |
| ✅ scribe T0.25 | 🟢 haiku | 01:14:49 | 01:15:18 | 0m29s | 0k | 10k | 103k | 368k | **481k** |
| ✅ explainer T0.25 | 🔵 sonnet | 01:14:49 | 01:15:39 | 0m50s | 0k | 8k | 78k | 281k | **368k** |
| ✅ docs check T0.25 1 | 🟢 haiku | 01:15:39 | 01:15:42 | 0m03s | 0k | 0k | 39k | 76k | **116k** |
| ✅ scribe T0.25 (timings) | 🟢 haiku | 01:15:43 | 01:15:46 | 0m03s | 0k | 0k | 37k | 44k | **81k** |

### 4. ticket-run · 2026-11-28 01:15:58 to 01:17:53 · ⏱️ 1m54s

| Phase | Start | End | Elapsed | Steps |
| --- | --- | --- | --- | --- |
| Gate | 01:15:58 | 01:16:40 | 0m41s | 4 |
| Waves | | | not run | 0 |
| Verify | 01:16:40 | 01:17:38 | 0m58s | 1 |
| Review | | | not run | 0 |
| Finish | 01:17:39 | 01:17:53 | 0m14s | 3 |

Tokens of this run: 0k · 10k · 288k · 783k · **1.08M** (input · output · cache write · cache read · total)

| Step | Model | Start | End | Elapsed | Input | Output | Cache write | Cache read | Total |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ gate T0.25 | 🟢 haiku | 01:15:58 | 01:16:09 | 0m10s | 0k | 4k | 44k | 168k | **217k** |
| ✅ plan check T0.25 | 🟢 haiku | 01:16:09 | 01:16:12 | 0m03s | 0k | 0k | 39k | 76k | **116k** |
| ✅ start rule T0.25 | 🟢 haiku | 01:16:12 | 01:16:26 | 0m13s | 0k | 0k | 39k | 76k | **116k** |
| ✅ integrator prepare T0.25 | 🔵 sonnet | 01:16:26 | 01:16:40 | 0m13s | 0k | 0k | 37k | 85k | **123k** |
| ✅ verifier round 1 | 🟢 haiku | 01:16:40 | 01:17:38 | 0m58s | 0k | 0k | 37k | 123k | **161k** |
| ✅ scribe T0.25 | 🟢 haiku | 01:17:39 | 01:17:47 | 0m08s | 0k | 3k | 53k | 213k | **270k** |
| ✅ docs check T0.25 1 | 🟢 haiku | 01:17:48 | 01:17:52 | 0m04s | 0k | 0k | 36k | 39k | **76k** |
| 🔄 integrator finish T0.25 | 🔵 sonnet | 01:17:53 | 01:17:53 | 0m00s | 0k | 0k | 0k | 0k | **0k** |
<!-- /timings -->
