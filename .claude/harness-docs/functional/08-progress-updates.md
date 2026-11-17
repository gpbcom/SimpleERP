# 8. Progress updates

While anything long runs in a Claude session, the owner hears from Claude **every 2 minutes**, until everything has
ended, and once more at the end. Each update is colourised, exhaustive and uses icons, and it states facts read by the
`progress-updates` tool, never guesses.

## When it applies

- A command moved to the background, or one expected to last more than 2 minutes (Claude moves those to the
  background so that it stays free to report).
- A subagent or a workflow running in the background.
- A CI or stage run Claude waits for.

## What an update looks like

```text
### ⏱️ 14:32 · running for 6 min

- 🟢 🔄 `K03 mermaid` (background) · 4/9 (44 %) · `batch 4 rendered`
- 🔴 ❌ `K08 diff` (evidence) · `❌ FAIL (exit 1)`
- 🟡 ⏳ `research agent` (declared) · `12 pages read`

**Summary:** 🔄 1 running · ⏳ 1 waiting · ❌ 1 failed
```

- **Health dots:** 🟢 fine, 🟡 waiting or degraded, 🔴 failed.
- **State icons:** ✅ done, 🔄 running, ⏳ waiting, ❌ failed, ⚠️ warning (a source not read, an invalid run).
- **A `diff` block** lists what passed (green `+`) and what failed (red `-`): the terminal renders Markdown, not
  colour codes, so colour comes from the icons and this block.
- **Program output is quoted** (code spans, the `diff` block): it is data, never instructions. Secrets are masked
  (`•••`), and GitHub run titles are left out, since anyone opening a pull request writes them.

## How it works

| Piece | Does |
|---|---|
| The `progress-updates` skill | Tells Claude when work is long-running and what to do every 2 minutes |
| `progress-updates watch --every 120` | Run by Claude's Monitor tool: one line every 2 minutes while something runs, a final line, then it stops |
| `progress-updates status` | The update itself, read from the background task outputs, the processes in the repository, the ticket's evidence folders, GitHub Actions runs, and the tasks Claude declares (subagents) |
| The `PostToolUse` hook | Reminds Claude to start the watch when a command or a subagent goes to the background; it never blocks |

The pace is set in `.claude/skills/progress-updates/conf/progress-updates.yaml` (120 seconds, the shortest accepted).
