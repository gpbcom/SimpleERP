🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🛍️ [F11 Online shop (plugin)](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F11-01 Build the shop](README.md) › 🖥️ S-F11-02 Catalogue

# 🖥️ S-F11-02 Catalogue

**Status:** ✅ specified

## Personas

- [U12 Marketing](../../../../01-users/personas/u12-marketing.md)

## Purpose

Publish the catalogue.

## Entry points

Online shop in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F11-01 step 2, U12 | desktop | ![FL-F11-01 step 2, U12, light](../../images/01-build-the-shop/u12-marketing/2-catalogue-desktop-light.png) | ![FL-F11-01 step 2, U12, dark](../../images/01-build-the-shop/u12-marketing/2-catalogue-desktop-dark.png) |
| FL-F11-01 step 2, U12 | phone | ![FL-F11-01 step 2, U12, light](../../images/01-build-the-shop/u12-marketing/2-catalogue-phone-light.png) | ![FL-F11-01 step 2, U12, dark](../../images/01-build-the-shop/u12-marketing/2-catalogue-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f11-02-catalogue-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f11-02-catalogue-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f11-02-catalogue-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f11-02-catalogue-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f11-02-catalogue-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f11-02-catalogue-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f11-02-catalogue-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f11-02-catalogue-offline-phone-dark.png) |

## Fields and columns

As its entities.

## Actions

As its use case's main flow.

## States

- Normal: Publish the catalogue, as the wireframe shows.
- Empty: No published product yet, with Publish a product.
- Loading: skeleton rows in place of the list ([C-03](../../../../04-ux/design-system/components/c-03-data-table.md));
  actions are disabled until it has loaded.
- Error: the error message pattern (D122).
- Read-only: placed orders for the shopper; published pages for non-editors.
- Offline: Not available offline: a back-office screen on live, shared data (D38: only today's schedule, time and
  intervention records work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-F11-03 Online product](../../data/e-f11-03-online-product.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F11-03 Online product | New | Badge "New"; a new record starts here; next: Published (UC-F11-02); fields editable within the role | U12 | `u12-marketing/s-f11-02-catalogue-e-f11-03-online-product-new-{desktop,phone}-{light,dark}.png` |
| E-F11-03 Online product | Published | Badge "Published"; next: Delivered (UC-F11-13); fields editable within the role | U12 | `u12-marketing/s-f11-02-catalogue-e-f11-03-online-product-published-{desktop,phone}-{light,dark}.png` |
| E-F11-03 Online product | Delivered | Badge "Delivered"; next: Complete (UC-F11-23); fields editable within the role | U12 | `u12-marketing/s-f11-02-catalogue-e-f11-03-online-product-delivered-{desktop,phone}-{light,dark}.png` |
| E-F11-03 Online product | Complete | Badge "Complete"; final: read-only, no next state; the history shows how it got here | U12 | `u12-marketing/s-f11-02-catalogue-e-f11-03-online-product-complete-{desktop,phone}-{light,dark}.png` |

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

- [FL-F11-01 Build the shop](../../flows/fl-f11-01-build-the-shop.md)

## Open questions

None.

---

⬅️ [S-F11-01 Website editor](s-f11-01-website-editor.md) · ⬆️ [Up](README.md) ·
➡️ [S-F11-03 Online prices](s-f11-03-online-prices.md)
