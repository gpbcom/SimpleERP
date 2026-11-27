🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🎓 [SC12 Education and training](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC12-02 Enrol and fund](README.md) › 🖥️ S-SC12-04 Funding

# 🖥️ S-SC12-04 Funding

**Status:** ✅ specified

## Personas

- [U38 Training coordinator](../../../../01-users/personas/u38-training-coordinator.md)
- [U05 Accounting](../../../../01-users/personas/u05-accounting.md)

## Purpose

Used to get funding ([UC-SC12-04](../../use-cases/02-enrol-and-fund/uc-sc12-04-get-funding.md)).

## Entry points

Education and training in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC12-02 step 2, U38 | desktop | ![FL-SC12-02 step 2, U38, light](../../images/02-enrol-and-fund/u38-training-coordinator/2-funding-desktop-light.png) | ![FL-SC12-02 step 2, U38, dark](../../images/02-enrol-and-fund/u38-training-coordinator/2-funding-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc12-04-funding-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc12-04-funding-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc12-04-funding-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc12-04-funding-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc12-04-funding-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc12-04-funding-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-sc12-04-funding-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-sc12-04-funding-offline-desktop-dark.png) |

## Fields and columns

The fields of [E-SC12-05 Training funding](../../data/e-sc12-05-training-funding.md),
[E-F6-14 Funder agreement](../../../../02-functional/f06-customers-and-sales/data/e-f06-14-funder-agreement.md), shown
as the entity pages list them, with their examples.

## Actions

- Request funding: [UC-SC12-04](../../use-cases/02-enrol-and-fund/uc-sc12-04-get-funding.md), step 1.
- Record the decision: [UC-SC12-04](../../use-cases/02-enrol-and-fund/uc-sc12-04-get-funding.md), step 2.
- Split the price: [UC-SC12-04](../../use-cases/02-enrol-and-fund/uc-sc12-04-get-funding.md), step 3.
- Tell the learner: [UC-SC12-04](../../use-cases/02-enrol-and-fund/uc-sc12-04-get-funding.md), step 4.

## States

- Normal: funding requests, decisions and each payer's share.
- Empty: "No funding".
- Loading: the frame and titles show at once with placeholder rows; within 1 second
  ([D408](../../../../06-decisions/technical/d408-performance-and-profiles.md)) the data replaces them, and a longer
  load shows a progress line saying what loads.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)) says what failed
  and what to do; what was typed is kept. For example, refused: the learner is told.
- Read-only: granted shares are read-only.
- Offline: not available offline: office work on enrolments, funding and billing. Offline work is kept for the phone
  forms of the field, [D38](../../../../06-decisions/ux/d38-offline-field-tasks.md),
  [UC-F2-22](../../../../02-functional/f02-no-code-configuration/use-cases/09-portals-and-offline-forms/uc-f02-22-fill-a-form-offline-on-the-phone.md).
  A banner says the connection is lost; what is on screen stays visible, every action is disabled and nothing is queued
  until the connection is back.

Shown entities (VD-15): [E-SC12-05 Training funding](../../data/e-sc12-05-training-funding.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC12-05 Training funding | Requested | Badge "Requested"; a new record starts here; next: Granted or Refused (UC-SC12-04); fields editable within the role | U05, U38 | `u05-accounting/s-sc12-04-funding-e-sc12-05-training-funding-requested-desktop-{light,dark}.png`, `u38-training-coordinator/s-sc12-04-funding-e-sc12-05-training-funding-requested-desktop-{light,dark}.png` |
| E-SC12-05 Training funding | Granted | Badge "Granted"; final: read-only, no next state; the history shows how it got here | U05, U38 | `u05-accounting/s-sc12-04-funding-e-sc12-05-training-funding-granted-desktop-{light,dark}.png`, `u38-training-coordinator/s-sc12-04-funding-e-sc12-05-training-funding-granted-desktop-{light,dark}.png` |
| E-SC12-05 Training funding | Refused | Badge "Refused"; final: read-only, no next state; the history shows how it got here | U05, U38 | `u05-accounting/s-sc12-04-funding-e-sc12-05-training-funding-refused-desktop-{light,dark}.png`, `u38-training-coordinator/s-sc12-04-funding-e-sc12-05-training-funding-refused-desktop-{light,dark}.png` |

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

- [FL-SC12-02 Enrol and fund](../../flows/fl-sc12-02-enrol-and-fund.md)

## Open questions

None.

---

⬅️ [S-SC12-03 Enrolment](s-sc12-03-enrolment.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC12-05 Invitations](s-sc12-05-invitations.md)
