🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
🏭 [F12 Manufacturing (plugin)](../README.md) › 🔀 [Flows](README.md) › 🔀 FL-F12-02 Plan production

# 🔀 FL-F12-02 Plan production

**Status:** ✅ specified

## Summary

Covers UC-F12-03, UC-F12-15.

## Personas

- [U04 Purchasing](../../../01-users/personas/u04-purchasing.md)
- [U15 Warehouse operator](../../../01-users/personas/u15-warehouse-operator.md)
- [U21 Production planner](../../../01-users/personas/u21-production-planner.md)

## Flowchart

```mermaid
flowchart LR
  A[Forecasts and orders] --> B[Master plan]
  B --> C[Proposals]
  C --> D[Pick and stage]
```

## Sequence diagram

See each use case.

## Steps

| Step | Persona | Screen | Use case | What happens |
|---|---|---|---|---|
| 1 | U21, U04 | [S-F12-03](../screens/02-plan-production/s-f12-03-master-plan.md) | [UC-F12-03](../use-cases/02-plan-production/uc-f12-03-plan-production.md) | Plan production |
| 2 | U15 | [S-F12-15](../screens/02-plan-production/s-f12-15-pick-for-production.md) | [UC-F12-15](../use-cases/02-plan-production/uc-f12-15-pick-and-stage-components.md) | Pick and stage components |

### Entities and screens

| Entity | States in this flow | Shown at step and screen | Aggregated view |
|---|---|---|---|
| [E-F7-21 Demand forecast](../../f07-purchasing-and-stock/data/e-f07-21-demand-forecast.md) | Active | 1 [S-F12-03](../screens/02-plan-production/s-f12-03-master-plan.md) | Demand forecasts |
| [E-F6-04 Order](../../f06-customers-and-sales/data/e-f06-04-order.md) | Open, In progress, Cancelled, Done | Shown elsewhere: [S-F6-05 Order](../../f06-customers-and-sales/screens/02-quote-to-order/s-f06-05-order.md) | Orders |
| [E-F12-12 Master plan line](../data/e-f12-12-master-plan-line.md) | Recorded | 1 [S-F12-03](../screens/02-plan-production/s-f12-03-master-plan.md) | Master plan lines |
| [E-F12-04 Manufacturing order](../data/e-f12-04-manufacturing-order.md) | Draft, Confirmed, Cancelled, In progress, Done | 1 [S-F12-03](../screens/02-plan-production/s-f12-03-master-plan.md) | Manufacturing orders |

## Errors

As each use case.

## Images

Every step and error, for each persona taking part, in light and dark mode (D120). Steps are numbered as in the Steps
table; E rows are the error cases.

| Step | Persona | Device | Light | Dark |
|---|---|---|---|---|
| 1 | U21 | desktop | [light](../images/02-plan-production/u21-production-planner/1-master-plan-desktop-light.png) | [dark](../images/02-plan-production/u21-production-planner/1-master-plan-desktop-dark.png) |
| 1 | U21 | phone | [light](../images/02-plan-production/u21-production-planner/1-master-plan-phone-light.png) | [dark](../images/02-plan-production/u21-production-planner/1-master-plan-phone-dark.png) |
| 1 | U04 | desktop | [light](../images/02-plan-production/u04-purchasing/1-master-plan-desktop-light.png) | [dark](../images/02-plan-production/u04-purchasing/1-master-plan-desktop-dark.png) |
| 2 | U15 | phone | [light](../images/02-plan-production/u15-warehouse-operator/2-pick-and-stage-phone-light.png) | [dark](../images/02-plan-production/u15-warehouse-operator/2-pick-and-stage-phone-dark.png) |
| 2 | U15 | tablet | [light](../images/02-plan-production/u15-warehouse-operator/2-pick-and-stage-tablet-light.png) | [dark](../images/02-plan-production/u15-warehouse-operator/2-pick-and-stage-tablet-dark.png) |
| E1 | U21 | desktop | [light](../images/02-plan-production/u21-production-planner/e1-overload-desktop-light.png) | [dark](../images/02-plan-production/u21-production-planner/e1-overload-desktop-dark.png) |
| E1 | U21 | phone | [light](../images/02-plan-production/u21-production-planner/e1-overload-phone-light.png) | [dark](../images/02-plan-production/u21-production-planner/e1-overload-phone-dark.png) |

## Open questions

None.

---

⬅️ [FL-F12-01 Define the products](fl-f12-01-define-the-products.md) · ⬆️ [Up](README.md) ·
➡️ [FL-F12-03 Make the products](fl-f12-03-make-the-products.md)
