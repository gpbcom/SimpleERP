🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🏭 [F12 Manufacturing (plugin)](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F12-03 Make the products](README.md) › 🖥️ S-F12-11 Unbuild and repair

# 🖥️ S-F12-11 Unbuild and repair

**Status:** ✅ specified

## Personas

- [U21 Production planner](../../../../01-users/personas/u21-production-planner.md)
- [U20 Production operator](../../../../01-users/personas/u20-production-operator.md)

## Purpose

Unbuild, rework and repair.

## Entry points

Manufacturing in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F12-03 step 4, U21 | desktop | ![FL-F12-03 step 4, U21, light](../../images/03-make-the-products/u21-production-planner/4-unbuild-repair-desktop-light.png) | ![FL-F12-03 step 4, U21, dark](../../images/03-make-the-products/u21-production-planner/4-unbuild-repair-desktop-dark.png) |
| FL-F12-03 step 4, U21 | phone | ![FL-F12-03 step 4, U21, light](../../images/03-make-the-products/u21-production-planner/4-unbuild-repair-phone-light.png) | ![FL-F12-03 step 4, U21, dark](../../images/03-make-the-products/u21-production-planner/4-unbuild-repair-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f12-11-unbuild-and-repair-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f12-11-unbuild-and-repair-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f12-11-unbuild-and-repair-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f12-11-unbuild-and-repair-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f12-11-unbuild-and-repair-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f12-11-unbuild-and-repair-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f12-11-unbuild-and-repair-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f12-11-unbuild-and-repair-offline-phone-dark.png) |

## Fields and columns

As its entities.

## Actions

As its use case's main flow.

## States

- Normal: Unbuild, rework and repair, as the wireframe shows.
- Empty: No unbuild or repair order yet, with New order.
- Loading: skeleton rows in place of the list ([C-03](../../../../04-ux/design-system/components/c-03-data-table.md));
  actions are disabled until it has loaded.
- Error: the error message pattern (D122).
- Read-only: done manufacturing orders and recorded checks, corrected by a new record.
- Offline: Not available offline: a back-office screen on live, shared data (D38: only today's schedule, time and
  intervention records work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-F12-04 Manufacturing order](../../data/e-f12-04-manufacturing-order.md),
[E-F12-29 Unbuild order](../../data/e-f12-29-unbuild-order.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F12-04 Manufacturing order | Draft | Badge "Draft"; a new record starts here; next: Confirmed or Cancelled (UC-F12-04, BR-F12-02); fields editable within the role | U20, U21 | `u20-production-operator/s-f12-11-unbuild-and-repair-e-f12-04-manufacturing-order-draft-tablet-{light,dark}.png`, `u21-production-planner/s-f12-11-unbuild-and-repair-e-f12-04-manufacturing-order-draft-{desktop,phone}-{light,dark}.png` |
| E-F12-04 Manufacturing order | Confirmed | Badge "Confirmed"; next: In progress or Cancelled (UC-F12-27, BR-F12-02); fields editable within the role | U20, U21 | `u20-production-operator/s-f12-11-unbuild-and-repair-e-f12-04-manufacturing-order-confirmed-tablet-{light,dark}.png`, `u21-production-planner/s-f12-11-unbuild-and-repair-e-f12-04-manufacturing-order-confirmed-{desktop,phone}-{light,dark}.png` |
| E-F12-04 Manufacturing order | In progress | Badge "In progress"; next: Done or Cancelled (UC-F12-04, BR-F12-02); fields editable within the role | U20, U21 | `u20-production-operator/s-f12-11-unbuild-and-repair-e-f12-04-manufacturing-order-in-progress-tablet-{light,dark}.png`, `u21-production-planner/s-f12-11-unbuild-and-repair-e-f12-04-manufacturing-order-in-progress-{desktop,phone}-{light,dark}.png` |
| E-F12-04 Manufacturing order | Done | Badge "Done"; final: read-only, no next state; the history shows how it got here | U20, U21 | `u20-production-operator/s-f12-11-unbuild-and-repair-e-f12-04-manufacturing-order-done-tablet-{light,dark}.png`, `u21-production-planner/s-f12-11-unbuild-and-repair-e-f12-04-manufacturing-order-done-{desktop,phone}-{light,dark}.png` |
| E-F12-29 Unbuild order | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U20, U21 | `u20-production-operator/s-f12-11-unbuild-and-repair-e-f12-29-unbuild-order-active-tablet-{light,dark}.png`, `u21-production-planner/s-f12-11-unbuild-and-repair-e-f12-29-unbuild-order-active-{desktop,phone}-{light,dark}.png` |

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

- [FL-F12-03 Make the products](../../flows/fl-f12-03-make-the-products.md)

## Open questions

None.

---

⬅️ [S-F12-10 Engineering change](../01-define-the-products/s-f12-10-engineering-change.md) · ⬆️ [Up](README.md) ·
➡️ [S-F12-12 Production cost variance](../05-subcontracting-and-costs/s-f12-12-production-cost-variance.md)
