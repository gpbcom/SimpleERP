🏠 [Specs](../../../README.md) › ⚙️ [Technical capabilities](../../README.md) › 🔗 [T5 API and webhooks](../README.md) ›
📌 [Requirements](README.md) › 📌 REQ-T05-02 Paging, filters, idempotency

# 📌 REQ-T05-02 Paging, filters, idempotency

**Status:** ✅ specified

## Statement

Lists use cursor paging, filters and sorting; writes accept an idempotency key.

## Why

Confirmed by the owner on 2026-11-12; D410.

## Acceptance criteria

1. **Given** a write repeated with its key, done once.
2. **Given** a list of a million rows, paged.

## Measure

Duplicate writes.

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

⬅️ [REQ-T05-01 REST with OpenAPI behind one gateway](req-t05-01-rest-openapi.md) · ⬆️ [Up](README.md) ·
➡️ [REQ-T05-03 problem+json errors](req-t05-03-problem-json.md)
