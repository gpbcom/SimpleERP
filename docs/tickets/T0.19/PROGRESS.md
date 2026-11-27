# T0.19: Progress

**Status:** 🟡 Planned

<!-- ticket:specs -->
## 📚 Specifications

The specification and design pages of [TICKET.md](TICKET.md), copied by `python3 .claude/scripts/tickets/ticket_refs.py sync`.

- [Deployment](../../technical/infrastructure/deployment.md)
- [📌 REQ-T09-02: Compose and Helm everywhere](../../specs/03-technical/t09-install-backups-and-updates/requirements/req-t09-02-compose-and-helm.md)
- [📜 D421: Infrastructure: fully CNCF compatible](../../specs/06-decisions/technical/d421-infrastructure-cncf.md)
- [📜 D438: Repository layout](../../specs/06-decisions/technical/d438-repository-layout.md)
- [Repository layout](../../technical/architecture/repository-layout.md)
- [Installation](../../specs/05-non-functional/installation.md)
<!-- /ticket:specs -->

## 📝 Events

| Time | Event | By | Result |
| --- | --- | --- | --- |
| 2026-11-27 18:17 | Plan written: 18 tasks, 4 waves | ticket-plan | ⏳ Awaiting approval |
| 2026-11-27 18:28 | Plan approved by the person (group approval) | 👤 person | 🟢 Approved |
| 2026-11-27 23:47 | Wave 1: 8 of 8 tasks done | workers | ✅ |
| 2026-11-27 23:47 | Integrate (Waves) | integrator | ✅ 8 integrated, 0 blocked, not committed |
| 2026-11-27 23:47 | Wave 2: 6 of 6 tasks done | workers | ✅ |
| 2026-11-27 23:47 | Integrate (Waves) | integrator | ✅ 6 integrated, 1 blocked, not committed |
| 2026-11-27 23:47 | Wave 3: 1 of 2 tasks done | workers | ❌ |
| 2026-11-27 23:47 | Integrate (Waves) | integrator | ✅ 1 integrated, 0 blocked, not committed |
| 2026-11-27 23:47 | Stopped in wave 3: K15 not done | workers | ❌ |
| 2026-11-27 23:51 | Plan change: K15 also adds infra/helm/templates/.gitkeep (helm lint --strict refused the umbrella chart without templates/); new task K19 moves test_helm_changes.py and test_helm_workflow.py into helm/ sub-folders, so tests/ci/detect_changes/ and tests/ci/workflows/checks/ stay at five Python files with T0.18 | 👤 person (P0 standing order) | 🟢 Approved |
| 2026-11-27 23:57 | Wave 2: 1 of 1 tasks done | workers | ✅ |
| 2026-11-27 23:57 | Integrate (Waves) | integrator | ✅ 1 integrated, 1 blocked, not committed |
| 2026-11-27 23:57 | Wave 3: 1 of 1 tasks done | workers | ✅ |
| 2026-11-27 23:57 | Integrate (Waves) | integrator | ✅ 1 integrated, 0 blocked, not committed |
| 2026-11-27 23:57 | Wave 4: 2 of 2 tasks done | workers | ✅ |
| 2026-11-27 23:57 | Integrate (Waves) | integrator | ✅ 2 integrated, 0 blocked, not committed |
| 2026-11-27 23:57 | Verify 1 (2 not applicable) | verifier | ❌ 1 failures |
| 2026-11-27 23:57 | Verify 2 (2 not applicable) | verifier | ❌ 1 failures |
| 2026-11-27 23:57 | Verify 3 (2 not applicable) | verifier | ❌ 1 failures |
| 2026-11-27 23:57 | Stopped: checks failing | verifier | ❌ pytest, infra/helm/README.md: tests/ci/detect_changes/test_repository_layout.py::TestRepositoryLayout::test_a_readme_of_a_folder_without_a_project_selects_nothing[infra/helm/README.md] fails: the README of infra/helm selects the repository and helm targets (repository true, helm true) where the test expects none. 1 failed, 1274 passed, 3 skipped. Not an environment failure. |
| 2026-11-27 23:57 | Work left uncommitted in /home/guillaume/Documents/Projects/Others/simple-erp on feature/tickets; /ticket-run T0.19 continues it | scribe | ⚠️ |
| 2026-11-28 00:01 | Plan change: new task K20 updates tests/ci/detect_changes/test_repository_layout.py, which still listed infra/helm/README.md as a folder without a project; it now checks that the chart's README selects helm and the repository tests | 👤 person (P0 standing order) | 🟢 Approved |
| 2026-11-28 00:02 | Wave 1: 1 of 1 tasks done | workers | ✅ |
| 2026-11-28 00:02 | Integrate (Waves) | integrator | ✅ 1 integrated, 0 blocked, not committed |
| 2026-11-28 00:02 | Verify 1 (2 not applicable) | verifier | ✅ passed |
| 2026-11-28 00:02 | Review 1 (full) | reviewer | ✅ 0 blocking, 6 follow-ups |
| 2026-11-28 00:02 | Waiting for the person's code review: nothing is committed or pushed until PLAN.md says **Push:** 🟢 Approved (TKT-18) | scribe | 👀 |
| 2026-11-28 00:05 | Push approved after the code review | 👤 person | 🟢 |
| 2026-11-28 00:05 | Verify 1 (2 not applicable) | verifier | ✅ passed |

