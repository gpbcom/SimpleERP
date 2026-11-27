🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🏪 [F10 Point of sale (plugin)](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F10-05 Self-order and kiosk](README.md) › 🖥️ S-F10-13 Kiosk

# 🖥️ S-F10-13 Kiosk

**Status:** ✅ specified

## Personas

- [U09 Customer](../../../../01-users/personas/u09-customer.md)

## Purpose

Order at a kiosk.

## Entry points

Point of sale in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F10-05 step 2, U09 | phone | ![FL-F10-05 step 2, U09, light](../../images/05-self-order-and-kiosk/u09-customer/2-kiosk-phone-light.png) | ![FL-F10-05 step 2, U09, dark](../../images/05-self-order-and-kiosk/u09-customer/2-kiosk-phone-dark.png) |
| Empty | phone | ![Empty, light](../../images/states/s-f10-13-kiosk-empty-phone-light.png) | ![Empty, dark](../../images/states/s-f10-13-kiosk-empty-phone-dark.png) |
| Loading | phone | ![Loading, light](../../images/states/s-f10-13-kiosk-loading-phone-light.png) | ![Loading, dark](../../images/states/s-f10-13-kiosk-loading-phone-dark.png) |
| Read-only | phone | ![Read-only, light](../../images/states/s-f10-13-kiosk-read-only-phone-light.png) | ![Read-only, dark](../../images/states/s-f10-13-kiosk-read-only-phone-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f10-13-kiosk-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f10-13-kiosk-offline-phone-dark.png) |

## Fields and columns

As its entities.

## Actions

As its use case's main flow.

## States

- Normal: Order at a kiosk, as the wireframe shows.
- Empty: No item in the order yet, with Start an order.
- Loading: skeleton rows in place of the list ([C-03](../../../../04-ux/design-system/components/c-03-data-table.md));
  actions are disabled until it has loaded.
- Error: the error message pattern (D122).
- Read-only: closed sessions and recorded sales, which are inalterable (CR-FR-026).
- Offline: The till keeps selling, numbering and chaining its sales locally and syncs on reconnect
  ([BR-F10-06](../../business-rules/br-f10-06-offline-keeps-selling.md)); a card terminal that loses its link cancels
  the payment; a warning shows after 24 hours offline.

Shown entities (VD-15): [E-F10-03 Point of sale order](../../data/e-f10-03-point-of-sale-order.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F10-03 Point of sale order | Draft | Badge "Draft"; a new record starts here; next: Paid (UC-F10-03); fields editable within the role | U09 | `u09-customer/s-f10-13-kiosk-e-f10-03-point-of-sale-order-draft-phone-{light,dark}.png` |
| E-F10-03 Point of sale order | Paid | Badge "Paid"; next: Invoiced (UC-F10-04); fields editable within the role | U09 | `u09-customer/s-f10-13-kiosk-e-f10-03-point-of-sale-order-paid-phone-{light,dark}.png` |
| E-F10-03 Point of sale order | Invoiced | Badge "Invoiced"; next: Refunded (UC-F10-03); fields editable within the role | U09 | `u09-customer/s-f10-13-kiosk-e-f10-03-point-of-sale-order-invoiced-phone-{light,dark}.png` |
| E-F10-03 Point of sale order | Refunded | Badge "Refunded"; final: read-only, no next state; the history shows how it got here | U09 | `u09-customer/s-f10-13-kiosk-e-f10-03-point-of-sale-order-refunded-phone-{light,dark}.png` |

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

- [FL-F10-05 Self-order and kiosk](../../flows/fl-f10-05-self-order-and-kiosk.md)

## Open questions

None.

---

⬅️ [S-F10-12 QR menu](s-f10-12-qr-menu.md) · ⬆️ [Up](README.md) ·
➡️ [S-F10-14 Mobile till](../06-mobile-and-delivery/s-f10-14-mobile-till.md)
