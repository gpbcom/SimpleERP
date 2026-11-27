🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
💶 [F13 Payroll (plugin)](../../README.md) › 🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-F13-01 Set up](README.md) ›
🖥️ S-F13-02 Employee pay

# 🖥️ S-F13-02 Employee pay

**Status:** ✅ specified

## Personas

- [U45 Payroll officer](../../../../01-users/personas/u45-payroll-officer.md)
- [U06 HR](../../../../01-users/personas/u06-hr.md)

## Purpose

Set up employees' pay.

## Entry points

Payroll in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F13-01 step 2, U45 | desktop | ![FL-F13-01 step 2, U45, light](../../images/01-set-up/u45-payroll-officer/2-employee-desktop-light.png) | ![FL-F13-01 step 2, U45, dark](../../images/01-set-up/u45-payroll-officer/2-employee-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f13-02-employee-pay-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f13-02-employee-pay-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f13-02-employee-pay-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f13-02-employee-pay-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f13-02-employee-pay-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f13-02-employee-pay-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f13-02-employee-pay-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f13-02-employee-pay-offline-desktop-dark.png) |

## Fields and columns

As its entities.

## Actions

As its use case's main flow.

## States

- Normal: the employee's contract from F9, salary, classification and pay elements.
- Empty: "No pay elements yet": shown for a new employee, with the contract's salary pre-filled.
- Loading: the frame and titles show at once with placeholder rows for the employee's pay profile; within 1 second
  (D408) the data replaces them, and a longer load shows a progress line saying what loads.
- Error: the error message pattern (D122).
- Read-only: HR reads the pay profile and changes contracts in F9 only; the employee reads their own profile.
- Offline: not available offline: set-up is office work on a desktop. D38 keeps only today's schedule, time and
  intervention records offline. A banner says the connection is lost; what is on screen stays visible, every action is
  disabled and nothing is queued until the connection is back.

Shown entities (VD-15): [E-F13-02 Employee pay profile](../../data/e-f13-02-employee-pay-profile.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F13-02 Employee pay profile | Checked | Badge "Checked"; a new record starts here; next: Complete (UC-F13-02); fields editable within the role | U06, U45 | `u06-hr/s-f13-02-employee-pay-e-f13-02-employee-pay-profile-checked-desktop-{light,dark}.png`, `u45-payroll-officer/s-f13-02-employee-pay-e-f13-02-employee-pay-profile-checked-desktop-{light,dark}.png` |
| E-F13-02 Employee pay profile | Complete | Badge "Complete"; final: read-only, no next state; the history shows how it got here | U06, U45 | `u06-hr/s-f13-02-employee-pay-e-f13-02-employee-pay-profile-complete-desktop-{light,dark}.png`, `u45-payroll-officer/s-f13-02-employee-pay-e-f13-02-employee-pay-profile-complete-desktop-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop; approvals and receipts also on the phone.

## Accessibility

Labelled controls; amounts and states as text.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)
- [C-10 Empty state](../../../../04-ux/design-system/components/c-10-empty-state.md)

## Shown in

- [FL-F13-01 Set up](../../flows/fl-f13-01-set-up.md)

## Open questions

None.

---

⬅️ [S-F13-01 Payroll set-up](s-f13-01-payroll-set-up.md) · ⬆️ [Up](README.md) ·
➡️ [S-F13-03 Pay inputs](../02-monthly-pay-run/s-f13-03-pay-inputs.md)
