🏠 [Specs](../../../README.md) › 🏷️ [Sectors](../../README.md) › 🍽️ [SC06 Restaurant and hospitality](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-SC06-16 Pitch prices follow the season grid

# 📏 BR-SC06-16 Pitch prices follow the season grid

**Status:** 🔄 waiting for the owner

## Statement

The price of a pitch night is the price of the season in which that night falls, for the pitch's type and the number of
people, plus the options chosen. A stay over two seasons is priced night by night, and a night with no price in the grid
cannot be sold.

## Why

Pricing a whole stay at one season misprices the nights at the edge, and an unpriced night is sold at a guess. The owner
asked for campsites ([D550](../../../06-decisions/sectors/d550-benchmark-gaps-sc06-hospitality.md)).

## Examples

| Case | Result |
|---|---|
| Night in high season, caravan | the high-season price of the caravan type |
| Stay over mid and high season | each night at its own season |
| Night with no price in the grid | not sold |
| Extra person above the pitch's allowance | the extra person's price is added |
| Dog chosen as an option | the dog option is added per night |

## Applies to

- [UC-SC06-16](../use-cases/06-campsites-catering-groups-and-pricing/uc-sc06-16-rent-campsite-pitches.md)
- [E-SC06-13 Pitch](../data/e-sc06-13-pitch.md)
- [E-SC06-07 Rate plan](../data/e-sc06-07-rate-plan.md)

## Exceptions

None.

## Configurable

The seasons, their dates and the prices, by the owner.

## Open questions

None.

---

⬅️ [BR-SC06-15 Guest data kept no longer than needed](br-sc06-15-guest-data-kept-no-longer-than-needed.md) ·
⬆️ [Up](README.md) · ➡️ [BR-SC06-17 Catering quotes list allergens](br-sc06-17-catering-quotes-list-allergens.md)