## 🔜 Follow-ups

| File | What to change |
| --- | --- |
| `.github/workflows/ci.yml` `tests/ci/workflows/test_ci_workflow.py` | Add `helm` to the `needs` of the `images` job, as `terraform` already is, and add `helm` to `CHECK_JOBS` in the test. Right now a failing Helm check (step 2) does not stop the images from being built, and a push to develop could still publish them. The `result` job and automerge still gate the merge, so this is not blocking. (K-owner: the CI wiring task) |
| `infra/helm/values.yaml` `infra/helm/charts/platform/values.yaml` `infra/helm/charts/backoffice/values.yaml` `infra/helm/charts/platform/templates/_helpers.tpl` `infra/helm/charts/backoffice/templates/_helpers.tpl` `tests/infra/helm/test_rendering.py` | An empty `global.image.tag` falls back to `appVersion` 0.1.0, but no image is ever published under that tag, so a plain `helm install` without `--set global.image.tag` renders fine and then ends in ImagePullBackOff. Use `required` on the tag, or keep the fallback and say plainly in the README that the tag must be set. |
| `infra/helm/charts/platform/templates/deployment.yaml` `infra/helm/charts/platform/templates/_helpers.tpl` `infra/helm/charts/backoffice/templates/deployment.yaml` `infra/helm/charts/backoffice/templates/_helpers.tpl` | The two charts were written separately and differ for no reason. platform uses `if .Values.x` while backoffice uses `with`, the securityContext sits in a different place, and only backoffice adds the `helm.sh/chart` label. Align them, or move the shared helpers into a library chart before more service charts copy one of the two. |
| `tests/ci/check_helm/test_check_helm.py` `tests/infra/helm/test_charts.py` | Move the module-level constants (`REPOSITORY`, `SCRIPT`, `HELM_ROOT`, `TAG`, `NEEDS_TOOLS`, `ROOT`, `HELM`, `CHARTS`, `CHART_NAMES`) into ClassVars of the test class, as test_rendering.py and test_values.py already do. tests/conventions does not enforce this today. |
| `.github/workflows/release.yml` | Re-wrap the header comment line changed by this ticket ("commit with everything selected (Python, TypeScript, Terraform and Helm)..."). It now runs well past 120 characters. |
| `docs/tickets/T0.19/tests-evidences/` | Add a local run of `.github/scripts/check_helm.sh` with kubeconform installed (the helm.xml report), so the Kubernetes schema validation of AC2 has evidence beyond CI. The three kubeconform tests were skipped in the recorded pytest run (3 skipped). |

<!-- timings -->
## ⏱️ Timings

Measured from the agents' transcripts by `python3 .claude/scripts/reports/progress.py timings --ticket T0.19` (TKT-10).

