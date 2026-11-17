🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
🛍️ [F11 Online shop (plugin)](../README.md) › 📏 [Business rules](README.md) ›
📏 BR-F11-04 Prices with taxes and delivery

# 📏 BR-F11-04 Prices with taxes and delivery

**Status:** ✅ specified

## Statement

Consumers see prices including VAT and the delivery cost before ordering; a B2B website may show prices excluding VAT;
in France:
[CR-FR-034 Consumers see prices including VAT](../../../10-country-packs/france/consumer/cr-fr-034-prices-shown-including-vat.md),
[CR-FR-065 Information before an online order](../../../10-country-packs/france/consumer/cr-fr-065-online-pre-contract-information.md).

## Why

See [D308](../../../06-decisions/f11-online-shop/d308-online-shop-coverage.md).

## Examples

| Case | Result |
|---|---|
| B2C site | 24.00 EUR incl. VAT, delivery 4.90 EUR shown |
| B2B site | 20.00 EUR excl. VAT |

## Applies to

Every F11 use case concerned.

- [UC-F11-24 Publish product feeds to shopping comparators](../use-cases/08-product-content-and-listings/uc-f11-24-publish-product-feeds-to-shopping-comparators.md)

## Exceptions

None.

## Configurable

B2C or B2B per website.

## Open questions

None.

---

⬅️ [BR-F11-03 The withdrawal function is always available](br-f11-03-withdrawal-function-always-available.md) ·
⬆️ [Up](README.md) ·
➡️ [BR-F11-05 Reductions show the reference price](br-f11-05-reductions-show-the-reference-price.md)
