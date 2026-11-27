🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🏭 [F12 Manufacturing (plugin)](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F12-02 Plan production](README.md) › 🖥️ S-F12-03 Master plan

# 🖥️ S-F12-03 Master plan

**Status:** ✅ specified

## Personas

- [U21 Production planner](../../../../01-users/personas/u21-production-planner.md)
- [U04 Purchasing](../../../../01-users/personas/u04-purchasing.md)

## Purpose

Plan production.

## Entry points

Manufacturing in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F12-02 step 1, U21 | desktop | ![FL-F12-02 step 1, U21, light](../../images/02-plan-production/u21-production-planner/1-master-plan-desktop-light.png) | ![FL-F12-02 step 1, U21, dark](../../images/02-plan-production/u21-production-planner/1-master-plan-desktop-dark.png) |
| FL-F12-02 step 1, U21 | phone | ![FL-F12-02 step 1, U21, light](../../images/02-plan-production/u21-production-planner/1-master-plan-phone-light.png) | ![FL-F12-02 step 1, U21, dark](../../images/02-plan-production/u21-production-planner/1-master-plan-phone-dark.png) |
| Error E1, U21 | desktop | ![Error E1, U21, light](../../images/02-plan-production/u21-production-planner/e1-overload-desktop-light.png) | ![Error E1, U21, dark](../../images/02-plan-production/u21-production-planner/e1-overload-desktop-dark.png) |
| Error E1, U21 | phone | ![Error E1, U21, light](../../images/02-plan-production/u21-production-planner/e1-overload-phone-light.png) | ![Error E1, U21, dark](../../images/02-plan-production/u21-production-planner/e1-overload-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f12-03-master-plan-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f12-03-master-plan-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f12-03-master-plan-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f12-03-master-plan-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f12-03-master-plan-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f12-03-master-plan-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f12-03-master-plan-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f12-03-master-plan-offline-phone-dark.png) |

## Fields and columns

As its entities.

## Actions

As its use case's main flow.

## States

- Normal: Plan production, as the wireframe shows.
- Empty: No demand to plan yet, with Nothing to plan.
- Loading: skeleton rows in place of the list ([C-03](../../../../04-ux/design-system/components/c-03-data-table.md));
  actions are disabled until it has loaded.
- Error: the error message pattern (D122).
- Read-only: done manufacturing orders and recorded checks, corrected by a new record.
- Offline: Not available offline: a back-office screen on live, shared data (D38: only today's schedule, time and
  intervention records work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-F7-21 Demand forecast](../../../f07-purchasing-and-stock/data/e-f07-21-demand-forecast.md),
[E-F12-12 Master plan line](../../data/e-f12-12-master-plan-line.md),
[E-F12-04 Manufacturing order](../../data/e-f12-04-manufacturing-order.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F7-21 Demand forecast | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U04, U21 | `u04-purchasing/s-f12-03-master-plan-e-f07-21-demand-forecast-active-desktop-{light,dark}.png`, `u21-production-planner/s-f12-03-master-plan-e-f07-21-demand-forecast-active-{desktop,phone}-{light,dark}.png` |
| E-F12-12 Master plan line | Recorded | Badge "Recorded"; a new record starts here; no other state; fields editable within the role | U04, U21 | `u04-purchasing/s-f12-03-master-plan-e-f12-12-master-plan-line-recorded-desktop-{light,dark}.png`, `u21-production-planner/s-f12-03-master-plan-e-f12-12-master-plan-line-recorded-{desktop,phone}-{light,dark}.png` |
| E-F12-04 Manufacturing order | Draft | Badge "Draft"; a new record starts here; next: Confirmed or Cancelled (UC-F12-04, BR-F12-02); fields editable within the role | U04, U21 | `u04-purchasing/s-f12-03-master-plan-e-f12-04-manufacturing-order-draft-desktop-{light,dark}.png`, `u21-production-planner/s-f12-03-master-plan-e-f12-04-manufacturing-order-draft-{desktop,phone}-{light,dark}.png` |
| E-F12-04 Manufacturing order | Confirmed | Badge "Confirmed"; next: In progress or Cancelled (UC-F12-27, BR-F12-02); fields editable within the role | U04, U21 | `u04-purchasing/s-f12-03-master-plan-e-f12-04-manufacturing-order-confirmed-desktop-{light,dark}.png`, `u21-production-planner/s-f12-03-master-plan-e-f12-04-manufacturing-order-confirmed-{desktop,phone}-{light,dark}.png` |
| E-F12-04 Manufacturing order | Cancelled | Badge "Cancelled"; final: read-only, no next state; the history shows how it got here | U04, U21 | `u04-purchasing/s-f12-03-master-plan-e-f12-04-manufacturing-order-cancelled-desktop-{light,dark}.png`, `u21-production-planner/s-f12-03-master-plan-e-f12-04-manufacturing-order-cancelled-{desktop,phone}-{light,dark}.png` |
| E-F12-04 Manufacturing order | In progress | Badge "In progress"; next: Done or Cancelled (UC-F12-04, BR-F12-02); fields editable within the role | U04, U21 | `u04-purchasing/s-f12-03-master-plan-e-f12-04-manufacturing-order-in-progress-desktop-{light,dark}.png`, `u21-production-planner/s-f12-03-master-plan-e-f12-04-manufacturing-order-in-progress-{desktop,phone}-{light,dark}.png` |
| E-F12-04 Manufacturing order | Done | Badge "Done"; final: read-only, no next state; the history shows how it got here | U04, U21 | `u04-purchasing/s-f12-03-master-plan-e-f12-04-manufacturing-order-done-desktop-{light,dark}.png`, `u21-production-planner/s-f12-03-master-plan-e-f12-04-manufacturing-order-done-{desktop,phone}-{light,dark}.png` |

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

- [FL-F12-02 Plan production](../../flows/fl-f12-02-plan-production.md)

## Open questions

None.

---

⬅️ [S-F12-02 Routing](../01-define-the-products/s-f12-02-routing.md) · ⬆️ [Up](README.md) ·
➡️ [S-F12-04 Manufacturing order](../03-make-the-products/s-f12-04-manufacturing-order.md)
