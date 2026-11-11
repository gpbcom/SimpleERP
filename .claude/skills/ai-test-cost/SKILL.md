---
name: ai-test-cost
description: Run every test that calls a paid AI (the Claude API, or any other billed model) through the cost guard `ai-cost run`, which caps the paid tests of a ticket at $20 all runs together, refuses a run whose estimate does not fit, kills a run at 90 % of the cap, blocks the ticket until the human raises the cap, and writes every run to the ticket's tests-evidences/COST.md. Use before running any test marked `llm`, `pytest -m llm` or `pytest --llm`, or any other command that makes a paid model call, and whenever the PreToolUse hook refused a command because it "calls a paid AI" or sets an AI_COST_ variable.
---

# AI test cost: $20 per ticket, all runs together

Every test that makes a paid AI call is charged to its ticket. The cap is **$20 for all the paid tests of a ticket together**. The guard keeps one ledger per ticket in `~/.local/state/ai-test-cost/<KEY>.json`, and writes it out as `docs/tickets/<KEY>/tests-evidences/COST.md` in the repository you call it from.

A `PreToolUse` hook (`.claude/skills/ai-test-cost/bin/ai-cost gate`) refuses, in every Claude session:

- a paid test not run through the guard: any `pytest` whose `-m` or `--markexpr` expression names `llm` (other than `not llm`), any `pytest --llm`, the same options hidden in `PYTEST_ADDOPTS`, inside `bash -c '...'` or a shell here-document, and the other commands of `conf/paid-commands.yaml`;
- `ai-cost run` without `--ticket`, with a key that is not a ticket, or for a blocked ticket;
- any `ai-cost raise-cap`, wherever it is called: after variables, `env`, `uv run` or `python -m ai_cost`, inside `bash -c '...'`, or as the command of an `ai-cost run`;
- any command that sets or exports an `AI_COST_` variable, except `AI_COST_CALLER_CWD`.

The hook reads each command word by word, so quoting a marker or a command name does not hide it. Quoted text that is only mentioned (a `grep` pattern, a commit message) and the body of a here-document fed to `python3` or `cat` are not commands, and are let through.

## How the cost is measured

The usage source is set in `conf/settings.yaml` (`usage_source`):

- `anthropic` (the default): the guard reads the Anthropic Admin API usage report (`GET /v1/organizations/usage_report/messages`, minute buckets, grouped by model) with the admin key in `ANTHROPIC_ADMIN_KEY`, and prices the tokens with `conf/prices.yaml`. The report counts the whole organisation: set `AI_COST_API_KEY_ID` to the id of the API key the tests use, so that Claude Code's own calls and a colleague's are not counted. The report arrives about 5 minutes late, so a run's cost is final (`settled`) at the first `ai-cost` command 5 minutes after its end.
- `estimate`: nothing is measured, each run is charged its estimate, and `ai-cost charge` corrects it afterwards.

Prices: `conf/prices.yaml`, Claude API first-party rates read on the Anthropic pricing page (the file names the page and the date). A model the file does not know is priced as the most expensive one.

The settings that enforce the cap (cap, kill ratio, usage source, files, state folder) are read from the versioned `conf/settings.yaml` only, never from the environment: changing one is a reviewed change of that file. The environment may only set `AI_COST_CALLER_CWD` (set by `bin/ai-cost`), `AI_COST_API_KEY_ID` and the secret `ANTHROPIC_ADMIN_KEY`, all three in the human's own shell.

## Run a paid test

1. **Mark it.** A test that calls a paid AI carries the pytest marker `llm`. The repository's root `tests/conftest.py` fails any `llm` test that runs without `AI_COST_RUN_ID`, which only `ai-cost run` sets, so a paid test cannot run outside the guard by accident.
2. **Estimate** its cost: calls times (input tokens times the input price plus output tokens times the output price), from `conf/prices.yaml`, plus a margin. Use a previous run's measure (`ai-cost status <KEY>`) when there is one.
3. **Run it through the guard**, from the folder the test needs:

   ```bash
   .claude/skills/ai-test-cost/bin/ai-cost run --ticket <KEY> --estimate-usd <n> --label "<what it tests>" [--soft] [--on-kill "<stop command>"] -- <command>
   ```

   - The run is **refused** (exit code 3, nothing started) when the ticket is blocked or the estimate is above what is left.
   - The child gets `AI_COST_RUN_ID` and `AI_COST_TICKET`.
   - Every minute the guard measures the run. At **90 % of the cap** ($18) it kills the run's whole process group, runs `--on-kill`, and **blocks the ticket** (exit code 3).
   - A run whose cost cannot be measured 3 times in a row is stopped: the cap cannot be enforced blind.
   - Without `ANTHROPIC_ADMIN_KEY`, a measured run is a usage error (exit code 2): ask the human to set the key, or use `--soft` and then `ai-cost charge` with the figure read on the Console's Cost page.
4. **Keep the evidence.** The run is in `docs/tickets/<KEY>/tests-evidences/COST.md`, written by the guard, never by hand. Name the run id in the evidence README of the test. The evidence folder is local (gitignored) and is archived to the ticket's GitHub pre-release at hand-over.

## Other commands

| Command | Use |
|---|---|
| `ai-cost status <KEY>` | Spend, cap and every run, the ended runs settled first. |
| `ai-cost remaining <KEY>` | What the ticket may still spend, in USD. |
| `ai-cost charge <KEY> <usd> --label "..." --note "<where the figure comes from>"` | Charge a cost measured elsewhere, such as a soft run's real cost. |
| `ai-cost raise-cap <KEY> <usd>` | **The human only, in their own terminal.** The hook refuses it from a Claude session, and the command itself opens `/dev/tty`, shows a random 6-character code there and needs it typed back: without a terminal, or with another answer, it exits with code 3 and the cap is unchanged. `ticket-docs file-gate` refuses a Write or Edit in the ledger folder. These stop mistakes, not a deliberate forgery by a process of the same user. A blocked ticket stays blocked until the human raises its cap above what it spent. |

## Rules

- TEST-5 in `.claude/rules/testing.md`: every test calling a paid AI runs through `ai-cost run`, $20 per ticket all runs together, `COST.md` in the ticket's evidence folder.
- A new paid command that is not a pytest run goes into `conf/paid-commands.yaml`, as a regular expression, so that the hook catches it.
- Never set an `AI_COST_` variable, never edit `conf/settings.yaml` to loosen the guard without the human's review, and never run `raise-cap`.
