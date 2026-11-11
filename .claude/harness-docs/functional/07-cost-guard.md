# 7. Cost guard

Tests that call a paid AI model (the Claude API or any other billed model) are capped at **$20 per ticket, all runs
together** (rule TEST-5). simple-erp makes no paid call yet; the guard is ready for the first one.

## How it protects you

| Layer | What it does |
|---|---|
| The `llm` marker | A test that calls a paid model is marked `@pytest.mark.llm`. `tests/conftest.py` makes it fail unless `ai-cost run` started it |
| `ai-cost run` | Refuses a run whose estimate does not fit what is left, measures the run while it goes, kills it at 90 % of the cap and blocks the ticket |
| The gate hook | Refuses, in every Claude session, a paid command not run through `ai-cost run`, any `ai-cost raise-cap`, and any command that sets an `AI_COST_*` variable |
| `conf/settings.yaml` | The cap, the kill ratio and the measurement come from this versioned file only, never from the environment, so no command can loosen them |
| `COST.md` | Every run, written in the ticket's `tests-evidences/` by the guard itself |

A pytest run counts as paid when its `-m` / `--markexpr` expression names `llm` (`-m "not llm"` is free), when it has
`--llm`, or when `PYTEST_ADDOPTS` carries either.

## How the cost is measured

From the Anthropic Admin API's usage report, minute by minute, priced with `conf/prices.yaml` (read from Anthropic's
pricing page on 2026-11-10). It needs an Admin API key in `ANTHROPIC_ADMIN_KEY`, and counts the whole organisation
unless `AI_COST_API_KEY_ID` names the key the tests use. The report lags about five minutes, so a run's cost settles a
few minutes after it ends. Without an Admin key, a run is charged its estimate (`--soft`) and corrected with
`ai-cost charge`.

## What you do

| When | Command, in your own terminal |
|---|---|
| See what a ticket spent | `.claude/skills/ai-test-cost/bin/ai-cost status GH-<n>` |
| A ticket is blocked and more tests are worth it | `.claude/skills/ai-test-cost/bin/ai-cost raise-cap GH-<n> 30` |

**Note:** the gate refuses every command when its settings file cannot be read (it fails closed). If Bash commands
are suddenly all refused with a settings error, fix `conf/settings.yaml`.
