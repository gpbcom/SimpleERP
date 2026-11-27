🏠 [Specs](../../README.md) › 📜 [Decisions](../README.md) › 🛒 [Decisions: F6 Customers and sales](README.md) ›
📜 D253 Online payments

# 📜 D253 Online payments

**Status:** ✅ decided

## Context

How customers pay online.

## Options

- Providers the company picks.
- SEPA only.
- No online payment.

## Choice

The company connects the providers it uses: cards and wallets (Stripe, Mollie, PayPal), SEPA direct debit (GoCardless),
bank transfer with a reference; card numbers never reach SimpleERP; payments are reconciled automatically.

## Decided by

The owner, on 2026-11-10, in the specification interview.

## Consequences

BR-F6-02; PCI DSS scope kept minimal (D241); connectors in T12, keys in the vault (D240).

## Related

- [F6 Customers and sales](../../02-functional/f06-customers-and-sales/README.md)

---

⬅️ [D252 The customer portal](d252-customer-portal.md) · ⬆️ [Up](README.md) ·
➡️ [D254 Quote acceptance](d254-quote-acceptance.md)
