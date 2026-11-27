🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🎓 [SC12 Education and training](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC12-03 Deliver and assess](README.md) › 🖥️ S-SC12-09 Satisfaction

# 🖥️ S-SC12-09 Satisfaction

**Status:** ✅ specified

## Personas

- [U38 Training coordinator](../../../../01-users/personas/u38-training-coordinator.md)
- [U09 Customer](../../../../01-users/personas/u09-customer.md)

## Purpose

Used to collect satisfaction ([UC-SC12-09](../../use-cases/03-deliver-and-assess/uc-sc12-09-collect-satisfaction.md)).

## Entry points

Education and training in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC12-03 step 4, U38 | desktop | ![FL-SC12-03 step 4, U38, light](../../images/03-deliver-and-assess/u38-training-coordinator/4-satisfaction-desktop-light.png) | ![FL-SC12-03 step 4, U38, dark](../../images/03-deliver-and-assess/u38-training-coordinator/4-satisfaction-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc12-09-satisfaction-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc12-09-satisfaction-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc12-09-satisfaction-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc12-09-satisfaction-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc12-09-satisfaction-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc12-09-satisfaction-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-sc12-09-satisfaction-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-sc12-09-satisfaction-offline-desktop-dark.png) |

## Fields and columns

The fields of [E-SC12-09 Survey answer](../../data/e-sc12-09-survey-answer.md), shown as the entity pages list them,
with their examples.

## Actions

- Send: [UC-SC12-09](../../use-cases/03-deliver-and-assess/uc-sc12-09-collect-satisfaction.md), step 1.
- Answer: [UC-SC12-09](../../use-cases/03-deliver-and-assess/uc-sc12-09-collect-satisfaction.md), step 2.
- Analyse: [UC-SC12-09](../../use-cases/03-deliver-and-assess/uc-sc12-09-collect-satisfaction.md), step 3.
- Keep as evidence: [UC-SC12-09](../../use-cases/03-deliver-and-assess/uc-sc12-09-collect-satisfaction.md), step 4.

## States

- Normal: survey answers and scores per session.
- Empty: "No answer".
- Loading: the frame and titles show at once with placeholder rows; within 1 second
  ([D408](../../../../06-decisions/technical/d408-performance-and-profiles.md)) the data replaces them, and a longer
  load shows a progress line saying what loads.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)) says what failed
  and what to do; what was typed is kept. For example, a low score: an action is opened.
- Read-only: answers are read-only.
- Offline: not available offline: office work on enrolments, funding and billing. Offline work is kept for the phone
  forms of the field, [D38](../../../../06-decisions/ux/d38-offline-field-tasks.md),
  [UC-F2-22](../../../../02-functional/f02-no-code-configuration/use-cases/09-portals-and-offline-forms/uc-f02-22-fill-a-form-offline-on-the-phone.md).
  A banner says the connection is lost; what is on screen stays visible, every action is disabled and nothing is queued
  until the connection is back.

Shown entities (VD-15): [E-SC12-09 Survey answer](../../data/e-sc12-09-survey-answer.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC12-09 Survey answer | Recorded | Badge "Recorded"; a new record starts here; no other state; fields editable within the role | U09, U38 | `u09-customer/s-sc12-09-satisfaction-e-sc12-09-survey-answer-recorded-phone-{light,dark}.png`, `u38-training-coordinator/s-sc12-09-satisfaction-e-sc12-09-survey-answer-recorded-desktop-{light,dark}.png` |

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

- [FL-SC12-03 Deliver and assess](../../flows/fl-sc12-03-deliver-and-assess.md)

## Open questions

None.

---

⬅️ [S-SC12-08 Certificates](s-sc12-08-certificates.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC12-10 Billing](../02-enrol-and-fund/s-sc12-10-billing.md)
