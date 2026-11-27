🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
💶 [F13 Payroll (plugin)](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F13-02 Monthly pay run](README.md) › 🖥️ S-F13-03 Pay inputs

# 🖥️ S-F13-03 Pay inputs

**Status:** ✅ specified

## Personas

- [U45 Payroll officer](../../../../01-users/personas/u45-payroll-officer.md)
- [U06 HR](../../../../01-users/personas/u06-hr.md)

## Purpose

Collect pay inputs from F9.

## Entry points

Payroll in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F13-02 step 1, U45 | desktop | ![FL-F13-02 step 1, U45, light](../../images/02-monthly-pay-run/u45-payroll-officer/1-inputs-desktop-light.png) | ![FL-F13-02 step 1, U45, dark](../../images/02-monthly-pay-run/u45-payroll-officer/1-inputs-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f13-03-pay-inputs-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f13-03-pay-inputs-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f13-03-pay-inputs-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f13-03-pay-inputs-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f13-03-pay-inputs-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f13-03-pay-inputs-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f13-03-pay-inputs-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f13-03-pay-inputs-offline-desktop-dark.png) |

## Fields and columns

As its entities.

## Actions

As its use case's main flow.

## States

- Normal: the inputs of the period per employee (time, overtime, leave, absences, expenses) with their closing state.
- Empty: "No inputs for this period yet": shown before F9 sends any; the closing date is shown.
- Loading: the frame and titles show at once with placeholder rows for the inputs of the period; within 1 second (D408)
  the data replaces them, and a longer load shows a progress line saying what loads.
- Error: the error message pattern (D122).
- Read-only: once the inputs are closed (BR-F13-03), late inputs go to the next period and the list is read-only.
- Offline: not available offline: inputs are collected in the office from F9. D38 keeps only today's schedule, time and
  intervention records offline. A banner says the connection is lost; what is on screen stays visible, every action is
  disabled and nothing is queued until the connection is back.

Shown entities (VD-15): [E-F13-03 Pay input](../../data/e-f13-03-pay-input.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F13-03 Pay input | Open | Badge "Open"; a new record starts here; next: Complete or Late (UC-F13-03); fields editable within the role | U06, U45 | `u06-hr/s-f13-03-pay-inputs-e-f13-03-pay-input-open-desktop-{light,dark}.png`, `u45-payroll-officer/s-f13-03-pay-inputs-e-f13-03-pay-input-open-desktop-{light,dark}.png` |
| E-F13-03 Pay input | Complete | Badge "Complete"; next: Closed (UC-F13-03); fields editable within the role | U06, U45 | `u06-hr/s-f13-03-pay-inputs-e-f13-03-pay-input-complete-desktop-{light,dark}.png`, `u45-payroll-officer/s-f13-03-pay-inputs-e-f13-03-pay-input-complete-desktop-{light,dark}.png` |
| E-F13-03 Pay input | Late | Badge "Late"; next: Complete (UC-F13-03); fields editable within the role | U06, U45 | `u06-hr/s-f13-03-pay-inputs-e-f13-03-pay-input-late-desktop-{light,dark}.png`, `u45-payroll-officer/s-f13-03-pay-inputs-e-f13-03-pay-input-late-desktop-{light,dark}.png` |
| E-F13-03 Pay input | Closed | Badge "Closed"; final: read-only, no next state; the history shows how it got here | U06, U45 | `u06-hr/s-f13-03-pay-inputs-e-f13-03-pay-input-closed-desktop-{light,dark}.png`, `u45-payroll-officer/s-f13-03-pay-inputs-e-f13-03-pay-input-closed-desktop-{light,dark}.png` |

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

- [FL-F13-02 Monthly pay run](../../flows/fl-f13-02-monthly-pay-run.md)

## Open questions

None.

---

⬅️ [S-F13-02 Employee pay](../01-set-up/s-f13-02-employee-pay.md) · ⬆️ [Up](README.md) ·
➡️ [S-F13-04 Pay computation](s-f13-04-pay-computation.md)
