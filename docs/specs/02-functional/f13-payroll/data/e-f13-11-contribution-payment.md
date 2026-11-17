🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) › 💶 [F13 Payroll (plugin)](../README.md) ›
🗃️ [Data](README.md) › 🗃️ E-F13-11 Contribution payment

# 🗃️ E-F13-11 Contribution payment

**Status:** ✅ specified

## Purpose

Contributions paid to a collector.

## Fields

| Name | Type | Required | Validation | Default | Example | Personal data | Custom fields |
|---|---|---|---|---|---|---|---|
| collector, period, amount | records | yes | - | - | social security, Nov, 41 200 | no | no |

## Relations

As its use cases.

## Lifecycle

```mermaid
stateDiagram-v2
  [*] --> Active : UC-F13-12
```

## Indexes and search

By number, date, partner.

## Retention

As an accounting record:
[CR-FR-002 Accounting records kept 10 years](../../../10-country-packs/france/accounting/cr-fr-002-accounting-records-kept-ten-years.md).

## Audit

Every change.

## Import and export

CSV, FEC where relevant.

## Used by

- [UC-F13-12](../use-cases/03-declarations-and-payments/uc-f13-12-pay-contributions-to-the-collectors.md)
- [UC-F13-25 Pay farm workers under the MSA](../use-cases/07-schemes-and-special-contracts/uc-f13-25-pay-farm-workers-under-the-msa.md)

## Open questions

None.

---

⬅️ [E-F13-10 Correction](e-f13-10-correction.md) · ⬆️ [Up](README.md) ·
➡️ [E-F13-12 Payroll entry](e-f13-12-payroll-entry.md)
