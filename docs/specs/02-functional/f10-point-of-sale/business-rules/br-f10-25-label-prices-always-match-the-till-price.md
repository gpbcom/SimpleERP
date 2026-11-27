🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
🏪 [F10 Point of sale (plugin)](../README.md) › 📏 [Business rules](README.md) ›
📏 BR-F10-25 Label prices always match the till price

# 📏 BR-F10-25 Label prices always match the till price

**Status:** ✅ specified

## Statement

The price, unit price and promotion shown on an electronic label must equal those of the till; when a label cannot be
brought to the till price within the delay set, it is flagged Mismatch, the till warns the sellers, and the price at the
till is the price charged unless the law or the shop's terms say that the lower shelf price must be honoured.

## Why

A shelf price that differs from the till breaks the price display rules and starts disputes at the checkout. The owner's
answer: "Electronic shelf labels"
([D529](../../../06-decisions/f10-point-of-sale/d529-benchmark-gaps-f10-point-of-sale.md)).

## Examples

| Case | Result |
|---|---|
| The till price changes to 6.90 | the label shows 6.90 within the delay |
| The label connector is down for an hour | labels are flagged, the till warns |
| A label shows 7.90 and the till 6.90 | Mismatch, the shop honours the lower price at the till |
| A promotion ends at midnight | labels return to the normal price after midnight |
| A label with no unit price on a weighed product | flagged to complete the product |

## Applies to

- [UC-F10-31 Update electronic shelf labels](../use-cases/12-takeaway-softpos-and-labels/uc-f10-31-update-electronic-shelf-labels.md)
- [E-F10-23 Shelf label](../data/e-f10-23-shelf-label.md)
- [UC-F10-06 Apply prices, promotions and combos](../use-cases/02-sell-at-the-counter/uc-f10-06-apply-prices-promotions-and-combos.md)

## Exceptions

A label of a product sold only on request, with no shelf price, is not required.

## Configurable

Yes: the update delay and the choice of honouring the lower price are set per shop.

## Open questions

None.

---

⬅️ [BR-F10-24](br-f10-24-tap-to-pay-follows-the-card-terminal-rules-and-the-till-log.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F10-26](br-f10-26-layaway-deposits-are-refunded-per-the-shops-terms.md)
