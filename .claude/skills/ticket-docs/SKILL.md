---
name: ticket-docs
description: Create and maintain the local documentation folder of a simple-erp ticket (a GitHub issue #n, key GH-<n>) under docs/tickets/GH-<n>/ - TICKET, PLAN, IMPLEMENTATION, PROGRESS, README, EXPLAIN, TESTS-CATALOG, TESTS-NOTICE, RELEASE-NOTE, attachments/, tests-evidences/, and STATUS.md when paused or at a rebase conflict - with status icons, the time spent per step and in total, TDD per code step (tests commit, red run, code, green run), evidence recorded with `ticket-docs record-run` for every run (unit, GUI, E2E, local, CI, dev and QA stage runs), every report kept and indexed, a requirements audit, the project documentation (project-docs) and release note (release-notes) at hand-over, and the archive of the folder to the GitHub pre-release evidence-GH-<n>. Use when asked to create or start a ticket's documentation folder, to plan or implement an issue, to record a test run, to pause or resume a ticket, to audit its requirements, to hand it over, or when a rebase on develop conflicts; also load it when resuming work on a ticket whose folder exists.
argument-hint: <GH-n or issue URL> [create|implement|pause|resume|handover]
---

# Ticket documentation folder

Arguments: `$ARGUMENTS`: the ticket (`GH-<n>`, `#<n>` or the issue URL) and an optional mode (default `create`, or `resume` when the folder exists).

- **Folder:** `docs/tickets/GH-<n>/` at the repository root. It is **local and not versioned** (`.gitignore`): `ticket-docs archive` keeps it on GitHub (TEST-9). Confirm the path in the reply.
- **Templates:** [templates/](templates/). Copy them, replace `<KEY>`, `<TITLE>`, `<DATE>` (YYYY-MM-DD), then fill every `<…>` placeholder. Never leave a placeholder in a finished file.
- **Rules the folder must follow:** `AGENT.md` and `.claude/rules/`, each loaded live by its skill: **coding-style-rules** (CS), **git-deploy-rules** (GIT, DEP), **testing-rules** (TEST), **ticket-documentation-rules** (DOC). Load them at creation, before writing code, before every commit and at hand-over; the version read at that moment applies.
- **The tool:** `.claude/skills/ticket-docs/bin/ticket-docs <command>` (written `ticket-docs` below):

| Command | Does |
|---|---|
| `record-run --ticket <KEY> --kind unit\|gui\|e2e\|check --where local\|ci\|dev\|qa --check <name> --what "<text>" [--expect red] -- <command>` | Runs the command and writes `tests-evidences/<where>-<date>-<check>/`: README (command, commit, kind, place, date, result), `console.txt`, and the reports (adds `--junitxml`/`--html` to `pytest`, copies Playwright's report and `results.json`). Exits with the command's code |
| `record-run … --run-id <id>` | Same for a GitHub Actions run: downloads its artifacts and log, reads its result and commit |
| `check <KEY> [--offline]` | Checks the folder against this skill and the rules (TEST-7, TEST-8, TEST-9, DOC-1, DOC-2, DOC-3, GIT-5…). Prints nothing when complete. `--offline` leaves out the GitHub archive check |
| `report-index [--output <file>]` | Regenerates `docs/tickets/README.md`, the index of every run of every ticket (or writes it elsewhere) |
| `history-bundle <KEY>` | Saves the branch's commits in `tests-evidences/history/` before a squash (GIT-4), with their list (`.txt`) and their base (`.base`) |
| `allow-squash <KEY>` | **Human only, in their own terminal.** After `git reset --soft <base>`, opens `/dev/tty`, shows a random 6-character code there and writes a one-shot permit (`~/.local/state/claude-harness/squash-permits/<KEY>.json`: branch, `HEAD`, staged tree, 30 minutes) once that code is typed back. With it `git-gate` passes the one squash commit. It fails closed without a terminal, so Claude's Bash cannot run it, and the gate refuses it anyway |
| `file-gate` | The `PreToolUse` hook on Write, Edit, MultiEdit and NotebookEdit: refuses a file in a folder of `guard_state_folders` (squash permits, AI test ledgers), with `~`, links and `..` resolved |
| `archive <KEY> [--dry-run]` | Zips the folder and uploads it to the pre-release `evidence-<KEY>`, then comments the link on the issue. `--dry-run` prints the gh commands instead |
| `board <KEY> "<Status>"` | Sets the issue's Status on the project board of `conf/github.yaml` (Backlog, Ready, In progress, In review, QA, Done) |
| `git-gate`, `time-reminder` | The `PreToolUse` and `PostToolUse` hooks (`.claude/settings.json`) |

Every command but `board` and the hooks takes `--root <docs/tickets folder>`; by default it is the one of the current repository, or of the main checkout from a linked worktree. What a folder must hold is in [conf/folder-rules.yaml](conf/folder-rules.yaml).

## What the folder holds

| File | Required | Written | Holds |
|---|---|---|---|
| `TICKET.md` | yes | creation | The issue: metadata, related issues, the body **unchanged** (reformatted as Markdown, topics numbered T1…), the rules read from text and images, the **exhaustive acceptance criteria**, the attachments table |
| `PLAN.md` | yes | creation | Context, decisions, steps (each code step TDD: tests commit, red run, code, green run), AC → tests → validation, rules enforced, files modified (summary + link), out of scope, verification. **Takes precedence** over IMPLEMENTATION.md |
| `IMPLEMENTATION.md` | yes | creation, then kept current | The implementation choices and their justification, the exact list of files modified (§0), and per file today vs target |
| `TESTS-CATALOG.md` | yes | creation | Every test, one block per AC (ID, level, file, given / when / then, state kept / fixed / new), the AC → tests matrix, counts |
| `TESTS-NOTICE.md` | yes | creation | How to run each test level, **adapted** from `.claude/rules/TESTS-NOTICE.md` to this feature |
| `PROGRESS.md` | yes | creation, then **at the end of every sub-step** | Status table with the time spent, stage validation, documentation, release note, pull request, PR review, log per step, final verification, with status icons |
| `README.md` | yes | creation, then on every status change | **Presents the feature**, its current status, and the index of the folder |
| `EXPLAIN.md` | yes | skeleton + **§6 at creation**; the rest at hand-over | DOC-1 hand-over document for developers and testers |
| `RELEASE-NOTE.md` | yes, at hand-over | release-notes skill | DOC-3 release note for users |
| `STATUS.md` | when paused, and at every rebase conflict | when the owner pauses the ticket; as soon as a rebase conflict is detected | Pause: why, the exact state left behind, how to resume. Rebase conflict: one ❌ entry per conflict |
| `attachments/` | yes | creation | Every file attached to the issue body or comments |
| `tests-evidences/` | yes | `README.md` index at creation, one folder per run after | Proof of every run, every report kept |
| `tests-evidences/dev-<date>-requirements-audit/REPORT.md` | yes, once finished | hand-over | The requirements audit |

Extra files only when the ticket needs them (e.g. `PR-DESCRIPTION.md` while a PR waits). List each one in README.md.

## Status icons (PROGRESS.md and STATUS.md)

Only these icons, and both files carry this legend under their title.

| Icon | Meaning |
|---|---|
| ✅ | Done / PASS (always with its evidence link, TEST-8) |
| 🔄 | In progress |
| ⬜ | To do |
| ⏳ | Waiting: the owner's go or yes, an approval, an answer |
| ⏸️ | Paused (see STATUS.md) |
| ▶️ | Resumed (STATUS.md entries) |
| ❌ | Failed / FAIL |
| ⚠️ | Warning: invalid run (environment failure), unrelated failures, deviation |
| 🚫 | Out of scope (Dn), never PASS |
| 💻 🟦 🟪 | Where it ran: local, dev stage, QA stage |

Where they go:
- **PROGRESS.md:** every cell of the Status table starts with an icon; every step heading of the Log ends with its icon (`### Step 3 — Customer storage (2026-11-12) ✅`); each step entry has a **Sub-steps** line (`✅ tests commit · ✅ 🔴 red run · ✅ code · 🔄 🟢 green run · ⬜ checks`); the stage, documentation, release-note and final-verification tables put an icon in every result cell.
- **STATUS.md:** every dated entry heading starts with an icon (`## ⏸️ 2026-11-12: paused on …`, `## ▶️ …: resumed …`, `## ❌ …: rebase conflict on develop in <file>`); "How to resume" is a checklist of ⬜ / ✅ items.
- README.md's status line starts with the same icon as PROGRESS.md's current step.

## Time spent (PROGRESS.md)

The time spent **must** be computed for every step and for the whole ticket, and all of it lives in PROGRESS.md.

- **Status table columns:** `Step | Status | Started | Finished | Elapsed`. A ⬜ step reads `—` in the three time cells; a 🔄 / ⏳ / ⏸️ step has its Started time and an Elapsed **so far** (`1h10 so far`); a ✅ step has all three.
- **Read the clock, never guess:** `date '+%F %H:%M'` when a step starts (write Started and 🔄 at once, before the work) and when it ends.
- **Elapsed** = Finished − Started − the waits and pauses of that step, written `<h>h<mm>`. Each excluded period is listed on the step's **Time** line: `- **Time:** 2026-11-12 09:12 → 2026-11-12 11:47 · elapsed 2h05 · excluded: ⏳ 10:20–10:50 the owner's yes for the push`.
- **Kept current, never filled at the end.** At the end of **every sub-step** (and every commit, run, wait or pause), update the running step's Elapsed so far, its **Time** line, and the **Total time** line.
- **Hook:** `ticket-docs time-reminder` runs after every `git commit` on a ticket branch. When PROGRESS.md has no 🔄 step, or its latest clock reading is more than 15 minutes old, it asks you to update the times before anything else. Act on it at once.
- **Total time** line under the Status table: the sum of the steps' Elapsed, the sum of the excluded waits and pauses, and the wall-clock span.
- **A step re-opened** later (review fix, re-run) is a new Status row with its own times.
- **Missed clock:** rebuild the time from the evidence (commit times, evidence README dates), mark the cell `(reconstructed)` and say from what on the Time line.

## Mode `create` — the documentation folder

"Create the documentation folder" means **this mode only**: no branch, test or code, no board change, no comment posted. Stop at the end and wait for the owner's go.

1. **Read the issue** with the GitHub MCP: `issue_read` (body, comments, labels, sub-issues), then the linked issues and pull requests. If the MCP cannot read the private repository, use `gh issue view <n> --json title,body,comments,labels,assignees,milestone` instead. Never invent content.
2. **Download every attachment** (images and files in the body and comments, `https://github.com/user-attachments/...`) into `attachments/` with `gh api` or `curl -H "Authorization: Bearer $(gh auth token)"`, keep their names, check each with `file`. Describe each one in TICKET.md's attachments table: size, what it shows, which topics and ACs it serves.
3. **Read the code read-only** (`git fetch origin`, then `git show`, `git log`, `git grep` on `origin/develop`; no checkout) to know today vs target.
4. **Re-read `AGENT.md` and `.claude/rules/`.**
5. **Write the files in this order:** TICKET → PLAN → IMPLEMENTATION → TESTS-CATALOG → TESTS-NOTICE → EXPLAIN (skeleton + §6) → PROGRESS (step 0a logged) → README → `tests-evidences/README.md`.
6. **Check:** `ticket-docs check <KEY>` must print nothing.
7. **Reply:** the folder path, the files created, the questions of EXPLAIN §6.2, and that the implementation waits for the owner's go.

## Content rules

**Acceptance criteria (TICKET.md)**
- Exhaustive, numbered AC1…, grouped by topic, plus non-regression, contract and constraint ACs.
- An issue without ACs (bug, vague story) gets **derived** ACs, headed "derived, to be confirmed by the owner".
- UI issues: every element of every screenshot maps to an AC.

**PLAN.md**
- Decisions table `Dn`: the owner's (with the date) and Claude's proposals, marked "(Proposed)".
- **Every code step is TDD (TEST-7):** its tests are listed in the step, committed alone, seen red, then the code. No test step at the end, no exemption.
- **AC → tests → validation** table: every AC, its test IDs, how it is validated (unit, Playwright, Bruno, stage), the planned evidence folder.
- **Development rules enforced:** one row per rule ID (CS, GIT, DEP, DOC, TEST) with how it applies, the exact check, and when. Rules not applicable are listed with the reason.
- **Files modified:** the exact list lives once, in IMPLEMENTATION.md §0.
- **Out of scope:** each item named. A removed step stays in PLAN.md labelled "Out of scope (Dn)"; an out-of-scope AC is never PASS.
- Steps: 0a documentation folder, 0b setup (branch per GIT-8, issue → In progress, baselines), code steps (TDD), local checks, 🟦 dev stage, 🔬 requirements audit, 📚 documentation, 📝 release note, final run and hand-over, pull request, 🟪 QA stage, 📦 archive.

**IMPLEMENTATION.md**
- §0 **Files modified — exact list**, grouped by service / front end / package, then kind (new / modified / deleted), paths in alphabetical order, each with its change, its section and its tests; what was checked and left unchanged too. A ticket check (G02) compares `git diff --name-only origin/develop...HEAD` with §0 at the local checks and the final step.
- §1 **Implementation choices**: one block per choice, with the decision ID of EXPLAIN §6.3: context, options and their trade-offs, the choice, **the justification**, consequences, the ACs it serves.
- §2… per file: today (with line numbers on the base commit) vs target. Updated when the implementation deviates; the deviation and its reason also go to PROGRESS.md.

**EXPLAIN.md (DOC-1)**
- The 7 sections of `.claude/rules/ticket-documentation.md`, in order, with **3.1 API changes** first in §3.
- **§6 is written at plan time:** risks and open points (R = business, T = technical, F = front), the **questions for the issue** (numbered, each with a proposed answer; posted by the owner, never by Claude), and the **decision log** filled as answers arrive.
- The other sections stay "Not written yet: filled at hand-over" until implementation and tests are over.

## Mode `implement` — while the ticket is built

- The folder exists **before** any implementation. If it does not, run mode `create` first.
- **Setup (0b):** create the branch per GIT-8 from `origin/develop` (`git switch -c feature/GH-<n>-<slug> origin/develop`), move the issue to **In progress** on the board.
- **Each code step, in this order (TEST-7):**
  1. write the tests; `git commit` them alone (`[GH-<n>] test: …`);
  2. `ticket-docs record-run --ticket <KEY> --kind unit --where local --check tdd-red-<step> --expect red --what "<…>" -- <the tests>`; check that the failures point at the code to write;
  3. write the code; ruff, mypy, conventions; `git commit` (`[GH-<n>] feat|fix|refactor: …`);
  4. `ticket-docs record-run … --check unit-<step> --what "<…>" -- <the tests>`.
  The `git-gate` hook refuses a production-code commit without a red run since the last green one, or that adds new test files together with the code.
- **PROGRESS.md is updated at the end of every sub-step**: status icon, files touched, test counts, commit hash, evidence links, deviations and their reason, the **Sub-steps**, **Time** and **Rules** lines.
- README.md's status line follows PROGRESS.md.
- Local commits are free; every squash and every push waits for the owner's explicit yes, asked each time (GIT-1).

## Stages: tested on dev **and** on QA

A feature is never done on local tests alone: its commit runs on the **dev stage and the QA stage** (`.github/workflows/stage.yml`). The stages are ephemeral: each run starts the commit's images on a GitHub runner with the seeded data set, runs the tests, records a GitHub Deployment on the `dev` or `qa` environment and uploads every report. There is no stage to book or to wait for.

1. **Dev**, before the pull request, once the branch is pushed (GIT-1): `gh workflow run stage.yml --ref <branch> -f stage=dev -f ref=$(git rev-parse HEAD)`. It runs the smoke test, the Bruno collection and Playwright `@smoke`.
2. **QA**, once the pull request is open and every earlier step is ✅ (GIT-6): `gh workflow run stage.yml --ref <branch> -f stage=qa -f ref=$(git rev-parse HEAD)`. Ask the owner's yes first (GIT-6: it is the QA gate, ⏳ excluded from the step's time); the run then runs the full Playwright suite, Bruno, the upgrade test from the previous release, and the dependency scan.
3. **Evidence:** `gh run watch <run-id>`, then `ticket-docs record-run --ticket <KEY> --kind e2e --where dev|qa --check stage --what "<…>" --run-id <run-id>`. Search its `actions.log` for dependency errors (DEP-3).
4. A run that fails on its environment (a runner outage, a registry timeout) is ⚠️ invalid and run again, never ✅. Its folder is kept (TEST-9).
5. Only the owner can waive QA, logged as a decision (`Dn`) in EXPLAIN §6.3. The QA row then reads 🚫 with that Dn, never ✅.

## Evidence (tests-evidences/)

- One folder per run, written by `ticket-docs record-run`: `tests-evidences/<where>-<YYYY-MM-DD>-<check>/` with its README and the raw reports (TEST-8, TEST-9).
- **Every ✅, PASS, "green" or "works"**, in a reply, PROGRESS.md, EXPLAIN.md or the pull request, links to its evidence folder, on the commit claimed. No folder, no claim.
- **No folder is ever deleted**, failed, red and invalid runs included. No file over 5 MB.
- Scratchpad outputs are not evidence.
- No secret, token, password or signed URL in any file.
- After each run: `ticket-docs report-index`.

## Requirements audit — every finished ticket

A ticket is not finished until its **requirements audit** is written: an independent check, on the stage's seeded data, that every requirement of TICKET.md holds on the final commit, and that what users see is right. The tests prove the code does what the plan says; the audit asks whether the result is what the issue asked for.

- **When:** at hand-over, once the final commit has run on the dev stage, and again after a review fix that changes behaviour. Before the QA run.
- **Folder:** `tests-evidences/dev-<YYYY-MM-DD>-requirements-audit/` with `README.md` (from RUN-README), `REPORT.md` (from [REQUIREMENTS-AUDIT.md](templates/tests-evidences/REQUIREMENTS-AUDIT.md)), and the scripts and raw data of each figure.
- **Method:**
  1. Start from the issue's goal and any review comment, not from the test plan.
  2. List every requirement: each topic (T…) and AC of TICKET.md, plus EXPLAIN §3.1. Out-of-scope ones get a 🚫 row with their Dn.
  3. Collect the data twice on the same seeded stage: with the `develop` images and with the branch's.
  4. Check each requirement against the source of truth, record by record.
  5. Follow the data to every layer users touch (API, screens). A layer the ticket's data never reaches is "Not concerned", with the reason.
  6. Count each branch of a new matching (TEST-3).
  7. Write findings A1… with severity and owner. Each 🔴 / 🟠 finding is fixed before hand-over, or named in the pull request and EXPLAIN §6.
  8. State the limits.
- **Logged:** PROGRESS.md Status row `🔬 Requirements audit` with its verdict and link; README.md lists `REPORT.md`; the findings go to EXPLAIN §6.

## Mode `handover`

In this order, each step logged in PROGRESS.md with its times:

1. Re-run every level on the final commit (unit, conventions, checks), each with `record-run`; the dev stage run of that commit.
2. **Requirements audit** (above).
3. **📚 Documentation (DOC-2):** load the **project-docs** skill, mode `update`. `project-docs check --ticket <KEY>` prints nothing.
4. **📝 Release note (DOC-3):** load the **release-notes** skill, mode `ticket`. `release-notes check --ticket <KEY>` prints nothing.
5. PROGRESS.md **Total time** final and "Acceptance criteria — final verification": one row per AC with one result cell per place (💻, 🟦, 🟪), each with its evidence.
6. EXPLAIN.md complete; `ticket-docs report-index`; `ticket-docs check <KEY>` prints nothing.
7. **Pull request**, below.
8. **🟪 QA stage (GIT-6)**, then the PR review (pr-review-followup skill).
9. **📦 Archive (TEST-9):** `ticket-docs archive <KEY>`, logged with the asset and comment links. Again after every review round.

## Pull request

Load the **git-deploy-rules** skill first. Never open the pull request before every step above it is ✅ in PROGRESS.md:

1. **History bundle:** `ticket-docs history-bundle <KEY>` (keeps TEST-7 provable after the squash).
2. **Squash into one commit (GIT-4):** ask the owner first (GIT-1), showing the branch, the remote, the commits and the resulting message. On the yes, run `git merge-base HEAD origin/develop` (`origin/master` for a hotfix) and `git reset --soft <that commit>` as two commands. Then the owner runs `ticket-docs allow-squash <KEY>` **in their own terminal** and types back the code it shows there: `git-gate` lets the squash, which adds tests and code together, through only with that one-shot permit (same branch, `HEAD` and staged tree, within 30 minutes). Commit right after, staging nothing else: `git commit -m "[GH-<n>] <type>: <summary>"`. `git rev-list --count origin/develop..HEAD` prints `1`.
3. **Push:** ask again (GIT-1); a yes covers that one push.
4. **Description (GIT-5):** 10 lines at most with `Closes #<n>`, written first in PROGRESS.md's "Pull request" section. No "Generated with Claude Code" line.
5. **Open the pull request** (`gh pr create --base develop --body-file …`), then `pr-watch register <KEY>` (GIT-7).
6. **Issue → In review (GIT-3)**, logged with its date.
7. **Release note on the issue (DOC-3):** post RELEASE-NOTE.md as an issue comment starting with `<!-- release-note -->` (`gh issue comment <n> --body-file …`).

**What these barriers stop, and what they cannot:** `git-gate`, `file-gate` and the `/dev/tty` code stop accidents and a Claude session going down the wrong path: a squash without the owner, a permit or an AI cost ledger written by a tool call, `allow-squash` or `raise-cap` run from Claude's Bash (it has no terminal). They cannot stop a deliberate forgery by a process running as the same user, which can write any file and drive a pseudo-terminal: Claude runs as the owner's own user and there is no other account to hold a secret. `ticket-docs check <KEY>` at hand-over, CI and the review are the enforcement of TEST-7 and GIT-4.

A review fix is folded into the single commit, then history bundle, squash, push and description follow the same rules again, and the new commit gets its own dev and QA runs.

## Rebase conflicts — STATUS.md

Every rebase conflict of a ticket is kept in its `STATUS.md`, whoever finds it: a local `git rebase`, `git merge-tree` showing `CONFLICT`, or the PR watcher's `rebase_conflict` event. The ticket is not paused for that.

1. **As soon as it is detected**, before resolving it: create STATUS.md from [templates/STATUS.md](templates/STATUS.md) if needed, and add at the top `## ❌ <date>: rebase conflict on <target> in <file(s)> (<where>)` with `### In short`, `### Conflict` (where and when, effect, base vs target, conflicting files from `git merge-tree --write-tree --name-only --messages <target> HEAD`, **the cause**), `### Resolution` (commands, the choice and **why**, every commit before and after, every mistake and how it was caught, the force-push with the owner's yes), `### Verification` (no conflict marker, the branch's own change only, tests and checks on the new base, the CI and stage runs after), `### State left behind`, `### How to resume`.
2. **When the runs after the resolution pass**, add `## ✅ <date>: rebase conflict resolved` on top, with its evidence.
3. PROGRESS.md logs it in the step where it happened, with a link to STATUS.md.
4. **Never resolve in one chained call:** a script that rewrites a conflicted file is checked (`git diff --check`, `grep -c '^<<<<<<<'`) before `git add` and `git rebase --continue`, which run as separate commands.

## Mode `pause` — STATUS.md

Only when the owner pauses the ticket for some time. Not for an ordinary end of day.

1. Create or extend STATUS.md: who paused it, when, their words; the issue (what happens, cause, evidence); **the exact state left behind** (branch, commits pushed and local, uncommitted changes saved as a patch in `tests-evidences/`); how to resume, step by step; open questions.
2. PROGRESS.md: the current step becomes "⏸️ **Paused** (date) — see [STATUS.md](STATUS.md)", and its **Time** line gets the pause start. README.md says the same.
3. Nothing is pushed or run on a stage after the pause point.

## Mode `resume`

1. Read README.md, PROGRESS.md, and STATUS.md if present; re-read `AGENT.md` and `.claude/rules/`.
2. If STATUS.md exists: add `## ▶️ <date>: resumed — what changed since the pause` at the top and follow its "How to resume".
3. PROGRESS.md and README.md go back to the current status; the paused step's **Time** line closes the pause.
4. If the ticket has an open pull request: `pr-watch status` must list it with this session as owner; otherwise `pr-watch register <KEY>` (GIT-7). Then `pr-watch show <KEY>`.
