---
name: ticket
description: Open, plan, run or review a roadmap ticket of SimpleERP (TKT rules). Use it to fill the ticket template, check a TICKET.md or a PLAN.md, split a ticket into a task graph, start the agents in their own worktrees, verify and review the work, then, once the person approves the push, commit it once and open its pull request to develop. Load it with .claude/rules/tickets.md.
---

# Roadmap tickets

A ticket is a roadmap item of `docs/specs/00-vision/roadmap/phases/`, worked by an agent graph. The rules are in
[`.claude/rules/tickets.md`](../../rules/tickets.md) (TKT rules). This page says how to use them. It does not copy them.

A ticket refers to the specifications of `docs/specs/` by their IDs, as the page titles write them: `UC-F6-01`,
`S-F6-01`, `BR-F6-01`, `E-F6-01`, `FL-F6-01`, `REQ-T01-01`, `D438`. Each links to its page, the ID in the link text:
`[📝 UC-F6-01: Capture and qualify a lead](../../specs/02-functional/f06-customers-and-sales/use-cases/01-lead-to-quote/uc-f06-01-capture-and-qualify-a-lead.md)`.
`scripts/spec_ids.py <ID>` prints the page of an ID. The design pages it builds on are in `docs/technical/`.

## The steps

| Step | Command | What runs | Result |
| --- | --- | --- | --- |
| 1. Plan | `/ticket-plan <ID>` | ticket-writer writes `TICKET.md`, `check_ticket.py` checks it, planner writes `PLAN.md`, scribe writes the files, `check_plan.py` checks the graph | `PLAN.md` with `**Plan:** 🟡 Awaiting approval`. The run stops there. |
| 2. Approve | Edit the status line | Nothing runs | `**Plan:** 🟢 Approved`. The person does this, and only the person. |
| 3. Run | `/ticket-run <ID>` | `check_plan.py` as a gate, then the waves in worktrees, the integrator, the verifier, the reviewer, the explainer | `EXPLAIN.md`, `IMPLEMENTATION.md` and `REVIEW.md` written, the work still uncommitted, `**Push:** 🟡 Awaiting code review` in `PLAN.md`. The run stops there. |
| 4. Code review | Edit the push line | Nothing runs | `**Push:** 🟢 Approved`, once the person has reviewed the code (TKT-18). The person does this, and only the person. |
| 5. Push | `/ticket-run <ID>` again | The checks again, then `ticket_tree.py finish` | One commit holding only this ticket's files, pushed, with the pull request to `develop` (label `automerge`); GitHub merges it once CI passes (TKT-15). |

`/ticket-run` refuses any status other than `🟢 Approved`. It skips the tasks already integrated
(`ticket_tree.py status`), so a re-run continues where it stopped (TKT-11).

### Plan

- `TICKET.md` is written by the **ticket-writer** from the specifications and the roadmap only (TKT-2). It is checked
  by `check_ticket.py`, and fixed at most twice. The plan stops when `TICKET.md` links no specification page.
