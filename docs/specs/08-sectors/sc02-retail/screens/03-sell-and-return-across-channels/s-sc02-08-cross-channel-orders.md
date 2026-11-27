🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🛍️ [SC02 Retail](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC02-03 Sell and return across channels](README.md) ›
🖥️ S-SC02-08 Cross-channel orders

# 🖥️ S-SC02-08 Cross-channel orders

**Status:** ✅ specified

## Personas

- [U17 Cashier](../../../../01-users/personas/u17-cashier.md)
- [U09 Customer](../../../../01-users/personas/u09-customer.md)

## Purpose

Used to sell across channels
([UC-SC02-08](../../use-cases/03-sell-and-return-across-channels/uc-sc02-08-sell-across-channels.md)).

## Entry points

Retail in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC02-03 step 1, U17 | desktop | ![FL-SC02-03 step 1, U17, light](../../images/03-sell-and-return-across-channels/u17-cashier/1-endless-aisle-desktop-light.png) | ![FL-SC02-03 step 1, U17, dark](../../images/03-sell-and-return-across-channels/u17-cashier/1-endless-aisle-desktop-dark.png) |
| FL-SC02-03 step 1, U17 | phone | ![FL-SC02-03 step 1, U17, light](../../images/03-sell-and-return-across-channels/u17-cashier/1-endless-aisle-phone-light.png) | ![FL-SC02-03 step 1, U17, dark](../../images/03-sell-and-return-across-channels/u17-cashier/1-endless-aisle-phone-dark.png) |
| FL-SC02-03 step 1, U17 | tablet | ![FL-SC02-03 step 1, U17, light](../../images/03-sell-and-return-across-channels/u17-cashier/1-endless-aisle-tablet-light.png) | ![FL-SC02-03 step 1, U17, dark](../../images/03-sell-and-return-across-channels/u17-cashier/1-endless-aisle-tablet-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc02-08-cross-channel-orders-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc02-08-cross-channel-orders-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc02-08-cross-channel-orders-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc02-08-cross-channel-orders-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc02-08-cross-channel-orders-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc02-08-cross-channel-orders-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc02-08-cross-channel-orders-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc02-08-cross-channel-orders-offline-phone-dark.png) |

## Fields and columns

The fields of [E-SC02-01 Store](../../data/e-sc02-01-store.md), shown as the entity pages list them, with their
examples.

## Actions

- Order: [UC-SC02-08](../../use-cases/03-sell-and-return-across-channels/uc-sc02-08-sell-across-channels.md), step 1.
- Pick in the store holding it:
  [UC-SC02-08](../../use-cases/03-sell-and-return-across-channels/uc-sc02-08-sell-across-channels.md), step 2.
- Collect or ship: [UC-SC02-08](../../use-cases/03-sell-and-return-across-channels/uc-sc02-08-sell-across-channels.md),
  step 3.
- Close the order: [UC-SC02-08](../../use-cases/03-sell-and-return-across-channels/uc-sc02-08-sell-across-channels.md),
  step 4.

## States

- Normal: the order, the stores holding the product, the picking store and the order's state.
- Empty: "No order to prepare".
- Loading: the frame and titles show at once with placeholder rows; within 1 second
  ([D408](../../../../06-decisions/technical/d408-performance-and-profiles.md)) the data replaces them, and a longer
  load shows a progress line saying what loads.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)) says what failed
  and what to do; what was typed is kept. For example, the stock is gone when picking: another store holding it is
  proposed.
- Read-only: a collected order is read-only.
- Offline: not available offline: stock across stores is live; the till keeps selling offline what it holds,
  [UC-F10-14](../../../../02-functional/f10-point-of-sale/use-cases/06-mobile-and-delivery/uc-f10-14-sell-on-the-move-and-offline.md).

Shown entities (VD-15): none; no flow's Entities and screens table names an entity on this screen.

## Responsive behaviour

Desktop; approvals and receipts also on the phone.

## Accessibility

Labelled controls; amounts and states as text.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)

## Shown in

- [FL-SC02-03 Sell and return across channels](../../flows/fl-sc02-03-sell-and-return-across-channels.md)

## Open questions

None.

---

⬅️ [S-SC02-07 Store count](../02-keep-stock-right/s-sc02-07-store-count.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC02-09 Returns](s-sc02-09-returns.md)
