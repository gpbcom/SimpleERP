🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🛍️ [F11 Online shop (plugin)](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F11-02 Shop and check out](README.md) › 🖥️ S-F11-06 Payment

# 🖥️ S-F11-06 Payment

**Status:** ✅ specified

## Personas

- [U09 Customer](../../../../01-users/personas/u09-customer.md)

## Purpose

Pay online.

## Entry points

Online shop in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F11-02 step 3, U09 | phone | ![FL-F11-02 step 3, U09, light](../../images/02-shop-and-check-out/u09-customer/3-payment-phone-light.png) | ![FL-F11-02 step 3, U09, dark](../../images/02-shop-and-check-out/u09-customer/3-payment-phone-dark.png) |
| Error E1, U09 | phone | ![Error E1, U09, light](../../images/02-shop-and-check-out/u09-customer/e1-payment-refused-phone-light.png) | ![Error E1, U09, dark](../../images/02-shop-and-check-out/u09-customer/e1-payment-refused-phone-dark.png) |
| Error E1, U09 | phone | ![Error E1, U09, light](../../images/07-payment-risk/u09-customer/e1-payment-refused-phone-light.png) | ![Error E1, U09, dark](../../images/07-payment-risk/u09-customer/e1-payment-refused-phone-dark.png) |
| Empty | phone | ![Empty, light](../../images/states/s-f11-06-payment-empty-phone-light.png) | ![Empty, dark](../../images/states/s-f11-06-payment-empty-phone-dark.png) |
| Loading | phone | ![Loading, light](../../images/states/s-f11-06-payment-loading-phone-light.png) | ![Loading, dark](../../images/states/s-f11-06-payment-loading-phone-dark.png) |
| Read-only | phone | ![Read-only, light](../../images/states/s-f11-06-payment-read-only-phone-light.png) | ![Read-only, dark](../../images/states/s-f11-06-payment-read-only-phone-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f11-06-payment-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f11-06-payment-offline-phone-dark.png) |

## Fields and columns

As its entities.

## Actions

As its use case's main flow.

## States

- Normal: Pay online, as the wireframe shows.
- Empty: No payment means set up yet, with Set up payments.
- Loading: skeleton rows in place of the list ([C-03](../../../../04-ux/design-system/components/c-03-data-table.md));
  actions are disabled until it has loaded.
- Error: the error message pattern (D122).
- Read-only: placed orders for the shopper; published pages for non-editors.
- Offline: Not available offline: an outside user's page served live (D407 keeps portals and website apart from the
  offline-first app); the browser shows that the page cannot be reached.

Shown entities (VD-15): [E-F11-05 Checkout](../../data/e-f11-05-checkout.md),
[E-F11-16 Fraud check](../../data/e-f11-16-fraud-check.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F11-05 Checkout | Recorded | Badge "Recorded"; a new record starts here; no other state; fields editable within the role | U09 | `u09-customer/s-f11-06-payment-e-f11-05-checkout-recorded-phone-{light,dark}.png` |
| E-F11-16 Fraud check | Accepted | Badge "Accepted"; a new record starts here; next: Held (UC-F11-21); fields editable within the role | U09 | `u09-customer/s-f11-06-payment-e-f11-16-fraud-check-accepted-phone-{light,dark}.png` |

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

- [FL-F11-02 Shop and check out](../../flows/fl-f11-02-shop-and-check-out.md)
- [FL-F11-07 Payment risk](../../flows/fl-f11-07-payment-risk.md)

## Open questions

None.

---

⬅️ [S-F11-05 Checkout](s-f11-05-checkout.md) · ⬆️ [Up](README.md) ·
➡️ [S-F11-07 Delivery options](s-f11-07-delivery-options.md)
