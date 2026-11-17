🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
💶 [F13 Payroll (plugin)](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F13-10 Special contracts and outsourced payroll](README.md) › 🖥️ S-F13-29 Days-based contracts

# 🖥️ S-F13-29 Days-based contracts

**Status:** 🔄 waiting for the owner

## Personas

- [U45 Payroll officer](../../../../01-users/personas/u45-payroll-officer.md): every package and the months to confirm.
- [U01 Employee](../../../../01-users/personas/u01-employee.md): their own days, from their phone.

## Purpose

Follow each package: days worked, rest taken, days left; declare and confirm the days of a month.

## Entry points

Payroll (plugin) › Days-based contracts; on a phone, My days in the self-service.

## Wireframe

```text
+---------------------------------------------------------------------------------------------+
| Days-based contracts: 2026                              Waiting 6   Rest alerts 2   [Remind] |
|---------------------------------------------------------------------------------------------|
| EMPLOYEE     PACKAGE  WORKED  LEFT  MONTH      DECLARED  CONFIRMED  REST                   |
| Lea M.       218      187     31    Nov 2026   20        Waiting    OK                     |
| Karim D.     218      214     4     Nov 2026   22        Confirmed  Too few rest days       |
| [Open] [Declare for] [Return] [Confirm]                                                     |
+---------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F13-10 step 2, U45 | desktop | ![FL-F13-10 step 2, U45, light](../../images/10-special-contracts-and-outsourcing/u45-payroll-officer/2-days-based-contracts-desktop-light.png) | ![FL-F13-10 step 2, U45, dark](../../images/10-special-contracts-and-outsourcing/u45-payroll-officer/2-days-based-contracts-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f13-29-days-based-contracts-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f13-29-days-based-contracts-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f13-29-days-based-contracts-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f13-29-days-based-contracts-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f13-29-days-based-contracts-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f13-29-days-based-contracts-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f13-29-days-based-contracts-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f13-29-days-based-contracts-offline-desktop-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Employee | E-F13-29 employee | name | no | yes |
| Package | E-F13-29 package days | number | yes, at the start of the year | yes |
| Days worked | E-F13-29 days worked | number | no | yes |
| Days left | E-F13-29 days left | number | no | yes |
| Month and days declared | E-F13-29 declarations | month and number | by the employee | yes |
| Rest check | E-F13-29 rest | OK, too few rest days | no | no |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Declare | phone | employee | the days of the month, sent to the manager |
| Confirm | row | manager | the month is confirmed |
| Return | row | manager | the declaration goes back to the employee with a comment |
| Remind | header | payroll officer | a reminder to every employee who has not declared |

## States

- Normal: the packages with days worked, days left and the month's status.
- Empty: No days-based contract, with Add a contract in the HR records.
- Loading: the headings and the table as placeholders; the values follow.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); a refused
  declaration shows the days left and the rule.
- Read-only: the record in a locked state: values shown, no action offered.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-F13-29 Days package](../../data/e-f13-29-days-package.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F13-29 Days package | Open | Badge "Open"; a new record starts here; next: Complete or Closed (BR-F13-26, UC-F13-36); fields editable within the role | U45, U01 | `u45-payroll-officer/s-f13-29-days-based-contracts-e-f13-29-days-package-open-desktop-{light,dark}.png`, `u01-employee/s-f13-29-days-based-contracts-e-f13-29-days-package-open-{desktop,phone}-{light,dark}.png` |
| E-F13-29 Days package | Complete | Badge "Complete"; next: Closed (UC-F13-36); fields editable within the role | U45, U01 | `u45-payroll-officer/s-f13-29-days-based-contracts-e-f13-29-days-package-complete-desktop-{light,dark}.png`, `u01-employee/s-f13-29-days-based-contracts-e-f13-29-days-package-complete-{desktop,phone}-{light,dark}.png` |
| E-F13-29 Days package | Closed | Badge "Closed"; final: read-only, no next state; the history shows how it got here | U45, U01 | `u45-payroll-officer/s-f13-29-days-based-contracts-e-f13-29-days-package-closed-desktop-{light,dark}.png`, `u01-employee/s-f13-29-days-based-contracts-e-f13-29-days-package-closed-{desktop,phone}-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

The payroll officer's table is desktop only. The employee declares and reads their days on a phone: the month, the days
worked, the days left and a confirm button.

## Accessibility

Every control is reachable by keyboard; states and errors are announced to screen readers and never rely on colour
alone; each field has its visible label.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)
- [C-01 Button](../../../../04-ux/design-system/components/c-01-button.md)

## Shown in

- [FL-F13-10](../../flows/fl-f13-10-special-contracts-and-outsourcing.md)

## Open questions

None.

---

⬅️ [S-F13-28 Posted workers](s-f13-28-posted-workers.md) · ⬆️ [Up](README.md) ·
➡️ [S-F13-30 Outsourced payroll](s-f13-30-outsourced-payroll.md)
