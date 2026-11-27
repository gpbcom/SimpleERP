🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🛍️ [F11 Online shop (plugin)](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F11-03 After the order](README.md) › 🖥️ S-F11-09 Withdrawal

# 🖥️ S-F11-09 Withdrawal

**Status:** ✅ specified

## Personas

- [U09 Customer](../../../../01-users/personas/u09-customer.md)
- [U03 Sales](../../../../01-users/personas/u03-sales.md)

## Purpose

Withdraw, return and refund.

## Entry points

Online shop in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F11-03 step 1, U09 | phone | ![FL-F11-03 step 1, U09, light](../../images/03-after-the-order/u09-customer/1-account-phone-light.png) | ![FL-F11-03 step 1, U09, dark](../../images/03-after-the-order/u09-customer/1-account-phone-dark.png) |
| Error E1, U09 | phone | ![Error E1, U09, light](../../images/03-after-the-order/u09-customer/e1-excluded-product-phone-light.png) | ![Error E1, U09, dark](../../images/03-after-the-order/u09-customer/e1-excluded-product-phone-dark.png) |
| Empty | phone | ![Empty, light](../../images/states/s-f11-09-withdrawal-empty-phone-light.png) | ![Empty, dark](../../images/states/s-f11-09-withdrawal-empty-phone-dark.png) |
| Loading | phone | ![Loading, light](../../images/states/s-f11-09-withdrawal-loading-phone-light.png) | ![Loading, dark](../../images/states/s-f11-09-withdrawal-loading-phone-dark.png) |
| Read-only | phone | ![Read-only, light](../../images/states/s-f11-09-withdrawal-read-only-phone-light.png) | ![Read-only, dark](../../images/states/s-f11-09-withdrawal-read-only-phone-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f11-09-withdrawal-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f11-09-withdrawal-offline-phone-dark.png) |

## Fields and columns

As its entities.

## Actions

As its use case's main flow.

## States

- Normal: Withdraw, return and refund, as the wireframe shows.
- Empty: No order that can be withdrawn yet, with See my orders.
- Loading: skeleton rows in place of the list ([C-03](../../../../04-ux/design-system/components/c-03-data-table.md));
  actions are disabled until it has loaded.
- Error: the error message pattern (D122).
- Read-only: placed orders for the shopper; published pages for non-editors.
- Offline: Not available offline: an outside user's page served live (D407 keeps portals and website apart from the
  offline-first app); the browser shows that the page cannot be reached.

Shown entities (VD-15): [E-F11-08 Withdrawal request](../../data/e-f11-08-withdrawal-request.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F11-08 Withdrawal request | Received | Badge "Received"; a new record starts here; next: Acknowledged (UC-F11-09); fields editable within the role | U03, U09 | `u03-sales/s-f11-09-withdrawal-e-f11-08-withdrawal-request-received-{desktop,phone,tablet}-{light,dark}.png`, `u09-customer/s-f11-09-withdrawal-e-f11-08-withdrawal-request-received-phone-{light,dark}.png` |
| E-F11-08 Withdrawal request | Acknowledged | Badge "Acknowledged"; next: Returned (UC-F11-09); fields editable within the role | U03, U09 | `u03-sales/s-f11-09-withdrawal-e-f11-08-withdrawal-request-acknowledged-{desktop,phone,tablet}-{light,dark}.png`, `u09-customer/s-f11-09-withdrawal-e-f11-08-withdrawal-request-acknowledged-phone-{light,dark}.png` |
| E-F11-08 Withdrawal request | Returned | Badge "Returned"; next: Refunded (UC-F11-09); fields editable within the role | U03, U09 | `u03-sales/s-f11-09-withdrawal-e-f11-08-withdrawal-request-returned-{desktop,phone,tablet}-{light,dark}.png`, `u09-customer/s-f11-09-withdrawal-e-f11-08-withdrawal-request-returned-phone-{light,dark}.png` |
| E-F11-08 Withdrawal request | Refunded | Badge "Refunded"; final: read-only, no next state; the history shows how it got here | U03, U09 | `u03-sales/s-f11-09-withdrawal-e-f11-08-withdrawal-request-refunded-{desktop,phone,tablet}-{light,dark}.png`, `u09-customer/s-f11-09-withdrawal-e-f11-08-withdrawal-request-refunded-phone-{light,dark}.png` |

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

- [FL-F11-03 After the order](../../flows/fl-f11-03-after-the-order.md)

## Open questions

None.

---

⬅️ [S-F11-08 Order confirmation](../02-shop-and-check-out/s-f11-08-order-confirmation.md) · ⬆️ [Up](README.md) ·
➡️ [S-F11-10 Customer account](s-f11-10-customer-account.md)
