# 6. PR watcher

Once a ticket's pull request is open, the PR watcher keeps an eye on it, so you do not have to. When something needs
work, it brings it back to **the ticket's own Claude session** (GIT-7), the one that holds the ticket's context.

## What it watches

Every 10 minutes on working days, 08:00 to 19:50 (a `systemd --user` timer), for each registered open pull request:

| Event | When |
|---|---|
| `rebase_conflict` | The branch no longer merges cleanly into its base (`develop` or `master`), tried in memory |
| `checks_failed` | A CI check of the pull request's commit failed (one event per commit, listing every failure) |
| `stage_failed` | The dev or QA stage run of the commit failed |
| `changes_requested` | A reviewer's latest review asks for changes (a later approval clears it) |
| `review_comments` | New review or conversation comments, except the author's own replies |
| `qa_waiting` | A QA run has waited more than 30 minutes for its approval |

## What you see

| You see | Do |
|---|---|
| A VS Code tab with the ticket's session and `/pr-watch GH-<n>` typed | Press **Enter** |
| A desktop notification "type /pr-watch GH-<n> in its terminal session" | Type it in that terminal |
| The same notification an hour later | Press Enter in the session, or `pr-watch ack GH-<n>` to silence it |

Then Claude reads the events, fixes what its session owns (tests first), logs it in PROGRESS.md, and **stops before
any squash or push** to ask you (GIT-1). The prompt hook also hands the waiting events to the session whenever you
type in it.

## What it never does

- Push, rebase or change a working tree. It fetches into `refs/pr-watch/*` only.
- Act in another session, a new one or a headless one.
- Run on a real pull request from a test.

## Commands

```bash
.claude/skills/pr-watch/bin/pr-watch status            # every watched pull request, its session and waiting events
.claude/skills/pr-watch/bin/pr-watch show GH-<n>       # what it found
.claude/skills/pr-watch/bin/pr-watch register GH-<n>   # from the ticket's session, right after opening the pull request
.claude/skills/pr-watch/bin/pr-watch install-units     # once per machine, then: systemctl --user enable --now claude-pr-watch.timer
```

The overview of every watched pull request is generated in `docs/tickets/pull-request-summary/README.md`.
