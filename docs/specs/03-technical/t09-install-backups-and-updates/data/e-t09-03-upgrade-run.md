🏠 [Specs](../../../README.md) › ⚙️ [Technical capabilities](../../README.md) ›
🚀 [T9 Install, backups and updates](../README.md) › 🗃️ [Data](README.md) › 🗃️ E-T09-03 Upgrade run

# 🗃️ E-T09-03 Upgrade run

**Status:** ✅ specified

## Purpose

An upgrade and its result.

## Fields

| Name | Type | Required | Validation | Default | Example | Personal data | Custom fields |
|---|---|---|---|---|---|---|---|
| from, to, copy result, live result | records | yes | REQ-T09-05 | - | 3.3, 3.4, passed, passed | no | no |

The main fields only; the rest is generated from the code (D406).

## Relations

As its interfaces.

## Lifecycle

```mermaid
stateDiagram-v2
  [*] --> Recorded : REQ-T09-05
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

- [T9 requirements](../requirements/README.md)

## Open questions

None.

---

⬅️ [E-T09-02 Restore point](e-t09-02-restore-point.md) · ⬆️ [Up](README.md) ·
➡️ [E-T09-04 Namespace access grant](e-t09-04-namespace-access-grant.md)
