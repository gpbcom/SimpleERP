🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
🏪 [F10 Point of sale (plugin)](../README.md) › 📏 [Business rules](README.md) ›
📏 BR-F10-17 Restricted items need an age check

# 📏 BR-F10-17 Restricted items need an age check

**Status:** ✅ specified

## Statement

A basket with an age-restricted item cannot be paid before the cashier records the age check; a refusal removes the item
and is logged.

## Why

Selling alcohol or tobacco to minors is an offence.

## Examples

| Case | Result |
|---|---|
| Wine scanned | Prompt |
| Under age | Item removed, logged |

## Applies to

- [UC-F10-22 Check age for restricted sales](../use-cases/08-vouchers-and-age-checks/uc-f10-22-check-age-for-restricted-sales.md)

## Exceptions

None.

## Configurable

No.

## Open questions

None.

---

⬅️ [BR-F10-16 Meal vouchers pay food within the daily cap](br-f10-16-meal-vouchers-pay-food-within-the-daily-cap.md) ·
⬆️ [Up](README.md) · ➡️ [BR-F10-18 Cash moves are counted by two](br-f10-18-cash-moves-are-counted-by-two.md)
