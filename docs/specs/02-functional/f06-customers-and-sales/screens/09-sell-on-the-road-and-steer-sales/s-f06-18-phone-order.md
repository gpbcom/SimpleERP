🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🛒 [F6 Customers and sales](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F6-09 Sell on the road and steer sales](README.md) › 🖥️ S-F6-18 Phone order

# 🖥️ S-F6-18 Phone order

**Status:** ✅ specified

## Personas

- [U42 Sales representative](../../../../01-users/personas/u42-sales-representative.md)
- [U03 Sales](../../../../01-users/personas/u03-sales.md)

## Purpose

Take an order on the phone, online or offline.

## Entry points

The rep's app › a customer › New order.

## Wireframe

```text
+----------------------------+
| Offline · 1 order waiting  |
| Brasserie du Parc          |
| [search catalogue]         |
| Beer 33cl x24   12 x 12.40 |
| Water 1L x6     20 x 3.10  |
| Total excl. VAT  210.80    |
| [Signature]  [Save order]  |
+----------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F6-09 step 1, U42 | desktop | ![FL-F6-09 step 1, U42, light](../../images/09-sell-on-the-road-and-steer-sales/u42-sales-representative/1-phone-order-desktop-light.png) | ![FL-F6-09 step 1, U42, dark](../../images/09-sell-on-the-road-and-steer-sales/u42-sales-representative/1-phone-order-desktop-dark.png) |
| FL-F6-09 step 1, U42 | phone | ![FL-F6-09 step 1, U42, light](../../images/09-sell-on-the-road-and-steer-sales/u42-sales-representative/1-phone-order-phone-light.png) | ![FL-F6-09 step 1, U42, dark](../../images/09-sell-on-the-road-and-steer-sales/u42-sales-representative/1-phone-order-phone-dark.png) |
| FL-F6-09 step 1, U42 | tablet | ![FL-F6-09 step 1, U42, light](../../images/09-sell-on-the-road-and-steer-sales/u42-sales-representative/1-phone-order-tablet-light.png) | ![FL-F6-09 step 1, U42, dark](../../images/09-sell-on-the-road-and-steer-sales/u42-sales-representative/1-phone-order-tablet-dark.png) |
| Error E1, U42 | desktop | ![Error E1, U42, light](../../images/09-sell-on-the-road-and-steer-sales/u42-sales-representative/e1-phone-order-refused-desktop-light.png) | ![Error E1, U42, dark](../../images/09-sell-on-the-road-and-steer-sales/u42-sales-representative/e1-phone-order-refused-desktop-dark.png) |
| Error E1, U42 | phone | ![Error E1, U42, light](../../images/09-sell-on-the-road-and-steer-sales/u42-sales-representative/e1-phone-order-refused-phone-light.png) | ![Error E1, U42, dark](../../images/09-sell-on-the-road-and-steer-sales/u42-sales-representative/e1-phone-order-refused-phone-dark.png) |
| Error E1, U42 | tablet | ![Error E1, U42, light](../../images/09-sell-on-the-road-and-steer-sales/u42-sales-representative/e1-phone-order-refused-tablet-light.png) | ![Error E1, U42, dark](../../images/09-sell-on-the-road-and-steer-sales/u42-sales-representative/e1-phone-order-refused-tablet-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f06-18-phone-order-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f06-18-phone-order-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f06-18-phone-order-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f06-18-phone-order-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f06-18-phone-order-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f06-18-phone-order-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f06-18-phone-order-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f06-18-phone-order-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Editable |
|---|---|---|
| Customer, lines, prices, signature | E-F6-04 | yes |

## Actions

| Action | Who | Result |
|---|---|---|
| Save | representative | Queued or confirmed |
| Accept differences | representative | After sync |

## States

- Normal: take an order on the phone, online or offline.
- Empty: no line yet: Search the catalogue or scan.
- Loading: the catalogue greyed while it loads from the phone's store.
- Error: the error message pattern (D122).
- Read-only: confirmed orders.
- Offline: Works offline: customers, price lists and stock loaded before leaving stay on the phone; orders wait in a
  queue and are priced and checked again on sync
  ([BR-F6-14](../../business-rules/br-f06-14-offline-orders-are-checked-again-on-sync.md)).

Shown entities (VD-15): [E-F6-04 Order](../../data/e-f06-04-order.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F6-04 Order | Open | Badge "Open"; a new record starts here; next: In progress or Cancelled (UC-F6-05); fields editable within the role | U42 | `u42-sales-representative/s-f06-18-phone-order-e-f06-04-order-open-{desktop,phone,tablet}-{light,dark}.png` |
| E-F6-04 Order | In progress | Badge "In progress"; next: Done or Cancelled (UC-F6-05); fields editable within the role | U42 | `u42-sales-representative/s-f06-18-phone-order-e-f06-04-order-in-progress-{desktop,phone,tablet}-{light,dark}.png` |
| E-F6-04 Order | Cancelled | Badge "Cancelled"; final: read-only, no next state; the history shows how it got here | U42 | `u42-sales-representative/s-f06-18-phone-order-e-f06-04-order-cancelled-{desktop,phone,tablet}-{light,dark}.png` |
| E-F6-04 Order | Done | Badge "Done"; final: read-only, no next state; the history shows how it got here | U42 | `u42-sales-representative/s-f06-18-phone-order-e-f06-04-order-done-{desktop,phone,tablet}-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Phone and tablet.

## Accessibility

Every status is a word, not only a colour; tables have headers; actions are buttons with labels.

## Components

- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)
- [C-04 Card](../../../../04-ux/design-system/components/c-04-card.md)
- [C-01 Button](../../../../04-ux/design-system/components/c-01-button.md)

## Shown in

- [FL-F6-09 Sell on the road and steer sales](../../flows/fl-f06-09-sell-on-the-road-and-steer-sales.md)

## Open questions

None.

---

⬅️ [S-F6-17 Funders and caps](../07-special-invoicing/s-f06-17-funders-and-caps.md) · ⬆️ [Up](README.md) ·
➡️ [S-F6-19 Statement of account](../07-special-invoicing/s-f06-19-statement-of-account.md)
