🏠 [Specs](../../../README.md) › 🏷️ [Sectors](../../README.md) › 🎭 [SC16 Events and culture](../README.md) ›
🗃️ [Data](README.md) › 🗃️ E-SC16-02 Event budget

# 🗃️ E-SC16-02 Event budget

**Status:** 🔄 waiting for the owner

## Purpose

Budget and actuals.

## Fields

| Name | Type | Required | Validation | Default | Example | Personal data | Custom fields |
|---|---|---|---|---|---|---|---|
| event, line, planned, actual | records | yes | - | - | Jazz Night, artists, 18 000, 17 400 | no | no |

## Relations

(Proposed) As its use cases.

## Lifecycle

```mermaid
stateDiagram-v2
  [*] --> Open : UC-SC16-01
  Open --> Approved : UC-SC16-01
  Approved --> Closed : UC-SC16-18
  Open --> Refused : UC-SC16-01
  Approved --> Refused : UC-SC16-01
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

- [UC-SC16-01](../use-cases/01-plan-and-book/uc-sc16-01-plan-an-event-and-its-budget.md)
- [UC-SC16-18](../use-cases/05-declarations-and-reports/uc-sc16-18-report-after-the-event.md)

## Open questions

None.

---

⬅️ [E-SC16-01 Show](e-sc16-01-show.md) · ⬆️ [Up](README.md) · ➡️ [E-SC16-03 Venue room](e-sc16-03-venue-room.md)
