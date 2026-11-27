🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
🛍️ [F11 Online shop (plugin)](../README.md) › 📏 [Business rules](README.md) › 📏 BR-F11-14 Payment keys in the vault

# 📏 BR-F11-14 Payment keys in the vault

**Status:** ✅ specified

## Statement

Payment provider keys are stored in the vault (D240) and no card number ever reaches SimpleERP (D253).

## Why

See [D308](../../../06-decisions/f11-online-shop/d308-online-shop-coverage.md).

## Examples

| Case | Result |
|---|---|
| Provider set up | Key in the vault, only its reference in settings |

## Applies to

Every F11 use case concerned.

- [UC-F11-21 Screen orders for fraud and authenticate payments](../use-cases/07-payment-risk/uc-f11-21-screen-orders-for-fraud-and-authenticate-payments.md)

## Exceptions

None.

## Configurable

Providers per website.

## Open questions

None.

---

⬅️ [BR-F11-13 B2B prices for approved customers](br-f11-13-b2b-prices-for-approved-customers.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F11-15 Accepted terms are kept](br-f11-15-accepted-terms-are-kept.md)
