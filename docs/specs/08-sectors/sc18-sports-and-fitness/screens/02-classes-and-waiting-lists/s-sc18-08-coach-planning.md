🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🏋️ [SC18 Sports and fitness](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC18-02 Classes and waiting lists](README.md) ›
🖥️ S-SC18-08 Coach planning

# 🖥️ S-SC18-08 Coach planning

**Status:** 🔄 waiting for the owner

## Personas

- [U13 Owner](../../../../01-users/personas/u13-owner.md): the planning of every coach.
- [U53 Coach](../../../../01-users/personas/u53-coach.md): their own week.

## Purpose

Assign classes to qualified coaches and see their hours and their qualifications' end dates.

## Entry points

Sports and fitness › Coach planning; the coach's workspace; the AI assistant.

## Wireframe

```text
+--------------------------------------------------------------------------------------------------+
| Coach planning: week 50                                                [Replace a coach]         |
| Coach       Mon         Tue         Wed          Hours   Diploma                                 |
| Sana M.     Yoga 18:30  -           Pilates 12:00 14/20   valid to 2028-02                       |
| Louis T.    -           Cycling 07:00 -           8/16    valid to 2027-01 (flagged)             |
| Hugo B.     -           -           Boxing 19:00  6/12    valid to 2028-06                       |
| [Assign]  [Propose a replacement]  [Ask the coach]                                               |
+--------------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC18-02 step 4, U13 | desktop | ![FL-SC18-02 step 4, U13, light](../../images/02-classes-and-waiting-lists/u13-owner/4-coach-planning-desktop-light.png) | ![FL-SC18-02 step 4, U13, dark](../../images/02-classes-and-waiting-lists/u13-owner/4-coach-planning-desktop-dark.png) |
| FL-SC18-02 step 4, U13 | phone | ![FL-SC18-02 step 4, U13, light](../../images/02-classes-and-waiting-lists/u13-owner/4-coach-planning-phone-light.png) | ![FL-SC18-02 step 4, U13, dark](../../images/02-classes-and-waiting-lists/u13-owner/4-coach-planning-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc18-08-coach-planning-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc18-08-coach-planning-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc18-08-coach-planning-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc18-08-coach-planning-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc18-08-coach-planning-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc18-08-coach-planning-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc18-08-coach-planning-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc18-08-coach-planning-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Coach | E-F9-01 employee record | link | no | yes |
| Class | E-SC18-04 class | link | yes | yes |
| Diploma | E-F9-12 qualification | text and date | no | no |
| Hours | E-F9-16 shift | number of the week | no | no |
| Answer | E-F9-16 answer | accept, decline | yes | no |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Assign | class | owner | the class is given to the coach after the check |
| Propose a replacement | class | owner | qualified and free coaches are listed |
| Accept | class | coach | the assignment is confirmed |
| Decline | class | coach | the class returns to the owner |

## States

- Normal: the coaches' weeks with their classes, hours and diplomas.
- Empty: No class to plan this week.
- Loading: the headings and the table as placeholders; the values follow.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); a missing
  diploma or an exceeded limit, with what to do.
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

⬅️ [S-SC18-07 Waiting list](s-sc18-07-waiting-list.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC18-09 Federation licences](../03-licences-and-competitions/s-sc18-09-federation-licences.md)
