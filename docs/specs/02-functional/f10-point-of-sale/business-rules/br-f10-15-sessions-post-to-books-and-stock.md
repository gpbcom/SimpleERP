🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
🏪 [F10 Point of sale (plugin)](../README.md) › 📏 [Business rules](README.md) ›
📏 BR-F10-15 Closed sessions post to the books and stock

# 📏 BR-F10-15 Closed sessions post to the books and stock

**Status:** ✅ specified

## Statement

Closing a session posts its sales, payments and VAT to accounting (F8), per payment method, and its stock moves (F7).

## Why

See [D295](../../../06-decisions/f10-point-of-sale/d295-pos-coverage.md).

## Examples

| Case | Result |
|---|---|
| Session closed | One entry per payment method, stock moved |

## Applies to

Every F10 use case concerned.

- [UC-F10-24 Match card-terminal settlements net of fees](../use-cases/09-cash-and-settlements/uc-f10-24-match-card-terminal-settlements-net-of-fees.md)

- [UC-F10-28 Read hourly sales, staff performance and basket analysis](../use-cases/11-store-reports/uc-f10-28-read-hourly-sales-staff-performance-and-basket-analysis.md)

## Exceptions

None.

## Configurable

Journals and accounts per point of sale.

## Open questions

None.

---

⬅️ [BR-F10-14 Training mode is marked](br-f10-14-training-mode-is-marked.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F10-16 Meal vouchers pay food within the daily cap](br-f10-16-meal-vouchers-pay-food-within-the-daily-cap.md)
