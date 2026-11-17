🏠 [Specs](../../README.md) › 📜 [Decisions](../README.md) › 🧭 [Decisions: Foundations](README.md) ›
📜 D28 Legal assistant

# 📜 D28 Legal assistant

**Status:** ✅ decided

## Context

The owner asked for a feature other ERPs do not have (ticket GH-2).

## Options

- Not discussed: the owner stated it.

## Choice

A RAG over the law of each enabled country, France first, connected to the chatbot, that checks the rights of both the
employees and the company (F15, with T11 for the legal corpora).

## Decided by

The owner, on 2026-11-10, in the specification interview.

## Consequences

See the related pages.

## Related

- [F15 Legal assistant](../../02-functional/f15-legal-assistant/README.md)
- [T11 Legal corpora](../../03-technical/t11-legal-corpora/README.md)

---

⬅️ [D27 RAG platform on Milvus](d27-rag-platform-on-milvus.md) · ⬆️ [Up](README.md) ·
➡️ [D29 Social media module](d29-social-media-module.md)
