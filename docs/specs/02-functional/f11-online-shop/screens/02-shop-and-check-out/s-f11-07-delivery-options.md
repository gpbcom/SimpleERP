🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🛍️ [F11 Online shop (plugin)](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F11-02 Shop and check out](README.md) › 🖥️ S-F11-07 Delivery options

# 🖥️ S-F11-07 Delivery options

**Status:** ✅ specified

## Personas

- [U09 Customer](../../../../01-users/personas/u09-customer.md)
- [U15 Warehouse operator](../../../../01-users/personas/u15-warehouse-operator.md)

## Purpose

Choose delivery or click & collect.

## Entry points

Online shop in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F11-02 step 4, U09 | phone | ![FL-F11-02 step 4, U09, light](../../images/02-shop-and-check-out/u09-customer/4-delivery-or-pickup-phone-light.png) | ![FL-F11-02 step 4, U09, dark](../../images/02-shop-and-check-out/u09-customer/4-delivery-or-pickup-phone-dark.png) |
| Empty | phone | ![Empty, light](../../images/states/s-f11-07-delivery-options-empty-phone-light.png) | ![Empty, dark](../../images/states/s-f11-07-delivery-options-empty-phone-dark.png) |
| Loading | phone | ![Loading, light](../../images/states/s-f11-07-delivery-options-loading-phone-light.png) | ![Loading, dark](../../images/states/s-f11-07-delivery-options-loading-phone-dark.png) |
| Read-only | phone | ![Read-only, light](../../images/states/s-f11-07-delivery-options-read-only-phone-light.png) | ![Read-only, dark](../../images/states/s-f11-07-delivery-options-read-only-phone-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f11-07-delivery-options-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f11-07-delivery-options-offline-phone-dark.png) |

## Fields and columns

As its entities.

## Actions

As its use case's main flow.

## States

- Normal: Choose delivery or click & collect, as the wireframe shows.
- Empty: No delivery method for this address yet, with Change the address.
- Loading: skeleton rows in place of the list ([C-03](../../../../04-ux/design-system/components/c-03-data-table.md));
  actions are disabled until it has loaded.
- Error: the error message pattern (D122).
- Read-only: placed orders for the shopper; published pages for non-editors.
- Offline: Not available offline: an outside user's page served live (D407 keeps portals and website apart from the
  offline-first app); the browser shows that the page cannot be reached.

Shown entities (VD-15): [E-F11-07 Delivery method](../../data/e-f11-07-delivery-method.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F11-07 Delivery method | Recorded | Badge "Recorded"; a new record starts here; no other state; fields editable within the role | U09, U15 | `u09-customer/s-f11-07-delivery-options-e-f11-07-delivery-method-recorded-phone-{light,dark}.png`, `u15-warehouse-operator/s-f11-07-delivery-options-e-f11-07-delivery-method-recorded-{phone,tablet}-{light,dark}.png` |

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

## Open questions

None.

---

⬅️ [S-F11-06 Payment](s-f11-06-payment.md) · ⬆️ [Up](README.md) ·
➡️ [S-F11-08 Order confirmation](s-f11-08-order-confirmation.md)
