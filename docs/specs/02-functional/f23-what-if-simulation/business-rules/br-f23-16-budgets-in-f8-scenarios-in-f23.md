🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
🔮 [F23 What-if simulation and impact](../README.md) › 📏 [Business rules](README.md) ›
📏 BR-F23-16 Budgets in F8, scenarios in F23

# 📏 BR-F23-16 Budgets in F8, scenarios in F23

**Status:** ✅ specified

## Statement

The budget and its comparison with actuals belong to F8 (UC-F8-19 Plan and forecast); every forecast scenario, driver
and simulation belongs to F23, and the F8 budget is one of the inputs of F23's baseline, so that one figure is never
kept in two places.

## Why

The overlap between UC-F8-19 and F23 is resolved this way (D480).

## Examples

| Case | Result |
|---|---|
| Budget 2027 approved in F8 | passes: used by F23's baseline |
| Scenario "supplier +8 %" | passes: lives in F23 only |
| A forecast scenario created in F8 | fails: opened in F23 |

## Applies to

- [UC-F23-24 Measure forecast accuracy and recalibrate](../use-cases/07-accuracy-and-drivers/uc-f23-24-measure-forecast-accuracy-and-recalibrate.md)
- [UC-F23-01 See the baseline forecast](../use-cases/01-build-a-scenario/uc-f23-01-see-the-baseline-forecast.md)

## Exceptions

None.

## Configurable

No.

## Open questions

None.

---

⬅️ [BR-F23-15 Accuracy measured, recalibration decided](br-f23-15-accuracy-measured-recalibration-decided.md) ·
⬆️ [Up](README.md) ·
➡️ [BR-F23-17 Sector drivers from the sector pack](br-f23-17-sector-drivers-from-the-sector-pack.md)
