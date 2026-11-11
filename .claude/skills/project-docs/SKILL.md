---
name: project-docs
description: Keep the versioned project documentation of simple-erp current (rule DOC-2) - README.md at the root, docs/functional/ (what users can do and see, one chapter per business capability, from docs/specs/) and docs/technical/ (architecture, services, front ends, data model, API, configuration, CI/CD and stages, tests and traceability, development process, operations). Mode `init` writes them the first time; mode `update` runs at the end of every ticket (hand-over, before the pull request), maps the branch's changed files to the chapters with conf/doc-map.yaml, updates each chapter concerned, stamps it, and logs it in PROGRESS.md's Documentation section; `project-docs check` must print nothing. Use at every ticket hand-over, after a release, when a chapter is found out of date, or when asked to write, refresh or check the README or the functional or technical documentation.
argument-hint: [init | update GH-<n> | check]
---

# Project documentation (DOC-2)

Arguments: `$ARGUMENTS`: the mode (`update` by default when a ticket is in progress) and the ticket key.

The project documentation is what a newcomer reads. It is **versioned**; in `docs/`, only `specs/`, `functional/` and `technical/` are (`.gitignore`). Ticket folders are not project documentation.

| Where | For | Holds |
|---|---|---|
| `README.md` | Everyone, first | What simple-erp is, the quick start, the commands, the layout, the services and front ends, links to the rest |
| `docs/functional/` | Users, testers, product | What users can do and see: one chapter per business capability (customers, …), its screens, rules and flows |
| `docs/technical/` | Developers, operators | How it is built and run: one chapter per subject, and one per service and per front end |
| `docs/specs/` | Input | The specifications and flowcharts. Read, never rewritten by this skill |

**The tool:** `.claude/skills/project-docs/bin/project-docs`:
- `map [--base origin/develop]` lists the chapters the branch's changed files concern (`conf/doc-map.yaml`);
- `check [--ticket <KEY>] [--base origin/develop]` prints nothing when the documentation is complete and current (below).

## Writing rules

- Plain British English, short sentences, no em dashes (`AGENT.md`). Identifiers in backticks.
- Each folder has a `README.md` that links every chapter of the folder, with one line on what it holds.
- Diagrams are Mermaid blocks (`flowchart`, `sequenceDiagram`, `erDiagram`), never images of diagrams.
- Describe what exists, not what is planned: a planned part is named once, in a "Not built yet" line.
- No secret, token, password, internal URL with credentials, or personal data.
- Every chapter ends with `Last reviewed: <YYYY-MM-DD> (<KEY>)`, the ticket that last changed it.
- Functional chapters never explain code; technical chapters may link the code (`services/<service>/src/...`).

## Mode `init`

Once, when the documentation does not exist yet. Read `AGENT.md`, `pyproject.toml`, `conf/`, `docs/specs/`, `.github/workflows/`, `.claude/rules/` and the code, then write from [templates/](templates/):

1. `README.md`.
2. `docs/functional/README.md`, and one chapter per business capability found in `docs/specs/` (e.g. `customers.md` from `docs/specs/flowcharts/customer.mmd`).
3. `docs/technical/README.md`, then `architecture.md`, `api.md`, `data-model.md`, `configuration.md`, `ci-cd-and-stages.md`, `tests-and-traceability.md`, `development-process.md`, `operations.md`, and `services/<service>.md` / `frontends/<frontend>.md` for each one that exists.
4. `project-docs check` prints nothing.

## Mode `update`, at the end of a ticket

1. **What changed:** `project-docs map` (the chapters concerned and the paths that concern them), with the ticket's TICKET.md, EXPLAIN.md §2 (what changed for users) and §3 (what changed in the code), and IMPLEMENTATION.md.
2. **Update each chapter concerned:**
   - functional chapters take what users can now do or see (EXPLAIN §2), in users' words;
   - technical chapters take the how (EXPLAIN §3): flows, contracts, configuration, commands;
   - `README.md` changes when a command, the layout, a service or front end, or the quick start changes;
   - a new capability, service or front end gets its own chapter, linked from its folder's README.
3. **Stamp** each changed chapter `Last reviewed: <date> (<KEY>)`.
4. **A chapter concerned but left as it is** gets a row in PROGRESS.md's Documentation table: `no doc impact: <reason>` (e.g. "internal refactoring, no behaviour or contract change").
5. **Log** every chapter in PROGRESS.md's Documentation section, with ✅ and what changed.
6. **Check:** `project-docs check --ticket <KEY>` prints nothing. Commit the documentation with the ticket's code (`[GH-<n>] docs: …`).

## What `project-docs check` verifies

- Every Markdown file of `docs/functional/` and `docs/technical/` is linked from its folder's `README.md`.
- Every relative link of `README.md`, `docs/functional/` and `docs/technical/` resolves.
- Every service (`services/*/`) and front end (`frontends/*/`) has its technical chapter.
- Every chapter has its `Last reviewed:` line, and no em dash.
- Mermaid blocks render, when `mmdc` (mermaid-cli) is on the PATH; otherwise nothing is printed about them and a WARNING in the harness log (`~/.local/state/claude-harness/project-docs.log`) says they were skipped.
- **With `--ticket`:** every chapter `map` returns for the branch was changed in the branch, or is waived with `no doc impact` in the ticket's PROGRESS.md.

CI runs `project-docs check` without `--ticket` on every pull request (ticket folders are local).
