🏠 [Specs](../../../README.md) › 🏷️ [Sectors](../../README.md) › 🌾 [SC13 Agriculture and food](../README.md) ›
🗃️ [Data](README.md) › 🗃️ E-SC13-01 Plot

# 🗃️ E-SC13-01 Plot

**Status:** 🔄 waiting for the owner

## Purpose

A farm plot.

## Fields

| Name | Type | Required | Validation | Default | Example | Personal data | Custom fields |
|---|---|---|---|---|---|---|---|
| name, area, location | records | yes | - | - | Les Prés, 4.2 ha | no | no |
| organic | yes, no, converting | yes | BR-SC13-08 | no | yes | no | no |

## Relations

(Proposed) As its use cases.

## Lifecycle

```mermaid
stateDiagram-v2
  [*] --> New : UC-SC13-01
  New --> Refused : UC-SC13-01
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

- [UC-SC13-01](../use-cases/01-crops/uc-sc13-01-map-plots-and-plan-crops.md)
- [UC-SC13-07](../use-cases/03-farm-business/uc-sc13-07-declare-cap-aid.md)

## Open questions

None.

---

⬆️ [Up](README.md) · ➡️ [E-SC13-02 Crop plan](e-sc13-02-crop-plan.md)
