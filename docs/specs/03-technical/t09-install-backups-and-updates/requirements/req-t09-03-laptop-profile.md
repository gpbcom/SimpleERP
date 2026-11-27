🏠 [Specs](../../../README.md) › ⚙️ [Technical capabilities](../../README.md) ›
🚀 [T9 Install, backups and updates](../README.md) › 📌 [Requirements](README.md) ›
📌 REQ-T09-03 The laptop profile within 8 GB

# 📌 REQ-T09-03 The laptop profile within 8 GB

**Status:** ✅ specified

## Statement

The laptop profile runs within 8 GB of RAM; the installer checks the machine.

The budget is proved by a measured prototype on the owner's machine before it is promised; with the AI turned off,
Milvus is not installed (REQ-T08-01).

## Why

Confirmed by the owner on 2026-11-12; D408.

## Acceptance criteria

1. **Given** a laptop under the budget, it installs.
2. **Given** a machine too small, the installer says so.

## Measure

Memory at rest.

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

⬅️ [REQ-T09-02 Compose and Helm everywhere](req-t09-02-compose-and-helm.md) · ⬆️ [Up](README.md) ·
➡️ [REQ-T09-04 Backups: RPO 15 minutes, RTO 4 hours](req-t09-04-backups-targets.md)
