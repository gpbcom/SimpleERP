🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
🔭 [F17 Competitive analysis](../README.md) › 🗃️ [Data](README.md) › 🗃️ E-F17-12 Win-loss record

# 🗃️ E-F17-12 Win-loss record

**Status:** ✅ specified

## Purpose

A deal won or lost against a competitor.

## Fields

| Name | Type | Required | Validation | Default | Example | Personal data | Custom fields |
|---|---|---|---|---|---|---|---|
| deal, competitor, outcome, reason | records | yes | BR-F17-12 | - | D-120, Rival SA, lost, price | no | no |

## Relations

As its use cases.

## Lifecycle

```mermaid
stateDiagram-v2
  [*] --> Recorded : UC-F17-14
```

## Indexes and search

By number, date, partner.

## Retention

Kept for the period of its kind of record in the country pack (D293), or else its kind's default in the
[retention schedule](../../../05-non-functional/data-retention.md).

## Audit

Every change.

## Import and export

CSV, FEC where relevant.

## Used by

- [UC-F17-14](../use-cases/03-analyse-and-arm-sales/uc-f17-14-analyse-wins-and-losses.md)

## Open questions

None.

---

⬅️ [E-F17-11 Battle card](e-f17-11-battle-card.md) · ⬆️ [Up](README.md) · ➡️ [E-F17-13 Alert](e-f17-13-alert.md)
