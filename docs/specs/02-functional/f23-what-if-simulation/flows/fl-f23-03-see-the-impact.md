🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
🔮 [F23 What-if simulation and impact](../README.md) › 🔀 [Flows](README.md) › 🔀 FL-F23-03 See the impact

# 🔀 FL-F23-03 See the impact

**Status:** ✅ specified

## Summary

Covers UC-F23-06, UC-F23-07, UC-F23-08, UC-F23-09, UC-F23-10, UC-F23-11, UC-F23-12, UC-F23-13.

## Personas

- [U03 Sales](../../../01-users/personas/u03-sales.md)
- [U04 Purchasing](../../../01-users/personas/u04-purchasing.md)
- [U05 Accounting](../../../01-users/personas/u05-accounting.md)
- [U06 HR](../../../01-users/personas/u06-hr.md)
- [U13 Owner](../../../01-users/personas/u13-owner.md)
- [U21 Production planner](../../../01-users/personas/u21-production-planner.md)
- [U31 Treasurer](../../../01-users/personas/u31-treasurer.md)

## Flowchart

```mermaid
flowchart LR
  A[Results] --> B[Sales and margin]
  A --> C[Cash and statements]
  A --> D[Stock and capacity]
  A --> E[Staff and legal]
  E -.-> UUCF2326[Simulate a price change on the pipeline]
  UUCF2326 -.-> UUCF2327[Simulate a supplier switch]
  UUCF2327 -.-> UUCF2328[Simulate a hiring plan]
  UUCF2328 -.-> UUCF2330[Simulate a new shift or machine]
```

## Sequence diagram

See each use case.

## Steps

| Step | Persona | Screen | Use case | What happens |
|---|---|---|---|---|
| 1 | U13, U03 | [S-F23-06](../screens/03-see-the-impact/s-f23-06-sales-impact.md) | [UC-F23-06](../use-cases/03-see-the-impact/uc-f23-06-see-the-impact-on-sales-and-margin.md) | See the impact on sales and margin |
| 2 | U31, U05 | [S-F23-07](../screens/03-see-the-impact/s-f23-07-cash-impact.md) | [UC-F23-07](../use-cases/03-see-the-impact/uc-f23-07-see-the-impact-on-cash-and-treasury.md) | See the impact on cash and treasury |
| 3 | U05 | [S-F23-08](../screens/03-see-the-impact/s-f23-08-statements-impact.md) | [UC-F23-08](../use-cases/03-see-the-impact/uc-f23-08-see-the-impact-on-the-profit-and-loss-and-balance-sheet.md) | See the impact on the profit and loss and balance sheet |
| 4 | U04 | [S-F23-09](../screens/03-see-the-impact/s-f23-09-stock-impact.md) | [UC-F23-09](../use-cases/03-see-the-impact/uc-f23-09-see-the-impact-on-stock-and-purchases.md) | See the impact on stock and purchases |
| 5 | U21 | [S-F23-10](../screens/03-see-the-impact/s-f23-10-capacity-impact.md) | [UC-F23-10](../use-cases/03-see-the-impact/uc-f23-10-see-the-impact-on-production-and-capacity.md) | See the impact on production and capacity |
| 6 | U06 | [S-F23-11](../screens/03-see-the-impact/s-f23-11-staff-impact.md) | [UC-F23-11](../use-cases/03-see-the-impact/uc-f23-11-see-the-impact-on-staff-payroll-and-planning.md) | See the impact on staff, payroll and planning |
| 7 | U13, U05 | [S-F23-12](../screens/03-see-the-impact/s-f23-12-legal-impact.md) | [UC-F23-12](../use-cases/03-see-the-impact/uc-f23-12-see-legal-thresholds-and-taxes-crossed.md) | See legal thresholds and taxes crossed |
| 8 | U13 | [S-F23-13](../screens/03-see-the-impact/s-f23-13-platform-costs-impact.md) | [UC-F23-13](../use-cases/03-see-the-impact/uc-f23-13-include-platform-costs-in-a-scenario.md) | Include platform costs in a scenario |
| 9 | U03 | [S-F23-06](../screens/03-see-the-impact/s-f23-06-sales-impact.md) | [UC-F23-26](../use-cases/03-see-the-impact/uc-f23-26-simulate-a-price-change-on-the-pipeline.md) | Simulate a price change on the pipeline |
| 10 | U04 | [S-F23-09](../screens/03-see-the-impact/s-f23-09-stock-impact.md) | [UC-F23-27](../use-cases/03-see-the-impact/uc-f23-27-simulate-a-supplier-switch.md) | Simulate a supplier switch |
| 11 | U06 | [S-F23-11](../screens/03-see-the-impact/s-f23-11-staff-impact.md) | [UC-F23-28](../use-cases/03-see-the-impact/uc-f23-28-simulate-a-hiring-plan.md) | Simulate a hiring plan |
| 12 | U21 | [S-F23-10](../screens/03-see-the-impact/s-f23-10-capacity-impact.md) | [UC-F23-30](../use-cases/03-see-the-impact/uc-f23-30-simulate-a-new-shift-or-machine.md) | Simulate a new shift or machine |

