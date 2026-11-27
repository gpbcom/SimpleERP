🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
🏪 [F10 Point of sale (plugin)](../README.md) › 📏 [Business rules](README.md) ›
📏 BR-F10-12 Loyalty needs a customer, vouchers follow VAT rules

# 📏 BR-F10-12 Loyalty needs a customer, vouchers follow VAT rules

**Status:** ✅ specified

## Statement

Rewards need an identified customer; a gift card or voucher bears VAT by its kind; in France:
[CR-FR-013 VAT on gift cards and vouchers](../../../10-country-packs/france/tax-and-vat/cr-fr-013-vouchers-vat.md).

## Why

See [D295](../../../06-decisions/f10-point-of-sale/d295-pos-coverage.md).

## Examples

| Case | Result |
|---|---|
| Reward with no customer | Asks to identify the customer |

## Applies to

Every F10 use case concerned.

- [UC-F10-25 Serve a customer with their profile](../use-cases/10-clienteling-transfers-and-tax-free/uc-f10-25-serve-a-customer-with-their-profile.md)

## Exceptions

None.

## Configurable

Programmes, points, rewards, validity.

## Open questions

None.

---

⬅️ [BR-F10-11 Self-order only while the session is open](br-f10-11-self-order-while-open.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F10-13 Delivery orders through connectors](br-f10-13-delivery-orders-through-connectors.md)
