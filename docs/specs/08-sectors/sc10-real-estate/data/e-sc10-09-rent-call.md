🏠 [Specs](../../../README.md) › 🏷️ [Sectors](../../README.md) › 🏘️ [SC10 Real estate](../README.md) ›
🗃️ [Data](README.md) › 🗃️ E-SC10-09 Rent call

# 🗃️ E-SC10-09 Rent call

**Status:** 🔄 waiting for the owner

## Purpose

A monthly call and its payment.

## Fields

| Name | Type | Required | Validation | Default | Example | Personal data | Custom fields |
|---|---|---|---|---|---|---|---|
| lease, month | records | yes | - | - | S. Roux, Dec | yes | no |
| rent, charges, paid | amounts | yes | BR-SC10-05 | - | 800, 90, 890 | no | no |

## Relations

(Proposed) As its use cases.

## Lifecycle

```mermaid
stateDiagram-v2
  [*] --> Recorded : UC-SC10-08
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

- [UC-SC10-08](../use-cases/04-rents-and-landlords/uc-sc10-08-call-rents-and-issue-receipts.md)
- [UC-SC10-14](../use-cases/04-rents-and-landlords/uc-sc10-14-handle-unpaid-rents.md)
- [UC-SC10-19](../use-cases/06-portal-and-assistant/uc-sc10-19-give-landlords-tenants-and-co-owners-their-portal.md)

## Open questions

None.

---

⬅️ [E-SC10-08 Deposit](e-sc10-08-deposit.md) · ⬆️ [Up](README.md) ·
➡️ [E-SC10-10 Charge settlement](e-sc10-10-charge-settlement.md)
