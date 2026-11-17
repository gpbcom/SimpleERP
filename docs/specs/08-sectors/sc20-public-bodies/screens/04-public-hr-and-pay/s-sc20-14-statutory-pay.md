🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🏛️ [SC20 Public bodies](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC20-04 Public-sector HR and pay](README.md) › 🖥️ S-SC20-14 Statutory pay

# 🖥️ S-SC20-14 Statutory pay

**Status:** 🔄 waiting for the owner

## Personas

- [U45 Payroll officer](../../../../01-users/personas/u45-payroll-officer.md): the month's pay by employee, with the
  index number, the point value and the supplements.

## Purpose

Compute the statutory pay of civil servants from the index number and the point value.

## Entry points

Public bodies › Statutory pay; the monthly pay run.

## Wireframe

```text
+--------------------------------------------------------------------------------------------------+
| Statutory pay: July 2027                                    Point value 5.8731   [Compute]       |
| Employee   Grade        Step  Index   Basic pay   Supplements   Gross     Difference             |
| Roux       Tech. B      4     410     2,408.07    186.20        2,594.27  0.00                   |
| Faure      Admin. C     2     364     2,137.89    120.00        2,257.89  +36.40                 |
| Petit      Tech. B      5     430     -           -             -         No step                |
+--------------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC20-04 step 2, U45 | desktop | ![FL-SC20-04 step 2, U45, light](../../images/04-public-hr-and-pay/u45-payroll-officer/2-statutory-pay-desktop-light.png) | ![FL-SC20-04 step 2, U45, dark](../../images/04-public-hr-and-pay/u45-payroll-officer/2-statutory-pay-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc20-14-statutory-pay-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc20-14-statutory-pay-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc20-14-statutory-pay-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc20-14-statutory-pay-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc20-14-statutory-pay-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc20-14-statutory-pay-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-sc20-14-statutory-pay-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-sc20-14-statutory-pay-offline-desktop-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Employee | E-F13-04 employee | link | no | yes |
| Index number | E-SC20-11 index number | number | no | yes |
| Point value | E-F13-16 point value | amount | no | yes |
| Supplements | E-F13-04 supplements | list of supplement and amount | yes | no |
| Difference | E-F13-04 difference | amount | no | no |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Compute | header | payroll officer | the pay of the month is computed |
| Explain a difference | row | payroll officer | a difference is explained or corrected |
| Continue to the pay run | header | payroll officer | the lines go to the pay run |

## States

- Normal: the employees with grade, step, index number, basic pay, supplements and difference.
- Empty: No civil servant to pay this month.
- Loading: the headings and the table as placeholders; the values follow.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); a missing step,
  a point value missing for the month, with the employee named.
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

⬅️ [S-SC20-13 Grades and steps](s-sc20-13-grades-and-steps.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC20-15 Public contributions](s-sc20-15-public-contributions.md)
