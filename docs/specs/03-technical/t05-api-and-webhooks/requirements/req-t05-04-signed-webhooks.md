🏠 [Specs](../../../README.md) › ⚙️ [Technical capabilities](../../README.md) › 🔗 [T5 API and webhooks](../README.md) ›
📌 [Requirements](README.md) › 📌 REQ-T05-04 Signed webhooks

# 📌 REQ-T05-04 Signed webhooks

**Status:** ✅ specified

## Statement

Webhooks are signed, retried and can be replayed.

## Why

Confirmed by the owner on 2026-11-12; D410.

## Acceptance criteria

1. **Given** a webhook delivered, its signature checks.
2. **Given** a receiver down, retried then replayable.

## Measure

Delivery rate.

## Priority

Must

## Capabilities served

F6, F24

## Tests

Unit and contract tests of the service that implements it; isolation, policy and evaluation tests where it applies
(D426).

## Open questions

None.

---

⬅️ [REQ-T05-03 problem+json errors](req-t05-03-problem-json.md) · ⬆️ [Up](README.md) ·
➡️ [REQ-T05-05 Contracts tested](req-t05-05-contract-tests.md)
