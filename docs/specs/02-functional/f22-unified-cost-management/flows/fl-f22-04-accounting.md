🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
💸 [F22 Unified platform cost management](../README.md) › 🔀 [Flows](README.md) › 🔀 FL-F22-04 Accounting

# 🔀 FL-F22-04 Accounting

**Status:** ✅ specified

## Summary

Covers UC-F22-03, UC-F22-12, UC-F22-13, UC-F22-14, UC-F22-19.

## Personas

- [U02 Manager](../../../01-users/personas/u02-manager.md)
- [U05 Accounting](../../../01-users/personas/u05-accounting.md)
- [U13 Owner](../../../01-users/personas/u13-owner.md)

## Flowchart

```mermaid
flowchart LR
  A[Costs] --> B[Allocation]
  B --> C[Invoice matching]
  C --> D[Reports and forecast]
```

## Sequence diagram

See each use case.

## Steps

| Step | Persona | Screen | Use case | What happens |
|---|---|---|---|---|
| 1 | U02, U05 | [S-F22-03](../screens/04-accounting/s-f22-03-cost-allocation.md) | [UC-F22-03](../use-cases/04-accounting/uc-f22-03-see-costs-per-department-project-and-client.md) | See costs per department, project and client |
| 2 | U13, U05 | [S-F22-12](../screens/04-accounting/s-f22-12-forecast.md) | [UC-F22-12](../use-cases/04-accounting/uc-f22-12-forecast-the-month-s-costs.md) | Forecast the month's costs |
| 3 | U05 | [S-F22-13](../screens/04-accounting/s-f22-13-invoice-matching.md) | [UC-F22-13](../use-cases/04-accounting/uc-f22-13-match-suppliers-invoices-in-accounting.md) | Match suppliers' invoices in accounting |
| 4 | U05 | [S-F22-14](../screens/04-accounting/s-f22-14-allocation-rules.md) | [UC-F22-14](../use-cases/04-accounting/uc-f22-14-allocate-costs-to-accounts-and-projects.md) | Allocate costs to accounts and projects |
| 5 | U05, U13 | [S-F22-19](../screens/04-accounting/s-f22-19-cost-reports.md) | [UC-F22-19](../use-cases/04-accounting/uc-f22-19-export-and-report-costs.md) | Export and report costs |

### Entities and screens

| Entity | States in this flow | Shown at step and screen | Aggregated view |
|---|---|---|---|
| [E-F22-02 Metered call record](../data/e-f22-02-metered-call-record.md) | Recorded | 1 [S-F22-03](../screens/04-accounting/s-f22-03-cost-allocation.md); 3 [S-F22-13](../screens/04-accounting/s-f22-13-invoice-matching.md); 4 [S-F22-14](../screens/04-accounting/s-f22-14-allocation-rules.md); 5 [S-F22-19](../screens/04-accounting/s-f22-19-cost-reports.md) | Metered call records |
| [E-F22-09 Allocation rule](../data/e-f22-09-allocation-rule.md) | Active | 1 [S-F22-03](../screens/04-accounting/s-f22-03-cost-allocation.md); 4 [S-F22-14](../screens/04-accounting/s-f22-14-allocation-rules.md) | Allocation rules |
| [E-F22-12 Invoice match](../data/e-f22-12-invoice-match.md) | Matched, Flagged | 3 [S-F22-13](../screens/04-accounting/s-f22-13-invoice-matching.md) | Invoice matches |
| [E-F22-11 Forecast](../data/e-f22-11-forecast.md) | Active | 2 [S-F22-12](../screens/04-accounting/s-f22-12-forecast.md); 5 [S-F22-19](../screens/04-accounting/s-f22-19-cost-reports.md) | Forecasts |

## Errors

As each use case.

## Images

Every step and error, for each persona taking part, in light and dark mode (D120). Steps are numbered as in the Steps
table; E rows are the error cases.

| Step | Persona | Device | Light | Dark |
|---|---|---|---|---|
| 1 | U02 | desktop | [light](../images/04-accounting/u02-manager/1-allocation-desktop-light.png) | [dark](../images/04-accounting/u02-manager/1-allocation-desktop-dark.png) |
| 1 | U02 | phone | [light](../images/04-accounting/u02-manager/1-allocation-phone-light.png) | [dark](../images/04-accounting/u02-manager/1-allocation-phone-dark.png) |
| 1 | U05 | desktop | [light](../images/04-accounting/u05-accounting/1-allocation-desktop-light.png) | [dark](../images/04-accounting/u05-accounting/1-allocation-desktop-dark.png) |
| 2 | U13 | desktop | [light](../images/04-accounting/u13-owner/2-forecast-desktop-light.png) | [dark](../images/04-accounting/u13-owner/2-forecast-desktop-dark.png) |
| 2 | U13 | phone | [light](../images/04-accounting/u13-owner/2-forecast-phone-light.png) | [dark](../images/04-accounting/u13-owner/2-forecast-phone-dark.png) |
| 2 | U05 | desktop | [light](../images/04-accounting/u05-accounting/2-forecast-desktop-light.png) | [dark](../images/04-accounting/u05-accounting/2-forecast-desktop-dark.png) |
| 3 | U05 | desktop | [light](../images/04-accounting/u05-accounting/3-matching-desktop-light.png) | [dark](../images/04-accounting/u05-accounting/3-matching-desktop-dark.png) |
| 4 | U05 | desktop | [light](../images/04-accounting/u05-accounting/4-rules-desktop-light.png) | [dark](../images/04-accounting/u05-accounting/4-rules-desktop-dark.png) |
| 5 | U05 | desktop | [light](../images/04-accounting/u05-accounting/5-reports-desktop-light.png) | [dark](../images/04-accounting/u05-accounting/5-reports-desktop-dark.png) |
| 5 | U13 | desktop | [light](../images/04-accounting/u13-owner/5-reports-desktop-light.png) | [dark](../images/04-accounting/u13-owner/5-reports-desktop-dark.png) |
| 5 | U13 | phone | [light](../images/04-accounting/u13-owner/5-reports-phone-light.png) | [dark](../images/04-accounting/u13-owner/5-reports-phone-dark.png) |
| E1 | U05 | desktop | [light](../images/04-accounting/u05-accounting/e1-gap-desktop-light.png) | [dark](../images/04-accounting/u05-accounting/e1-gap-desktop-dark.png) |

## Open questions

None.

---

⬅️ [FL-F22-03 Runs](fl-f22-03-runs.md) · ⬆️ [Up](README.md) · ➡️ [FL-F22-05 Billing](fl-f22-05-billing.md)
