🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
📦 [F7 Purchasing and stock](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F7-05 Count, trace and analyse](README.md) › 🖥️ S-F7-08 Traceability

# 🖥️ S-F7-08 Traceability

**Status:** ✅ specified

## Personas

- [U04 Purchasing](../../../../01-users/personas/u04-purchasing.md)
- [U02 Manager](../../../../01-users/personas/u02-manager.md)

## Purpose

Trace lots and serials, recall.

## Entry points

Purchasing or Stock in the menu.

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F7-05 step 2, U04 | desktop | ![FL-F7-05 step 2, U04, light](../../images/05-count-trace-and-analyse/u04-purchasing/2-trace-a-lot-desktop-light.png) | ![FL-F7-05 step 2, U04, dark](../../images/05-count-trace-and-analyse/u04-purchasing/2-trace-a-lot-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f07-08-traceability-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f07-08-traceability-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f07-08-traceability-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f07-08-traceability-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f07-08-traceability-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f07-08-traceability-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f07-08-traceability-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f07-08-traceability-offline-desktop-dark.png) |

## Fields and columns

As its entities.

## Actions

As its use case's main flow.

## States

- Normal: Trace lots and serials, recall, as the wireframe shows.
- Empty: No lot or serial matching the search yet, with Clear the search.
- Loading: skeleton rows in place of the list ([C-03](../../../../04-ux/design-system/components/c-03-data-table.md));
  actions are disabled until it has loaded.
- Error: the error message pattern (D122).
- Read-only: confirmed moves and posted valuations, corrected by a new move.
- Offline: Not available offline: a back-office screen on live, shared data (D38: only today's schedule, time and
  intervention records work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-F7-10 Lot or serial](../../data/e-f07-10-lot-or-serial.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F7-10 Lot or serial | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U04 | `u04-purchasing/s-f07-08-traceability-e-f07-10-lot-or-serial-active-desktop-{light,dark}.png` |

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

- [FL-F7-05 Count, trace and analyse](../../flows/fl-f07-05-count-trace-and-analyse.md)

## Open questions

None.

---

⬅️ [S-F7-07 Stock count](s-f07-07-stock-count.md) · ⬆️ [Up](README.md) ·
➡️ [S-F7-09 Stock valuation](../02-receive-and-store/s-f07-09-stock-valuation.md)
