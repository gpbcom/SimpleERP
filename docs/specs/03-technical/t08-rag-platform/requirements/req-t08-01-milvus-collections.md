🏠 [Specs](../../../README.md) › ⚙️ [Technical capabilities](../../README.md) ›
📚 [T8 RAG platform (Milvus)](../README.md) › 📌 [Requirements](README.md) › 📌 REQ-T08-01 Milvus collections

# 📌 REQ-T08-01 Milvus collections

**Status:** ✅ specified

## Statement

Milvus standalone on every profile, a collection per company, one shared read-only collection for the law.

Milvus runs where the AI or semantic search is on; with the AI turned off it is optional and not installed (D22).

## Why

Confirmed by the owner on 2026-11-12; D409.

## Acceptance criteria

1. **Given** a new company, its collection created.
2. **Given** the law collection, read-only for all.

## Measure

Collections.

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

⬆️ [Up](README.md) · ➡️ [REQ-T08-02 Rights at query time](req-t08-02-rights-at-query.md)
