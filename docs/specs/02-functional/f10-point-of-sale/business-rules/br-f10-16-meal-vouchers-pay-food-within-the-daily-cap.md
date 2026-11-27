🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
🏪 [F10 Point of sale (plugin)](../README.md) › 📏 [Business rules](README.md) ›
📏 BR-F10-16 Meal vouchers pay food within the daily cap

# 📏 BR-F10-16 Meal vouchers pay food within the daily cap

**Status:** ✅ specified

## Statement

Meal vouchers pay only eligible food items, up to the legal daily cap per customer, never give change, and are refused
on Sundays and holidays unless the rule allows it.

## Why

Issuers refuse claims that break the rules (CR-FR-112).

## Examples

| Case | Result |
|---|---|
| 31.50 eligible, cap 25 | 25 by voucher |
| Paper 9.00 for 7.80 | No change |

## Applies to

- [UC-F10-21 Accept meal vouchers within the daily cap](../use-cases/08-vouchers-and-age-checks/uc-f10-21-accept-meal-vouchers-within-the-daily-cap.md)

## Exceptions

None.

## Configurable

The cap and days follow the country pack.

## Open questions

None.

---

⬅️ [BR-F10-15 Closed sessions post to the books and stock](br-f10-15-sessions-post-to-books-and-stock.md) ·
⬆️ [Up](README.md) ·
➡️ [BR-F10-17 Restricted items need an age check](br-f10-17-restricted-items-need-an-age-check.md)
