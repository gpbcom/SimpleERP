🏠 [Specs](../../README.md) › 📜 [Decisions](../README.md) ›
🤖 [Decisions: F25 DevOps agents (hosted edition)](README.md) › 📜 D433 The USER family and its labels

# 📜 D433 The USER family and its labels

**Status:** ✅ decided

## Context

How customers' requests appear in the repository's features and tickets (GIT-10).

## Options

- A USER family with two component labels.
- Secondary labels on existing families.

## Choice

A new feature family USER, confirmed by the owner on 2026-11-12: a USER feature holds exactly one ticket, carrying
exactly one of the component labels USER-FEATURE-REQUEST or USER-REPORTED-BUG. The agents' resulting work goes into
SPECS or PRODUCT features, linked to the customer's feature. The harness (GIT-10 and its check) is changed in its own
HARNESS ticket.

## Decided by

The owner, on 2026-11-12, in the specification interview.

## Consequences

BR-F25-02, BR-F25-03.

## Related

- [F25 DevOps agents](../../02-functional/f25-devops-agents/README.md)

---

⬅️ [D432 DevOps agents](d432-devops-agents-coverage.md) · ⬆️ [Up](README.md) ·
➡️ [D434 Maintainers approve agents' work](d434-maintainer-approval-label.md)
