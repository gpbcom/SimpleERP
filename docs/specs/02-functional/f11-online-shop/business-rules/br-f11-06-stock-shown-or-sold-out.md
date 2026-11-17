🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
🛍️ [F11 Online shop (plugin)](../README.md) › 📏 [Business rules](README.md) › 📏 BR-F11-06 Stock shown or sold out

# 📏 BR-F11-06 Stock shown or sold out

**Status:** ✅ specified

## Statement

A product shows its availability; when out of stock it is sold out unless the product allows selling on order, and
customers may ask to be told when it is back.

## Why

See [D308](../../../06-decisions/f11-online-shop/d308-online-shop-coverage.md).

## Examples

| Case | Result |
|---|---|
| 0 in stock, no selling on order | Sold out, back-in-stock alert offered |

## Applies to

Every F11 use case concerned.

- [UC-F11-26 Take pre-orders and back-in-stock reservations](../use-cases/09-pre-orders-and-b2b-buying/uc-f11-26-take-pre-orders-and-back-in-stock-reservations.md)

## Exceptions

None.

## Configurable

Per product: continue selling, threshold shown.

## Open questions

None.

---

⬅️ [BR-F11-05 Reductions show the reference price](br-f11-05-reductions-show-the-reference-price.md) ·
⬆️ [Up](README.md) · ➡️ [BR-F11-07 Click & collect only where in stock](br-f11-07-click-and-collect-where-in-stock.md)
