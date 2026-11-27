🏠 [Specs](../../../README.md) › ⚙️ [Technical capabilities](../../README.md) › 🔗 [T5 API and webhooks](../README.md) ›
📌 [Requirements](README.md) › 📌 REQ-T05-07 Offline devices and sync

# 📌 REQ-T05-07 Offline devices and sync

**Status:** ✅ specified

## Statement

Offline-first apps (tills, waiters' tablets, field workers, carers, drivers) keep a local encrypted store and sync
through one protocol: number ranges reserved per device so that receipts stay numbered and inalterable offline, conflict
rules per record type (last write, merge or ask), and no more personal data on the device than its work needs.

## Why

Confirmed by the owner on 2026-11-12; D405 (offline devices); TC-06; the review of 2026-11-12 (R14).

## Acceptance criteria

1. **Given** a till offline for a day, its receipts synced with no gap and no duplicate.
2. **Given** two devices changing the same record offline, the record type's conflict rule applied and shown.

## Measure

Sync conflicts and losses per release.

## Priority

Must

## Capabilities served

F9, F10, SC01, SC04, SC06, SC07, SC15

## Tests

Unit and contract tests of the service that implements it; isolation, policy and evaluation tests where it applies
(D426).

## Open questions

None.

---

⬅️ [REQ-T05-06 Rate limits](req-t05-06-rate-limits.md) · ⬆️ [Up](README.md)
