🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🏪 [F10 Point of sale (plugin)](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F10-10 Clienteling, transfers and tax-free](README.md) › 🖥️ S-F10-24 Clienteling

# 🖥️ S-F10-24 Clienteling

**Status:** ✅ specified

## Personas

- [U17 Cashier](../../../../01-users/personas/u17-cashier.md)
- [U23 Store manager](../../../../01-users/personas/u23-store-manager.md)

## Purpose

See a recognised customer's history, sizes and wish list, and add notes.

## Entry points

The till or the seller's tablet › Customer.

## Wireframe

```text
+------------------------------------------------------------------+
| Lea Roux   card 4410   recognised (agreed 2025-03)                 |
| Sizes 38   Likes blue, linen                                       |
| Last purchases: dress (Lyon, 10-02), scarf (online, 09-14)         |
| Wish list: navy coat 38 [Find in other stores]  [+ Wish] [+ Note]  |
+------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F10-10 step 1, U17 | desktop | ![FL-F10-10 step 1, U17, light](../../images/10-clienteling-transfers-and-tax-free/u17-cashier/1-clienteling-desktop-light.png) | ![FL-F10-10 step 1, U17, dark](../../images/10-clienteling-transfers-and-tax-free/u17-cashier/1-clienteling-desktop-dark.png) |
| FL-F10-10 step 1, U17 | phone | ![FL-F10-10 step 1, U17, light](../../images/10-clienteling-transfers-and-tax-free/u17-cashier/1-clienteling-phone-light.png) | ![FL-F10-10 step 1, U17, dark](../../images/10-clienteling-transfers-and-tax-free/u17-cashier/1-clienteling-phone-dark.png) |
| FL-F10-10 step 1, U17 | tablet | ![FL-F10-10 step 1, U17, light](../../images/10-clienteling-transfers-and-tax-free/u17-cashier/1-clienteling-tablet-light.png) | ![FL-F10-10 step 1, U17, dark](../../images/10-clienteling-transfers-and-tax-free/u17-cashier/1-clienteling-tablet-dark.png) |
| Error E1, U17 | desktop | ![Error E1, U17, light](../../images/10-clienteling-transfers-and-tax-free/u17-cashier/e1-clienteling-refused-desktop-light.png) | ![Error E1, U17, dark](../../images/10-clienteling-transfers-and-tax-free/u17-cashier/e1-clienteling-refused-desktop-dark.png) |
| Error E1, U17 | phone | ![Error E1, U17, light](../../images/10-clienteling-transfers-and-tax-free/u17-cashier/e1-clienteling-refused-phone-light.png) | ![Error E1, U17, dark](../../images/10-clienteling-transfers-and-tax-free/u17-cashier/e1-clienteling-refused-phone-dark.png) |
| Error E1, U17 | tablet | ![Error E1, U17, light](../../images/10-clienteling-transfers-and-tax-free/u17-cashier/e1-clienteling-refused-tablet-light.png) | ![Error E1, U17, dark](../../images/10-clienteling-transfers-and-tax-free/u17-cashier/e1-clienteling-refused-tablet-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f10-24-clienteling-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f10-24-clienteling-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f10-24-clienteling-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f10-24-clienteling-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f10-24-clienteling-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f10-24-clienteling-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f10-24-clienteling-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f10-24-clienteling-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Editable |
|---|---|---|
| History, sizes, wishes, notes | E-F10-19 | wishes and notes |

## Actions

| Action | Who | Result |
|---|---|---|
| Add a wish or note | sellers | Saved |
| Find in other stores | sellers | UC-F10-26 |

## States

- Normal: see a recognised customer's history, sizes and wish list, and add notes.
- Empty: a customer without consent: "Purchase history only".
- Loading: skeleton rows in place of the list ([C-03](../../../../04-ux/design-system/components/c-03-data-table.md));
  actions disabled until it has loaded.
- Error: the error message pattern (D122).
- Read-only: for other stores' sellers: read only.
- Offline: The profile loaded before the network dropped stays readable; notes and wishes wait for the network.

Shown entities (VD-15): [E-F10-19 Clienteling profile](../../data/e-f10-19-clienteling-profile.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F10-19 Clienteling profile | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U17 | `u17-cashier/s-f10-24-clienteling-e-f10-19-clienteling-profile-active-{desktop,phone,tablet}-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Tablet and till.

## Accessibility

Every status is a word, not only a colour; tables have headers; actions are buttons with labels.

## Components

- [C-04 Card](../../../../04-ux/design-system/components/c-04-card.md)
- [C-01 Button](../../../../04-ux/design-system/components/c-01-button.md)

## Shown in

- [FL-F10-10 Clienteling, transfers and tax-free](../../flows/fl-f10-10-clienteling-transfers-and-tax-free.md)

## Open questions

None.

---

⬅️ [S-F10-23 Card settlements](../09-cash-and-settlements/s-f10-23-card-settlements.md) · ⬆️ [Up](README.md) ·
➡️ [S-F10-25 Store stock and transfers](s-f10-25-store-stock-and-transfers.md)
