🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🎓 [SC12 Education and training](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC12-05 Private school](README.md) › 🖥️ S-SC12-19 School fees

# 🖥️ S-SC12-19 School fees

**Status:** 🔄 waiting for the owner

## Personas

- [U05 Accounting](../../../../01-users/personas/u05-accounting.md)
- [U09 Customer](../../../../01-users/personas/u09-customer.md)

## Purpose

Used to enrol students in a private school
([UC-SC12-15](../../use-cases/05-private-school/uc-sc12-15-enrol-students-in-a-private-school.md)); to bill school fees
and grants ([UC-SC12-19](../../use-cases/05-private-school/uc-sc12-19-bill-school-fees-and-grants.md)).

## Entry points

Education and training in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC12-05 step 1, U05 | desktop | ![FL-SC12-05 step 1, U05, light](../../images/05-private-school/u05-accounting/1-school-enrolment-desktop-light.png) | ![FL-SC12-05 step 1, U05, dark](../../images/05-private-school/u05-accounting/1-school-enrolment-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc12-19-school-fees-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc12-19-school-fees-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc12-19-school-fees-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc12-19-school-fees-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc12-19-school-fees-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc12-19-school-fees-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-sc12-19-school-fees-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-sc12-19-school-fees-offline-desktop-dark.png) |

## Fields and columns

The fields of [E-SC12-14 Student](../../data/e-sc12-14-student.md),
[E-SC12-18 School fee](../../data/e-sc12-18-school-fee.md),
[E-F8-18 Grant](../../../../02-functional/f08-accounting/data/e-f08-18-grant.md), shown as the entity pages list them,
with their examples.

## Actions

- Set fees: [UC-SC12-15](../../use-cases/05-private-school/uc-sc12-15-enrol-students-in-a-private-school.md), step 4.
- Bill: [UC-SC12-19](../../use-cases/05-private-school/uc-sc12-19-bill-school-fees-and-grants.md), step 1.
- Pay: [UC-SC12-19](../../use-cases/05-private-school/uc-sc12-19-bill-school-fees-and-grants.md), step 2.
- Collect: [UC-SC12-19](../../use-cases/05-private-school/uc-sc12-19-bill-school-fees-and-grants.md), step 3.
- Apply grants: [UC-SC12-19](../../use-cases/05-private-school/uc-sc12-19-bill-school-fees-and-grants.md), step 4.

## States

- Normal: fees per student and period, payments and grants.
- Empty: "No fee".
- Loading: the frame and titles show at once with placeholder rows; within 1 second
  ([D408](../../../../06-decisions/technical/d408-performance-and-profiles.md)) the data replaces them, and a longer
  load shows a progress line saying what loads.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)) says what failed
  and what to do; what was typed is kept. For example, the school not open yet: enrolment is blocked
  ([BR-SC12-11](../../business-rules/br-sc12-11-school-opened-after-declaration.md)).
- Read-only: parents read their own.
- Offline: not available offline: office work on enrolments, funding and billing. Offline work is kept for the phone
  forms of the field, [D38](../../../../06-decisions/ux/d38-offline-field-tasks.md),
  [UC-F2-22](../../../../02-functional/f02-no-code-configuration/use-cases/09-portals-and-offline-forms/uc-f02-22-fill-a-form-offline-on-the-phone.md).
  A banner says the connection is lost; what is on screen stays visible, every action is disabled and nothing is queued
  until the connection is back.

Shown entities (VD-15): [E-SC12-14 Student](../../data/e-sc12-14-student.md),
[E-SC12-18 School fee](../../data/e-sc12-18-school-fee.md),
[E-F8-18 Grant](../../../../02-functional/f08-accounting/data/e-f08-18-grant.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC12-14 Student | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U05, U09, U38 | `u05-accounting/s-sc12-19-school-fees-e-sc12-14-student-active-desktop-{light,dark}.png`, `u09-customer/s-sc12-19-school-fees-e-sc12-14-student-active-phone-{light,dark}.png`, `u38-training-coordinator/s-sc12-19-school-fees-e-sc12-14-student-active-desktop-{light,dark}.png` |
| E-SC12-18 School fee | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U05, U09, U38 | `u05-accounting/s-sc12-19-school-fees-e-sc12-18-school-fee-active-desktop-{light,dark}.png`, `u09-customer/s-sc12-19-school-fees-e-sc12-18-school-fee-active-phone-{light,dark}.png`, `u38-training-coordinator/s-sc12-19-school-fees-e-sc12-18-school-fee-active-desktop-{light,dark}.png` |
| E-F8-18 Grant | Granted | Badge "Granted"; a new record starts here; next: Received (UC-SC12-19); fields editable within the role | U05, U09, U38 | `u05-accounting/s-sc12-19-school-fees-e-f08-18-grant-granted-desktop-{light,dark}.png`, `u09-customer/s-sc12-19-school-fees-e-f08-18-grant-granted-phone-{light,dark}.png`, `u38-training-coordinator/s-sc12-19-school-fees-e-f08-18-grant-granted-desktop-{light,dark}.png` |
| E-F8-18 Grant | Received | Badge "Received"; next: Closed (UC-F8-22); fields editable within the role | U05, U09, U38 | `u05-accounting/s-sc12-19-school-fees-e-f08-18-grant-received-desktop-{light,dark}.png`, `u09-customer/s-sc12-19-school-fees-e-f08-18-grant-received-phone-{light,dark}.png`, `u38-training-coordinator/s-sc12-19-school-fees-e-f08-18-grant-received-desktop-{light,dark}.png` |

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

⬅️ [S-SC12-18 Pupil attendance](s-sc12-18-pupil-attendance.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC12-20 Training assistant](../03-deliver-and-assess/s-sc12-20-training-assistant.md)
