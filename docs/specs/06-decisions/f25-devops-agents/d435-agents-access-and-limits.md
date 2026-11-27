🏠 [Specs](../../README.md) › 📜 [Decisions](../README.md) ›
🤖 [Decisions: F25 DevOps agents (hosted edition)](README.md) › 📜 D435 The agents' access and limits

# 📜 D435 The agents' access and limits

**Status:** ✅ decided

## Context

What the agents may reach.

## Options

- Read the managed SimpleERP, the repository and the specs; write only branches, pull requests and issues.
- Wider write access.

## Choice

The agents read the customer's namespace on the fully managed SimpleERP (as F20: read-only, audited, masked, never
secrets), read the repository and the specs, and write only branches, pull requests, issues and comments; they never
merge, deploy, change labels reserved to maintainers, or reach another customer's data.

## Decided by

The owner, on 2026-11-12, in the specification interview.

## Consequences

BR-F25-04, BR-F25-05.

Revised by D442 on 2026-11-12: the agents read only a masked copy of the customer's company, from their isolated
cluster, never the live namespace; a namespace holding health data stays out of their models' reach unless the hosting
and the model path are HDS-certified (review R27).

Revised by D452 on 2026-11-12: the hosting engineer (U48) runs the agents' runners and rights; maintainers (U47) approve
their work.

## Related

- [F25 DevOps agents](../../02-functional/f25-devops-agents/README.md)

---

⬅️ [D434 Maintainers approve agents' work](d434-maintainer-approval-label.md) · ⬆️ [Up](README.md) ·
➡️ [D436 F25 use cases](d436-f25-use-cases.md)
