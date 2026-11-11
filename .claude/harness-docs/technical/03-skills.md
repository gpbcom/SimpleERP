# 3. Skills

A skill is a folder `.claude/skills/<name>/` with a `SKILL.md`: front matter (`name`, `description`) and a procedure.
Claude Code shows every skill's name and description in each session and loads the full file when a task matches.
**The description is the trigger:** it lists what the skill covers and when to load it.

| Skill | Trigger (summary) | Files | Writes |
|---|---|---|---|
| **ticket-docs** | Create, plan, implement, record a run, pause, resume, audit or hand over a ticket; a rebase conflict | `templates/`, `conf/github.yaml`, tool `ticket-docs` | `docs/tickets/GH-n/`, the index, the board, the archive |
| **coding-style-rules** | Before writing, changing or reviewing code; before every commit | loads `AGENT.md` + `rules/coding-style.md` | |
| **git-deploy-rules** | Branches, commits, squash, push, pull requests, board, dependencies, stages, releases | loads `rules/git-rules-and-deploy.md` | |
| **testing-rules** | Before writing code (tests first), running tests, claiming a pass, hand-over | loads `rules/testing.md` | |
| **ticket-documentation-rules** | EXPLAIN.md, project docs, release notes, hand-over | loads `rules/ticket-documentation.md` | |
| **project-docs** | End of every ticket, after a release, docs out of date | `conf/doc-map.yaml`, `templates/`, tool `project-docs` | `README.md`, `docs/functional/`, `docs/technical/` |
| **release-notes** | End of every ticket, a release or hotfix, the next version | `conf/changelog-types.yaml`, `templates/`, tool `release-notes` | `RELEASE-NOTE.md`, `changelog.d/`, `CHANGELOG.md`, issue comments |
| **pr-watch** | `/pr-watch GH-n`, the hook's events, registering a pull request | `conf/watch.yaml`, `systemd/`, `templates/`, tool `pr-watch` | `~/.local/state/claude-pr-watch/`, the PR summary |
| **pr-review-followup** | After a pull request is opened or pushed, review comments | | PROGRESS.md "PR review", fixes, rule proposals |
| **ai-test-cost** | Before any paid AI test; a gate refusal | `conf/`, `templates/COST.md`, tool `ai-cost` | `~/.local/state/ai-test-cost/`, `COST.md` |
| **cve-scan** | Scan for CVEs, secrets, misconfigurations; Dependabot alerts | tool `cve-scan` | `~/.cache/cve-scan/…/CVE-REPORT.md` |
| **exception-and-log-messages** | Any `raise`, log call or field validator | | |

## The rule-skill pattern

The four rule skills hold no rule. Each one:
1. names its source of truth and shows it live (`!`cat "$(git rev-parse --show-toplevel)/…"``), so the skill and
   the file can never disagree;
2. says how to apply the rules (checks before committing, results on PROGRESS.md's **Rules** line);
3. says where a new rule goes (the file, next free ID, never the skill);
4. lists the rules' short names in its **description**, so that a task touching one of them loads it. Adding a rule
   updates that list.

## Writing or changing a skill

- Keep the description precise and complete: it alone decides when the skill loads.
- A skill never copies a rule: it points to the rule file.
- A tool behind a skill follows `AGENT.md`, is written tests first, and has its own tests.
