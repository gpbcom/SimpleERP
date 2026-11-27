🏠 [Specs](../../../README.md) › 🏷️ [Sectors](../../README.md) › 🎭 [SC16 Events and culture](../README.md) ›
🗃️ [Data](README.md) › 🗃️ E-SC16-11 Sponsorship

# 🗃️ E-SC16-11 Sponsorship

**Status:** ✅ specified

## Purpose

A sponsor's contract and benefits.

## Fields

| Name | Type | Required | Validation | Default | Example | Personal data | Custom fields |
|---|---|---|---|---|---|---|---|
| sponsor, amount, benefits | records | yes | - | - | Acme, 15 000, logo and 20 tickets | no | no |

## Relations

As its use cases.

## Lifecycle

```mermaid
stateDiagram-v2
  [*] --> Active : UC-SC16-10
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

- [UC-SC16-10](../use-cases/03-people-and-partners/uc-sc16-10-manage-sponsors-and-partners.md)

## Open questions

None.

---

⬅️ [E-SC16-10 Staffing post](e-sc16-10-staffing-post.md) · ⬆️ [Up](README.md) ·
➡️ [E-SC16-12 Stand](e-sc16-12-stand.md)
