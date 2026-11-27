🏠 [Specs](../../../README.md) › ⚙️ [Technical capabilities](../../README.md) ›
📚 [T8 RAG platform (Milvus)](../README.md) › 📌 [Requirements](README.md) › 📌 REQ-T08-03 Changes and erasures followed

# 📌 REQ-T08-03 Changes and erasures followed

**Status:** ✅ specified

## Statement

Changes and erasures follow from the databases through events.

## Why

Confirmed by the owner on 2026-11-12; D405.

## Acceptance criteria

1. **Given** a record erased, gone from search.
2. **Given** a record changed, re-indexed.

## Measure

Index lag.

## Priority

Must

## Capabilities served

F3

## Tests

Unit and contract tests of the service that implements it; isolation, policy and evaluation tests where it applies
(D426).

## Open questions

None.

---

⬅️ [REQ-T08-02 Rights at query time](req-t08-02-rights-at-query.md) · ⬆️ [Up](README.md) ·
➡️ [REQ-T08-04 Hybrid search on CPU](req-t08-04-hybrid-search.md)
