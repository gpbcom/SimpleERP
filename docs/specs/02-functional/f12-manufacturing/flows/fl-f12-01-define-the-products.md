🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
🏭 [F12 Manufacturing (plugin)](../README.md) › 🔀 [Flows](README.md) › 🔀 FL-F12-01 Define the products

# 🔀 FL-F12-01 Define the products

**Status:** ✅ specified

## Summary

Covers UC-F12-01, UC-F12-02, UC-F12-10.

## Personas

- [U02 Manager](../../../01-users/personas/u02-manager.md)
- [U21 Production planner](../../../01-users/personas/u21-production-planner.md)

## Flowchart

```mermaid
flowchart LR
  A[Bill of materials] --> B[Work centres and routings]
  B --> C[Engineering changes]
```

## Sequence diagram

See each use case.

## Steps

| Step | Persona | Screen | Use case | What happens |
|---|---|---|---|---|
| 1 | U21 | [S-F12-01](../screens/01-define-the-products/s-f12-01-bill-of-materials.md) | [UC-F12-01](../use-cases/01-define-the-products/uc-f12-01-define-bills-of-materials.md) | Define bills of materials |
| 2 | U21 | [S-F12-02](../screens/01-define-the-products/s-f12-02-routing.md) | [UC-F12-02](../use-cases/01-define-the-products/uc-f12-02-define-work-centres-and-routings.md) | Define work centres and routings |
| 3 | U21, U02 | [S-F12-10](../screens/01-define-the-products/s-f12-10-engineering-change.md) | [UC-F12-10](../use-cases/01-define-the-products/uc-f12-10-manage-engineering-changes.md) | Manage engineering changes |

### Entities and screens

| Entity | States in this flow | Shown at step and screen | Aggregated view |
|---|---|---|---|
| [E-F12-01 Bill of materials](../data/e-f12-01-bill-of-materials.md) | Draft, Approved, Retired | 1 [S-F12-01](../screens/01-define-the-products/s-f12-01-bill-of-materials.md); 3 [S-F12-10](../screens/01-define-the-products/s-f12-10-engineering-change.md) | Bill of materials |
| [E-F12-02 Work centre](../data/e-f12-02-work-centre.md) | Active | 2 [S-F12-02](../screens/01-define-the-products/s-f12-02-routing.md) | Work centres |
| [E-F12-03 Routing operation](../data/e-f12-03-routing-operation.md) | Active | 2 [S-F12-02](../screens/01-define-the-products/s-f12-02-routing.md) | Routing operations |
| [E-F12-11 Engineering change](../data/e-f12-11-engineering-change.md) | Active | 3 [S-F12-10](../screens/01-define-the-products/s-f12-10-engineering-change.md) | Engineering changes |

## Errors

As each use case.

## Images

Every step and error, for each persona taking part, in light and dark mode (D120). Steps are numbered as in the Steps
table; E rows are the error cases.

| Step | Persona | Device | Light | Dark |
|---|---|---|---|---|
| 1 | U21 | desktop | [light](../images/01-define-the-products/u21-production-planner/1-bill-of-materials-desktop-light.png) | [dark](../images/01-define-the-products/u21-production-planner/1-bill-of-materials-desktop-dark.png) |
| 1 | U21 | phone | [light](../images/01-define-the-products/u21-production-planner/1-bill-of-materials-phone-light.png) | [dark](../images/01-define-the-products/u21-production-planner/1-bill-of-materials-phone-dark.png) |
| 2 | U21 | desktop | [light](../images/01-define-the-products/u21-production-planner/2-routing-desktop-light.png) | [dark](../images/01-define-the-products/u21-production-planner/2-routing-desktop-dark.png) |
| 2 | U21 | phone | [light](../images/01-define-the-products/u21-production-planner/2-routing-phone-light.png) | [dark](../images/01-define-the-products/u21-production-planner/2-routing-phone-dark.png) |
| 3 | U02 | desktop | [light](../images/01-define-the-products/u02-manager/3-engineering-change-desktop-light.png) | [dark](../images/01-define-the-products/u02-manager/3-engineering-change-desktop-dark.png) |
| 3 | U02 | phone | [light](../images/01-define-the-products/u02-manager/3-engineering-change-phone-light.png) | [dark](../images/01-define-the-products/u02-manager/3-engineering-change-phone-dark.png) |
| 3 | U21 | desktop | [light](../images/01-define-the-products/u21-production-planner/3-engineering-change-desktop-light.png) | [dark](../images/01-define-the-products/u21-production-planner/3-engineering-change-desktop-dark.png) |
| 3 | U21 | phone | [light](../images/01-define-the-products/u21-production-planner/3-engineering-change-phone-light.png) | [dark](../images/01-define-the-products/u21-production-planner/3-engineering-change-phone-dark.png) |
| E1 | U21 | desktop | [light](../images/01-define-the-products/u21-production-planner/e1-component-loop-desktop-light.png) | [dark](../images/01-define-the-products/u21-production-planner/e1-component-loop-desktop-dark.png) |
| E1 | U21 | phone | [light](../images/01-define-the-products/u21-production-planner/e1-component-loop-phone-light.png) | [dark](../images/01-define-the-products/u21-production-planner/e1-component-loop-phone-dark.png) |

## Open questions

None.

---

⬆️ [Up](README.md) · ➡️ [FL-F12-02 Plan production](fl-f12-02-plan-production.md)
