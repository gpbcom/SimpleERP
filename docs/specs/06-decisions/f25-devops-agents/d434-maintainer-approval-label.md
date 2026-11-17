🏠 [Specs](../../README.md) › 📜 [Decisions](../README.md) ›
🤖 [Decisions: F25 DevOps agents (hosted edition)](README.md) › 📜 D434 Maintainers approve agents' work

# 📜 D434 Maintainers approve agents' work

**Status:** ✅ decided

## Context

How maintainers' approval of agent-created features and tickets is marked.

## Options

- An approval label, Backlog until approved.
- A GitHub review only.

## Choice

Agent-created features and tickets carry the label needs-maintainer-approval and stay in Backlog; only a simple-ERP
maintainer (U47) removes it and moves them to Ready; the harness check refuses Ready or In progress while the label is
on.

## Decided by

The owner, on 2026-11-12, in the specification interview.

## Consequences

BR-F25-07.

Revised by D441 on 2026-11-12: removing the label, or moving a status, by anyone but a maintainer is reported and
reverted by a workflow, with branch protection; Backlog is the only status allowed while the label is on; harness ticket
GH-23 (pull request #24) builds it, pending until merged.

Revised by D452 on 2026-11-12: the maintainer who approves is the repository maintainer (U47), not the hosting engineer
(U48).

## Related

- [F25 DevOps agents](../../02-functional/f25-devops-agents/README.md)

---

⬅️ [D433 The USER family and its labels](d433-user-family-and-labels.md) · ⬆️ [Up](README.md) ·
➡️ [D435 The agents' access and limits](d435-agents-access-and-limits.md)
