🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) ›
📦 [SC15 Wholesale and distribution](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-SC15-02 Orders](README.md) › 🖥️ S-SC15-18 B2B portal

# 🖥️ S-SC15-18 B2B portal

**Status:** ✅ specified

## Personas

- [U09 Customer](../../../../01-users/personas/u09-customer.md)

## Purpose

Used to give customers a B2B portal and catalogue
([UC-SC15-18](../../use-cases/02-orders/uc-sc15-18-give-customers-a-b2b-portal-and-catalogue.md)).

## Entry points

Wholesale and distribution in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC15-02 step 5, U09 | phone | ![FL-SC15-02 step 5, U09, light](../../images/02-orders/u09-customer/5-portal-phone-light.png) | ![FL-SC15-02 step 5, U09, dark](../../images/02-orders/u09-customer/5-portal-phone-dark.png) |
| Empty | phone | ![Empty, light](../../images/states/s-sc15-18-b2b-portal-empty-phone-light.png) | ![Empty, dark](../../images/states/s-sc15-18-b2b-portal-empty-phone-dark.png) |
| Loading | phone | ![Loading, light](../../images/states/s-sc15-18-b2b-portal-loading-phone-light.png) | ![Loading, dark](../../images/states/s-sc15-18-b2b-portal-loading-phone-dark.png) |
| Read-only | phone | ![Read-only, light](../../images/states/s-sc15-18-b2b-portal-read-only-phone-light.png) | ![Read-only, dark](../../images/states/s-sc15-18-b2b-portal-read-only-phone-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc15-18-b2b-portal-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc15-18-b2b-portal-offline-phone-dark.png) |

## Fields and columns

The fields of [E-SC15-04 Sales order](../../data/e-sc15-04-sales-order.md),
[E-SC15-01 Price agreement](../../data/e-sc15-01-price-agreement.md), shown as the entity pages list them, with their
examples.

## Actions

- Sign in: [UC-SC15-18](../../use-cases/02-orders/uc-sc15-18-give-customers-a-b2b-portal-and-catalogue.md), step 1.
- Order at own prices: [UC-SC15-18](../../use-cases/02-orders/uc-sc15-18-give-customers-a-b2b-portal-and-catalogue.md),
  step 2.
- Place the order: [UC-SC15-18](../../use-cases/02-orders/uc-sc15-18-give-customers-a-b2b-portal-and-catalogue.md), step
  3.
- Follow: [UC-SC15-18](../../use-cases/02-orders/uc-sc15-18-give-customers-a-b2b-portal-and-catalogue.md), step 4.

## States

- Normal: the customer's catalogue, orders, deliveries and invoices.
- Empty: "No order yet".
- Loading: the frame and titles show at once with placeholder rows; within 1 second
  ([D408](../../../../06-decisions/technical/d408-performance-and-profiles.md)) the data replaces them, and a longer
  load shows a progress line saying what loads.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)) says what failed
  and what to do; what was typed is kept. For example, over credit: the order is held
  ([BR-SC15-08](../../business-rules/br-sc15-08-credit-limit-before-shipping.md)).
- Read-only: the customer sees only their own.
- Offline: not available offline: a portal page for customers.

Shown entities (VD-15): [E-SC15-04 Sales order](../../data/e-sc15-04-sales-order.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC15-04 Sales order | Held | Badge "Held"; next: Confirmed (UC-SC15-04); fields editable within the role | U09 | `u09-customer/s-sc15-18-b2b-portal-e-sc15-04-sales-order-held-phone-{light,dark}.png` |

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

⬅️ [S-SC15-17 Buying](../04-import-and-suppliers/s-sc15-17-buying.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC15-19 Supplier performance](../04-import-and-suppliers/s-sc15-19-supplier-performance.md)
