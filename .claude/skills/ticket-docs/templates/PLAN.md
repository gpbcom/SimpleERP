# Plan — <KEY>: <TITLE>

Written <DATE>. **Takes precedence over [IMPLEMENTATION.md](IMPLEMENTATION.md).** Ticket and acceptance criteria: [TICKET.md](TICKET.md). Progress: [PROGRESS.md](PROGRESS.md). Tests: [TESTS-CATALOG.md](TESTS-CATALOG.md). Risks, questions and decision log: [EXPLAIN.md §6](EXPLAIN.md#6-limitations-risks-and-out-of-scope).

**Status:** only step 0a (this documentation folder) is done. The implementation starts on the owner's go.

## Context

<What the ticket asks, per topic, in plain words; what exists today (file:line on the base commit); the constraints.>

### Decisions

| # | Decision |
|---|---|
| D1 | <decision> (the owner, <DATE>) |
| D2 | (Proposed) <decision proposed by Claude; its justification is in [IMPLEMENTATION.md §1](IMPLEMENTATION.md#1-implementation-choices)> |

## What the screenshots need: already available vs to compute

<UI tickets only; otherwise delete this section.>

| Image | Element | Already in the API | Computed by the back end | Computed by the front end |
|---|---|---|---|---|
| <n> | <label / figure> | <field path or —> | <what> | <what> |

### Formulas per filter

<Each % and amount, its formula, and the mockup figures recomputed for each filter; mismatches → EXPLAIN §6.2 questions.>

## Acceptance criteria → unit tests → validation

The criteria are defined in [TICKET.md](TICKET.md#acceptance-criteria); the tests in [TESTS-CATALOG.md](TESTS-CATALOG.md).

| AC | Unit tests | Other tests | Validation (level, where) | Evidence (planned folder) |
|---|---|---|---|---|
| AC1 | <IDs> | <Playwright, Bruno, stage IDs> | <unit + 🟦 dev and 🟪 QA stage run> | `tests-evidences/<stage>-<date>-<check>/` |
| AC<n> | — | — | **Out of scope (Dn)**, never PASS | — |

## Ticket folder first: `docs/tickets/<KEY>/`

Step 0a writes TICKET, PLAN, IMPLEMENTATION, TESTS-CATALOG, TESTS-NOTICE, EXPLAIN (skeleton + §6), PROGRESS, README, `attachments/` and `tests-evidences/README.md` before any branch, test or code.

## Development rules enforced

[AGENT.md](../../../AGENT.md) and the files of `.claude/rules/` are re-read at step 0b, before every commit and at the final step; the version read at that moment applies: [coding-style.md](../../../.claude/rules/coding-style.md), [git-rules-and-deploy.md](../../../.claude/rules/git-rules-and-deploy.md), [ticket-documentation.md](../../../.claude/rules/ticket-documentation.md), [testing.md](../../../.claude/rules/testing.md), [rule-proposals.md](../../../.claude/rules/rule-proposals.md). Every PROGRESS.md step entry ends with a **Rules** line.

| ID | How it applies | Check (exact command or script) | When |
|---|---|---|---|
| CS-1 | <what is extended / reused instead of copied> | <the searches run, and what they found> | before each commit |
| <ID> | Not applied: <reason> | — | — |
| G02 (ticket check) | The diff holds exactly the files of [IMPLEMENTATION.md §0](IMPLEMENTATION.md#0-files-modified--exact-list) | `git diff --name-only origin/develop` compared with §0 | local checks, final step |

## Files modified

**The exact list is [IMPLEMENTATION.md §0](IMPLEMENTATION.md#0-files-modified--exact-list).** In short:
- <project>: <n> new, <n> modified, <n> deleted.
- Checked, unchanged: <projects>.

## Steps

**Step 0a — documentation folder** (this session).

**Step 0b — setup:** branch `feature/<KEY>-<slug>` (or `bugfix/`, GIT-8) from `origin/develop` at `<base commit>`, issue → **In progress** on the board, baselines (unit count, conventions), rules re-read.

**Step 1 — <name>:** <what changes>. TDD (TEST-7): tests <IDs> committed alone → 🔴 red run → code → 🟢 green run. Done when <condition>.

**Step <n> — Out of scope (Dn):** <kept, labelled; not done>.

**Step <n> — local checks:** ruff, mypy, `tests/conventions`, the CS checks in scope, DEP-1, G02 (diff vs IMPLEMENTATION §0), each recorded with `ticket-docs record-run`.

**Step <n> — 🟦 dev stage:** `gh workflow run stage.yml --ref <branch> -f stage=dev -f ref=<sha>` (smoke, Bruno, Playwright `@smoke`), DEP-3 on its log, `ticket-docs record-run --run-id`.

**Step <n> — 🔬 requirements audit:** on the stage running the final commit, every requirement of TICKET.md checked on the seeded data, `develop` vs the branch (template `REQUIREMENTS-AUDIT.md`) → `tests-evidences/dev-<date>-requirements-audit/REPORT.md`. Every 🔴 / 🟠 finding fixed, or named in the PR description and EXPLAIN §6, before the QA run.

**Step <n> — 📚 documentation (DOC-2):** project-docs `update`; `project-docs check --ticket <KEY>` prints nothing.

**Step <n> — 📝 release note (DOC-3):** release-notes `ticket`; `release-notes check --ticket <KEY>` prints nothing.

**Step <n> — 🟪 QA stage (GIT-6):** once the pull request is open and every earlier step is ✅: `gh workflow run stage.yml --ref <branch> -f stage=qa -f ref=<sha>`, approved by the owner; full Playwright, Bruno, upgrade test, DEP-3; the run announced on the pull request.

**Step <n> — final acceptance run and hand-over:**
1. Every level on the final commit.
2. PROGRESS.md "Acceptance criteria — final verification".
3. EXPLAIN.md complete (DOC-1 check prints nothing).
4. History bundle, squash into one commit (GIT-4) and push, each on the owner's yes (GIT-1); pull request with a description of 10 lines at most and `Closes #<n>`, recorded in PROGRESS.md (GIT-5); `pr-watch register <KEY>` (GIT-7); issue → In review (GIT-3).
5. QA stage run (GIT-6), then `ticket-docs archive <KEY>` (TEST-9).

## Out of scope

- <item> (Dn).

## Verification

- **Each code step:** <compile, lint, the step's test IDs green, unit count ≥ previous>; PROGRESS.md and the catalog State column updated before moving on.
- **End to end:** every PASS links to a `tests-evidences/` folder; a run whose environment failed is marked invalid and re-run.
