🏠 [Specs](../../../README.md) › ⚙️ [Technical capabilities](../../README.md) ›
🚀 [T9 Install, backups and updates](../README.md) › 📌 [Requirements](README.md) ›
📌 REQ-T09-04 Backups: RPO 15 minutes, RTO 4 hours

# 📌 REQ-T09-04 Backups: RPO 15 minutes, RTO 4 hours

**Status:** ✅ specified

## Statement

Continuous archiving and daily snapshots give RPO 15 minutes and RTO 4 hours; one company restorable alone; a monthly
restore test.

In the hosted edition and on IT providers' platforms, daily backups are kept 30 days and monthly ones 12 months;
self-hosted installs default to daily backups kept 30 days (D24, D444).

## Why

Confirmed by the owner on 2026-11-12; D422.

Revised by D444 on 2026-11-12.

## Acceptance criteria

1. **Given** a restore test, within 4 hours.
2. **Given** one company restored, others untouched.

## Measure

Restore time.

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

⬅️ [REQ-T09-03 The laptop profile within 8 GB](req-t09-03-laptop-profile.md) · ⬆️ [Up](README.md) ·
➡️ [REQ-T09-05 Upgrades on a copy, rollback](req-t09-05-safe-upgrades.md)
