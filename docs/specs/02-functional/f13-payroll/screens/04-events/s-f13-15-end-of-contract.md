🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
💶 [F13 Payroll (plugin)](../../README.md) › 🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-F13-04 Events](README.md) ›
🖥️ S-F13-15 End of contract

# 🖥️ S-F13-15 End of contract

**Status:** ✅ specified

## Personas

- [U45 Payroll officer](../../../../01-users/personas/u45-payroll-officer.md)
- [U06 HR](../../../../01-users/personas/u06-hr.md)

## Purpose

End a contract.

## Entry points

Payroll in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F13-04 step 2, U45 | desktop | ![FL-F13-04 step 2, U45, light](../../images/04-events/u45-payroll-officer/2-end-of-contract-desktop-light.png) | ![FL-F13-04 step 2, U45, dark](../../images/04-events/u45-payroll-officer/2-end-of-contract-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f13-15-end-of-contract-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f13-15-end-of-contract-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f13-15-end-of-contract-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f13-15-end-of-contract-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f13-15-end-of-contract-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f13-15-end-of-contract-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f13-15-end-of-contract-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f13-15-end-of-contract-offline-desktop-dark.png) |

## Fields and columns

As its entities.

## Actions

As its use case's main flow.

## States

- Normal: the leaver's final pay and documents with their readiness for the last day.
- Empty: "No contract ending": shown when no end of contract is planned.
- Loading: the frame and titles show at once with placeholder rows for the end-of-contract file; within 1 second (D408)
  the data replaces them, and a longer load shows a progress line saying what loads.
- Error: the error message pattern (D122).
- Read-only: HR reads; documents once given are read-only.
- Offline: not available offline: documents are produced on the server. D38 keeps only today's schedule, time and
  intervention records offline. A banner says the connection is lost; what is on screen stays visible, every action is
  disabled and nothing is queued until the connection is back.

Shown entities (VD-15): [E-F13-14 End-of-contract file](../../data/e-f13-14-end-of-contract-file.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F13-14 End-of-contract file | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U06, U45 | `u06-hr/s-f13-15-end-of-contract-e-f13-14-end-of-contract-file-active-desktop-{light,dark}.png`, `u45-payroll-officer/s-f13-15-end-of-contract-e-f13-14-end-of-contract-file-active-desktop-{light,dark}.png` |

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

⬅️ [S-F13-14 Sick leave](s-f13-14-sick-leave.md) · ⬆️ [Up](README.md) ·
➡️ [S-F13-16 Simulations](s-f13-16-simulations.md)
