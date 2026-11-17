🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
🔮 [F23 What-if simulation and impact](../README.md) › 📏 [Business rules](README.md) ›
📏 BR-F23-19 Each rolling forecast keeps its version

# 📏 BR-F23-19 Each rolling forecast keeps its version

**Status:** 🔄 waiting for the owner

## Statement

Every rolled forecast is saved as its own numbered version with its horizon, its assumptions and its author; a published
version is never overwritten or edited, and an older version stays readable and comparable.

## Why

The value of a rolling forecast is to see how expectations moved and whether they were right
([UC-F23-24](../use-cases/07-accuracy-and-drivers/uc-f23-24-measure-forecast-accuracy-and-recalibrate.md)); overwriting
would erase that. The owner asked for a rolling forecast
([D542](../../../06-decisions/f23-what-if-simulation/d542-benchmark-gaps-f23-what-if-simulation.md)).

## Examples

| Case | Result |
|---|---|
| Version 11 published | version 10 is Superseded and still readable |
| A correction found in version 11 | version 12 is made, version 11 stays |
| Two versions compared | the move per line and per assumption is shown |
| A draft discarded | no version number is used |
| Accuracy measured a year later | the versions of that year are compared with the actuals |

## Applies to

- [UC-F23-32](../use-cases/08-budgets-rolling-group-and-valuation/uc-f23-32-roll-the-forecast-forward.md)
- [E-F23-16 Forecast version](../data/e-f23-16-forecast-version.md)
- [UC-F23-24](../use-cases/07-accuracy-and-drivers/uc-f23-24-measure-forecast-accuracy-and-recalibrate.md)

## Exceptions

None.

## Configurable

The horizon length, by accounting.

## Open questions

None.

---

⬅️ [BR-F23-18 A budget is frozen once approved](br-f23-18-a-budget-is-frozen-once-approved.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F23-20 Group scenarios eliminate intercompany flows](br-f23-20-group-scenarios-eliminate-intercompany-flows.md)
