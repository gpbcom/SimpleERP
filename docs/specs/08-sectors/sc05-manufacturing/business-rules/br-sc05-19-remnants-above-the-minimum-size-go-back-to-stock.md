🏠 [Specs](../../../README.md) › 🏷️ [Sectors](../../README.md) › 🏭 [SC05 Manufacturing](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-SC05-19 Remnants above the minimum size go back to stock

# 📏 BR-SC05-19 Remnants above the minimum size go back to stock

**Status:** ✅ specified

## Statement

A leftover whose two smaller sides are above the minimum size set for its material goes back to stock as a remnant, with
its dimensions, its lot and its material certificate. A smaller leftover is scrapped and counted as waste. Planned
layouts use remnants before new stock.

## Why

Good material left on the floor or used last is the main hidden cost of cutting trades, and a remnant with no
certificate cannot be sold on to customers who ask for it. The owner asked for cutting optimisation
([D549](../../../06-decisions/sectors/d549-benchmark-gaps-sc05-manufacturing.md)).

## Examples

| Case | Result |
|---|---|
| Leftover 420 x 300 mm, minimum 200 x 200 | a remnant in stock |
| Leftover 150 x 90 mm | scrapped as waste |
| A remnant and new stock both fit | the remnant is used first |
| Remnant with no certificate | blocked for customers that require one |
| Remnant unused for a year | proposed for scrap |

## Applies to

- [UC-SC05-19](../use-cases/06-excise-refurbishment-and-cutting/uc-sc05-19-optimise-cutting-and-keep-remnants.md)
- [E-SC05-18 Remnant](../data/e-sc05-18-remnant.md)
- [E-F7-10](../../../02-functional/f07-purchasing-and-stock/data/e-f07-10-lot-or-serial.md)

## Exceptions

None.

## Configurable

The minimum remnant size per material and the age after which a remnant is proposed for scrap, by the production
planner.

## Open questions

None.

---

⬅️ [BR-SC05-18](br-sc05-18-production-starts-only-after-the-proof-is-approved.md) · ⬆️ [Up](README.md)
