🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🎓 [SC12 Education and training](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC12-03 Deliver and assess](README.md) › 🖥️ S-SC12-07 E-learning

# 🖥️ S-SC12-07 E-learning

**Status:** ✅ specified

## Personas

- [U09 Customer](../../../../01-users/personas/u09-customer.md)
- [U38 Training coordinator](../../../../01-users/personas/u38-training-coordinator.md)

## Purpose

Used to run e-learning modules
([UC-SC12-07](../../use-cases/03-deliver-and-assess/uc-sc12-07-run-e-learning-modules.md)).

## Entry points

Education and training in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC12-03 step 2, U09 | phone | ![FL-SC12-03 step 2, U09, light](../../images/03-deliver-and-assess/u09-customer/2-e-learning-phone-light.png) | ![FL-SC12-03 step 2, U09, dark](../../images/03-deliver-and-assess/u09-customer/2-e-learning-phone-dark.png) |
| Empty | phone | ![Empty, light](../../images/states/s-sc12-07-e-learning-empty-phone-light.png) | ![Empty, dark](../../images/states/s-sc12-07-e-learning-empty-phone-dark.png) |
| Loading | phone | ![Loading, light](../../images/states/s-sc12-07-e-learning-loading-phone-light.png) | ![Loading, dark](../../images/states/s-sc12-07-e-learning-loading-phone-dark.png) |
| Read-only | phone | ![Read-only, light](../../images/states/s-sc12-07-e-learning-read-only-phone-light.png) | ![Read-only, dark](../../images/states/s-sc12-07-e-learning-read-only-phone-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc12-07-e-learning-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc12-07-e-learning-offline-phone-dark.png) |

## Fields and columns

The fields of [E-SC12-07 E-learning record](../../data/e-sc12-07-e-learning-record.md), shown as the entity pages list
them, with their examples.

## Actions

- Assign: [UC-SC12-07](../../use-cases/03-deliver-and-assess/uc-sc12-07-run-e-learning-modules.md), step 1.
- Follow: [UC-SC12-07](../../use-cases/03-deliver-and-assess/uc-sc12-07-run-e-learning-modules.md), step 2.
- Import progress: [UC-SC12-07](../../use-cases/03-deliver-and-assess/uc-sc12-07-run-e-learning-modules.md), step 3.
- Count as attendance: [UC-SC12-07](../../use-cases/03-deliver-and-assess/uc-sc12-07-run-e-learning-modules.md), step 4.

## States

- Normal: modules assigned with progress and time.
- Empty: "No module".
- Loading: the frame and titles show at once with placeholder rows; within 1 second
  ([D408](../../../../06-decisions/technical/d408-performance-and-profiles.md)) the data replaces them, and a longer
  load shows a progress line saying what loads.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)) says what failed
  and what to do; what was typed is kept. For example, the platform down: it is shown and retried.
- Read-only: imported progress is read-only.
- Offline: not available offline: progress comes from the learning platform.

Shown entities (VD-15): [E-SC12-07 E-learning record](../../data/e-sc12-07-e-learning-record.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC12-07 E-learning record | Recorded | Badge "Recorded"; a new record starts here; no other state; fields editable within the role | U09, U38 | `u09-customer/s-sc12-07-e-learning-e-sc12-07-e-learning-record-recorded-phone-{light,dark}.png`, `u38-training-coordinator/s-sc12-07-e-learning-e-sc12-07-e-learning-record-recorded-desktop-{light,dark}.png` |

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

⬅️ [S-SC12-06 Attendance](s-sc12-06-attendance.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC12-08 Certificates](s-sc12-08-certificates.md)
