🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🛍️ [F11 Online shop (plugin)](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F11-02 Shop and check out](README.md) › 🖥️ S-F11-04 Shop

# 🖥️ S-F11-04 Shop

**Status:** ✅ specified

## Personas

- [U09 Customer](../../../../01-users/personas/u09-customer.md)

## Purpose

Browse and search the shop.

## Entry points

Online shop in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F11-02 step 1, U09 | phone | ![FL-F11-02 step 1, U09, light](../../images/02-shop-and-check-out/u09-customer/1-browse-phone-light.png) | ![FL-F11-02 step 1, U09, dark](../../images/02-shop-and-check-out/u09-customer/1-browse-phone-dark.png) |
| Empty | phone | ![Empty, light](../../images/states/s-f11-04-shop-empty-phone-light.png) | ![Empty, dark](../../images/states/s-f11-04-shop-empty-phone-dark.png) |
| Loading | phone | ![Loading, light](../../images/states/s-f11-04-shop-loading-phone-light.png) | ![Loading, dark](../../images/states/s-f11-04-shop-loading-phone-dark.png) |
| Read-only | phone | ![Read-only, light](../../images/states/s-f11-04-shop-read-only-phone-light.png) | ![Read-only, dark](../../images/states/s-f11-04-shop-read-only-phone-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f11-04-shop-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f11-04-shop-offline-phone-dark.png) |

## Fields and columns

As its entities.

## Actions

As its use case's main flow.

## States

- Normal: Browse and search the shop, as the wireframe shows.
- Empty: No product matching the search yet, with Clear the filters.
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

- [FL-F11-02 Shop and check out](../../flows/fl-f11-02-shop-and-check-out.md)

## Open questions

None.

---

⬅️ [S-F11-03 Online prices](../01-build-the-shop/s-f11-03-online-prices.md) · ⬆️ [Up](README.md) ·
➡️ [S-F11-05 Checkout](s-f11-05-checkout.md)
