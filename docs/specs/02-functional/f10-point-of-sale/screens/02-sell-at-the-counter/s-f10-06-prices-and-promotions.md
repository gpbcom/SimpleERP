🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🏪 [F10 Point of sale (plugin)](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F10-02 Sell at the counter](README.md) › 🖥️ S-F10-06 Prices and promotions

# 🖥️ S-F10-06 Prices and promotions

**Status:** ✅ specified

## Personas

- [U17 Cashier](../../../../01-users/personas/u17-cashier.md)
- [U02 Manager](../../../../01-users/personas/u02-manager.md)

## Purpose

Apply prices, promotions and combos.

## Entry points

Point of sale in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F10-02 step 3, U17 | desktop | ![FL-F10-02 step 3, U17, light](../../images/02-sell-at-the-counter/u17-cashier/3-promotion-desktop-light.png) | ![FL-F10-02 step 3, U17, dark](../../images/02-sell-at-the-counter/u17-cashier/3-promotion-desktop-dark.png) |
| FL-F10-02 step 3, U17 | phone | ![FL-F10-02 step 3, U17, light](../../images/02-sell-at-the-counter/u17-cashier/3-promotion-phone-light.png) | ![FL-F10-02 step 3, U17, dark](../../images/02-sell-at-the-counter/u17-cashier/3-promotion-phone-dark.png) |
| FL-F10-02 step 3, U17 | tablet | ![FL-F10-02 step 3, U17, light](../../images/02-sell-at-the-counter/u17-cashier/3-promotion-tablet-light.png) | ![FL-F10-02 step 3, U17, dark](../../images/02-sell-at-the-counter/u17-cashier/3-promotion-tablet-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f10-06-prices-and-promotions-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f10-06-prices-and-promotions-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f10-06-prices-and-promotions-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f10-06-prices-and-promotions-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f10-06-prices-and-promotions-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f10-06-prices-and-promotions-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f10-06-prices-and-promotions-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f10-06-prices-and-promotions-offline-phone-dark.png) |

## Fields and columns

As its entities.

## Actions

As its use case's main flow.

## States

- Normal: Apply prices, promotions and combos, as the wireframe shows.
- Empty: No promotion yet, with New promotion.
- Loading: skeleton rows in place of the list ([C-03](../../../../04-ux/design-system/components/c-03-data-table.md));
  actions are disabled until it has loaded.
- Error: the error message pattern (D122).
- Read-only: closed sessions and recorded sales, which are inalterable (CR-FR-026).
- Offline: Not available offline: a back-office screen on live, shared data (D38: only today's schedule, time and
  intervention records work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-F10-08 Price promotion](../../data/e-f10-08-price-promotion.md),
[E-F10-09 Combo](../../data/e-f10-09-combo.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F10-08 Price promotion | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U02, U17 | `u02-manager/s-f10-06-prices-and-promotions-e-f10-08-price-promotion-active-{desktop,phone}-{light,dark}.png`, `u17-cashier/s-f10-06-prices-and-promotions-e-f10-08-price-promotion-active-{desktop,phone,tablet}-{light,dark}.png` |
| E-F10-09 Combo | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U17, U02 | `u17-cashier/s-f10-06-prices-and-promotions-e-f10-09-combo-active-{desktop,phone,tablet}-{light,dark}.png`, `u02-manager/s-f10-06-prices-and-promotions-e-f10-09-combo-active-{desktop,phone}-{light,dark}.png` |

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

- [FL-F10-02 Sell at the counter](../../flows/fl-f10-02-sell-at-the-counter.md)

## Open questions

None.

---

⬅️ [S-F10-05 Receipt](s-f10-05-receipt.md) · ⬆️ [Up](README.md) ·
➡️ [S-F10-07 Loyalty](../03-after-sales/s-f10-07-loyalty.md)
