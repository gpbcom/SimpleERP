🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
💶 [F13 Payroll (plugin)](../../README.md) › 🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-F13-04 Events](README.md) ›
🖥️ S-F13-14 Sick leave

# 🖥️ S-F13-14 Sick leave

**Status:** ✅ specified

## Personas

- [U45 Payroll officer](../../../../01-users/personas/u45-payroll-officer.md)
- [U06 HR](../../../../01-users/personas/u06-hr.md)

## Purpose

Handle sick leave and daily allowances.

## Entry points

Payroll in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F13-04 step 1, U45 | desktop | ![FL-F13-04 step 1, U45, light](../../images/04-events/u45-payroll-officer/1-sick-leave-desktop-light.png) | ![FL-F13-04 step 1, U45, dark](../../images/04-events/u45-payroll-officer/1-sick-leave-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f13-14-sick-leave-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f13-14-sick-leave-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f13-14-sick-leave-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f13-14-sick-leave-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f13-14-sick-leave-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f13-14-sick-leave-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f13-14-sick-leave-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f13-14-sick-leave-offline-desktop-dark.png) |

## Fields and columns

As its entities.

## Actions

As its use case's main flow.

## States

- Normal: sick leaves of the period with their allowances, top-ups and event declarations.
- Empty: "No sick leave this period".
- Loading: the frame and titles show at once with placeholder rows for the sick leaves; within 1 second (D408) the data
  replaces them, and a longer load shows a progress line saying what loads.
- Error: the error message pattern (D122).
- Read-only: HR reads; declared events are read-only.
- Offline: not available offline: declarations need the connector. D38 keeps only today's schedule, time and
  intervention records offline. A banner says the connection is lost; what is on screen stays visible, every action is
  disabled and nothing is queued until the connection is back.

Shown entities (VD-15): [E-F13-13 Sick leave](../../data/e-f13-13-sick-leave.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F13-13 Sick leave | New | Badge "New"; a new record starts here; next: Paid (UC-F13-14); fields editable within the role | U06, U45 | `u06-hr/s-f13-14-sick-leave-e-f13-13-sick-leave-new-desktop-{light,dark}.png`, `u45-payroll-officer/s-f13-14-sick-leave-e-f13-13-sick-leave-new-desktop-{light,dark}.png` |
| E-F13-13 Sick leave | Paid | Badge "Paid"; final: read-only, no next state; the history shows how it got here | U06, U45 | `u06-hr/s-f13-14-sick-leave-e-f13-13-sick-leave-paid-desktop-{light,dark}.png`, `u45-payroll-officer/s-f13-14-sick-leave-e-f13-13-sick-leave-paid-desktop-{light,dark}.png` |

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

- [FL-F13-04 Events](../../flows/fl-f13-04-events.md)

## Open questions

None.

---

⬅️ [S-F13-13 Payroll entries](../03-declarations-and-payments/s-f13-13-payroll-entries.md) · ⬆️ [Up](README.md) ·
➡️ [S-F13-15 End of contract](s-f13-15-end-of-contract.md)
