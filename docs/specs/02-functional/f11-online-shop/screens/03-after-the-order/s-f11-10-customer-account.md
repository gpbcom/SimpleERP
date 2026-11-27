🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🛍️ [F11 Online shop (plugin)](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F11-03 After the order](README.md) › 🖥️ S-F11-10 Customer account

# 🖥️ S-F11-10 Customer account

**Status:** ✅ specified

## Personas

- [U09 Customer](../../../../01-users/personas/u09-customer.md)

## Purpose

Use the customer account.

## Entry points

Online shop in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F11-03 step 4, U09 | phone | ![FL-F11-03 step 4, U09, light](../../images/03-after-the-order/u09-customer/4-customer-account-phone-light.png) | ![FL-F11-03 step 4, U09, dark](../../images/03-after-the-order/u09-customer/4-customer-account-phone-dark.png) |
| Empty | phone | ![Empty, light](../../images/states/s-f11-10-customer-account-empty-phone-light.png) | ![Empty, dark](../../images/states/s-f11-10-customer-account-empty-phone-dark.png) |
| Loading | phone | ![Loading, light](../../images/states/s-f11-10-customer-account-loading-phone-light.png) | ![Loading, dark](../../images/states/s-f11-10-customer-account-loading-phone-dark.png) |
| Read-only | phone | ![Read-only, light](../../images/states/s-f11-10-customer-account-read-only-phone-light.png) | ![Read-only, dark](../../images/states/s-f11-10-customer-account-read-only-phone-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f11-10-customer-account-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f11-10-customer-account-offline-phone-dark.png) |

## Fields and columns

As its entities.

## Actions

As its use case's main flow.

## States

- Normal: Use the customer account, as the wireframe shows.
- Empty: No order yet, with Start shopping.
- Loading: skeleton rows in place of the list ([C-03](../../../../04-ux/design-system/components/c-03-data-table.md));
  actions are disabled until it has loaded.
- Error: the error message pattern (D122).
- Read-only: placed orders for the shopper; published pages for non-editors.
- Offline: Not available offline: an outside user's page served live (D407 keeps portals and website apart from the
  offline-first app); the browser shows that the page cannot be reached.

Shown entities (VD-15): none; no flow's Entities and screens table names an entity on this screen.

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

⬅️ [S-F11-09 Withdrawal](s-f11-09-withdrawal.md) · ⬆️ [Up](README.md) ·
➡️ [S-F11-11 B2B access](../04-special-sales/s-f11-11-b2b-access.md)
