🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
📦 [F7 Purchasing and stock](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F7-05 Count, trace and analyse](README.md) › 🖥️ S-F7-11 Stock analytics

# 🖥️ S-F7-11 Stock analytics

**Status:** ✅ specified

## Personas

- [U13 Owner](../../../../01-users/personas/u13-owner.md)
- [U02 Manager](../../../../01-users/personas/u02-manager.md)
- [U04 Purchasing](../../../../01-users/personas/u04-purchasing.md)

## Purpose

Analyse stock.

## Entry points

Purchasing or Stock in the menu.

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F7-05 step 3, U13 | desktop | ![FL-F7-05 step 3, U13, light](../../images/05-count-trace-and-analyse/u13-owner/3-stock-analytics-desktop-light.png) | ![FL-F7-05 step 3, U13, dark](../../images/05-count-trace-and-analyse/u13-owner/3-stock-analytics-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f07-11-stock-analytics-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f07-11-stock-analytics-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f07-11-stock-analytics-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f07-11-stock-analytics-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f07-11-stock-analytics-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f07-11-stock-analytics-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f07-11-stock-analytics-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f07-11-stock-analytics-offline-phone-dark.png) |

## Fields and columns

As its entities.

## Actions

As its use case's main flow.

## States

- Normal: Analyse stock, as the wireframe shows.
- Empty: No stock movement in the period yet, with Change the period.
- Loading: skeleton rows in place of the list ([C-03](../../../../04-ux/design-system/components/c-03-data-table.md));
  actions are disabled until it has loaded.
- Error: the error message pattern (D122).
- Read-only: confirmed moves and posted valuations, corrected by a new move.
- Offline: Not available offline: a back-office screen on live, shared data (D38: only today's schedule, time and
  intervention records work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-F7-11 Stock count](../../data/e-f07-11-stock-count.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F7-11 Stock count | To count | Badge "To count"; a new record starts here; next: Counted (UC-F7-07); fields editable within the role | U13 | `u13-owner/s-f07-11-stock-analytics-e-f07-11-stock-count-to-count-{desktop,phone}-{light,dark}.png` |
| E-F7-11 Stock count | To approve | Badge "To approve"; next: Applied (BR-F7-06); fields editable within the role | U13 | `u13-owner/s-f07-11-stock-analytics-e-f07-11-stock-count-to-approve-{desktop,phone}-{light,dark}.png` |
| E-F7-11 Stock count | Applied | Badge "Applied"; final: read-only, no next state; the history shows how it got here | U13 | `u13-owner/s-f07-11-stock-analytics-e-f07-11-stock-count-applied-{desktop,phone}-{light,dark}.png` |

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

⬅️ [S-F7-10 Returns and scrap](../04-pick-pack-and-ship/s-f07-10-returns-and-scrap.md) · ⬆️ [Up](README.md) ·
➡️ [S-F7-12 Supplier portal](../01-procure/s-f07-12-supplier-portal.md)
