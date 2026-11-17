🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
🏪 [F10 Point of sale (plugin)](../README.md) › 🗃️ [Data](README.md) › 🗃️ E-F10-06 Closure

# 🗃️ E-F10-06 Closure

**Status:** ✅ specified

## Purpose

A daily, monthly or yearly closure.

## Fields

| Name | Type | Required | Validation | Default | Example | Personal data | Custom fields |
|---|---|---|---|---|---|---|---|
| kind | day, month, year | yes | - | - | day | no | no |
| period | dates | yes | - | - | 2026-11-11 | no | no |
| totals | period and perpetual grand totals, per VAT rate | yes | BR-F10-01 | - | 3 214.80 / 812 455.20 | no | no |
| signature | hash | yes | chained | auto | 71ab... | no | no |

## Relations

As its use cases.

## Lifecycle

```mermaid
stateDiagram-v2
  [*] --> Active : BR-F10-01
```

## Indexes and search

By number, date, partner.

## Retention

Till data:
[CR-FR-029 Till data kept six years](../../../10-country-packs/france/point-of-sale/cr-fr-029-till-data-kept-six-years.md)
line by line; as an accounting record:
[CR-FR-002 Accounting records kept 10 years](../../../10-country-packs/france/accounting/cr-fr-002-accounting-records-kept-ten-years.md).

## Audit

Every change.

## Import and export

CSV, FEC where relevant.

## Used by

- [UC-F10-01](../use-cases/01-till-session/uc-f10-01-open-and-close-a-till-session.md)
- [UC-F10-18](../use-cases/07-set-up-and-report/uc-f10-18-report-sales-and-keep-the-legal-archives.md)

## Open questions

None.

---

⬅️ [E-F10-05 Receipt](e-f10-05-receipt.md) · ⬆️ [Up](README.md) · ➡️ [E-F10-07 Till archive](e-f10-07-till-archive.md)
