🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🛍️ [F11 Online shop (plugin)](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F11-05 Grow the shop](README.md) › 🖥️ S-F11-20 Shop assistant

# 🖥️ S-F11-20 Shop assistant

**Status:** ✅ specified

## Personas

- [U12 Marketing](../../../../01-users/personas/u12-marketing.md)
- [U03 Sales](../../../../01-users/personas/u03-sales.md)

## Purpose

Ask the AI assistant about the shop.

## Entry points

Online shop in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F11-05 step 4, U12 | desktop | ![FL-F11-05 step 4, U12, light](../../images/05-grow-the-shop/u12-marketing/4-assistant-desktop-light.png) | ![FL-F11-05 step 4, U12, dark](../../images/05-grow-the-shop/u12-marketing/4-assistant-desktop-dark.png) |
| FL-F11-05 step 4, U12 | phone | ![FL-F11-05 step 4, U12, light](../../images/05-grow-the-shop/u12-marketing/4-assistant-phone-light.png) | ![FL-F11-05 step 4, U12, dark](../../images/05-grow-the-shop/u12-marketing/4-assistant-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f11-20-shop-assistant-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f11-20-shop-assistant-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f11-20-shop-assistant-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f11-20-shop-assistant-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f11-20-shop-assistant-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f11-20-shop-assistant-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f11-20-shop-assistant-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f11-20-shop-assistant-offline-phone-dark.png) |

## Fields and columns

As its entities.

## Actions

As its use case's main flow.

## States

- Normal: Ask the AI assistant about the shop, as the wireframe shows.
- Empty: No question yet, with Ask a question.
- Loading: skeleton rows in place of the list ([C-03](../../../../04-ux/design-system/components/c-03-data-table.md));
  actions are disabled until it has loaded.
- Error: the error message pattern (D122).
- Read-only: placed orders for the shopper; published pages for non-editors.
- Offline: The AI assistant says it is offline; questions are queued and answered when the network is back, with a
  notification, and changes still need confirmation then
  ([D182](../../../../06-decisions/f03-assistant/d182-offline-assistant.md)).

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

⬅️ [S-F11-19 Legal pages](../06-channels-and-legal/s-f11-19-legal-pages.md) · ⬆️ [Up](README.md) ·
➡️ [S-F11-21 Order risk](../07-payment-risk/s-f11-21-order-risk.md)
