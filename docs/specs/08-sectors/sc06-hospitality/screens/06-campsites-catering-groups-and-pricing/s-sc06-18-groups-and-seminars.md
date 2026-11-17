🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) ›
🍽️ [SC06 Restaurant and hospitality](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-SC06-06 Campsites, catering, groups, pricing and licences](README.md) ›
🖥️ S-SC06-18 Groups and seminars

# 🖥️ S-SC06-18 Groups and seminars

**Status:** 🔄 waiting for the owner

## Personas

- [U28 Hotel receptionist](../../../../01-users/personas/u28-hotel-receptionist.md): the blocks, their cut-off dates and
  rooming lists.
- [U09 Customer](../../../../01-users/personas/u09-customer.md): their own block and the list of guests to name.

## Purpose

Hold a block of rooms for a group, follow its rooming list and release the unnamed rooms at the cut-off date.

## Entry points

Restaurant and hospitality › Group bookings; the booking calendar; the organiser's link.

## Wireframe

```text
+--------------------------------------------------------------------------------------------------+
| Group G-044  Seminar Alpes Tech  4-6 June                  State: Confirmed   [Release now]      |
| Rooms 30 (20 double, 10 single)   Rate 118.00   Deposit 20 %   Cut-off 2026-05-20                |
| Night      Held   Named   To release   Meeting room   Meals                                      |
| 2026-06-04  30     24      6            Salle A        Lunch 28                                  |
| 2026-06-05  30     24      6            Salle A        Lunch, dinner 28                          |
| Rooming list: 24 of 30 named          Attrition 10 %      [Send reminder]                        |
+--------------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC06-06 step 3, U28 | desktop | ![FL-SC06-06 step 3, U28, light](../../images/06-campsites-catering-groups-and-pricing/u28-hotel-receptionist/3-groups-and-seminars-desktop-light.png) | ![FL-SC06-06 step 3, U28, dark](../../images/06-campsites-catering-groups-and-pricing/u28-hotel-receptionist/3-groups-and-seminars-desktop-dark.png) |
| FL-SC06-06 step 3, U28 | tablet | ![FL-SC06-06 step 3, U28, light](../../images/06-campsites-catering-groups-and-pricing/u28-hotel-receptionist/3-groups-and-seminars-tablet-light.png) | ![FL-SC06-06 step 3, U28, dark](../../images/06-campsites-catering-groups-and-pricing/u28-hotel-receptionist/3-groups-and-seminars-tablet-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc06-18-groups-and-seminars-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc06-18-groups-and-seminars-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc06-18-groups-and-seminars-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc06-18-groups-and-seminars-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc06-18-groups-and-seminars-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc06-18-groups-and-seminars-read-only-desktop-dark.png) |
| Offline | tablet | ![Offline, light](../../images/states/s-sc06-18-groups-and-seminars-offline-tablet-light.png) | ![Offline, dark](../../images/states/s-sc06-18-groups-and-seminars-offline-tablet-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Group and organiser | E-SC06-15 organiser | link | no | yes |
| Dates | E-SC06-15 from, to | dates | yes while Option | yes |
| Rooms held | E-SC06-15 rooms | number per type | yes while Option | yes |
| Rate | E-SC06-15 rate | amount in EUR | yes while Option | yes |
| Option date | E-SC06-15 option date | date | yes while Option | yes |
| Cut-off date | E-SC06-15 cut-off date | date | yes while Option | yes |
| Rooms named | E-SC06-15 rooms named | number | no | no |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Hold rooms | header | receptionist | the rooms are held on the calendar on option |
| Confirm | header | receptionist | the block becomes Confirmed after the deposit |
| Enter rooming list | block | receptionist, organiser | a reservation per named guest |
| Release now | block | receptionist | the unnamed rooms return to sale before the date |

## States

- Normal: the nights with the rooms held, named and to release.
- Empty: No group yet, with New group.
- Loading: the headings and the table as placeholders; the values follow.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); more rooms than
  free on a night, with the nights that fail.
- Read-only: the record in a locked state: values shown, no action offered.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-SC06-15 Group booking](../../data/e-sc06-15-group-booking.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC06-15 Group booking | Option | Badge "Option"; a new record starts here; next: Confirmed or Lapsed (UC-SC06-18, BR-SC06-18); fields editable within the role | U28, U09 | `u28-hotel-receptionist/s-sc06-18-groups-and-seminars-e-sc06-15-group-booking-option-{desktop,tablet}-{light,dark}.png`, `u09-customer/s-sc06-18-groups-and-seminars-e-sc06-15-group-booking-option-phone-{light,dark}.png` |
| E-SC06-15 Group booking | Confirmed | Badge "Confirmed"; next: Released (BR-SC06-18); fields editable within the role | U28, U09 | `u28-hotel-receptionist/s-sc06-18-groups-and-seminars-e-sc06-15-group-booking-confirmed-{desktop,tablet}-{light,dark}.png`, `u09-customer/s-sc06-18-groups-and-seminars-e-sc06-15-group-booking-confirmed-phone-{light,dark}.png` |
| E-SC06-15 Group booking | Lapsed | Badge "Lapsed"; final: read-only, no next state; the history shows how it got here | U28, U09 | `u28-hotel-receptionist/s-sc06-18-groups-and-seminars-e-sc06-15-group-booking-lapsed-{desktop,tablet}-{light,dark}.png`, `u09-customer/s-sc06-18-groups-and-seminars-e-sc06-15-group-booking-lapsed-phone-{light,dark}.png` |
| E-SC06-15 Group booking | Released | Badge "Released"; next: Closed (UC-SC06-18); fields editable within the role | U28, U09 | `u28-hotel-receptionist/s-sc06-18-groups-and-seminars-e-sc06-15-group-booking-released-{desktop,tablet}-{light,dark}.png`, `u09-customer/s-sc06-18-groups-and-seminars-e-sc06-15-group-booking-released-phone-{light,dark}.png` |
| E-SC06-15 Group booking | Closed | Badge "Closed"; final: read-only, no next state; the history shows how it got here | U28, U09 | `u28-hotel-receptionist/s-sc06-18-groups-and-seminars-e-sc06-15-group-booking-closed-{desktop,tablet}-{light,dark}.png`, `u09-customer/s-sc06-18-groups-and-seminars-e-sc06-15-group-booking-closed-phone-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop for the receptionist. The organiser's page on a phone lists the guests to name with one row per room.

## Accessibility

Every control is reachable by keyboard; states and errors are announced to screen readers and never rely on colour
alone; each field has its visible label.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)
- [C-01 Button](../../../../04-ux/design-system/components/c-01-button.md)

## Shown in

- [FL-SC06-06](../../flows/fl-sc06-06-campsites-catering-groups-and-pricing.md)

## Open questions

None.

---

⬅️ [S-SC06-17 Catering](s-sc06-17-catering.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC06-19 Dynamic pricing](s-sc06-19-dynamic-pricing.md)
