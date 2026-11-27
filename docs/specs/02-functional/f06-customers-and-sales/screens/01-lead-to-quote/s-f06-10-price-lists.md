🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🛒 [F6 Customers and sales](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F6-01 Lead to quote](README.md) › 🖥️ S-F6-10 Price lists

# 🖥️ S-F6-10 Price lists

**Status:** ✅ specified

## Personas

- [U02 Manager](../../../../01-users/personas/u02-manager.md)
- [U13 Owner](../../../../01-users/personas/u13-owner.md)

## Purpose

Manage price lists and discounts.

## Entry points

Sales in the menu; the portal for customers.

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F6-01 step 4, U02 | desktop | ![FL-F6-01 step 4, U02, light](../../images/01-lead-to-quote/u02-manager/4-price-lists-desktop-light.png) | ![FL-F6-01 step 4, U02, dark](../../images/01-lead-to-quote/u02-manager/4-price-lists-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f06-10-price-lists-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f06-10-price-lists-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f06-10-price-lists-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f06-10-price-lists-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f06-10-price-lists-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f06-10-price-lists-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f06-10-price-lists-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f06-10-price-lists-offline-phone-dark.png) |

## Fields and columns

As its entities.

## Actions

As its use cases' main flows.

## States

- Normal: Manage price lists and discounts, as the wireframe shows.
- Empty: No price list yet, with New price list.
- Loading: skeleton rows in place of the list ([C-03](../../../../04-ux/design-system/components/c-03-data-table.md));
  actions are disabled until it has loaded.
- Error: the error message pattern (D122).
- Read-only: sent, signed or posted documents, changed only by a new version, a credit note or an amendment.
- Offline: Not available offline: a back-office screen on live, shared data (D38: only today's schedule, time and
  intervention records work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-F6-08 Sales price list](../../data/e-f06-08-sales-price-list.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F6-08 Sales price list | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U02, U13 | `u02-manager/s-f06-10-price-lists-e-f06-08-sales-price-list-active-{desktop,phone}-{light,dark}.png`, `u13-owner/s-f06-10-price-lists-e-f06-08-sales-price-list-active-{desktop,phone}-{light,dark}.png` |

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

⬅️ [S-F6-09 Subscriptions](../04-subscriptions/s-f06-09-subscriptions.md) · ⬆️ [Up](README.md) ·
➡️ [S-F6-11 Lead scoring](../05-benchmark-additions/s-f06-11-lead-scoring.md)
