🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 💇 [SC17 Beauty and wellness](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC17-01 Book staff and cabins](README.md) › 🖥️ S-SC17-02 Online booking

# 🖥️ S-SC17-02 Online booking

**Status:** 🔄 waiting for the owner

## Personas

- [U09 Customer](../../../../01-users/personas/u09-customer.md): the services, the free slots and their own bookings.

## Purpose

Let a customer choose services, a staff member and a free slot, pay the deposit and get a confirmation.

## Entry points

The salon's public booking page; a link in a message or a social post.

## Wireframe

```text
+--------------------------------------------------------------------------------------------------+
| Book a visit: Rue Verte salon                                       Step 2 of 3                  |
| Services   Facial 60 min 55.00 EUR    Cut 45 min 32.00 EUR                                       |
| With       [ Anyone v ]   Date  Saturday 21 November                                             |
| Free slots  [10:00]  [14:30]  [16:00]                                                            |
| Deposit 10.00 EUR, kept if you do not come and do not cancel 24 hours before                     |
| [Pay the deposit and confirm]                                                                    |
+--------------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC17-01 step 2, U09 | phone | ![FL-SC17-01 step 2, U09, light](../../images/01-book-staff-and-cabins/u09-customer/2-online-booking-phone-light.png) | ![FL-SC17-01 step 2, U09, dark](../../images/01-book-staff-and-cabins/u09-customer/2-online-booking-phone-dark.png) |
| Empty | phone | ![Empty, light](../../images/states/s-sc17-02-online-booking-empty-phone-light.png) | ![Empty, dark](../../images/states/s-sc17-02-online-booking-empty-phone-dark.png) |
| Loading | phone | ![Loading, light](../../images/states/s-sc17-02-online-booking-loading-phone-light.png) | ![Loading, dark](../../images/states/s-sc17-02-online-booking-loading-phone-dark.png) |
| Read-only | phone | ![Read-only, light](../../images/states/s-sc17-02-online-booking-read-only-phone-light.png) | ![Read-only, dark](../../images/states/s-sc17-02-online-booking-read-only-phone-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc17-02-online-booking-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc17-02-online-booking-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Services | E-F4-11 appointment type | list | yes while Held | yes |
| Staff member | E-SC17-02 staff member | choice or anyone | yes while Held | no |
| Date and time | E-SC17-02 starts at | slot | yes while Held | yes |
| Cabin | E-SC17-02 cabin | link | no | no |
| Deposit | E-SC17-03 amount | amount | no | no |
| Customer | E-F6-01 customer record | name, phone, email | yes while Held | yes |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Take this slot | slot | customer | the slot is Held for ten minutes |
| Pay and confirm | footer | customer | the booking becomes Confirmed |
| Move | booking | customer, beautician | a new slot, the old one released |
| Cancel | booking | customer, beautician | the booking becomes Cancelled and the deposit rule applies |

## States

- Normal: the free slots of the services and staff chosen, with the deposit and the terms.
- Empty: No free slot, with the nearest dates and a waiting list.
- Loading: the headings and the table as placeholders; the values follow.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); a slot taken
  meanwhile or a failed payment, with the nearest slots.
- Read-only: the record in a locked state: values shown, no action offered.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-SC17-02 Salon booking](../../data/e-sc17-02-salon-booking.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC17-02 Salon booking | Held | Badge "Held"; a new record starts here; next: Confirmed or Cancelled (UC-SC17-02, BR-SC17-02); fields editable within the role | U09 | `u09-customer/s-sc17-02-online-booking-e-sc17-02-salon-booking-held-phone-{light,dark}.png` |
| E-SC17-02 Salon booking | Confirmed | Badge "Confirmed"; next: Arrived, No show or Cancelled (UC-SC17-03, BR-SC17-04, UC-SC17-04); fields editable within the role | U09 | `u09-customer/s-sc17-02-online-booking-e-sc17-02-salon-booking-confirmed-phone-{light,dark}.png` |
| E-SC17-02 Salon booking | Cancelled | Badge "Cancelled"; final: read-only, no next state; the history shows how it got here | U09 | `u09-customer/s-sc17-02-online-booking-e-sc17-02-salon-booking-cancelled-phone-{light,dark}.png` |
| E-SC17-02 Salon booking | Arrived | Badge "Arrived"; next: Done (UC-SC17-09); fields editable within the role | U09 | `u09-customer/s-sc17-02-online-booking-e-sc17-02-salon-booking-arrived-phone-{light,dark}.png` |
| E-SC17-02 Salon booking | Done | Badge "Done"; final: read-only, no next state; the history shows how it got here | U09 | `u09-customer/s-sc17-02-online-booking-e-sc17-02-salon-booking-done-phone-{light,dark}.png` |
| E-SC17-02 Salon booking | No show | Badge "No show"; final: read-only, no next state; the history shows how it got here | U09 | `u09-customer/s-sc17-02-online-booking-e-sc17-02-salon-booking-no-show-phone-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Phone first: one column, the slots as large buttons.

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

⬅️ [S-SC17-01 Salon set-up](s-sc17-01-salon-setup.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC17-03 Desk booking](s-sc17-03-desk-booking.md)
