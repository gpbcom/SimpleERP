🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
📦 [F7 Purchasing and stock](../README.md) › 📏 [Business rules](README.md) ›
📏 BR-F7-14 Safety stock triggers a suggestion

# 📏 BR-F7-14 Safety stock triggers a suggestion

**Status:** ✅ specified

## Statement

When an item's forecast stock at a location goes under its safety stock, a replenishment suggestion up to its maximum
appears; a minimum above the maximum is refused.

## Why

Explicit levels per item make replenishment predictable (D464).

## Examples

| Case | Result |
|---|---|
| Forecast 35, safety 40, max 300 | Suggest 265 |
| Min 300, max 200 | Refused |

## Applies to

- [UC-F7-21 Set safety stock and min/max per item](../use-cases/03-replenish/uc-f07-21-set-safety-stock-and-min-max-per-item.md)

## Exceptions

None.

## Configurable

No.

## Open questions

None.

---

⬅️ [BR-F7-13](br-f07-13-catalogue-and-punch-out-carts-become-requests.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F7-15](br-f07-15-eco-contributions-are-shown-apart-and-declared.md)
