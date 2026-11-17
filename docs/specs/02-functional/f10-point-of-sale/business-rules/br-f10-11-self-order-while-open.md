🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
🏪 [F10 Point of sale (plugin)](../README.md) › 📏 [Business rules](README.md) ›
📏 BR-F10-11 Self-order only while the session is open

# 📏 BR-F10-11 Self-order only while the session is open

**Status:** ✅ specified

## Statement

QR and kiosk orders are taken only while the point of sale has an open session; a kiosk takes no cash.

## Why

See [D295](../../../06-decisions/f10-point-of-sale/d295-pos-coverage.md).

## Examples

| Case | Result |
|---|---|
| QR order after closing | Menu shown, ordering off |

## Applies to

Every F10 use case concerned.

## Exceptions

None.

## Configurable

Ordering mode: menu only, order, order and pay.

## Open questions

None.

---

⬅️ [BR-F10-10 Orders go to their preparation station](br-f10-10-orders-routed-to-their-station.md) ·
⬆️ [Up](README.md) ·
➡️ [BR-F10-12 Loyalty needs a customer, vouchers follow VAT rules](br-f10-12-loyalty-and-vouchers.md)
