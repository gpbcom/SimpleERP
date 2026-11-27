🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🏛️ [SC20 Public bodies](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC20-03 Citizen services](README.md) › 🖥️ S-SC20-10 Hall booking

# 🖥️ S-SC20-10 Hall booking

**Status:** ✅ specified

## Personas

- [U56 Citizen](../../../../01-users/personas/u56-citizen.md): the halls and the equipment to book on the phone, with
  the rate and the deposit.

## Purpose

Book a municipal hall or equipment at the council's rates with the safety capacity checked.

## Entry points

Public bodies › Hall bookings; the portal's Book a hall button.

## Wireframe

```text
+--------------------------------------------------------------------------------------------------+
| Halls                                                 Date: 14 June 2027   [Book]                |
| Hall            Capacity   Free      Resident   Association   Others   Deposit                   |
| Village hall    100        yes       160        120           400      300                       |
| Sports hall     300        no        -          -             -        500                       |
| Equipment: 20 tables, 100 chairs, stage      People: 80      Purpose: Wedding                    |
+--------------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC20-03 step 2, U56 | phone | ![FL-SC20-03 step 2, U56, light](../../images/03-citizen-services/u56-citizen/2-hall-booking-phone-light.png) | ![FL-SC20-03 step 2, U56, dark](../../images/03-citizen-services/u56-citizen/2-hall-booking-phone-dark.png) |
| Empty | phone | ![Empty, light](../../images/states/s-sc20-10-hall-booking-empty-phone-light.png) | ![Empty, dark](../../images/states/s-sc20-10-hall-booking-empty-phone-dark.png) |
| Loading | phone | ![Loading, light](../../images/states/s-sc20-10-hall-booking-loading-phone-light.png) | ![Loading, dark](../../images/states/s-sc20-10-hall-booking-loading-phone-dark.png) |
| Read-only | phone | ![Read-only, light](../../images/states/s-sc20-10-hall-booking-read-only-phone-light.png) | ![Read-only, dark](../../images/states/s-sc20-10-hall-booking-read-only-phone-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc20-10-hall-booking-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc20-10-hall-booking-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Hall or equipment | E-SC20-09 resource | list of bookable resources | yes while Requested | yes |
| Date | E-SC20-09 date | date | yes while Requested | yes |
| People | E-SC20-09 people | number | yes while Requested | yes |
| Class of user | E-SC20-09 class | resident, association, other | no | yes |
| Rate | E-SC20-09 rate | amount | no | yes |
| Deposit | E-SC20-09 deposit | amount | no | yes |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Book | form | citizen | the booking is requested with its rate and deposit |
| Confirm | row | office worker | the booking is confirmed once the deposit is paid |
| Close | row | office worker | the use is checked and the deposit returned or kept |

## States

- Normal: the halls and equipment with capacity, availability, rates and deposit, and the bookings.
- Empty: No hall available on this date.
- Loading: the headings and the table as placeholders; the values follow.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); a hall already
  booked, a capacity exceeded, a deposit not paid, with the hall named.
- Read-only: the record in a locked state: values shown, no action offered.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-SC20-09 Hall booking](../../data/e-sc20-09-hall-booking.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC20-09 Hall booking | Requested | Badge "Requested"; a new record starts here; next: Confirmed or Cancelled (BR-SC20-10); fields editable within the role | U56 | `u56-citizen/s-sc20-10-hall-booking-e-sc20-09-hall-booking-requested-phone-{light,dark}.png` |
| E-SC20-09 Hall booking | Confirmed | Badge "Confirmed"; next: Used or Cancelled (UC-SC20-10); fields editable within the role | U56 | `u56-citizen/s-sc20-10-hall-booking-e-sc20-09-hall-booking-confirmed-phone-{light,dark}.png` |
| E-SC20-09 Hall booking | Used | Badge "Used"; next: Closed (UC-SC20-10); fields editable within the role | U56 | `u56-citizen/s-sc20-10-hall-booking-e-sc20-09-hall-booking-used-phone-{light,dark}.png` |
| E-SC20-09 Hall booking | Closed | Badge "Closed"; final: read-only, no next state; the history shows how it got here | U56 | `u56-citizen/s-sc20-10-hall-booking-e-sc20-09-hall-booking-closed-phone-{light,dark}.png` |
| E-SC20-09 Hall booking | Cancelled | Badge "Cancelled"; final: read-only, no next state; the history shows how it got here | U56 | `u56-citizen/s-sc20-10-hall-booking-e-sc20-09-hall-booking-cancelled-phone-{light,dark}.png` |

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

- [FL-SC20-03 Citizen services](../../flows/fl-sc20-03-citizen-services.md)

## Open questions

None.

---

⬅️ [S-SC20-09 Citizen request](s-sc20-09-citizen-request.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC20-11 Public payments](s-sc20-11-public-payments.md)
