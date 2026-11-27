🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
🛍️ [F11 Online shop (plugin)](../README.md) › 📏 [Business rules](README.md) ›
📏 BR-F11-03 The withdrawal function is always available

# 📏 BR-F11-03 The withdrawal function is always available

**Status:** ✅ specified

## Statement

A consumer withdraws from the account or a public form at any time, receives an acknowledgement on a durable medium, and
is refunded within the country pack's period; in France:
[CR-FR-036 Consumer withdrawal right](../../../10-country-packs/france/consumer/cr-fr-036-withdrawal-right.md).

## Why

See [D308](../../../06-decisions/f11-online-shop/d308-online-shop-coverage.md).

## Examples

| Case | Result |
|---|---|
| Withdrawal on day 12 | Accepted, acknowledged, refund within 14 days |
| Personalised product | Refused, the exception named |

## Applies to

Every F11 use case concerned.

## Exceptions

None.

## Configurable

Exceptions per product (the country pack's list).

## Open questions

None.

---

⬅️ [BR-F11-02 The order button states the obligation to pay](br-f11-02-order-button-states-the-obligation-to-pay.md) ·
⬆️ [Up](README.md) · ➡️ [BR-F11-04 Prices with taxes and delivery](br-f11-04-prices-with-taxes-and-delivery.md)
