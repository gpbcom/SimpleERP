🏠 [Specs](../../../README.md) › 🏷️ [Sectors](../../README.md) › 🍽️ [SC06 Restaurant and hospitality](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-SC06-21 Allergies are shown at every order

# 📏 BR-SC06-21 Allergies are shown at every order

**Status:** 🔄 waiting for the owner

## Statement

The allergies of a guest are shown at the top of every order taken for them, in the restaurant, the bar and room
service, and a dish that contains one of them triggers a warning before the order is sent to the kitchen.

## Why

An allergy known to the hotel but not shown to the waiter is the usual cause of a serious incident. The owner asked for
guest profiles ([D550](../../../06-decisions/sectors/d550-benchmark-gaps-sc06-hospitality.md)).

## Examples

| Case | Result |
|---|---|
| Guest allergic to peanuts, order opened | the allergy is shown in red |
| Dish with peanuts added to the order | a warning before sending |
| New allergy told to the waiter | added at once to the open order |
| Guest who refused to be kept | only the allergies of the stay |
| Profile anonymised | no allergy shown for a later order |

## Applies to

- [UC-SC06-21](../use-cases/06-campsites-catering-groups-and-pricing/uc-sc06-21-know-the-guest.md)
- [E-SC06-18 Guest profile](../data/e-sc06-18-guest-profile.md)
- [E-F10-03](../../../02-functional/f10-point-of-sale/data/e-f10-03-point-of-sale-order.md)

## Exceptions

None.

## Configurable

The retention period of the profile, by the owner within the limit of the country pack.

## Open questions

None.

---

⬅️ [BR-SC06-20](br-sc06-20-alcohol-is-served-within-the-licences-category-and-hours.md) · ⬆️ [Up](README.md)
