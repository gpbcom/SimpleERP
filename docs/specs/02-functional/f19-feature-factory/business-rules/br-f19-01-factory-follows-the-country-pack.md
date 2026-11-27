🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
🏭 [F19 Feature factory (hosted edition)](../README.md) › 📏 [Business rules](README.md) ›
📏 BR-F19-01 Prices and credits follow the country pack

# 📏 BR-F19-01 Prices and credits follow the country pack

**Status:** ✅ specified

## Statement

Every legal value of the factory's billing (VAT, credit notes, invoice mentions, reverse charge, e-invoicing) comes from
the country pack; in France:
[CR-FR-205 VAT on the promotion credit](../../../10-country-packs/france/tax-and-vat/cr-fr-205-promotion-credit-vat-treatment.md),
[CR-FR-200 Credit notes and corrective invoices](../../../10-country-packs/france/invoicing/cr-fr-200-credit-notes.md),
[CR-FR-202 Price reductions on invoices](../../../10-country-packs/france/invoicing/cr-fr-202-price-reductions-on-invoices.md),
[CR-FR-201 Self-billing](../../../10-country-packs/france/invoicing/cr-fr-201-self-billing.md),
[CR-FR-015 Mandatory invoice mentions](../../../10-country-packs/france/invoicing/cr-fr-015-invoice-mandatory-mentions.md),
[CR-FR-100 VAT on services to clients abroad](../../../10-country-packs/france/tax-and-vat/cr-fr-100-vat-on-services-abroad.md).

## Why

See [D390](../../../06-decisions/f19-feature-factory/d390-feature-price-and-promotion-credit.md).

## Examples

| Case | Result |
|---|---|
| Customer in Germany with a VAT number | Reverse charge mention |

## Applies to

Every F19 use case concerned.

- [UC-F19-25 Post feature invoices, credits and refunds to accounting](../use-cases/05-bill-and-credit/uc-f19-25-post-feature-invoices-credits-and-refunds-to-accounting.md)

## Exceptions

None.

## Configurable

No.

## Open questions

None.

---

⬆️ [Up](README.md) · ➡️ [BR-F19-02 A feature is a plugin, never a core change](br-f19-02-feature-is-a-plugin.md)
