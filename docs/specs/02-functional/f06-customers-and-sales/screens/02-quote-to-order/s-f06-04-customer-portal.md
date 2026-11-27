🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🛒 [F6 Customers and sales](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F6-02 Quote to order](README.md) › 🖥️ S-F6-04 Customer portal

# 🖥️ S-F6-04 Customer portal

**Status:** ✅ specified

## Personas

- [U09 Customer](../../../../01-users/personas/u09-customer.md)

## Purpose

Accept or sign a quote; Use the customer portal.

## Entry points

Sales in the menu; the portal for customers.

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F6-02 step 1, U09 | phone | ![FL-F6-02 step 1, U09, light](../../images/02-quote-to-order/u09-customer/1-accept-in-portal-phone-light.png) | ![FL-F6-02 step 1, U09, dark](../../images/02-quote-to-order/u09-customer/1-accept-in-portal-phone-dark.png) |
| Empty | phone | ![Empty, light](../../images/states/s-f06-04-customer-portal-empty-phone-light.png) | ![Empty, dark](../../images/states/s-f06-04-customer-portal-empty-phone-dark.png) |
| Loading | phone | ![Loading, light](../../images/states/s-f06-04-customer-portal-loading-phone-light.png) | ![Loading, dark](../../images/states/s-f06-04-customer-portal-loading-phone-dark.png) |
| Read-only | phone | ![Read-only, light](../../images/states/s-f06-04-customer-portal-read-only-phone-light.png) | ![Read-only, dark](../../images/states/s-f06-04-customer-portal-read-only-phone-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f06-04-customer-portal-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f06-04-customer-portal-offline-phone-dark.png) |

## Fields and columns

As its entities.

## Actions

As its use cases' main flows.

## States

- Normal: Accept or sign a quote; Use the customer portal, as the wireframe shows.
- Empty: No document shared with this customer yet, with Contact us.
- Loading: skeleton rows in place of the list ([C-03](../../../../04-ux/design-system/components/c-03-data-table.md));
  actions are disabled until it has loaded.
- Error: the error message pattern (D122).
- Read-only: sent, signed or posted documents, changed only by a new version, a credit note or an amendment.
- Offline: Not available offline: an outside user's page served live (D407 keeps portals and website apart from the
  offline-first app); the browser shows that the page cannot be reached.

Shown entities (VD-15): [E-F6-01 Customer record](../../data/e-f06-01-customer-record.md),
[E-F6-03 Quote](../../data/e-f06-03-quote.md),
[E-F6-07 Subscription contract](../../data/e-f06-07-subscription-contract.md),
[E-F6-05 Invoice](../../data/e-f06-05-invoice.md), [E-F6-21 Payment reminder](../../data/e-f06-21-payment-reminder.md),
[E-F6-17 Invoice dispute](../../data/e-f06-17-invoice-dispute.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F6-01 Customer record | Active | Badge "Active"; final: read-only, no next state; the history shows how it got here | U09 | `u09-customer/s-f06-04-customer-portal-e-f06-01-customer-record-active-phone-{light,dark}.png` |
| E-F6-03 Quote | Draft | Badge "Draft"; a new record starts here; next: To approve or Refused (UC-F6-03); fields editable within the role | U09 | `u09-customer/s-f06-04-customer-portal-e-f06-03-quote-draft-phone-{light,dark}.png` |
| E-F6-03 Quote | To approve | Badge "To approve"; next: Sent, Refused or Expired (UC-F11-27, UC-F6-03, UC-F6-04); fields editable within the role | U09 | `u09-customer/s-f06-04-customer-portal-e-f06-03-quote-to-approve-phone-{light,dark}.png` |
| E-F6-03 Quote | Sent | Badge "Sent"; next: Accepted, Refused or Expired (UC-F11-27, UC-F6-03, UC-F6-04); fields editable within the role | U09 | `u09-customer/s-f06-04-customer-portal-e-f06-03-quote-sent-phone-{light,dark}.png` |
| E-F6-03 Quote | Accepted | Badge "Accepted"; next: Expired (UC-F6-04); fields editable within the role | U09 | `u09-customer/s-f06-04-customer-portal-e-f06-03-quote-accepted-phone-{light,dark}.png` |
| E-F6-07 Subscription contract | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U09 | `u09-customer/s-f06-04-customer-portal-e-f06-07-subscription-contract-active-phone-{light,dark}.png` |
| E-F6-05 Invoice | Sent | Badge "Sent"; a new record starts here; next: Received or Refused (UC-F6-06); fields editable within the role | U09 | `u09-customer/s-f06-04-customer-portal-e-f06-05-invoice-sent-phone-{light,dark}.png` |
| E-F6-05 Invoice | Received | Badge "Received"; next: Paid or Refused (UC-F6-06); fields editable within the role | U09 | `u09-customer/s-f06-04-customer-portal-e-f06-05-invoice-received-phone-{light,dark}.png` |
| E-F6-05 Invoice | Paid | Badge "Paid"; next: Draft or Refused (BR-F6-07, UC-F6-06); fields editable within the role | U09 | `u09-customer/s-f06-04-customer-portal-e-f06-05-invoice-paid-phone-{light,dark}.png` |
| E-F6-05 Invoice | Draft | Badge "Draft"; next: Issued or Refused (UC-F6-06); fields editable within the role | U09 | `u09-customer/s-f06-04-customer-portal-e-f06-05-invoice-draft-phone-{light,dark}.png` |
| E-F6-21 Payment reminder | Active | Badge "Active"; a new record starts here; next: Paused or Stopped (UC-F6-24, UC-F6-23, BR-F6-05); fields editable within the role | U09 | `u09-customer/s-f06-04-customer-portal-e-f06-21-payment-reminder-active-phone-{light,dark}.png` |
| E-F6-21 Payment reminder | Paused | Badge "Paused"; next: Active or Stopped (UC-F6-24); fields editable within the role | U09 | `u09-customer/s-f06-04-customer-portal-e-f06-21-payment-reminder-paused-phone-{light,dark}.png` |
| E-F6-21 Payment reminder | Stopped | Badge "Stopped"; final: read-only, no next state; the history shows how it got here | U09 | `u09-customer/s-f06-04-customer-portal-e-f06-21-payment-reminder-stopped-phone-{light,dark}.png` |
| E-F6-17 Invoice dispute | Open | Badge "Open"; a new record starts here; next: Settled (UC-F6-24); fields editable within the role | U09 | `u09-customer/s-f06-04-customer-portal-e-f06-17-invoice-dispute-open-phone-{light,dark}.png` |
| E-F6-01 Customer record | Accepted | Badge "Accepted"; a new record starts here; next: Active (UC-F6-11); fields editable within the role | U09 | `u09-customer/s-f06-04-customer-portal-e-f06-01-customer-record-accepted-phone-{light,dark}.png` |

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
- [FL-F6-08 Collect and settle](../../flows/fl-f06-08-collect-and-settle.md)

## Open questions

None.

---

⬅️ [S-F6-03 Quote editor](../01-lead-to-quote/s-f06-03-quote-editor.md) · ⬆️ [Up](README.md) ·
➡️ [S-F6-05 Order](s-f06-05-order.md)
