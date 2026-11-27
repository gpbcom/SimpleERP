🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
📦 [F7 Purchasing and stock](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F7-03 Replenish](README.md) › 🖥️ S-F7-13 Warehouse setup

# 🖥️ S-F7-13 Warehouse setup

**Status:** ✅ specified

## Personas

- [U07 Administrator](../../../../01-users/personas/u07-administrator.md)
- [U02 Manager](../../../../01-users/personas/u02-manager.md)

## Purpose

Set up warehouses, routes and rules.

## Entry points

Purchasing or Stock in the menu.

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F7-03 step 1, U07 | desktop | ![FL-F7-03 step 1, U07, light](../../images/03-replenish/u07-administrator/1-replenishment-report-desktop-light.png) | ![FL-F7-03 step 1, U07, dark](../../images/03-replenish/u07-administrator/1-replenishment-report-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f07-13-warehouse-setup-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f07-13-warehouse-setup-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f07-13-warehouse-setup-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f07-13-warehouse-setup-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f07-13-warehouse-setup-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f07-13-warehouse-setup-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f07-13-warehouse-setup-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f07-13-warehouse-setup-offline-desktop-dark.png) |

## Fields and columns

As its entities.

## Actions

As its use case's main flow.

## States

- Normal: Set up warehouses, routes and rules, as the wireframe shows.
- Empty: No warehouse besides the main one yet, with Add a warehouse.
- Loading: skeleton rows in place of the list ([C-03](../../../../04-ux/design-system/components/c-03-data-table.md));
  actions are disabled until it has loaded.
- Error: the error message pattern (D122).
- Read-only: confirmed moves and posted valuations, corrected by a new move.
- Offline: Not available offline: a back-office screen on live, shared data (D38: only today's schedule, time and
  intervention records work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-F7-07 Location](../../data/e-f07-07-location.md),
[E-F7-08 Route](../../data/e-f07-08-route.md), [E-F7-09 Reordering rule](../../data/e-f07-09-reordering-rule.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F7-07 Location | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U07 | `u07-administrator/s-f07-13-warehouse-setup-e-f07-07-location-active-desktop-{light,dark}.png` |
| E-F7-08 Route | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U02, U07 | `u02-manager/s-f07-13-warehouse-setup-e-f07-08-route-active-{desktop,phone}-{light,dark}.png`, `u07-administrator/s-f07-13-warehouse-setup-e-f07-08-route-active-desktop-{light,dark}.png` |
| E-F7-09 Reordering rule | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U07 | `u07-administrator/s-f07-13-warehouse-setup-e-f07-09-reordering-rule-active-desktop-{light,dark}.png` |

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

⬅️ [S-F7-12 Supplier portal](../01-procure/s-f07-12-supplier-portal.md) · ⬆️ [Up](README.md) ·
➡️ [S-F7-14 Tenders](../06-benchmark-additions/s-f07-14-tenders.md)
