🏠 [Specs](../../README.md) › ⚙️ [Technical capabilities](../README.md) ›
🧗 [Technical challenges from the functional side](README.md) › 📚 TC-08 Search and RAG that respect rights and erasure

# 📚 TC-08 Search and RAG that respect rights and erasure

**Status:** ✅ listed for the technical interviews

## Challenge

Index records, documents, meetings, attachments and the law so that a user never retrieves what they may not read, and
an erased record disappears from every index.

## Raised by

- [F3 Assistant](../../02-functional/f03-assistant/README.md)
- [F4 Meetings](../../02-functional/f04-meetings/README.md)
- [F15 Legal assistant](../../02-functional/f15-legal-assistant/README.md)
- [F17 Competitive analysis](../../02-functional/f17-competitive-analysis/README.md)
- [T8 RAG platform (Milvus)](../t08-rag-platform/README.md)

## Why it is hard

- Rights change after a document is indexed (a role change, a record rule).
- Each company has its own vectors, and the law is one shared, read-only corpus.
- Deletes and GDPR erasures must follow to the vector store, the keyword index and caches.

## Already decided

- [D19](../../06-decisions/foundations/d19-one-database-per-company.md) One database per company

## Options to weigh

- Filtering at query time by the user's rights, or indexes per role.
- Change data capture from the databases to the search stores.
- Hybrid search (dense and keyword) and reranking on CPU only.

## Settled in

- 19c Storage ([chapter](../../../technical/data/storage.md))
- 19i AI operations ([chapter](../../../technical/operations/ai-operations.md))
- Then the technical capabilities: [T8 RAG platform (Milvus)](../t08-rag-platform/README.md).

## Questions for the interview

- How fresh must search be after a change: seconds or minutes?
- Is a re-index from scratch acceptable as the recovery path?

---

⬅️ [TC-07 The AI assistant can do everything, within the user's rights](tc-07-ai-everywhere-within-rights.md) ·
⬆️ [Up](README.md) · ➡️ [TC-09 Local AI without a graphics card](tc-09-local-ai-without-a-graphics-card.md)
