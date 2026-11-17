🏠 [Specs](../../../README.md) › ⚙️ [Technical capabilities](../../README.md) › 🧾 [T3 Audit trail](../README.md) ›
🗃️ [Data](README.md) › 🗃️ E-T03-03 Chain checkpoint

# 🗃️ E-T03-03 Chain checkpoint

**Status:** ✅ specified

## Purpose

A verified point of a company's chain.

## Fields

| Name | Type | Required | Validation | Default | Example | Personal data | Custom fields |
|---|---|---|---|---|---|---|---|
| company, entry, hash, checked at | records | yes | REQ-T03-02 | - | Acme, E-900, h900, 02:00 | no | no |

The main fields only; the rest is generated from the code (D406).

## Relations

As its interfaces.

## Lifecycle

```mermaid
stateDiagram-v2
  [*] --> Recorded : REQ-T03-02
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

- [T3 requirements](../requirements/README.md)

## Open questions

None.

---

⬅️ [E-T03-02 AI action detail](e-t03-02-ai-action-detail.md) · ⬆️ [Up](README.md)
