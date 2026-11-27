🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🏋️ [SC18 Sports and fitness](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC18-02 Classes and waiting lists](README.md) › 🖥️ S-SC18-07 Waiting list

# 🖥️ S-SC18-07 Waiting list

**Status:** 🔄 waiting for the owner

## Personas

- [U53 Coach](../../../../01-users/personas/u53-coach.md): the lists of their classes.
- [U09 Customer](../../../../01-users/personas/u09-customer.md): their own position and offers.

## Purpose

Show the waiting list of a class in order and offer a freed place to the first member.

## Entry points

Sports and fitness › Classes; the class's page; the app's notification.

## Wireframe

```text
+--------------------------------------------------------------------------------------------------+
| Waiting list: Yoga Mon 18:30                                          Full 20/20                 |
| Position  Member        Since        State                                                       |
| 1         Jules P.      Mon 09:12    Offered, 24 minutes left                                    |
| 2         Noor A.       Mon 10:40    Waiting                                                     |
| 3         Lea D.        Tue 08:05    Waiting                                                     |
| [Add by hand]  [Skip]  [Close the list]                                                          |
+--------------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC18-02 step 3, U53 | phone | ![FL-SC18-02 step 3, U53, light](../../images/02-classes-and-waiting-lists/u53-coach/3-waiting-list-phone-light.png) | ![FL-SC18-02 step 3, U53, dark](../../images/02-classes-and-waiting-lists/u53-coach/3-waiting-list-phone-dark.png) |
| Empty | phone | ![Empty, light](../../images/states/s-sc18-07-waiting-list-empty-phone-light.png) | ![Empty, dark](../../images/states/s-sc18-07-waiting-list-empty-phone-dark.png) |
| Loading | phone | ![Loading, light](../../images/states/s-sc18-07-waiting-list-loading-phone-light.png) | ![Loading, dark](../../images/states/s-sc18-07-waiting-list-loading-phone-dark.png) |
| Read-only | phone | ![Read-only, light](../../images/states/s-sc18-07-waiting-list-read-only-phone-light.png) | ![Read-only, dark](../../images/states/s-sc18-07-waiting-list-read-only-phone-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc18-07-waiting-list-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc18-07-waiting-list-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Position | E-SC18-05 waiting position | number | no | yes |
| Member | E-SC18-05 member | link | no | yes |
| Since | E-SC18-05 booked on | date and time | no | no |
| Offer | E-SC18-05 offer expires at | date and time | no | no |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Accept | offer | member | the booking becomes Booked |
| Skip | list row | coach, owner | the offer goes to the next member |
| Add by hand | header | coach, owner | a member is added with a reason |

## States

- Normal: the list in order with each member's state and the time left on an offer.
- Empty: Nobody is waiting.
- Loading: the headings and the table as placeholders; the values follow.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); an offer that
  cannot be made (no credit), with the member skipped.
- Read-only: the record in a locked state: values shown, no action offered.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): none; no flow's Entities and screens table names an entity on this screen.

## Responsive behaviour

The coach and the member use the phone, the owner and the treasurer a desktop, with the same actions in one column.

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

⬅️ [S-SC18-06 Class booking](s-sc18-06-class-booking.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC18-08 Coach planning](s-sc18-08-coach-planning.md)
