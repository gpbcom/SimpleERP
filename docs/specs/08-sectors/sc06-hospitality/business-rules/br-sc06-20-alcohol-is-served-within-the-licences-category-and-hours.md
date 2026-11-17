🏠 [Specs](../../../README.md) › 🏷️ [Sectors](../../README.md) › 🍽️ [SC06 Restaurant and hospitality](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-SC06-20 Alcohol is served within the licence's category and hours

# 📏 BR-SC06-20 Alcohol is served within the licence's category and hours

**Status:** 🔄 waiting for the owner

## Statement

Alcohol is served only within the category and the hours of the venue's active licence. A sale outside the category
(spirits under a licence for beer and wine, or alcohol without a meal under a meals-only licence) or outside the hours
is refused and recorded.

## Why

Serving outside the licence exposes the owner to fines and to the loss of the licence, and the till is the only place
that can stop the sale. The owner asked for alcohol licences
([D550](../../../06-decisions/sectors/d550-benchmark-gaps-sc06-hospitality.md)). (Proposed) The France-pack rule is
written later.

## Examples

| Case | Result |
|---|---|
| Beer at 14:00 under an active category III licence | sold |
| Cocktail at 03:10 with hours to 02:00 | refused |
| Spirits with no meal under a meals-only licence | refused |
| Expired licence | no alcohol for the venue |
| Permit ending in 80 days | sold, and the owner is warned |

## Applies to

- [UC-SC06-20](../use-cases/06-campsites-catering-groups-and-pricing/uc-sc06-20-keep-alcohol-licences-current.md)
- [E-SC06-17 Licence](../data/e-sc06-17-licence.md)
- [E-F10-16 Age check](../../../02-functional/f10-point-of-sale/data/e-f10-16-age-check.md)
- France-pack rule, (Proposed) until its law is read:
  [CR-FR-235 Alcohol licences and opening hours](../../../10-country-packs/france/hospitality/cr-fr-235-alcohol-licences.md)

## Exceptions

None.

## Configurable

The hours per weekday and the warning delay, by the owner.

## Open questions

None.

---

⬅️ [BR-SC06-19](br-sc06-19-dynamic-prices-stay-within-floor-and-ceiling.md) · ⬆️ [Up](README.md) ·
➡️ [BR-SC06-21 Allergies are shown at every order](br-sc06-21-allergies-are-shown-at-every-order.md)
