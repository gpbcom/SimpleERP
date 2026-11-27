🏠 [Specs](../../README.md) › 📜 [Decisions](../README.md) › 🔮 [Decisions: F23 What-if simulation and impact](README.md) ›
📜 D542 Benchmark gaps of F23 What-if simulation

# 📜 D542 Benchmark gaps of F23 What-if simulation

**Status:** ✅ decided

## Context

The owner asked on 2026-11-14 for a benchmark of the specifications against the other ERPs and the AI-native contenders,
and was asked one question per block
(interview record (the owner's interview of 2026-11-14 on the benchmark gaps, not kept in the repository)). The benchmark found four planning
features that F23 did not cover: a budget built with the department owners, a rolling forecast with its versions,
scenarios across a group and valuation scenarios. F23 already has the baseline, scenarios, runs on a copy and the impact
views; the budget stays in the accounting
[BR-F23-16](../../02-functional/f23-what-if-simulation/business-rules/br-f23-16-budgets-in-f8-scenarios-in-f23.md), so
the contributions of the managers feed it and are frozen once it is approved.

## Options

- G115 Collaborative budget: contributions from the department owners with a frozen approved budget, or a budget typed
  by accounting alone.
- G116 Rolling forecast: a rolling forecast whose versions are kept, or one forecast that is overwritten.
- G117 Group scenarios: group scenarios with the intercompany flows eliminated, or one scenario per company.
- G118 Valuation scenarios: valuations that show their method and assumptions, or none.
- Every answer was a choice among adding the gap with full depth now, later or never; the interview record keeps the
  owner's answers, not every option.

## Choice

F23 gets four use cases in one new flow, FL-F23-08, each with its screen and its rule, and three entities with their
lists; the group scenario has no entity of its own, since its result is kept with the simulation runs. All at full depth
now.

| Gap | Point | Decision | The owner's answer |
|---|---|---|---|
| G115 | Collaborative budget | UC-F23-31: a collaborative budget whose approved contributions are frozen | "Collaborative budget" |
| G116 | Rolling forecast | UC-F23-32: a rolling forecast that keeps each version | "Rolling forecast" |
| G117 | Group scenarios | UC-F23-33: group scenarios that eliminate intercompany flows | "Group scenarios" |
| G118 | Valuation scenarios | UC-F23-34: valuations with their method and assumptions | "Valuation scenarios" |

## Decided by

The owner, on 2026-11-14, in the GH-2 benchmark-gaps interview
(interview record (the owner's interview of 2026-11-14 on the benchmark gaps, not kept in the repository), section "F23 What-if simulation").

## Consequences

- G115 Collaborative budget:
  [UC-F23-31](../../02-functional/f23-what-if-simulation/use-cases/08-budgets-rolling-group-and-valuation/uc-f23-31-build-the-budget-with-department-owners.md),
  [S-F23-25](../../02-functional/f23-what-if-simulation/screens/08-budgets-rolling-group-and-valuation/s-f23-25-collaborative-budget.md)
  and
  [BR-F23-18](../../02-functional/f23-what-if-simulation/business-rules/br-f23-18-a-budget-is-frozen-once-approved.md),
  with [E-F23-15](../../02-functional/f23-what-if-simulation/data/e-f23-15-budget-contribution.md) Budget contribution
  and its list
  [S-F23-L15](../../02-functional/f23-what-if-simulation/screens/00-lists/s-f23-l15-budget-contributions.md).
- G116 Rolling forecast:
  [UC-F23-32](../../02-functional/f23-what-if-simulation/use-cases/08-budgets-rolling-group-and-valuation/uc-f23-32-roll-the-forecast-forward.md),
  [S-F23-26](../../02-functional/f23-what-if-simulation/screens/08-budgets-rolling-group-and-valuation/s-f23-26-rolling-forecast.md)
  and
  [BR-F23-19](../../02-functional/f23-what-if-simulation/business-rules/br-f23-19-each-rolling-forecast-keeps-its-version.md),
  with [E-F23-16](../../02-functional/f23-what-if-simulation/data/e-f23-16-forecast-version.md) Forecast version and its
  list [S-F23-L16](../../02-functional/f23-what-if-simulation/screens/00-lists/s-f23-l16-forecast-versions.md).
- G117 Group scenarios:
  [UC-F23-33](../../02-functional/f23-what-if-simulation/use-cases/08-budgets-rolling-group-and-valuation/uc-f23-33-run-a-group-scenario.md),
  [S-F23-27](../../02-functional/f23-what-if-simulation/screens/08-budgets-rolling-group-and-valuation/s-f23-27-group-scenario.md)
  and
  [BR-F23-20](../../02-functional/f23-what-if-simulation/business-rules/br-f23-20-group-scenarios-eliminate-intercompany-flows.md).
- G118 Valuation scenarios:
  [UC-F23-34](../../02-functional/f23-what-if-simulation/use-cases/08-budgets-rolling-group-and-valuation/uc-f23-34-value-the-company.md),
  [S-F23-28](../../02-functional/f23-what-if-simulation/screens/08-budgets-rolling-group-and-valuation/s-f23-28-valuation.md)
  and
  [BR-F23-21](../../02-functional/f23-what-if-simulation/business-rules/br-f23-21-valuations-show-their-method-and-assumptions.md),
  with [E-F23-17](../../02-functional/f23-what-if-simulation/data/e-f23-17-valuation.md) Valuation and its list
  [S-F23-L17](../../02-functional/f23-what-if-simulation/screens/00-lists/s-f23-l17-valuations.md).
- Drawn in
  [FL-F23-08](../../02-functional/f23-what-if-simulation/flows/fl-f23-08-budgets-rolling-group-and-valuation.md)
  Budgets, rolling forecasts, group and valuation.

## Related

- [FL-F23-08](../../02-functional/f23-what-if-simulation/flows/fl-f23-08-budgets-rolling-group-and-valuation.md)
- [D401 What-if simulation coverage](d401-what-if-coverage.md)
- [D480](d480-f23-gaps-and-improvements.md)
- [BR-F23-16](../../02-functional/f23-what-if-simulation/business-rules/br-f23-16-budgets-in-f8-scenarios-in-f23.md)

---

⬅️ [D541](../f22-unified-cost-management/d541-benchmark-gaps-f22-unified-cost-management.md) · ⬆️ [Up](README.md) ·
➡️ [D543 Benchmark gaps of F24 Integrations hub](../f24-integrations-hub/d543-benchmark-gaps-f24-integrations-hub.md)
