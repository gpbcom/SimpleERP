🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🏪 [F10 Point of sale (plugin)](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F10-06 Mobile and delivery](README.md) › 🖥️ S-F10-17 Delivery orders

# 🖥️ S-F10-17 Delivery orders

**Status:** ✅ specified

## Personas

- [U17 Cashier](../../../../01-users/personas/u17-cashier.md)
- [U19 Kitchen staff](../../../../01-users/personas/u19-kitchen-staff.md)

## Purpose

Take delivery-platform orders.

## Entry points

Point of sale in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F10-06 step 2, U17 | desktop | ![FL-F10-06 step 2, U17, light](../../images/06-mobile-and-delivery/u17-cashier/2-delivery-desktop-light.png) | ![FL-F10-06 step 2, U17, dark](../../images/06-mobile-and-delivery/u17-cashier/2-delivery-desktop-dark.png) |
| FL-F10-06 step 2, U17 | phone | ![FL-F10-06 step 2, U17, light](../../images/06-mobile-and-delivery/u17-cashier/2-delivery-phone-light.png) | ![FL-F10-06 step 2, U17, dark](../../images/06-mobile-and-delivery/u17-cashier/2-delivery-phone-dark.png) |
| FL-F10-06 step 2, U17 | tablet | ![FL-F10-06 step 2, U17, light](../../images/06-mobile-and-delivery/u17-cashier/2-delivery-tablet-light.png) | ![FL-F10-06 step 2, U17, dark](../../images/06-mobile-and-delivery/u17-cashier/2-delivery-tablet-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f10-17-delivery-orders-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f10-17-delivery-orders-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f10-17-delivery-orders-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f10-17-delivery-orders-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f10-17-delivery-orders-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f10-17-delivery-orders-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f10-17-delivery-orders-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f10-17-delivery-orders-offline-phone-dark.png) |

## Fields and columns

As its entities.

## Actions

As its use case's main flow.

## States

- Normal: Take delivery-platform orders, as the wireframe shows.
- Empty: No delivery order yet, with Connect a platform.
- Loading: skeleton rows in place of the list ([C-03](../../../../04-ux/design-system/components/c-03-data-table.md));
  actions are disabled until it has loaded.
- Error: the error message pattern (D122).
- Read-only: closed sessions and recorded sales, which are inalterable (CR-FR-026).
- Offline: Not available offline: a back-office screen on live, shared data (D38: only today's schedule, time and
  intervention records work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-F10-03 Point of sale order](../../data/e-f10-03-point-of-sale-order.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F10-03 Point of sale order | Draft | Badge "Draft"; a new record starts here; next: Paid (UC-F10-03); fields editable within the role | U17, U19 | `u17-cashier/s-f10-17-delivery-orders-e-f10-03-point-of-sale-order-draft-{desktop,phone,tablet}-{light,dark}.png`, `u19-kitchen-staff/s-f10-17-delivery-orders-e-f10-03-point-of-sale-order-draft-desktop-{light,dark}.png` |

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

- [FL-F10-06 Mobile and delivery](../../flows/fl-f10-06-mobile-and-delivery.md)

## Open questions

None.

---

⬅️ [S-F10-16 Staff login](../01-till-session/s-f10-16-staff-login.md) · ⬆️ [Up](README.md) ·
➡️ [S-F10-18 Point of sale reports](../07-set-up-and-report/s-f10-18-point-of-sale-reports.md)
