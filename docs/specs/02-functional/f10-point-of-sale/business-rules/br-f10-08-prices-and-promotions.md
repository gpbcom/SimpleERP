🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
🏪 [F10 Point of sale (plugin)](../README.md) › 📏 [Business rules](README.md) ›
📏 BR-F10-08 Prices, promotions and reference prices

# 📏 BR-F10-08 Prices, promotions and reference prices

**Status:** ✅ specified

## Statement

The price comes from the pricelist rules; a combo has a fixed price; a promotion shown to consumers states its reference
price; in France:
[CR-FR-035 Reference price of a price reduction](../../../10-country-packs/france/consumer/cr-fr-035-reference-price-for-reductions.md),
[CR-FR-034 Consumers see prices including VAT](../../../10-country-packs/france/consumer/cr-fr-034-prices-shown-including-vat.md).

## Why

See [D295](../../../06-decisions/f10-point-of-sale/d295-pos-coverage.md).

## Examples

| Case | Result |
|---|---|
| -20 % shown | Reference price = lowest in the last 30 days |

## Applies to

Every F10 use case concerned.

## Exceptions

None.

## Configurable

Pricelists, promotions, combos.

## Open questions

None.

---

⬅️ [BR-F10-07 Paper receipts on request](br-f10-07-receipts-on-request.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F10-09 Weighed items come from the scale](br-f10-09-weighed-items-from-the-scale.md)
