🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🛒 [F6 Customers and sales](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F6-03 Invoice and get paid](README.md) › 🖥️ S-F6-07 Payments and reconciliation

# 🖥️ S-F6-07 Payments and reconciliation

**Status:** ✅ specified

## Personas

- [U09 Customer](../../../../01-users/personas/u09-customer.md)
- [U05 Accounting](../../../../01-users/personas/u05-accounting.md)

## Purpose

Get paid online and reconcile.

## Entry points

Sales in the menu; the portal for customers.

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F6-03 step 2, U05 | desktop | ![FL-F6-03 step 2, U05, light](../../images/03-invoice-and-get-paid/u05-accounting/2-payments-desktop-light.png) | ![FL-F6-03 step 2, U05, dark](../../images/03-invoice-and-get-paid/u05-accounting/2-payments-desktop-dark.png) |
| Empty | phone | ![Empty, light](../../images/states/s-f06-07-payments-and-reconciliation-empty-phone-light.png) | ![Empty, dark](../../images/states/s-f06-07-payments-and-reconciliation-empty-phone-dark.png) |
| Loading | phone | ![Loading, light](../../images/states/s-f06-07-payments-and-reconciliation-loading-phone-light.png) | ![Loading, dark](../../images/states/s-f06-07-payments-and-reconciliation-loading-phone-dark.png) |
| Read-only | phone | ![Read-only, light](../../images/states/s-f06-07-payments-and-reconciliation-read-only-phone-light.png) | ![Read-only, dark](../../images/states/s-f06-07-payments-and-reconciliation-read-only-phone-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f06-07-payments-and-reconciliation-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f06-07-payments-and-reconciliation-offline-phone-dark.png) |

## Fields and columns

As its entities.

## Actions

As its use cases' main flows.

## States

- Normal: Get paid online and reconcile, as the wireframe shows.
- Empty: No payment to reconcile yet, with Import a statement.
- Loading: skeleton rows in place of the list ([C-03](../../../../04-ux/design-system/components/c-03-data-table.md));
  actions are disabled until it has loaded.
- Error: the error message pattern (D122).
- Read-only: sent, signed or posted documents, changed only by a new version, a credit note or an amendment.
- Offline: Not available offline: a back-office screen on live, shared data (D38: only today's schedule, time and
  intervention records work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-F6-06 Customer payment](../../data/e-f06-06-customer-payment.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F6-06 Customer payment | Matched | Badge "Matched"; a new record starts here; no other state; fields editable within the role | U05, U09 | `u05-accounting/s-f06-07-payments-and-reconciliation-e-f06-06-customer-payment-matched-desktop-{light,dark}.png`, `u09-customer/s-f06-07-payments-and-reconciliation-e-f06-06-customer-payment-matched-phone-{light,dark}.png` |
| E-F6-06 Customer payment | Refused | Badge "Refused"; a new record starts here; no other state; fields editable within the role | U05, U09 | `u05-accounting/s-f06-07-payments-and-reconciliation-e-f06-06-customer-payment-refused-desktop-{light,dark}.png`, `u09-customer/s-f06-07-payments-and-reconciliation-e-f06-06-customer-payment-refused-phone-{light,dark}.png` |

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

- [FL-F6-03 Invoice and get paid](../../flows/fl-f06-03-invoice-and-get-paid.md)

## Open questions

None.

---

⬅️ [S-F6-06 Invoice](s-f06-06-invoice.md) · ⬆️ [Up](README.md) · ➡️ [S-F6-08 Reminders](s-f06-08-reminders.md)
