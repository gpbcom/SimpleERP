🏠 [Specs](../../../README.md) › 🏷️ [Sectors](../../README.md) › 🍽️ [SC06 Restaurant and hospitality](../README.md) ›
🗃️ [Data](README.md) › 🗃️ E-SC06-04 Waste record

# 🗃️ E-SC06-04 Waste record

**Status:** 🔄 waiting for the owner

## Purpose

Food thrown or given.

## Fields

| Name | Type | Required | Validation | Default | Example | Personal data | Custom fields |
|---|---|---|---|---|---|---|---|
| product, quantity | records | yes | - | - | salad, 2 kg | no | no |
| reason | expired, spoiled, donated | yes | - | - | expired | no | no |

## Relations

(Proposed) As its use cases.

## Lifecycle

```mermaid
stateDiagram-v2
  [*] --> Recorded : UC-SC06-04
```

## Indexes and search

(Proposed) By number, date, partner.

## Retention

Kept for the period of its kind of record in the country pack (D293), or else its kind's default in the
[retention schedule](../../../05-non-functional/data-retention.md).

## Audit

Every change.

## Import and export

(Proposed) CSV, FEC where relevant.

## Used by

- [UC-SC06-04](../use-cases/02-kitchen-stock-and-staff/uc-sc06-04-manage-perishables-waste-and-counts.md)

## Open questions

None.

---

⬅️ [E-SC06-03 Hygiene record](e-sc06-03-hygiene-record.md) · ⬆️ [Up](README.md) ·
➡️ [E-SC06-05 Staff benefit](e-sc06-05-staff-benefit.md)
