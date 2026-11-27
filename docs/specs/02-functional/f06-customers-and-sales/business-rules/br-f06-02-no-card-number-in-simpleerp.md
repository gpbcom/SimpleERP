🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
🛒 [F6 Customers and sales](../README.md) › 📏 [Business rules](README.md) › 📏 BR-F6-02 No card number in SimpleERP

# 📏 BR-F6-02 No card number in SimpleERP

**Status:** ✅ specified

## Statement

Online payments go through the providers the company connects; SimpleERP never receives, stores or logs a card number,
only the provider's payment reference and status; payments are matched to invoices automatically, and unmatched ones
listed.

## Why

Keeps PCI DSS scope minimal (D241). See [D253](../../../06-decisions/f06-customers-and-sales/d253-online-payments.md).

## Examples

| Case | Result |
|---|---|
| A card payment on the portal | Stripe's page takes the card; SimpleERP gets the payment status and marks the invoice paid |
| A transfer with the invoice number in its reference | Matched automatically |

## Applies to

Every F6 use case concerned.

## Exceptions

None.

## Configurable

Yes: the providers per company.

## Open questions

None.

---

⬅️ [BR-F6-01 Acceptance is proven](br-f06-01-acceptance-is-proven.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F6-03 The portal shows only the customer's own](br-f06-03-portal-shows-only-the-customer-s-own.md)
