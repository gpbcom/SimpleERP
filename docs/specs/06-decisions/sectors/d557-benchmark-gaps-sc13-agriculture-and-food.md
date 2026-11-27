🏠 [Specs](../../README.md) › 📜 [Decisions](../README.md) › 🏭 [Decisions: Sectors](README.md) ›
📜 D557 Benchmark gaps of SC13 Agriculture and food

# 📜 D557 Benchmark gaps of SC13 Agriculture and food

**Status:** ✅ decided

## Context

The owner asked on 2026-11-14 for a benchmark of the specifications against the other ERPs and the AI-native contenders,
and was asked one question per block
(interview record (the owner's interview of 2026-11-14 on the benchmark gaps, not kept in the repository)). The benchmark found five situations
that agricultural suites handle and SC13 did not: vineyards, agricultural contractors, cooperatives, basket
subscriptions and forestry. Each carries a duty or an agreement (declarations on a date, billing on the agreed basis,
rebates from deliveries, baskets from the season contract, fellings within the plan).

## Options

- G20 Vineyards: plots with yield checks and declarations drawn from the records, or the declarations typed from a
  spreadsheet each year.
- G175 Farm contractors: jobs billed on the agreed basis from the driver's record, or an invoice typed at month end.
- G176 Cooperatives: deliveries settled by grade with a rebate from the deliveries, or a statement prepared outside the
  system.
- G177 Basket subscriptions: season contracts with absences and a weekly plan, or a list of members kept in a
  spreadsheet.
- G178 Forestry: lots checked against the management plan and traced to the parcel, or sales recorded as plain invoices.
- Every answer was a choice among adding the gap with full depth now, later or never; the interview record keeps the
  owner's answers, not every option.

## Choice

SC13 gets five use cases in one new flow, FL-SC13-06, each with its screen, its rule, its entity and its list. All at
full depth now. Each legal duty is written in plain words and marked as proposed until its France-pack rule was
written (the rules now exist).

| Gap | Point | Decision | The owner's answer |
|---|---|---|---|
| G20 | Vineyards | UC-SC13-21: harvest and stock declarations drawn from the plots and the cellar | "Vineyards" |
| G175 | Farm contractors | UC-SC13-22: jobs billed by hectare or hour as agreed | "Farm contractors" |
| G176 | Cooperatives | UC-SC13-23: rebates that follow each member's deliveries | "Cooperatives" |
| G177 | Basket subscriptions | UC-SC13-24: baskets that follow the season's contract | "Basket subscriptions" |
| G178 | Forestry | UC-SC13-25: fellings that follow the management plan | "Forestry" |

## Decided by

The owner, on 2026-11-14, in the GH-2 benchmark-gaps interview
(interview record (the owner's interview of 2026-11-14 on the benchmark gaps, not kept in the repository), section "SC13 Agriculture and
food").

## Consequences

- G20 Vineyards:
  [UC-SC13-21](../../08-sectors/sc13-agriculture-and-food/use-cases/06-vineyards-contractors-and-cooperatives/uc-sc13-21-run-the-vineyard-and-the-cellar.md),
  [S-SC13-21](../../08-sectors/sc13-agriculture-and-food/screens/06-vineyards-contractors-and-cooperatives/s-sc13-21-vineyard.md)
  and
  [BR-SC13-16](../../08-sectors/sc13-agriculture-and-food/business-rules/br-sc13-16-harvest-and-stock-declarations-are-filed-on-time.md),
  with [E-SC13-17](../../08-sectors/sc13-agriculture-and-food/data/e-sc13-17-vine-plot.md) Vine plot and its list
  [S-SC13-L17](../../08-sectors/sc13-agriculture-and-food/screens/00-lists/s-sc13-l17-vine-plots.md).
- G175 Farm contractors:
  [UC-SC13-22](../../08-sectors/sc13-agriculture-and-food/use-cases/06-vineyards-contractors-and-cooperatives/uc-sc13-22-work-as-an-agricultural-contractor.md),
  [S-SC13-22](../../08-sectors/sc13-agriculture-and-food/screens/06-vineyards-contractors-and-cooperatives/s-sc13-22-farm-contractor.md)
  and
  [BR-SC13-17](../../08-sectors/sc13-agriculture-and-food/business-rules/br-sc13-17-jobs-are-billed-by-hectare-or-hour-as-agreed.md),
  with [E-SC13-18](../../08-sectors/sc13-agriculture-and-food/data/e-sc13-18-field-job.md) Field job and its list
  [S-SC13-L18](../../08-sectors/sc13-agriculture-and-food/screens/00-lists/s-sc13-l18-field-jobs.md).
- G176 Cooperatives:
  [UC-SC13-23](../../08-sectors/sc13-agriculture-and-food/use-cases/06-vineyards-contractors-and-cooperatives/uc-sc13-23-run-a-cooperative.md),
  [S-SC13-23](../../08-sectors/sc13-agriculture-and-food/screens/06-vineyards-contractors-and-cooperatives/s-sc13-23-cooperative.md)
  and
  [BR-SC13-18](../../08-sectors/sc13-agriculture-and-food/business-rules/br-sc13-18-rebates-follow-the-members-deliveries.md),
  with [E-SC13-19](../../08-sectors/sc13-agriculture-and-food/data/e-sc13-19-member-delivery.md) Member delivery and its
  list [S-SC13-L19](../../08-sectors/sc13-agriculture-and-food/screens/00-lists/s-sc13-l19-member-deliveries.md).
- G177 Basket subscriptions:
  [UC-SC13-24](../../08-sectors/sc13-agriculture-and-food/use-cases/06-vineyards-contractors-and-cooperatives/uc-sc13-24-sell-basket-subscriptions.md),
  [S-SC13-24](../../08-sectors/sc13-agriculture-and-food/screens/06-vineyards-contractors-and-cooperatives/s-sc13-24-baskets.md)
  and
  [BR-SC13-19](../../08-sectors/sc13-agriculture-and-food/business-rules/br-sc13-19-baskets-follow-the-seasons-contract.md),
  with [E-SC13-20](../../08-sectors/sc13-agriculture-and-food/data/e-sc13-20-basket-subscription.md) Basket subscription
  and its list
  [S-SC13-L20](../../08-sectors/sc13-agriculture-and-food/screens/00-lists/s-sc13-l20-basket-subscriptions.md).
- G178 Forestry:
  [UC-SC13-25](../../08-sectors/sc13-agriculture-and-food/use-cases/06-vineyards-contractors-and-cooperatives/uc-sc13-25-manage-forests-and-timber-sales.md),
  [S-SC13-25](../../08-sectors/sc13-agriculture-and-food/screens/06-vineyards-contractors-and-cooperatives/s-sc13-25-forestry.md)
  and
  [BR-SC13-20](../../08-sectors/sc13-agriculture-and-food/business-rules/br-sc13-20-fellings-follow-the-management-plan.md),
  with [E-SC13-21](../../08-sectors/sc13-agriculture-and-food/data/e-sc13-21-timber-lot.md) Timber lot and its list
  [S-SC13-L21](../../08-sectors/sc13-agriculture-and-food/screens/00-lists/s-sc13-l21-timber-lots.md).
- Drawn in
  [FL-SC13-06](../../08-sectors/sc13-agriculture-and-food/flows/fl-sc13-06-vineyards-contractors-and-cooperatives.md)
  Vineyards, contractors, cooperatives, baskets, forests.

## Related

- [FL-SC13-06](../../08-sectors/sc13-agriculture-and-food/flows/fl-sc13-06-vineyards-contractors-and-cooperatives.md)
- [D293](../country-packs/d293-capabilities-take-legal-rules-from-the-pack.md)
- [U40 Farmer](../../01-users/personas/u40-farmer.md)

---

⬅️ [D556 Benchmark gaps of SC12 Education and training](d556-benchmark-gaps-sc12-education-and-training.md) ·
⬆️ [Up](README.md) · ➡️ [D558 Benchmark gaps of SC14 IT and software](d558-benchmark-gaps-sc14-it-and-software.md)
