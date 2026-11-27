🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
💶 [F13 Payroll (plugin)](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F13-02 Monthly pay run](README.md) › 🖥️ S-F13-08 Payslips

# 🖥️ S-F13-08 Payslips

**Status:** ✅ specified

## Personas

- [U45 Payroll officer](../../../../01-users/personas/u45-payroll-officer.md)
- [U01 Employee](../../../../01-users/personas/u01-employee.md)

## Purpose

Issue clarified payslips digitally.

## Entry points

Payroll in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F13-02 step 6, U45 | desktop | ![FL-F13-02 step 6, U45, light](../../images/02-monthly-pay-run/u45-payroll-officer/6-payslip-desktop-light.png) | ![FL-F13-02 step 6, U45, dark](../../images/02-monthly-pay-run/u45-payroll-officer/6-payslip-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f13-08-payslips-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f13-08-payslips-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f13-08-payslips-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f13-08-payslips-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f13-08-payslips-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f13-08-payslips-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f13-08-payslips-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f13-08-payslips-offline-desktop-dark.png) |

## Fields and columns

As its entities.

## Actions

As its use case's main flow.

## States

- Normal: the payslips of the run with their delivery state; for the employee, their own payslips by month.
- Empty: "No payslip yet": for a new employee before their first pay day.
- Loading: the frame and titles show at once with placeholder rows for the payslips; within 1 second (D408) the data
  replaces them, and a longer load shows a progress line saying what loads.
- Error: the error message pattern (D122).
- Read-only: payslips are never edited once issued; the employee reads only their own.
- Offline: A payslip already opened stays readable on the phone; new payslips need the network. Nothing else is queued:
  D38 keeps only today's schedule, time and intervention records offline; a banner says the connection is lost and the
  actions come back with it.

Shown entities (VD-15): [E-F13-07 Payslip](../../data/e-f13-07-payslip.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F13-07 Payslip | Published | Badge "Published"; a new record starts here; next: Available (UC-F13-08); fields editable within the role | U01, U45 | `u01-employee/s-f13-08-payslips-e-f13-07-payslip-published-{desktop,phone}-{light,dark}.png`, `u45-payroll-officer/s-f13-08-payslips-e-f13-07-payslip-published-desktop-{light,dark}.png` |
| E-F13-07 Payslip | Available | Badge "Available"; final: read-only, no next state; the history shows how it got here | U01, U45 | `u01-employee/s-f13-08-payslips-e-f13-07-payslip-available-{desktop,phone}-{light,dark}.png`, `u45-payroll-officer/s-f13-08-payslips-e-f13-07-payslip-available-desktop-{light,dark}.png` |

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

⬅️ [S-F13-07 Pay run](s-f13-07-pay-run.md) · ⬆️ [Up](README.md) ·
➡️ [S-F13-09 Pay transfers](../03-declarations-and-payments/s-f13-09-pay-transfers.md)
