🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
💶 [F13 Payroll (plugin)](../../README.md) › 🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-F13-04 Events](README.md) ›
🖥️ S-F13-16 Simulations

# 🖥️ S-F13-16 Simulations

**Status:** ✅ specified

## Personas

- [U45 Payroll officer](../../../../01-users/personas/u45-payroll-officer.md)
- [U13 Owner](../../../../01-users/personas/u13-owner.md)

## Purpose

Simulate pay and costs.

## Entry points

Payroll in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F13-04 step 3, U45 | desktop | ![FL-F13-04 step 3, U45, light](../../images/04-events/u45-payroll-officer/3-simulation-desktop-light.png) | ![FL-F13-04 step 3, U45, dark](../../images/04-events/u45-payroll-officer/3-simulation-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f13-16-simulations-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f13-16-simulations-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f13-16-simulations-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f13-16-simulations-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f13-16-simulations-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f13-16-simulations-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f13-16-simulations-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f13-16-simulations-offline-desktop-dark.png) |

## Fields and columns

As its entities.

## Actions

As its use case's main flow.

## States

- Normal: the cases simulated side by side with gross, net and employer cost.
- Empty: "No simulation yet": a form invites to enter a hire or a raise.
- Loading: the frame and titles show at once with placeholder rows for the simulations; within 1 second (D408) the data
  replaces them, and a longer load shows a progress line saying what loads.
- Error: the error message pattern (D122).
- Read-only: the owner reads simulations shared with them; simulations never change pay.
- Offline: The owner's phone shows simulations last loaded; new ones need the network. Nothing else is queued: D38 keeps
  only today's schedule, time and intervention records offline; a banner says the connection is lost and the actions
  come back with it.

Shown entities (VD-15): [E-F13-27 Pay simulation](../../data/e-f13-27-pay-simulation.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F13-27 Pay simulation | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U13, U45 | `u13-owner/s-f13-16-simulations-e-f13-27-pay-simulation-active-{desktop,phone}-{light,dark}.png`, `u45-payroll-officer/s-f13-16-simulations-e-f13-27-pay-simulation-active-desktop-{light,dark}.png` |

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

⬅️ [S-F13-15 End of contract](s-f13-15-end-of-contract.md) · ⬆️ [Up](README.md) ·
➡️ [S-F13-17 Benefits](s-f13-17-benefits.md)
