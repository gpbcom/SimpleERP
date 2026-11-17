🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
📦 [F7 Purchasing and stock](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F7-05 Count, trace and analyse](README.md) › 🖥️ S-F7-07 Stock count

# 🖥️ S-F7-07 Stock count

**Status:** ✅ specified

## Personas

- [U15 Warehouse operator](../../../../01-users/personas/u15-warehouse-operator.md)
- [U02 Manager](../../../../01-users/personas/u02-manager.md)

## Purpose

Count stock.

## Entry points

Purchasing or Stock in the menu.

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F7-05 step 1, U15 | phone | ![FL-F7-05 step 1, U15, light](../../images/05-count-trace-and-analyse/u15-warehouse-operator/1-cycle-count-phone-light.png) | ![FL-F7-05 step 1, U15, dark](../../images/05-count-trace-and-analyse/u15-warehouse-operator/1-cycle-count-phone-dark.png) |
| Empty | phone | ![Empty, light](../../images/states/s-f07-07-stock-count-empty-phone-light.png) | ![Empty, dark](../../images/states/s-f07-07-stock-count-empty-phone-dark.png) |
| Loading | phone | ![Loading, light](../../images/states/s-f07-07-stock-count-loading-phone-light.png) | ![Loading, dark](../../images/states/s-f07-07-stock-count-loading-phone-dark.png) |
| Read-only | phone | ![Read-only, light](../../images/states/s-f07-07-stock-count-read-only-phone-light.png) | ![Read-only, dark](../../images/states/s-f07-07-stock-count-read-only-phone-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f07-07-stock-count-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f07-07-stock-count-offline-phone-dark.png) |

## Fields and columns

As its entities.

## Actions

As its use case's main flow.

## States

- Normal: Count stock, as the wireframe shows.
- Empty: No count planned yet, with Plan a count.
- Loading: skeleton rows in place of the list ([C-03](../../../../04-ux/design-system/components/c-03-data-table.md));
  actions are disabled until it has loaded.
- Error: the error message pattern (D122).
- Read-only: confirmed moves and posted valuations, corrected by a new move.
- Offline: Works offline in the barcode app
  ([D271](../../../../06-decisions/f07-purchasing-and-stock/d271-warehouse-operations.md)): scans and quantities are
  kept on the device in a queue shown with its count, and sent when the network is back; the stock seen is the one
  loaded before going offline.

Shown entities (VD-15): [E-F7-11 Stock count](../../data/e-f07-11-stock-count.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F7-11 Stock count | To count | Badge "To count"; a new record starts here; next: Counted (UC-F7-07); fields editable within the role | U15 | `u15-warehouse-operator/s-f07-07-stock-count-e-f07-11-stock-count-to-count-{phone,tablet}-{light,dark}.png` |
| E-F7-11 Stock count | Counted | Badge "Counted"; next: To approve (UC-F7-07); fields editable within the role | U15 | `u15-warehouse-operator/s-f07-07-stock-count-e-f07-11-stock-count-counted-{phone,tablet}-{light,dark}.png` |
| E-F7-11 Stock count | To approve | Badge "To approve"; next: Applied (BR-F7-06); fields editable within the role | U15 | `u15-warehouse-operator/s-f07-07-stock-count-e-f07-11-stock-count-to-approve-{phone,tablet}-{light,dark}.png` |
| E-F7-11 Stock count | Applied | Badge "Applied"; final: read-only, no next state; the history shows how it got here | U15 | `u15-warehouse-operator/s-f07-07-stock-count-e-f07-11-stock-count-applied-{phone,tablet}-{light,dark}.png` |

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

⬅️ [S-F7-06 Pick, pack and ship](../04-pick-pack-and-ship/s-f07-06-pick-pack-and-ship.md) · ⬆️ [Up](README.md) ·
➡️ [S-F7-08 Traceability](s-f07-08-traceability.md)