- `PLAN.md` is written by the **planner** (opus). It holds a table and a ` ```json ` block of tasks (TKT-3). It is
  checked by `check_plan.py`.

### Approve

Change the status line of `PLAN.md` from `**Plan:** 🟡 Awaiting approval` to `**Plan:** 🟢 Approved`. A change to an
approved brief or check is approved again and recorded in 📝 Events before the re-run (TKT-11).

### Run

- **Gate:** `check_plan.py` runs again, then the start rule `tickets.py check` (TKT-16): every prerequisite merged on
  `origin/develop`, no open ticket on the same areas, no field ticket before its campaign. `/ticket-run <ID> --force`
  starts anyway on the person's decision.
- **One checkout for every ticket (TKT-16):** `ticket_tree.py prepare` puts the main checkout on `feature/tickets`,
  the branch every running ticket shares (from `origin/develop` when no other ticket runs), and records the ticket's
  own files, starting with `docs/tickets/<ID>/`. Several tickets run at once, each touching only its own files. The
  card moves to 🔄 Running (TKT-17).
- **No intermediate commit (TKT-5):** the ticket's work stays uncommitted in its home until the ticket is done.
- **Waves:** each task runs in its own git worktree. It starts with `ticket_tree.py start` (moves to the ticket's
  commit and copies the uncommitted work in) and ends with `ticket_tree.py handoff` (saves its own changes as a patch).
  At most 8 agents run at once per ticket (TKT-4).
- **Integrator:** after each wave, applies the wave's hand-offs to the home in task order with `ticket_tree.py
  integrate`.
- **Verifier:** runs `checks.py` for the ticket, in its home. A failure goes back to the agent that owns the files, at
  most twice. A failure flagged `environment` goes to nobody: the run stops and the person fixes the environment
  (TKT-6).
- **Reviewer:** reviews the diff against `TICKET.md`, the specifications and the rules. Only blocking findings go back to
  the fixers (TKT-12). The note is written to `REVIEW.md`.
- **Explainer:** writes `EXPLAIN.md` (how it works, files and lines changed) and `IMPLEMENTATION.md` (each choice
  against its alternatives, with the trade-off) from the workers' decisions and the diff (TKT-14), beside the scribe.
- **Code review by the person (TKT-18):** the run stops before any commit, with `**Push:** 🟡 Awaiting code review`
  in `PLAN.md`. The person reviews the uncommitted code in the ticket's home, changes the line to
  `**Push:** 🟢 Approved` and runs `/ticket-run <ID>` again: the checks run again, then the commit and the push.
- **Commit and pull request (TKT-15):** after the person's code review (TKT-18), the integrator runs `ticket_tree.py
  finish`: one commit on `feature/tickets` holding **only this ticket's files**, pushed, with the pull request of
  `feature/tickets` to `develop` opened or updated (one `Closes #<issue>` per ticket, label `automerge`). The card moves
  to 👀 In review. GitHub merges it once CI passes, the issue closes and the card moves to 🏁 Done.

### Several tickets at once, and groups of issues (TKT-16, TKT-20)

| Command | Does |
| --- | --- |
| `/issue-plan <refs>` | Plans every ticket of an issue with its child issues, or of a group: `#12` (a ticket, an epic or a phase issue), `T0.10`, `E0.4`, `P1`, several at once |
| `python3 .claude/scripts/tickets/tickets.py approve <refs>` | The person's approval of every plan of the group that passes `check_plan.py` (Claude asks first) |
| `/issue-run <refs>` | Runs the approved tickets of the group, every one the start rule allows at once, the others as soon as they may |
| `python3 .claude/scripts/tickets/tickets.py resolve <refs>` | The tickets of a group, in order, with their state and what they wait for |
| `python3 .claude/scripts/tickets/tickets.py watch <refs>` | The group's report every 2 minutes, with `▶️ CAN START <ID>` lines |
| `python3 .claude/scripts/tickets/tickets.py list` | Every open ticket: the files it owns and its areas |
| `python3 .claude/scripts/tickets/tickets.py prune` | Once everything is merged, puts the main checkout back on `develop`, then deletes every merged, integrated or superseded branch and worker worktree after a backup bundle (TKT-25) |
| `python3 .claude/scripts/tickets/tickets.py branches` | Every branch with its verdict: 🔒 protected, 🔄 open, 🧹 delete, 🌱 live (the only ones to rebase) |
| `python3 .claude/scripts/github/board.py show` or `/board` | The Kanban board in the terminal (TKT-17) |

## Templates

| Template | Used for |
| --- | --- |
| [`templates/TICKET.md`](templates/TICKET.md) | The ticket: roadmap links, what it delivers, the specifications it builds on, acceptance criteria, out of scope |
| [`templates/REVIEW.md`](templates/REVIEW.md) | The reviewer's note for the person: verdict, what changed, acceptance criteria |
| [`templates/EXPLAIN.md`](templates/EXPLAIN.md) | How the delivered work works, step by step, with the files and lines changed |
| [`templates/IMPLEMENTATION.md`](templates/IMPLEMENTATION.md) | Each implementation choice against its alternatives, with the trade-off |

