# CLAUDE.md

@AGENT.md

## Class layout

- **Async methods MUST always be declared after the sync methods**, within each banner section of a class: under
  "Internal Helpers Methods", the sync helpers then the async helpers; under "Publicly Exposed Methods", the sync
  public methods then the async ones (`AGENT.md`, "File shape"). `tests/conventions/` fails on a sync method declared
  after an async one of the same section.

## The harness

SimpleERP is an open-source, self-hosted, AI-native ERP (see `README.md`). Its Claude Code harness is versioned with
the code, in `.claude/`.

- **Specifications:** `docs/specs/`, in SimpleERP's own format: one page per item, each with its ID, in the shape of
  its template in `docs/specs/_templates/`. Features `02-functional/fNN-*/` (use cases, screens, business rules, data,
  flows), technical capabilities `03-technical/tNN-*/`, non-functional `05-non-functional/`, decisions
  `06-decisions/`, sectors `08-sectors/`, HTML mock-ups of every screen state in `04-ux/mockups/`. Design pages are in
  `docs/technical/`. A ticket states nothing the specifications or the roadmap do not state (TKT-8).
- **Roadmap:** `docs/specs/00-vision/roadmap/phases/`, one page per phase (P0 to P11) with its epics, sprints and
  tickets, and the ticket graph in `phases/gantt/ticket-graph.json`.
- **Tickets:** the roadmap's tickets, IDs `T<phase>.<nn>` (`T2.04`), are worked by an agent graph under the TKT rules
  (`.claude/rules/tickets.md`). `/ticket-plan <ID>` writes `docs/tickets/<ID>/TICKET.md` and a task graph in
  `PLAN.md`, then stops; the person approves the plan (`**Plan:** 🟢 Approved`); `/ticket-run <ID>` runs the waves in
  parallel worktrees, integrates, verifies, reviews, writes `EXPLAIN.md` and `IMPLEMENTATION.md` (TKT-14), then stops
  for the person's code review: nothing is committed or pushed until `PLAN.md` says `**Push:** 🟢 Approved` (TKT-18).
  The ticket is then committed once and its pull request to `develop` is merged by GitHub once CI passes (TKT-15).
- **Several tickets at once** (TKT-16): every running ticket works in the main checkout, on the shared branch
  `feature/tickets`, with its files in `docs/tickets/<ID>/`; each commits only its own files when it finishes.
  `/ticket-run` checks the start rule first (prerequisites done, no open ticket on the same areas).
  `python3 .claude/scripts/tickets/tickets.py list|prune` shows the open tickets and, once all is merged, goes back to
  `develop`.
- **Issues and groups** (TKT-20): `/issue-plan <refs>` plans an issue with its child issues, or a group (`#12`,
  `T2.04`, `E2.1`, `P2`); the person approves it with `python3 .claude/scripts/tickets/tickets.py approve <refs>`;
  `/issue-run <refs>` runs it as fast as the start rule allows.
- **Front ends** (TKT-21): a ticket that changes `frontend/` lists in "Screens touched" every screen it builds, as links
  to the screen pages `S-F<n>-MM` of the specifications, and its plan has a Playwright task in `frontend/<app>/e2e/`.
- **Board** (TKT-17): the GitHub project **SimpleERP roadmap** holds one issue per phase, epic and ticket, in columns
  📥 Backlog, ✅ Ready, 📝 Planned, 🔄 Running, 👀 In review, 🏁 Done. The workflows move the cards; `/board` or
  `python3 .claude/scripts/github/board.py show` prints it, and the status line shows the open tickets and the counts.
- **Customer issues:** the only issues outside the roadmap. A customer's request is labelled `USER-FEATURE-REQUEST` or
  `USER-REPORTED-BUG` (issue forms of `.github/ISSUE_TEMPLATE/`); one created by an agent carries
  `needs-maintainer-approval` and stays in Backlog until a maintainer removes it.
- **GitFlow** (TKT-15, TKT-25): the repository is `gpbcom/SimpleERP`. `develop` and `master` change only through pull
  requests; work happens on `feature/`, `bugfix/`, `release/` and `hotfix/` branches. The git hooks of `.githooks/`
  (`python3 .claude/scripts/tickets/tickets.py setup`, once per clone) and `.claude/hooks/guard_git.py` enforce it.
  `tickets.py branches` gives every branch its verdict; only a 🌱 live branch is rebased onto `develop`. No commit or
  push is made outside the harness unless the person asks.
- **Releases** (TKT-26): `/release` starts `.github/workflows/release.yml` on `develop`; every suite runs, the
  changelog, release notes and test reports are written on `release/<version>`, and `automerge.yml` merges it into
  `master`, tags it, publishes it and brings it back to `develop`. No commit or merge by hand.
- **Agents:** `.claude/agents/` (planner and reviewer on opus, workers on sonnet, mechanical work on haiku, TKT-7);
  workflows in `.claude/workflows/`.
- **Progress every 2 minutes** (TKT-9): when a ticket workflow starts, arm the Monitor tool with
  `python3 .claude/scripts/reports/progress.py watch --every 120 --run <run id>` and relay each report in full.
- **Clean up after yourself** (TKT-27): every run removes the temporary files, folders and worktrees it makes,
  even when it fails; `checks.py` removes what a killed run left before it makes its own clean tree, and pytest
  keeps its temporary files with that tree. An agent removes its own scratch worktrees, branches and files when
  its work is done.
- **Rules that hold** (TKT-22 to TKT-24): every rule names its enforcers in `.claude/rules/enforcement.json`; "done"
  is defined once; harness scripts run in a shallow CI checkout. **A gap found in the harness is closed with the fix,
  a test that fails without it, and the rule with its enforcers.**
