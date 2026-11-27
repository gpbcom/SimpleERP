🏠 [Specs](../../../README.md) › ⚙️ [Technical capabilities](../../README.md) ›
🏢 [T1 Companies and data isolation](../README.md) › 📌 [Requirements](README.md) ›
📌 REQ-T01-02 The company context at every layer

# 📌 REQ-T01-02 The company context at every layer

**Status:** ✅ specified

## Statement

The company context is checked at the gateway, in each service and in storage, with row-level security as a second
guard.

## Why

Confirmed by the owner on 2026-11-12; D405.

## Acceptance criteria

1. **Given** a request without a company, it is refused at the gateway.
2. **Given** a service bug forgets the filter, row-level security still refuses the row.

## Measure

Isolation tests per service.

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

⬅️ [REQ-T01-01 A database, bucket and vector collection per company](req-t01-01-company-stores.md) ·
⬆️ [Up](README.md) · ➡️ [REQ-T01-03 Provider access visible and audited](req-t01-03-provider-access-visible.md)
