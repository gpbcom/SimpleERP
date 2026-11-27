🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) › 💶 [F13 Payroll (plugin)](../README.md) ›
🔀 [Flows](README.md) › 🔀 FL-F13-01 Set up

# 🔀 FL-F13-01 Set up

**Status:** ✅ specified

## Summary

Covers UC-F13-01, UC-F13-02.

## Personas

- [U06 HR](../../../01-users/personas/u06-hr.md)
- [U07 Administrator](../../../01-users/personas/u07-administrator.md)
- [U45 Payroll officer](../../../01-users/personas/u45-payroll-officer.md)

## Flowchart

```mermaid
flowchart LR
  A[Company payroll] --> B[Employee pay]
```

## Sequence diagram

See each use case.

## Steps

| Step | Persona | Screen | Use case | What happens |
|---|---|---|---|---|
| 1 | U45, U07 | [S-F13-01](../screens/01-set-up/s-f13-01-payroll-set-up.md) | [UC-F13-01](../use-cases/01-set-up/uc-f13-01-set-up-the-company-s-payroll.md) | Set up the company's payroll |
| 2 | U45, U06 | [S-F13-02](../screens/01-set-up/s-f13-02-employee-pay.md) | [UC-F13-02](../use-cases/01-set-up/uc-f13-02-set-up-employees-pay.md) | Set up employees' pay |

### Entities and screens

| Entity | States in this flow | Shown at step and screen | Aggregated view |
|---|---|---|---|
| [E-F13-01 Payroll establishment](../data/e-f13-01-payroll-establishment.md) | Active | 1 [S-F13-01](../screens/01-set-up/s-f13-01-payroll-set-up.md) | Payroll establishments |
| [E-F13-02 Employee pay profile](../data/e-f13-02-employee-pay-profile.md) | Checked, Complete | 2 [S-F13-02](../screens/01-set-up/s-f13-02-employee-pay.md) | Employee pay profiles |

## Errors

As each use case.

## Images

Every step and error, for each persona taking part, in light and dark mode (D120). Steps are numbered as in the Steps
table; E rows are the error cases.

| Step | Persona | Device | Light | Dark |
|---|---|---|---|---|
| 1 | U45 | desktop | [light](../images/01-set-up/u45-payroll-officer/1-company-desktop-light.png) | [dark](../images/01-set-up/u45-payroll-officer/1-company-desktop-dark.png) |
| 1 | U07 | desktop | [light](../images/01-set-up/u07-administrator/1-company-desktop-light.png) | [dark](../images/01-set-up/u07-administrator/1-company-desktop-dark.png) |
| 2 | U45 | desktop | [light](../images/01-set-up/u45-payroll-officer/2-employee-desktop-light.png) | [dark](../images/01-set-up/u45-payroll-officer/2-employee-desktop-dark.png) |
| 2 | U06 | desktop | [light](../images/01-set-up/u06-hr/2-employee-desktop-light.png) | [dark](../images/01-set-up/u06-hr/2-employee-desktop-dark.png) |
| E1 | U45 | desktop | [light](../images/01-set-up/u45-payroll-officer/e1-below-minimum-desktop-light.png) | [dark](../images/01-set-up/u45-payroll-officer/e1-below-minimum-desktop-dark.png) |

## Open questions

None.

---

⬆️ [Up](README.md) · ➡️ [FL-F13-02 Monthly pay run](fl-f13-02-monthly-pay-run.md)
