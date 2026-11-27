🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
💸 [F22 Unified platform cost management](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F22-02 Budgets and stops](README.md) › 🖥️ S-F22-06 Budgets

# 🖥️ S-F22-06 Budgets

**Status:** ✅ specified

## Personas

- [U13 Owner](../../../../01-users/personas/u13-owner.md)
- [U02 Manager](../../../../01-users/personas/u02-manager.md)

## Purpose

Set budgets at every level.

## Entry points

Unified platform cost management in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F22-02 step 1, U13 | desktop | ![FL-F22-02 step 1, U13, light](../../images/02-budgets-and-stops/u13-owner/1-budgets-desktop-light.png) | ![FL-F22-02 step 1, U13, dark](../../images/02-budgets-and-stops/u13-owner/1-budgets-desktop-dark.png) |
| FL-F22-02 step 1, U13 | phone | ![FL-F22-02 step 1, U13, light](../../images/02-budgets-and-stops/u13-owner/1-budgets-phone-light.png) | ![FL-F22-02 step 1, U13, dark](../../images/02-budgets-and-stops/u13-owner/1-budgets-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f22-06-budgets-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f22-06-budgets-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f22-06-budgets-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f22-06-budgets-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f22-06-budgets-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f22-06-budgets-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f22-06-budgets-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f22-06-budgets-offline-phone-dark.png) |

## Fields and columns

As its entities.

## Actions

As its use case's main flow.

## States

- Normal: budgets per level with thresholds.
- Empty: "No budget": nothing stops.
- Loading: the frame and titles show at once with placeholder rows for the budgets; within 1 second (D408) the data
  replaces them, and a longer load shows a progress line saying what loads.
- Error: the error message pattern (D122).
- Read-only: accounting reads; managers their team.
- Offline: not available offline: set online. D38 keeps only today's schedule, time and intervention records offline. A
  banner says the connection is lost; what is on screen stays visible, every action is disabled and nothing is queued
  until the connection is back.

Shown entities (VD-15): [E-F22-06 Cost budget](../../data/e-f22-06-cost-budget.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F22-06 Cost budget | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U02, U13 | `u02-manager/s-f22-06-budgets-e-f22-06-cost-budget-active-{desktop,phone}-{light,dark}.png`, `u13-owner/s-f22-06-budgets-e-f22-06-cost-budget-active-{desktop,phone}-{light,dark}.png` |

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

- [FL-F22-02 Budgets and stops](../../flows/fl-f22-02-budgets-and-stops.md)

## Open questions

None.

---

⬅️ [S-F22-05 Payment mode](../01-see-and-set-up/s-f22-05-payment-mode.md) · ⬆️ [Up](README.md) ·
➡️ [S-F22-07 Budget warnings](s-f22-07-budget-warnings.md)
