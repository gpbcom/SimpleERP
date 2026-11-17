🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 💇 [SC17 Beauty and wellness](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC17-01 Book staff and cabins](README.md) › 🖥️ S-SC17-03 Desk booking

# 🖥️ S-SC17-03 Desk booking

**Status:** 🔄 waiting for the owner

## Personas

- [U52 Beautician](../../../../01-users/personas/u52-beautician.md): the bookings of the salon, with the customers'
  balances.

## Purpose

Book a visit for a customer at the desk or on the phone with the same rules as online.

## Entry points

Beauty and wellness › Desk booking; the tablet at the chair; the AI assistant.

## Wireframe

```text
+--------------------------------------------------------------------------------------------------+
| Desk booking                                                   Customer: Camille R.              |
| Balance: package Facial 3 sessions left, voucher 20.00 EUR                                       |
| Services   [ Cut 45 min v ] [+ add]      With  [ Anyone v ]                                      |
| Slots      Sat 10:00  Sat 11:30  Mon 09:00        [Rebook in 4 weeks]                            |
| Confirmation by  [x] text message  [ ] email  [ ] printed                                        |
| [Book]                                                                                           |
+--------------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC17-01 step 3, U52 | tablet | ![FL-SC17-01 step 3, U52, light](../../images/01-book-staff-and-cabins/u52-beautician/3-desk-booking-tablet-light.png) | ![FL-SC17-01 step 3, U52, dark](../../images/01-book-staff-and-cabins/u52-beautician/3-desk-booking-tablet-dark.png) |
| FL-SC17-01 step 3, U52 | phone | ![FL-SC17-01 step 3, U52, light](../../images/01-book-staff-and-cabins/u52-beautician/3-desk-booking-phone-light.png) | ![FL-SC17-01 step 3, U52, dark](../../images/01-book-staff-and-cabins/u52-beautician/3-desk-booking-phone-dark.png) |
| Empty | phone | ![Empty, light](../../images/states/s-sc17-03-desk-booking-empty-phone-light.png) | ![Empty, dark](../../images/states/s-sc17-03-desk-booking-empty-phone-dark.png) |
| Loading | phone | ![Loading, light](../../images/states/s-sc17-03-desk-booking-loading-phone-light.png) | ![Loading, dark](../../images/states/s-sc17-03-desk-booking-loading-phone-dark.png) |
| Read-only | phone | ![Read-only, light](../../images/states/s-sc17-03-desk-booking-read-only-phone-light.png) | ![Read-only, dark](../../images/states/s-sc17-03-desk-booking-read-only-phone-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc17-03-desk-booking-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc17-03-desk-booking-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Customer | E-F6-01 customer record | link | yes | yes |
| Services | E-SC17-02 services | list | yes | yes |
| Staff member | E-SC17-02 staff member | choice or anyone | yes | no |
| Slot | E-SC17-02 starts at | date and time | yes | yes |
| Confirmation channel | E-F5-10 consent | choice | yes | yes |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Book | footer | beautician, manager | the booking is saved and confirmed |
| Rebook | header | beautician | the same services four weeks later, when a slot is free |
| Send payment link | footer | beautician | the customer pays the deposit on their phone |

## States

- Normal: the customer, their balances, the services and the free slots.
- Empty: No customer chosen yet, with Find a customer.
- Loading: the headings and the table as placeholders; the values follow.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); a taken slot or
  a missing contact, with the nearest slots.
- Read-only: the record in a locked state: values shown, no action offered.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): none; no flow's Entities and screens table names an entity on this screen.

## Responsive behaviour

The beautician works on the tablet at the chair, the manager on a desktop and the customer on a phone, with the same
actions in one column.

## Accessibility

Every control is reachable by keyboard; states and errors are announced to screen readers and never rely on colour
alone; each field has its visible label.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)
- [C-01 Button](../../../../04-ux/design-system/components/c-01-button.md)

## Shown in

- [FL-SC17-01 Book staff and cabins](../../flows/fl-sc17-01-book-staff-and-cabins.md)

## Open questions

None.

---

⬅️ [S-SC17-02 Online booking](s-sc17-02-online-booking.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC17-04 Deposits and no-shows](s-sc17-04-deposits-and-no-shows.md)
