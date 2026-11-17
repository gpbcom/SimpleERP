🏠 [Specs](../../../README.md) › ⚙️ [Technical capabilities](../../README.md) › 🏛️ [T11 Legal corpora](../README.md) ›
📌 [Requirements](README.md) › 📌 REQ-T11-02 One rules library by date

# 📌 REQ-T11-02 One rules library by date

**Status:** ✅ specified

## Statement

One rules library reads values by the date of the fact.

## Why

Confirmed by the owner on 2026-11-12; D405.

## Acceptance criteria

1. **Given** an invoice of last year, last year's rate.
2. **Given** a future-dated rule, applied from its date.

## Measure

Rule reads.

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

⬅️ [REQ-T11-01 Signed, versioned packs](req-t11-01-signed-packs.md) · ⬆️ [Up](README.md) ·
➡️ [REQ-T11-03 Law ingested and versioned](req-t11-03-law-ingestion.md)
