🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
📦 [F7 Purchasing and stock](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F7-02 Receive and store](README.md) › 🖥️ S-F7-09 Stock valuation

# 🖥️ S-F7-09 Stock valuation

**Status:** ✅ specified

## Personas

- [U05 Accounting](../../../../01-users/personas/u05-accounting.md)

## Purpose

Value stock and landed costs.

## Entry points

Purchasing or Stock in the menu.

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F7-02 step 4, U05 | desktop | ![FL-F7-02 step 4, U05, light](../../images/02-receive-and-store/u05-accounting/4-stock-valuation-desktop-light.png) | ![FL-F7-02 step 4, U05, dark](../../images/02-receive-and-store/u05-accounting/4-stock-valuation-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f07-09-stock-valuation-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f07-09-stock-valuation-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f07-09-stock-valuation-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f07-09-stock-valuation-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f07-09-stock-valuation-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f07-09-stock-valuation-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f07-09-stock-valuation-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f07-09-stock-valuation-offline-desktop-dark.png) |

## Fields and columns

As its entities.

## Actions

As its use case's main flow.

## States

- Normal: Value stock and landed costs, as the wireframe shows.
- Empty: No stock to value yet, with Receive stock first.
- Loading: skeleton rows in place of the list ([C-03](../../../../04-ux/design-system/components/c-03-data-table.md));
  actions are disabled until it has loaded.
- Error: the error message pattern (D122).
- Read-only: confirmed moves and posted valuations, corrected by a new move.
- Offline: Not available offline: a back-office screen on live, shared data (D38: only today's schedule, time and
  intervention records work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-F7-12 Landed cost](../../data/e-f07-12-landed-cost.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F7-12 Landed cost | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U05 | `u05-accounting/s-f07-09-stock-valuation-e-f07-12-landed-cost-active-desktop-{light,dark}.png` |

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

- [FL-F7-02 Receive and store](../../flows/fl-f07-02-receive-and-store.md)

## Open questions

None.

---

⬅️ [S-F7-08 Traceability](../05-count-trace-and-analyse/s-f07-08-traceability.md) · ⬆️ [Up](README.md) ·
➡️ [S-F7-10 Returns and scrap](../04-pick-pack-and-ship/s-f07-10-returns-and-scrap.md)
