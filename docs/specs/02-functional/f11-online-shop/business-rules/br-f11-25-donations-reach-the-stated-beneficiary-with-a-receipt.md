🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
🛍️ [F11 Online shop (plugin)](../README.md) › 📏 [Business rules](README.md) ›
📏 BR-F11-25 Donations reach the stated beneficiary with a receipt

# 📏 BR-F11-25 Donations reach the stated beneficiary with a receipt

**Status:** ✅ specified

## Statement

A donation is shown at checkout with the name of its beneficiary, is kept apart from the sale and its VAT, is paid on in
full to that beneficiary on the dates set, and, when the beneficiary may issue tax receipts, is receipted to the donor;
a donation never goes to a beneficiary other than the one shown.

## Why

Donors trust the shop to pass their gift on. A donation that is mixed with sales, or kept, or sent elsewhere, breaks
that trust and the receipt rules. The owner's answer: "Donations at checkout"
([D530](../../../06-decisions/f11-online-shop/d530-benchmark-gaps-f11-online-shop.md)).

## Examples

| Case | Result |
|---|---|
| 2 euros to Cats Shelter | paid on in full to Cats Shelter, never to another beneficiary |
| The beneficiary may issue receipts | a receipt goes to the donor |
| The beneficiary may not issue receipts | a confirmation with no tax mention |
| The order is withdrawn before the payment to the beneficiary | the donation is refunded |
| A round-up of 0.40 euros | a donation line of 0.40 euros, no VAT |

## Applies to

- [UC-F11-30 Accept donations at checkout](../use-cases/11-donations-gift-cards-and-cross-border/uc-f11-30-accept-donations-at-checkout.md)
- [E-F11-24 Donation](../data/e-f11-24-donation.md)
- [UC-F11-05 Check out](../use-cases/02-shop-and-check-out/uc-f11-05-check-out.md)

## Exceptions

A donation already passed on is not refunded with a withdrawn order.

## Configurable

Yes: the amounts offered, the dates of payment to the beneficiary and the campaign period are set per campaign.

## Open questions

None.

---

⬅️ [BR-F11-24 Shop reports respect tracker consent](br-f11-24-shop-reports-respect-tracker-consent.md) ·
⬆️ [Up](README.md) ·
➡️ [BR-F11-26 Wishlists are private unless shared](br-f11-26-wishlists-are-private-unless-shared.md)
