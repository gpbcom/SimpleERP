🏠 [Specs](../../../README.md) › ⚙️ [Technical capabilities](../../README.md) ›
🚀 [T9 Install, backups and updates](../README.md) › 📌 [Requirements](README.md) ›
📌 REQ-T09-05 Upgrades on a copy, rollback

# 📌 REQ-T09-05 Upgrades on a copy, rollback

**Status:** ✅ specified

## Statement

Upgrades run on a copy first and roll back automatically on failure.

## Why

Confirmed by the owner on 2026-11-12; D422, D423.

## Acceptance criteria

1. **Given** an upgrade failing on the copy, not applied.
2. **Given** an upgrade failing live, rolled back.

## Measure

Failed upgrades.

## Priority

Must

## Capabilities served

All: F1 to F25 and the sectors SC01 to SC16.

## Tests

Unit and contract tests of the service that implements it; isolation, policy and evaluation tests where it applies
(D426).

## Open questions

None.

---

⬅️ [REQ-T09-04 Backups: RPO 15 minutes, RTO 4 hours](req-t09-04-backups-targets.md) · ⬆️ [Up](README.md) ·
➡️ [REQ-T09-06 GitOps for hosted clusters](req-t09-06-gitops.md)
