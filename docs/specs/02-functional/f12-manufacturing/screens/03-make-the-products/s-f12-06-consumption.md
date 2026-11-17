🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🏭 [F12 Manufacturing (plugin)](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F12-03 Make the products](README.md) › 🖥️ S-F12-06 Consumption

# 🖥️ S-F12-06 Consumption

**Status:** ✅ specified

## Personas

- [U20 Production operator](../../../../01-users/personas/u20-production-operator.md)
- [U15 Warehouse operator](../../../../01-users/personas/u15-warehouse-operator.md)

## Purpose

Consume components, trace lots and serials.

## Entry points

Manufacturing in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F12-03 step 3, U20 | tablet | ![FL-F12-03 step 3, U20, light](../../images/03-make-the-products/u20-production-operator/3-consume-and-trace-tablet-light.png) | ![FL-F12-03 step 3, U20, dark](../../images/03-make-the-products/u20-production-operator/3-consume-and-trace-tablet-dark.png) |
| Empty | tablet | ![Empty, light](../../images/states/s-f12-06-consumption-empty-tablet-light.png) | ![Empty, dark](../../images/states/s-f12-06-consumption-empty-tablet-dark.png) |
| Loading | tablet | ![Loading, light](../../images/states/s-f12-06-consumption-loading-tablet-light.png) | ![Loading, dark](../../images/states/s-f12-06-consumption-loading-tablet-dark.png) |
| Read-only | tablet | ![Read-only, light](../../images/states/s-f12-06-consumption-read-only-tablet-light.png) | ![Read-only, dark](../../images/states/s-f12-06-consumption-read-only-tablet-dark.png) |
| Offline | tablet | ![Offline, light](../../images/states/s-f12-06-consumption-offline-tablet-light.png) | ![Offline, dark](../../images/states/s-f12-06-consumption-offline-tablet-dark.png) |

## Fields and columns

As its entities.

## Actions

As its use case's main flow.

## States

- Normal: Consume components, trace lots and serials, as the wireframe shows.
- Empty: No component to consume yet, with Back to the order.
- Loading: skeleton rows in place of the list ([C-03](../../../../04-ux/design-system/components/c-03-data-table.md));
  actions are disabled until it has loaded.
- Error: the error message pattern (D122).
- Read-only: done manufacturing orders and recorded checks, corrected by a new record.
- Offline: Works offline on the shop-floor tablet,
  [UC-F12-26](../../use-cases/11-finite-schedule-and-the-tablet/uc-f12-26-keep-working-on-the-tablet-without-the-network.md),
  the work orders loaded at the start of the shift, their instructions and the operator's start, stop, quantity and
  check records stay on the tablet and are sent in order when the network is back.

Shown entities (VD-15): [E-F12-04 Manufacturing order](../../data/e-f12-04-manufacturing-order.md),
[E-F12-25 Recipe](../../data/e-f12-25-recipe.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F12-04 Manufacturing order | Draft | Badge "Draft"; a new record starts here; next: Confirmed or Cancelled (UC-F12-04, BR-F12-02); fields editable within the role | U15, U20 | `u15-warehouse-operator/s-f12-06-consumption-e-f12-04-manufacturing-order-draft-{phone,tablet}-{light,dark}.png`, `u20-production-operator/s-f12-06-consumption-e-f12-04-manufacturing-order-draft-tablet-{light,dark}.png` |
| E-F12-04 Manufacturing order | Confirmed | Badge "Confirmed"; next: In progress or Cancelled (UC-F12-27, BR-F12-02); fields editable within the role | U15, U20 | `u15-warehouse-operator/s-f12-06-consumption-e-f12-04-manufacturing-order-confirmed-{phone,tablet}-{light,dark}.png`, `u20-production-operator/s-f12-06-consumption-e-f12-04-manufacturing-order-confirmed-tablet-{light,dark}.png` |
| E-F12-04 Manufacturing order | In progress | Badge "In progress"; next: Done or Cancelled (UC-F12-04, BR-F12-02); fields editable within the role | U15, U20 | `u15-warehouse-operator/s-f12-06-consumption-e-f12-04-manufacturing-order-in-progress-{phone,tablet}-{light,dark}.png`, `u20-production-operator/s-f12-06-consumption-e-f12-04-manufacturing-order-in-progress-tablet-{light,dark}.png` |
| E-F12-04 Manufacturing order | Done | Badge "Done"; final: read-only, no next state; the history shows how it got here | U15, U20 | `u15-warehouse-operator/s-f12-06-consumption-e-f12-04-manufacturing-order-done-{phone,tablet}-{light,dark}.png`, `u20-production-operator/s-f12-06-consumption-e-f12-04-manufacturing-order-done-tablet-{light,dark}.png` |
| E-F12-25 Recipe | Draft | Badge "Draft"; a new record starts here; next: Approved (BR-SC06-04); fields editable within the role | U20 | `u20-production-operator/s-f12-06-consumption-e-f12-25-recipe-draft-tablet-{light,dark}.png` |
| E-F12-25 Recipe | Approved | Badge "Approved"; next: Superseded (BR-SC06-04); fields editable within the role | U20 | `u20-production-operator/s-f12-06-consumption-e-f12-25-recipe-approved-tablet-{light,dark}.png` |
| E-F12-25 Recipe | Superseded | Badge "Superseded"; final: read-only, no next state; the history shows how it got here | U20 | `u20-production-operator/s-f12-06-consumption-e-f12-25-recipe-superseded-tablet-{light,dark}.png` |

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
- [FL-F12-09 Recipes and batches](../../flows/fl-f12-09-recipes-and-batches.md)

## Open questions

None.

---

⬅️ [S-F12-05 Shop-floor tablet](s-f12-05-shop-floor-tablet.md) · ⬆️ [Up](README.md) ·
➡️ [S-F12-07 Quality checks](../04-quality-and-maintenance/s-f12-07-quality-checks.md)
