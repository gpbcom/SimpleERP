🏠 [Specs](../../../README.md) › ⚙️ [Technical capabilities](../../README.md) ›
📚 [T8 RAG platform (Milvus)](../README.md) › 🗃️ [Data](README.md) › 🗃️ E-T08-01 Collection

# 🗃️ E-T08-01 Collection

**Status:** ✅ specified

## Purpose

A vector collection.

## Fields

| Name | Type | Required | Validation | Default | Example | Personal data | Custom fields |
|---|---|---|---|---|---|---|---|
| owner, kind | records | yes | REQ-T08-01 | - | Acme, company | no | no |

The main fields only; the rest is generated from the code (D406).

## Relations

As its interfaces.

## Lifecycle

```mermaid
stateDiagram-v2
  [*] --> Active : REQ-T08-01
```

## Indexes and search

By company and id.

## Retention

Kept for the period of its kind of record in the country pack (D293), or else its kind's default in the
[retention schedule](../../../05-non-functional/data-retention.md).

## Audit

Every change (T3).

## Import and export

With the company's export (T1).

## Used by

- [T8 requirements](../requirements/README.md)

## Open questions

None.

---

⬆️ [Up](README.md) · ➡️ [E-T08-02 Chunk](e-t08-02-chunk.md)
