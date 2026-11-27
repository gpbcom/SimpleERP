🏠 [Specs](../../README.md) › 📜 [Decisions](../README.md) › 🛒 [Decisions: F6 Customers and sales](README.md) ›
📜 D260 VAT configurable

# 📜 D260 VAT configurable

**Status:** ✅ decided

## Context

The owner: "The VAT must be configurable".

## Options

- Configurable by accounting and administrators.
- Fixed French rates.

## Choice

Configurable: VAT rates with their validity dates per country; the rate per product or service category, changeable per
line; the VAT regime per customer (normal, exempt, reverse charge, intra-EU, export, OSS for EU consumers); the legal
mention per regime; VAT due on payment (services) or on invoice (goods, or the option for debits) per company; amounts
shown excluding or including VAT per document type and per user.

## Decided by

The owner, on 2026-11-10, in the specification interview.

## Consequences

BR-F6-08's settings, kept by accounting (U05) and administrators (U07); a rate change applies from its date, never to
issued invoices; F8 posts VAT per rate and regime.

## Related

- [D259](d259-vat-visible.md)
- [F6 Customers and sales](../../02-functional/f06-customers-and-sales/README.md)
- [F8 Accounting](../../02-functional/f08-accounting/README.md)

---

⬅️ [D259 VAT visible](d259-vat-visible.md) · ⬆️ [Up](README.md) ·
➡️ [D261 Going automatic](../f16-customer-support-agents/d261-go-live-bar.md)
