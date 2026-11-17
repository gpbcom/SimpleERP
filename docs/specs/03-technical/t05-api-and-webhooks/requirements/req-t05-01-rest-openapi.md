🏠 [Specs](../../../README.md) › ⚙️ [Technical capabilities](../../README.md) › 🔗 [T5 API and webhooks](../README.md) ›
📌 [Requirements](README.md) › 📌 REQ-T05-01 REST with OpenAPI behind one gateway

# 📌 REQ-T05-01 REST with OpenAPI behind one gateway

**Status:** ✅ specified

## Statement

Each service publishes an OpenAPI generated from its code, behind one gateway, with the version in the path.

## Why

Confirmed by the owner on 2026-11-12; D406, D410.

## Acceptance criteria

1. **Given** a service starts, its OpenAPI is served.
2. **Given** a call to /v1, routed to the right service.

## Measure

Endpoints documented.

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

⬆️ [Up](README.md) · ➡️ [REQ-T05-02 Paging, filters, idempotency](req-t05-02-paging-and-idempotency.md)
