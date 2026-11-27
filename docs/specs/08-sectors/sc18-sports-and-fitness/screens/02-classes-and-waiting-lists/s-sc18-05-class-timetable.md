🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🏋️ [SC18 Sports and fitness](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC18-02 Classes and waiting lists](README.md) ›
🖥️ S-SC18-05 Class timetable

# 🖥️ S-SC18-05 Class timetable

**Status:** ✅ specified

## Personas

- [U13 Owner](../../../../01-users/personas/u13-owner.md): every class and its capacity.

## Purpose

Create and publish classes with their coach, room, time and capacity.

## Entry points

Sports and fitness › Classes; the timetable of the app; the AI assistant.

## Wireframe

```text
+--------------------------------------------------------------------------------------------------+
| Timetable: autumn season                                                [New class]              |
| Class            Day/time       Coach       Room   Cap  Booked   State                           |
| Yoga             Mon 18:30      Sana M.     A      20   20       Full                            |
| Cycling          Tue 07:00      Louis T.    B      16   9        Published                       |
| Boxing           Wed 19:00      Hugo B.     A      14   -        Draft                           |
| [Publish the timetable]  [Cancel a class]  [Replace the coach]                                   |
+--------------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC18-02 step 1, U13 | desktop | ![FL-SC18-02 step 1, U13, light](../../images/02-classes-and-waiting-lists/u13-owner/1-class-timetable-desktop-light.png) | ![FL-SC18-02 step 1, U13, dark](../../images/02-classes-and-waiting-lists/u13-owner/1-class-timetable-desktop-dark.png) |
| FL-SC18-02 step 1, U13 | phone | ![FL-SC18-02 step 1, U13, light](../../images/02-classes-and-waiting-lists/u13-owner/1-class-timetable-phone-light.png) | ![FL-SC18-02 step 1, U13, dark](../../images/02-classes-and-waiting-lists/u13-owner/1-class-timetable-phone-dark.png) |
| Error E1, U13 | desktop | ![Error E1, U13, light](../../images/02-classes-and-waiting-lists/u13-owner/e1-the-class-is-full-desktop-light.png) | ![Error E1, U13, dark](../../images/02-classes-and-waiting-lists/u13-owner/e1-the-class-is-full-desktop-dark.png) |
| Error E1, U13 | phone | ![Error E1, U13, light](../../images/02-classes-and-waiting-lists/u13-owner/e1-the-class-is-full-phone-light.png) | ![Error E1, U13, dark](../../images/02-classes-and-waiting-lists/u13-owner/e1-the-class-is-full-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc18-05-class-timetable-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc18-05-class-timetable-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc18-05-class-timetable-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc18-05-class-timetable-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc18-05-class-timetable-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc18-05-class-timetable-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc18-05-class-timetable-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc18-05-class-timetable-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Activity | E-SC18-04 activity | choice | yes while Draft | yes |
| Coach | E-SC18-04 coach | employee | yes while Draft | yes |
| Room | E-SC18-04 room | bookable resource | yes while Draft | yes |
| Day and time | E-SC18-04 starts at | date and time | yes while Draft | yes |
| Capacity | E-SC18-04 capacity | number | yes while Draft | yes |
| Minimum to run | E-SC18-04 minimum | number | yes while Draft | no |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| New class | header | owner | a class is created Draft |
| Publish | header | owner | the classes become Published |
| Cancel | class row | owner | the class becomes Cancelled and the members are told |
| Replace the coach | class row | owner | a coach with the diploma is assigned |

## States

- Normal: the classes with their coach, room, capacity and booked places.
- Empty: No class yet, with New class.
- Loading: the headings and the table as placeholders; the values follow.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); a room taken or
  a coach without the diploma, with what to do.
- Read-only: the record in a locked state: values shown, no action offered.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-SC18-04 Class](../../data/e-sc18-04-class.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC18-04 Class | Draft | Badge "Draft"; a new record starts here; next: Published (UC-SC18-05); fields editable within the role | U13 | `u13-owner/s-sc18-05-class-timetable-e-sc18-04-class-draft-{desktop,phone}-{light,dark}.png` |
| E-SC18-04 Class | Published | Badge "Published"; next: Full, Held or Cancelled (BR-SC18-05, UC-SC18-05); fields editable within the role | U13 | `u13-owner/s-sc18-05-class-timetable-e-sc18-04-class-published-{desktop,phone}-{light,dark}.png` |
| E-SC18-04 Class | Full | Badge "Full"; next: Published, Held or Cancelled (UC-SC18-07, UC-SC18-05); fields editable within the role | U13 | `u13-owner/s-sc18-05-class-timetable-e-sc18-04-class-full-{desktop,phone}-{light,dark}.png` |
| E-SC18-04 Class | Held | Badge "Held"; final: read-only, no next state; the history shows how it got here | U13 | `u13-owner/s-sc18-05-class-timetable-e-sc18-04-class-held-{desktop,phone}-{light,dark}.png` |
| E-SC18-04 Class | Cancelled | Badge "Cancelled"; final: read-only, no next state; the history shows how it got here | U13 | `u13-owner/s-sc18-05-class-timetable-e-sc18-04-class-cancelled-{desktop,phone}-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop first; the member reads the timetable on a phone.

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

⬅️ [S-SC18-04 Membership changes](../01-memberships-and-access/s-sc18-04-membership-changes.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC18-06 Class booking](s-sc18-06-class-booking.md)
