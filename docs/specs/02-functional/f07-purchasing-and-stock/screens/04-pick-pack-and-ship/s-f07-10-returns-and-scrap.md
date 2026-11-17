🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
📦 [F7 Purchasing and stock](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F7-04 Pick, pack and ship](README.md) › 🖥️ S-F7-10 Returns and scrap

# 🖥️ S-F7-10 Returns and scrap

**Status:** ✅ specified

## Personas

- [U15 Warehouse operator](../../../../01-users/personas/u15-warehouse-operator.md)

## Purpose

Handle returns and scrap.

## Entry points

Purchasing or Stock in the menu.

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F7-04 step 2, U15 | phone | ![FL-F7-04 step 2, U15, light](../../images/04-pick-pack-and-ship/u15-warehouse-operator/2-returns-and-scrap-phone-light.png) | ![FL-F7-04 step 2, U15, dark](../../images/04-pick-pack-and-ship/u15-warehouse-operator/2-returns-and-scrap-phone-dark.png) |
| FL-F7-04 step 2, U15 | tablet | ![FL-F7-04 step 2, U15, light](../../images/04-pick-pack-and-ship/u15-warehouse-operator/2-returns-and-scrap-tablet-light.png) | ![FL-F7-04 step 2, U15, dark](../../images/04-pick-pack-and-ship/u15-warehouse-operator/2-returns-and-scrap-tablet-dark.png) |
| Empty | phone | ![Empty, light](../../images/states/s-f07-10-returns-and-scrap-empty-phone-light.png) | ![Empty, dark](../../images/states/s-f07-10-returns-and-scrap-empty-phone-dark.png) |
| Loading | phone | ![Loading, light](../../images/states/s-f07-10-returns-and-scrap-loading-phone-light.png) | ![Loading, dark](../../images/states/s-f07-10-returns-and-scrap-loading-phone-dark.png) |
| Read-only | phone | ![Read-only, light](../../images/states/s-f07-10-returns-and-scrap-read-only-phone-light.png) | ![Read-only, dark](../../images/states/s-f07-10-returns-and-scrap-read-only-phone-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f07-10-returns-and-scrap-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f07-10-returns-and-scrap-offline-phone-dark.png) |

## Fields and columns

As its entities.

## Actions

As its use case's main flow.

## States

- Normal: Handle returns and scrap, as the wireframe shows.
- Empty: No return or scrap yet, with New return.
- Loading: skeleton rows in place of the list ([C-03](../../../../04-ux/design-system/components/c-03-data-table.md));
  actions are disabled until it has loaded.
- Error: the error message pattern (D122).
- Read-only: confirmed moves and posted valuations, corrected by a new move.
- Offline: Works offline in the barcode app
  ([D271](../../../../06-decisions/f07-purchasing-and-stock/d271-warehouse-operations.md)): scans and quantities are
  kept on the device in a queue shown with its count, and sent when the network is back; the stock seen is the one
  loaded before going offline.

Shown entities (VD-15): [E-F7-04 Transfer](../../data/e-f07-04-transfer.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F7-04 Transfer | Sent | Badge "Sent"; a new record starts here; next: Received or Lost (UC-F10-26); fields editable within the role | U15 | `u15-warehouse-operator/s-f07-10-returns-and-scrap-e-f07-04-transfer-sent-{phone,tablet}-{light,dark}.png` |
| E-F7-04 Transfer | Received | Badge "Received"; next: Reserved or Lost (UC-F10-26); fields editable within the role | U15 | `u15-warehouse-operator/s-f07-10-returns-and-scrap-e-f07-04-transfer-received-{phone,tablet}-{light,dark}.png` |
| E-F7-04 Transfer | Lost | Badge "Lost"; final: read-only, no next state; the history shows how it got here | U15 | `u15-warehouse-operator/s-f07-10-returns-and-scrap-e-f07-04-transfer-lost-{phone,tablet}-{light,dark}.png` |
| E-F7-04 Transfer | Reserved | Badge "Reserved"; next: Flagged (UC-F10-26); fields editable within the role | U15 | `u15-warehouse-operator/s-f07-10-returns-and-scrap-e-f07-04-transfer-reserved-{phone,tablet}-{light,dark}.png` |
| E-F7-04 Transfer | Flagged | Badge "Flagged"; next: Reserved (UC-F10-26); fields editable within the role | U15 | `u15-warehouse-operator/s-f07-10-returns-and-scrap-e-f07-04-transfer-flagged-{phone,tablet}-{light,dark}.png` |

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

- [FL-F7-04 Pick, pack and ship](../../flows/fl-f07-04-pick-pack-and-ship.md)

## Open questions

None.

---

⬅️ [S-F7-09 Stock valuation](../02-receive-and-store/s-f07-09-stock-valuation.md) · ⬆️ [Up](README.md) ·
➡️ [S-F7-11 Stock analytics](../05-count-trace-and-analyse/s-f07-11-stock-analytics.md)