| Measure | Value |
| --- | --- |
| 🕒 Ticket started | 2026-11-27 18:07:05 |
| 🕒 Last activity | 2026-11-28 00:05:56 |
| ⏱️ **Overall ticket time** (first start to last activity) | **5h58m51s** |
| 🤖 Time with agents working (sum of runs) | 34m09s |
| ⏸️ Time between runs (approvals, fixes) | 5h24m41s |
| 🔁 Workflow runs | 5 |
| 🪙 **Tokens consumed** (input, output, cache write, cache read) | **30.47M** |

#### 🪙 Tokens by model

| Model | Input | Output | Cache write | Cache read | Total |
| --- | --- | --- | --- | --- | --- |
| 🟢 haiku | 0k | 152k | 1.42M | 5.28M | **6.86M** |
| 🔵 sonnet | 0k | 256k | 1.98M | 15.10M | **17.34M** |
| 🟣 opus | 0k | 130k | 439k | 5.71M | **6.28M** |
| **All models** | 1k | 539k | 3.84M | 26.09M | **30.47M** |

### 1. ticket-plan · 2026-11-27 18:07:05 to 18:17:24 · ⏱️ 10m18s

| Phase | Start | End | Elapsed | Steps |
| --- | --- | --- | --- | --- |
| Ticket | 18:07:05 | 18:07:53 | 0m47s | 2 |
| Check | 18:07:53 | 18:07:57 | 0m03s | 1 |
| Plan | 18:07:57 | 18:15:56 | 7m58s | 1 |
| Write | 18:15:56 | 18:17:24 | 1m27s | 2 |

Tokens of this run: 0k · 207k · 786k · 7.13M · **8.12M** (input · output · cache write · cache read · total)

| Step | Model | Start | End | Elapsed | Input | Output | Cache write | Cache read | Total |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ done check T0.19 | 🟢 haiku | 18:07:05 | 18:07:11 | 0m05s | 0k | 0k | 37k | 73k | **112k** |
| ✅ ticket-writer T0.19 | 🔵 sonnet | 18:07:12 | 18:07:53 | 0m40s | 0k | 21k | 175k | 1.50M | **1.70M** |
| ✅ check TICKET.md T0.19 | 🟢 haiku | 18:07:53 | 18:07:57 | 0m03s | 0k | 0k | 35k | 38k | **73k** |
| ✅ planner T0.19 | 🟣 opus | 18:07:57 | 18:15:56 | 7m58s | 0k | 114k | 307k | 4.77M | **5.19M** |
| ✅ scribe T0.19 | 🟢 haiku | 18:15:56 | 18:17:19 | 1m22s | 0k | 70k | 192k | 671k | **933k** |
| ✅ check PLAN.md T0.19 | 🟢 haiku | 18:17:19 | 18:17:24 | 0m04s | 0k | 0k | 37k | 73k | **112k** |

### 2. ticket-run · 2026-11-27 23:39:20 to 23:47:32 · ⏱️ 8m11s

| Phase | Start | End | Elapsed | Steps |
| --- | --- | --- | --- | --- |
| Gate | 23:39:20 | 23:40:00 | 0m40s | 4 |
| Waves | 23:40:02 | 23:47:32 | 7m29s | 21 |
| Verify | | | not run | 0 |
| Review | | | not run | 0 |
| Finish | | | not run | 0 |

Tokens of this run: 0k · 204k · 1.30M · 11.10M · **12.61M** (input · output · cache write · cache read · total)