### Entities and screens

| Entity | States in this flow | Shown at step and screen | Aggregated view |
|---|---|---|---|
| [E-F23-05 Impact result](../data/e-f23-05-impact-result.md) | Recorded | 1, 9 [S-F23-06](../screens/03-see-the-impact/s-f23-06-sales-impact.md); 2 [S-F23-07](../screens/03-see-the-impact/s-f23-07-cash-impact.md); 3 [S-F23-08](../screens/03-see-the-impact/s-f23-08-statements-impact.md); 4, 10 [S-F23-09](../screens/03-see-the-impact/s-f23-09-stock-impact.md); 5, 12 [S-F23-10](../screens/03-see-the-impact/s-f23-10-capacity-impact.md); 6, 11 [S-F23-11](../screens/03-see-the-impact/s-f23-11-staff-impact.md); 7 [S-F23-12](../screens/03-see-the-impact/s-f23-12-legal-impact.md); 8 [S-F23-13](../screens/03-see-the-impact/s-f23-13-platform-costs-impact.md) | Impact results |
| [E-F23-03 Scenario change](../data/e-f23-03-scenario-change.md) | Active | 8 [S-F23-13](../screens/03-see-the-impact/s-f23-13-platform-costs-impact.md) | Scenario changes |
| [E-F6-02 Opportunity](../../f06-customers-and-sales/data/e-f06-02-opportunity.md) | Active | Shown elsewhere: [S-F6-01 Pipeline](../../f06-customers-and-sales/screens/01-lead-to-quote/s-f06-01-pipeline.md) | Opportunities |
| [E-F9-16 Shift](../../f09-hr-and-projects/data/e-f09-16-shift.md) | Draft, Published | Shown elsewhere: [S-F9-30 Scheduling board](../../f09-hr-and-projects/screens/12-schedule-customer-requests/s-f09-30-scheduling-board.md) | Shifts |
| [E-F12-09 Equipment](../../f12-manufacturing/data/e-f12-09-equipment.md) | Active | Shown elsewhere: [S-F12-08 Maintenance](../../f12-manufacturing/screens/04-quality-and-maintenance/s-f12-08-maintenance.md) | Equipments |

## Errors

As each use case.

## Images

Every step and error, for each persona taking part, in light and dark mode (D120). Steps are numbered as in the Steps
table; E rows are the error cases.

