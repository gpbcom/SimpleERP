🏠 [Specs](../../../README.md) › 🏷️ [Sectors](../../README.md) › 🍽️ [SC06 Restaurant and hospitality](../README.md) ›
🗃️ [Data](README.md) › 🗃️ E-SC06-03 Hygiene record

# 🗃️ E-SC06-03 Hygiene record

**Status:** 🔄 waiting for the owner

## Purpose

A reading or check.

## Fields

| Name | Type | Required | Validation | Default | Example | Personal data | Custom fields |
|---|---|---|---|---|---|---|---|
| kind, place | records | yes | - | - | temperature, cold room | no | no |
| value, time, by | records | yes | BR-SC06-05 | - | 2 °C, 08:00, A. V. | no | no |

## Relations

(Proposed) As its use cases.

## Lifecycle

```mermaid
stateDiagram-v2
  [*] --> Recorded : UC-SC06-03
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

- [UC-SC06-03](../use-cases/01-menus-and-food-safety/uc-sc06-03-keep-food-hygiene-records.md)

## Open questions

None.

---

⬅️ [E-SC06-02 Menu dish](e-sc06-02-menu-dish.md) · ⬆️ [Up](README.md) ·
➡️ [E-SC06-04 Waste record](e-sc06-04-waste-record.md)
