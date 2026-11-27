🏠 [Specs](../../../README.md) › 🏷️ [Sectors](../../README.md) › 🍽️ [SC06 Restaurant and hospitality](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-SC06-19 Dynamic prices stay within floor and ceiling

# 📏 BR-SC06-19 Dynamic prices stay within floor and ceiling

**Status:** ✅ specified

## Statement

A price computed by a dynamic rule is never below the floor nor above the ceiling set for its room type. A price outside
the limits is cut to the nearest limit and the cut is recorded with the rule that caused it.

## Why

A rule that follows demand with no limit can sell a room for nothing or at a price that drives guests away. The owner
asked for dynamic pricing ([D550](../../../06-decisions/sectors/d550-benchmark-gaps-sc06-hospitality.md)).

## Examples

| Case | Result |
|---|---|
| Computed 149.50, limits 90.00 to 190.00 | 149.50 |
| Computed 210.00, ceiling 190.00 | 190.00, cut recorded |
| Computed 70.00, floor 90.00 | 90.00, cut recorded |
| Two rules on one night | higher priority first |
| Paused rule | base rate |

## Applies to

- [UC-SC06-19](../use-cases/06-campsites-catering-groups-and-pricing/uc-sc06-19-set-prices-dynamically.md)
- [E-SC06-16 Price rule](../data/e-sc06-16-price-rule.md)
- [E-SC06-07 Rate plan](../data/e-sc06-07-rate-plan.md)

## Exceptions

None.

## Configurable

The floor, the ceiling and the priority of each rule, by the owner.

## Open questions

None.

---

⬅️ [BR-SC06-18](br-sc06-18-room-blocks-are-released-at-the-cut-off-date.md) · ⬆️ [Up](README.md) ·
➡️ [BR-SC06-20](br-sc06-20-alcohol-is-served-within-the-licences-category-and-hours.md)
