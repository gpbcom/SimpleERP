🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
🛍️ [F11 Online shop (plugin)](../README.md) › 📏 [Business rules](README.md) ›
📏 BR-F11-23 Stores fulfil only with stock and capacity

# 📏 BR-F11-23 Stores fulfil only with stock and capacity

**Status:** ✅ specified

## Statement

An online order is assigned to a store only if it has the stock and its daily capacity; the item is reserved at once.

## Why

A store must not promise what it cannot pick.

## Examples

| Case | Result |
|---|---|
| Capacity 20, 21st order | Not assigned |
| Sold at the counter | Next store |

## Applies to

- [UC-F11-28 Fulfil online orders from a store](../use-cases/10-fulfil-from-stores-and-report/uc-f11-28-fulfil-online-orders-from-a-store.md)

## Exceptions

None.

## Configurable

No.

## Open questions

None.

---

⬅️ [BR-F11-22](br-f11-22-b2b-requests-become-f6-quotes-punch-out-carts-go-back.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F11-24 Shop reports respect tracker consent](br-f11-24-shop-reports-respect-tracker-consent.md)
