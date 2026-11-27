🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
🔮 [F23 What-if simulation and impact](../README.md) › 📏 [Business rules](README.md) ›
📏 BR-F23-17 Sector drivers from the sector pack

# 📏 BR-F23-17 Sector drivers from the sector pack

**Status:** ✅ specified

## Statement

A sector pack may add drivers the scenarios use (occupancy for hotels and restaurants, utilisation for consulting, fill
rate for training), each with its formula and data source in the company's records.

## Why

Scenarios speak the sector's language (D480).

## Examples

| Case | Result |
|---|---|
| Restaurant: occupancy = covers over seats per service | passes |
| Consulting: utilisation = billable hours over hours worked | passes |
| Training: fill rate = learners over places per session | passes |
| Driver with no data source | passes: entered as an assumption and marked |

## Applies to

- [UC-F23-25 Use sector drivers](../use-cases/07-accuracy-and-drivers/uc-f23-25-use-sector-drivers.md)
- [UC-F23-03 Change one or several elements](../use-cases/01-build-a-scenario/uc-f23-03-change-one-or-several-elements.md)

## Exceptions

None.

## Configurable

The company may adjust a driver's target, not its formula.

## Open questions

None.

---

⬅️ [BR-F23-16 Budgets in F8, scenarios in F23](br-f23-16-budgets-in-f8-scenarios-in-f23.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F23-18 A budget is frozen once approved](br-f23-18-a-budget-is-frozen-once-approved.md)
