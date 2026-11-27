🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) ›
🚛 [SC07 Transport and logistics](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-SC07-01 Orders and planning](README.md) › 🖥️ S-SC07-01 Transport orders

# 🖥️ S-SC07-01 Transport orders

**Status:** ✅ specified

## Personas

- [U03 Sales](../../../../01-users/personas/u03-sales.md)
- [U29 Dispatcher](../../../../01-users/personas/u29-dispatcher.md)

## Purpose

Used to quote and take transport orders
([UC-SC07-01](../../use-cases/01-orders-and-planning/uc-sc07-01-quote-and-take-transport-orders.md)).

## Entry points

Transport and logistics in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC07-01 step 1, U03 | desktop | ![FL-SC07-01 step 1, U03, light](../../images/01-orders-and-planning/u03-sales/1-order-desktop-light.png) | ![FL-SC07-01 step 1, U03, dark](../../images/01-orders-and-planning/u03-sales/1-order-desktop-dark.png) |
| FL-SC07-01 step 1, U03 | phone | ![FL-SC07-01 step 1, U03, light](../../images/01-orders-and-planning/u03-sales/1-order-phone-light.png) | ![FL-SC07-01 step 1, U03, dark](../../images/01-orders-and-planning/u03-sales/1-order-phone-dark.png) |
| FL-SC07-01 step 1, U03 | tablet | ![FL-SC07-01 step 1, U03, light](../../images/01-orders-and-planning/u03-sales/1-order-tablet-light.png) | ![FL-SC07-01 step 1, U03, dark](../../images/01-orders-and-planning/u03-sales/1-order-tablet-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc07-01-transport-orders-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc07-01-transport-orders-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc07-01-transport-orders-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc07-01-transport-orders-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc07-01-transport-orders-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc07-01-transport-orders-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc07-01-transport-orders-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc07-01-transport-orders-offline-phone-dark.png) |

## Fields and columns

The fields of [E-SC07-01 Transport order](../../data/e-sc07-01-transport-order.md), shown as the entity pages list them,
with their examples.

## Actions

- Quote: [UC-SC07-01](../../use-cases/01-orders-and-planning/uc-sc07-01-quote-and-take-transport-orders.md), step 1.
- Accept: [UC-SC07-01](../../use-cases/01-orders-and-planning/uc-sc07-01-quote-and-take-transport-orders.md), step 2.
- Record the order: [UC-SC07-01](../../use-cases/01-orders-and-planning/uc-sc07-01-quote-and-take-transport-orders.md),
  step 3.

## States

- Normal: quotes and orders with lane, weight, pallets, windows and state.
- Empty: "No order", with New order.
- Loading: the frame and titles show at once with placeholder rows; within 1 second
  ([D408](../../../../06-decisions/technical/d408-performance-and-profiles.md)) the data replaces them, and a longer
  load shows a progress line saying what loads.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)) says what failed
  and what to do; what was typed is kept. For example, a lane without a rate: sales is asked to set one.
- Read-only: an accepted order changes only by the dispatcher.
- Offline: not available offline: dispatch and office work on live, shared data. Offline work is kept for the phone
  forms of the field, [D38](../../../../06-decisions/ux/d38-offline-field-tasks.md),
  [UC-F2-22](../../../../02-functional/f02-no-code-configuration/use-cases/09-portals-and-offline-forms/uc-f02-22-fill-a-form-offline-on-the-phone.md).
  A banner says the connection is lost; what is on screen stays visible, every action is disabled and nothing is queued
  until the connection is back.

Shown entities (VD-15): [E-SC07-01 Transport order](../../data/e-sc07-01-transport-order.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC07-01 Transport order | Quoted | Badge "Quoted"; a new record starts here; next: Ordered (UC-SC07-01); fields editable within the role | U03, U09, U29 | `u03-sales/s-sc07-01-transport-orders-e-sc07-01-transport-order-quoted-{desktop,phone,tablet}-{light,dark}.png`, `u09-customer/s-sc07-01-transport-orders-e-sc07-01-transport-order-quoted-phone-{light,dark}.png`, `u29-dispatcher/s-sc07-01-transport-orders-e-sc07-01-transport-order-quoted-{desktop,phone}-{light,dark}.png` |
| E-SC07-01 Transport order | Ordered | Badge "Ordered"; next: Planned (UC-SC07-01); fields editable within the role | U03, U09, U29 | `u03-sales/s-sc07-01-transport-orders-e-sc07-01-transport-order-ordered-{desktop,phone,tablet}-{light,dark}.png`, `u09-customer/s-sc07-01-transport-orders-e-sc07-01-transport-order-ordered-phone-{light,dark}.png`, `u29-dispatcher/s-sc07-01-transport-orders-e-sc07-01-transport-order-ordered-{desktop,phone}-{light,dark}.png` |
| E-SC07-01 Transport order | Planned | Badge "Planned"; next: Delivered (UC-SC07-01); fields editable within the role | U03, U09, U29 | `u03-sales/s-sc07-01-transport-orders-e-sc07-01-transport-order-planned-{desktop,phone,tablet}-{light,dark}.png`, `u09-customer/s-sc07-01-transport-orders-e-sc07-01-transport-order-planned-phone-{light,dark}.png`, `u29-dispatcher/s-sc07-01-transport-orders-e-sc07-01-transport-order-planned-{desktop,phone}-{light,dark}.png` |
| E-SC07-01 Transport order | Delivered | Badge "Delivered"; next: Billed (UC-SC07-01); fields editable within the role | U03, U09, U29 | `u03-sales/s-sc07-01-transport-orders-e-sc07-01-transport-order-delivered-{desktop,phone,tablet}-{light,dark}.png`, `u09-customer/s-sc07-01-transport-orders-e-sc07-01-transport-order-delivered-phone-{light,dark}.png`, `u29-dispatcher/s-sc07-01-transport-orders-e-sc07-01-transport-order-delivered-{desktop,phone}-{light,dark}.png` |
| E-SC07-01 Transport order | Billed | Badge "Billed"; final: read-only, no next state; the history shows how it got here | U03, U09, U29 | `u03-sales/s-sc07-01-transport-orders-e-sc07-01-transport-order-billed-{desktop,phone,tablet}-{light,dark}.png`, `u09-customer/s-sc07-01-transport-orders-e-sc07-01-transport-order-billed-phone-{light,dark}.png`, `u29-dispatcher/s-sc07-01-transport-orders-e-sc07-01-transport-order-billed-{desktop,phone}-{light,dark}.png` |

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

- [FL-SC07-01 Orders and planning](../../flows/fl-sc07-01-orders-and-planning.md)

## Open questions

None.

---

⬆️ [Up](README.md) · ➡️ [S-SC07-02 Trip planning](s-sc07-02-trip-planning.md)
