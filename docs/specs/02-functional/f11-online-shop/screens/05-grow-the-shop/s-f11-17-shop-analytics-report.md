🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🛍️ [F11 Online shop (plugin)](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F11-05 Grow the shop](README.md) › 🖥️ S-F11-17 Shop analytics report

# 🖥️ S-F11-17 Shop analytics report

**Status:** ✅ specified

## Personas

- [U12 Marketing](../../../../01-users/personas/u12-marketing.md)
- [U13 Owner](../../../../01-users/personas/u13-owner.md)

## Purpose

Read shop analytics.

## Entry points

Online shop in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F11-05 step 3, U12 | desktop | ![FL-F11-05 step 3, U12, light](../../images/05-grow-the-shop/u12-marketing/3-analytics-desktop-light.png) | ![FL-F11-05 step 3, U12, dark](../../images/05-grow-the-shop/u12-marketing/3-analytics-desktop-dark.png) |
| FL-F11-05 step 3, U12 | phone | ![FL-F11-05 step 3, U12, light](../../images/05-grow-the-shop/u12-marketing/3-analytics-phone-light.png) | ![FL-F11-05 step 3, U12, dark](../../images/05-grow-the-shop/u12-marketing/3-analytics-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f11-17-shop-analytics-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f11-17-shop-analytics-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f11-17-shop-analytics-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f11-17-shop-analytics-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f11-17-shop-analytics-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f11-17-shop-analytics-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f11-17-shop-analytics-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f11-17-shop-analytics-offline-phone-dark.png) |

## Fields and columns

As its entities.

## Actions

As its use case's main flow.

## States

- Normal: Read shop analytics, as the wireframe shows.
- Empty: No visit in the period yet, with Change the period.
- Loading: skeleton rows in place of the list ([C-03](../../../../04-ux/design-system/components/c-03-data-table.md));
  actions are disabled until it has loaded.
- Error: the error message pattern (D122).
- Read-only: placed orders for the shopper; published pages for non-editors.
- Offline: Not available offline: a back-office screen on live, shared data (D38: only today's schedule, time and
  intervention records work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): none; no flow's Entities and screens table names an entity on this screen.

## Responsive behaviour

Desktop; approvals and receipts also on the phone.

## Accessibility

Labelled controls; amounts and states as text.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)

## Shown in

- [FL-F11-05 Grow the shop](../../flows/fl-f11-05-grow-the-shop.md)

## Open questions

None.

---

⬅️ [S-F11-16 SEO and languages](../01-build-the-shop/s-f11-16-seo-and-languages.md) · ⬆️ [Up](README.md) ·
➡️ [S-F11-18 Channels](../06-channels-and-legal/s-f11-18-channels.md)
