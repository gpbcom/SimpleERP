🏠 [Specs](../../README.md) › ⚙️ [Technical capabilities](../README.md) ›
🧗 [Technical challenges from the functional side](README.md) › 🏢 TC-01 Isolation of companies at every layer

# 🏢 TC-01 Isolation of companies at every layer

**Status:** ✅ listed for the technical interviews

## Challenge

Keep each company's data apart in every store and every path (database, files, search, vectors, caches, logs, AI
prompts, exports), whether one company runs alone, an IT provider hosts many, or the publisher hosts the hosted edition.

## Raised by

- [F1 Administration](../../02-functional/f01-administration/README.md)
- [F3 Assistant](../../02-functional/f03-assistant/README.md)
- [F14 Plugin store](../../02-functional/f14-plugin-store/README.md)
- [F18 Hosted websites and domains (hosted edition)](../../02-functional/f18-hosted-websites-and-domains/README.md)
- [F19 Feature factory (hosted edition)](../../02-functional/f19-feature-factory/README.md)
- [F20 Hosted support assistant (hosted edition)](../../02-functional/f20-hosted-support-assistant/README.md)
- [T1 Companies and data isolation](../t01-companies-and-data-isolation/README.md)
- [T8 RAG platform (Milvus)](../t08-rag-platform/README.md)

## Why it is hard

- One database per company multiplies migrations, connections and backups by the number of companies.
- The provider's administrator may enter any client company, and the hosted support assistant reads a customer's
  namespace: both cross the boundary on purpose and must be the only crossings.
- Shared corpora (the law, the public store) sit next to private data in the same search.

## Already decided

- [D1](../../06-decisions/foundations/d01-runs-for-a-company-or-a-provider.md) One company or an IT provider
- [D19](../../06-decisions/foundations/d19-one-database-per-company.md) One database per company
- [D393](../../06-decisions/f20-hosted-support-assistant/d393-hosted-support-assistant-coverage.md) Hosted support
  assistant: access and approvals

## Options to weigh

- Database per company, schema per company or rows with a company key, per store.
- One deployment per company, per provider or shared, and how the hosted edition maps customers to Kubernetes
  namespaces.
- Where the company context is enforced: gateway, service, storage, or all three.

## Settled in

- 19a Architecture and scalability ([chapter](../../../technical/architecture/architecture.md))
- 19c Storage ([chapter](../../../technical/data/storage.md))
- 19f Security ([chapter](../../../technical/security/security.md))
- Then the technical capabilities: [T1 Companies and data isolation](../t01-companies-and-data-isolation/README.md).

## Questions for the interview

- How many companies must one provider platform hold, and one hosted cluster?
- Is one database per company kept for the hosted edition, or only for self-hosting?

---

⬆️ [Up](README.md) ·
➡️ [TC-02 Modules switched on in one click, and a plugin-first core](tc-02-modules-and-plugins-at-runtime.md)
