🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🛍️ [SC02 Retail](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC02-03 Sell and return across channels](README.md) ›
🖥️ S-SC02-09 Returns

# 🖥️ S-SC02-09 Returns

**Status:** 🔄 waiting for the owner

## Personas

- [U17 Cashier](../../../../01-users/personas/u17-cashier.md)
- [U09 Customer](../../../../01-users/personas/u09-customer.md)

## Purpose

Used to return across channels
([UC-SC02-09](../../use-cases/03-sell-and-return-across-channels/uc-sc02-09-return-across-channels.md)).

## Entry points

Retail in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC02-03 step 2, U17 | desktop | ![FL-SC02-03 step 2, U17, light](../../images/03-sell-and-return-across-channels/u17-cashier/2-return-anywhere-desktop-light.png) | ![FL-SC02-03 step 2, U17, dark](../../images/03-sell-and-return-across-channels/u17-cashier/2-return-anywhere-desktop-dark.png) |
| FL-SC02-03 step 2, U17 | phone | ![FL-SC02-03 step 2, U17, light](../../images/03-sell-and-return-across-channels/u17-cashier/2-return-anywhere-phone-light.png) | ![FL-SC02-03 step 2, U17, dark](../../images/03-sell-and-return-across-channels/u17-cashier/2-return-anywhere-phone-dark.png) |
| FL-SC02-03 step 2, U17 | tablet | ![FL-SC02-03 step 2, U17, light](../../images/03-sell-and-return-across-channels/u17-cashier/2-return-anywhere-tablet-light.png) | ![FL-SC02-03 step 2, U17, dark](../../images/03-sell-and-return-across-channels/u17-cashier/2-return-anywhere-tablet-dark.png) |
| Error E1, U17 | desktop | ![Error E1, U17, light](../../images/03-sell-and-return-across-channels/u17-cashier/e1-return-late-desktop-light.png) | ![Error E1, U17, dark](../../images/03-sell-and-return-across-channels/u17-cashier/e1-return-late-desktop-dark.png) |
| Error E1, U17 | phone | ![Error E1, U17, light](../../images/03-sell-and-return-across-channels/u17-cashier/e1-return-late-phone-light.png) | ![Error E1, U17, dark](../../images/03-sell-and-return-across-channels/u17-cashier/e1-return-late-phone-dark.png) |
| Error E1, U17 | tablet | ![Error E1, U17, light](../../images/03-sell-and-return-across-channels/u17-cashier/e1-return-late-tablet-light.png) | ![Error E1, U17, dark](../../images/03-sell-and-return-across-channels/u17-cashier/e1-return-late-tablet-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc02-09-returns-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc02-09-returns-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc02-09-returns-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc02-09-returns-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc02-09-returns-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc02-09-returns-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc02-09-returns-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc02-09-returns-offline-phone-dark.png) |

## Fields and columns

The fields of [E-SC02-01 Store](../../data/e-sc02-01-store.md), shown as the entity pages list them, with their
examples.

## Actions

- Find the order: [UC-SC02-09](../../use-cases/03-sell-and-return-across-channels/uc-sc02-09-return-across-channels.md),
  step 1.
- Check the policy:
  [UC-SC02-09](../../use-cases/03-sell-and-return-across-channels/uc-sc02-09-return-across-channels.md), step 2.
- Refund or exchange:
  [UC-SC02-09](../../use-cases/03-sell-and-return-across-channels/uc-sc02-09-return-across-channels.md), step 3.
- Put back or set aside:
  [UC-SC02-09](../../use-cases/03-sell-and-return-across-channels/uc-sc02-09-return-across-channels.md), step 4.

## States

- Normal: the order found, its lines, the policy dates and the refund or exchange.
- Empty: "Search an order".
- Loading: the frame and titles show at once with placeholder rows; within 1 second
  ([D408](../../../../06-decisions/technical/d408-performance-and-profiles.md)) the data replaces them, and a longer
  load shows a progress line saying what loads.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)) says what failed
  and what to do; what was typed is kept. For example, past the return period: the return is refused with the date.
- Read-only: a refunded line is read-only.
- Offline: the till's offline mode records the return and syncs it,
  [UC-F10-14](../../../../02-functional/f10-point-of-sale/use-cases/06-mobile-and-delivery/uc-f10-14-sell-on-the-move-and-offline.md);
  orders from other channels need the network.

Shown entities (VD-15): none; no flow's Entities and screens table names an entity on this screen.

## Responsive behaviour

(Proposed) Desktop; approvals and receipts also on the phone.

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

⬅️ [S-SC02-08 Cross-channel orders](s-sc02-08-cross-channel-orders.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC02-10 Customer profile](../04-customers-and-staff/s-sc02-10-customer-profile.md)
