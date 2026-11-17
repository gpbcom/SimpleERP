🏠 [Specs](../../../README.md) › ⚙️ [Technical capabilities](../../README.md) › 🔗 [T5 API and webhooks](../README.md) ›
📌 [Requirements](README.md) › 📌 REQ-T05-06 Rate limits

# 📌 REQ-T05-06 Rate limits

**Status:** ✅ specified

## Statement

Calls are limited per company and per token.

## Why

Confirmed by the owner on 2026-11-12; D410.

## Acceptance criteria

1. **Given** a token over its limit, 429 with a retry time.
2. **Given** a company over its limit, others unaffected.

## Measure

429 rate.

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

⬅️ [REQ-T05-05 Contracts tested](req-t05-05-contract-tests.md) · ⬆️ [Up](README.md) ·
➡️ [REQ-T05-07 Offline devices and sync](req-t05-07-offline-devices-and-sync.md)
