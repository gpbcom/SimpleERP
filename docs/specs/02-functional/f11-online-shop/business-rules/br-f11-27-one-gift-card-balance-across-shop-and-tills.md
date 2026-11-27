🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
🛍️ [F11 Online shop (plugin)](../README.md) › 📏 [Business rules](README.md) ›
📏 BR-F11-27 One gift-card balance across shop and tills

# 📏 BR-F11-27 One gift-card balance across shop and tills

**Status:** ✅ specified

## Statement

A gift card has one balance, kept once, that is used and reduced in the same way online and at every till, and no amount
above the balance can be spent on any channel; a use on one channel is visible on the other within seconds, and a card
past its validity or blocked is refused everywhere.

## Why

A card whose balance differs between the shop and the till is spent twice. The holder expects one card, one balance. The
owner's answer: "Gift cards online"
([D530](../../../06-decisions/f11-online-shop/d530-benchmark-gaps-f11-online-shop.md)).

## Examples

| Case | Result |
|---|---|
| A card of 50 euros, 30 spent online | 20 euros at the till, 20 euros online |
| An order of 60 euros with a card of 50 | 50 from the card, 10 by another means |
| Two tills use the same card at once | the second is refused or reduced to what is left |
| A blocked card | refused online and at every till |
| A card at its end date | refused everywhere, balance treated per the legal rules |

## Applies to

- [UC-F11-32 Sell and redeem gift cards online](../use-cases/11-donations-gift-cards-and-cross-border/uc-f11-32-sell-and-redeem-gift-cards-online.md)
- [E-F11-26 Online gift card](../data/e-f11-26-online-gift-card.md)
- [UC-F10-07 Use loyalty, gift cards and e-wallet](../../f10-point-of-sale/use-cases/03-after-sales/uc-f10-07-use-loyalty-gift-cards-and-e-wallet.md)
- [E-F10-10 Loyalty card and gift card](../../f10-point-of-sale/data/e-f10-10-loyalty-card-and-gift-card.md)

## Exceptions

A refund of a purchase paid with a card returns to that card.

## Configurable

Yes: amounts offered, the validity and the wrong-try limit are set per shop.

## Open questions

None.

---

⬅️ [BR-F11-26 Wishlists are private unless shared](br-f11-26-wishlists-are-private-unless-shared.md) ·
⬆️ [Up](README.md) ·
➡️ [BR-F11-28 VAT follows the customer's country under OSS](br-f11-28-vat-follows-the-customers-country-under-oss.md)
