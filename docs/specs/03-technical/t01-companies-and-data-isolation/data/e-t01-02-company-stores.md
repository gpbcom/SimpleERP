🏠 [Specs](../../../README.md) › ⚙️ [Technical capabilities](../../README.md) ›
🏢 [T1 Companies and data isolation](../README.md) › 🗃️ [Data](README.md) › 🗃️ E-T01-02 Company stores

# 🗃️ E-T01-02 Company stores

**Status:** ✅ specified

## Purpose

Where a company's data lives.

## Fields

| Name | Type | Required | Validation | Default | Example | Personal data | Custom fields |
|---|---|---|---|---|---|---|---|
| database, bucket, vector collection, key ids | records | yes | REQ-T01-01 | - | acme_db, acme, acme, k-12 | no | no |

The main fields only; the rest is generated from the code (D406).

## Relations

As its interfaces.

## Lifecycle

```mermaid
stateDiagram-v2
  [*] --> Active : REQ-T01-01
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

- [T1 requirements](../requirements/README.md)

## Open questions

None.

---

⬅️ [E-T01-01 Company](e-t01-01-company.md) · ⬆️ [Up](README.md) ·
➡️ [E-T01-03 Provider session](e-t01-03-provider-session.md)