## Scripts

| Script | Usage | What it checks |
| --- | --- | --- |
| `scripts/check_ticket.py` | `python3 .claude/skills/ticket/scripts/check_ticket.py <ID>` | `TICKET.md` against the template and `docs/specs/`: IDs, links, sections, screens (TKT-21) |
| `scripts/check_plan.py` | `python3 .claude/skills/ticket/scripts/check_plan.py <ID> [--min-parallel N]` | The task graph of `PLAN.md`: ids, agents, dependencies, files, waves, the Playwright task of the screens (TKT-21) |
| `scripts/spec_ids.py` | `python3 .claude/skills/ticket/scripts/spec_ids.py <ID>...` | Prints the page of each specification ID, or `unknown` |
| `.claude/scripts/tickets/checks.py` | `python3 .claude/scripts/tickets/checks.py --ticket <ID> [--base develop]` | Every applicable check of the code and the specifications, with the verdict in JSON |
| `.claude/scripts/tickets/ticket_tree.py` | `python3 .claude/scripts/tickets/ticket_tree.py <command> --ticket <ID>` | The uncommitted work: `prepare`, `status`, `start`, `handoff`, `integrate`, `diff`, `changes` (the files and lines table of `EXPLAIN.md`), `docs` (every file and line of `EXPLAIN.md` and `IMPLEMENTATION.md` is a working clickable link), `finish` (the single commit, refused while `docs` finds a problem) |
| `.claude/scripts/reports/progress.py` | `python3 .claude/scripts/reports/progress.py watch --every 120 --run <run id>` | The progress report of a run, every 2 minutes (TKT-9) |
| `.claude/scripts/reports/progress.py` | `python3 .claude/scripts/reports/progress.py timings --ticket <ID> --write` | Elapsed time and tokens in `PROGRESS.md` (TKT-10) |

The scripts print nothing when all is well, except `checks.py`, `progress.py` and `ticket_tree.py`, which print their report.

## Hooks

Hooks are registered in [`.claude/settings.json`](../../settings.json).

| Hook | Event | What it does | Catalogue |
| --- | --- | --- | --- |
| `.claude/hooks/format_edited.py` | After each Edit, Write or MultiEdit | Formats the one file just changed | [`.claude/hooks/formatters.json`](../../hooks/formatters.json) |
| `.claude/hooks/check_touched.py` | When a worker agent stops | Runs the checks of the layers of the worker's own changes (since `ticket_tree.py start`), and hands the task back on failure, at most twice | [`.claude/hooks/layer-checks.json`](../../hooks/layer-checks.json) |

The hooks do nothing outside a linked worktree, so the main checkout is never checked by them.

## Agents

| Kind of task | Agent |
| --- | --- |
| Python (`backend/`, `plugins/`, `sdk/`, `packs/`) | `implementer` |
| Front end (`frontend/`) | `frontend-implementer` |
| Tests, Playwright tests of the screens in `frontend/<app>/e2e/` included (TKT-21) | `test-writer` |
| Documentation (`README.md`, `docs/functional/`, `docs/technical/`) | `doc-writer` |
| Review | `reviewer` |
| `EXPLAIN.md` and `IMPLEMENTATION.md` | `explainer` |

The other agents, `planner`, `ticket-writer`, `integrator`, `scribe` and `verifier`, are in
[`.claude/agents/`](../../agents/). Their models are fixed by TKT-7.

## Rules

Read [`.claude/rules/tickets.md`](../../rules/tickets.md) before planning or running a ticket. Code follows the
repository's [`AGENT.md`](../../../AGENT.md) and [`.claude/rules/coding-style.md`](../../rules/coding-style.md); tests
follow [`.claude/rules/testing.md`](../../rules/testing.md). The specifications of `docs/specs/` are read-only for a
ticket.
