🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🛍️ [F11 Online shop (plugin)](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F11-09 Pre-orders and B2B buying](README.md) › 🖥️ S-F11-26 Pre-order

# 🖥️ S-F11-26 Pre-order

**Status:** ✅ specified

## Personas

- [U09 Customer](../../../../01-users/personas/u09-customer.md)
- [U12 Marketing and communication](../../../../01-users/personas/u12-marketing.md)

## Purpose

Let shoppers pre-order or reserve items not in stock; set pre-orders.

## Entry points

The product page (shoppers); Shop › Pre-orders (marketing).

## Wireframe

```text
Product page (phone)
  Spring jacket   89 EUR
  Ships around 2027-02-15
  [Pre-order: pay 30 % now]
  Sold out in 40: [Reserve when back]
Marketing: Pre-orders  Spring jacket  64 open  date [2027-02-15]
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F11-09 step 1, U09 | phone | ![FL-F11-09 step 1, U09, light](../../images/09-pre-orders-and-b2b-buying/u09-customer/1-pre-order-phone-light.png) | ![FL-F11-09 step 1, U09, dark](../../images/09-pre-orders-and-b2b-buying/u09-customer/1-pre-order-phone-dark.png) |
| Error E1, U09 | phone | ![Error E1, U09, light](../../images/09-pre-orders-and-b2b-buying/u09-customer/e1-pre-order-refused-phone-light.png) | ![Error E1, U09, dark](../../images/09-pre-orders-and-b2b-buying/u09-customer/e1-pre-order-refused-phone-dark.png) |
| Empty | phone | ![Empty, light](../../images/states/s-f11-26-pre-order-empty-phone-light.png) | ![Empty, dark](../../images/states/s-f11-26-pre-order-empty-phone-dark.png) |
| Loading | phone | ![Loading, light](../../images/states/s-f11-26-pre-order-loading-phone-light.png) | ![Loading, dark](../../images/states/s-f11-26-pre-order-loading-phone-dark.png) |
| Read-only | phone | ![Read-only, light](../../images/states/s-f11-26-pre-order-read-only-phone-light.png) | ![Read-only, dark](../../images/states/s-f11-26-pre-order-read-only-phone-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f11-26-pre-order-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f11-26-pre-order-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Editable |
|---|---|---|
| Date, payment, open pre-orders | E-F11-21 | date (marketing) |

## Actions

| Action | Who | Result |
|---|---|---|
| Pre-order | shoppers | Pre-order recorded |
| Reserve | shoppers | Told when back |

## States

- Normal: let shoppers pre-order or reserve items not in stock; set pre-orders.
- Empty: no pre-order open: the page shows Sold out and Reserve.
- Loading: skeleton rows in place of the list ([C-03](../../../../04-ux/design-system/components/c-03-data-table.md));
  actions disabled until it has loaded.
- Error: the error message pattern (D122).
- Read-only: shipped pre-orders.
- Offline: Not available offline: the shop is served live
  ([D407](../../../../06-decisions/technical/d407-front-end.md)).

Shown entities (VD-15): [E-F11-21 Pre-order and reservation](../../data/e-f11-21-pre-order-and-reservation.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F11-21 Pre-order and reservation | Open | Badge "Open"; a new record starts here; next: Shipped, Held or Cancelled (UC-F11-26); fields editable within the role | U09 | `u09-customer/s-f11-26-pre-order-e-f11-21-pre-order-and-reservation-open-phone-{light,dark}.png` |
| E-F11-21 Pre-order and reservation | Held | Badge "Held"; next: Shipped (UC-F11-26); fields editable within the role | U09 | `u09-customer/s-f11-26-pre-order-e-f11-21-pre-order-and-reservation-held-phone-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Phone and desktop.

## Accessibility

Every status is a word, not only a colour; tables have headers; actions are buttons with labels.

## Components

- [C-04 Card](../../../../04-ux/design-system/components/c-04-card.md)
- [C-01 Button](../../../../04-ux/design-system/components/c-01-button.md)

## Shown in

- [FL-F11-09 Pre-orders and B2B buying](../../flows/fl-f11-09-pre-orders-and-b2b-buying.md)

## Open questions

None.

---

⬅️ [S-F11-25 Product safety](../08-product-content-and-listings/s-f11-25-product-safety.md) · ⬆️ [Up](README.md) ·
➡️ [S-F11-27 Store fulfilment](../10-fulfil-from-stores-and-report/s-f11-27-store-fulfilment.md)
