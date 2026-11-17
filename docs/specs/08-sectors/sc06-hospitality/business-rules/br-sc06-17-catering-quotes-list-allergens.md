🏠 [Specs](../../../README.md) › 🏷️ [Sectors](../../README.md) › 🍽️ [SC06 Restaurant and hospitality](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-SC06-17 Catering quotes list allergens

# 📏 BR-SC06-17 Catering quotes list allergens

**Status:** 🔄 waiting for the owner

## Statement

A catering quote lists the allergens of every dish it contains, taken from the dish's recipe. A dish whose allergens are
not entered cannot be added to a quote, and the allergen list sent with the quote is the one kept with the order.

## Why

The customer decides for their guests from the quote, and an allergen missing on the quote harms someone far from the
kitchen. The owner asked for catering ([D550](../../../06-decisions/sectors/d550-benchmark-gaps-sc06-hospitality.md)).

## Examples

| Case | Result |
|---|---|
| Dish with allergens in its recipe | listed on the quote |
| Dish with no allergen list | cannot be added |
| Recipe changed after the quote | the customer is told and the quote is sent again |
| Vegetarian variant | its own allergen list |
| Allergen list sent | kept with the order |

## Applies to

- [UC-SC06-17](../use-cases/06-campsites-catering-groups-and-pricing/uc-sc06-17-quote-and-deliver-catering.md)
- [E-SC06-14 Catering order](../data/e-sc06-14-catering-order.md)
- [E-SC06-02 Menu dish](../data/e-sc06-02-menu-dish.md)

## Exceptions

None.

## Configurable

The allergen wording per language, in the settings.

## Open questions

None.

---

⬅️ [BR-SC06-16 Pitch prices follow the season grid](br-sc06-16-pitch-prices-follow-the-season-grid.md) ·
⬆️ [Up](README.md) · ➡️ [BR-SC06-18](br-sc06-18-room-blocks-are-released-at-the-cut-off-date.md)
