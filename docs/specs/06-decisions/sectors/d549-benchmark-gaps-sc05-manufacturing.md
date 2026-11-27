🏠 [Specs](../../README.md) › 📜 [Decisions](../README.md) › 🏭 [Decisions: Sectors](README.md) ›
📜 D549 Benchmark gaps of SC05 Manufacturing

# 📜 D549 Benchmark gaps of SC05 Manufacturing

**Status:** ✅ decided

## Context

The owner asked on 2026-11-14 for a benchmark of the specifications against the other ERPs and the AI-native contenders,
and was asked one question per block
(interview record (the owner's interview of 2026-11-14 on the benchmark gaps, not kept in the repository)). The benchmark found four situations
that manufacturers handle and SC05 did not: alcohol excise for breweries and distilleries, refurbishment of electronics,
personalised products and the cutting of sheets and bars. Two carry a legal or contractual limit (the duty due only on
release from the bonded warehouse, the customer's approved proof).

## Options

- G143 Alcohol excise: bonded stock with the duty computed at release, or an excise return typed by hand each month.
- G144 Refurbishment: units tested and graded on a tablet with a confirmed grade, or free notes on the stock item.
- G145 Personalisation: a versioned proof approved by the customer before production, or an approval by email outside
  the order.
- G146 Cutting optimisation: layouts on remnants first with leftovers back in stock, or cuts planned on paper.
- Every answer was a choice among adding the gap with full depth now, later or never; the interview record keeps the
  owner's answers, not every option.

## Choice

SC05 gets four use cases in one new flow, FL-SC05-06, each with its screen, its rule, its entity and its list. All at
full depth now. Each legal duty is written in plain words and marked as proposed until its France-pack rule was
written (the rules now exist).

| Gap | Point | Decision | The owner's answer |
|---|---|---|---|
| G143 | Alcohol excise | UC-SC05-16: excise computed when goods leave the bonded warehouse | "Alcohol excise" |
| G144 | Refurbishment | UC-SC05-17: every refurbished unit graded after its tests | "Refurbishment" |
| G145 | Personalisation | UC-SC05-18: production only after the customer's approved proof | "Personalisation" |
| G146 | Cutting optimisation | UC-SC05-19: remnants above the minimum size kept in stock | "Cutting optimisation" |

## Decided by

The owner, on 2026-11-14, in the GH-2 benchmark-gaps interview
(interview record (the owner's interview of 2026-11-14 on the benchmark gaps, not kept in the repository), section "SC05 Manufacturing").

## Consequences

- G143 Alcohol excise:
  [UC-SC05-16](../../08-sectors/sc05-manufacturing/use-cases/06-excise-refurbishment-and-cutting/uc-sc05-16-declare-alcohol-excise.md),
  [S-SC05-16](../../08-sectors/sc05-manufacturing/screens/06-excise-refurbishment-and-cutting/s-sc05-16-alcohol-excise.md)
  and
  [BR-SC05-16](../../08-sectors/sc05-manufacturing/business-rules/br-sc05-16-excise-is-due-when-goods-leave-the-bonded-warehouse.md),
  with [E-SC05-15](../../08-sectors/sc05-manufacturing/data/e-sc05-15-bonded-stock.md) Bonded stock and its list
  [S-SC05-L15](../../08-sectors/sc05-manufacturing/screens/00-lists/s-sc05-l15-bonded-stocks.md).
- G144 Refurbishment:
  [UC-SC05-17](../../08-sectors/sc05-manufacturing/use-cases/06-excise-refurbishment-and-cutting/uc-sc05-17-refurbish-electronics.md),
  [S-SC05-17](../../08-sectors/sc05-manufacturing/screens/06-excise-refurbishment-and-cutting/s-sc05-17-refurbishment.md)
  and
  [BR-SC05-17](../../08-sectors/sc05-manufacturing/business-rules/br-sc05-17-every-refurbished-unit-is-graded-and-tested.md),
  with [E-SC05-16](../../08-sectors/sc05-manufacturing/data/e-sc05-16-graded-unit.md) Graded unit and its list
  [S-SC05-L16](../../08-sectors/sc05-manufacturing/screens/00-lists/s-sc05-l16-graded-units.md).
- G145 Personalisation:
  [UC-SC05-18](../../08-sectors/sc05-manufacturing/use-cases/06-excise-refurbishment-and-cutting/uc-sc05-18-personalise-products-for-customers.md),
  [S-SC05-18](../../08-sectors/sc05-manufacturing/screens/06-excise-refurbishment-and-cutting/s-sc05-18-personalisation.md)
  and
  [BR-SC05-18](../../08-sectors/sc05-manufacturing/business-rules/br-sc05-18-production-starts-only-after-the-proof-is-approved.md),
  with [E-SC05-17](../../08-sectors/sc05-manufacturing/data/e-sc05-17-proof.md) Proof and its list
  [S-SC05-L17](../../08-sectors/sc05-manufacturing/screens/00-lists/s-sc05-l17-proofs.md).
- G146 Cutting optimisation:
  [UC-SC05-19](../../08-sectors/sc05-manufacturing/use-cases/06-excise-refurbishment-and-cutting/uc-sc05-19-optimise-cutting-and-keep-remnants.md),
  [S-SC05-19](../../08-sectors/sc05-manufacturing/screens/06-excise-refurbishment-and-cutting/s-sc05-19-cutting.md) and
  [BR-SC05-19](../../08-sectors/sc05-manufacturing/business-rules/br-sc05-19-remnants-above-the-minimum-size-go-back-to-stock.md),
  with [E-SC05-18](../../08-sectors/sc05-manufacturing/data/e-sc05-18-remnant.md) Remnant and its list
  [S-SC05-L18](../../08-sectors/sc05-manufacturing/screens/00-lists/s-sc05-l18-remnants.md).
- Drawn in [FL-SC05-06](../../08-sectors/sc05-manufacturing/flows/fl-sc05-06-excise-refurbishment-and-cutting.md)
  Excise, refurbishment, personalisation and cutting.

## Related

- [FL-SC05-06](../../08-sectors/sc05-manufacturing/flows/fl-sc05-06-excise-refurbishment-and-cutting.md)
- [D329 Manufacturing sector coverage](d329-manufacturing-sector-coverage.md)
- [D331 SC05 use cases](d331-sc05-use-cases.md)
- [U21 Production planner](../../01-users/personas/u21-production-planner.md)

---

⬅️ [D548 Benchmark gaps of SC04 Home care](d548-benchmark-gaps-sc04-home-care.md) · ⬆️ [Up](README.md) ·
➡️ [D550 Benchmark gaps of SC06 Hospitality](d550-benchmark-gaps-sc06-hospitality.md)
