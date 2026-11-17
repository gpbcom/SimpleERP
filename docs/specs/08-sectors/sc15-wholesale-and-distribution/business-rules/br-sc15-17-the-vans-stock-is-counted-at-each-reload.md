🏠 [Specs](../../../README.md) › 🏷️ [Sectors](../../README.md) › 📦 [SC15 Wholesale and distribution](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-SC15-17 The van's stock is counted at each reload

# 📏 BR-SC15-17 The van's stock is counted at each reload

**Status:** ✅ specified

## Statement

A van's stock is counted at each reload, and the count is compared with the expected stock, which is what was loaded
minus what was sold plus what was returned. A difference is explained or posted as a loss before the van can be loaded
again.

## Why

A van that leaves again with an unexplained difference hides losses, and a stock figure that is not counted drifts. The
owner asked for van sales
([D559](../../../06-decisions/sectors/d559-benchmark-gaps-sc15-wholesale-and-distribution.md)). The
France-pack rule is written later.

## Examples

| Case | Result |
|---|---|
| Loaded 120, sold 18, counted 98 | expected 102, difference 4 |
| Difference posted as a loss | the van can be reloaded |
| No count | no reload |
| Sale above the stock | refused |
| Offline sales | kept and sent later |

## Applies to

- [UC-SC15-22](../use-cases/06-beverages-vans-weights-and-devices/uc-sc15-22-sell-from-the-van.md)
- [E-SC15-16 Van stock](../data/e-sc15-16-van-stock.md)
- [E-F7-11](../../../02-functional/f07-purchasing-and-stock/data/e-f07-11-stock-count.md)

## Exceptions

A difference below the tolerance set by the manager is posted automatically with the count.

## Configurable

The tolerance of the difference and the reload rule, by the manager.

## Open questions

None.

---

⬅️ [BR-SC15-16 Excise and deposits show on each invoice](br-sc15-16-excise-and-deposits-show-on-each-invoice.md) ·
⬆️ [Up](README.md) ·
➡️ [BR-SC15-18 The invoice uses the weighed quantity](br-sc15-18-the-invoice-uses-the-weighed-quantity.md)
