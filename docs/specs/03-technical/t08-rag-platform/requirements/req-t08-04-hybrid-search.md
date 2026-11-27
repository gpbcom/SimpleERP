🏠 [Specs](../../../README.md) › ⚙️ [Technical capabilities](../../README.md) ›
📚 [T8 RAG platform (Milvus)](../README.md) › 📌 [Requirements](README.md) › 📌 REQ-T08-04 Hybrid search on CPU

# 📌 REQ-T08-04 Hybrid search on CPU

**Status:** ✅ specified

## Statement

Dense and keyword search with a local reranker on CPU.

## Why

Confirmed by the owner on 2026-11-12; D417.

## Acceptance criteria

1. **Given** a query with a code, keyword hit.
2. **Given** a vague question, dense hit.

## Measure

Recall.

## Priority

Must

## Capabilities served

F3, F15

## Tests

Unit and contract tests of the service that implements it; isolation, policy and evaluation tests where it applies
(D426).

## Open questions

None.

---

⬅️ [REQ-T08-03 Changes and erasures followed](req-t08-03-changes-followed.md) · ⬆️ [Up](README.md) ·
➡️ [REQ-T08-05 Index rebuild](req-t08-05-index-rebuild.md)
