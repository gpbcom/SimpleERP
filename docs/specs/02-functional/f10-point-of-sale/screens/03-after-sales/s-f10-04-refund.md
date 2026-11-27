🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🏪 [F10 Point of sale (plugin)](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F10-03 After sales](README.md) › 🖥️ S-F10-04 Refund

# 🖥️ S-F10-04 Refund

**Status:** ✅ specified

## Personas

- [U17 Cashier](../../../../01-users/personas/u17-cashier.md)
- [U02 Manager](../../../../01-users/personas/u02-manager.md)

## Purpose

Refund or exchange.

## Entry points

Point of sale in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F10-03 step 1, U17 | desktop | ![FL-F10-03 step 1, U17, light](../../images/03-after-sales/u17-cashier/1-refund-desktop-light.png) | ![FL-F10-03 step 1, U17, dark](../../images/03-after-sales/u17-cashier/1-refund-desktop-dark.png) |
| FL-F10-03 step 1, U17 | phone | ![FL-F10-03 step 1, U17, light](../../images/03-after-sales/u17-cashier/1-refund-phone-light.png) | ![FL-F10-03 step 1, U17, dark](../../images/03-after-sales/u17-cashier/1-refund-phone-dark.png) |
| FL-F10-03 step 1, U17 | tablet | ![FL-F10-03 step 1, U17, light](../../images/03-after-sales/u17-cashier/1-refund-tablet-light.png) | ![FL-F10-03 step 1, U17, dark](../../images/03-after-sales/u17-cashier/1-refund-tablet-dark.png) |
| Error E1, U17 | desktop | ![Error E1, U17, light](../../images/03-after-sales/u17-cashier/e1-refund-limit-desktop-light.png) | ![Error E1, U17, dark](../../images/03-after-sales/u17-cashier/e1-refund-limit-desktop-dark.png) |
| Error E1, U17 | phone | ![Error E1, U17, light](../../images/03-after-sales/u17-cashier/e1-refund-limit-phone-light.png) | ![Error E1, U17, dark](../../images/03-after-sales/u17-cashier/e1-refund-limit-phone-dark.png) |
| Error E1, U17 | tablet | ![Error E1, U17, light](../../images/03-after-sales/u17-cashier/e1-refund-limit-tablet-light.png) | ![Error E1, U17, dark](../../images/03-after-sales/u17-cashier/e1-refund-limit-tablet-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f10-04-refund-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f10-04-refund-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f10-04-refund-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f10-04-refund-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f10-04-refund-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f10-04-refund-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f10-04-refund-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f10-04-refund-offline-phone-dark.png) |

## Fields and columns

As its entities.

## Actions

As its use case's main flow.

## States

- Normal: Refund or exchange, as the wireframe shows.
- Empty: No sale found for this ticket yet, with Search again.
- Loading: skeleton rows in place of the list ([C-03](../../../../04-ux/design-system/components/c-03-data-table.md));
  actions are disabled until it has loaded.
- Error: the error message pattern (D122).
- Read-only: closed sessions and recorded sales, which are inalterable (CR-FR-026).
- Offline: The till keeps selling, numbering and chaining its sales locally and syncs on reconnect
  ([BR-F10-06](../../business-rules/br-f10-06-offline-keeps-selling.md)); a card terminal that loses its link cancels
  the payment; a warning shows after 24 hours offline.

Shown entities (VD-15): [E-F10-05 Receipt](../../data/e-f10-05-receipt.md),
[E-F10-03 Point of sale order](../../data/e-f10-03-point-of-sale-order.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F10-05 Receipt | Recorded | Badge "Recorded"; a new record starts here; no other state; fields editable within the role | U02, U17 | `u02-manager/s-f10-04-refund-e-f10-05-receipt-recorded-{desktop,phone}-{light,dark}.png`, `u17-cashier/s-f10-04-refund-e-f10-05-receipt-recorded-{desktop,phone,tablet}-{light,dark}.png` |
| E-F10-03 Point of sale order | Draft | Badge "Draft"; a new record starts here; next: Paid (UC-F10-03); fields editable within the role | U02, U17 | `u02-manager/s-f10-04-refund-e-f10-03-point-of-sale-order-draft-{desktop,phone}-{light,dark}.png`, `u17-cashier/s-f10-04-refund-e-f10-03-point-of-sale-order-draft-{desktop,phone,tablet}-{light,dark}.png` |
| E-F10-03 Point of sale order | Paid | Badge "Paid"; next: Invoiced (UC-F10-04); fields editable within the role | U02, U17 | `u02-manager/s-f10-04-refund-e-f10-03-point-of-sale-order-paid-{desktop,phone}-{light,dark}.png`, `u17-cashier/s-f10-04-refund-e-f10-03-point-of-sale-order-paid-{desktop,phone,tablet}-{light,dark}.png` |
| E-F10-03 Point of sale order | Invoiced | Badge "Invoiced"; next: Refunded (UC-F10-03); fields editable within the role | U02, U17 | `u02-manager/s-f10-04-refund-e-f10-03-point-of-sale-order-invoiced-{desktop,phone}-{light,dark}.png`, `u17-cashier/s-f10-04-refund-e-f10-03-point-of-sale-order-invoiced-{desktop,phone,tablet}-{light,dark}.png` |
| E-F10-03 Point of sale order | Refunded | Badge "Refunded"; final: read-only, no next state; the history shows how it got here | U02, U17 | `u02-manager/s-f10-04-refund-e-f10-03-point-of-sale-order-refunded-{desktop,phone}-{light,dark}.png`, `u17-cashier/s-f10-04-refund-e-f10-03-point-of-sale-order-refunded-{desktop,phone,tablet}-{light,dark}.png` |

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

- [FL-F10-03 After sales](../../flows/fl-f10-03-after-sales.md)

## Open questions

None.

---

⬅️ [S-F10-03 Payment](../02-sell-at-the-counter/s-f10-03-payment.md) · ⬆️ [Up](README.md) ·
➡️ [S-F10-05 Receipt](../02-sell-at-the-counter/s-f10-05-receipt.md)
