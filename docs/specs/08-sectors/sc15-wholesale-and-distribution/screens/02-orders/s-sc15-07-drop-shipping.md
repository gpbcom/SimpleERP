🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) ›
📦 [SC15 Wholesale and distribution](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-SC15-02 Orders](README.md) › 🖥️ S-SC15-07 Drop-shipping

# 🖥️ S-SC15-07 Drop-shipping

**Status:** ✅ specified

## Personas

- [U04 Purchasing](../../../../01-users/personas/u04-purchasing.md)
- [U03 Sales](../../../../01-users/personas/u03-sales.md)

## Purpose

Used to drop-ship from suppliers ([UC-SC15-07](../../use-cases/02-orders/uc-sc15-07-drop-ship-from-suppliers.md)).

## Entry points

Wholesale and distribution in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC15-02 step 4, U04 | desktop | ![FL-SC15-02 step 4, U04, light](../../images/02-orders/u04-purchasing/4-drop-ship-desktop-light.png) | ![FL-SC15-02 step 4, U04, dark](../../images/02-orders/u04-purchasing/4-drop-ship-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc15-07-drop-shipping-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc15-07-drop-shipping-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc15-07-drop-shipping-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc15-07-drop-shipping-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc15-07-drop-shipping-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc15-07-drop-shipping-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-sc15-07-drop-shipping-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-sc15-07-drop-shipping-offline-desktop-dark.png) |

## Fields and columns

The fields of [E-SC15-04 Sales order](../../data/e-sc15-04-sales-order.md),
[E-SC15-06 Purchase proposal](../../data/e-sc15-06-purchase-proposal.md), shown as the entity pages list them, with
their examples.

## Actions

- Take the order: [UC-SC15-07](../../use-cases/02-orders/uc-sc15-07-drop-ship-from-suppliers.md), step 1.
- Order from the supplier: [UC-SC15-07](../../use-cases/02-orders/uc-sc15-07-drop-ship-from-suppliers.md), step 2.
- Supplier ships: [UC-SC15-07](../../use-cases/02-orders/uc-sc15-07-drop-ship-from-suppliers.md), step 3.
- Bill the customer: [UC-SC15-07](../../use-cases/02-orders/uc-sc15-07-drop-ship-from-suppliers.md), step 4.

## States

- Normal: drop-ship orders with supplier and tracking.
- Empty: "No drop-ship".
- Loading: the frame and titles show at once with placeholder rows; within 1 second
  ([D408](../../../../06-decisions/technical/d408-performance-and-profiles.md)) the data replaces them, and a longer
  load shows a progress line saying what loads.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)) says what failed
  and what to do; what was typed is kept. For example, the supplier late: the customer is told.
- Read-only: billed ones are read-only.
- Offline: not available offline: office work on agreements, accounts and statistics. Offline work is kept for the phone
  forms of the field, [D38](../../../../06-decisions/ux/d38-offline-field-tasks.md),
  [UC-F2-22](../../../../02-functional/f02-no-code-configuration/use-cases/09-portals-and-offline-forms/uc-f02-22-fill-a-form-offline-on-the-phone.md).
  A banner says the connection is lost; what is on screen stays visible, every action is disabled and nothing is queued
  until the connection is back.

Shown entities (VD-15): [E-SC15-06 Purchase proposal](../../data/e-sc15-06-purchase-proposal.md),
[E-SC15-04 Sales order](../../data/e-sc15-04-sales-order.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC15-06 Purchase proposal | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U04 | `u04-purchasing/s-sc15-07-drop-shipping-e-sc15-06-purchase-proposal-active-desktop-{light,dark}.png` |
| E-SC15-04 Sales order | Held | Badge "Held"; next: Confirmed (UC-SC15-04); fields editable within the role | U03, U04 | `u03-sales/s-sc15-07-drop-shipping-e-sc15-04-sales-order-held-{desktop,phone,tablet}-{light,dark}.png`, `u04-purchasing/s-sc15-07-drop-shipping-e-sc15-04-sales-order-held-desktop-{light,dark}.png` |

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

⬅️ [S-SC15-06 Back-orders](s-sc15-06-back-orders.md) · ⬆️ [Up](README.md) · ➡️ [S-SC15-08 Waves](s-sc15-08-waves.md)
