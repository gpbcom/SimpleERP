---
name: git-deploy-rules
description: The enforced git and deploy rules of simple-erp, GIT-1…GIT-n and DEP-1…DEP-n, read live from .claude/rules/git-rules-and-deploy.md - GIT-1 ask before every squash or push, GIT-3 issue to In review on the project board once the pull request is open, GIT-4 one squashed commit (history bundle saved first), GIT-5 a pull request description of 10 lines at most with "Closes #n" recorded in PROGRESS.md, GIT-6 the QA stage run (gh workflow run stage.yml --ref <branch> -f stage=qa) only once every earlier step has passed, announced on the pull request, GIT-7 a pull request fixed only in its ticket's own Claude session (pr-watch), GIT-8 GitFlow branch names, bases, targets, releases, hotfixes and v<x.y.z> tags, GIT-10 a feature is a parent issue (labels `feature` + one family HARNESS/SPECS/PRODUCT/TESTS/USER, never empty; a USER feature, a customer's request, holds exactly one ticket) made of tickets (sub-issues) with exactly one component label HARNESS/SPECS/INFRA/BACKEND/FRONTEND/E2E-TESTS/LOAD-TESTS/UNIT-TESTS/USER-FEATURE-REQUEST/USER-REPORTED-BUG allowed by the family, an issue created by an agent labelled `needs-maintainer-approval` and kept in Backlog until a maintainer removes the label, titled `[LABEL] Verb phrase`, with the sections Description, Implementation, Acceptance criteria, Tests, References (pinned spec or harness-rule IDs), Attachments, DEP-1 dependency files resolve before a push or stage run, DEP-2 lock files regenerated and pins moved together, DEP-3 dependency errors in Actions logs are failures, DEP-4 workflow actions pinned to commit SHAs and write permissions per job. Load before creating or editing a GitHub issue, feature or ticket, any branch creation, commit, squash, rebase, push, pull request, project-board change, dependency change, stage run, release or hotfix.
---

# Git and deploy rules (GIT, DEP)

**Source of truth:** `.claude/rules/git-rules-and-deploy.md`, loaded below as it is now. If the section below is empty or shows a command instead of the rules, Read that file before going on. The file wins over anything else; never copy its rules into another file.

## Delivery order for a ticket

1. Branch named under GIT-8, issue moved to **In progress**.
2. TEST-7 for every code step: tests-only commit, red run, code, green run.
3. Local checks green, with their evidence (ticket-docs skill).
4. DEP-1 before any push or stage run.
5. Dev stage run of the commit (`gh workflow run stage.yml --ref <branch> -f stage=dev -f ref=<sha>`), with its evidence.
6. **History bundle, then squash into one commit (GIT-4)**: ask first (GIT-1), with AskUserQuestion showing the branch, the remote, the commits to squash and the resulting message.
7. **Push (GIT-1)**: ask again; a yes covers that one push only.
8. **Pull request (GIT-5)**: 10 lines at most with `Closes #<n>`, written first in PROGRESS.md's "Pull request" section, its check silent. Then `pr-watch register <KEY>` (GIT-7) and the issue to **In review** (GIT-3).
9. DEP-3 on every Actions log of the commit.
10. **QA run (GIT-6)** once every step before it has passed; the comment on the pull request; the issue to **QA**.

The repository owner's additions for Claude: no `Co-Authored-By` trailer in commits, no "Generated with Claude Code" line in pull request descriptions.

A new rule about git, pull requests or deploys goes into the rules file, in its format (next free ID, **Rule** / **Why** / **How to apply**, a summary-table row, IDs never reused), not into this skill.

## Rules in force

!`cat "$(git rev-parse --show-toplevel)/.claude/rules/git-rules-and-deploy.md"`
