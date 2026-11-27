🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
💶 [F13 Payroll (plugin)](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F13-10 Special contracts and outsourced payroll](README.md) › 🖥️ S-F13-31 Staff representatives

# 🖥️ S-F13-31 Staff representatives

**Status:** 🔄 waiting for the owner

## Personas

- [U06 Human resources](../../../../01-users/personas/u06-hr.md): every mandate, credit and hour.
- [U45 Payroll officer](../../../../01-users/personas/u45-payroll-officer.md): the confirmed hours of the month.

## Purpose

Follow each mandate's credit and the hours used, and confirm hours for payroll.

## Entry points

Payroll (plugin) › Staff representatives; HR › Company records.

## Wireframe

```text
+---------------------------------------------------------------------------------------------+
| Staff representatives: November 2026               Hours to confirm 3   Over credit 1   [Export] |
|---------------------------------------------------------------------------------------------|
| PERSON      MANDATE            CREDIT  USED  LEFT  CARRY  STATUS                            |
| Nadia B.    Staff committee    20      14    6     0      Confirmed                         |
| Paul R.     Union delegate     12      13    -1    0      Held for review                   |
| [Confirm] [Hold] [Share credit] [Open]                                                      |
+---------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F13-10 step 4, U06 | desktop | ![FL-F13-10 step 4, U06, light](../../images/10-special-contracts-and-outsourcing/u06-hr/4-staff-representatives-desktop-light.png) | ![FL-F13-10 step 4, U06, dark](../../images/10-special-contracts-and-outsourcing/u06-hr/4-staff-representatives-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f13-31-staff-representatives-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f13-31-staff-representatives-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f13-31-staff-representatives-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f13-31-staff-representatives-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f13-31-staff-representatives-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f13-31-staff-representatives-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f13-31-staff-representatives-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f13-31-staff-representatives-offline-desktop-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Person and mandate | E-F13-31 person, mandate | text | no | yes |
| Credit | E-F13-31 monthly credit | hours | yes, by HR | yes |
| Hours used | E-F13-31 hours | hours and date | by the representative | yes |
| Hours left | E-F13-31 left | hours | no | yes |
| Carry-over | E-F13-31 carry-over | hours | by HR | no |
| Status | E-F13-31 state | badge | by HR | yes |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Record hours | row | representative, HR | adds hours against the credit |
| Confirm | row | HR | the hours go to the pay input as work time |
| Hold | row | HR | the hours wait for a reason |
| Share credit | row | HR | moves hours between two mandates |

## States

- Normal: the mandates with their credit, hours used and hours left.
- Empty: No mandate recorded, with Add a mandate in the company records.
- Loading: the headings and the table as placeholders; the values follow.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); a refused hour
  shows the rule and the mandate's dates.
- Read-only: the record in a locked state: values shown, no action offered.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-F13-31 Delegation hours](../../data/e-f13-31-delegation-hours.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F13-31 Delegation hours | Recorded | Badge "Recorded"; a new record starts here; next: Confirmed or Held (UC-F13-38); fields editable within the role | U06, U45 | `u06-hr/s-f13-31-staff-representatives-e-f13-31-delegation-hours-recorded-desktop-{light,dark}.png`, `u45-payroll-officer/s-f13-31-staff-representatives-e-f13-31-delegation-hours-recorded-desktop-{light,dark}.png` |
| E-F13-31 Delegation hours | Confirmed | Badge "Confirmed"; next: Paid (BR-F13-28); fields editable within the role | U06, U45 | `u06-hr/s-f13-31-staff-representatives-e-f13-31-delegation-hours-confirmed-desktop-{light,dark}.png`, `u45-payroll-officer/s-f13-31-staff-representatives-e-f13-31-delegation-hours-confirmed-desktop-{light,dark}.png` |
| E-F13-31 Delegation hours | Held | Badge "Held"; next: Confirmed or Refused (UC-F13-38); fields editable within the role | U06, U45 | `u06-hr/s-f13-31-staff-representatives-e-f13-31-delegation-hours-held-desktop-{light,dark}.png`, `u45-payroll-officer/s-f13-31-staff-representatives-e-f13-31-delegation-hours-held-desktop-{light,dark}.png` |
| E-F13-31 Delegation hours | Refused | Badge "Refused"; final: read-only, no next state; the history shows how it got here | U06, U45 | `u06-hr/s-f13-31-staff-representatives-e-f13-31-delegation-hours-refused-desktop-{light,dark}.png`, `u45-payroll-officer/s-f13-31-staff-representatives-e-f13-31-delegation-hours-refused-desktop-{light,dark}.png` |
| E-F13-31 Delegation hours | Paid | Badge "Paid"; final: read-only, no next state; the history shows how it got here | U06, U45 | `u06-hr/s-f13-31-staff-representatives-e-f13-31-delegation-hours-paid-desktop-{light,dark}.png`, `u45-payroll-officer/s-f13-31-staff-representatives-e-f13-31-delegation-hours-paid-desktop-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

HR's table is desktop only. The representative records and reads their hours on a phone.

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

⬅️ [S-F13-30 Outsourced payroll](s-f13-30-outsourced-payroll.md) · ⬆️ [Up](README.md) ·
➡️ [S-F13-L01 Payroll establishments](../00-lists/s-f13-l01-payroll-establishments.md)
