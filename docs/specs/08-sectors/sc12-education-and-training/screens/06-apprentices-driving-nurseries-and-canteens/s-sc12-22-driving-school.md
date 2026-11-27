🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🎓 [SC12 Education and training](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC12-06 Apprentices, driving schools, nurseries, canteens](README.md) ›
🖥️ S-SC12-22 Driving school

# 🖥️ S-SC12-22 Driving school

**Status:** ✅ specified

## Personas

- [U38 Training coordinator](../../../../01-users/personas/u38-training-coordinator.md): the planning, the instructors
  and the learners' hours.
- [U39 Trainer](../../../../01-users/personas/u39-trainer.md): their lessons and booklet entries.

## Purpose

Plan and record lessons with authorised instructors, keep the booklet and follow each learner's hours to the exam.

## Entry points

Education and training › Driving lessons; the week planning; the instructor's phone.

## Wireframe

```text
+--------------------------------------------------------------------------------------------------+
| Week 47   Instructor Mr Roche (category B, authorised until 2028-03-31)     [Book a lesson]      |
| Lesson      Learner       Date and time        Vehicle    State                                  |
| DL-2026-310 Sofia B.      2026-11-21 10:00     Car 3      Booked                                 |
| DL-2026-311 Marc T.       2026-11-21 11:00     Car 3      Booked                                 |
| DL-2026-309 Sofia B.      2026-11-14 10:00     Car 3      Done   1 h   Booklet updated           |
| Learner Sofia B.: 21 hours of 20 needed     Exam booked 2026-12-04                               |
+--------------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC12-06 step 2, U38 | desktop | ![FL-SC12-06 step 2, U38, light](../../images/06-apprentices-driving-nurseries-and-canteens/u38-training-coordinator/2-driving-school-desktop-light.png) | ![FL-SC12-06 step 2, U38, dark](../../images/06-apprentices-driving-nurseries-and-canteens/u38-training-coordinator/2-driving-school-desktop-dark.png) |
| Error E1, U38 | desktop | ![Error E1, U38, light](../../images/06-apprentices-driving-nurseries-and-canteens/u38-training-coordinator/e1-the-instructor-is-not-authorised-desktop-light.png) | ![Error E1, U38, dark](../../images/06-apprentices-driving-nurseries-and-canteens/u38-training-coordinator/e1-the-instructor-is-not-authorised-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc12-22-driving-school-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc12-22-driving-school-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc12-22-driving-school-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc12-22-driving-school-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc12-22-driving-school-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc12-22-driving-school-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-sc12-22-driving-school-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-sc12-22-driving-school-offline-desktop-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Learner | E-SC12-21 learner | link | yes while Booked | yes |
| Instructor | E-SC12-21 instructor | trainer link | yes while Booked | yes |
| Vehicle | E-SC12-21 vehicle | choice | yes while Booked | yes |
| Date, time and length | E-SC12-21 date, time, hours | date, time, number | yes while Booked | yes |
| Booklet entry | E-SC12-21 booklet entry | text | yes while Booked | no |
| Category | E-SC12-21 category | choice | yes while Booked | yes |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Book | planning | learner, coordinator | a lesson Booked with an authorised instructor |
| Start and end | lesson | instructor | the lesson becomes Done with its booklet entry |
| Cancel | lesson | learner, coordinator | the lesson becomes Cancelled |
| Mark as missed | lesson | instructor | the lesson becomes Missed |

## States

- Normal: the week's lessons per instructor and vehicle, with the learner's hours.
- Empty: No lesson yet, with Book a lesson.
- Loading: the headings and the table as placeholders; the values follow.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); an instructor
  not authorised or a vehicle not available, with the alternatives.
- Read-only: the record in a locked state: values shown, no action offered.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-SC12-21 Driving lesson](../../data/e-sc12-21-driving-lesson.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC12-21 Driving lesson | Booked | Badge "Booked"; a new record starts here; next: Done, Cancelled or Missed (UC-SC12-22); fields editable within the role | U38, U39 | `u38-training-coordinator/s-sc12-22-driving-school-e-sc12-21-driving-lesson-booked-desktop-{light,dark}.png`, `u39-trainer/s-sc12-22-driving-school-e-sc12-21-driving-lesson-booked-{desktop,phone,tablet}-{light,dark}.png` |
| E-SC12-21 Driving lesson | Done | Badge "Done"; final: read-only, no next state; the history shows how it got here | U38, U39 | `u38-training-coordinator/s-sc12-22-driving-school-e-sc12-21-driving-lesson-done-desktop-{light,dark}.png`, `u39-trainer/s-sc12-22-driving-school-e-sc12-21-driving-lesson-done-{desktop,phone,tablet}-{light,dark}.png` |
| E-SC12-21 Driving lesson | Cancelled | Badge "Cancelled"; final: read-only, no next state; the history shows how it got here | U38, U39 | `u38-training-coordinator/s-sc12-22-driving-school-e-sc12-21-driving-lesson-cancelled-desktop-{light,dark}.png`, `u39-trainer/s-sc12-22-driving-school-e-sc12-21-driving-lesson-cancelled-{desktop,phone,tablet}-{light,dark}.png` |
| E-SC12-21 Driving lesson | Missed | Badge "Missed"; final: read-only, no next state; the history shows how it got here | U38, U39 | `u38-training-coordinator/s-sc12-22-driving-school-e-sc12-21-driving-lesson-missed-desktop-{light,dark}.png`, `u39-trainer/s-sc12-22-driving-school-e-sc12-21-driving-lesson-missed-{desktop,phone,tablet}-{light,dark}.png` |

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

⬅️ [S-SC12-21 Apprentice training centre](s-sc12-21-cfa.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC12-23 Nursery](s-sc12-23-nursery.md)
