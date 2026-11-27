🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🏪 [F10 Point of sale (plugin)](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F10-02 Sell at the counter](README.md) › 🖥️ S-F10-02 Till

# 🖥️ S-F10-02 Till

**Status:** ✅ specified

## Personas

- [U17 Cashier](../../../../01-users/personas/u17-cashier.md)

## Purpose

Sell at the counter.

## Entry points

Point of sale in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F10-02 step 1, U17 | desktop | ![FL-F10-02 step 1, U17, light](../../images/02-sell-at-the-counter/u17-cashier/1-basket-desktop-light.png) | ![FL-F10-02 step 1, U17, dark](../../images/02-sell-at-the-counter/u17-cashier/1-basket-desktop-dark.png) |
| FL-F10-02 step 1, U17 | phone | ![FL-F10-02 step 1, U17, light](../../images/02-sell-at-the-counter/u17-cashier/1-basket-phone-light.png) | ![FL-F10-02 step 1, U17, dark](../../images/02-sell-at-the-counter/u17-cashier/1-basket-phone-dark.png) |
| FL-F10-02 step 1, U17 | tablet | ![FL-F10-02 step 1, U17, light](../../images/02-sell-at-the-counter/u17-cashier/1-basket-tablet-light.png) | ![FL-F10-02 step 1, U17, dark](../../images/02-sell-at-the-counter/u17-cashier/1-basket-tablet-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f10-02-till-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f10-02-till-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f10-02-till-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f10-02-till-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f10-02-till-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f10-02-till-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f10-02-till-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f10-02-till-offline-phone-dark.png) |

## Fields and columns

As its entities.

## Actions

As its use case's main flow.

## States

- Normal: Sell at the counter, as the wireframe shows.
- Empty: No line in the basket yet, with Scan or pick a product.
- Loading: skeleton rows in place of the list ([C-03](../../../../04-ux/design-system/components/c-03-data-table.md));
  actions are disabled until it has loaded.
- Error: the error message pattern (D122).
- Read-only: closed sessions and recorded sales, which are inalterable (CR-FR-026).
- Offline: The till keeps selling, numbering and chaining its sales locally and syncs on reconnect
  ([BR-F10-06](../../business-rules/br-f10-06-offline-keeps-selling.md)); a card terminal that loses its link cancels
  the payment; a warning shows after 24 hours offline.

Shown entities (VD-15): none; no flow's Entities and screens table names an entity on this screen.

## Responsive behaviour

Desktop; approvals and receipts also on the phone.

## Accessibility

Labelled controls; amounts and states as text.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)

## Shown in

- [FL-F10-02 Sell at the counter](../../flows/fl-f10-02-sell-at-the-counter.md)

## Open questions

None.

---

⬅️ [S-F10-01 Till session](../01-till-session/s-f10-01-till-session.md) · ⬆️ [Up](README.md) ·
➡️ [S-F10-03 Payment](s-f10-03-payment.md)
