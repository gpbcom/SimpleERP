🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
📦 [F7 Purchasing and stock](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F7-02 Receive and store](README.md) › 🖥️ S-F7-03 Receipt

# 🖥️ S-F7-03 Receipt

**Status:** ✅ specified

## Personas

- [U15 Warehouse operator](../../../../01-users/personas/u15-warehouse-operator.md)

## Purpose

Receive goods.

## Entry points

Purchasing or Stock in the menu.

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F7-02 step 1, U15 | phone | ![FL-F7-02 step 1, U15, light](../../images/02-receive-and-store/u15-warehouse-operator/1-receive-phone-light.png) | ![FL-F7-02 step 1, U15, dark](../../images/02-receive-and-store/u15-warehouse-operator/1-receive-phone-dark.png) |
| FL-F7-02 step 1, U15 | tablet | ![FL-F7-02 step 1, U15, light](../../images/02-receive-and-store/u15-warehouse-operator/1-receive-tablet-light.png) | ![FL-F7-02 step 1, U15, dark](../../images/02-receive-and-store/u15-warehouse-operator/1-receive-tablet-dark.png) |
| Error E1, U15 | phone | ![Error E1, U15, light](../../images/02-receive-and-store/u15-warehouse-operator/e1-quality-failed-phone-light.png) | ![Error E1, U15, dark](../../images/02-receive-and-store/u15-warehouse-operator/e1-quality-failed-phone-dark.png) |
| Error E1, U15 | tablet | ![Error E1, U15, light](../../images/02-receive-and-store/u15-warehouse-operator/e1-quality-failed-tablet-light.png) | ![Error E1, U15, dark](../../images/02-receive-and-store/u15-warehouse-operator/e1-quality-failed-tablet-dark.png) |
| Empty | phone | ![Empty, light](../../images/states/s-f07-03-receipt-empty-phone-light.png) | ![Empty, dark](../../images/states/s-f07-03-receipt-empty-phone-dark.png) |
| Loading | phone | ![Loading, light](../../images/states/s-f07-03-receipt-loading-phone-light.png) | ![Loading, dark](../../images/states/s-f07-03-receipt-loading-phone-dark.png) |
| Read-only | phone | ![Read-only, light](../../images/states/s-f07-03-receipt-read-only-phone-light.png) | ![Read-only, dark](../../images/states/s-f07-03-receipt-read-only-phone-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f07-03-receipt-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f07-03-receipt-offline-phone-dark.png) |

## Fields and columns

As its entities.

## Actions

As its use case's main flow.

## States

- Normal: Receive goods, as the wireframe shows.
- Empty: No receipt expected yet, with Receive without an order.
- Loading: skeleton rows in place of the list ([C-03](../../../../04-ux/design-system/components/c-03-data-table.md));
  actions are disabled until it has loaded.
- Error: the error message pattern (D122).
- Read-only: confirmed moves and posted valuations, corrected by a new move.
- Offline: Works offline in the barcode app
  ([D271](../../../../06-decisions/f07-purchasing-and-stock/d271-warehouse-operations.md)): scans and quantities are
  kept on the device in a queue shown with its count, and sent when the network is back; the stock seen is the one
  loaded before going offline.

Shown entities (VD-15): [E-F7-04 Transfer](../../data/e-f07-04-transfer.md),
[E-F7-22 Delivery note](../../data/e-f07-22-delivery-note.md),
[E-F7-10 Lot or serial](../../data/e-f07-10-lot-or-serial.md),
[E-F7-19 Safety data sheet](../../data/e-f07-19-safety-data-sheet.md),
[E-F7-07 Location](../../data/e-f07-07-location.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F7-04 Transfer | Sent | Badge "Sent"; a new record starts here; next: Received or Lost (UC-F10-26); fields editable within the role | U15 | `u15-warehouse-operator/s-f07-03-receipt-e-f07-04-transfer-sent-{phone,tablet}-{light,dark}.png` |
| E-F7-04 Transfer | Received | Badge "Received"; next: Reserved or Lost (UC-F10-26); fields editable within the role | U15 | `u15-warehouse-operator/s-f07-03-receipt-e-f07-04-transfer-received-{phone,tablet}-{light,dark}.png` |
| E-F7-04 Transfer | Lost | Badge "Lost"; final: read-only, no next state; the history shows how it got here | U15 | `u15-warehouse-operator/s-f07-03-receipt-e-f07-04-transfer-lost-{phone,tablet}-{light,dark}.png` |
| E-F7-04 Transfer | Reserved | Badge "Reserved"; next: Flagged (UC-F10-26); fields editable within the role | U15 | `u15-warehouse-operator/s-f07-03-receipt-e-f07-04-transfer-reserved-{phone,tablet}-{light,dark}.png` |
| E-F7-04 Transfer | Flagged | Badge "Flagged"; next: Reserved (UC-F10-26); fields editable within the role | U15 | `u15-warehouse-operator/s-f07-03-receipt-e-f07-04-transfer-flagged-{phone,tablet}-{light,dark}.png` |
| E-F7-22 Delivery note | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U15 | `u15-warehouse-operator/s-f07-03-receipt-e-f07-22-delivery-note-active-{phone,tablet}-{light,dark}.png` |
| E-F7-10 Lot or serial | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U15 | `u15-warehouse-operator/s-f07-03-receipt-e-f07-10-lot-or-serial-active-{phone,tablet}-{light,dark}.png` |
| E-F7-19 Safety data sheet | Active | Badge "Active"; a new record starts here; next: Superseded (UC-F7-23); fields editable within the role | U15 | `u15-warehouse-operator/s-f07-03-receipt-e-f07-19-safety-data-sheet-active-{phone,tablet}-{light,dark}.png` |
| E-F7-19 Safety data sheet | Superseded | Badge "Superseded"; final: read-only, no next state; the history shows how it got here | U15 | `u15-warehouse-operator/s-f07-03-receipt-e-f07-19-safety-data-sheet-superseded-{phone,tablet}-{light,dark}.png` |
| E-F7-07 Location | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U15 | `u15-warehouse-operator/s-f07-03-receipt-e-f07-07-location-active-{phone,tablet}-{light,dark}.png` |

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

⬅️ [S-F7-02 Purchase order](../01-procure/s-f07-02-purchase-order.md) · ⬆️ [Up](README.md) ·
➡️ [S-F7-04 Supplier invoice matching](../01-procure/s-f07-04-supplier-invoice-matching.md)
