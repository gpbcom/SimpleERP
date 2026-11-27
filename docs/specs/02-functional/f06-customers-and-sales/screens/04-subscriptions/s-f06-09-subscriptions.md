🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🛒 [F6 Customers and sales](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F6-04 Subscriptions](README.md) › 🖥️ S-F6-09 Subscriptions

# 🖥️ S-F6-09 Subscriptions

**Status:** ✅ specified

## Personas

- [U03 Sales](../../../../01-users/personas/u03-sales.md)
- [U05 Accounting](../../../../01-users/personas/u05-accounting.md)

## Purpose

Manage subscriptions.

## Entry points

Sales in the menu; the portal for customers.

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F6-04 step 1, U03 | desktop | ![FL-F6-04 step 1, U03, light](../../images/04-subscriptions/u03-sales/1-subscriptions-desktop-light.png) | ![FL-F6-04 step 1, U03, dark](../../images/04-subscriptions/u03-sales/1-subscriptions-desktop-dark.png) |
| FL-F6-04 step 1, U03 | phone | ![FL-F6-04 step 1, U03, light](../../images/04-subscriptions/u03-sales/1-subscriptions-phone-light.png) | ![FL-F6-04 step 1, U03, dark](../../images/04-subscriptions/u03-sales/1-subscriptions-phone-dark.png) |
| FL-F6-04 step 1, U03 | tablet | ![FL-F6-04 step 1, U03, light](../../images/04-subscriptions/u03-sales/1-subscriptions-tablet-light.png) | ![FL-F6-04 step 1, U03, dark](../../images/04-subscriptions/u03-sales/1-subscriptions-tablet-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f06-09-subscriptions-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f06-09-subscriptions-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f06-09-subscriptions-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f06-09-subscriptions-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f06-09-subscriptions-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f06-09-subscriptions-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f06-09-subscriptions-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f06-09-subscriptions-offline-phone-dark.png) |

## Fields and columns

As its entities.

## Actions

As its use cases' main flows.

## States

- Normal: Manage subscriptions, as the wireframe shows.
- Empty: No subscription yet, with New subscription.
- Loading: skeleton rows in place of the list ([C-03](../../../../04-ux/design-system/components/c-03-data-table.md));
  actions are disabled until it has loaded.
- Error: the error message pattern (D122).
- Read-only: sent, signed or posted documents, changed only by a new version, a credit note or an amendment.
- Offline: Not available offline: a back-office screen on live, shared data (D38: only today's schedule, time and
  intervention records work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-F6-07 Subscription contract](../../data/e-f06-07-subscription-contract.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F6-07 Subscription contract | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U03, U05 | `u03-sales/s-f06-09-subscriptions-e-f06-07-subscription-contract-active-{desktop,phone,tablet}-{light,dark}.png`, `u05-accounting/s-f06-09-subscriptions-e-f06-07-subscription-contract-active-desktop-{light,dark}.png` |

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

- [FL-F6-04 Subscriptions](../../flows/fl-f06-04-subscriptions.md)

## Open questions

None.

---

⬅️ [S-F6-08 Reminders](../03-invoice-and-get-paid/s-f06-08-reminders.md) · ⬆️ [Up](README.md) ·
➡️ [S-F6-10 Price lists](../01-lead-to-quote/s-f06-10-price-lists.md)
