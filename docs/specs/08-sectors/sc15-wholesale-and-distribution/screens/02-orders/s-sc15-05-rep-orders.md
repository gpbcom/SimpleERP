🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) ›
📦 [SC15 Wholesale and distribution](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-SC15-02 Orders](README.md) › 🖥️ S-SC15-05 Rep orders

# 🖥️ S-SC15-05 Rep orders

**Status:** ✅ specified

## Personas

- [U42 Sales representative](../../../../01-users/personas/u42-sales-representative.md)
- [U09 Customer](../../../../01-users/personas/u09-customer.md)

## Purpose

Used to take orders on the road, offline
([UC-SC15-05](../../use-cases/02-orders/uc-sc15-05-take-orders-on-the-road-offline.md)).

## Entry points

Wholesale and distribution in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC15-02 step 2, U42 | phone | ![FL-SC15-02 step 2, U42, light](../../images/02-orders/u42-sales-representative/2-rep-order-phone-light.png) | ![FL-SC15-02 step 2, U42, dark](../../images/02-orders/u42-sales-representative/2-rep-order-phone-dark.png) |
| FL-SC15-02 step 2, U42 | desktop | ![FL-SC15-02 step 2, U42, light](../../images/02-orders/u42-sales-representative/2-rep-order-desktop-light.png) | ![FL-SC15-02 step 2, U42, dark](../../images/02-orders/u42-sales-representative/2-rep-order-desktop-dark.png) |
| FL-SC15-02 step 2, U42 | tablet | ![FL-SC15-02 step 2, U42, light](../../images/02-orders/u42-sales-representative/2-rep-order-tablet-light.png) | ![FL-SC15-02 step 2, U42, dark](../../images/02-orders/u42-sales-representative/2-rep-order-tablet-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc15-05-rep-orders-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc15-05-rep-orders-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc15-05-rep-orders-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc15-05-rep-orders-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc15-05-rep-orders-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc15-05-rep-orders-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc15-05-rep-orders-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc15-05-rep-orders-offline-phone-dark.png) |

## Fields and columns

The fields of [E-SC15-04 Sales order](../../data/e-sc15-04-sales-order.md), shown as the entity pages list them, with
their examples.

## Actions

- Visit: [UC-SC15-05](../../use-cases/02-orders/uc-sc15-05-take-orders-on-the-road-offline.md), step 1.
- Order: [UC-SC15-05](../../use-cases/02-orders/uc-sc15-05-take-orders-on-the-road-offline.md), step 2.
- Sign: [UC-SC15-05](../../use-cases/02-orders/uc-sc15-05-take-orders-on-the-road-offline.md), step 3.
- Sync: [UC-SC15-05](../../use-cases/02-orders/uc-sc15-05-take-orders-on-the-road-offline.md), step 4.

## States

- Normal: the customer, catalogue at its prices, the order and sync state.
- Empty: "No order today".
- Loading: the frame and titles show at once with placeholder rows; within 1 second
  ([D408](../../../../06-decisions/technical/d408-performance-and-profiles.md)) the data replaces them, and a longer
  load shows a progress line saying what loads.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)) says what failed
  and what to do; what was typed is kept. For example, stock gone at sync: the line becomes a back-order.
- Read-only: synced orders are read-only.
- Offline: works offline,
  [UC-F6-21](../../../../02-functional/f06-customers-and-sales/use-cases/09-sell-on-the-road-and-steer-sales/uc-f06-21-take-orders-offline-on-the-road.md),
  customers, prices and stock of the last sync are kept on the tablet; orders wait and are rechecked on sync,
  [BR-F6-14](../../../../02-functional/f06-customers-and-sales/business-rules/br-f06-14-offline-orders-are-checked-again-on-sync.md).

Shown entities (VD-15): [E-SC15-04 Sales order](../../data/e-sc15-04-sales-order.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC15-04 Sales order | Held | Badge "Held"; next: Confirmed (UC-SC15-04); fields editable within the role | U09, U42 | `u09-customer/s-sc15-05-rep-orders-e-sc15-04-sales-order-held-phone-{light,dark}.png`, `u42-sales-representative/s-sc15-05-rep-orders-e-sc15-04-sales-order-held-{desktop,phone,tablet}-{light,dark}.png` |

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

- [FL-SC15-02 Orders](../../flows/fl-sc15-02-orders.md)

## Open questions

None.

---

⬅️ [S-SC15-04 EDI orders](s-sc15-04-edi-orders.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC15-06 Back-orders](s-sc15-06-back-orders.md)
