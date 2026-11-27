🏠 [Specs](../../../README.md) › 🏷️ [Sectors](../../README.md) › 🩺 [SC09 Health practices](../README.md) ›
🗃️ [Data](README.md) › 🗃️ E-SC09-07 Patient invoice

# 🗃️ E-SC09-07 Patient invoice

**Status:** 🔄 waiting for the owner

## Purpose

What the patient pays.

## Fields

| Name | Type | Required | Validation | Default | Example | Personal data | Custom fields |
|---|---|---|---|---|---|---|---|
| patient, acts | records | yes | BR-SC09-04 | - | J. Martin, consultation | yes | no |
| amount, extra fee | amounts | yes | - | - | 30.00, 0 | no | no |

## Relations

(Proposed) As its use cases.

## Lifecycle

```mermaid
stateDiagram-v2
  [*] --> Active : BR-SC09-04
```

## Indexes and search

(Proposed) By number, date, partner.

## Retention

As an accounting record:
[CR-FR-002 Accounting records kept 10 years](../../../10-country-packs/france/accounting/cr-fr-002-accounting-records-kept-ten-years.md).

## Audit

Every change.

## Import and export

(Proposed) CSV, FEC where relevant.

## Used by

- [UC-SC09-08](../use-cases/03-insurance-billing/uc-sc09-08-bill-patients-and-show-fees.md)

## Open questions

None.

---

⬅️ [E-SC09-06 Insurer return](e-sc09-06-insurer-return.md) · ⬆️ [Up](README.md) ·
➡️ [E-SC09-08 Health exchange](e-sc09-08-health-exchange.md)
