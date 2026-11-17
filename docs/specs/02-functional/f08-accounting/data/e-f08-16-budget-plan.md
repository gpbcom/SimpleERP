🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) › 📒 [F8 Accounting](../README.md) ›
🗃️ [Data](README.md) › 🗃️ E-F8-16 Budget plan

# 🗃️ E-F8-16 Budget plan

**Status:** ✅ specified

## Purpose

A budget plan or forecast scenario.

## Fields

| Name | Type | Required | Validation | Default | Example | Personal data | Custom fields |
|---|---|---|---|---|---|---|---|
| scenario | text | yes | - | - | Base 2027 | no | no |
| drivers | lines | yes | - | - | Headcount, prices | no | no |

## Relations

As its use cases.

## Lifecycle

```mermaid
stateDiagram-v2
  [*] --> Active : UC-F8-19
```

## Indexes and search

By name, date, owner.

## Retention

Kept for the period of its kind of record in the country pack (D293), or else its kind's default in the
[retention schedule](../../../05-non-functional/data-retention.md). See
[CR-FR-002 Accounting records kept 10 years](../../../10-country-packs/france/accounting/cr-fr-002-accounting-records-kept-ten-years.md).

## Audit

Every change.

## Import and export

CSV.

## Used by

- [UC-F8-19](../use-cases/06-benchmark-additions/uc-f08-19-plan-and-forecast.md)

## Open questions

None.

---

⬅️ [E-F8-15 Company card](e-f08-15-company-card.md) · ⬆️ [Up](README.md) ·
➡️ [E-F8-17 Client money ledger](e-f08-17-client-money-ledger.md)
