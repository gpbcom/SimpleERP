---
name: pr-watch
description: Handle what the PR watcher found on a ticket's open GitHub pull request (rebase conflict with its base, failed checks, a failed dev or qa stage deployment, changes requested, new review comments, a qa approval waiting too long), in the ticket's own Claude session, with the ticket documentation and the rules; register a ticket's pull request with its session; read or refresh the summary page docs/tickets/pull-request-summary/README.md. Use when the prompt is `/pr-watch GH-<n>` (the watcher typed it after reopening the session), when the UserPromptSubmit hook hands over "PR watcher" events, right after a ticket's pull request is opened (register it), or when asked about the watched pull requests.
---

# PR watch: fix a ticket's pull request in the ticket's own session

A background watcher (`pr-watch once`, a systemd user timer, every 10 minutes on working days from 08:00 to 19:50) checks every registered open pull request on GitHub: a rebase on its base branch (`develop` or `master`) tried in memory, the check runs and CI runs of its head commit, the latest `dev` and `qa` deployments of that commit, the reviews and comments, and a `qa` approval that waits too long. A new problem goes into the ticket's inbox, and the ticket's own session is reopened in VS Code with `/pr-watch GH-<n>` typed: **the person presses Enter**. A session open in a terminal is only notified. Nothing ever runs in another session (GIT-7).

Every command below is `pr-watch`, which is `.claude/skills/pr-watch/bin/pr-watch` in the repository.

## When the prompt is `/pr-watch GH-<n>`

1. **Read the events:** `pr-watch show GH-<n>` (the prompt hook also hands them over). Each has a kind, a title, a link and an excerpt.
2. **Take them:** `pr-watch ack GH-<n>` (or `pr-watch ack GH-<n> <event-id> ...` for some of them). Taken events are no longer handed over or reminded.
3. **Load the rules and the ticket:** the `ticket-docs` skill (resume the ticket folder `docs/tickets/GH-<n>/`), `git-deploy-rules`, `coding-style-rules`, `testing-rules`, and `ai-test-cost` before any test that calls a paid AI. The rules themselves are in `.claude/rules/`.
4. **Handle each kind:**

   | Kind | What to do |
   |---|---|
   | `rebase_conflict` | Write the conflict entry in STATUS.md **first** (ticket-docs rule), then rebase the branch on `origin/<base>` (the base the event names, `develop` or `master`), resolve, run the tests, and log it in PROGRESS.md with times. `pr-watch log GH-<n> rebased "<files resolved>"`. |
   | `checks_failed` | Open the run linked by the event. Reproduce locally and fix with TDD: the failing test first (TEST-7). A dependency error is a failure. `pr-watch log GH-<n> fixed "<what>" --link <commit>`. |
   | `stage_failed` | Open the deployment or the `stage.yml` run. Find whether the commit or the stage is at fault; fix the code with TDD, or report a stage problem to the person. Never start a new stage run before the fix is pushed. |
   | `changes_requested` | Hand over to the **pr-review-followup** skill, which verifies and triages every remark of the review. |
   | `review_comments` | Hand over to **pr-review-followup** as well: each new comment is verified, answered or fixed. Comments of the pull request's own author are never events. |
   | `qa_waiting` | The `qa` deployment waits for its reviewer's approval. Tell the person: approving is theirs, not the session's. |

5. **Stop before squash and push** (GIT-1): tell the person what is ready, `pr-watch log GH-<n> waiting_push "<commit>"`, and wait for an explicit yes. The branch stays one squashed commit (GIT-4). After the push, `pr-watch log GH-<n> pushed "<old> -> <new>"`. The QA run starts only once every earlier step is ✅ with its evidence (GIT-6): `gh workflow run stage.yml -f stage=qa -f ref=<sha>`, then `pr-watch log GH-<n> qa_started "<run URL>"`.

Each `ack` and `log` writes the summary page again.

