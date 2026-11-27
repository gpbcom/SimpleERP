🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🛍️ [F11 Online shop (plugin)](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F11-01 Build the shop](README.md) › 🖥️ S-F11-03 Online prices

# 🖥️ S-F11-03 Online prices

**Status:** ✅ specified

## Personas

- [U12 Marketing](../../../../01-users/personas/u12-marketing.md)
- [U03 Sales](../../../../01-users/personas/u03-sales.md)

## Purpose

Set online prices and promotions.

## Entry points

Online shop in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F11-01 step 3, U12 | desktop | ![FL-F11-01 step 3, U12, light](../../images/01-build-the-shop/u12-marketing/3-prices-desktop-light.png) | ![FL-F11-01 step 3, U12, dark](../../images/01-build-the-shop/u12-marketing/3-prices-desktop-dark.png) |
| FL-F11-01 step 3, U12 | phone | ![FL-F11-01 step 3, U12, light](../../images/01-build-the-shop/u12-marketing/3-prices-phone-light.png) | ![FL-F11-01 step 3, U12, dark](../../images/01-build-the-shop/u12-marketing/3-prices-phone-dark.png) |
| Error E1, U12 | desktop | ![Error E1, U12, light](../../images/01-build-the-shop/u12-marketing/e1-reduction-without-reference-desktop-light.png) | ![Error E1, U12, dark](../../images/01-build-the-shop/u12-marketing/e1-reduction-without-reference-desktop-dark.png) |
| Error E1, U12 | phone | ![Error E1, U12, light](../../images/01-build-the-shop/u12-marketing/e1-reduction-without-reference-phone-light.png) | ![Error E1, U12, dark](../../images/01-build-the-shop/u12-marketing/e1-reduction-without-reference-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f11-03-online-prices-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f11-03-online-prices-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f11-03-online-prices-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f11-03-online-prices-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f11-03-online-prices-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f11-03-online-prices-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f11-03-online-prices-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f11-03-online-prices-offline-phone-dark.png) |

## Fields and columns

As its entities.

## Actions

As its use case's main flow.

## States

- Normal: Set online prices and promotions, as the wireframe shows.
- Empty: No online price or promotion yet, with New promotion.
- Loading: skeleton rows in place of the list ([C-03](../../../../04-ux/design-system/components/c-03-data-table.md));
  actions are disabled until it has loaded.
- Error: the error message pattern (D122).
- Read-only: placed orders for the shopper; published pages for non-editors.
- Offline: Not available offline: a back-office screen on live, shared data (D38: only today's schedule, time and
  intervention records work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-F11-11 Online promotion code](../../data/e-f11-11-online-promotion-code.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F11-11 Online promotion code | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U03, U12 | `u03-sales/s-f11-03-online-prices-e-f11-11-online-promotion-code-active-{desktop,phone,tablet}-{light,dark}.png`, `u12-marketing/s-f11-03-online-prices-e-f11-11-online-promotion-code-active-{desktop,phone}-{light,dark}.png` |

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

⬅️ [S-F11-02 Catalogue](s-f11-02-catalogue.md) · ⬆️ [Up](README.md) ·
➡️ [S-F11-04 Shop](../02-shop-and-check-out/s-f11-04-shop.md)
