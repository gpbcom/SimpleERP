🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🏪 [F10 Point of sale (plugin)](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F10-03 After sales](README.md) › 🖥️ S-F10-07 Loyalty

# 🖥️ S-F10-07 Loyalty

**Status:** ✅ specified

## Personas

- [U17 Cashier](../../../../01-users/personas/u17-cashier.md)
- [U09 Customer](../../../../01-users/personas/u09-customer.md)

## Purpose

Use loyalty, gift cards and e-wallet.

## Entry points

Point of sale in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F10-03 step 2, U17 | desktop | ![FL-F10-03 step 2, U17, light](../../images/03-after-sales/u17-cashier/2-loyalty-desktop-light.png) | ![FL-F10-03 step 2, U17, dark](../../images/03-after-sales/u17-cashier/2-loyalty-desktop-dark.png) |
| FL-F10-03 step 2, U17 | phone | ![FL-F10-03 step 2, U17, light](../../images/03-after-sales/u17-cashier/2-loyalty-phone-light.png) | ![FL-F10-03 step 2, U17, dark](../../images/03-after-sales/u17-cashier/2-loyalty-phone-dark.png) |
| FL-F10-03 step 2, U17 | tablet | ![FL-F10-03 step 2, U17, light](../../images/03-after-sales/u17-cashier/2-loyalty-tablet-light.png) | ![FL-F10-03 step 2, U17, dark](../../images/03-after-sales/u17-cashier/2-loyalty-tablet-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f10-07-loyalty-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f10-07-loyalty-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f10-07-loyalty-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f10-07-loyalty-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f10-07-loyalty-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f10-07-loyalty-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f10-07-loyalty-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f10-07-loyalty-offline-phone-dark.png) |

## Fields and columns

As its entities.

## Actions

As its use case's main flow.

## States

- Normal: Use loyalty, gift cards and e-wallet, as the wireframe shows.
- Empty: No loyalty card or gift card yet, with Issue one.
- Loading: skeleton rows in place of the list ([C-03](../../../../04-ux/design-system/components/c-03-data-table.md));
  actions are disabled until it has loaded.
- Error: the error message pattern (D122).
- Read-only: closed sessions and recorded sales, which are inalterable (CR-FR-026).
- Offline: The till keeps selling, numbering and chaining its sales locally and syncs on reconnect
  ([BR-F10-06](../../business-rules/br-f10-06-offline-keeps-selling.md)); a card terminal that loses its link cancels
  the payment; a warning shows after 24 hours offline.

Shown entities (VD-15): [E-F10-10 Loyalty card and gift card](../../data/e-f10-10-loyalty-card-and-gift-card.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F10-10 Loyalty card and gift card | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U09, U17 | `u09-customer/s-f10-07-loyalty-e-f10-10-loyalty-card-and-gift-card-active-phone-{light,dark}.png`, `u17-cashier/s-f10-07-loyalty-e-f10-10-loyalty-card-and-gift-card-active-{desktop,phone,tablet}-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop; approvals and receipts also on the phone.

## Accessibility

Labelled controls; amounts and states as text.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)

## Shown in

- [FL-F10-03 After sales](../../flows/fl-f10-03-after-sales.md)

## Open questions

None.

---

⬅️ [S-F10-06 Prices and promotions](../02-sell-at-the-counter/s-f10-06-prices-and-promotions.md) · ⬆️ [Up](README.md) ·
➡️ [S-F10-08 Weighing](../02-sell-at-the-counter/s-f10-08-weighing.md)
