# 🔀 Pull requests: summary

> Written by the `pr-watch` skill (`.claude/skills/pr-watch`) after every watcher run and every operation a ticket session logs. Do not edit it by hand: the next run overwrites it. The details of each operation are in the ticket's `PROGRESS.md`.

**Last checked:** ${last_checked} · **Next check:** ${next_check} · **Watched:** ${open_count} open · ${merged_count} merged · ${closed_count} closed

**Now:** ${status_counts}

**Status:** 🟢 green · 🔀 conflicts with its base · 🔧 checks failed · 🚧 stage deployment failed · ✍️ changes requested · ⚠️ could not be checked

**Checks and stages:** ✅ passed · ❌ failed · 🔄 running · ⬜ replaced · ❔ no status yet · 🟦 dev · 🟪 qa

**Handling:** ⏳ waiting for you (press Enter on `/pr-watch <KEY>` in the Claude tab) · 🔄 taken by the ticket's session · — nothing to do

**Events:** 🔀 rebase conflict · 🔧 checks failed · 🚧 stage failed · ✍️ changes requested · 💬 review comments · 🟪 qa approval waiting

**Operations:** 📝 registered · 🔎 detected · 📨 session reopened · 🔔 notified · 🔄 taken by the session · 🔁 rebased · 🛠️ fixed · ⏳ waiting for push approval · 🚀 pushed · 🟪 QA run started · ✅ merged · 🚫 closed · ⚠️ warning · 💬 note

**💰 AI cost:** what the ticket's AI tests cost so far, against its cap (`ai-test-cost` skill). ⛔ the cap stopped them.

Times are local, `YYYY-MM-DD HH:MM`.

## Ongoing pull requests

| Status | Ticket | Pull request | Branch | Checks | Stages | Review | Handling | 💰 AI cost | Session | Opened | Last operation |
|---|---|---|---|---|---|---|---|---|---|---|---|
${ongoing_rows}

## Open pull requests nobody watches

Open pull requests of the watched repositories with no ticket session registered. Run `pr-watch register <KEY>` in the ticket's session to watch one.

| Pull request | Ticket | Title | Updated |
|---|---|---|---|
${unwatched_rows}

## Operations

Newest first, the last ${operations_shown}.

| Time | | Ticket | Pull request | Operation |
|---|---|---|---|---|
${operation_rows}

## ✅ Merged pull requests

| Ticket | Pull request | Opened | Merged | Time to merge | Watcher events | 💰 AI cost |
|---|---|---|---|---|---|---|
${merged_rows}

## 🚫 Closed pull requests

| Ticket | Pull request | Opened | Closed | Open for | Watcher events | 💰 AI cost |
|---|---|---|---|---|---|---|
${closed_rows}
