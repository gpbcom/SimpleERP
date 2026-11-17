🏠 [Specs](../../../README.md) › 🏷️ [Sectors](../../README.md) › 🌾 [SC13 Agriculture and food](../README.md) ›
🗃️ [Data](README.md) › 🗃️ E-SC13-03 Field operation

# 🗃️ E-SC13-03 Field operation

**Status:** 🔄 waiting for the owner

## Purpose

A treatment or fertilisation.

## Fields

| Name | Type | Required | Validation | Default | Example | Personal data | Custom fields |
|---|---|---|---|---|---|---|---|
| plot, date, product, dose | records | yes | BR-SC13-02 | - | Les Prés, 3 Apr, product X, 1 l/ha | no | no |
| operator | person | yes | - | - | U40 | yes | no |

## Relations

(Proposed) As its use cases.

## Lifecycle

```mermaid
stateDiagram-v2
  [*] --> Active : BR-SC13-02
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

- [UC-SC13-02](../use-cases/01-crops/uc-sc13-02-record-treatments-and-inputs.md)
- [UC-SC13-03](../use-cases/01-crops/uc-sc13-03-record-fertilisation-and-the-nitrogen-plan.md)
- [UC-SC13-20](../use-cases/03-farm-business/uc-sc13-20-ask-the-assistant.md)

## Open questions

None.

---

⬅️ [E-SC13-02 Crop plan](e-sc13-02-crop-plan.md) · ⬆️ [Up](README.md) · ➡️ [E-SC13-04 Lot](e-sc13-04-lot.md)
