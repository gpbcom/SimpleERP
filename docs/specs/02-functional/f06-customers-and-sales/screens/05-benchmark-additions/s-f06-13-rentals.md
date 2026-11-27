🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🛒 [F6 Customers and sales](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F6-05 Benchmark additions](README.md) › 🖥️ S-F6-13 Rentals

# 🖥️ S-F6-13 Rentals

**Status:** ✅ specified

## Personas

- [U03 Sales](../../../../01-users/personas/u03-sales.md)
- [U15 Warehouse operator](../../../../01-users/personas/u15-warehouse-operator.md)
- [U09 Customer](../../../../01-users/personas/u09-customer.md)

## Purpose

Rent out equipment.

## Entry points

Customers and sales in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F6-05 step 3, U03 | desktop | ![FL-F6-05 step 3, U03, light](../../images/05-benchmark-additions/u03-sales/3-rental-desktop-light.png) | ![FL-F6-05 step 3, U03, dark](../../images/05-benchmark-additions/u03-sales/3-rental-desktop-dark.png) |
| FL-F6-05 step 3, U03 | phone | ![FL-F6-05 step 3, U03, light](../../images/05-benchmark-additions/u03-sales/3-rental-phone-light.png) | ![FL-F6-05 step 3, U03, dark](../../images/05-benchmark-additions/u03-sales/3-rental-phone-dark.png) |
| FL-F6-05 step 3, U03 | tablet | ![FL-F6-05 step 3, U03, light](../../images/05-benchmark-additions/u03-sales/3-rental-tablet-light.png) | ![FL-F6-05 step 3, U03, dark](../../images/05-benchmark-additions/u03-sales/3-rental-tablet-dark.png) |
| Error E1, U03 | desktop | ![Error E1, U03, light](../../images/05-benchmark-additions/u03-sales/e1-double-booked-desktop-light.png) | ![Error E1, U03, dark](../../images/05-benchmark-additions/u03-sales/e1-double-booked-desktop-dark.png) |
| Error E1, U03 | phone | ![Error E1, U03, light](../../images/05-benchmark-additions/u03-sales/e1-double-booked-phone-light.png) | ![Error E1, U03, dark](../../images/05-benchmark-additions/u03-sales/e1-double-booked-phone-dark.png) |
| Error E1, U03 | tablet | ![Error E1, U03, light](../../images/05-benchmark-additions/u03-sales/e1-double-booked-tablet-light.png) | ![Error E1, U03, dark](../../images/05-benchmark-additions/u03-sales/e1-double-booked-tablet-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f06-13-rentals-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f06-13-rentals-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f06-13-rentals-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f06-13-rentals-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f06-13-rentals-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f06-13-rentals-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f06-13-rentals-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f06-13-rentals-offline-phone-dark.png) |

## Fields and columns

As its entities.

## Actions

As its use case's main flow.

## States

- Normal: Rent out equipment, as the wireframe shows.
- Empty: No rental yet, with New rental.
- Loading: skeleton rows in place of the list ([C-03](../../../../04-ux/design-system/components/c-03-data-table.md));
  actions are disabled until it has loaded.
- Error: the error message pattern (D122).
- Read-only: sent, signed or posted documents, changed only by a new version, a credit note or an amendment.
- Offline: Not available offline: a back-office screen on live, shared data (D38: only today's schedule, time and
  intervention records work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-F6-09 Rental](../../data/e-f06-09-rental.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F6-09 Rental | Booked | Badge "Booked"; a new record starts here; next: Picked up (UC-F6-15); fields editable within the role | U03, U09 | `u03-sales/s-f06-13-rentals-e-f06-09-rental-booked-{desktop,phone,tablet}-{light,dark}.png`, `u09-customer/s-f06-13-rentals-e-f06-09-rental-booked-phone-{light,dark}.png` |
| E-F6-09 Rental | Picked up | Badge "Picked up"; next: Returned (UC-F6-15); fields editable within the role | U03, U09 | `u03-sales/s-f06-13-rentals-e-f06-09-rental-picked-up-{desktop,phone,tablet}-{light,dark}.png`, `u09-customer/s-f06-13-rentals-e-f06-09-rental-picked-up-phone-{light,dark}.png` |
| E-F6-09 Rental | Returned | Badge "Returned"; next: Late (UC-F6-15); fields editable within the role | U03, U09 | `u03-sales/s-f06-13-rentals-e-f06-09-rental-returned-{desktop,phone,tablet}-{light,dark}.png`, `u09-customer/s-f06-13-rentals-e-f06-09-rental-returned-phone-{light,dark}.png` |
| E-F6-09 Rental | Late | Badge "Late"; next: Returned (UC-F6-15); fields editable within the role | U03, U09 | `u03-sales/s-f06-13-rentals-e-f06-09-rental-late-{desktop,phone,tablet}-{light,dark}.png`, `u09-customer/s-f06-13-rentals-e-f06-09-rental-late-phone-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

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

⬅️ [S-F6-12 Product configurator](s-f06-12-product-configurator.md) · ⬆️ [Up](README.md) ·
➡️ [S-F6-14 Usage billing](s-f06-14-usage-billing.md)
