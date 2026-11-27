🏠 [Specs](../../README.md) › 📜 [Decisions](../README.md) ›
🤖 [Decisions: F25 DevOps agents (hosted edition)](README.md) ›
📜 D442 The DevOps agents' runners in an isolated cluster

# 📜 D442 The DevOps agents' runners in an isolated cluster

**Status:** ✅ decided

## Context

R4: the DevOps agents run agent-written code on self-hosted runners inside the production hosting cluster with a
production read account; self-hosted runners are advised against on public repositories.

## Options

- A separate isolated cluster, reads from a masked copy.
- Runners in the hosting cluster (D437).
- GitHub-hosted runners.

## Choice

The runners live in a separate, isolated European cluster, with no outbound access except GitHub and the AI gateway;
production is read only from a masked copy of the reporting customer's company, never from the live namespace; jobs from
forks or outside pull requests never run on these runners.

## Decided by

The owner, on 2026-11-12 at 14:53, round 1 of the decisions on the independent review (R4, PROGRESS.md, step 21).

## Consequences

Revises D437 (the runners leave the hosting cluster) and D435 (the agents read a masked copy). REQ-T09-07 and the F25
build study say so.

## Related

- [How to build the DevOps agents](../../02-functional/f25-devops-agents/build-study.md)
- [F25 DevOps agents (hosted edition)](../../02-functional/f25-devops-agents/README.md)
- [D437](d437-devops-agents-in-the-ci.md)
- [D435](d435-agents-access-and-limits.md)
- Independent review of 2026-11-12 (the independent review of 2026-11-12, not kept in the repository)

---

⬅️ [D441 The approval label reported and reverted](d441-approval-label-reported-and-reverted.md) · ⬆️ [Up](README.md) ·
➡️ [D443](../vision/d443-paid-plugins-sell-support-updates-hosting.md)
