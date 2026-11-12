# CLAUDE.md

@AGENT.md

## The harness

This repository carries its own Claude Code harness, versioned with the code. Its documentation is in
`.claude/harness-docs/` (start with `HOWTO.md`).

- **Rules:** `.claude/rules/`. Coding (CS, on top of `AGENT.md`), git and deploy (GIT, DEP), testing (TEST) and
  documentation (DOC). The rule skills load them live: `coding-style-rules`, `git-deploy-rules`, `testing-rules`,
  `ticket-documentation-rules`.
- **Tickets:** a GitHub issue `#<n>` is the ticket `GH-<n>`. Its local folder is `docs/tickets/GH-<n>/` (not
  versioned, archived to the GitHub pre-release `evidence-GH-<n>`). The `ticket-docs` skill creates and keeps it.
- **Tests come before the code, and nothing passes without its evidence** (TEST-7, TEST-8, TEST-9).
- **Work is planned as features made of tickets** (GIT-10): a feature is a parent issue (`feature` + one family
  `HARNESS`, `SPECS`, `PRODUCT`, `TESTS` or `USER`), its tickets are sub-issues with exactly one component label and
  the ticket format. A `USER` feature (a customer's request) holds one ticket, `USER-FEATURE-REQUEST` or
  `USER-REPORTED-BUG`; an issue created by an agent carries `needs-maintainer-approval` and stays in Backlog until a
  maintainer removes it.
- **Branches follow GitFlow** (GIT-8). Every squash and every push waits for an explicit yes (GIT-1).
- **At the end of a ticket:** `project-docs` updates `README.md`, `docs/functional/` and `docs/technical/` (DOC-2);
  `release-notes` writes the release note and the changelog fragment (DOC-3).
- **Hooks** (`.claude/settings.json`): the PR watcher's inbox, the paid-AI cost gate, the TDD gate and the time
  reminder.
