🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) › 👥 [F9 HR and projects](../README.md) ›
🗃️ [Data](README.md) › 🗃️ E-F9-15 Visitor

# 🗃️ E-F9-15 Visitor

**Status:** ✅ specified

## Purpose

A visitor at a station.

## Fields

| Name | Type | Required | Validation | Default | Example | Personal data | Custom fields |
|---|---|---|---|---|---|---|---|
| name, company | text | yes | - | - | J. Durand, Durand SA | yes | no |
| host | employee | yes | - | - | Léa Moreau | no | no |
| in, out | times | yes | - | - | 10:02 to 11:15 | no | no |

## Relations

As its use cases.

## Lifecycle

```mermaid
stateDiagram-v2
  [*] --> Checked : UC-F9-14
  Checked --> Planned : UC-F9-14
```

## Indexes and search

By number, date, partner.

## Retention

Kept for the period of its kind of record in the France country pack, not the accounting one. See
[CR-FR-047 HR records retention](../../../10-country-packs/france/labour/cr-fr-047-hr-records-retention.md).

## Audit

Every change.

## Import and export

CSV, FEC where relevant.

## Used by

- [UC-F9-14](../use-cases/05-workplace-services/uc-f09-14-welcome-visitors.md)

## Open questions

None.

---

⬅️ [E-F9-14 Approval request](e-f09-14-approval-request.md) · ⬆️ [Up](README.md) ·
➡️ [E-F9-16 Shift](e-f09-16-shift.md)