| Step | Model | Start | End | Elapsed | Input | Output | Cache write | Cache read | Total |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ gate T0.19 | 🟢 haiku | 23:39:20 | 23:39:31 | 0m11s | 0k | 5k | 47k | 206k | **259k** |
| ✅ plan check T0.19 | 🟢 haiku | 23:39:32 | 23:39:35 | 0m03s | 0k | 0k | 38k | 76k | **115k** |
| ✅ start rule T0.19 | 🟢 haiku | 23:39:35 | 23:39:45 | 0m09s | 0k | 0k | 38k | 76k | **115k** |
| ✅ integrator prepare T0.19 | 🔵 sonnet | 23:39:46 | 23:40:00 | 0m14s | 0k | 0k | 37k | 84k | **122k** |
| ✅ K01 test-writer | 🔵 sonnet | 23:40:02 | 23:41:38 | 1m35s | 0k | 14k | 55k | 699k | **769k** |
| ✅ K02 test-writer | 🔵 sonnet | 23:40:03 | 23:42:08 | 2m04s | 0k | 22k | 72k | 775k | **870k** |
| ✅ K03 test-writer | 🔵 sonnet | 23:40:05 | 23:41:12 | 1m07s | 0k | 15k | 48k | 597k | **661k** |
| ✅ K04 test-writer | 🔵 sonnet | 23:40:06 | 23:41:48 | 1m42s | 0k | 10k | 49k | 502k | **562k** |
| ✅ K05 test-writer | 🔵 sonnet | 23:40:08 | 23:41:49 | 1m40s | 0k | 12k | 61k | 598k | **672k** |
| ✅ K06 test-writer | 🔵 sonnet | 23:40:11 | 23:41:04 | 0m52s | 0k | 10k | 52k | 372k | **435k** |
| ✅ K07 test-writer | 🔵 sonnet | 23:40:14 | 23:40:51 | 0m37s | 0k | 2k | 49k | 272k | **324k** |
| ✅ K08 test-writer | 🔵 sonnet | 23:40:18 | 23:40:54 | 0m35s | 0k | 1k | 43k | 176k | **221k** |
| ✅ integrator Waves | 🔵 sonnet | 23:42:22 | 23:42:40 | 0m18s | 0k | 0k | 40k | 123k | **165k** |
| ✅ K09 implementer | 🔵 sonnet | 23:42:42 | 23:44:23 | 1m41s | 0k | 28k | 85k | 830k | **944k** |
| ✅ K10 implementer | 🔵 sonnet | 23:42:44 | 23:44:23 | 1m38s | 0k | 31k | 83k | 928k | **1.04M** |
| ✅ K11 implementer | 🔵 sonnet | 23:42:46 | 23:43:55 | 1m09s | 0k | 5k | 45k | 364k | **415k** |
| ✅ K12 implementer | 🔵 sonnet | 23:42:48 | 23:44:04 | 1m16s | 0k | 5k | 60k | 753k | **819k** |
| ✅ K13 implementer | 🔵 sonnet | 23:42:49 | 23:44:03 | 1m13s | 0k | 3k | 51k | 365k | **420k** |
| ✅ K14 implementer | 🔵 sonnet | 23:42:52 | 23:43:54 | 1m02s | 0k | 3k | 47k | 363k | **414k** |
| ✅ integrator Waves | 🔵 sonnet | 23:44:37 | 23:45:00 | 0m22s | 0k | 2k | 43k | 302k | **349k** |
| ❌ K15 implementer | 🔵 sonnet | 23:45:01 | 23:46:02 | 1m00s | 0k | 3k | 49k | 467k | **521k** |
| ✅ K16 implementer | 🔵 sonnet | 23:45:03 | 23:45:42 | 0m39s | 0k | 3k | 47k | 596k | **648k** |
| ❌ K15 implementer | 🔵 sonnet | 23:46:11 | 23:47:00 | 0m49s | 0k | 13k | 58k | 955k | **1.03M** |
| ✅ integrator Waves | 🔵 sonnet | 23:47:01 | 23:47:19 | 0m17s | 0k | 1k | 44k | 307k | **352k** |
| ✅ scribe T0.19 | 🟢 haiku | 23:47:19 | 23:47:32 | 0m12s | 0k | 3k | 46k | 304k | **354k** |

### 3. ticket-run · 2026-11-27 23:49:12 to 23:57:40 · ⏱️ 8m27s

| Phase | Start | End | Elapsed | Steps |
| --- | --- | --- | --- | --- |
| Gate | 23:49:12 | 23:49:54 | 0m42s | 4 |
| Waves | 23:49:55 | 23:53:52 | 3m56s | 7 |
| Verify | 23:53:52 | 23:57:27 | 3m34s | 5 |
| Review | | | not run | 0 |
| Finish | 23:57:27 | 23:57:40 | 0m12s | 1 |

