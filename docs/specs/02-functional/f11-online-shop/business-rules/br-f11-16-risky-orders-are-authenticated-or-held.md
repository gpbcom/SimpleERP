🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
🛍️ [F11 Online shop (plugin)](../README.md) › 📏 [Business rules](README.md) ›
📏 BR-F11-16 Risky orders are authenticated or held

# 📏 BR-F11-16 Risky orders are authenticated or held

**Status:** ✅ specified

## Statement

Each order is scored; strong authentication is asked where the rules or a medium risk require it, and a high-risk order
is held until a person accepts or cancels it.

## Why

Fraud costs goods and chargeback fees.

## Examples

| Case | Result |
|---|---|
| Foreign card, new account | 3-D Secure |
| 3 orders in 10 minutes | Held |

## Applies to

- [UC-F11-21 Screen orders for fraud and authenticate payments](../use-cases/07-payment-risk/uc-f11-21-screen-orders-for-fraud-and-authenticate-payments.md)

## Exceptions

None.

## Configurable

No.

## Open questions

None.

---

⬅️ [BR-F11-15 Accepted terms are kept](br-f11-15-accepted-terms-are-kept.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F11-17](br-f11-17-chargebacks-are-answered-before-their-deadline.md)
