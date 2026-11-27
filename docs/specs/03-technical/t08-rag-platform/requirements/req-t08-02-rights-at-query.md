🏠 [Specs](../../../README.md) › ⚙️ [Technical capabilities](../../README.md) ›
📚 [T8 RAG platform (Milvus)](../README.md) › 📌 [Requirements](README.md) › 📌 REQ-T08-02 Rights at query time

# 📌 REQ-T08-02 Rights at query time

**Status:** ✅ specified

## Statement

A search never returns what the user may not read.

## Why

Confirmed by the owner on 2026-11-12; D414.

## Acceptance criteria

1. **Given** a record outside the user's rights, not returned.
2. **Given** rights changed, the next search follows.

## Measure

Leak tests.

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

⬅️ [REQ-T08-01 Milvus collections](req-t08-01-milvus-collections.md) · ⬆️ [Up](README.md) ·
➡️ [REQ-T08-03 Changes and erasures followed](req-t08-03-changes-followed.md)
