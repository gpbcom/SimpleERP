🏠 [Specs](../../../README.md) › ⚙️ [Technical capabilities](../../README.md) ›
📚 [T8 RAG platform (Milvus)](../README.md) › 🗃️ [Data](README.md) › 🗃️ E-T08-02 Chunk

# 🗃️ E-T08-02 Chunk

**Status:** ✅ specified

## Purpose

An indexed piece of a record or document.

## Fields

| Name | Type | Required | Validation | Default | Example | Personal data | Custom fields |
|---|---|---|---|---|---|---|---|
| source record, rights, vector, text | records | yes | REQ-T08-02 | - | INV-142, sales, ..., ... | yes | no |

The main fields only; the rest is generated from the code (D406).

## Relations

As its interfaces.

## Lifecycle

```mermaid
stateDiagram-v2
  [*] --> Active : REQ-T08-02
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

⬅️ [E-T08-01 Collection](e-t08-01-collection.md) · ⬆️ [Up](README.md) · ➡️ [E-T08-03 Index job](e-t08-03-index-job.md)
