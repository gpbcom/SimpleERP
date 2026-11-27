🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🎓 [SC12 Education and training](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC12-05 Private school](README.md) › 🖥️ S-SC12-18 Pupil attendance

# 🖥️ S-SC12-18 Pupil attendance

**Status:** 🔄 waiting for the owner

## Personas

- [U39 Trainer](../../../../01-users/personas/u39-trainer.md)
- [U09 Customer](../../../../01-users/personas/u09-customer.md)

## Purpose

Used to follow pupils' attendance and inform parents,
[UC-SC12-18](../../use-cases/05-private-school/uc-sc12-18-follow-pupils-attendance-and-inform-parents.md).

## Entry points

Education and training in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC12-05 step 3, U39 | phone | ![FL-SC12-05 step 3, U39, light](../../images/05-private-school/u39-trainer/3-absences-phone-light.png) | ![FL-SC12-05 step 3, U39, dark](../../images/05-private-school/u39-trainer/3-absences-phone-dark.png) |
| FL-SC12-05 step 3, U39 | desktop | ![FL-SC12-05 step 3, U39, light](../../images/05-private-school/u39-trainer/3-absences-desktop-light.png) | ![FL-SC12-05 step 3, U39, dark](../../images/05-private-school/u39-trainer/3-absences-desktop-dark.png) |
| FL-SC12-05 step 3, U39 | tablet | ![FL-SC12-05 step 3, U39, light](../../images/05-private-school/u39-trainer/3-absences-tablet-light.png) | ![FL-SC12-05 step 3, U39, dark](../../images/05-private-school/u39-trainer/3-absences-tablet-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc12-18-pupil-attendance-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc12-18-pupil-attendance-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc12-18-pupil-attendance-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc12-18-pupil-attendance-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc12-18-pupil-attendance-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc12-18-pupil-attendance-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc12-18-pupil-attendance-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc12-18-pupil-attendance-offline-phone-dark.png) |

## Fields and columns

The fields of [E-SC12-17 Pupil absence](../../data/e-sc12-17-pupil-absence.md), shown as the entity pages list them,
with their examples.

## Actions

- Take attendance:
  [UC-SC12-18](../../use-cases/05-private-school/uc-sc12-18-follow-pupils-attendance-and-inform-parents.md), step 1.
- Notify parents:
  [UC-SC12-18](../../use-cases/05-private-school/uc-sc12-18-follow-pupils-attendance-and-inform-parents.md), step 2.
- Give the reason:
  [UC-SC12-18](../../use-cases/05-private-school/uc-sc12-18-follow-pupils-attendance-and-inform-parents.md), step 3.
- Record: [UC-SC12-18](../../use-cases/05-private-school/uc-sc12-18-follow-pupils-attendance-and-inform-parents.md),
  step 4.

## States

- Normal: the lesson's pupils with present or absent and reasons.
- Empty: "No lesson now".
- Loading: the frame and titles show at once with placeholder rows; within 1 second
  ([D408](../../../../06-decisions/technical/d408-performance-and-profiles.md)) the data replaces them, and a longer
  load shows a progress line saying what loads.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)) says what failed
  and what to do; what was typed is kept. For example, no contact: the office calls.
- Read-only: past days are read-only.
- Offline: attendance taken without network is kept and synced; parents are told once synced,
  [UC-F2-22](../../../../02-functional/f02-no-code-configuration/use-cases/09-portals-and-offline-forms/uc-f02-22-fill-a-form-offline-on-the-phone.md).

Shown entities (VD-15): [E-SC12-17 Pupil absence](../../data/e-sc12-17-pupil-absence.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC12-17 Pupil absence | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U09, U38, U39 | `u09-customer/s-sc12-18-pupil-attendance-e-sc12-17-pupil-absence-active-phone-{light,dark}.png`, `u38-training-coordinator/s-sc12-18-pupil-attendance-e-sc12-17-pupil-absence-active-desktop-{light,dark}.png`, `u39-trainer/s-sc12-18-pupil-attendance-e-sc12-17-pupil-absence-active-{desktop,phone,tablet}-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

(Proposed) Desktop; approvals and receipts also on the phone.

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

⬅️ [S-SC12-17 Grades](s-sc12-17-grades.md) · ⬆️ [Up](README.md) · ➡️ [S-SC12-19 School fees](s-sc12-19-school-fees.md)