Tokens of this run: 0k · 46k · 722k · 3.94M · **4.71M** (input · output · cache write · cache read · total)

| Step | Model | Start | End | Elapsed | Input | Output | Cache write | Cache read | Total |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ gate T0.19 | 🟢 haiku | 23:49:12 | 23:49:25 | 0m13s | 0k | 6k | 50k | 171k | **227k** |
| ✅ plan check T0.19 | 🟢 haiku | 23:49:26 | 23:49:29 | 0m02s | 0k | 0k | 37k | 40k | **77k** |
| ✅ start rule T0.19 | 🟢 haiku | 23:49:29 | 23:49:40 | 0m10s | 0k | 0k | 39k | 77k | **117k** |
| ✅ integrator prepare T0.19 | 🔵 sonnet | 23:49:40 | 23:49:54 | 0m13s | 0k | 0k | 38k | 86k | **125k** |
| ✅ K19 implementer | 🔵 sonnet | 23:49:55 | 23:50:40 | 0m44s | 0k | 2k | 42k | 400k | **445k** |
| ✅ integrator Waves | 🔵 sonnet | 23:50:41 | 23:50:54 | 0m13s | 0k | 1k | 42k | 298k | **343k** |
| ✅ K15 implementer | 🔵 sonnet | 23:50:56 | 23:51:48 | 0m51s | 0k | 3k | 43k | 364k | **411k** |
| ✅ integrator Waves | 🔵 sonnet | 23:52:02 | 23:52:15 | 0m13s | 0k | 0k | 41k | 168k | **211k** |
| ✅ K17 doc-writer | 🟢 haiku | 23:52:17 | 23:53:25 | 1m07s | 0k | 11k | 59k | 609k | **680k** |
| ✅ K18 doc-writer | 🟢 haiku | 23:52:19 | 23:53:14 | 0m54s | 0k | 3k | 51k | 404k | **459k** |
| ✅ integrator Waves | 🔵 sonnet | 23:53:41 | 23:53:52 | 0m11s | 0k | 0k | 44k | 212k | **257k** |
| ✅ verifier round 1 | 🟢 haiku | 23:53:52 | 23:54:47 | 0m54s | 0k | 1k | 41k | 81k | **123k** |
| ❌ FIX-K15+K18 implementer (fix) | 🔵 sonnet | 23:54:49 | 23:55:08 | 0m19s | 0k | 2k | 46k | 308k | **357k** |
| ✅ verifier round 2 | 🟢 haiku | 23:55:09 | 23:56:03 | 0m54s | 0k | 0k | 5k | 116k | **123k** |
| ❌ FIX-K15+K18 implementer (fix) | 🔵 sonnet | 23:56:05 | 23:56:30 | 0m25s | 0k | 3k | 44k | 266k | **314k** |
| ✅ verifier round 3 | 🟢 haiku | 23:56:33 | 23:57:27 | 0m54s | 0k | 0k | 41k | 81k | **123k** |
| ✅ scribe T0.19 | 🟢 haiku | 23:57:27 | 23:57:40 | 0m12s | 0k | 5k | 51k | 256k | **312k** |

### 4. ticket-run · 2026-11-27 23:58:32 to 00:03:47 · ⏱️ 5m14s

| Phase | Start | End | Elapsed | Steps |
| --- | --- | --- | --- | --- |
| Gate | 23:58:32 | 23:59:13 | 0m40s | 4 |
| Waves | 23:59:15 | 23:59:54 | 0m38s | 2 |
| Verify | 23:59:54 | 00:00:48 | 0m53s | 1 |
| Review | 00:00:48 | 00:02:32 | 1m44s | 1 |
| Finish | 00:02:32 | 00:03:47 | 1m14s | 4 |

Tokens of this run: 0k · 68k · 748k · 2.94M · **3.76M** (input · output · cache write · cache read · total)

