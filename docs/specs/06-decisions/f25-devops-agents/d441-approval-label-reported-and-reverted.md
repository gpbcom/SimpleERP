🏠 [Specs](../../README.md) › 📜 [Decisions](../README.md) ›
🤖 [Decisions: F25 DevOps agents (hosted edition)](README.md) › 📜 D441 The approval label reported and reverted

# 📜 D441 The approval label reported and reverted

**Status:** ✅ decided

## Context

R3: needs-maintainer-approval cannot be enforced as D434 wrote it: the agents' App token with Issues write can remove
any label, and the harness check of GH-23 only reports.

## Options

- A workflow that reverts, plus branch protection.
- GitHub permissions alone.
- The harness check alone.

## Choice

A workflow on the label and project-status events reverts any removal of needs-maintainer-approval and any status move
made by someone who is not a maintainer, the agents' and the intake's Apps included, and reports it; branch protection
requires a maintainer's review before any merge; Backlog is the only status allowed while the label is on. The workflow
is built in a harness ticket, GH-23 (pull request #24), and counts as pending until it is merged.

## Decided by

The owner, on 2026-11-12 at 14:55, round 2 of the decisions on the independent review (R3, PROGRESS.md, step 21).

## Consequences

Revises D434 ("refuses" becomes "reported and reverted"); BR-F25-07, TC-24 and the F25 build study say so.

## Related

- [F25 DevOps agents (hosted edition)](../../02-functional/f25-devops-agents/README.md)
- [How to build the DevOps agents](../../02-functional/f25-devops-agents/build-study.md)
- [D434](d434-maintainer-approval-label.md)
- [Independent review of 2026-11-12](../../../tickets/GH-2/review/2026-11-12-review.md)

---

⬅️ [D440](../vision/d440-local-by-default-outside-by-choice.md) · ⬆️ [Up](README.md) ·
➡️ [D442 The DevOps agents' runners in an isolated cluster](d442-devops-runners-isolated-cluster.md)
