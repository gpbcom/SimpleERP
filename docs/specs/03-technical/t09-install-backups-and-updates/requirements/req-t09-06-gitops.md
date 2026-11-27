🏠 [Specs](../../../README.md) › ⚙️ [Technical capabilities](../../README.md) ›
🚀 [T9 Install, backups and updates](../README.md) › 📌 [Requirements](README.md) ›
📌 REQ-T09-06 GitOps for hosted clusters

# 📌 REQ-T09-06 GitOps for hosted clusters

**Status:** ✅ specified

## Statement

Hosted clusters change only through Git and Argo CD.

## Why

Confirmed by the owner on 2026-11-12; D420.

## Acceptance criteria

1. **Given** a manual change, reverted.
2. **Given** a revert in Git, rolled back.

## Measure

Drift found.

## Priority

Must

## Capabilities served

F18 to F20, F25

## Tests

Unit and contract tests of the service that implements it; isolation, policy and evaluation tests where it applies
(D426).

## Open questions

None.

---

⬅️ [REQ-T09-05 Upgrades on a copy, rollback](req-t09-05-safe-upgrades.md) · ⬆️ [Up](README.md) ·
➡️ [REQ-T09-07 Read-only namespace access](req-t09-07-read-only-namespace-access.md)
