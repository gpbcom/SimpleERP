🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
📦 [F7 Purchasing and stock](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F7-03 Replenish](README.md) › 🖥️ S-F7-05 Replenishment

# 🖥️ S-F7-05 Replenishment

**Status:** ✅ specified

## Personas

- [U04 Purchasing](../../../../01-users/personas/u04-purchasing.md)

## Purpose

Replenish stock.

## Entry points

Purchasing or Stock in the menu.

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F7-03 step 3, U04 | desktop | ![FL-F7-03 step 3, U04, light](../../images/03-replenish/u04-purchasing/3-replenishment-desktop-light.png) | ![FL-F7-03 step 3, U04, dark](../../images/03-replenish/u04-purchasing/3-replenishment-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f07-05-replenishment-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f07-05-replenishment-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f07-05-replenishment-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f07-05-replenishment-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f07-05-replenishment-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f07-05-replenishment-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f07-05-replenishment-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f07-05-replenishment-offline-desktop-dark.png) |

## Fields and columns

As its entities.

## Actions

As its use case's main flow.

## States

- Normal: Replenish stock, as the wireframe shows.
- Empty: No suggested order yet, with Add a reordering rule.
- Loading: skeleton rows in place of the list ([C-03](../../../../04-ux/design-system/components/c-03-data-table.md));
  actions are disabled until it has loaded.
- Error: the error message pattern (D122).
- Read-only: confirmed moves and posted valuations, corrected by a new move.
- Offline: Not available offline: a back-office screen on live, shared data (D38: only today's schedule, time and
  intervention records work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-F7-09 Reordering rule](../../data/e-f07-09-reordering-rule.md),
[E-F7-21 Demand forecast](../../data/e-f07-21-demand-forecast.md),
[E-F7-03 Purchase order](../../data/e-f07-03-purchase-order.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F7-09 Reordering rule | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U04 | `u04-purchasing/s-f07-05-replenishment-e-f07-09-reordering-rule-active-desktop-{light,dark}.png` |
| E-F7-21 Demand forecast | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U04 | `u04-purchasing/s-f07-05-replenishment-e-f07-21-demand-forecast-active-desktop-{light,dark}.png` |
| E-F7-03 Purchase order | Draft | Badge "Draft"; a new record starts here; next: Sent (UC-F7-02); fields editable within the role | U04 | `u04-purchasing/s-f07-05-replenishment-e-f07-03-purchase-order-draft-desktop-{light,dark}.png` |
| E-F7-03 Purchase order | Sent | Badge "Sent"; next: Confirmed (UC-F7-02); fields editable within the role | U04 | `u04-purchasing/s-f07-05-replenishment-e-f07-03-purchase-order-sent-desktop-{light,dark}.png` |
| E-F7-03 Purchase order | Confirmed | Badge "Confirmed"; next: Received (UC-F7-04); fields editable within the role | U04 | `u04-purchasing/s-f07-05-replenishment-e-f07-03-purchase-order-confirmed-desktop-{light,dark}.png` |
| E-F7-03 Purchase order | Received | Badge "Received"; next: Billed (UC-F7-01); fields editable within the role | U04 | `u04-purchasing/s-f07-05-replenishment-e-f07-03-purchase-order-received-desktop-{light,dark}.png` |
| E-F7-03 Purchase order | Billed | Badge "Billed"; final: read-only, no next state; the history shows how it got here | U04 | `u04-purchasing/s-f07-05-replenishment-e-f07-03-purchase-order-billed-desktop-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop; receipts, picking and counts on phones, offline.

## Accessibility

Labelled controls; quantities and states as text.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)

## Shown in

- [FL-F7-03 Replenish](../../flows/fl-f07-03-replenish.md)

## Open questions

None.

---

⬅️ [S-F7-04 Supplier invoice matching](../01-procure/s-f07-04-supplier-invoice-matching.md) · ⬆️ [Up](README.md) ·
➡️ [S-F7-06 Pick, pack and ship](../04-pick-pack-and-ship/s-f07-06-pick-pack-and-ship.md)
