🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🏠 [SC04 Home care](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC04-05 People and quality](README.md) › 🖥️ S-SC04-13 Carer skills

# 🖥️ S-SC04-13 Carer skills

**Status:** ✅ specified

## Personas

- [U25 Care coordinator](../../../../01-users/personas/u25-care-coordinator.md)
- [U06 HR](../../../../01-users/personas/u06-hr.md)

## Purpose

Used to manage carers' skills and training
([UC-SC04-13](../../use-cases/05-people-and-quality/uc-sc04-13-manage-carers-skills-and-training.md)).

## Entry points

Home care in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC04-05 step 3, U25 | desktop | ![FL-SC04-05 step 3, U25, light](../../images/05-people-and-quality/u25-care-coordinator/3-skills-desktop-light.png) | ![FL-SC04-05 step 3, U25, dark](../../images/05-people-and-quality/u25-care-coordinator/3-skills-desktop-dark.png) |
| FL-SC04-05 step 3, U25 | phone | ![FL-SC04-05 step 3, U25, light](../../images/05-people-and-quality/u25-care-coordinator/3-skills-phone-light.png) | ![FL-SC04-05 step 3, U25, dark](../../images/05-people-and-quality/u25-care-coordinator/3-skills-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc04-13-carer-skills-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc04-13-carer-skills-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc04-13-carer-skills-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc04-13-carer-skills-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc04-13-carer-skills-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc04-13-carer-skills-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc04-13-carer-skills-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc04-13-carer-skills-offline-phone-dark.png) |

## Fields and columns

The fields of [E-SC04-11 Carer qualification](../../data/e-sc04-11-carer-qualification.md), shown as the entity pages
list them, with their examples.

## Actions

- Record skills: [UC-SC04-13](../../use-cases/05-people-and-quality/uc-sc04-13-manage-carers-skills-and-training.md),
  step 1.
- Plan training: [UC-SC04-13](../../use-cases/05-people-and-quality/uc-sc04-13-manage-carers-skills-and-training.md),
  step 2.
- Use in planning: [UC-SC04-13](../../use-cases/05-people-and-quality/uc-sc04-13-manage-carers-skills-and-training.md),
  step 3.
- Pair with a tutor:
  [UC-SC04-13](../../use-cases/05-people-and-quality/uc-sc04-13-manage-carers-skills-and-training.md), step 4.

## States

- Normal: carers' qualifications with expiry and planned training.
- Empty: "No qualification recorded".
- Loading: the frame and titles show at once with placeholder rows; within 1 second
  ([D408](../../../../06-decisions/technical/d408-performance-and-profiles.md)) the data replaces them, and a longer
  load shows a progress line saying what loads.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)) says what failed
  and what to do; what was typed is kept. For example, an expired qualification: the carer is not assigned to visits
  needing it.
- Read-only: carers read their own.
- Offline: not available offline: office work at the agency on shared planning and billing data. Offline work is kept
  for the phone forms of the field, [D38](../../../../06-decisions/ux/d38-offline-field-tasks.md),
  [UC-F2-22](../../../../02-functional/f02-no-code-configuration/use-cases/09-portals-and-offline-forms/uc-f02-22-fill-a-form-offline-on-the-phone.md).
  A banner says the connection is lost; what is on screen stays visible, every action is disabled and nothing is queued
  until the connection is back.

Shown entities (VD-15): [E-SC04-11 Carer qualification](../../data/e-sc04-11-carer-qualification.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC04-11 Carer qualification | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U06, U25 | `u06-hr/s-sc04-13-carer-skills-e-sc04-11-carer-qualification-active-desktop-{light,dark}.png`, `u25-care-coordinator/s-sc04-13-carer-skills-e-sc04-11-carer-qualification-active-{desktop,phone}-{light,dark}.png` |

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

- [FL-SC04-05 People and quality](../../flows/fl-sc04-05-people-and-quality.md)

## Open questions

None.

---

⬅️ [S-SC04-12 Quality](s-sc04-12-quality.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC04-14 Activity reports](s-sc04-14-activity-reports.md)
