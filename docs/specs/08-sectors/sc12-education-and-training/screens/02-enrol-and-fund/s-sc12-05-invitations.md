🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🎓 [SC12 Education and training](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC12-02 Enrol and fund](README.md) › 🖥️ S-SC12-05 Invitations

# 🖥️ S-SC12-05 Invitations

**Status:** 🔄 waiting for the owner

## Personas

- [U38 Training coordinator](../../../../01-users/personas/u38-training-coordinator.md)
- [U09 Customer](../../../../01-users/personas/u09-customer.md)

## Purpose

Used to send invitations and needs assessments
([UC-SC12-05](../../use-cases/02-enrol-and-fund/uc-sc12-05-send-invitations-and-needs-assessments.md)).

## Entry points

Education and training in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC12-02 step 3, U38 | desktop | ![FL-SC12-02 step 3, U38, light](../../images/02-enrol-and-fund/u38-training-coordinator/3-invitation-desktop-light.png) | ![FL-SC12-02 step 3, U38, dark](../../images/02-enrol-and-fund/u38-training-coordinator/3-invitation-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc12-05-invitations-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc12-05-invitations-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc12-05-invitations-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc12-05-invitations-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc12-05-invitations-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc12-05-invitations-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-sc12-05-invitations-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-sc12-05-invitations-offline-desktop-dark.png) |

## Fields and columns

The fields of [E-SC12-03 Enrolment](../../data/e-sc12-03-enrolment.md), shown as the entity pages list them, with their
examples.

## Actions

- Send: [UC-SC12-05](../../use-cases/02-enrol-and-fund/uc-sc12-05-send-invitations-and-needs-assessments.md), step 1.
- Answer: [UC-SC12-05](../../use-cases/02-enrol-and-fund/uc-sc12-05-send-invitations-and-needs-assessments.md), step 2.
- Share: [UC-SC12-05](../../use-cases/02-enrol-and-fund/uc-sc12-05-send-invitations-and-needs-assessments.md), step 3.
- Keep as evidence:
  [UC-SC12-05](../../use-cases/02-enrol-and-fund/uc-sc12-05-send-invitations-and-needs-assessments.md), step 4.

## States

- Normal: invitations, questionnaires and answers.
- Empty: "No invitation".
- Loading: the frame and titles show at once with placeholder rows; within 1 second
  ([D408](../../../../06-decisions/technical/d408-performance-and-profiles.md)) the data replaces them, and a longer
  load shows a progress line saying what loads.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)) says what failed
  and what to do; what was typed is kept. For example, no answer: a reminder is sent.
- Read-only: sent ones are read-only.
- Offline: not available offline: office work on enrolments, funding and billing. Offline work is kept for the phone
  forms of the field, [D38](../../../../06-decisions/ux/d38-offline-field-tasks.md),
  [UC-F2-22](../../../../02-functional/f02-no-code-configuration/use-cases/09-portals-and-offline-forms/uc-f02-22-fill-a-form-offline-on-the-phone.md).
  A banner says the connection is lost; what is on screen stays visible, every action is disabled and nothing is queued
  until the connection is back.

Shown entities (VD-15): [E-F1-04 Invitation](../../../../02-functional/f01-administration/data/e-f01-04-invitation.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F1-04 Invitation | Sent | Badge "Sent"; a new record starts here; next: Accepted, Expired, Cancelled or Not delivered (UC-F1-03); fields editable within the role | U09, U38 | `u09-customer/s-sc12-05-invitations-e-f01-04-invitation-sent-phone-{light,dark}.png`, `u38-training-coordinator/s-sc12-05-invitations-e-f01-04-invitation-sent-desktop-{light,dark}.png` |
| E-F1-04 Invitation | Accepted | Badge "Accepted"; final: read-only, no next state; the history shows how it got here | U09, U38 | `u09-customer/s-sc12-05-invitations-e-f01-04-invitation-accepted-phone-{light,dark}.png`, `u38-training-coordinator/s-sc12-05-invitations-e-f01-04-invitation-accepted-desktop-{light,dark}.png` |
| E-F1-04 Invitation | Expired | Badge "Expired"; final: read-only, no next state; the history shows how it got here | U09, U38 | `u09-customer/s-sc12-05-invitations-e-f01-04-invitation-expired-phone-{light,dark}.png`, `u38-training-coordinator/s-sc12-05-invitations-e-f01-04-invitation-expired-desktop-{light,dark}.png` |
| E-F1-04 Invitation | Cancelled | Badge "Cancelled"; final: read-only, no next state; the history shows how it got here | U09, U38 | `u09-customer/s-sc12-05-invitations-e-f01-04-invitation-cancelled-phone-{light,dark}.png`, `u38-training-coordinator/s-sc12-05-invitations-e-f01-04-invitation-cancelled-desktop-{light,dark}.png` |
| E-F1-04 Invitation | Not delivered | Badge "Not delivered"; final: read-only, no next state; the history shows how it got here | U09, U38 | `u09-customer/s-sc12-05-invitations-e-f01-04-invitation-not-delivered-phone-{light,dark}.png`, `u38-training-coordinator/s-sc12-05-invitations-e-f01-04-invitation-not-delivered-desktop-{light,dark}.png` |

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

- [FL-SC12-02 Enrol and fund](../../flows/fl-sc12-02-enrol-and-fund.md)

## Open questions

None.

---

⬅️ [S-SC12-04 Funding](s-sc12-04-funding.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC12-06 Attendance](../03-deliver-and-assess/s-sc12-06-attendance.md)
