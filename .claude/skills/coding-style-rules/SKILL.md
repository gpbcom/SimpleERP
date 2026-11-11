---
name: coding-style-rules
description: The enforced coding rules of simple-erp, read live from AGENT.md and .claude/rules/coding-style.md. AGENT.md is the main rulebook (layers api → service → storage → models, one class per file whatever its kind, five Python files per folder at most, Runnable lifecycle and factories, import groups, typing without Any, SE* exceptions, one sentence per line in messages, every method logs, Pydantic field validators, YAML catalogues, StrEnum, tests mirror src without mocks, British English, no em dashes). The CS rules add to it - CS-1 no duplicated code or behaviour, CS-2 no ticket references in code comments, CS-3 a constructor in every class, CS-4 private methods under the "Internal Helpers Methods" banner, CS-5 Runnable children expose only initialize/run/close/execute, CS-6 Pydantic models instead of TypedDict, CS-7 five source files per folder, CS-10 short per-item logs that reuse computed results, CS-11 failures returned as values never dropped and nothing recorded as done before it is done, CS-13 one layer owns the retry of a call, CS-14 no nested imports, CS-15 match/case beyond three if/elif, CS-16 StrEnum members instead of raw string comparisons. Load before writing, changing or reviewing any code in simple-erp (services, front ends, packages, the harness tools in .claude/skills) and before every commit.
---

# Coding style rules (AGENT.md + CS)

**Sources of truth:** `AGENT.md` at the repository root, then `.claude/rules/coding-style.md`. Both are loaded below as they are now. If a section below is empty or shows a command instead of the rules, Read the file before going on. The files win over anything else; never copy their rules into another file.

## How to apply

1. Read each rule's **Scope** line before applying it. A rule out of scope is listed as "not applied" with the reason in the ticket's PLAN.md and PROGRESS.md.
2. Before writing code: search for code, tests and infrastructure to extend instead of writing a second version (CS-1).
3. Before writing code: write its tests first (TEST-7, **testing-rules** skill).
4. Before every commit: run the **Check** of every rule in scope on the change, and `uv run pytest tests/conventions`. Each must print nothing or pass. Log the results in the step's **Rules** line of PROGRESS.md.
5. A new rule the repository owner states about code goes into `.claude/rules/coding-style.md` (next free ID, **Rule** / **Why** / **Check**, a summary-table row, IDs never reused), or into `AGENT.md` when it is about how simple-erp code is laid out. Never into this skill. Proposals from reviews wait in `.claude/rules/rule-proposals.md`.

## AGENT.md

!`cat "$(git rev-parse --show-toplevel)/AGENT.md"`

## CS rules in force

!`cat "$(git rev-parse --show-toplevel)/.claude/rules/coding-style.md"`