| Step | Persona | Device | Light | Dark |
|---|---|---|---|---|
| 1 | U03 | desktop | [light](../images/03-see-the-impact/u03-sales/1-sales-desktop-light.png) | [dark](../images/03-see-the-impact/u03-sales/1-sales-desktop-dark.png) |
| 1 | U03 | phone | [light](../images/03-see-the-impact/u03-sales/1-sales-phone-light.png) | [dark](../images/03-see-the-impact/u03-sales/1-sales-phone-dark.png) |
| 1 | U03 | tablet | [light](../images/03-see-the-impact/u03-sales/1-sales-tablet-light.png) | [dark](../images/03-see-the-impact/u03-sales/1-sales-tablet-dark.png) |
| 1 | U13 | desktop | [light](../images/03-see-the-impact/u13-owner/1-sales-desktop-light.png) | [dark](../images/03-see-the-impact/u13-owner/1-sales-desktop-dark.png) |
| 1 | U13 | phone | [light](../images/03-see-the-impact/u13-owner/1-sales-phone-light.png) | [dark](../images/03-see-the-impact/u13-owner/1-sales-phone-dark.png) |
| 2 | U31 | desktop | [light](../images/03-see-the-impact/u31-treasurer/2-cash-desktop-light.png) | [dark](../images/03-see-the-impact/u31-treasurer/2-cash-desktop-dark.png) |
| 2 | U31 | phone | [light](../images/03-see-the-impact/u31-treasurer/2-cash-phone-light.png) | [dark](../images/03-see-the-impact/u31-treasurer/2-cash-phone-dark.png) |
| 2 | U05 | desktop | [light](../images/03-see-the-impact/u05-accounting/2-cash-desktop-light.png) | [dark](../images/03-see-the-impact/u05-accounting/2-cash-desktop-dark.png) |
| 3 | U05 | desktop | [light](../images/03-see-the-impact/u05-accounting/3-statements-desktop-light.png) | [dark](../images/03-see-the-impact/u05-accounting/3-statements-desktop-dark.png) |
| 4 | U04 | desktop | [light](../images/03-see-the-impact/u04-purchasing/4-stock-desktop-light.png) | [dark](../images/03-see-the-impact/u04-purchasing/4-stock-desktop-dark.png) |
| 5 | U21 | desktop | [light](../images/03-see-the-impact/u21-production-planner/5-capacity-desktop-light.png) | [dark](../images/03-see-the-impact/u21-production-planner/5-capacity-desktop-dark.png) |
| 5 | U21 | phone | [light](../images/03-see-the-impact/u21-production-planner/5-capacity-phone-light.png) | [dark](../images/03-see-the-impact/u21-production-planner/5-capacity-phone-dark.png) |
| 6 | U06 | desktop | [light](../images/03-see-the-impact/u06-hr/6-staff-desktop-light.png) | [dark](../images/03-see-the-impact/u06-hr/6-staff-desktop-dark.png) |
| 7 | U13 | desktop | [light](../images/03-see-the-impact/u13-owner/7-legal-desktop-light.png) | [dark](../images/03-see-the-impact/u13-owner/7-legal-desktop-dark.png) |
| 7 | U13 | phone | [light](../images/03-see-the-impact/u13-owner/7-legal-phone-light.png) | [dark](../images/03-see-the-impact/u13-owner/7-legal-phone-dark.png) |
| 7 | U05 | desktop | [light](../images/03-see-the-impact/u05-accounting/7-legal-desktop-light.png) | [dark](../images/03-see-the-impact/u05-accounting/7-legal-desktop-dark.png) |
| 8 | U13 | desktop | [light](../images/03-see-the-impact/u13-owner/8-platform-desktop-light.png) | [dark](../images/03-see-the-impact/u13-owner/8-platform-desktop-dark.png) |
| 8 | U13 | phone | [light](../images/03-see-the-impact/u13-owner/8-platform-phone-light.png) | [dark](../images/03-see-the-impact/u13-owner/8-platform-phone-dark.png) |
| E1 | U21 | desktop | [light](../images/03-see-the-impact/u21-production-planner/e1-no-data-desktop-light.png) | [dark](../images/03-see-the-impact/u21-production-planner/e1-no-data-desktop-dark.png) |
| E1 | U21 | phone | [light](../images/03-see-the-impact/u21-production-planner/e1-no-data-phone-light.png) | [dark](../images/03-see-the-impact/u21-production-planner/e1-no-data-phone-dark.png) |
| 9 | U03 | desktop | [light](../images/03-see-the-impact/u03-sales/9-sales-impact-desktop-light.png) | [dark](../images/03-see-the-impact/u03-sales/9-sales-impact-desktop-dark.png) |
| 9 | U03 | phone | [light](../images/03-see-the-impact/u03-sales/9-sales-impact-phone-light.png) | [dark](../images/03-see-the-impact/u03-sales/9-sales-impact-phone-dark.png) |
| 9 | U03 | tablet | [light](../images/03-see-the-impact/u03-sales/9-sales-impact-tablet-light.png) | [dark](../images/03-see-the-impact/u03-sales/9-sales-impact-tablet-dark.png) |
| 10 | U04 | desktop | [light](../images/03-see-the-impact/u04-purchasing/10-stock-impact-desktop-light.png) | [dark](../images/03-see-the-impact/u04-purchasing/10-stock-impact-desktop-dark.png) |
| 11 | U06 | desktop | [light](../images/03-see-the-impact/u06-hr/11-staff-impact-desktop-light.png) | [dark](../images/03-see-the-impact/u06-hr/11-staff-impact-desktop-dark.png) |
| 12 | U21 | desktop | [light](../images/03-see-the-impact/u21-production-planner/12-capacity-impact-desktop-light.png) | [dark](../images/03-see-the-impact/u21-production-planner/12-capacity-impact-desktop-dark.png) |
| 12 | U21 | phone | [light](../images/03-see-the-impact/u21-production-planner/12-capacity-impact-phone-light.png) | [dark](../images/03-see-the-impact/u21-production-planner/12-capacity-impact-phone-dark.png) |

## Open questions

None.

---

⬅️ [FL-F23-02 Run](fl-f23-02-run.md) · ⬆️ [Up](README.md) · ➡️ [FL-F23-04 Decide](fl-f23-04-decide.md)
