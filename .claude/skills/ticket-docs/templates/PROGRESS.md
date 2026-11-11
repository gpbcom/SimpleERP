# <KEY> — Progress

Updated at the end of every step and sub-step (status icon, files touched, test counts, commit, deviations and their reason, **Sub-steps**, **Time** and **Rules** lines). Plan: [PLAN.md](PLAN.md). Tests: [TESTS-CATALOG.md](TESTS-CATALOG.md). Evidence: [tests-evidences/README.md](tests-evidences/README.md).

**Legend:** ✅ done / PASS · 🔄 in progress · ⬜ to do · ⏳ waiting · ⏸️ paused · ❌ failed · ⚠️ warning / invalid run · 🚫 out of scope · 💻 local · 🟦 dev stage · 🟪 QA stage

## Status

Times are local, `YYYY-MM-DD HH:MM`, read with `date '+%F %H:%M'` when the step starts and when it ends, never guessed. **Elapsed** = Finished − Started − the ⏳ waits and ⏸️ pauses of the step (each listed on its **Time** line in the Log), written `<h>h<mm>`. Updated at the end of **every sub-step**, not only when a step ends: a 🔄 step shows `<h>h<mm> so far`.

Every code step goes **tests commit → 🔴 red run → code → 🟢 green run** (TEST-7), each run in its evidence folder (TEST-8).

| Step (PLAN.md) | Status | Started | Finished | Elapsed |
|---|---|---|---|---|
| 0a — Ticket documentation folder | ✅ Done | <DATE> <HH:MM> | <DATE> <HH:MM> | <h>h<mm> |
| 0b — Setup (branch, issue In progress) | ⏳ Waiting for the owner's go | — | — | — |
| <n> — <name> (TDD) | ⬜ To do | — | — | — |
| <n> — 💻 Local checks | ⬜ To do | — | — | — |
| <n> — 🟦 Dev stage | ⬜ To do | — | — | — |
| <n> — 🔬 Requirements audit (develop vs branch) | ⬜ To do | — | — | — |
| <n> — 📚 Documentation (DOC-2, project-docs) | ⬜ To do | — | — | — |
| <n> — 📝 Release note (DOC-3, release-notes) | ⬜ To do | — | — | — |
| <n> — Final acceptance run and hand-over | ⬜ To do | — | — | — |
| <n> — History bundle · squash (GIT-4) · push (GIT-1) · pull request (GIT-5) · In review (GIT-3) | ⬜ To do | — | — | — |
| <n> — 🟪 QA stage (GIT-6) | ⬜ To do | — | — | — |
| <n> — 📦 Archive (TEST-9) | ⬜ To do | — | — | — |
| <n> — PR review round 1 (pr-review-followup) | ⬜ To do | — | — | — |

**Total time:** <h>h<mm> elapsed (sum of the steps) · <h>h<mm> waiting / paused (excluded) · wall-clock <first Started> → <last Finished, or "running">.

Out of scope (marked in PLAN.md, never PASS): <🚫 item (Dn), or "none">.

## Stage validation

The commit is tested on the dev stage **and** the QA stage before the ticket is done (`stage.yml`, GIT-6). Each row links the run's evidence folder (TEST-8).

| Where | Status | Run | Commit | Result | Evidence |
|---|---|---|---|---|---|
| 💻 Local | ⬜ To do | — | — | — | — |
| 🟦 Dev | ⬜ To do | <Actions run URL> | — | — | — |
| 🟪 QA | ⬜ To do | <Actions run URL, approved by the owner on <date>> | — | — | — |

## Documentation

DOC-2 (project-docs skill): each chapter of `README.md`, `docs/functional/` and `docs/technical/` mapped from the branch's changes, updated or waived.

| Chapter | Status | What changed |
|---|---|---|
| <path> | ⬜ To do | <what changed, or "no doc impact: <reason>"> |

## Release note

DOC-3 (release-notes skill): [RELEASE-NOTE.md](RELEASE-NOTE.md) and `changelog.d/<KEY>.<type>.md`.

| Item | Status | Detail |
|---|---|---|
| RELEASE-NOTE.md | ⬜ To do | — |
| Changelog fragment | ⬜ To do | <`changelog.d/<KEY>.<type>.md`> |
| Issue comment `<!-- release-note -->` | ⬜ To do | <date, comment link: after the push> |

