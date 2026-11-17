🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
🏭 [F12 Manufacturing (plugin)](../README.md) › 🔀 [Flows](README.md) › 🔀 FL-F12-03 Make the products

# 🔀 FL-F12-03 Make the products

**Status:** ✅ specified

## Summary

Covers UC-F12-04, UC-F12-05, UC-F12-06, UC-F12-11.

## Personas

- [U02 Manager](../../../01-users/personas/u02-manager.md)
- [U15 Warehouse operator](../../../01-users/personas/u15-warehouse-operator.md)
- [U20 Production operator](../../../01-users/personas/u20-production-operator.md)
- [U21 Production planner](../../../01-users/personas/u21-production-planner.md)

## Flowchart

```mermaid
flowchart LR
  A[Manufacturing order] --> B[Shop-floor tablet]
  B --> C[Consume and trace]
  C --> D[Done]
  D -.-> E[Unbuild or repair]
```

## Sequence diagram

See each use case.

## Steps

| Step | Persona | Screen | Use case | What happens |
|---|---|---|---|---|
| 1 | U21, U02 | [S-F12-04](../screens/03-make-the-products/s-f12-04-manufacturing-order.md) | [UC-F12-04](../use-cases/03-make-the-products/uc-f12-04-launch-and-follow-manufacturing-orders.md) | Launch and follow manufacturing orders |
| 2 | U20 | [S-F12-05](../screens/03-make-the-products/s-f12-05-shop-floor-tablet.md) | [UC-F12-05](../use-cases/03-make-the-products/uc-f12-05-work-on-the-shop-floor-tablet.md) | Work on the shop-floor tablet |
| 3 | U20, U15 | [S-F12-06](../screens/03-make-the-products/s-f12-06-consumption.md) | [UC-F12-06](../use-cases/03-make-the-products/uc-f12-06-consume-components-trace-lots-and-serials.md) | Consume components, trace lots and serials |
| 4 | U21, U20 | [S-F12-11](../screens/03-make-the-products/s-f12-11-unbuild-and-repair.md) | [UC-F12-11](../use-cases/03-make-the-products/uc-f12-11-unbuild-rework-and-repair.md) | Unbuild, rework and repair |

### Entities and screens

| Entity | States in this flow | Shown at step and screen | Aggregated view |
|---|---|---|---|
| [E-F12-04 Manufacturing order](../data/e-f12-04-manufacturing-order.md) | Draft, Confirmed, In progress, Done | 1 [S-F12-04](../screens/03-make-the-products/s-f12-04-manufacturing-order.md); 2 [S-F12-05](../screens/03-make-the-products/s-f12-05-shop-floor-tablet.md); 3 [S-F12-06](../screens/03-make-the-products/s-f12-06-consumption.md); 4 [S-F12-11](../screens/03-make-the-products/s-f12-11-unbuild-and-repair.md) | Manufacturing orders |
| [E-F12-28 Shop-floor terminal](../data/e-f12-28-shop-floor-terminal.md) | Active | 2 [S-F12-05](../screens/03-make-the-products/s-f12-05-shop-floor-tablet.md) | Shop-floor terminals |
| [E-F12-29 Unbuild order](../data/e-f12-29-unbuild-order.md) | Active | 4 [S-F12-11](../screens/03-make-the-products/s-f12-11-unbuild-and-repair.md) | Unbuild orders |
| [E-F7-14 Repair order](../../f07-purchasing-and-stock/data/e-f07-14-repair-order.md) | Done | Shown elsewhere: [S-F7-17 Repairs](../../f07-purchasing-and-stock/screens/06-benchmark-additions/s-f07-17-repairs.md) | Repair orders |

## Errors

As each use case.

## Images

Every step and error, for each persona taking part, in light and dark mode (D120). Steps are numbered as in the Steps
table; E rows are the error cases.

| Step | Persona | Device | Light | Dark |
|---|---|---|---|---|
| 1 | U21 | desktop | [light](../images/03-make-the-products/u21-production-planner/1-manufacturing-order-desktop-light.png) | [dark](../images/03-make-the-products/u21-production-planner/1-manufacturing-order-desktop-dark.png) |
| 1 | U21 | phone | [light](../images/03-make-the-products/u21-production-planner/1-manufacturing-order-phone-light.png) | [dark](../images/03-make-the-products/u21-production-planner/1-manufacturing-order-phone-dark.png) |
| 1 | U02 | desktop | [light](../images/03-make-the-products/u02-manager/1-manufacturing-order-desktop-light.png) | [dark](../images/03-make-the-products/u02-manager/1-manufacturing-order-desktop-dark.png) |
| 1 | U02 | phone | [light](../images/03-make-the-products/u02-manager/1-manufacturing-order-phone-light.png) | [dark](../images/03-make-the-products/u02-manager/1-manufacturing-order-phone-dark.png) |
| 2 | U20 | tablet | [light](../images/03-make-the-products/u20-production-operator/2-shop-floor-tablet-tablet-light.png) | [dark](../images/03-make-the-products/u20-production-operator/2-shop-floor-tablet-tablet-dark.png) |
| 3 | U20 | tablet | [light](../images/03-make-the-products/u20-production-operator/3-consume-and-trace-tablet-light.png) | [dark](../images/03-make-the-products/u20-production-operator/3-consume-and-trace-tablet-dark.png) |
| 3 | U15 | phone | [light](../images/03-make-the-products/u15-warehouse-operator/3-consume-and-trace-phone-light.png) | [dark](../images/03-make-the-products/u15-warehouse-operator/3-consume-and-trace-phone-dark.png) |
| 3 | U15 | tablet | [light](../images/03-make-the-products/u15-warehouse-operator/3-consume-and-trace-tablet-light.png) | [dark](../images/03-make-the-products/u15-warehouse-operator/3-consume-and-trace-tablet-dark.png) |
| 4 | U21 | desktop | [light](../images/03-make-the-products/u21-production-planner/4-unbuild-repair-desktop-light.png) | [dark](../images/03-make-the-products/u21-production-planner/4-unbuild-repair-desktop-dark.png) |
| 4 | U21 | phone | [light](../images/03-make-the-products/u21-production-planner/4-unbuild-repair-phone-light.png) | [dark](../images/03-make-the-products/u21-production-planner/4-unbuild-repair-phone-dark.png) |
| 4 | U20 | tablet | [light](../images/03-make-the-products/u20-production-operator/4-unbuild-repair-tablet-light.png) | [dark](../images/03-make-the-products/u20-production-operator/4-unbuild-repair-tablet-dark.png) |
| E1 | U21 | desktop | [light](../images/03-make-the-products/u21-production-planner/e1-missing-components-desktop-light.png) | [dark](../images/03-make-the-products/u21-production-planner/e1-missing-components-desktop-dark.png) |
| E1 | U21 | phone | [light](../images/03-make-the-products/u21-production-planner/e1-missing-components-phone-light.png) | [dark](../images/03-make-the-products/u21-production-planner/e1-missing-components-phone-dark.png) |

## Open questions

None.

---

⬅️ [FL-F12-02 Plan production](fl-f12-02-plan-production.md) · ⬆️ [Up](README.md) ·
➡️ [FL-F12-04 Quality and maintenance](fl-f12-04-quality-and-maintenance.md)
