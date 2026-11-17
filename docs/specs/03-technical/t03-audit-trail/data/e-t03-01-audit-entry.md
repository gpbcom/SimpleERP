🏠 [Specs](../../../README.md) › ⚙️ [Technical capabilities](../../README.md) › 🧾 [T3 Audit trail](../README.md) ›
🗃️ [Data](README.md) › 🗃️ E-T03-01 Audit entry

# 🗃️ E-T03-01 Audit entry

**Status:** ✅ specified

## Purpose

One recorded action.

## Fields

| Name | Type | Required | Validation | Default | Example | Personal data | Custom fields |
|---|---|---|---|---|---|---|---|
| who, what, when, before, after, hash, previous hash | records | yes | REQ-T03-01 | - | U-9, quote Q-88 sent, 10:02, ..., h2, h1 | yes | no |

The main fields only; the rest is generated from the code (D406).

## Relations

As its interfaces.

## Lifecycle

```mermaid
stateDiagram-v2
  [*] --> Recorded : REQ-T03-01
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

⬆️ [Up](README.md) · ➡️ [E-T03-02 AI action detail](e-t03-02-ai-action-detail.md)
