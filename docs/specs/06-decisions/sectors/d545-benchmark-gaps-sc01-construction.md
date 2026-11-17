🏠 [Specs](../../README.md) › 📜 [Decisions](../README.md) › 🏭 [Decisions: Sectors](README.md) ›
📜 D545 Benchmark gaps of SC01 Construction

# 📜 D545 Benchmark gaps of SC01 Construction

**Status:** ✅ decided

## Context

The owner asked on 2026-11-14 for a benchmark of the specifications against the other ERPs and the AI-native contenders,
and was asked one question per block
([interview record](../../../tickets/GH-2/interviews/2026-11-14-benchmark-gaps.md)). The benchmark found four situations
that construction and property suites handle and SC01 did not: price revision with the BT and TP indices, the property
developer's off-plan sales, quantities taken from a building model and renovation grant files. Three carry a legal limit
(the index of the contract's month, the caps on calls for funds, the label required for a grant).

## Options

- G127 Price revision indices: a revision formula with the index of the contract's month, or a manual percentage on each
  bill.
- G128 Property developer: off-plan lots with calls for funds capped by stage, or ordinary progress invoices.
- G129 BIM quantities: quantities linked to the model version, or quantities retyped from drawings.
- G130 Energy-renovation grants: a grant file with a label check at signature, or a document folder with no check.
- Every answer was a choice among adding the gap with full depth now, later or never; the interview record keeps the
  owner's answers, not every option.

## Choice

SC01 gets four use cases in one new flow, FL-SC01-06, each with its screen, its rule, its entity and its list. All at
full depth now. Each legal duty is written in plain words and marked (Proposed) until the France-pack rule is written.

| Gap | Point | Decision | The owner's answer |
|---|---|---|---|
| G127 | Price revision indices | UC-SC01-16: revisions that use the index of the contract's month | "Price revision indices" |
| G128 | Property developer | UC-SC01-17: calls for funds that follow the legal stage caps | "Property developer" |
| G129 | BIM quantities | UC-SC01-18: quantities that keep a link to the model version | "BIM quantities" |
| G130 | Energy-renovation grants | UC-SC01-19: grant files that check the RGE label at signature | "Energy-renovation grants" |

## Decided by

The owner, on 2026-11-14, in the GH-2 benchmark-gaps interview
([interview record](../../../tickets/GH-2/interviews/2026-11-14-benchmark-gaps.md), section "SC01 Construction").

## Consequences

- G127 Price revision indices:
  [UC-SC01-16](../../08-sectors/sc01-construction/use-cases/06-revision-developers-bim-and-grants/uc-sc01-16-revise-prices-with-the-bt-and-tp-indices.md),
  [S-SC01-16](../../08-sectors/sc01-construction/screens/06-revision-developers-bim-and-grants/s-sc01-16-price-revision.md)
  and
  [BR-SC01-16](../../08-sectors/sc01-construction/business-rules/br-sc01-16-revisions-use-the-index-of-the-contracts-month.md),
  with [E-SC01-15](../../08-sectors/sc01-construction/data/e-sc01-15-revision-formula.md) Revision formula and its list
  [S-SC01-L15](../../08-sectors/sc01-construction/screens/00-lists/s-sc01-l15-revision-formulas.md).
- G128 Property developer:
  [UC-SC01-17](../../08-sectors/sc01-construction/use-cases/06-revision-developers-bim-and-grants/uc-sc01-17-sell-off-plan-homes.md),
  [S-SC01-17](../../08-sectors/sc01-construction/screens/06-revision-developers-bim-and-grants/s-sc01-17-off-plan-sales.md)
  and
  [BR-SC01-17](../../08-sectors/sc01-construction/business-rules/br-sc01-17-calls-for-funds-follow-the-legal-stage-caps.md),
  with [E-SC01-16](../../08-sectors/sc01-construction/data/e-sc01-16-off-plan-lot.md) Off-plan lot and its list
  [S-SC01-L16](../../08-sectors/sc01-construction/screens/00-lists/s-sc01-l16-off-plan-lots.md).
- G129 BIM quantities:
  [UC-SC01-18](../../08-sectors/sc01-construction/use-cases/06-revision-developers-bim-and-grants/uc-sc01-18-take-quantities-from-a-bim-model.md),
  [S-SC01-18](../../08-sectors/sc01-construction/screens/06-revision-developers-bim-and-grants/s-sc01-18-bim-quantities.md)
  and
  [BR-SC01-18](../../08-sectors/sc01-construction/business-rules/br-sc01-18-quantities-keep-a-link-to-the-model-version.md),
  with [E-SC01-17](../../08-sectors/sc01-construction/data/e-sc01-17-bim-import.md) BIM import and its list
  [S-SC01-L17](../../08-sectors/sc01-construction/screens/00-lists/s-sc01-l17-bim-imports.md).
- G130 Energy-renovation grants:
  [UC-SC01-19](../../08-sectors/sc01-construction/use-cases/06-revision-developers-bim-and-grants/uc-sc01-19-prepare-renovation-grant-files.md),
  [S-SC01-19](../../08-sectors/sc01-construction/screens/06-revision-developers-bim-and-grants/s-sc01-19-renovation-grants.md)
  and
  [BR-SC01-19](../../08-sectors/sc01-construction/business-rules/br-sc01-19-grants-need-the-rge-label-at-signature.md),
  with [E-SC01-18](../../08-sectors/sc01-construction/data/e-sc01-18-grant-file.md) Grant file and its list
  [S-SC01-L18](../../08-sectors/sc01-construction/screens/00-lists/s-sc01-l18-grant-files.md).
- Drawn in [FL-SC01-06](../../08-sectors/sc01-construction/flows/fl-sc01-06-revision-developers-bim-and-grants.md) Price
  revision, off-plan sales, BIM and grants.

## Related

- [FL-SC01-06](../../08-sectors/sc01-construction/flows/fl-sc01-06-revision-developers-bim-and-grants.md)
- [D316 Construction sector coverage](d316-construction-sector-coverage.md)
- [D319 SC01 use cases](d319-sc01-use-cases.md)
- [U22 Site manager](../../01-users/personas/u22-site-manager.md)

---

⬅️ [D544 Benchmark gaps of F25 DevOps agents](../f25-devops-agents/d544-benchmark-gaps-f25-devops-agents.md) ·
⬆️ [Up](README.md) · ➡️ [D546 Benchmark gaps of SC02 Retail](d546-benchmark-gaps-sc02-retail.md)
