# 6. Tests and maintenance

## How the harness is tested

| Package | Tests | Stand-ins |
|---|---|---|
| harness-core | 95 | git sandboxes, fake programs on `PATH`, `httpx.MockTransport` handlers |
| ticket-docs | 411 | git sandboxes with bundles and worktrees, ticket folders built from templates, a fake `gh` |
| project-docs | 114 | documentation trees in `tmp_path`, a fake `mmdc` |
| release-notes | 174 | changelog trees, a fake GitHub API |
| pr-watch | 626 | a fake GitHub API, git sandboxes, fake session files, hook timing |
| ai-test-cost | 295 | fake usage reports, fake processes, an injectable terminal |
| cve-scan | 108 | recorded scanner outputs, fake scanner executables |

No test calls a real service, and `unittest.mock` is not used (`AGENT.md`). Every package was written tests first:
its red and green runs are in GH-1's evidence (`docs/tickets/GH-1/tests-evidences/`, archived to `evidence-GH-1`).

```bash
cd .claude/skills && uv sync
cd <package> && ../.venv/bin/pytest            # one package
../.venv/bin/mypy src tests && ../.venv/bin/ruff check .
```

CI's `harness tools` job runs ruff, mypy and pytest for every package and keeps the JUnit reports.

## Changing the harness

- **A rule:** edit its file in `.claude/rules/` (next ID, summary row, **Rule / Why / How to apply / Check**), and add
  its short name to the rule skill's description.
- **A skill:** edit its `SKILL.md`; the description decides when it loads.
- **A tool:** it is simple-erp code like any other: a ticket, a branch, tests first, evidence, review.
- **A hook:** edit `.claude/settings.json`; keep it under 0.5 s (measure it), let it exit 0 on its own errors, and deny
  only on purpose.
- **A catalogue** (`conf/*.yaml`): a reviewed change, never an environment variable.

## Known limits

- The usage report counts the whole Anthropic organisation unless `AI_COST_API_KEY_ID` is set, and has never been
  called with a real Admin key from here.
- Jenkins console scanning and the original QA bot's `/testing-*` comments have no GitHub equivalent and were not ported.
- The free plan forbids environment reviewers and rulesets on a private repository: the harness's own gates stand in.
- The board's views and automations are set by hand in the web page.
