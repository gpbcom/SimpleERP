🏠 [Specs](../../../README.md) › ⚙️ [Technical capabilities](../../README.md) ›
📚 [T8 RAG platform (Milvus)](../README.md) › 📌 [Requirements](README.md) › 📌 REQ-T08-06 Retrieval quality measured

# 📌 REQ-T08-06 Retrieval quality measured

**Status:** ✅ specified

## Statement

Retrieval quality is part of each feature's evaluation set.

## Why

Confirmed by the owner on 2026-11-12; D417.

## Acceptance criteria

1. **Given** a retrieval change, measured.
2. **Given** quality below threshold, release blocked.

## Measure

Recall at k.

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

⬅️ [REQ-T08-05 Index rebuild](req-t08-05-index-rebuild.md) · ⬆️ [Up](README.md)
