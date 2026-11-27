🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🏛️ [SC20 Public bodies](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC20-04 Public-sector HR and pay](README.md) ›
🖥️ S-SC20-15 Public contributions

# 🖥️ S-SC20-15 Public contributions

**Status:** ✅ specified

## Personas

- [U45 Payroll officer](../../../../01-users/personas/u45-payroll-officer.md): the contributions by scheme and employee,
  with the exceptions.

## Purpose

Compute and declare the contributions of public-sector staff by their pension scheme.

## Entry points

Public bodies › Contributions; the closed pay run.

## Wireframe

```text
+--------------------------------------------------------------------------------------------------+
| Contributions: July 2027                                  [Compute] [Prepare declaration]        |
| Scheme                       Employees   Base          Employee    Employer                      |
| Local civil servants' fund   186         452,300.00    ...         ...                           |
| General scheme + supplement  28          52,800.00     ...         ...                           |
| Exceptions: 3 (status change 2, threshold 1)                        [Review]                     |
+--------------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC20-04 step 3, U45 | desktop | ![FL-SC20-04 step 3, U45, light](../../images/04-public-hr-and-pay/u45-payroll-officer/3-public-contributions-desktop-light.png) | ![FL-SC20-04 step 3, U45, dark](../../images/04-public-hr-and-pay/u45-payroll-officer/3-public-contributions-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc20-15-public-contributions-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc20-15-public-contributions-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc20-15-public-contributions-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc20-15-public-contributions-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc20-15-public-contributions-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc20-15-public-contributions-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-sc20-15-public-contributions-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-sc20-15-public-contributions-offline-desktop-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Scheme | E-F13-17 scheme | text | no | yes |
| Employees | E-F13-17 employees | number | no | yes |
| Base | E-F13-09 base | amount | no | yes |
| Employee share | E-F13-09 employee | amount | no | yes |
| Employer share | E-F13-09 employer | amount | no | yes |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Compute | header | payroll officer | the contributions of the month are computed |
| Review exceptions | row | payroll officer | a status change or threshold is checked |
| Prepare declaration | header | payroll officer | the declaration is prepared |

## States

- Normal: the schemes with employees, base, employee and employer shares and the exceptions.
- Empty: No employee to declare this month.
- Loading: the headings and the table as placeholders; the values follow.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); a missing
  status, a missing rate, with the employee or scheme named.
- Read-only: the record in a locked state: values shown, no action offered.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): none; no flow's Entities and screens table names an entity on this screen.

## Responsive behaviour

Desktop only; on a phone, the app asks to continue on a larger screen.

## Accessibility

Every control is reachable by keyboard; states and errors are announced to screen readers and never rely on colour
alone; each field has its visible label.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)
- [C-01 Button](../../../../04-ux/design-system/components/c-01-button.md)

## Shown in

- [FL-SC20-04 Public-sector HR and pay](../../flows/fl-sc20-04-public-hr-and-pay.md)

## Open questions

None.

---

⬅️ [S-SC20-14 Statutory pay](s-sc20-14-statutory-pay.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC20-16 Budget assistant](s-sc20-16-budget-assistant.md)
