🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
🔮 [F23 What-if simulation and impact](../README.md) › 📏 [Business rules](README.md) ›
📏 BR-F23-18 A budget is frozen once approved

# 📏 BR-F23-18 A budget is frozen once approved

**Status:** ✅ specified

## Statement

Once the owner approves the budget, every contribution of the round is frozen: no line, amount or assumption changes,
and a revision is made as a new version of the budget plan in the accounting or as a scenario, never by editing a
contribution.

## Why

A budget that can be edited afterwards cannot be compared with actuals fairly. The owner asked for a collaborative
budget ([D542](../../../06-decisions/f23-what-if-simulation/d542-benchmark-gaps-f23-what-if-simulation.md)); the budget
lives in the accounting and scenarios in what-if
([BR-F23-16 Budgets in F8, scenarios in F23](br-f23-16-budgets-in-f8-scenarios-in-f23.md)).

## Examples

| Case | Result |
|---|---|
| Round approved on 2026-12-12 | all contributions frozen |
| A manager edits a line the day after | refused, Frozen |
| A revision needed in June | a new version of the budget plan, the contributions stay as they were |
| A manager who wants to test a different spend | a scenario in what-if, not an edit |
| A contribution still returned when the owner approves | approval is refused: every contribution must be accepted |

## Applies to

- [UC-F23-31](../use-cases/08-budgets-rolling-group-and-valuation/uc-f23-31-build-the-budget-with-department-owners.md)
- [E-F23-15 Budget contribution](../data/e-f23-15-budget-contribution.md)
- [BR-F23-16 Budgets in F8, scenarios in F23](br-f23-16-budgets-in-f8-scenarios-in-f23.md)
- [E-F8-16 Budget plan](../../f08-accounting/data/e-f08-16-budget-plan.md)

## Exceptions

None.

## Configurable

No.

## Open questions

None.

---

⬅️ [BR-F23-17 Sector drivers from the sector pack](br-f23-17-sector-drivers-from-the-sector-pack.md) ·
⬆️ [Up](README.md) ·
➡️ [BR-F23-19 Each rolling forecast keeps its version](br-f23-19-each-rolling-forecast-keeps-its-version.md)
