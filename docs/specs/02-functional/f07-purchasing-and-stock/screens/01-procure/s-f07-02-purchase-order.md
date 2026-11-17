🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
📦 [F7 Purchasing and stock](../../README.md) › 🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-F7-01 Procure](README.md) ›
🖥️ S-F7-02 Purchase order

# 🖥️ S-F7-02 Purchase order

**Status:** ✅ specified

## Personas

- [U04 Purchasing](../../../../01-users/personas/u04-purchasing.md)

## Purpose

Order from a supplier.

## Entry points

Purchasing or Stock in the menu.

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F7-01 step 2, U04 | desktop | ![FL-F7-01 step 2, U04, light](../../images/01-procure/u04-purchasing/2-purchase-order-desktop-light.png) | ![FL-F7-01 step 2, U04, dark](../../images/01-procure/u04-purchasing/2-purchase-order-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f07-02-purchase-order-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f07-02-purchase-order-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f07-02-purchase-order-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f07-02-purchase-order-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f07-02-purchase-order-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f07-02-purchase-order-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f07-02-purchase-order-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f07-02-purchase-order-offline-desktop-dark.png) |

## Fields and columns

As its entities.

## Actions

As its use case's main flow.

## States

- Normal: Order from a supplier, as the wireframe shows.
- Empty: No purchase order yet, with New order.
- Loading: skeleton rows in place of the list ([C-03](../../../../04-ux/design-system/components/c-03-data-table.md));
  actions are disabled until it has loaded.
- Error: the error message pattern (D122).
- Read-only: confirmed moves and posted valuations, corrected by a new move.
- Offline: Not available offline (D38): on a phone or a computer, the offline banner replaces the actions and nothing is
  changed until the network is back; nothing is queued.

Shown entities (VD-15): [E-F7-03 Purchase order](../../data/e-f07-03-purchase-order.md),
[E-F7-15 Supplier contract](../../data/e-f07-15-supplier-contract.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F7-03 Purchase order | Draft | Badge "Draft"; a new record starts here; next: Sent (UC-F7-02); fields editable within the role | U04 | `u04-purchasing/s-f07-02-purchase-order-e-f07-03-purchase-order-draft-desktop-{light,dark}.png` |
| E-F7-03 Purchase order | Sent | Badge "Sent"; next: Confirmed (UC-F7-02); fields editable within the role | U04 | `u04-purchasing/s-f07-02-purchase-order-e-f07-03-purchase-order-sent-desktop-{light,dark}.png` |
| E-F7-03 Purchase order | Confirmed | Badge "Confirmed"; next: Received (UC-F7-04); fields editable within the role | U04 | `u04-purchasing/s-f07-02-purchase-order-e-f07-03-purchase-order-confirmed-desktop-{light,dark}.png` |
| E-F7-03 Purchase order | Received | Badge "Received"; next: Billed (UC-F7-01); fields editable within the role | U04 | `u04-purchasing/s-f07-02-purchase-order-e-f07-03-purchase-order-received-desktop-{light,dark}.png` |
| E-F7-03 Purchase order | Billed | Badge "Billed"; final: read-only, no next state; the history shows how it got here | U04 | `u04-purchasing/s-f07-02-purchase-order-e-f07-03-purchase-order-billed-desktop-{light,dark}.png` |
| E-F7-15 Supplier contract | Draft | Badge "Draft"; a new record starts here; next: Active (UC-F7-18); fields editable within the role | U04 | `u04-purchasing/s-f07-02-purchase-order-e-f07-15-supplier-contract-draft-desktop-{light,dark}.png` |
| E-F7-15 Supplier contract | Active | Badge "Active"; next: Renewed or Ended (UC-F7-18); fields editable within the role | U04 | `u04-purchasing/s-f07-02-purchase-order-e-f07-15-supplier-contract-active-desktop-{light,dark}.png` |
| E-F7-15 Supplier contract | Renewed | Badge "Renewed"; final: read-only, no next state; the history shows how it got here | U04 | `u04-purchasing/s-f07-02-purchase-order-e-f07-15-supplier-contract-renewed-desktop-{light,dark}.png` |
| E-F7-15 Supplier contract | Ended | Badge "Ended"; final: read-only, no next state; the history shows how it got here | U04 | `u04-purchasing/s-f07-02-purchase-order-e-f07-15-supplier-contract-ended-desktop-{light,dark}.png` |

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

- [FL-F7-01 Procure](../../flows/fl-f07-01-procure.md)
- [FL-F7-07 Supplier agreements and performance](../../flows/fl-f07-07-supplier-agreements-and-performance.md)

## Open questions

None.

---

⬅️ [S-F7-01 Purchase request](s-f07-01-purchase-request.md) · ⬆️ [Up](README.md) ·
➡️ [S-F7-03 Receipt](../02-receive-and-store/s-f07-03-receipt.md)
