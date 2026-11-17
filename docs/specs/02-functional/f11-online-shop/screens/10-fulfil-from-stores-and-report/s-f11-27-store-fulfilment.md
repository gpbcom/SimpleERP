🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🛍️ [F11 Online shop (plugin)](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F11-10 Fulfil from stores and report](README.md) › 🖥️ S-F11-27 Store fulfilment

# 🖥️ S-F11-27 Store fulfilment

**Status:** ✅ specified

## Personas

- [U23 Store manager](../../../../01-users/personas/u23-store-manager.md)
- [U15 Warehouse operator](../../../../01-users/personas/u15-warehouse-operator.md)
- [U17 Cashier](../../../../01-users/personas/u17-cashier.md)

## Purpose

Pick, pack and ship online orders assigned to the store.

## Entry points

Store › Online orders.

## Wireframe

```text
+------------------------------------------+
| Online orders for Villeurbanne (3)       |
| W-1201 Navy coat 38   by 17:00 [Pick]    |
| W-1203 Scarf          by 17:00 [Pick]    |
| Scan item... ok  [Pack] [Print label]    |
+------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F11-10 step 1, U23 | desktop | ![FL-F11-10 step 1, U23, light](../../images/10-fulfil-from-stores-and-report/u23-store-manager/1-store-fulfilment-desktop-light.png) | ![FL-F11-10 step 1, U23, dark](../../images/10-fulfil-from-stores-and-report/u23-store-manager/1-store-fulfilment-desktop-dark.png) |
| FL-F11-10 step 1, U23 | phone | ![FL-F11-10 step 1, U23, light](../../images/10-fulfil-from-stores-and-report/u23-store-manager/1-store-fulfilment-phone-light.png) | ![FL-F11-10 step 1, U23, dark](../../images/10-fulfil-from-stores-and-report/u23-store-manager/1-store-fulfilment-phone-dark.png) |
| FL-F11-10 step 1, U23 | tablet | ![FL-F11-10 step 1, U23, light](../../images/10-fulfil-from-stores-and-report/u23-store-manager/1-store-fulfilment-tablet-light.png) | ![FL-F11-10 step 1, U23, dark](../../images/10-fulfil-from-stores-and-report/u23-store-manager/1-store-fulfilment-tablet-dark.png) |
| Error E1, U23 | desktop | ![Error E1, U23, light](../../images/10-fulfil-from-stores-and-report/u23-store-manager/e1-store-fulfilment-refused-desktop-light.png) | ![Error E1, U23, dark](../../images/10-fulfil-from-stores-and-report/u23-store-manager/e1-store-fulfilment-refused-desktop-dark.png) |
| Error E1, U23 | phone | ![Error E1, U23, light](../../images/10-fulfil-from-stores-and-report/u23-store-manager/e1-store-fulfilment-refused-phone-light.png) | ![Error E1, U23, dark](../../images/10-fulfil-from-stores-and-report/u23-store-manager/e1-store-fulfilment-refused-phone-dark.png) |
| Error E1, U23 | tablet | ![Error E1, U23, light](../../images/10-fulfil-from-stores-and-report/u23-store-manager/e1-store-fulfilment-refused-tablet-light.png) | ![Error E1, U23, dark](../../images/10-fulfil-from-stores-and-report/u23-store-manager/e1-store-fulfilment-refused-tablet-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f11-27-store-fulfilment-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f11-27-store-fulfilment-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f11-27-store-fulfilment-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f11-27-store-fulfilment-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f11-27-store-fulfilment-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f11-27-store-fulfilment-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f11-27-store-fulfilment-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f11-27-store-fulfilment-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Editable |
|---|---|---|
| Orders, items, deadlines | E-F11-23 | scans |

## Actions

| Action | Who | Result |
|---|---|---|
| Pick, pack, label | store staff | Shipped |
| Not found | store staff | Reassigned |

## States

- Normal: pick, pack and ship online orders assigned to the store.
- Empty: "No online order to pick".
- Loading: skeleton rows in place of the list ([C-03](../../../../04-ux/design-system/components/c-03-data-table.md));
  actions disabled until it has loaded.
- Error: the error message pattern (D122).
- Read-only: shipped orders.
- Offline: Picking scans work offline as the barcode app
  ([D271](../../../../06-decisions/f07-purchasing-and-stock/d271-warehouse-operations.md)); labels wait for the network.

Shown entities (VD-15): [E-F11-23 Store fulfilment](../../data/e-f11-23-store-fulfilment.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F11-23 Store fulfilment | Assigned | Badge "Assigned"; a new record starts here; next: Picked (UC-F11-28); fields editable within the role | U23 | `u23-store-manager/s-f11-27-store-fulfilment-e-f11-23-store-fulfilment-assigned-{desktop,phone,tablet}-{light,dark}.png` |
| E-F11-23 Store fulfilment | Picked | Badge "Picked"; next: Shipped (UC-F11-28); fields editable within the role | U23 | `u23-store-manager/s-f11-27-store-fulfilment-e-f11-23-store-fulfilment-picked-{desktop,phone,tablet}-{light,dark}.png` |
| E-F11-23 Store fulfilment | Shipped | Badge "Shipped"; next: Reassigned (UC-F11-28); fields editable within the role | U23 | `u23-store-manager/s-f11-27-store-fulfilment-e-f11-23-store-fulfilment-shipped-{desktop,phone,tablet}-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Tablet and phone.

## Accessibility

Every status is a word, not only a colour; tables have headers; actions are buttons with labels.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-01 Button](../../../../04-ux/design-system/components/c-01-button.md)

## Shown in

- [FL-F11-10 Fulfil from stores and report](../../flows/fl-f11-10-fulfil-from-stores-and-report.md)

## Open questions

None.

---

⬅️ [S-F11-26 Pre-order](../09-pre-orders-and-b2b-buying/s-f11-26-pre-order.md) · ⬆️ [Up](README.md) ·
➡️ [S-F11-28 Shop reports](s-f11-28-shop-reports.md)
