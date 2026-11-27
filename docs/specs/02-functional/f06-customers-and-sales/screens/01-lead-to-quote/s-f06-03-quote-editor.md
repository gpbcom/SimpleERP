🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🛒 [F6 Customers and sales](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F6-01 Lead to quote](README.md) › 🖥️ S-F6-03 Quote editor

# 🖥️ S-F6-03 Quote editor

**Status:** ✅ specified

## Personas

- [U03 Sales](../../../../01-users/personas/u03-sales.md)

## Purpose

Create and send a quote.

## Entry points

Sales in the menu; the portal for customers.

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F6-01 step 3, U03 | desktop | ![FL-F6-01 step 3, U03, light](../../images/01-lead-to-quote/u03-sales/3-quote-desktop-light.png) | ![FL-F6-01 step 3, U03, dark](../../images/01-lead-to-quote/u03-sales/3-quote-desktop-dark.png) |
| FL-F6-01 step 3, U03 | phone | ![FL-F6-01 step 3, U03, light](../../images/01-lead-to-quote/u03-sales/3-quote-phone-light.png) | ![FL-F6-01 step 3, U03, dark](../../images/01-lead-to-quote/u03-sales/3-quote-phone-dark.png) |
| Error E1, U03 | desktop | ![Error E1, U03, light](../../images/01-lead-to-quote/u03-sales/e1-discount-needs-approval-desktop-light.png) | ![Error E1, U03, dark](../../images/01-lead-to-quote/u03-sales/e1-discount-needs-approval-desktop-dark.png) |
| Error E1, U03 | phone | ![Error E1, U03, light](../../images/01-lead-to-quote/u03-sales/e1-discount-needs-approval-phone-light.png) | ![Error E1, U03, dark](../../images/01-lead-to-quote/u03-sales/e1-discount-needs-approval-phone-dark.png) |
| Error E1, U03 | tablet | ![Error E1, U03, light](../../images/01-lead-to-quote/u03-sales/e1-discount-needs-approval-tablet-light.png) | ![Error E1, U03, dark](../../images/01-lead-to-quote/u03-sales/e1-discount-needs-approval-tablet-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f06-03-quote-editor-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f06-03-quote-editor-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f06-03-quote-editor-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f06-03-quote-editor-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f06-03-quote-editor-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f06-03-quote-editor-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f06-03-quote-editor-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f06-03-quote-editor-offline-phone-dark.png) |

## Fields and columns

As its entities.

## Actions

As its use cases' main flows.

## States

- Normal: Create and send a quote, as the wireframe shows.
- Empty: No line on this quote yet, with Add a product.
- Loading: skeleton rows in place of the list ([C-03](../../../../04-ux/design-system/components/c-03-data-table.md));
  actions are disabled until it has loaded.
- Error: the error message pattern (D122).
- Read-only: sent, signed or posted documents, changed only by a new version, a credit note or an amendment.
- Offline: Works offline on the phone for orders and quotes taken on the road,
  [UC-F6-21](../../use-cases/09-sell-on-the-road-and-steer-sales/uc-f06-21-take-orders-offline-on-the-road.md), the
  customer list, price lists and stock loaded before leaving stay on the phone; new lines wait in a queue and are priced
  and checked again when the network is back.

Shown entities (VD-15): [E-F6-03 Quote](../../data/e-f06-03-quote.md),
[E-F6-08 Sales price list](../../data/e-f06-08-sales-price-list.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F6-03 Quote | Draft | Badge "Draft"; a new record starts here; next: To approve or Refused (UC-F6-03); fields editable within the role | U03 | `u03-sales/s-f06-03-quote-editor-e-f06-03-quote-draft-{desktop,phone,tablet}-{light,dark}.png` |
| E-F6-03 Quote | To approve | Badge "To approve"; next: Sent, Refused or Expired (UC-F11-27, UC-F6-03, UC-F6-04); fields editable within the role | U03 | `u03-sales/s-f06-03-quote-editor-e-f06-03-quote-to-approve-{desktop,phone,tablet}-{light,dark}.png` |
| E-F6-03 Quote | Refused | Badge "Refused"; final: read-only, no next state; the history shows how it got here | U03 | `u03-sales/s-f06-03-quote-editor-e-f06-03-quote-refused-{desktop,phone,tablet}-{light,dark}.png` |
| E-F6-03 Quote | Sent | Badge "Sent"; next: Accepted, Refused or Expired (UC-F11-27, UC-F6-03, UC-F6-04); fields editable within the role | U03 | `u03-sales/s-f06-03-quote-editor-e-f06-03-quote-sent-{desktop,phone,tablet}-{light,dark}.png` |
| E-F6-03 Quote | Expired | Badge "Expired"; final: read-only, no next state; the history shows how it got here | U03 | `u03-sales/s-f06-03-quote-editor-e-f06-03-quote-expired-{desktop,phone,tablet}-{light,dark}.png` |
| E-F6-03 Quote | Accepted | Badge "Accepted"; next: Expired (UC-F6-04); fields editable within the role | U03 | `u03-sales/s-f06-03-quote-editor-e-f06-03-quote-accepted-{desktop,phone,tablet}-{light,dark}.png` |
| E-F6-08 Sales price list | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U03 | `u03-sales/s-f06-03-quote-editor-e-f06-08-sales-price-list-active-{desktop,phone,tablet}-{light,dark}.png` |

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

- [FL-F6-01 Lead to quote](../../flows/fl-f06-01-lead-to-quote.md)

## Open questions

None.

---

⬅️ [S-F6-02 Lead](s-f06-02-lead.md) · ⬆️ [Up](README.md) ·
➡️ [S-F6-04 Customer portal](../02-quote-to-order/s-f06-04-customer-portal.md)
