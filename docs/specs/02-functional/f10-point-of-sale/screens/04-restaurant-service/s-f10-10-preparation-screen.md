🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🏪 [F10 Point of sale (plugin)](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F10-04 Restaurant service](README.md) › 🖥️ S-F10-10 Preparation screen

# 🖥️ S-F10-10 Preparation screen

**Status:** ✅ specified

## Personas

- [U19 Kitchen staff](../../../../01-users/personas/u19-kitchen-staff.md)

## Purpose

Prepare orders on kitchen screens.

## Entry points

Point of sale in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F10-04 step 2, U19 | desktop | ![FL-F10-04 step 2, U19, light](../../images/04-restaurant-service/u19-kitchen-staff/2-kitchen-screen-desktop-light.png) | ![FL-F10-04 step 2, U19, dark](../../images/04-restaurant-service/u19-kitchen-staff/2-kitchen-screen-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f10-10-preparation-screen-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f10-10-preparation-screen-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f10-10-preparation-screen-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f10-10-preparation-screen-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f10-10-preparation-screen-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f10-10-preparation-screen-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f10-10-preparation-screen-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f10-10-preparation-screen-offline-desktop-dark.png) |

## Fields and columns

As its entities.

## Actions

As its use case's main flow.

## States

- Normal: Prepare orders on kitchen screens, as the wireframe shows.
- Empty: No order to prepare yet, with Nothing waits.
- Loading: skeleton rows in place of the list ([C-03](../../../../04-ux/design-system/components/c-03-data-table.md));
  actions are disabled until it has loaded.
- Error: the error message pattern (D122).
- Read-only: closed sessions and recorded sales, which are inalterable (CR-FR-026).
- Offline: The till keeps selling, numbering and chaining its sales locally and syncs on reconnect
  ([BR-F10-06](../../business-rules/br-f10-06-offline-keeps-selling.md)); a card terminal that loses its link cancels
  the payment; a warning shows after 24 hours offline.

Shown entities (VD-15): [E-F10-03 Point of sale order](../../data/e-f10-03-point-of-sale-order.md),
[E-F10-13 Preparation ticket](../../data/e-f10-13-preparation-ticket.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F10-03 Point of sale order | Draft | Badge "Draft"; a new record starts here; next: Paid (UC-F10-03); fields editable within the role | U19 | `u19-kitchen-staff/s-f10-10-preparation-screen-e-f10-03-point-of-sale-order-draft-desktop-{light,dark}.png` |
| E-F10-03 Point of sale order | Paid | Badge "Paid"; next: Invoiced (UC-F10-04); fields editable within the role | U19 | `u19-kitchen-staff/s-f10-10-preparation-screen-e-f10-03-point-of-sale-order-paid-desktop-{light,dark}.png` |
| E-F10-03 Point of sale order | Invoiced | Badge "Invoiced"; next: Refunded (UC-F10-03); fields editable within the role | U19 | `u19-kitchen-staff/s-f10-10-preparation-screen-e-f10-03-point-of-sale-order-invoiced-desktop-{light,dark}.png` |
| E-F10-03 Point of sale order | Refunded | Badge "Refunded"; final: read-only, no next state; the history shows how it got here | U19 | `u19-kitchen-staff/s-f10-10-preparation-screen-e-f10-03-point-of-sale-order-refunded-desktop-{light,dark}.png` |
| E-F10-13 Preparation ticket | To prepare | Badge "To prepare"; a new record starts here; next: Ready (UC-F10-10); fields editable within the role | U19 | `u19-kitchen-staff/s-f10-10-preparation-screen-e-f10-13-preparation-ticket-to-prepare-desktop-{light,dark}.png` |
| E-F10-13 Preparation ticket | Ready | Badge "Ready"; next: Served (UC-F10-10); fields editable within the role | U19 | `u19-kitchen-staff/s-f10-10-preparation-screen-e-f10-13-preparation-ticket-ready-desktop-{light,dark}.png` |
| E-F10-13 Preparation ticket | Served | Badge "Served"; final: read-only, no next state; the history shows how it got here | U19 | `u19-kitchen-staff/s-f10-10-preparation-screen-e-f10-13-preparation-ticket-served-desktop-{light,dark}.png` |

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

⬅️ [S-F10-09 Floor](s-f10-09-floor.md) · ⬆️ [Up](README.md) · ➡️ [S-F10-11 Bill split](s-f10-11-bill-split.md)
