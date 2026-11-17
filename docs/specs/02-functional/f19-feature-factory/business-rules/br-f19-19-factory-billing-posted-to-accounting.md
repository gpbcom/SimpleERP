🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
🏭 [F19 Feature factory (hosted edition)](../README.md) › 📏 [Business rules](README.md) ›
📏 BR-F19-19 Factory billing posted to accounting

# 📏 BR-F19-19 Factory billing posted to accounting

**Status:** ✅ specified

## Statement

Every invoice, credit note and refund of the factory is posted to F8 with its revenue, VAT and receivable accounts, and
each payment is reconciled with its invoice; a credit note never pays out money (D390).

## Why

The factory's money must be in the books like any other (D476).

## Examples

| Case | Result |
|---|---|
| Invoice of 300.00 EUR plus 60.00 EUR VAT | passes: revenue 300.00, VAT 60.00, receivable 360.00 |
| Credit note of 150.00 EUR excluding VAT | passes: reduces revenue and VAT |
| Credit larger than the invoice | passes: rest carried forward, no payout |

## Applies to

- [UC-F19-25 Post feature invoices, credits and refunds to accounting](../use-cases/05-bill-and-credit/uc-f19-25-post-feature-invoices-credits-and-refunds-to-accounting.md)
- [UC-F19-26 Reconcile feature payments and follow up unpaid invoices](../use-cases/05-bill-and-credit/uc-f19-26-reconcile-feature-payments-and-follow-up-unpaid-invoices.md)
- [UC-F19-15 Receive the promotion credit](../use-cases/05-bill-and-credit/uc-f19-15-receive-the-promotion-credit.md)
- [UC-F19-16 Invoice features with the right VAT](../use-cases/05-bill-and-credit/uc-f19-16-invoice-features-with-the-right-vat.md)

## Exceptions

None.

## Configurable

The account mapping in F8.

## Open questions

None.

---

⬅️ [BR-F19-18 Security and privacy review before signing](br-f19-18-security-and-privacy-review-before-signing.md) ·
⬆️ [Up](README.md) ·
➡️ [BR-F19-20 Similar features are shown before any quote](br-f19-20-similar-features-are-shown-before-any-quote.md)
