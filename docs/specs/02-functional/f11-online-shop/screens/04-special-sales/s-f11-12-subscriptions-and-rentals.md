🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🛍️ [F11 Online shop (plugin)](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F11-04 B2B, subscriptions, rentals and digital](README.md) › 🖥️ S-F11-12 Subscriptions and rentals

# 🖥️ S-F11-12 Subscriptions and rentals

**Status:** ✅ specified

## Personas

- [U09 Customer](../../../../01-users/personas/u09-customer.md)
- [U12 Marketing](../../../../01-users/personas/u12-marketing.md)

## Purpose

Sell subscriptions and rentals online.

## Entry points

Online shop in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F11-04 step 2, U09 | phone | ![FL-F11-04 step 2, U09, light](../../images/04-special-sales/u09-customer/2-subscription-rental-phone-light.png) | ![FL-F11-04 step 2, U09, dark](../../images/04-special-sales/u09-customer/2-subscription-rental-phone-dark.png) |
| Empty | phone | ![Empty, light](../../images/states/s-f11-12-subscriptions-and-rentals-empty-phone-light.png) | ![Empty, dark](../../images/states/s-f11-12-subscriptions-and-rentals-empty-phone-dark.png) |
| Loading | phone | ![Loading, light](../../images/states/s-f11-12-subscriptions-and-rentals-loading-phone-light.png) | ![Loading, dark](../../images/states/s-f11-12-subscriptions-and-rentals-loading-phone-dark.png) |
| Read-only | phone | ![Read-only, light](../../images/states/s-f11-12-subscriptions-and-rentals-read-only-phone-light.png) | ![Read-only, dark](../../images/states/s-f11-12-subscriptions-and-rentals-read-only-phone-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f11-12-subscriptions-and-rentals-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f11-12-subscriptions-and-rentals-offline-phone-dark.png) |

## Fields and columns

As its entities.

## Actions

As its use case's main flow.

## States

- Normal: Sell subscriptions and rentals online, as the wireframe shows.
- Empty: No subscription or rental yet, with Browse plans.
- Loading: skeleton rows in place of the list ([C-03](../../../../04-ux/design-system/components/c-03-data-table.md));
  actions are disabled until it has loaded.
- Error: the error message pattern (D122).
- Read-only: placed orders for the shopper; published pages for non-editors.
- Offline: Not available offline: an outside user's page served live (D407 keeps portals and website apart from the
  offline-first app); the browser shows that the page cannot be reached.

Shown entities (VD-15): [E-F11-03 Online product](../../data/e-f11-03-online-product.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F11-03 Online product | New | Badge "New"; a new record starts here; next: Published (UC-F11-02); fields editable within the role | U09, U12 | `u09-customer/s-f11-12-subscriptions-and-rentals-e-f11-03-online-product-new-phone-{light,dark}.png`, `u12-marketing/s-f11-12-subscriptions-and-rentals-e-f11-03-online-product-new-{desktop,phone}-{light,dark}.png` |
| E-F11-03 Online product | Published | Badge "Published"; next: Delivered (UC-F11-13); fields editable within the role | U09, U12 | `u09-customer/s-f11-12-subscriptions-and-rentals-e-f11-03-online-product-published-phone-{light,dark}.png`, `u12-marketing/s-f11-12-subscriptions-and-rentals-e-f11-03-online-product-published-{desktop,phone}-{light,dark}.png` |
| E-F11-03 Online product | Delivered | Badge "Delivered"; next: Complete (UC-F11-23); fields editable within the role | U09, U12 | `u09-customer/s-f11-12-subscriptions-and-rentals-e-f11-03-online-product-delivered-phone-{light,dark}.png`, `u12-marketing/s-f11-12-subscriptions-and-rentals-e-f11-03-online-product-delivered-{desktop,phone}-{light,dark}.png` |
| E-F11-03 Online product | Complete | Badge "Complete"; final: read-only, no next state; the history shows how it got here | U09, U12 | `u09-customer/s-f11-12-subscriptions-and-rentals-e-f11-03-online-product-complete-phone-{light,dark}.png`, `u12-marketing/s-f11-12-subscriptions-and-rentals-e-f11-03-online-product-complete-{desktop,phone}-{light,dark}.png` |

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

- [FL-F11-04 B2B, subscriptions, rentals and digital](../../flows/fl-f11-04-special-sales.md)

## Open questions

None.

---

⬅️ [S-F11-11 B2B access](s-f11-11-b2b-access.md) · ⬆️ [Up](README.md) ·
➡️ [S-F11-13 Digital products](s-f11-13-digital-products.md)
