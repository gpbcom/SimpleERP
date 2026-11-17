🏠 [Specs](../../../README.md) › ⚙️ [Technical capabilities](../../README.md) › 🔗 [T5 API and webhooks](../README.md) ›
📌 [Requirements](README.md) › 📌 REQ-T05-03 problem+json errors

# 📌 REQ-T05-03 problem+json errors

**Status:** ✅ specified

## Statement

Errors are problem+json with the error codes of the error pattern.

## Why

Confirmed by the owner on 2026-11-12; D122, D410.

## Acceptance criteria

1. **Given** a refused call, a problem+json body with its code.
2. **Given** an error, no secret in it.

## Measure

Errors with codes.

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

⬅️ [REQ-T05-02 Paging, filters, idempotency](req-t05-02-paging-and-idempotency.md) · ⬆️ [Up](README.md) ·
➡️ [REQ-T05-04 Signed webhooks](req-t05-04-signed-webhooks.md)
