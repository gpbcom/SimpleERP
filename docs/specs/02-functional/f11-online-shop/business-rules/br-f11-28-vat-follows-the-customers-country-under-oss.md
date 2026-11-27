🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
🛍️ [F11 Online shop (plugin)](../README.md) › 📏 [Business rules](README.md) ›
📏 BR-F11-28 VAT follows the customer's country under OSS

# 📏 BR-F11-28 VAT follows the customer's country under OSS

**Status:** ✅ specified

## Statement

For a sale to a consumer in another EU country, the VAT rate is that of the customer's country of delivery when the
one-stop-shop scheme applies to the shop, the order records that country and rate, and the VAT is declared for each
country; a delivery country that is not open for sale is refused at checkout.

## Why

Charging the wrong country's VAT, or none, exposes the shop to back taxes and to penalties in several countries. The
owner's answer: "Cross-border selling"
([D530](../../../06-decisions/f11-online-shop/d530-benchmark-gaps-f11-online-shop.md)).

## Examples

| Case | Result |
|---|---|
| A shopper in Germany, delivery to Berlin | German VAT is applied and declared for Germany |
| A shopper in France | French VAT |
| A delivery to a country not open | refused at checkout with the countries served |
| A delivery outside the EU | no EU VAT on the goods, duties shown before payment |
| A change of the German rate | applies to orders from its date, with the history kept |

## Applies to

- [UC-F11-33 Sell across borders](../use-cases/11-donations-gift-cards-and-cross-border/uc-f11-33-sell-across-borders.md)
- [E-F11-27 Country price list](../data/e-f11-27-country-price-list.md)
- [UC-F11-05 Check out](../use-cases/02-shop-and-check-out/uc-f11-05-check-out.md)

## Exceptions

A shop below the EU-wide distance-sales threshold may keep its home VAT; the France pack says when.

## Configurable

Yes: countries, rates and the choice of the scheme are set by the accountant, with the history kept.

## Open questions

None.

---

⬅️ [BR-F11-27 One gift-card balance across shop and tills](br-f11-27-one-gift-card-balance-across-shop-and-tills.md) ·
⬆️ [Up](README.md)
