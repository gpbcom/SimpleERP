🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🛒 [F6 Customers and sales](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F6-03 Invoice and get paid](README.md) › 🖥️ S-F6-08 Reminders

# 🖥️ S-F6-08 Reminders

**Status:** ✅ specified

## Personas

- [U05 Accounting](../../../../01-users/personas/u05-accounting.md)

## Purpose

Remind late payers.

## Entry points

Sales in the menu; the portal for customers.

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F6-03 step 3, U05 | desktop | ![FL-F6-03 step 3, U05, light](../../images/03-invoice-and-get-paid/u05-accounting/3-automatic-reminders-desktop-light.png) | ![FL-F6-03 step 3, U05, dark](../../images/03-invoice-and-get-paid/u05-accounting/3-automatic-reminders-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f06-08-reminders-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f06-08-reminders-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f06-08-reminders-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f06-08-reminders-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f06-08-reminders-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f06-08-reminders-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f06-08-reminders-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f06-08-reminders-offline-desktop-dark.png) |

## Fields and columns

As its entities.

## Actions

As its use cases' main flows.

## States

- Normal: Remind late payers, as the wireframe shows.
- Empty: No overdue invoice yet, with Nothing to remind.
- Loading: skeleton rows in place of the list ([C-03](../../../../04-ux/design-system/components/c-03-data-table.md));
  actions are disabled until it has loaded.
- Error: the error message pattern (D122).
- Read-only: sent, signed or posted documents, changed only by a new version, a credit note or an amendment.
- Offline: Not available offline: a back-office screen on live, shared data (D38: only today's schedule, time and
  intervention records work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-F6-05 Invoice](../../data/e-f06-05-invoice.md),
[E-F6-21 Payment reminder](../../data/e-f06-21-payment-reminder.md),
[E-F6-22 Formal notice](../../data/e-f06-22-formal-notice.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F6-05 Invoice | Sent | Badge "Sent"; a new record starts here; next: Received or Refused (UC-F6-06); fields editable within the role | U05 | `u05-accounting/s-f06-08-reminders-e-f06-05-invoice-sent-desktop-{light,dark}.png` |
| E-F6-05 Invoice | Received | Badge "Received"; next: Paid or Refused (UC-F6-06); fields editable within the role | U05 | `u05-accounting/s-f06-08-reminders-e-f06-05-invoice-received-desktop-{light,dark}.png` |
| E-F6-05 Invoice | Paid | Badge "Paid"; next: Draft or Refused (BR-F6-07, UC-F6-06); fields editable within the role | U05 | `u05-accounting/s-f06-08-reminders-e-f06-05-invoice-paid-desktop-{light,dark}.png` |
| E-F6-21 Payment reminder | Active | Badge "Active"; a new record starts here; next: Paused or Stopped (UC-F6-24, UC-F6-23, BR-F6-05); fields editable within the role | U05 | `u05-accounting/s-f06-08-reminders-e-f06-21-payment-reminder-active-desktop-{light,dark}.png` |
| E-F6-21 Payment reminder | Paused | Badge "Paused"; next: Active or Stopped (UC-F6-24); fields editable within the role | U05 | `u05-accounting/s-f06-08-reminders-e-f06-21-payment-reminder-paused-desktop-{light,dark}.png` |
| E-F6-21 Payment reminder | Stopped | Badge "Stopped"; final: read-only, no next state; the history shows how it got here | U05 | `u05-accounting/s-f06-08-reminders-e-f06-21-payment-reminder-stopped-desktop-{light,dark}.png` |
| E-F6-22 Formal notice | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U05 | `u05-accounting/s-f06-08-reminders-e-f06-22-formal-notice-active-desktop-{light,dark}.png` |
| E-F6-05 Invoice | Draft | Badge "Draft"; next: Issued or Refused (UC-F6-06); fields editable within the role | U05 | `u05-accounting/s-f06-08-reminders-e-f06-05-invoice-draft-desktop-{light,dark}.png` |

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

⬅️ [S-F6-07 Payments and reconciliation](s-f06-07-payments-and-reconciliation.md) · ⬆️ [Up](README.md) ·
➡️ [S-F6-09 Subscriptions](../04-subscriptions/s-f06-09-subscriptions.md)