## Pull request

Opened only once the branch is one squashed commit (GIT-4, history bundle saved first), pushed on the owner's yes (GIT-1). The description has **10 lines at most** and `Closes #<n>` (GIT-5) and is copied here every time it is created or changed, newest on top.

| Step | Status | Detail |
|---|---|---|
| History bundle (GIT-4, TEST-7) | ⬜ To do | <`tests-evidences/history/…bundle`> |
| Squash into one commit (GIT-4) | ⬜ To do | <the owner's yes (date), commit> |
| Push (GIT-1) | ⬜ To do | <the owner's yes (date), remote branch> |
| Pull request (GIT-5) | ⬜ To do | <link, date> |
| Watched by pr-watch (GIT-7) | ⬜ To do | <`pr-watch register <KEY>`, date> |
| Issue → In review (GIT-3) | ⬜ To do | <date> |
| QA run started and announced (GIT-6) | ⬜ To do | <date, run URL, commit, comment link: only once local, dev, push and pull request are ✅> |
| Archive uploaded (TEST-9) | ⬜ To do | <release asset link, issue comment link> |

### Description — <date> (<n> / 10 lines)

```text
<the pull request description, 10 lines at most, with Closes #<n>>
```

## PR review

One round per push or QA run (pr-review-followup skill), newest on top: every review remark, verified, triaged (✅ fix · 📏 rule · ❓ asked · 🚫 by design) and acted on.

No round yet.

## Log

### Step 0a — Ticket documentation folder (<DATE>) ✅
- **Sub-steps:** ✅ issue read · ✅ attachments · ✅ code read-only · ✅ rules re-read · ✅ files written · ✅ checks
- **Time:** <DATE> <HH:MM> → <DATE> <HH:MM> · elapsed <h>h<mm> · excluded: <⏳ / ⏸️ from HH:MM to HH:MM, why; or "none">
  - <sub-step> <HH:MM>–<HH:MM> (<h>h<mm>) · <sub-step> <HH:MM>–<HH:MM> (<h>h<mm>) · …
- **Analysis:**
  - The GitHub issue was read with the GitHub MCP (`issue_read`); its <n> attachments were downloaded into [attachments/](attachments/) (checked with `file`).
  - The code was read only: <commit of `origin/develop`>.
  - **Findings:** <what exists, what is missing>.
- **Decisions:** <Dn by the owner, Dn proposed>: [EXPLAIN.md §6.3](EXPLAIN.md#63-decision-log).
- **Files created** (`docs/tickets/<KEY>/`): EXPLAIN.md (DOC-1 skeleton, §6 filled), IMPLEMENTATION.md, PLAN.md, PROGRESS.md, README.md, TESTS-CATALOG.md, TESTS-NOTICE.md, TICKET.md, `attachments/` (<n> files), `tests-evidences/README.md`.
- **No other file modified.** No branch, test or code. No issue or board change, no comment posted.
- **Checks:** ✅ `ticket-docs check <KEY>` prints nothing (DOC-1 included).
- **Rules:** DOC-1 ✅ (skeleton, §6 at plan time) · CS / GIT / DEP / TEST 🚫 not applicable (no code, no commit).
- **Next:** ⏳ the owner's go for step 0b; the owner posts the questions of [EXPLAIN.md §6.2](EXPLAIN.md#62-questions-for-the-issue--posted-by-the-owner-never-by-claude).

<!-- A code step entry looks like this:
### Step 2 — Customer storage (2026-11-12) ✅
- **Sub-steps:** ✅ tests commit `<sha>` · ✅ 🔴 red run ([local-2026-11-12-tdd-red-storage](tests-evidences/local-2026-11-12-tdd-red-storage/README.md)) · ✅ code `<sha>` · ✅ 🟢 green run ([local-2026-11-12-unit-storage](tests-evidences/local-2026-11-12-unit-storage/README.md)) · ✅ checks
-->

## Acceptance criteria — final verification

Filled at the final step, on the final commit. "—" = that place cannot test this criterion (say why in the Tests cell).

| AC | Tests | Command | Commit | 💻 Local | 🟦 Dev | 🟪 QA | Evidence |
|---|---|---|---|---|---|---|---|
| AC1 | <IDs> | <command> | <commit> | ⬜ | ⬜ | ⬜ | — |
