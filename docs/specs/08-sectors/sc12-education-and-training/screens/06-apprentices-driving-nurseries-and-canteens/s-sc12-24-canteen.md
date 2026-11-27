🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🎓 [SC12 Education and training](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC12-06 Apprentices, driving schools, nurseries, canteens](README.md) ›
🖥️ S-SC12-24 Canteen and activities

# 🖥️ S-SC12-24 Canteen and activities

**Status:** ✅ specified

## Personas

- [U38 Training coordinator](../../../../01-users/personas/u38-training-coordinator.md): the menus, cut-offs, counts and
  bills.
- [U09 Customer](../../../../01-users/personas/u09-customer.md): their pupil's bookings.

## Purpose

Book meals and activities before the cut-off, give the kitchen its count and bill the families.

## Entry points

Education and training › Meal bookings; the kitchen's count; the parent's phone.

## Wireframe

```text
+--------------------------------------------------------------------------------------------------+
| Week 47   Cut-off: Friday 9:00 for the next week                              [Set the menus]    |
| Day        Menu            Booked   Vegetarian   Allergens listed   State                        |
| Mon 11-23  Pasta bolognese  142      11           gluten, milk       Booked                      |
| Tue 11-24  Fish and rice    138      11           fish               Booked                      |
| Wed 11-25  Activity: pottery 24      -            -                  Booked                      |
| Pupil Emma: Mon vegetarian, Tue vegetarian      Locked after Friday 9:00                         |
| Late change request: 3 waiting for the coordinator                                               |
+--------------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC12-06 step 4, U38 | desktop | ![FL-SC12-06 step 4, U38, light](../../images/06-apprentices-driving-nurseries-and-canteens/u38-training-coordinator/4-canteen-desktop-light.png) | ![FL-SC12-06 step 4, U38, dark](../../images/06-apprentices-driving-nurseries-and-canteens/u38-training-coordinator/4-canteen-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc12-24-canteen-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc12-24-canteen-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc12-24-canteen-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc12-24-canteen-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc12-24-canteen-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc12-24-canteen-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-sc12-24-canteen-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-sc12-24-canteen-offline-desktop-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Pupil | E-SC12-23 pupil | link | no | yes |
| Date and menu | E-SC12-23 date, menu | date and choice | yes while Booked | yes |
| Diet and allergens | E-SC12-23 diet | choice | yes while Booked | no |
| Cut-off | E-SC12-23 cut-off | date and time | no | no |
| Served | E-SC12-23 served | yes or no | no | no |
| Charge | E-SC12-23 charge | amount | no | no |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Book | day | parent, coordinator | a meal or activity Booked before its cut-off |
| Cancel | booking | parent, coordinator | the booking becomes Cancelled if before the cut-off |
| Change after the lock | booking | coordinator | a change with its reason, audited |
| Mark as served | booking | kitchen | the booking becomes Served |

## States

- Normal: the days with menus, counts, diets and the pupil's bookings with their state.
- Empty: No menu yet, with Set the menus.
- Loading: the headings and the table as placeholders; the values follow.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); a booking after
  the cut-off or an allergen conflict, with the cut-off time or the menu to choose.
- Read-only: the record in a locked state: values shown, no action offered.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-SC12-23 Meal booking](../../data/e-sc12-23-meal-booking.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC12-23 Meal booking | Booked | Badge "Booked"; a new record starts here; next: Locked or Cancelled (BR-SC12-19, UC-SC12-24); fields editable within the role | U38, U09 | `u38-training-coordinator/s-sc12-24-canteen-e-sc12-23-meal-booking-booked-desktop-{light,dark}.png`, `u09-customer/s-sc12-24-canteen-e-sc12-23-meal-booking-booked-phone-{light,dark}.png` |
| E-SC12-23 Meal booking | Locked | Badge "Locked"; next: Served or Cancelled (UC-SC12-24); fields editable within the role | U38, U09 | `u38-training-coordinator/s-sc12-24-canteen-e-sc12-23-meal-booking-locked-desktop-{light,dark}.png`, `u09-customer/s-sc12-24-canteen-e-sc12-23-meal-booking-locked-phone-{light,dark}.png` |
| E-SC12-23 Meal booking | Cancelled | Badge "Cancelled"; final: read-only, no next state; the history shows how it got here | U38, U09 | `u38-training-coordinator/s-sc12-24-canteen-e-sc12-23-meal-booking-cancelled-desktop-{light,dark}.png`, `u09-customer/s-sc12-24-canteen-e-sc12-23-meal-booking-cancelled-phone-{light,dark}.png` |
| E-SC12-23 Meal booking | Served | Badge "Served"; final: read-only, no next state; the history shows how it got here | U38, U09 | `u38-training-coordinator/s-sc12-24-canteen-e-sc12-23-meal-booking-served-desktop-{light,dark}.png`, `u09-customer/s-sc12-24-canteen-e-sc12-23-meal-booking-served-phone-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

The coordinator works on a desktop; the apprentice, the instructor and the parents use the phone, with the same actions
in one column.

## Accessibility

Every control is reachable by keyboard; states and errors are announced to screen readers and never rely on colour
alone; each field has its visible label.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)
- [C-01 Button](../../../../04-ux/design-system/components/c-01-button.md)

## Shown in

- [FL-SC12-06](../../flows/fl-sc12-06-apprentices-driving-nurseries-and-canteens.md)

## Open questions

None.

---

⬅️ [S-SC12-23 Nursery](s-sc12-23-nursery.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC12-L01 Courses](../00-lists/s-sc12-l01-courses.md)
