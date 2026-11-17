🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🏪 [F10 Point of sale (plugin)](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F10-01 Till session](README.md) › 🖥️ S-F10-16 Staff login

# 🖥️ S-F10-16 Staff login

**Status:** ✅ specified

## Personas

- [U17 Cashier](../../../../01-users/personas/u17-cashier.md)
- [U18 Waiter](../../../../01-users/personas/u18-waiter.md)
- [U19 Kitchen staff](../../../../01-users/personas/u19-kitchen-staff.md)
- [U02 Manager](../../../../01-users/personas/u02-manager.md)

## Purpose

Log in staff and set till rights.

## Entry points

Point of sale in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F10-01 step 1, U17 | desktop | ![FL-F10-01 step 1, U17, light](../../images/01-till-session/u17-cashier/1-staff-login-desktop-light.png) | ![FL-F10-01 step 1, U17, dark](../../images/01-till-session/u17-cashier/1-staff-login-desktop-dark.png) |
| FL-F10-01 step 1, U17 | phone | ![FL-F10-01 step 1, U17, light](../../images/01-till-session/u17-cashier/1-staff-login-phone-light.png) | ![FL-F10-01 step 1, U17, dark](../../images/01-till-session/u17-cashier/1-staff-login-phone-dark.png) |
| FL-F10-01 step 1, U17 | tablet | ![FL-F10-01 step 1, U17, light](../../images/01-till-session/u17-cashier/1-staff-login-tablet-light.png) | ![FL-F10-01 step 1, U17, dark](../../images/01-till-session/u17-cashier/1-staff-login-tablet-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f10-16-staff-login-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f10-16-staff-login-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f10-16-staff-login-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f10-16-staff-login-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f10-16-staff-login-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f10-16-staff-login-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f10-16-staff-login-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f10-16-staff-login-offline-phone-dark.png) |

## Fields and columns

As its entities.

## Actions

As its use case's main flow.

## States

- Normal: Log in staff and set till rights, as the wireframe shows.
- Empty: No staff badge yet, with Add staff.
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

- [FL-F10-01 Till session](../../flows/fl-f10-01-till-session.md)

## Open questions

None.

---

⬅️ [S-F10-15 Point of sale settings](../07-set-up-and-report/s-f10-15-point-of-sale-settings.md) · ⬆️ [Up](README.md) ·
➡️ [S-F10-17 Delivery orders](../06-mobile-and-delivery/s-f10-17-delivery-orders.md)