| Step | Model | Start | End | Elapsed | Input | Output | Cache write | Cache read | Total |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ gate T0.19 | 🟢 haiku | 23:58:32 | 23:58:45 | 0m12s | 0k | 6k | 52k | 165k | **224k** |
| ✅ plan check T0.19 | 🟢 haiku | 23:58:45 | 23:58:49 | 0m03s | 0k | 0k | 42k | 75k | **118k** |
| ✅ start rule T0.19 | 🟢 haiku | 23:58:49 | 23:59:00 | 0m10s | 0k | 0k | 39k | 77k | **118k** |
| ✅ integrator prepare T0.19 | 🔵 sonnet | 23:59:00 | 23:59:13 | 0m13s | 0k | 0k | 38k | 86k | **126k** |
| ✅ K20 test-writer | 🔵 sonnet | 23:59:15 | 23:59:41 | 0m25s | 0k | 1k | 41k | 178k | **221k** |
| ✅ integrator Waves | 🔵 sonnet | 23:59:44 | 23:59:54 | 0m10s | 0k | 1k | 45k | 212k | **259k** |
| ✅ verifier round 1 | 🟢 haiku | 23:59:54 | 00:00:48 | 0m53s | 0k | 0k | 40k | 81k | **122k** |
| ✅ reviewer round 1 | 🟣 opus | 00:00:48 | 00:02:32 | 1m44s | 0k | 15k | 131k | 939k | **1.09M** |
| ✅ scribe T0.19 | 🟢 haiku | 00:02:32 | 00:03:09 | 0m36s | 0k | 19k | 106k | 476k | **602k** |
| ✅ explainer T0.19 | 🔵 sonnet | 00:02:32 | 00:03:38 | 1m05s | 0k | 21k | 131k | 479k | **633k** |
| ✅ docs check T0.19 1 | 🟢 haiku | 00:03:38 | 00:03:42 | 0m03s | 0k | 0k | 39k | 78k | **118k** |
| ✅ scribe T0.19 (timings) | 🟢 haiku | 00:03:42 | 00:03:47 | 0m04s | 0k | 0k | 38k | 87k | **126k** |

### 5. ticket-run · 2026-11-28 00:03:59 to 00:05:56 · ⏱️ 1m56s

| Phase | Start | End | Elapsed | Steps |
| --- | --- | --- | --- | --- |
| Gate | 00:03:59 | 00:04:42 | 0m42s | 4 |
| Waves | | | not run | 0 |
| Verify | 00:04:42 | 00:05:37 | 0m54s | 1 |
| Review | | | not run | 0 |
| Finish | 00:05:37 | 00:05:56 | 0m19s | 3 |

Tokens of this run: 0k · 11k · 286k · 971k · **1.27M** (input · output · cache write · cache read · total)

| Step | Model | Start | End | Elapsed | Input | Output | Cache write | Cache read | Total |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ gate T0.19 | 🟢 haiku | 00:03:59 | 00:04:13 | 0m13s | 0k | 6k | 48k | 172k | **227k** |
| ✅ plan check T0.19 | 🟢 haiku | 00:04:13 | 00:04:17 | 0m03s | 0k | 0k | 39k | 77k | **118k** |
| ✅ start rule T0.19 | 🟢 haiku | 00:04:17 | 00:04:28 | 0m11s | 0k | 0k | 39k | 77k | **118k** |
| ✅ integrator prepare T0.19 | 🔵 sonnet | 00:04:28 | 00:04:42 | 0m14s | 0k | 0k | 38k | 87k | **126k** |
| ✅ verifier round 1 | 🟢 haiku | 00:04:42 | 00:05:37 | 0m54s | 0k | 0k | 38k | 125k | **164k** |
| ✅ scribe T0.19 | 🟢 haiku | 00:05:37 | 00:05:50 | 0m13s | 0k | 2k | 45k | 308k | **356k** |
| ✅ docs check T0.19 1 | 🟢 haiku | 00:05:51 | 00:05:54 | 0m03s | 0k | 0k | 0k | 117k | **118k** |
| 🔄 integrator finish T0.19 | 🔵 sonnet | 00:05:54 | 00:05:56 | 0m01s | 0k | 0k | 35k | 4k | **40k** |
<!-- /timings -->
