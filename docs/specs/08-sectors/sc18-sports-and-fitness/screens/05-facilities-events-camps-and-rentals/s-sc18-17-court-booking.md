🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🏋️ [SC18 Sports and fitness](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC18-05 Facilities, events, camps and rentals](README.md) ›
🖥️ S-SC18-17 Court booking

# 🖥️ S-SC18-17 Court booking

**Status:** ✅ specified

## Personas

- [U09 Customer](../../../../01-users/personas/u09-customer.md): the free courts and their own bookings.
- [U13 Owner](../../../../01-users/personas/u13-owner.md): the occupation of every court.

## Purpose

Book a court or a facility by the hour at the right rate and see the occupation of the courts.

## Entry points

The member's app › Courts; Sports and fitness › Court bookings; the AI assistant.

## Wireframe

```text
+--------------------------------------------------------------------------------------------------+
| Courts: Saturday 21 November                                              Members rate           |
| Hour    Court 1       Court 2       Court 3                                                      |
| 09:00   taken         free 18 EUR   class                                                        |
| 10:00   free 18 EUR   free 18 EUR   free 22 EUR                                                  |
| 11:00   free 18 EUR   taken         free 22 EUR                                                  |
| Held for you: Court 2, 10:00 (9 minutes left)   [Pay 18.00 EUR]                                  |
+--------------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC18-05 step 1, U09 | phone | ![FL-SC18-05 step 1, U09, light](../../images/05-facilities-events-camps-and-rentals/u09-customer/1-court-booking-phone-light.png) | ![FL-SC18-05 step 1, U09, dark](../../images/05-facilities-events-camps-and-rentals/u09-customer/1-court-booking-phone-dark.png) |
| Error E1, U09 | phone | ![Error E1, U09, light](../../images/05-facilities-events-camps-and-rentals/u09-customer/e1-the-court-is-taken-phone-light.png) | ![Error E1, U09, dark](../../images/05-facilities-events-camps-and-rentals/u09-customer/e1-the-court-is-taken-phone-dark.png) |
| Empty | phone | ![Empty, light](../../images/states/s-sc18-17-court-booking-empty-phone-light.png) | ![Empty, dark](../../images/states/s-sc18-17-court-booking-empty-phone-dark.png) |
| Loading | phone | ![Loading, light](../../images/states/s-sc18-17-court-booking-loading-phone-light.png) | ![Loading, dark](../../images/states/s-sc18-17-court-booking-loading-phone-dark.png) |
| Read-only | phone | ![Read-only, light](../../images/states/s-sc18-17-court-booking-read-only-phone-light.png) | ![Read-only, dark](../../images/states/s-sc18-17-court-booking-read-only-phone-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc18-17-court-booking-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc18-17-court-booking-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Court | E-SC18-13 court | bookable resource | yes while Held | yes |
| Date and hour | E-SC18-13 starts at | date and time | yes while Held | yes |
| Booker | E-SC18-13 booker | member or guest | no | yes |
| Rate | E-SC18-13 rate | members or public | no | no |
| Price | E-SC18-13 price | amount | no | no |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Take a court | slot | member, guest | the court is Held for ten minutes |
| Pay | footer | member, guest | the booking becomes Confirmed |
| Cancel | booking row | member, owner | the booking becomes Cancelled |
| Block hours | header | owner | hours are taken out of the calendar for a class or works |

## States

- Normal: the courts and hours with their price and the booker's rate.
- Empty: No court free that day, with the next free days.
- Loading: the headings and the table as placeholders; the values follow.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); a court taken
  meanwhile or a failed payment, with the nearest hours.
- Read-only: the record in a locked state: values shown, no action offered.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-SC18-13 Court booking](../../data/e-sc18-13-court-booking.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC18-13 Court booking | Held | Badge "Held"; a new record starts here; next: Confirmed or Cancelled (UC-SC18-17); fields editable within the role | U09, U13 | `u09-customer/s-sc18-17-court-booking-e-sc18-13-court-booking-held-phone-{light,dark}.png`, `u13-owner/s-sc18-17-court-booking-e-sc18-13-court-booking-held-{desktop,phone}-{light,dark}.png` |
| E-SC18-13 Court booking | Confirmed | Badge "Confirmed"; next: Used, No show or Cancelled (UC-SC18-17); fields editable within the role | U09, U13 | `u09-customer/s-sc18-17-court-booking-e-sc18-13-court-booking-confirmed-phone-{light,dark}.png`, `u13-owner/s-sc18-17-court-booking-e-sc18-13-court-booking-confirmed-{desktop,phone}-{light,dark}.png` |
| E-SC18-13 Court booking | Cancelled | Badge "Cancelled"; final: read-only, no next state; the history shows how it got here | U09, U13 | `u09-customer/s-sc18-17-court-booking-e-sc18-13-court-booking-cancelled-phone-{light,dark}.png`, `u13-owner/s-sc18-17-court-booking-e-sc18-13-court-booking-cancelled-{desktop,phone}-{light,dark}.png` |
| E-SC18-13 Court booking | Used | Badge "Used"; final: read-only, no next state; the history shows how it got here | U09, U13 | `u09-customer/s-sc18-17-court-booking-e-sc18-13-court-booking-used-phone-{light,dark}.png`, `u13-owner/s-sc18-17-court-booking-e-sc18-13-court-booking-used-{desktop,phone}-{light,dark}.png` |
| E-SC18-13 Court booking | No show | Badge "No show"; final: read-only, no next state; the history shows how it got here | U09, U13 | `u09-customer/s-sc18-17-court-booking-e-sc18-13-court-booking-no-show-phone-{light,dark}.png`, `u13-owner/s-sc18-17-court-booking-e-sc18-13-court-booking-no-show-{desktop,phone}-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Phone first: the hours as a grid, one court at a time.

## Accessibility

Every control is reachable by keyboard; states and errors are announced to screen readers and never rely on colour
alone; each field has its visible label.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)
- [C-01 Button](../../../../04-ux/design-system/components/c-01-button.md)

## Shown in

- [FL-SC18-05](../../flows/fl-sc18-05-facilities-events-camps-and-rentals.md)

## Open questions

None.

---

⬅️ [S-SC18-16 Club AI assistant](../04-personal-training/s-sc18-16-club-assistant.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC18-18 Tournaments](s-sc18-18-tournaments.md)
