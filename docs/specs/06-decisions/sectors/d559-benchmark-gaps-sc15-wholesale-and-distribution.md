🏠 [Specs](../../README.md) › 📜 [Decisions](../README.md) › 🏭 [Decisions: Sectors](README.md) ›
📜 D559 Benchmark gaps of SC15 Wholesale and distribution

# 📜 D559 Benchmark gaps of SC15 Wholesale and distribution

**Status:** ✅ decided

## Context

The owner asked on 2026-11-14 for a benchmark of the specifications against the other ERPs and the AI-native contenders,
and was asked one question per block
([interview record](../../../tickets/GH-2/interviews/2026-11-14-benchmark-gaps.md)). The benchmark found four situations
that distribution suites handle and SC15 did not: beverage distribution, van sales, catch weight and medical devices.
Each carries a duty (duty and deposits shown on the invoice, a count at each reload, the weighed quantity invoiced, a
traceable lot).

## Options

- G183 Beverage distribution: duty, deposits and loans as lines of their own, or one price per item with the duty
  inside.
- G184 Van sales: a count at each reload before the next load, or a stock adjusted at month end.
- G185 Catch weight: invoicing on the weighed quantity, or on the nominal weight with credit notes afterwards.
- G186 Medical devices: lots linked to customers by UDI, or lots tracked as plain stock.
- Every answer was a choice among adding the gap with full depth now, later or never; the interview record keeps the
  owner's answers, not every option.

## Choice

SC15 gets four use cases in one new flow, FL-SC15-06, each with its screen and its rule, and an entity and a list for
three of them: catch weight needs no entity of its own, because the weights live on the order line. All at full depth
now. Each legal duty is written in plain words and marked (Proposed) until the France-pack rule is written.

| Gap | Point | Decision | The owner's answer |
|---|---|---|---|
| G183 | Beverage distribution | UC-SC15-21: excise and deposits shown on each invoice | "Beverage distribution" |
| G184 | Van sales | UC-SC15-22: the van's stock counted at each reload | "Van sales" |
| G185 | Catch weight | UC-SC15-23: invoices that use the weighed quantity | "Catch weight" |
| G186 | Medical devices | UC-SC15-24: every lot traceable by its UDI | "Medical devices" |

## Decided by

The owner, on 2026-11-14, in the GH-2 benchmark-gaps interview
([interview record](../../../tickets/GH-2/interviews/2026-11-14-benchmark-gaps.md), section "SC15 Wholesale and
distribution").

## Consequences

- G183 Beverage distribution:
  [UC-SC15-21](../../08-sectors/sc15-wholesale-and-distribution/use-cases/06-beverages-vans-weights-and-devices/uc-sc15-21-distribute-beverages.md),
  [S-SC15-21](../../08-sectors/sc15-wholesale-and-distribution/screens/06-beverages-vans-weights-and-devices/s-sc15-21-beverage-distribution.md)
  and
  [BR-SC15-16](../../08-sectors/sc15-wholesale-and-distribution/business-rules/br-sc15-16-excise-and-deposits-show-on-each-invoice.md),
  with [E-SC15-15](../../08-sectors/sc15-wholesale-and-distribution/data/e-sc15-15-bar-loan.md) Bar loan and its list
  [S-SC15-L15](../../08-sectors/sc15-wholesale-and-distribution/screens/00-lists/s-sc15-l15-bar-loans.md).
- G184 Van sales:
  [UC-SC15-22](../../08-sectors/sc15-wholesale-and-distribution/use-cases/06-beverages-vans-weights-and-devices/uc-sc15-22-sell-from-the-van.md),
  [S-SC15-22](../../08-sectors/sc15-wholesale-and-distribution/screens/06-beverages-vans-weights-and-devices/s-sc15-22-van-sales.md)
  and
  [BR-SC15-17](../../08-sectors/sc15-wholesale-and-distribution/business-rules/br-sc15-17-the-vans-stock-is-counted-at-each-reload.md),
  with [E-SC15-16](../../08-sectors/sc15-wholesale-and-distribution/data/e-sc15-16-van-stock.md) Van stock and its list
  [S-SC15-L16](../../08-sectors/sc15-wholesale-and-distribution/screens/00-lists/s-sc15-l16-van-stocks.md).
- G185 Catch weight:
  [UC-SC15-23](../../08-sectors/sc15-wholesale-and-distribution/use-cases/06-beverages-vans-weights-and-devices/uc-sc15-23-sell-by-catch-weight.md),
  [S-SC15-23](../../08-sectors/sc15-wholesale-and-distribution/screens/06-beverages-vans-weights-and-devices/s-sc15-23-catch-weight.md)
  and
  [BR-SC15-18](../../08-sectors/sc15-wholesale-and-distribution/business-rules/br-sc15-18-the-invoice-uses-the-weighed-quantity.md).
- G186 Medical devices:
  [UC-SC15-24](../../08-sectors/sc15-wholesale-and-distribution/use-cases/06-beverages-vans-weights-and-devices/uc-sc15-24-distribute-medical-devices.md),
  [S-SC15-24](../../08-sectors/sc15-wholesale-and-distribution/screens/06-beverages-vans-weights-and-devices/s-sc15-24-medical-devices.md)
  and
  [BR-SC15-19](../../08-sectors/sc15-wholesale-and-distribution/business-rules/br-sc15-19-every-lot-is-traceable-by-its-udi.md),
  with [E-SC15-17](../../08-sectors/sc15-wholesale-and-distribution/data/e-sc15-17-device-lot.md) Device lot and its
  list [S-SC15-L17](../../08-sectors/sc15-wholesale-and-distribution/screens/00-lists/s-sc15-l17-device-lots.md).
- Drawn in
  [FL-SC15-06](../../08-sectors/sc15-wholesale-and-distribution/flows/fl-sc15-06-beverages-vans-weights-and-devices.md)
  Beverages, van sales, catch weight and medical devices.

## Related

- [FL-SC15-06](../../08-sectors/sc15-wholesale-and-distribution/flows/fl-sc15-06-beverages-vans-weights-and-devices.md)
- [D293](../country-packs/d293-capabilities-take-legal-rules-from-the-pack.md)
- [U42 Sales representative](../../01-users/personas/u42-sales-representative.md)

---

⬅️ [D558 Benchmark gaps of SC14 IT and software](d558-benchmark-gaps-sc14-it-and-software.md) · ⬆️ [Up](README.md) ·
➡️ [D560 Benchmark gaps of SC16 Events and culture](d560-benchmark-gaps-sc16-events-and-culture.md)
