🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🛒 [F6 Customers and sales](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F6-03 Invoice and get paid](README.md) › 🖥️ S-F6-06 Invoice

# 🖥️ S-F6-06 Invoice

**Status:** ✅ specified

## Personas

- [U05 Accounting](../../../../01-users/personas/u05-accounting.md)
- [U16 Office worker](../../../../01-users/personas/u16-office-worker.md)

## Purpose

Invoice: deposits, progress and final; Credit note and refund.

## Entry points

Sales in the menu; the portal for customers.

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F6-03 step 1, U05 | desktop | ![FL-F6-03 step 1, U05, light](../../images/03-invoice-and-get-paid/u05-accounting/1-final-invoice-desktop-light.png) | ![FL-F6-03 step 1, U05, dark](../../images/03-invoice-and-get-paid/u05-accounting/1-final-invoice-desktop-dark.png) |
| Error E1, U05 | desktop | ![Error E1, U05, light](../../images/03-invoice-and-get-paid/u05-accounting/e1-platform-refused-desktop-light.png) | ![Error E1, U05, dark](../../images/03-invoice-and-get-paid/u05-accounting/e1-platform-refused-desktop-dark.png) |
| Error E1, U05 | desktop | ![Error E1, U05, light](../../images/07-special-invoicing/u05-accounting/e1-invoice-refused-desktop-light.png) | ![Error E1, U05, dark](../../images/07-special-invoicing/u05-accounting/e1-invoice-refused-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f06-06-invoice-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f06-06-invoice-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f06-06-invoice-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f06-06-invoice-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f06-06-invoice-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f06-06-invoice-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f06-06-invoice-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f06-06-invoice-offline-desktop-dark.png) |

## Fields and columns

As its entities.

## Actions

As its use cases' main flows.

## States

- Normal: Invoice: deposits, progress and final; Credit note and refund, as the wireframe shows.
- Empty: No invoice yet, with Invoice an order.
- Loading: skeleton rows in place of the list ([C-03](../../../../04-ux/design-system/components/c-03-data-table.md));
  actions are disabled until it has loaded.
- Error: the error message pattern (D122).
- Read-only: sent, signed or posted documents, changed only by a new version, a credit note or an amendment.
- Offline: Not available offline: a back-office screen on live, shared data (D38: only today's schedule, time and
  intervention records work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-F6-05 Invoice](../../data/e-f06-05-invoice.md),
[E-F6-06 Customer payment](../../data/e-f06-06-customer-payment.md),
[E-F6-14 Funder agreement](../../data/e-f06-14-funder-agreement.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F6-05 Invoice | Sent | Badge "Sent"; a new record starts here; next: Received or Refused (UC-F6-06); fields editable within the role | U05, U16 | `u05-accounting/s-f06-06-invoice-e-f06-05-invoice-sent-desktop-{light,dark}.png`, `u16-office-worker/s-f06-06-invoice-e-f06-05-invoice-sent-{desktop,phone}-{light,dark}.png` |
| E-F6-05 Invoice | Received | Badge "Received"; next: Paid or Refused (UC-F6-06); fields editable within the role | U05, U16 | `u05-accounting/s-f06-06-invoice-e-f06-05-invoice-received-desktop-{light,dark}.png`, `u16-office-worker/s-f06-06-invoice-e-f06-05-invoice-received-{desktop,phone}-{light,dark}.png` |
| E-F6-05 Invoice | Refused | Badge "Refused"; final: read-only, no next state; the history shows how it got here | U05, U16 | `u05-accounting/s-f06-06-invoice-e-f06-05-invoice-refused-desktop-{light,dark}.png`, `u16-office-worker/s-f06-06-invoice-e-f06-05-invoice-refused-{desktop,phone}-{light,dark}.png` |
| E-F6-05 Invoice | Paid | Badge "Paid"; next: Draft or Refused (BR-F6-07, UC-F6-06); fields editable within the role | U05, U16 | `u05-accounting/s-f06-06-invoice-e-f06-05-invoice-paid-desktop-{light,dark}.png`, `u16-office-worker/s-f06-06-invoice-e-f06-05-invoice-paid-{desktop,phone}-{light,dark}.png` |
| E-F6-05 Invoice | Draft | Badge "Draft"; next: Issued or Refused (UC-F6-06); fields editable within the role | U05, U16 | `u05-accounting/s-f06-06-invoice-e-f06-05-invoice-draft-desktop-{light,dark}.png`, `u16-office-worker/s-f06-06-invoice-e-f06-05-invoice-draft-{desktop,phone}-{light,dark}.png` |
| E-F6-05 Invoice | Issued | Badge "Issued"; next: Partly paid or Refused (BR-F6-07, UC-F6-06); fields editable within the role | U05, U16 | `u05-accounting/s-f06-06-invoice-e-f06-05-invoice-issued-desktop-{light,dark}.png`, `u16-office-worker/s-f06-06-invoice-e-f06-05-invoice-issued-{desktop,phone}-{light,dark}.png` |
| E-F6-05 Invoice | Partly paid | Badge "Partly paid"; next: Overdue (BR-F6-07); fields editable within the role | U05, U16 | `u05-accounting/s-f06-06-invoice-e-f06-05-invoice-partly-paid-desktop-{light,dark}.png`, `u16-office-worker/s-f06-06-invoice-e-f06-05-invoice-partly-paid-{desktop,phone}-{light,dark}.png` |
| E-F6-05 Invoice | Overdue | Badge "Overdue"; next: Partly paid (BR-F6-07); fields editable within the role | U05, U16 | `u05-accounting/s-f06-06-invoice-e-f06-05-invoice-overdue-desktop-{light,dark}.png`, `u16-office-worker/s-f06-06-invoice-e-f06-05-invoice-overdue-{desktop,phone}-{light,dark}.png` |
| E-F6-06 Customer payment | Matched | Badge "Matched"; a new record starts here; no other state; fields editable within the role | U05 | `u05-accounting/s-f06-06-invoice-e-f06-06-customer-payment-matched-desktop-{light,dark}.png` |
| E-F6-06 Customer payment | Refused | Badge "Refused"; a new record starts here; no other state; fields editable within the role | U05 | `u05-accounting/s-f06-06-invoice-e-f06-06-customer-payment-refused-desktop-{light,dark}.png` |
| E-F6-14 Funder agreement | Active | Badge "Active"; a new record starts here; next: Expired (UC-F6-20); fields editable within the role | U05 | `u05-accounting/s-f06-06-invoice-e-f06-14-funder-agreement-active-desktop-{light,dark}.png` |
| E-F6-14 Funder agreement | Expired | Badge "Expired"; final: read-only, no next state; the history shows how it got here | U05 | `u05-accounting/s-f06-06-invoice-e-f06-14-funder-agreement-expired-desktop-{light,dark}.png` |

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
- [FL-F6-07 Special invoicing](../../flows/fl-f06-07-special-invoicing.md)

## Open questions

None.

---

⬅️ [S-F6-05 Order](../02-quote-to-order/s-f06-05-order.md) · ⬆️ [Up](README.md) ·
➡️ [S-F6-07 Payments and reconciliation](s-f06-07-payments-and-reconciliation.md)
