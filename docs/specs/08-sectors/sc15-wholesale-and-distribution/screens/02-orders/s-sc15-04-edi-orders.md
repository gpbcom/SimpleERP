🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) ›
📦 [SC15 Wholesale and distribution](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-SC15-02 Orders](README.md) › 🖥️ S-SC15-04 EDI orders

# 🖥️ S-SC15-04 EDI orders

**Status:** ✅ specified

## Personas

- [U03 Sales](../../../../01-users/personas/u03-sales.md)

## Purpose

Used to take orders by EDI from retailers
([UC-SC15-04](../../use-cases/02-orders/uc-sc15-04-take-orders-by-edi-from-retailers.md)).

## Entry points

Wholesale and distribution in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC15-02 step 1, U03 | desktop | ![FL-SC15-02 step 1, U03, light](../../images/02-orders/u03-sales/1-edi-desktop-light.png) | ![FL-SC15-02 step 1, U03, dark](../../images/02-orders/u03-sales/1-edi-desktop-dark.png) |
| FL-SC15-02 step 1, U03 | phone | ![FL-SC15-02 step 1, U03, light](../../images/02-orders/u03-sales/1-edi-phone-light.png) | ![FL-SC15-02 step 1, U03, dark](../../images/02-orders/u03-sales/1-edi-phone-dark.png) |
| FL-SC15-02 step 1, U03 | tablet | ![FL-SC15-02 step 1, U03, light](../../images/02-orders/u03-sales/1-edi-tablet-light.png) | ![FL-SC15-02 step 1, U03, dark](../../images/02-orders/u03-sales/1-edi-tablet-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc15-04-edi-orders-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc15-04-edi-orders-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc15-04-edi-orders-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc15-04-edi-orders-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc15-04-edi-orders-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc15-04-edi-orders-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc15-04-edi-orders-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc15-04-edi-orders-offline-phone-dark.png) |

## Fields and columns

The fields of [E-SC15-04 Sales order](../../data/e-sc15-04-sales-order.md), shown as the entity pages list them, with
their examples.

## Actions

- Receive: [UC-SC15-04](../../use-cases/02-orders/uc-sc15-04-take-orders-by-edi-from-retailers.md), step 1.
- Validate: [UC-SC15-04](../../use-cases/02-orders/uc-sc15-04-take-orders-by-edi-from-retailers.md), step 2.
- Confirm: [UC-SC15-04](../../use-cases/02-orders/uc-sc15-04-take-orders-by-edi-from-retailers.md), step 3.

## States

- Normal: EDI orders with validation and confirmations.
- Empty: "No EDI order".
- Loading: the frame and titles show at once with placeholder rows; within 1 second
  ([D408](../../../../06-decisions/technical/d408-performance-and-profiles.md)) the data replaces them, and a longer
  load shows a progress line saying what loads.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)) says what failed
  and what to do; what was typed is kept. For example, a price differs: the order is held.
- Read-only: confirmed ones are read-only.
- Offline: not available offline: office work on agreements, accounts and statistics. Offline work is kept for the phone
  forms of the field, [D38](../../../../06-decisions/ux/d38-offline-field-tasks.md),
  [UC-F2-22](../../../../02-functional/f02-no-code-configuration/use-cases/09-portals-and-offline-forms/uc-f02-22-fill-a-form-offline-on-the-phone.md).
  A banner says the connection is lost; what is on screen stays visible, every action is disabled and nothing is queued
  until the connection is back.

Shown entities (VD-15): [E-SC15-04 Sales order](../../data/e-sc15-04-sales-order.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC15-04 Sales order | Confirmed | Badge "Confirmed"; a new record starts here; next: Partly shipped or Held (BR-SC15-05, UC-SC15-04); fields editable within the role | U03, U15 | `u03-sales/s-sc15-04-edi-orders-e-sc15-04-sales-order-confirmed-{desktop,phone,tablet}-{light,dark}.png`, `u15-warehouse-operator/s-sc15-04-edi-orders-e-sc15-04-sales-order-confirmed-{phone,tablet}-{light,dark}.png` |
| E-SC15-04 Sales order | Partly shipped | Badge "Partly shipped"; next: Shipped (UC-SC15-04); fields editable within the role | U03 | `u03-sales/s-sc15-04-edi-orders-e-sc15-04-sales-order-partly-shipped-{desktop,phone,tablet}-{light,dark}.png` |
| E-SC15-04 Sales order | Held | Badge "Held"; next: Confirmed (UC-SC15-04); fields editable within the role | U03, U15 | `u03-sales/s-sc15-04-edi-orders-e-sc15-04-sales-order-held-{desktop,phone,tablet}-{light,dark}.png`, `u15-warehouse-operator/s-sc15-04-edi-orders-e-sc15-04-sales-order-held-{phone,tablet}-{light,dark}.png` |
| E-SC15-04 Sales order | Shipped | Badge "Shipped"; final: read-only, no next state; the history shows how it got here | U03 | `u03-sales/s-sc15-04-edi-orders-e-sc15-04-sales-order-shipped-{desktop,phone,tablet}-{light,dark}.png` |

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

⬅️ [S-SC15-03 Yearly agreement](../01-prices-and-agreements/s-sc15-03-yearly-agreement.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC15-05 Rep orders](s-sc15-05-rep-orders.md)
