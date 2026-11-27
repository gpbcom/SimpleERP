🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🏪 [F10 Point of sale (plugin)](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F10-10 Clienteling, transfers and tax-free](README.md) › 🖥️ S-F10-25 Store stock and transfers

# 🖥️ S-F10-25 Store stock and transfers

**Status:** ✅ specified

## Personas

- [U17 Cashier](../../../../01-users/personas/u17-cashier.md)
- [U23 Store manager](../../../../01-users/personas/u23-store-manager.md)
- [U15 Warehouse operator](../../../../01-users/personas/u15-warehouse-operator.md)

## Purpose

See an item's stock in every store and ask, send and receive transfers.

## Entry points

The till › Stock; Store › Transfers.

## Wireframe

```text
+------------------------------------------------------------------+
| Navy coat  size 38                                                 |
| Lyon 0   Villeurbanne 2   Annecy 1   Warehouse 12   In transit 0   |
| [Transfer to Lyon]  [Ship to customer]   reserved for: Lea Roux    |
| Transfers: T-0331 Villeurbanne -> Lyon  sent 11-12  [Receive]      |
+------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F10-10 step 2, U17 | desktop | ![FL-F10-10 step 2, U17, light](../../images/10-clienteling-transfers-and-tax-free/u17-cashier/2-store-stock-and-transfers-desktop-light.png) | ![FL-F10-10 step 2, U17, dark](../../images/10-clienteling-transfers-and-tax-free/u17-cashier/2-store-stock-and-transfers-desktop-dark.png) |
| FL-F10-10 step 2, U17 | phone | ![FL-F10-10 step 2, U17, light](../../images/10-clienteling-transfers-and-tax-free/u17-cashier/2-store-stock-and-transfers-phone-light.png) | ![FL-F10-10 step 2, U17, dark](../../images/10-clienteling-transfers-and-tax-free/u17-cashier/2-store-stock-and-transfers-phone-dark.png) |
| FL-F10-10 step 2, U17 | tablet | ![FL-F10-10 step 2, U17, light](../../images/10-clienteling-transfers-and-tax-free/u17-cashier/2-store-stock-and-transfers-tablet-light.png) | ![FL-F10-10 step 2, U17, dark](../../images/10-clienteling-transfers-and-tax-free/u17-cashier/2-store-stock-and-transfers-tablet-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f10-25-store-stock-and-transfers-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f10-25-store-stock-and-transfers-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f10-25-store-stock-and-transfers-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f10-25-store-stock-and-transfers-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f10-25-store-stock-and-transfers-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f10-25-store-stock-and-transfers-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f10-25-store-stock-and-transfers-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f10-25-store-stock-and-transfers-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Editable |
|---|---|---|
| Stock per place, transfers | E-F7-04 | transfers |

## Actions

| Action | Who | Result |
|---|---|---|
| Transfer | sellers | Reserved and asked |
| Send, receive | store managers | Stock moved |

## States

- Normal: see an item's stock in every store and ask, send and receive transfers.
- Empty: the item is nowhere in stock: "Order it from the warehouse".
- Loading: skeleton rows in place of the list ([C-03](../../../../04-ux/design-system/components/c-03-data-table.md));
  actions disabled until it has loaded.
- Error: the error message pattern (D122).
- Read-only: received transfers.
- Offline: Stock seen offline is the last loaded, with its time; transfers wait for the network.

Shown entities (VD-15): [E-F7-04 Transfer](../../../f07-purchasing-and-stock/data/e-f07-04-transfer.md),
[E-F10-03 Point of sale order](../../data/e-f10-03-point-of-sale-order.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F7-04 Transfer | Sent | Badge "Sent"; a new record starts here; next: Received or Lost (UC-F10-26); fields editable within the role | U15, U17, U23 | `u15-warehouse-operator/s-f10-25-store-stock-and-transfers-e-f07-04-transfer-sent-{phone,tablet}-{light,dark}.png`, `u17-cashier/s-f10-25-store-stock-and-transfers-e-f07-04-transfer-sent-{desktop,phone,tablet}-{light,dark}.png`, `u23-store-manager/s-f10-25-store-stock-and-transfers-e-f07-04-transfer-sent-{desktop,phone,tablet}-{light,dark}.png` |
| E-F7-04 Transfer | Received | Badge "Received"; next: Reserved or Lost (UC-F10-26); fields editable within the role | U15, U17, U23 | `u15-warehouse-operator/s-f10-25-store-stock-and-transfers-e-f07-04-transfer-received-{phone,tablet}-{light,dark}.png`, `u17-cashier/s-f10-25-store-stock-and-transfers-e-f07-04-transfer-received-{desktop,phone,tablet}-{light,dark}.png`, `u23-store-manager/s-f10-25-store-stock-and-transfers-e-f07-04-transfer-received-{desktop,phone,tablet}-{light,dark}.png` |
| E-F7-04 Transfer | Lost | Badge "Lost"; final: read-only, no next state; the history shows how it got here | U15, U17, U23 | `u15-warehouse-operator/s-f10-25-store-stock-and-transfers-e-f07-04-transfer-lost-{phone,tablet}-{light,dark}.png`, `u17-cashier/s-f10-25-store-stock-and-transfers-e-f07-04-transfer-lost-{desktop,phone,tablet}-{light,dark}.png`, `u23-store-manager/s-f10-25-store-stock-and-transfers-e-f07-04-transfer-lost-{desktop,phone,tablet}-{light,dark}.png` |
| E-F7-04 Transfer | Reserved | Badge "Reserved"; next: Flagged (UC-F10-26); fields editable within the role | U15, U17, U23 | `u15-warehouse-operator/s-f10-25-store-stock-and-transfers-e-f07-04-transfer-reserved-{phone,tablet}-{light,dark}.png`, `u17-cashier/s-f10-25-store-stock-and-transfers-e-f07-04-transfer-reserved-{desktop,phone,tablet}-{light,dark}.png`, `u23-store-manager/s-f10-25-store-stock-and-transfers-e-f07-04-transfer-reserved-{desktop,phone,tablet}-{light,dark}.png` |
| E-F7-04 Transfer | Flagged | Badge "Flagged"; next: Reserved (UC-F10-26); fields editable within the role | U15, U17, U23 | `u15-warehouse-operator/s-f10-25-store-stock-and-transfers-e-f07-04-transfer-flagged-{phone,tablet}-{light,dark}.png`, `u17-cashier/s-f10-25-store-stock-and-transfers-e-f07-04-transfer-flagged-{desktop,phone,tablet}-{light,dark}.png`, `u23-store-manager/s-f10-25-store-stock-and-transfers-e-f07-04-transfer-flagged-{desktop,phone,tablet}-{light,dark}.png` |
| E-F10-03 Point of sale order | Draft | Badge "Draft"; a new record starts here; next: Paid (UC-F10-03); fields editable within the role | U17, U23 | `u17-cashier/s-f10-25-store-stock-and-transfers-e-f10-03-point-of-sale-order-draft-{desktop,phone,tablet}-{light,dark}.png`, `u23-store-manager/s-f10-25-store-stock-and-transfers-e-f10-03-point-of-sale-order-draft-{desktop,phone,tablet}-{light,dark}.png` |
| E-F10-03 Point of sale order | Paid | Badge "Paid"; next: Invoiced (UC-F10-04); fields editable within the role | U17, U23 | `u17-cashier/s-f10-25-store-stock-and-transfers-e-f10-03-point-of-sale-order-paid-{desktop,phone,tablet}-{light,dark}.png`, `u23-store-manager/s-f10-25-store-stock-and-transfers-e-f10-03-point-of-sale-order-paid-{desktop,phone,tablet}-{light,dark}.png` |
| E-F10-03 Point of sale order | Invoiced | Badge "Invoiced"; next: Refunded (UC-F10-03); fields editable within the role | U17, U23 | `u17-cashier/s-f10-25-store-stock-and-transfers-e-f10-03-point-of-sale-order-invoiced-{desktop,phone,tablet}-{light,dark}.png`, `u23-store-manager/s-f10-25-store-stock-and-transfers-e-f10-03-point-of-sale-order-invoiced-{desktop,phone,tablet}-{light,dark}.png` |
| E-F10-03 Point of sale order | Refunded | Badge "Refunded"; final: read-only, no next state; the history shows how it got here | U17, U23 | `u17-cashier/s-f10-25-store-stock-and-transfers-e-f10-03-point-of-sale-order-refunded-{desktop,phone,tablet}-{light,dark}.png`, `u23-store-manager/s-f10-25-store-stock-and-transfers-e-f10-03-point-of-sale-order-refunded-{desktop,phone,tablet}-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Till, tablet and phone.

## Accessibility

Every status is a word, not only a colour; tables have headers; actions are buttons with labels.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-01 Button](../../../../04-ux/design-system/components/c-01-button.md)

## Shown in

- [FL-F10-10 Clienteling, transfers and tax-free](../../flows/fl-f10-10-clienteling-transfers-and-tax-free.md)

## Open questions

None.

---

⬅️ [S-F10-24 Clienteling](s-f10-24-clienteling.md) · ⬆️ [Up](README.md) · ➡️ [S-F10-26 Tax-free](s-f10-26-tax-free.md)
