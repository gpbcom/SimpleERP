🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🏋️ [SC18 Sports and fitness](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC18-02 Classes and waiting lists](README.md) ›
🖥️ S-SC18-06 Class booking

# 🖥️ S-SC18-06 Class booking

**Status:** 🔄 waiting for the owner

## Personas

- [U09 Customer](../../../../01-users/personas/u09-customer.md): the classes, their own bookings and credits.

## Purpose

Let a member book, cancel and follow their places in classes.

## Entry points

The member's app › Classes; the member's page; the AI assistant.

## Wireframe

```text
+--------------------------------------------------------------------------------------------------+
| Classes: this week                                                      Credits 6                |
| Mon 18:30  Yoga       Sana M.   Full (20/20)        [Join the waiting list]                      |
| Tue 07:00  Cycling    Louis T.  9/16 places         [Book]                                       |
| Wed 19:00  Boxing     Hugo B.   3/14 places         [Book]                                       |
| My bookings  Tue 07:00 Cycling   Booked   closes 05:00   [Cancel]                                |
| Missed classes this month: 0                                                                     |
+--------------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC18-02 step 2, U09 | phone | ![FL-SC18-02 step 2, U09, light](../../images/02-classes-and-waiting-lists/u09-customer/2-class-booking-phone-light.png) | ![FL-SC18-02 step 2, U09, dark](../../images/02-classes-and-waiting-lists/u09-customer/2-class-booking-phone-dark.png) |
| Empty | phone | ![Empty, light](../../images/states/s-sc18-06-class-booking-empty-phone-light.png) | ![Empty, dark](../../images/states/s-sc18-06-class-booking-empty-phone-dark.png) |
| Loading | phone | ![Loading, light](../../images/states/s-sc18-06-class-booking-loading-phone-light.png) | ![Loading, dark](../../images/states/s-sc18-06-class-booking-loading-phone-dark.png) |
| Read-only | phone | ![Read-only, light](../../images/states/s-sc18-06-class-booking-read-only-phone-light.png) | ![Read-only, dark](../../images/states/s-sc18-06-class-booking-read-only-phone-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc18-06-class-booking-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc18-06-class-booking-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Class | E-SC18-05 class | link | no | yes |
| Member | E-SC18-05 member | link | no | yes |
| Credit | E-SC18-05 credit used | pack, included or drop-in | no | yes |
| State | E-SC18-05 state | badge | no | no |
| Booking closes | E-SC18-04 booking closes at | date and time | no | no |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Book | class row | member | the booking is saved Booked |
| Join the waiting list | class row | member | the booking is saved Waiting |
| Cancel | booking row | member | the booking becomes Cancelled and the credit returns |
| Mark attended | booking row | coach | the booking becomes Attended |

## States

- Normal: the classes with their free places and the member's own bookings.
- Empty: No class published this week.
- Loading: the headings and the table as placeholders; the values follow.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); a closed
  booking or no credit left, with the offer that follows.
- Read-only: the record in a locked state: values shown, no action offered.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-SC18-05 Class booking](../../data/e-sc18-05-class-booking.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC18-05 Class booking | Booked | Badge "Booked"; a new record starts here; next: Attended, Missed or Cancelled (UC-SC18-06); fields editable within the role | U09 | `u09-customer/s-sc18-06-class-booking-e-sc18-05-class-booking-booked-phone-{light,dark}.png` |
| E-SC18-05 Class booking | Waiting | Badge "Waiting"; a new record starts here; next: Booked or Cancelled (BR-SC18-07, UC-SC18-07); fields editable within the role | U09 | `u09-customer/s-sc18-06-class-booking-e-sc18-05-class-booking-waiting-phone-{light,dark}.png` |
| E-SC18-05 Class booking | Attended | Badge "Attended"; final: read-only, no next state; the history shows how it got here | U09 | `u09-customer/s-sc18-06-class-booking-e-sc18-05-class-booking-attended-phone-{light,dark}.png` |
| E-SC18-05 Class booking | Missed | Badge "Missed"; final: read-only, no next state; the history shows how it got here | U09 | `u09-customer/s-sc18-06-class-booking-e-sc18-05-class-booking-missed-phone-{light,dark}.png` |
| E-SC18-05 Class booking | Cancelled | Badge "Cancelled"; final: read-only, no next state; the history shows how it got here | U09 | `u09-customer/s-sc18-06-class-booking-e-sc18-05-class-booking-cancelled-phone-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Phone first: one column, the classes as cards.

## Accessibility

Every control is reachable by keyboard; states and errors are announced to screen readers and never rely on colour
alone; each field has its visible label.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)
- [C-01 Button](../../../../04-ux/design-system/components/c-01-button.md)

## Shown in

- [FL-SC18-02 Classes and waiting lists](../../flows/fl-sc18-02-classes-and-waiting-lists.md)

## Open questions

None.

---

⬅️ [S-SC18-05 Class timetable](s-sc18-05-class-timetable.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC18-07 Waiting list](s-sc18-07-waiting-list.md)
