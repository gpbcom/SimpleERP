# 2. Configuration and hooks

## `.claude/settings.json` (project scope, versioned)

| Event | Matcher | Command | Does |
|---|---|---|---|
| UserPromptSubmit | | `pr-watch-hook` | Adds the waiting PR-watcher events of this session's tickets to the prompt |
| PreToolUse | Bash | `ai-cost gate` | Denies a paid AI command outside `ai-cost run`, `raise-cap`, and commands setting `AI_COST_*` |
| PreToolUse | Bash | `ticket-docs git-gate` | Denies production code committed before its red run (TEST-7), and commits or pushes on `master`/`develop` (GIT-8) |
| PostToolUse | Bash | `ticket-docs time-reminder` | After a commit on a ticket branch, asks to update PROGRESS.md's times |

Every command is `"$CLAUDE_PROJECT_DIR"/.claude/skills/.venv/bin/<tool> …` with a 10 s timeout: the venv's entry points answer in
250 to 330 ms, the `bin/` wrappers (which go through `uv run`) in 400 to 460 ms. A hook prints its JSON answer or
nothing. The two hooks that only inform (`pr-watch-hook`, `time-reminder`) end with `|| true`; the two gates do not, and
the cost gate fails closed when its own settings file is unreadable. A fresh clone needs `uv sync` in `.claude/skills/`
before the hooks work: until then Claude Code reports them as failing, without blocking. The user-level `~/.claude/settings.json` is not touched.

## Catalogues (versioned, never in code)

| File | Holds |
|---|---|
| `ticket-docs/conf/github.yaml` | Owner, repository, branches, the board's IDs and Status options |
| `project-docs/conf/doc-map.yaml` | Changed paths → documentation chapters |
| `release-notes/conf/changelog-types.yaml` | Fragment types, their headings and semantic-version bumps |
| `pr-watch/conf/watch.yaml` | Timings (10 min runs, 60 min renotify, 30 min QA wait), GitHub settings |
| `ai-test-cost/conf/settings.yaml` | Cap ($20), kill ratio (90 %), usage source, files: never overridable from the environment |
| `ai-test-cost/conf/prices.yaml`, `paid-commands.yaml` | Model prices (source and date inside), paid command patterns |

## Environment variables

| Variable | Read by | For |
|---|---|---|
| `CLAUDE_PROJECT_DIR` | hooks | The repository root |
| `CLAUDE_CODE_SESSION_ID`, `CLAUDE_PID`, `CLAUDE_CODE_ENTRYPOINT` | pr-watch | The session to register and how to reach it |
| `<TOOL>_CALLER_CWD` | each tool | The caller's folder (set by its wrapper) |
| `GITHUB_TOKEN` | pr-watch, release-notes | A token; otherwise `gh auth token` is read at use time, never stored |
| `PR_WATCH_*` | pr-watch | Paths only (state folder) |
| `ANTHROPIC_ADMIN_KEY`, `AI_COST_API_KEY_ID` | ai-test-cost | The usage report; the key is never logged |
| `AI_COST_RUN_ID`, `AI_COST_TICKET` | `tests/conftest.py` | Set by `ai-cost run` for its child: an `llm` test without them fails |
