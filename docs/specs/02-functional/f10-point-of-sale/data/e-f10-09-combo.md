🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
🏪 [F10 Point of sale (plugin)](../README.md) › 🗃️ [Data](README.md) › 🗃️ E-F10-09 Combo

# 🗃️ E-F10-09 Combo

**Status:** ✅ specified

## Purpose

A set of choices sold at a fixed price.

## Fields

| Name | Type | Required | Validation | Default | Example | Personal data | Custom fields |
|---|---|---|---|---|---|---|---|
| name | text | yes | - | - | Lunch menu | no | no |
| choices | groups with extra prices | yes | - | - | Starter, main, drink | no | no |
| price | money | yes | fixed | - | 15.90 | no | no |

## Relations

As its use cases.

## Lifecycle

```mermaid
stateDiagram-v2
  [*] --> Active : UC-F10-06
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

- [UC-F10-06](../use-cases/02-sell-at-the-counter/uc-f10-06-apply-prices-promotions-and-combos.md)

## Open questions

None.

---

⬅️ [E-F10-08 Price promotion](e-f10-08-price-promotion.md) · ⬆️ [Up](README.md) ·
➡️ [E-F10-10 Loyalty card and gift card](e-f10-10-loyalty-card-and-gift-card.md)
