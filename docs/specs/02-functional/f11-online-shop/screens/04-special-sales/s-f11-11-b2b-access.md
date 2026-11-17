🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🛍️ [F11 Online shop (plugin)](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F11-04 B2B, subscriptions, rentals and digital](README.md) › 🖥️ S-F11-11 B2B access

# 🖥️ S-F11-11 B2B access

**Status:** ✅ specified

## Personas

- [U03 Sales](../../../../01-users/personas/u03-sales.md)
- [U09 Customer](../../../../01-users/personas/u09-customer.md)

## Purpose

Sell B2B online.

## Entry points

Online shop in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F11-04 step 1, U03 | desktop | ![FL-F11-04 step 1, U03, light](../../images/04-special-sales/u03-sales/1-b2b-access-desktop-light.png) | ![FL-F11-04 step 1, U03, dark](../../images/04-special-sales/u03-sales/1-b2b-access-desktop-dark.png) |
| FL-F11-04 step 1, U03 | phone | ![FL-F11-04 step 1, U03, light](../../images/04-special-sales/u03-sales/1-b2b-access-phone-light.png) | ![FL-F11-04 step 1, U03, dark](../../images/04-special-sales/u03-sales/1-b2b-access-phone-dark.png) |
| FL-F11-04 step 1, U03 | tablet | ![FL-F11-04 step 1, U03, light](../../images/04-special-sales/u03-sales/1-b2b-access-tablet-light.png) | ![FL-F11-04 step 1, U03, dark](../../images/04-special-sales/u03-sales/1-b2b-access-tablet-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f11-11-b2b-access-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f11-11-b2b-access-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f11-11-b2b-access-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f11-11-b2b-access-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f11-11-b2b-access-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f11-11-b2b-access-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f11-11-b2b-access-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f11-11-b2b-access-offline-phone-dark.png) |

## Fields and columns

As its entities.

## Actions

As its use case's main flow.

## States

- Normal: Sell B2B online, as the wireframe shows.
- Empty: No B2B customer yet, with Invite a customer.
- Loading: skeleton rows in place of the list ([C-03](../../../../04-ux/design-system/components/c-03-data-table.md));
  actions are disabled until it has loaded.
- Error: the error message pattern (D122).
- Read-only: placed orders for the shopper; published pages for non-editors.
- Offline: Not available offline: a back-office screen on live, shared data (D38: only today's schedule, time and
  intervention records work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-F11-09 Customer account](../../data/e-f11-09-customer-account.md),
[E-F6-03 Quote](../../../f06-customers-and-sales/data/e-f06-03-quote.md),
[E-F11-22 Punch-out session](../../data/e-f11-22-punch-out-session.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F11-09 Customer account | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U03, U09 | `u03-sales/s-f11-11-b2b-access-e-f11-09-customer-account-active-{desktop,phone,tablet}-{light,dark}.png`, `u09-customer/s-f11-11-b2b-access-e-f11-09-customer-account-active-phone-{light,dark}.png` |
| E-F6-03 Quote | Draft | Badge "Draft"; a new record starts here; next: To approve or Refused (UC-F6-03); fields editable within the role | U03, U09 | `u03-sales/s-f11-11-b2b-access-e-f06-03-quote-draft-{desktop,phone,tablet}-{light,dark}.png`, `u09-customer/s-f11-11-b2b-access-e-f06-03-quote-draft-phone-{light,dark}.png` |
| E-F6-03 Quote | To approve | Badge "To approve"; next: Sent, Refused or Expired (UC-F11-27, UC-F6-03, UC-F6-04); fields editable within the role | U03, U09 | `u03-sales/s-f11-11-b2b-access-e-f06-03-quote-to-approve-{desktop,phone,tablet}-{light,dark}.png`, `u09-customer/s-f11-11-b2b-access-e-f06-03-quote-to-approve-phone-{light,dark}.png` |
| E-F6-03 Quote | Sent | Badge "Sent"; next: Accepted, Refused or Expired (UC-F11-27, UC-F6-03, UC-F6-04); fields editable within the role | U03, U09 | `u03-sales/s-f11-11-b2b-access-e-f06-03-quote-sent-{desktop,phone,tablet}-{light,dark}.png`, `u09-customer/s-f11-11-b2b-access-e-f06-03-quote-sent-phone-{light,dark}.png` |
| E-F6-03 Quote | Expired | Badge "Expired"; final: read-only, no next state; the history shows how it got here | U03, U09 | `u03-sales/s-f11-11-b2b-access-e-f06-03-quote-expired-{desktop,phone,tablet}-{light,dark}.png`, `u09-customer/s-f11-11-b2b-access-e-f06-03-quote-expired-phone-{light,dark}.png` |
| E-F6-03 Quote | Accepted | Badge "Accepted"; next: Expired (UC-F6-04); fields editable within the role | U03, U09 | `u03-sales/s-f11-11-b2b-access-e-f06-03-quote-accepted-{desktop,phone,tablet}-{light,dark}.png`, `u09-customer/s-f11-11-b2b-access-e-f06-03-quote-accepted-phone-{light,dark}.png` |
| E-F11-22 Punch-out session | Open | Badge "Open"; a new record starts here; next: Returned (UC-F11-27); fields editable within the role | U03, U09 | `u03-sales/s-f11-11-b2b-access-e-f11-22-punch-out-session-open-{desktop,phone,tablet}-{light,dark}.png`, `u09-customer/s-f11-11-b2b-access-e-f11-22-punch-out-session-open-phone-{light,dark}.png` |
| E-F11-22 Punch-out session | Returned | Badge "Returned"; next: Expired (UC-F11-27); fields editable within the role | U03, U09 | `u03-sales/s-f11-11-b2b-access-e-f11-22-punch-out-session-returned-{desktop,phone,tablet}-{light,dark}.png`, `u09-customer/s-f11-11-b2b-access-e-f11-22-punch-out-session-returned-phone-{light,dark}.png` |
| E-F11-22 Punch-out session | Expired | Badge "Expired"; final: read-only, no next state; the history shows how it got here | U03, U09 | `u03-sales/s-f11-11-b2b-access-e-f11-22-punch-out-session-expired-{desktop,phone,tablet}-{light,dark}.png`, `u09-customer/s-f11-11-b2b-access-e-f11-22-punch-out-session-expired-phone-{light,dark}.png` |

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

- [FL-F11-04 B2B, subscriptions, rentals and digital](../../flows/fl-f11-04-special-sales.md)
- [FL-F11-09 Pre-orders and B2B buying](../../flows/fl-f11-09-pre-orders-and-b2b-buying.md)

## Open questions

None.

---

⬅️ [S-F11-10 Customer account](../03-after-the-order/s-f11-10-customer-account.md) · ⬆️ [Up](README.md) ·
➡️ [S-F11-12 Subscriptions and rentals](s-f11-12-subscriptions-and-rentals.md)
