🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🏪 [F10 Point of sale (plugin)](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F10-04 Restaurant service](README.md) › 🖥️ S-F10-09 Floor

# 🖥️ S-F10-09 Floor

**Status:** ✅ specified

## Personas

- [U18 Waiter](../../../../01-users/personas/u18-waiter.md)
- [U02 Manager](../../../../01-users/personas/u02-manager.md)

## Purpose

Run the restaurant floor and bookings.

## Entry points

Point of sale in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F10-04 step 1, U18 | phone | ![FL-F10-04 step 1, U18, light](../../images/04-restaurant-service/u18-waiter/1-floor-phone-light.png) | ![FL-F10-04 step 1, U18, dark](../../images/04-restaurant-service/u18-waiter/1-floor-phone-dark.png) |
| FL-F10-04 step 1, U18 | tablet | ![FL-F10-04 step 1, U18, light](../../images/04-restaurant-service/u18-waiter/1-floor-tablet-light.png) | ![FL-F10-04 step 1, U18, dark](../../images/04-restaurant-service/u18-waiter/1-floor-tablet-dark.png) |
| Empty | phone | ![Empty, light](../../images/states/s-f10-09-floor-empty-phone-light.png) | ![Empty, dark](../../images/states/s-f10-09-floor-empty-phone-dark.png) |
| Loading | phone | ![Loading, light](../../images/states/s-f10-09-floor-loading-phone-light.png) | ![Loading, dark](../../images/states/s-f10-09-floor-loading-phone-dark.png) |
| Read-only | phone | ![Read-only, light](../../images/states/s-f10-09-floor-read-only-phone-light.png) | ![Read-only, dark](../../images/states/s-f10-09-floor-read-only-phone-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f10-09-floor-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f10-09-floor-offline-phone-dark.png) |

## Fields and columns

As its entities.

## Actions

As its use case's main flow.

## States

- Normal: Run the restaurant floor and bookings, as the wireframe shows.
- Empty: No table in use yet, with Seat guests.
- Loading: skeleton rows in place of the list ([C-03](../../../../04-ux/design-system/components/c-03-data-table.md));
  actions are disabled until it has loaded.
- Error: the error message pattern (D122).
- Read-only: closed sessions and recorded sales, which are inalterable (CR-FR-026).
- Offline: The till keeps selling, numbering and chaining its sales locally and syncs on reconnect
  ([BR-F10-06](../../business-rules/br-f10-06-offline-keeps-selling.md)); a card terminal that loses its link cancels
  the payment; a warning shows after 24 hours offline.

Shown entities (VD-15): [E-F10-11 Floor and table](../../data/e-f10-11-floor-and-table.md),
[E-F10-03 Point of sale order](../../data/e-f10-03-point-of-sale-order.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F10-11 Floor and table | Free | Badge "Free"; a new record starts here; next: Occupied (UC-F10-09); fields editable within the role | U02, U18 | `u02-manager/s-f10-09-floor-e-f10-11-floor-and-table-free-{desktop,phone}-{light,dark}.png`, `u18-waiter/s-f10-09-floor-e-f10-11-floor-and-table-free-{phone,tablet}-{light,dark}.png` |
| E-F10-11 Floor and table | Occupied | Badge "Occupied"; next: Booked (UC-F10-09); fields editable within the role | U02, U18 | `u02-manager/s-f10-09-floor-e-f10-11-floor-and-table-occupied-{desktop,phone}-{light,dark}.png`, `u18-waiter/s-f10-09-floor-e-f10-11-floor-and-table-occupied-{phone,tablet}-{light,dark}.png` |
| E-F10-11 Floor and table | Booked | Badge "Booked"; final: read-only, no next state; the history shows how it got here | U02, U18 | `u02-manager/s-f10-09-floor-e-f10-11-floor-and-table-booked-{desktop,phone}-{light,dark}.png`, `u18-waiter/s-f10-09-floor-e-f10-11-floor-and-table-booked-{phone,tablet}-{light,dark}.png` |
| E-F10-03 Point of sale order | Draft | Badge "Draft"; a new record starts here; next: Paid (UC-F10-03); fields editable within the role | U02, U18 | `u02-manager/s-f10-09-floor-e-f10-03-point-of-sale-order-draft-{desktop,phone}-{light,dark}.png`, `u18-waiter/s-f10-09-floor-e-f10-03-point-of-sale-order-draft-{phone,tablet}-{light,dark}.png` |
| E-F10-03 Point of sale order | Paid | Badge "Paid"; next: Invoiced (UC-F10-04); fields editable within the role | U02, U18 | `u02-manager/s-f10-09-floor-e-f10-03-point-of-sale-order-paid-{desktop,phone}-{light,dark}.png`, `u18-waiter/s-f10-09-floor-e-f10-03-point-of-sale-order-paid-{phone,tablet}-{light,dark}.png` |
| E-F10-03 Point of sale order | Invoiced | Badge "Invoiced"; next: Refunded (UC-F10-03); fields editable within the role | U02, U18 | `u02-manager/s-f10-09-floor-e-f10-03-point-of-sale-order-invoiced-{desktop,phone}-{light,dark}.png`, `u18-waiter/s-f10-09-floor-e-f10-03-point-of-sale-order-invoiced-{phone,tablet}-{light,dark}.png` |
| E-F10-03 Point of sale order | Refunded | Badge "Refunded"; final: read-only, no next state; the history shows how it got here | U02, U18 | `u02-manager/s-f10-09-floor-e-f10-03-point-of-sale-order-refunded-{desktop,phone}-{light,dark}.png`, `u18-waiter/s-f10-09-floor-e-f10-03-point-of-sale-order-refunded-{phone,tablet}-{light,dark}.png` |

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

- [FL-F10-04 Restaurant service](../../flows/fl-f10-04-restaurant-service.md)

## Open questions

None.

---

⬅️ [S-F10-08 Weighing](../02-sell-at-the-counter/s-f10-08-weighing.md) · ⬆️ [Up](README.md) ·
➡️ [S-F10-10 Preparation screen](s-f10-10-preparation-screen.md)
