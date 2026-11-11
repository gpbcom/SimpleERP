# 4. The tools

Seven Python packages in one uv workspace, `.claude/skills/` (`pyproject.toml`, `uv.lock`, `.venv`). Each follows
`AGENT.md` (layers `api → service → storage → models`, one class per file, Pydantic models with per-field validators,
file-only logging) and was written tests first. Each tool has a `bin/<tool>` wrapper for people and skills
(`uv run --project .claude/skills --frozen`), and a console script in `.claude/skills/.venv/bin/` for the hooks.

| Package | Command | Commands |
|---|---|---|
| `harness-core` | | Shared: `Runnable`/`AsyncRunnable`, `GitRepository`, `BranchName` (GitFlow), `ShellCommandSplitter`, GitHub REST client, `MarkdownText`, `YamlCatalog`, `HarnessLogging`, test stand-ins (`GitSandbox`, `FakeProgram`, `GithubFake`) |
| `ticket-docs` | `ticket-docs` | `record-run`, `check`, `report-index`, `history-bundle`, `archive`, `board`, `git-gate`, `time-reminder` |
| `project-docs` | `project-docs` | `map`, `check` |
| `release-notes` | `release-notes` | `check`, `next-version`, `build`, `release-body` |
| `pr-watch` | `pr-watch`, `pr-watch-hook` | `once`, `register`, `backfill`, `show`, `ack`, `log`, `status`, `render`, `install-units`, `hook-inbox` |
| `ai-test-cost` | `ai-cost` | `run`, `status`, `remaining`, `charge`, `raise-cap`, `gate` |
| `cve-scan` | `cve-scan` | One scan: OSV-Scanner and Trivy when installed, merged findings |

## ticket-docs

- **`record-run`** runs a command and writes its evidence folder: the README (command, full commit, kind, place, date,
  result), `console.txt`, and the reports (`--junitxml`/`--html` added to pytest; Playwright's report copied). With
  `--run-id` it reads an Actions run with `gh`, downloads its artifacts and log.
- **`check`** ports every check of the original harness, plus TEST-7 (red run on a tests-only commit, an ancestor of the
  code; history bundles fetched when the commits were squashed), TEST-8 (every ✅ links a complete evidence folder),
  TEST-9 (reports per kind, 5 MB limit, the index, the archive) and DOC-2/DOC-3 rows. What a folder must hold is in
  `conf/folder-rules.yaml`: required files, headings, icons, production and test paths, package markers.
- **`git-gate`** reads the hook's command with the shared `ShellCommandSplitter`; it refuses commits and pushes on
  `master`/`develop`, and production code committed before its red run or with new tests in the same commit.
- **`archive`** zips the folder to the pre-release `evidence-GH-n` (assets never replaced) and comments the issue;
  **`board`** moves the issue's card through `gh api graphql`.

## project-docs and release-notes

- `project-docs map` reads `conf/doc-map.yaml` (first matching rule, `{service}`/`{frontend}` captures); `check` reads
  links, headings, `Last reviewed:` stamps and Mermaid blocks with `MarkdownText`, and renders Mermaid with `mmdc` when
  it is installed.
- `release-notes` reads `conf/changelog-types.yaml` and the release-note template; `release-body` reads the issues'
  `<!-- release-note -->` comments through the GitHub REST client (`conf/github-api.yaml`).

## pr-watch

- One run: for each registered open pull request, its state, check runs, workflow runs, dev/qa deployments, reviews
  and comments (cursors per source), and a rebase probe (`git fetch` into `refs/pr-watch/*`, `git merge-tree` against
  the pull request's base). New problems go to the ticket's inbox; the session is reopened with `xdg-open vscode://…`
  or notified.
- State in `~/.local/state/claude-pr-watch/` (registry, state, inboxes, operations log), atomic writes under a lock.
- `pr-watch-hook` is a light entry point that imports only what the prompt hook needs (about 0.25 s).

## ai-test-cost

- `run` checks the estimate, starts the command in its own process group with `AI_COST_RUN_ID`, polls the Anthropic
  usage report every minute, kills the group at 90 % of the cap and blocks the ticket.
- `gate` reads each command structurally (quotes, `;`, `&&`, `|`, `bash -c`, here-documents, `PYTEST_ADDOPTS`).
- `raise-cap` needs a terminal and the ticket key typed back; the gate also refuses it from any session.
- Settings only from `conf/settings.yaml`; prices in `conf/prices.yaml` with their source and date.
