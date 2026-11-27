🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
💶 [F13 Payroll (plugin)](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F13-02 Monthly pay run](README.md) › 🖥️ S-F13-07 Pay run

# 🖥️ S-F13-07 Pay run

**Status:** ✅ specified

## Personas

- [U45 Payroll officer](../../../../01-users/personas/u45-payroll-officer.md)
- [U13 Owner](../../../../01-users/personas/u13-owner.md)

## Purpose

Check and approve the pay run.

## Entry points

Payroll in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F13-02 step 5, U45 | desktop | ![FL-F13-02 step 5, U45, light](../../images/02-monthly-pay-run/u45-payroll-officer/5-approve-desktop-light.png) | ![FL-F13-02 step 5, U45, dark](../../images/02-monthly-pay-run/u45-payroll-officer/5-approve-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f13-07-pay-run-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f13-07-pay-run-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f13-07-pay-run-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f13-07-pay-run-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f13-07-pay-run-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f13-07-pay-run-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f13-07-pay-run-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f13-07-pay-run-offline-desktop-dark.png) |

## Fields and columns

As its entities.

## Actions

As its use case's main flow.

## States

- Normal: the run's totals, its anomalies to clear or accept, and the approval buttons.
- Empty: "No run for this period yet": shown before the computation, with a link to start it.
- Loading: the frame and titles show at once with placeholder rows for the run and its anomalies; within 1 second (D408)
  the data replaces them, and a longer load shows a progress line saying what loads.
- Error: the error message pattern (D122).
- Read-only: an approved run is read-only for the payroll officer; a paid run is locked (BR-F13-10); the owner approves
  only.
- Offline: The owner's approval on a phone shows the totals last loaded; approving needs the network. Nothing else is
  queued: D38 keeps only today's schedule, time and intervention records offline; a banner says the connection is lost
  and the actions come back with it.

Shown entities (VD-15): [E-F13-06 Pay run](../../data/e-f13-06-pay-run.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F13-06 Pay run | Recorded | Badge "Recorded"; a new record starts here; no other state; fields editable within the role | U13, U45 | `u13-owner/s-f13-07-pay-run-e-f13-06-pay-run-recorded-{desktop,phone}-{light,dark}.png`, `u45-payroll-officer/s-f13-07-pay-run-e-f13-06-pay-run-recorded-desktop-{light,dark}.png` |

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

⬅️ [S-F13-06 Withholding](s-f13-06-withholding.md) · ⬆️ [Up](README.md) · ➡️ [S-F13-08 Payslips](s-f13-08-payslips.md)
