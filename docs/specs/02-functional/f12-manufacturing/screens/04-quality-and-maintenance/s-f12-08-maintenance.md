🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🏭 [F12 Manufacturing (plugin)](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F12-04 Quality and maintenance](README.md) › 🖥️ S-F12-08 Maintenance

# 🖥️ S-F12-08 Maintenance

**Status:** ✅ specified

## Personas

- [U21 Production planner](../../../../01-users/personas/u21-production-planner.md)
- [U20 Production operator](../../../../01-users/personas/u20-production-operator.md)

## Purpose

Maintain equipment.

## Entry points

Manufacturing in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F12-04 step 2, U21 | desktop | ![FL-F12-04 step 2, U21, light](../../images/04-quality-and-maintenance/u21-production-planner/2-maintenance-desktop-light.png) | ![FL-F12-04 step 2, U21, dark](../../images/04-quality-and-maintenance/u21-production-planner/2-maintenance-desktop-dark.png) |
| FL-F12-04 step 2, U21 | phone | ![FL-F12-04 step 2, U21, light](../../images/04-quality-and-maintenance/u21-production-planner/2-maintenance-phone-light.png) | ![FL-F12-04 step 2, U21, dark](../../images/04-quality-and-maintenance/u21-production-planner/2-maintenance-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f12-08-maintenance-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f12-08-maintenance-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f12-08-maintenance-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f12-08-maintenance-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f12-08-maintenance-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f12-08-maintenance-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f12-08-maintenance-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f12-08-maintenance-offline-phone-dark.png) |

## Fields and columns

As its entities.

## Actions

As its use case's main flow.

## States

- Normal: Maintain equipment, as the wireframe shows.
- Empty: No maintenance request yet, with New request.
- Loading: skeleton rows in place of the list ([C-03](../../../../04-ux/design-system/components/c-03-data-table.md));
  actions are disabled until it has loaded.
- Error: the error message pattern (D122).
- Read-only: done manufacturing orders and recorded checks, corrected by a new record.
- Offline: Not available offline: a back-office screen on live, shared data (D38: only today's schedule, time and
  intervention records work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-F12-10 Maintenance request](../../data/e-f12-10-maintenance-request.md),
[E-F12-09 Equipment](../../data/e-f12-09-equipment.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F12-10 Maintenance request | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U20, U21 | `u20-production-operator/s-f12-08-maintenance-e-f12-10-maintenance-request-active-tablet-{light,dark}.png`, `u21-production-planner/s-f12-08-maintenance-e-f12-10-maintenance-request-active-{desktop,phone}-{light,dark}.png` |
| E-F12-09 Equipment | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U20, U21 | `u20-production-operator/s-f12-08-maintenance-e-f12-09-equipment-active-tablet-{light,dark}.png`, `u21-production-planner/s-f12-08-maintenance-e-f12-09-equipment-active-{desktop,phone}-{light,dark}.png` |

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

## Shown in

- [FL-F12-04 Quality and maintenance](../../flows/fl-f12-04-quality-and-maintenance.md)

## Open questions

None.

---

⬅️ [S-F12-07 Quality checks](s-f12-07-quality-checks.md) · ⬆️ [Up](README.md) ·
➡️ [S-F12-09 Subcontracting](../05-subcontracting-and-costs/s-f12-09-subcontracting.md)
