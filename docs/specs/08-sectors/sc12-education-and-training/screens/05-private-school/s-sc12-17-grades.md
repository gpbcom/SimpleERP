🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🎓 [SC12 Education and training](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC12-05 Private school](README.md) › 🖥️ S-SC12-17 Grades

# 🖥️ S-SC12-17 Grades

**Status:** ✅ specified

## Personas

- [U39 Trainer](../../../../01-users/personas/u39-trainer.md)
- [U38 Training coordinator](../../../../01-users/personas/u38-training-coordinator.md)

## Purpose

Used to record grades and report cards
([UC-SC12-17](../../use-cases/05-private-school/uc-sc12-17-record-grades-and-report-cards.md)).

## Entry points

Education and training in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC12-05 step 4, U39 | phone | ![FL-SC12-05 step 4, U39, light](../../images/05-private-school/u39-trainer/4-grades-phone-light.png) | ![FL-SC12-05 step 4, U39, dark](../../images/05-private-school/u39-trainer/4-grades-phone-dark.png) |
| FL-SC12-05 step 4, U39 | desktop | ![FL-SC12-05 step 4, U39, light](../../images/05-private-school/u39-trainer/4-grades-desktop-light.png) | ![FL-SC12-05 step 4, U39, dark](../../images/05-private-school/u39-trainer/4-grades-desktop-dark.png) |
| FL-SC12-05 step 4, U39 | tablet | ![FL-SC12-05 step 4, U39, light](../../images/05-private-school/u39-trainer/4-grades-tablet-light.png) | ![FL-SC12-05 step 4, U39, dark](../../images/05-private-school/u39-trainer/4-grades-tablet-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc12-17-grades-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc12-17-grades-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc12-17-grades-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc12-17-grades-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc12-17-grades-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc12-17-grades-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc12-17-grades-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc12-17-grades-offline-phone-dark.png) |

## Fields and columns

The fields of [E-SC12-16 Grade](../../data/e-sc12-16-grade.md), shown as the entity pages list them, with their
examples.

## Actions

- Enter grades: [UC-SC12-17](../../use-cases/05-private-school/uc-sc12-17-record-grades-and-report-cards.md), step 1.
- Hold the council: [UC-SC12-17](../../use-cases/05-private-school/uc-sc12-17-record-grades-and-report-cards.md), step
  2.
- Lock: [UC-SC12-17](../../use-cases/05-private-school/uc-sc12-17-record-grades-and-report-cards.md), step 3.
- Publish: [UC-SC12-17](../../use-cases/05-private-school/uc-sc12-17-record-grades-and-report-cards.md), step 4.

## States

- Normal: grades per student and subject, councils and report cards.
- Empty: "No grade".
- Loading: the frame and titles show at once with placeholder rows; within 1 second
  ([D408](../../../../06-decisions/technical/d408-performance-and-profiles.md)) the data replaces them, and a longer
  load shows a progress line saying what loads.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)) says what failed
  and what to do; what was typed is kept. For example, a change after the council: it is refused.
- Read-only: locked after the council.
- Offline: not available offline: office work on enrolments, funding and billing. Offline work is kept for the phone
  forms of the field, [D38](../../../../06-decisions/ux/d38-offline-field-tasks.md),
  [UC-F2-22](../../../../02-functional/f02-no-code-configuration/use-cases/09-portals-and-offline-forms/uc-f02-22-fill-a-form-offline-on-the-phone.md).
  A banner says the connection is lost; what is on screen stays visible, every action is disabled and nothing is queued
  until the connection is back.

Shown entities (VD-15): [E-SC12-16 Grade](../../data/e-sc12-16-grade.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC12-16 Grade | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U09, U38, U39 | `u09-customer/s-sc12-17-grades-e-sc12-16-grade-active-phone-{light,dark}.png`, `u38-training-coordinator/s-sc12-17-grades-e-sc12-16-grade-active-desktop-{light,dark}.png`, `u39-trainer/s-sc12-17-grades-e-sc12-16-grade-active-{desktop,phone,tablet}-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop; approvals and receipts also on the phone.

## Accessibility

Labelled controls; amounts and states as text.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)

## Shown in

- [FL-SC12-05 Private school](../../flows/fl-sc12-05-private-school.md)

## Open questions

None.

---

⬅️ [S-SC12-16 Timetables](s-sc12-16-timetables.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC12-18 Pupil attendance](s-sc12-18-pupil-attendance.md)
