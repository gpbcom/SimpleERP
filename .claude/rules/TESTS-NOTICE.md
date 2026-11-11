# How to run the tests

The reference each ticket's `TESTS-NOTICE.md` adapts. Every run that proves something is recorded with `ticket-docs record-run` (TEST-8), and its reports are kept (TEST-9).

Wrap heavy commands in a resource cap on a shared machine. Run `pytest` one file or one folder at a time, with `-n 2` at most.

## Levels

| Level | Kind | Where | What it proves |
|---|---|---|---|
| Unit | `unit` | local, CI | Each class does what its tests say |
| Conventions | `check` | local, CI | The rules `tests/conventions/` enforces (`AGENT.md`) |
| Static checks | `check` | local, CI | `ruff check`, `ruff format --check`, `mypy` |
| GUI | `gui` | local, dev, QA | A front end's screens and flows, Playwright against the real images |
| API | `e2e` | dev, QA | The HTTP APIs, the Bruno collection run headless (TEST-1) |
| Stage | `e2e` | dev, QA | The whole commit started from its images on a runner (`stage.yml`) |
| Upgrade | `e2e` | QA | The previous release's images and data, then this commit's images on top |

## Unit tests

```bash
uv sync
uv run pytest tests/<layer>/<package> -n 2
```

Recorded:

```bash
.claude/skills/ticket-docs/bin/ticket-docs record-run --ticket GH-<n> --kind unit --where local \
  --check unit-<step> --what "<what this run proves>" -- uv run pytest tests/<layer>/<package> -n 2
```

`record-run` adds `--junitxml` and `--html` to a `pytest` command itself, and writes `console.txt` and the README with the commit.

The harness tools have their own workspace: `cd .claude/skills/<tool> && ../.venv/bin/pytest` after `uv sync` in `.claude/skills/`.

## Static checks and conventions

```bash
uv run ruff check src tests
uv run ruff format --check <the files you edited>
uv run mypy src
uv run pytest tests/conventions
```

## GUI tests (Playwright)

```bash
docker compose -f compose.e2e.yaml up -d --wait
cd frontends/<frontend> && npx playwright test [--grep @smoke]
docker compose -f compose.e2e.yaml down -v
```

The reports go to `playwright-report/` and `test-results/results.json`; copy both into the evidence folder (`record-run --kind gui -- npx playwright test` copies them).

## Stage runs (dev and QA)

```bash
gh workflow run stage.yml --ref <branch> -f stage=dev -f ref=<commit>  # dev: smoke, Bruno, Playwright @smoke
gh workflow run stage.yml --ref <branch> -f stage=qa -f ref=<commit>   # QA: only on the owner's yes, the full suites (GIT-6)
gh run list --workflow stage.yml --commit <commit>          # find the run
gh run watch <run-id>
```

Then keep the proof:

```bash
.claude/skills/ticket-docs/bin/ticket-docs record-run --ticket GH-<n> --kind e2e --where dev \
  --check stage --what "<what this run proves>" --run-id <run-id>
```

With `--run-id`, `record-run` downloads the run's artifacts (`gh run download`), saves its log (DEP-3), and reads its result instead of running a command.

## Paid AI tests

Through the cost guard only (TEST-5):

```bash
.claude/skills/ai-test-cost/bin/ai-cost run --ticket GH-<n> --estimate-usd <n> --label "<what>" -- <command>
```
