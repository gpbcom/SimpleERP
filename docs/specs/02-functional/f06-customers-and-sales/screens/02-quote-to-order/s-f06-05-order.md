🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🛒 [F6 Customers and sales](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F6-02 Quote to order](README.md) › 🖥️ S-F6-05 Order

# 🖥️ S-F6-05 Order

**Status:** ✅ specified

## Personas

- [U03 Sales](../../../../01-users/personas/u03-sales.md)
- [U16 Office worker](../../../../01-users/personas/u16-office-worker.md)

## Purpose

Turn a quote into an order and follow it.

## Entry points

Sales in the menu; the portal for customers.

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F6-02 step 2, U03 | desktop | ![FL-F6-02 step 2, U03, light](../../images/02-quote-to-order/u03-sales/2-order-desktop-light.png) | ![FL-F6-02 step 2, U03, dark](../../images/02-quote-to-order/u03-sales/2-order-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f06-05-order-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f06-05-order-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f06-05-order-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f06-05-order-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f06-05-order-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f06-05-order-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f06-05-order-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f06-05-order-offline-phone-dark.png) |

## Fields and columns

As its entities.

## Actions

As its use cases' main flows.

## States

- Normal: Turn a quote into an order and follow it, as the wireframe shows.
- Empty: No order yet, with New order.
- Loading: skeleton rows in place of the list ([C-03](../../../../04-ux/design-system/components/c-03-data-table.md));
  actions are disabled until it has loaded.
- Error: the error message pattern (D122).
- Read-only: sent, signed or posted documents, changed only by a new version, a credit note or an amendment.
- Offline: Works offline on the phone for orders and quotes taken on the road,
  [UC-F6-21](../../use-cases/09-sell-on-the-road-and-steer-sales/uc-f06-21-take-orders-offline-on-the-road.md), the
  customer list, price lists and stock loaded before leaving stay on the phone; new lines wait in a queue and are priced
  and checked again when the network is back.

Shown entities (VD-15): [E-F6-04 Order](../../data/e-f06-04-order.md),
[E-F6-12 Credit limit](../../data/e-f06-12-credit-limit.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F6-04 Order | Open | Badge "Open"; a new record starts here; next: In progress or Cancelled (UC-F6-05); fields editable within the role | U03, U16 | `u03-sales/s-f06-05-order-e-f06-04-order-open-{desktop,phone,tablet}-{light,dark}.png`, `u16-office-worker/s-f06-05-order-e-f06-04-order-open-{desktop,phone}-{light,dark}.png` |
| E-F6-04 Order | In progress | Badge "In progress"; next: Done or Cancelled (UC-F6-05); fields editable within the role | U03, U16 | `u03-sales/s-f06-05-order-e-f06-04-order-in-progress-{desktop,phone,tablet}-{light,dark}.png`, `u16-office-worker/s-f06-05-order-e-f06-04-order-in-progress-{desktop,phone}-{light,dark}.png` |
| E-F6-04 Order | Cancelled | Badge "Cancelled"; final: read-only, no next state; the history shows how it got here | U03, U16 | `u03-sales/s-f06-05-order-e-f06-04-order-cancelled-{desktop,phone,tablet}-{light,dark}.png`, `u16-office-worker/s-f06-05-order-e-f06-04-order-cancelled-{desktop,phone}-{light,dark}.png` |
| E-F6-04 Order | Done | Badge "Done"; final: read-only, no next state; the history shows how it got here | U03, U16 | `u03-sales/s-f06-05-order-e-f06-04-order-done-{desktop,phone,tablet}-{light,dark}.png`, `u16-office-worker/s-f06-05-order-e-f06-04-order-done-{desktop,phone}-{light,dark}.png` |
| E-F6-12 Credit limit | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U03 | `u03-sales/s-f06-05-order-e-f06-12-credit-limit-active-{desktop,phone,tablet}-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop and phone; quotes on a phone at the customer's site.

## Accessibility

Labelled controls; amounts and states as text.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)

## Shown in

- [FL-F6-02 Quote to order](../../flows/fl-f06-02-quote-to-order.md)
- [FL-F6-06 Accounts and credit](../../flows/fl-f06-06-accounts-and-credit.md)

## Open questions

None.

---

⬅️ [S-F6-04 Customer portal](s-f06-04-customer-portal.md) · ⬆️ [Up](README.md) ·
➡️ [S-F6-06 Invoice](../03-invoice-and-get-paid/s-f06-06-invoice.md)
