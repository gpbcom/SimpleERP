🏠 [Specs](../../README.md) › 📜 [Decisions](../README.md) › 🛍️ [Decisions: F11 Online shop (plugin)](README.md) ›
📜 D530 Benchmark gaps of F11 Online shop

# 📜 D530 Benchmark gaps of F11 Online shop

**Status:** ✅ specified

## Context

The 2026-11-14 benchmark-gaps interview compared the specifications with the e-commerce features of the benchmarked
suites and offered each gap as an option
([interview record](../../../tickets/GH-2/interviews/2026-11-14-benchmark-gaps.md), section "F11 Online shop").

## Options

- Take each gap as a use case of F11 in a new flow, or leave it out.
- Where a gap overlaps an existing use case, extend that use case or add a new one.

## Choice

The owner selected all four gaps; each becomes a use case of F11, drawn in
[FL-F11-11 Donations, wishlists, gift cards and cross-border](../../02-functional/f11-online-shop/flows/fl-f11-11-donations-gift-cards-and-cross-border.md).

| Gap | Use case | The owner's answer |
|---|---|---|
| G67 | [UC-F11-30 Accept donations at checkout](../../02-functional/f11-online-shop/use-cases/11-donations-gift-cards-and-cross-border/uc-f11-30-accept-donations-at-checkout.md) | "Donations at checkout" |
| G68 | [UC-F11-31 Keep wishlists and compare products](../../02-functional/f11-online-shop/use-cases/11-donations-gift-cards-and-cross-border/uc-f11-31-keep-wishlists-and-compare-products.md) | "Wishlists and compare" |
| G69 | [UC-F11-32 Sell and redeem gift cards online](../../02-functional/f11-online-shop/use-cases/11-donations-gift-cards-and-cross-border/uc-f11-32-sell-and-redeem-gift-cards-online.md) | "Gift cards online" |
| G70 | [UC-F11-33 Sell across borders](../../02-functional/f11-online-shop/use-cases/11-donations-gift-cards-and-cross-border/uc-f11-33-sell-across-borders.md) | "Cross-border selling" |

## Decided by

The owner, on 2026-11-14, in the benchmark-gaps interview
([interview record](../../../tickets/GH-2/interviews/2026-11-14-benchmark-gaps.md), section "Block by block").

## Consequences

- Use cases
  [UC-F11-30 Accept donations at checkout](../../02-functional/f11-online-shop/use-cases/11-donations-gift-cards-and-cross-border/uc-f11-30-accept-donations-at-checkout.md)
  to
  [UC-F11-33 Sell across borders](../../02-functional/f11-online-shop/use-cases/11-donations-gift-cards-and-cross-border/uc-f11-33-sell-across-borders.md),
  screens
  [S-F11-29 Checkout donations](../../02-functional/f11-online-shop/screens/11-donations-gift-cards-and-cross-border/s-f11-29-checkout-donations.md)
  to
  [S-F11-32 Cross-border](../../02-functional/f11-online-shop/screens/11-donations-gift-cards-and-cross-border/s-f11-32-cross-border.md),
  rules
  [BR-F11-25 Donations reach the stated beneficiary with a receipt](../../02-functional/f11-online-shop/business-rules/br-f11-25-donations-reach-the-stated-beneficiary-with-a-receipt.md)
  to
  [BR-F11-28 VAT follows the customer's country under OSS](../../02-functional/f11-online-shop/business-rules/br-f11-28-vat-follows-the-customers-country-under-oss.md),
  entities [E-F11-24 Donation](../../02-functional/f11-online-shop/data/e-f11-24-donation.md) to
  [E-F11-27 Country price list](../../02-functional/f11-online-shop/data/e-f11-27-country-price-list.md) and their lists
  [S-F11-L24 Donations](../../02-functional/f11-online-shop/screens/00-lists/s-f11-l24-donations.md) to
  [S-F11-L27 Country price lists](../../02-functional/f11-online-shop/screens/00-lists/s-f11-l27-country-price-lists.md).
- The online gift card
  [E-F11-26 Online gift card](../../02-functional/f11-online-shop/data/e-f11-26-online-gift-card.md) and the till card
  [E-F10-10 Loyalty card and gift card](../../02-functional/f10-point-of-sale/data/e-f10-10-loyalty-card-and-gift-card.md)
  share one balance.
- The one-stop-shop declaration and threshold need a France pack rule, written later.

## Related

- [FL-F11-11 Donations, wishlists, gift cards and cross-border](../../02-functional/f11-online-shop/flows/fl-f11-11-donations-gift-cards-and-cross-border.md)
- [D458 F1 Administration: gaps and improvements](../f01-administration/d458-f01-gaps-and-improvements.md)
- [Interview record](../../../tickets/GH-2/interviews/2026-11-14-benchmark-gaps.md)

---

⬅️ [D529 Benchmark gaps of F10 Point of sale](../f10-point-of-sale/d529-benchmark-gaps-f10-point-of-sale.md) ·
⬆️ [Up](README.md) ·
➡️ [D531 Benchmark gaps of F12 Manufacturing](../f12-manufacturing/d531-benchmark-gaps-f12-manufacturing.md)
