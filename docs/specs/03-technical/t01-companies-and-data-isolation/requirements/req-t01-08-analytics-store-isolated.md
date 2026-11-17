🏠 [Specs](../../../README.md) › ⚙️ [Technical capabilities](../../README.md) ›
🏢 [T1 Companies and data isolation](../README.md) › 📌 [Requirements](README.md) ›
📌 REQ-T01-08 The analytics store kept apart and erasable

# 📌 REQ-T01-08 The analytics store kept apart and erasable

**Status:** ✅ specified

## Statement

The columnar analytics store keeps each company in its own database or partition, reached only with the company context;
a company's export and deletion (REQ-T01-07) and a person's erasure reach it, by deleting the rows or rebuilding them
from the events.

## Why

Confirmed by the owner on 2026-11-12; D19, D408; the review of 2026-11-12 (R25).

## Acceptance criteria

1. **Given** two companies in the analytics store, a query of one never returns a row of the other.
2. **Given** a person erased, their rows are gone from the analytics store.

## Measure

Isolation and erasure test pass rate.

## Priority

Must

## Capabilities served

F17, F22, F23 and every report (TC-15)

## Tests

Unit and contract tests of the service that implements it; isolation, policy and evaluation tests where it applies
(D426).

## Open questions

None.

---

⬅️ [REQ-T01-07 A whole company exported or deleted](req-t01-07-company-export-and-deletion.md) · ⬆️ [Up](README.md)