## Register a ticket's pull request

Right after the pull request is opened (or when resuming a ticket whose pull request is not watched), in the ticket's session:

```bash
pr-watch register GH-<n>                  # the link from the "Pull request" section of docs/tickets/GH-<n>/PROGRESS.md
pr-watch register GH-<n> --link <url>     # a link not in PROGRESS.md yet: https://github.com/<owner>/<repo>/pull/<number>
pr-watch register GH-<n> --no-session     # notifications only, no session to reopen
```

The session comes from `CLAUDE_CODE_SESSION_ID`, which Claude Code exports to every command (or `--session <id>`). The ticket folders are read in the main working tree of the repository, so registering from a worktree works too. Registering again changes the owner session and keeps what the watcher learnt.

`pr-watch backfill` proposes a session for every ticket folder whose pull request nobody watches (from the titles of the Claude Code transcripts). `pr-watch backfill --apply` registers the proposals: only on the person's go.

## Other commands

| Command | Use |
|---|---|
| `pr-watch status` | Every watched pull request, its state, owner session and waiting events. |
| `pr-watch render` | Write the summary page again. |
| `pr-watch once` | One watcher run, the timer's command. **Never run it by hand on real tickets without the person's go**: it reads GitHub, reopens sessions and shows notifications. |
| `pr-watch install-units` | Copy the systemd units to `~/.config/systemd/user/`. Enabling the timer stays the person's decision: `systemctl --user import-environment DISPLAY WAYLAND_DISPLAY DBUS_SESSION_BUS_ADDRESS` once per login, then `systemctl --user enable --now claude-pr-watch.timer`. |
| `pr-watch hook-inbox` | The `UserPromptSubmit` hook: it prints the hook JSON with the session's waiting events, or nothing, and always exits 0. |

## What the watcher detects

| Kind | When | Raised once per |
|---|---|---|
| `rebase_conflict` | `git merge-tree` of the head on the base finds conflicts, or the probe could not run and GitHub says `dirty` | head commit |
| `checks_failed` | a check run or a CI workflow run of the head commit failed, was cancelled, timed out or could not start | head commit, every failure listed |
| `stage_failed` | the latest `dev` or `qa` deployment of the head commit is `failure` or `error`, or else a `stage.yml` run of it failed | deployment, or run |
| `changes_requested` | a reviewer's latest decisive review asks for changes | review |
| `review_comments` | a review text, a line comment or a conversation comment written after the last run, by someone else than the author | comment |
| `qa_waiting` | a `qa` deployment has waited for its approval for longer than `qa_wait_minutes` (30) | waiting run |

The first read of a pull request's comments only sets the cursors, so older comments are never replayed. The timings and the GitHub settings are in `conf/watch.yaml`.

## Rules of the mechanism

- **Only the ticket's own session acts on its pull request** (GIT-7). The watcher never resumes a session that is open: two writers would mix one transcript.
- **The watcher never pushes, never rebases, never changes a working tree.** Its rebase probe fetches into `refs/pr-watch/*` only, never `refs/remotes/origin/*` (which `--force-with-lease` leases on), and merges in memory.
- **The GitHub token is read when needed** (`GITHUB_TOKEN`, else `gh auth token`), kept in memory, never logged or written.
- **No live test on tickets:** the watcher is tested with a GitHub stand-in, a git sandbox and recording programs (`tests/`), never by running it on a real ticket.
- State: `~/.local/state/claude-pr-watch/` (or `PR_WATCH_STATE_DIR`): `registry.json`, `state.json`, `inbox/GH-<n>.json`, `operations.jsonl` and the log `pr-watch.log`.
- The summary page `docs/tickets/pull-request-summary/README.md` is local (ignored by git) and generated: never edit it by hand. Its cost column reads the ai-test-cost ledgers in `~/.local/state/ai-test-cost/` (or `AI_COST_STATE_DIR`).
