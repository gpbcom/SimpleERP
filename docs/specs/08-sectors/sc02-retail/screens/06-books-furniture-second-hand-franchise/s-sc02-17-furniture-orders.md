🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🛍️ [SC02 Retail](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC02-06 Books, furniture, second-hand and franchise](README.md) ›
🖥️ S-SC02-17 Furniture orders

# 🖥️ S-SC02-17 Furniture orders

**Status:** ✅ specified

## Personas

- [U23 Store manager](../../../../01-users/personas/u23-store-manager.md): every order of the store.
- [U09 Customer](../../../../01-users/personas/u09-customer.md): their own order, its date and its slot.

## Purpose

Take a made-to-order piece with its deposit, keep the date tied to the supplier's confirmation and book the delivery.

## Entry points

Retail › Furniture orders; the quote's Order tab; the customer portal for the customer.

## Wireframe

```text
+--------------------------------------------------------------------------------------------------+
| Order FO-2026-088: Nordic sofa, grey fabric, 240 cm              Confirmed   [Save] [Book slot]  |
| Customer Claire P.      Total 1,890.00 EUR   Deposit 567.00 EUR (paid)   Balance 1,323.00 EUR    |
| Supplier  Maison Lorrain   Ordered 2026-11-14   Confirmed ready 2027-01-04                       |
| Transport 3 days    Earliest delivery 2027-01-07    Promised 2027-01-07                          |
| Slot  2027-01-07 morning, delivery and assembly      Customer signature  waiting                 |
| History  deposit received - ordered - confirmed by the supplier                                  |
+--------------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC02-06 step 2, U23 | desktop | ![FL-SC02-06 step 2, U23, light](../../images/06-books-furniture-second-hand-franchise/u23-store-manager/2-furniture-orders-desktop-light.png) | ![FL-SC02-06 step 2, U23, dark](../../images/06-books-furniture-second-hand-franchise/u23-store-manager/2-furniture-orders-desktop-dark.png) |
| FL-SC02-06 step 2, U23 | phone | ![FL-SC02-06 step 2, U23, light](../../images/06-books-furniture-second-hand-franchise/u23-store-manager/2-furniture-orders-phone-light.png) | ![FL-SC02-06 step 2, U23, dark](../../images/06-books-furniture-second-hand-franchise/u23-store-manager/2-furniture-orders-phone-dark.png) |
| FL-SC02-06 step 2, U23 | tablet | ![FL-SC02-06 step 2, U23, light](../../images/06-books-furniture-second-hand-franchise/u23-store-manager/2-furniture-orders-tablet-light.png) | ![FL-SC02-06 step 2, U23, dark](../../images/06-books-furniture-second-hand-franchise/u23-store-manager/2-furniture-orders-tablet-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc02-17-furniture-orders-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc02-17-furniture-orders-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc02-17-furniture-orders-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc02-17-furniture-orders-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc02-17-furniture-orders-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc02-17-furniture-orders-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc02-17-furniture-orders-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc02-17-furniture-orders-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Customer | E-SC02-14 customer | link | no | yes |
| Piece and options | E-SC02-14 options | model, fabric, dimensions | yes while Ordered | yes |
| Total, deposit, balance | E-SC02-14 amounts | amounts | no | yes |
| Supplier and confirmed date | E-SC02-14 supplier, confirmed date | text and date | yes while Ordered | no |
| Earliest and promised delivery | E-SC02-14 earliest, promised | dates | promised only | no |
| Slot | E-SC02-14 slot | date and half day | yes while Confirmed or Received | no |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Place with the supplier | header | store manager | the purchase order is created |
| Promise a date | order | store manager | the promised date within the earliest date |
| Book slot | order | store manager, customer | the slot is confirmed |
| Record delivery | order | store manager | the order becomes Delivered with the signature |
| Cancel | order | store manager | the order is Cancelled and the deposit handled |

## States

- Normal: the order with its options, amounts, the supplier's confirmed date, the promised date and the slot.
- Empty: No order yet, with New order.
- Loading: the headings and the table as placeholders; the values follow.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); a promised date
  before the earliest one, with the earliest date.
- Read-only: the record in a locked state: values shown, no action offered.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-SC02-14 Furniture order](../../data/e-sc02-14-furniture-order.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC02-14 Furniture order | Ordered | Badge "Ordered"; a new record starts here; next: Confirmed or Cancelled (BR-SC02-17, UC-SC02-17); fields editable within the role | U23, U09 | `u23-store-manager/s-sc02-17-furniture-orders-e-sc02-14-furniture-order-ordered-{desktop,phone,tablet}-{light,dark}.png`, `u09-customer/s-sc02-17-furniture-orders-e-sc02-14-furniture-order-ordered-phone-{light,dark}.png` |
| E-SC02-14 Furniture order | Confirmed | Badge "Confirmed"; next: Received or Cancelled (UC-SC02-17); fields editable within the role | U23, U09 | `u23-store-manager/s-sc02-17-furniture-orders-e-sc02-14-furniture-order-confirmed-{desktop,phone,tablet}-{light,dark}.png`, `u09-customer/s-sc02-17-furniture-orders-e-sc02-14-furniture-order-confirmed-phone-{light,dark}.png` |
| E-SC02-14 Furniture order | Received | Badge "Received"; next: Delivered (UC-SC02-17); fields editable within the role | U23, U09 | `u23-store-manager/s-sc02-17-furniture-orders-e-sc02-14-furniture-order-received-{desktop,phone,tablet}-{light,dark}.png`, `u09-customer/s-sc02-17-furniture-orders-e-sc02-14-furniture-order-received-phone-{light,dark}.png` |
| E-SC02-14 Furniture order | Delivered | Badge "Delivered"; final: read-only, no next state; the history shows how it got here | U23, U09 | `u23-store-manager/s-sc02-17-furniture-orders-e-sc02-14-furniture-order-delivered-{desktop,phone,tablet}-{light,dark}.png`, `u09-customer/s-sc02-17-furniture-orders-e-sc02-14-furniture-order-delivered-phone-{light,dark}.png` |
| E-SC02-14 Furniture order | Cancelled | Badge "Cancelled"; final: read-only, no next state; the history shows how it got here | U23, U09 | `u23-store-manager/s-sc02-17-furniture-orders-e-sc02-14-furniture-order-cancelled-{desktop,phone,tablet}-{light,dark}.png`, `u09-customer/s-sc02-17-furniture-orders-e-sc02-14-furniture-order-cancelled-phone-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop only; on a phone, the app asks to continue on a larger screen.

## Accessibility

Every control is reachable by keyboard; states and errors are announced to screen readers and never rely on colour
alone; each field has its visible label.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)
- [C-01 Button](../../../../04-ux/design-system/components/c-01-button.md)

## Shown in

- [FL-SC02-06](../../flows/fl-sc02-06-books-furniture-second-hand-franchise.md)

## Open questions

None.

---

⬅️ [S-SC02-16 Book trade](s-sc02-16-book-trade.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC02-18 Second-hand](s-sc02-18-second-hand.md)
