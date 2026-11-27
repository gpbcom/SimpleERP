🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
🤖 [F25 DevOps agents (hosted edition)](../README.md) › 📏 [Business rules](README.md) ›
📏 BR-F25-30 One active run per repository, resumed from its checkpoint

# 📏 BR-F25-30 One active run per repository, resumed from its checkpoint

**Status:** 🔄 waiting for the owner

## Statement

A repository has one active run of the agent team at a time; the other runs wait in a queue and a run in progress is
never cancelled by a new one. Each run has a 30-minute timeout, a turn limit and a budget limit. A run saves a
checkpoint after each stage, stored apart from the verified code, and an interrupted run resumes from it without losing
a commit or opening a second pull request.

## Why

Unattended runs stop for many reasons, and work already done must not be lost or paid twice, as the owner asked on
2026-11-16
[D567](../../../06-decisions/f25-devops-agents/d567-the-agent-team-roles-contract-worktrees-one-commit-verification.md).
Budgets warn then stop ([D398](../../../06-decisions/f22-unified-cost-management/d398-budgets-warn-then-stop.md)) and
every run is metered ([BR-F25-11](br-f25-11-agents-metered-and-audited.md)).

## Examples

| Case | Result |
|---|---|
| A second run asked while one is active | Queued, the active one goes on |
| A run stopped by the 30-minute timeout | rerun, resumes at the next unfinished stage |
| A checkpoint naming pull request 57 | pull request 57 updated, no second one |
| A recorded commit missing from its branch | no resume, the maintainer is told |
| A run stopped on its budget | resumes only once the budget is raised |

## Applies to

- [UC-F25-37](../use-cases/08-team-builds-a-ticket/uc-f25-37-resume-an-interrupted-run.md)
- [E-F25-23 Run checkpoint](../data/e-f25-23-run-checkpoint.md)
- [E-F25-10 Agent run](../data/e-f25-10-agent-run.md)
- [BR-F25-11 Agents are metered and audited](br-f25-11-agents-metered-and-audited.md)
- [UC-F25-36](../use-cases/08-team-builds-a-ticket/uc-f25-36-open-the-draft-pull-request-with-its-evidence.md)

## Exceptions

None.

## Configurable

(Proposed) The turn limit and the budget per run, by the maintainers within the budgets of F22; the timeout of 30
minutes and the single active run per repository are fixed.

## Open questions

None.

---

⬅️ [BR-F25-29](br-f25-29-a-draft-pull-request-carries-its-evidence-and-screenshots.md) · ⬆️ [Up](README.md)
