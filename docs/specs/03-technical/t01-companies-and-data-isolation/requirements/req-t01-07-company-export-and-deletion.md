🏠 [Specs](../../../README.md) › ⚙️ [Technical capabilities](../../README.md) ›
🏢 [T1 Companies and data isolation](../README.md) › 📌 [Requirements](README.md) ›
📌 REQ-T01-07 A whole company exported or deleted

# 📌 REQ-T01-07 A whole company exported or deleted

**Status:** ✅ specified

## Statement

A whole company can be exported in open formats or deleted on request, except records the law keeps.

## Why

Confirmed by the owner on 2026-11-12; Data switching and erasure rules of the country pack.

## Acceptance criteria

1. **Given** an export is asked, every store is included.
2. **Given** a deletion is asked, legal records are kept and the rest erased.

## Measure

Export completeness.

## Priority

Must

## Capabilities served

F1, F21

## Tests

Unit and contract tests of the service that implements it; isolation, policy and evaluation tests where it applies
(D426).

## Open questions

None.

---

⬅️ [REQ-T01-06 A company created from a template in under a minute](req-t01-06-company-from-template.md) ·
⬆️ [Up](README.md) ·
➡️ [REQ-T01-08 The analytics store kept apart and erasable](req-t01-08-analytics-store-isolated.md)
