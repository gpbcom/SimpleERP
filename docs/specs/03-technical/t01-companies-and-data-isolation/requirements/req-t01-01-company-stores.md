🏠 [Specs](../../../README.md) › ⚙️ [Technical capabilities](../../README.md) ›
🏢 [T1 Companies and data isolation](../README.md) › 📌 [Requirements](README.md) ›
📌 REQ-T01-01 A database, bucket and vector collection per company

# 📌 REQ-T01-01 A database, bucket and vector collection per company

**Status:** ✅ specified

## Statement

Each company has its own PostgreSQL database, object-storage bucket and vector collection.

## Why

Confirmed by the owner on 2026-11-12; D19, D405, D409.

## Acceptance criteria

1. **Given** a new company is created, its three stores exist and no other company can reach them.
2. **Given** two companies, a query of one never returns a row of the other.

## Measure

Stores per company; isolation test pass rate.

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

⬆️ [Up](README.md) · ➡️ [REQ-T01-02 The company context at every layer](req-t01-02-company-context-everywhere.md)
