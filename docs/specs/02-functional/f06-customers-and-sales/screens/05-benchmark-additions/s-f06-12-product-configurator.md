🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🛒 [F6 Customers and sales](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F6-05 Benchmark additions](README.md) › 🖥️ S-F6-12 Product configurator

# 🖥️ S-F6-12 Product configurator

**Status:** ✅ specified

## Personas

- [U03 Sales](../../../../01-users/personas/u03-sales.md)

## Purpose

Configure products in a quote.

## Entry points

Customers and sales in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F6-05 step 2, U03 | desktop | ![FL-F6-05 step 2, U03, light](../../images/05-benchmark-additions/u03-sales/2-configurator-desktop-light.png) | ![FL-F6-05 step 2, U03, dark](../../images/05-benchmark-additions/u03-sales/2-configurator-desktop-dark.png) |
| FL-F6-05 step 2, U03 | phone | ![FL-F6-05 step 2, U03, light](../../images/05-benchmark-additions/u03-sales/2-configurator-phone-light.png) | ![FL-F6-05 step 2, U03, dark](../../images/05-benchmark-additions/u03-sales/2-configurator-phone-dark.png) |
| FL-F6-05 step 2, U03 | tablet | ![FL-F6-05 step 2, U03, light](../../images/05-benchmark-additions/u03-sales/2-configurator-tablet-light.png) | ![FL-F6-05 step 2, U03, dark](../../images/05-benchmark-additions/u03-sales/2-configurator-tablet-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f06-12-product-configurator-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f06-12-product-configurator-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f06-12-product-configurator-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f06-12-product-configurator-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f06-12-product-configurator-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f06-12-product-configurator-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f06-12-product-configurator-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f06-12-product-configurator-offline-phone-dark.png) |

## Fields and columns

As its entities.

## Actions

As its use case's main flow.

## States

- Normal: Configure products in a quote, as the wireframe shows.
- Empty: No configurable product yet, with Make a product configurable.
- Loading: skeleton rows in place of the list ([C-03](../../../../04-ux/design-system/components/c-03-data-table.md));
  actions are disabled until it has loaded.
- Error: the error message pattern (D122).
- Read-only: sent, signed or posted documents, changed only by a new version, a credit note or an amendment.
- Offline: Not available offline: a back-office screen on live, shared data (D38: only today's schedule, time and
  intervention records work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): none; no flow's Entities and screens table names an entity on this screen.

## Responsive behaviour

Desktop; approvals and lists also on the phone.

## Accessibility

Labelled controls; amounts and states as text.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)

## Shown in

- [FL-F6-05 Benchmark additions](../../flows/fl-f06-05-benchmark-additions.md)

## Open questions

None.

---

⬅️ [S-F6-11 Lead scoring](s-f06-11-lead-scoring.md) · ⬆️ [Up](README.md) · ➡️ [S-F6-13 Rentals](s-f06-13-rentals.md)
