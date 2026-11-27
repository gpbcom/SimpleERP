🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
🔮 [F23 What-if simulation and impact](../README.md) › 📏 [Business rules](README.md) ›
📏 BR-F23-15 Accuracy measured, recalibration decided

# 📏 BR-F23-15 Accuracy measured, recalibration decided

**Status:** 🔄 waiting for the owner

## Statement

Each month, the forecast of the closed month is compared with the actuals per driver; a driver whose error is above the
tolerance gets a recalibration proposal, applied only when accounting accepts it.

## Why

A forecast is trusted when its accuracy is known (D480).

## Examples

| Case | Result |
|---|---|
| Sales volume forecast 100, actual 109, tolerance (Proposed) 5 % | passes: recalibration proposed |
| Accounting accepts | passes: baseline rebuilt with the new seasonality |
| Recalibration applied by itself | fails: never |

## Applies to

- [UC-F23-24 Measure forecast accuracy and recalibrate](../use-cases/07-accuracy-and-drivers/uc-f23-24-measure-forecast-accuracy-and-recalibrate.md)
- [UC-F23-01 See the baseline forecast](../use-cases/01-build-a-scenario/uc-f23-01-see-the-baseline-forecast.md)

## Exceptions

Months with a known one-off event may be excluded with a reason.

## Configurable

The tolerance per driver.

## Open questions

None.

---

⬅️ [BR-F23-14](br-f23-14-financing-options-with-their-terms-and-covenants.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F23-16 Budgets in F8, scenarios in F23](br-f23-16-budgets-in-f8-scenarios-in-f23.md)
