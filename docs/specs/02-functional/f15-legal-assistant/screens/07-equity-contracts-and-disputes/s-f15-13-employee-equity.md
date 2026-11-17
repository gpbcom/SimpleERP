🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
⚖️ [F15 Legal assistant](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F15-07 Equity, contracts, meetings and disputes](README.md) › 🖥️ S-F15-13 Employee equity

# 🖥️ S-F15-13 Employee equity

**Status:** 🔄 waiting for the owner

## Personas

- [U13 Owner](../../../../01-users/personas/u13-owner.md): the plans and every grant.
- [U01 Employee](../../../../01-users/personas/u01-employee.md): their own grants and vesting, from a phone.

## Purpose

Grant equity under an approved plan, follow its vesting and prepare the exercise.

## Entry points

Administration › Company records › Employee equity; the employee's self-service.

## Wireframe

```text
+---------------------------------------------------------------------------------------------+
| Employee equity: 2026 plan (approved 2026-05-20)         Pool 10,000   Granted 6,000   Left 4,000 |
|---------------------------------------------------------------------------------------------|
| BENEFICIARY  INSTRUMENT  QUANTITY  STRIKE   GRANTED     CLIFF       VESTED  STATE           |
| Lea M.       BSPCE       2,000     3.00 EUR 2026-11-14  2027-11-14   0       Granted         |
| Karim D.     Free share  500       -        2026-02-01  2027-02-01   0       Vesting         |
| [New grant] [Vesting calendar] [Exercise]                                                   |
+---------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F15-07 step 2, U13 | desktop | ![FL-F15-07 step 2, U13, light](../../images/07-equity-contracts-and-disputes/u13-owner/2-employee-equity-desktop-light.png) | ![FL-F15-07 step 2, U13, dark](../../images/07-equity-contracts-and-disputes/u13-owner/2-employee-equity-desktop-dark.png) |
| FL-F15-07 step 2, U13 | phone | ![FL-F15-07 step 2, U13, light](../../images/07-equity-contracts-and-disputes/u13-owner/2-employee-equity-phone-light.png) | ![FL-F15-07 step 2, U13, dark](../../images/07-equity-contracts-and-disputes/u13-owner/2-employee-equity-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f15-13-employee-equity-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f15-13-employee-equity-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f15-13-employee-equity-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f15-13-employee-equity-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f15-13-employee-equity-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f15-13-employee-equity-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f15-13-employee-equity-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f15-13-employee-equity-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Beneficiary | E-F15-16 beneficiary | name | no | yes |
| Plan and instrument | E-F15-16 plan, instrument | text | while Proposed | yes |
| Quantity and strike | E-F15-16 quantity, strike price | number and amount | while Proposed | yes |
| Grant date and vesting | E-F15-16 dates | dates | while Proposed | yes |
| Vested and exercised | E-F15-16 vested, exercised | numbers | no | no |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| New grant | header | owner | a grant is proposed against the plan |
| Vesting calendar | grant | owner, employee | the dates and quantities of each step |
| Exercise | row | owner, employee | prepares the register movement and the payroll entry |
| Cancel | row | owner | cancels a grant that has not vested |

## States

- Normal: the plans with their pool and the grants with their vesting.
- Empty: No plan approved yet, with Record the shareholders' approval.
- Loading: the headings and the table as placeholders; the values follow.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); a refused grant
  shows the pool left or the plan's end date.
- Read-only: the record in a locked state: values shown, no action offered.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-F15-16 Equity grant](../../data/e-f15-16-equity-grant.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F15-16 Equity grant | Proposed | Badge "Proposed"; a new record starts here; next: Granted or Cancelled (BR-F15-19, UC-F15-15); fields editable within the role | U13, U01 | `u13-owner/s-f15-13-employee-equity-e-f15-16-equity-grant-proposed-{desktop,phone}-{light,dark}.png`, `u01-employee/s-f15-13-employee-equity-e-f15-16-equity-grant-proposed-{desktop,phone}-{light,dark}.png` |
| E-F15-16 Equity grant | Granted | Badge "Granted"; next: Vesting or Lapsed (UC-F15-15); fields editable within the role | U13, U01 | `u13-owner/s-f15-13-employee-equity-e-f15-16-equity-grant-granted-{desktop,phone}-{light,dark}.png`, `u01-employee/s-f15-13-employee-equity-e-f15-16-equity-grant-granted-{desktop,phone}-{light,dark}.png` |
| E-F15-16 Equity grant | Vesting | Badge "Vesting"; next: Vested or Lapsed (UC-F15-15); fields editable within the role | U13, U01 | `u13-owner/s-f15-13-employee-equity-e-f15-16-equity-grant-vesting-{desktop,phone}-{light,dark}.png`, `u01-employee/s-f15-13-employee-equity-e-f15-16-equity-grant-vesting-{desktop,phone}-{light,dark}.png` |
| E-F15-16 Equity grant | Vested | Badge "Vested"; next: Exercised (UC-F15-15); fields editable within the role | U13, U01 | `u13-owner/s-f15-13-employee-equity-e-f15-16-equity-grant-vested-{desktop,phone}-{light,dark}.png`, `u01-employee/s-f15-13-employee-equity-e-f15-16-equity-grant-vested-{desktop,phone}-{light,dark}.png` |
| E-F15-16 Equity grant | Exercised | Badge "Exercised"; final: read-only, no next state; the history shows how it got here | U13, U01 | `u13-owner/s-f15-13-employee-equity-e-f15-16-equity-grant-exercised-{desktop,phone}-{light,dark}.png`, `u01-employee/s-f15-13-employee-equity-e-f15-16-equity-grant-exercised-{desktop,phone}-{light,dark}.png` |
| E-F15-16 Equity grant | Lapsed | Badge "Lapsed"; final: read-only, no next state; the history shows how it got here | U13, U01 | `u13-owner/s-f15-13-employee-equity-e-f15-16-equity-grant-lapsed-{desktop,phone}-{light,dark}.png`, `u01-employee/s-f15-13-employee-equity-e-f15-16-equity-grant-lapsed-{desktop,phone}-{light,dark}.png` |
| E-F15-16 Equity grant | Cancelled | Badge "Cancelled"; final: read-only, no next state; the history shows how it got here | U13, U01 | `u13-owner/s-f15-13-employee-equity-e-f15-16-equity-grant-cancelled-{desktop,phone}-{light,dark}.png`, `u01-employee/s-f15-13-employee-equity-e-f15-16-equity-grant-cancelled-{desktop,phone}-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

The owner's table is desktop only. The employee reads their grants, the vesting calendar and what they can exercise on a
phone.

## Accessibility

Every control is reachable by keyboard; states and errors are announced to screen readers and never rely on colour
alone; each field has its visible label.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)
- [C-01 Button](../../../../04-ux/design-system/components/c-01-button.md)

## Shown in

- [FL-F15-07](../../flows/fl-f15-07-equity-contracts-and-disputes.md)

## Open questions

None.

---

⬅️ [S-F15-12 Cap table](s-f15-12-cap-table.md) · ⬆️ [Up](README.md) · ➡️ [S-F15-14 Dilution](s-f15-14-dilution.md)
