🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
📦 [F7 Purchasing and stock](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F7-06 Benchmark additions](README.md) › 🖥️ S-F7-14 Tenders

# 🖥️ S-F7-14 Tenders

**Status:** ✅ specified

## Personas

- [U04 Purchasing](../../../../01-users/personas/u04-purchasing.md)
- [U10 Supplier](../../../../01-users/personas/u10-supplier.md)

## Purpose

Run a call for tenders and rate suppliers.

## Entry points

Purchasing and stock in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F7-06 step 1, U04 | desktop | ![FL-F7-06 step 1, U04, light](../../images/06-benchmark-additions/u04-purchasing/1-tenders-desktop-light.png) | ![FL-F7-06 step 1, U04, dark](../../images/06-benchmark-additions/u04-purchasing/1-tenders-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f07-14-tenders-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f07-14-tenders-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f07-14-tenders-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f07-14-tenders-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f07-14-tenders-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f07-14-tenders-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f07-14-tenders-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f07-14-tenders-offline-desktop-dark.png) |

## Fields and columns

As its entities.

## Actions

As its use case's main flow.

## States

- Normal: Run a call for tenders and rate suppliers, as the wireframe shows.
- Empty: No call for tenders yet, with New call for tenders.
- Loading: skeleton rows in place of the list ([C-03](../../../../04-ux/design-system/components/c-03-data-table.md));
  actions are disabled until it has loaded.
- Error: the error message pattern (D122).
- Read-only: confirmed moves and posted valuations, corrected by a new move.
- Offline: Not available offline: a back-office screen on live, shared data (D38: only today's schedule, time and
  intervention records work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-F7-13 Call for tenders](../../data/e-f07-13-call-for-tenders.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F7-13 Call for tenders | Recorded | Badge "Recorded"; a new record starts here; no other state; fields editable within the role | U04, U10 | `u04-purchasing/s-f07-14-tenders-e-f07-13-call-for-tenders-recorded-desktop-{light,dark}.png`, `u10-supplier/s-f07-14-tenders-e-f07-13-call-for-tenders-recorded-phone-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop; approvals and lists also on the phone.

## Accessibility

Labelled controls; amounts and states as text.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)

## Shown in

- [FL-F7-06 Benchmark additions](../../flows/fl-f07-06-benchmark-additions.md)

## Open questions

None.

---

⬅️ [S-F7-13 Warehouse setup](../03-replenish/s-f07-13-warehouse-setup.md) · ⬆️ [Up](README.md) ·
➡️ [S-F7-15 Group trade](s-f07-15-group-trade.md)
