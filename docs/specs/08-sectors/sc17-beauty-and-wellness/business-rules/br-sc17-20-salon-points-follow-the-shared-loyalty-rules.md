🏠 [Specs](../../../README.md) › 🏷️ [Sectors](../../README.md) › 💇 [SC17 Beauty and wellness](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-SC17-20 Salon points follow the shared loyalty rules

# 📏 BR-SC17-20 Salon points follow the shared loyalty rules

**Status:** ✅ specified

## Statement

The salon's points and rewards follow the loyalty rules shared with the point of sale: the same card, the same balance
and the same expiry in every salon and till of the company, and a referral reward is given only for a first visit of a
person who was not a client.

## Why

Separate loyalty schemes per salon confuse clients and split their points. The owner asked for loyalty and referrals
([D561](../../../06-decisions/sectors/d561-benchmark-gaps-sc17-beauty-and-wellness.md)).

## Examples

| Case | Result |
|---|---|
| 1 point per euro, sale of 73 EUR | 73 points |
| Same client in two salons | one balance |
| Refunded sale | points removed |
| Referral of an existing client | no reward |
| Reward reached | offered at the next sale |

## Applies to

- [UC-SC17-20](../use-cases/05-rentals-care-records-and-loyalty/uc-sc17-20-run-loyalty-and-referrals.md)
- [E-F10-10](../../../02-functional/f10-point-of-sale/data/e-f10-10-loyalty-card-and-gift-card.md)

## Exceptions

None.

## Configurable

The rates, the reward and the expiry of points, by the manager within the shared rules.

## Open questions

None.

---

⬅️ [BR-SC17-19](br-sc17-19-photos-are-kept-only-with-the-clients-consent.md) · ⬆️ [Up](README.md)
