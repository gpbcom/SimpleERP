🏠 [Specs](../../../README.md) › 🏷️ [Sectors](../../README.md) › 🩺 [SC09 Health practices](../README.md) ›
🗃️ [Data](README.md) › 🗃️ E-SC09-06 Insurer return

# 🗃️ E-SC09-06 Insurer return

**Status:** 🔄 waiting for the owner

## Purpose

A payment or rejection from an insurer.

## Fields

| Name | Type | Required | Validation | Default | Example | Personal data | Custom fields |
|---|---|---|---|---|---|---|---|
| care sheet, insurer | records | yes | - | - | CS-4471, CPAM | no | no |
| result, amount | paid or rejected, amount | yes | - | - | paid, 21.00 | no | no |

## Relations

(Proposed) As its use cases.

## Lifecycle

```mermaid
stateDiagram-v2
  [*] --> Matched : UC-SC09-07
  [*] --> Reconciled : UC-SC09-07
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

- [UC-SC09-07](../use-cases/03-insurance-billing/uc-sc09-07-handle-third-party-payment-and-insurers-returns.md)
- [UC-SC09-15](../use-cases/05-practice-organisation/uc-sc09-15-keep-practice-accounts.md)

## Open questions

None.

---

⬅️ [E-SC09-05 Care sheet](e-sc09-05-care-sheet.md) · ⬆️ [Up](README.md) ·
➡️ [E-SC09-07 Patient invoice](e-sc09-07-patient-invoice.md)
