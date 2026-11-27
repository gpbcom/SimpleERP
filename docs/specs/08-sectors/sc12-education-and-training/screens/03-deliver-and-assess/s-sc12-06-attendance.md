🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🎓 [SC12 Education and training](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC12-03 Deliver and assess](README.md) › 🖥️ S-SC12-06 Attendance

# 🖥️ S-SC12-06 Attendance

**Status:** ✅ specified

## Personas

- [U39 Trainer](../../../../01-users/personas/u39-trainer.md)
- [U09 Customer](../../../../01-users/personas/u09-customer.md)

## Purpose

Used to sign attendance per half-day
([UC-SC12-06](../../use-cases/03-deliver-and-assess/uc-sc12-06-sign-attendance-per-half-day.md)).

## Entry points

Education and training in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC12-03 step 1, U39 | phone | ![FL-SC12-03 step 1, U39, light](../../images/03-deliver-and-assess/u39-trainer/1-attendance-phone-light.png) | ![FL-SC12-03 step 1, U39, dark](../../images/03-deliver-and-assess/u39-trainer/1-attendance-phone-dark.png) |
| FL-SC12-03 step 1, U39 | desktop | ![FL-SC12-03 step 1, U39, light](../../images/03-deliver-and-assess/u39-trainer/1-attendance-desktop-light.png) | ![FL-SC12-03 step 1, U39, dark](../../images/03-deliver-and-assess/u39-trainer/1-attendance-desktop-dark.png) |
| FL-SC12-03 step 1, U39 | tablet | ![FL-SC12-03 step 1, U39, light](../../images/03-deliver-and-assess/u39-trainer/1-attendance-tablet-light.png) | ![FL-SC12-03 step 1, U39, dark](../../images/03-deliver-and-assess/u39-trainer/1-attendance-tablet-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc12-06-attendance-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc12-06-attendance-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc12-06-attendance-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc12-06-attendance-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc12-06-attendance-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc12-06-attendance-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc12-06-attendance-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc12-06-attendance-offline-phone-dark.png) |

## Fields and columns

The fields of [E-SC12-06 Attendance sheet](../../data/e-sc12-06-attendance-sheet.md), shown as the entity pages list
them, with their examples.

## Actions

- Open the sheet: [UC-SC12-06](../../use-cases/03-deliver-and-assess/uc-sc12-06-sign-attendance-per-half-day.md), step
  1.
- Sign: [UC-SC12-06](../../use-cases/03-deliver-and-assess/uc-sc12-06-sign-attendance-per-half-day.md), step 2.
- Confirm: [UC-SC12-06](../../use-cases/03-deliver-and-assess/uc-sc12-06-sign-attendance-per-half-day.md), step 3.
- Check: [UC-SC12-06](../../use-cases/03-deliver-and-assess/uc-sc12-06-sign-attendance-per-half-day.md), step 4.

## States

- Normal: the half-day's learners and signatures.
- Empty: "No sheet today".
- Loading: the frame and titles show at once with placeholder rows; within 1 second
  ([D408](../../../../06-decisions/technical/d408-performance-and-profiles.md)) the data replaces them, and a longer
  load shows a progress line saying what loads.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)) says what failed
  and what to do; what was typed is kept. For example, a missing signature: it is flagged.
- Read-only: confirmed sheets are read-only.
- Offline: works offline,
  [UC-F2-22](../../../../02-functional/f02-no-code-configuration/use-cases/09-portals-and-offline-forms/uc-f02-22-fill-a-form-offline-on-the-phone.md),
  the day's sheets are kept on the tablet; signatures sync in order,
  [BR-F2-21](../../../../02-functional/f02-no-code-configuration/business-rules/br-f02-21-offline-forms-keep-only-what-is-needed-and-sync-in-order.md).

Shown entities (VD-15): [E-SC12-06 Attendance sheet](../../data/e-sc12-06-attendance-sheet.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC12-06 Attendance sheet | Confirmed | Badge "Confirmed"; a new record starts here; next: Complete (UC-SC12-06); fields editable within the role | U09, U38, U39 | `u09-customer/s-sc12-06-attendance-e-sc12-06-attendance-sheet-confirmed-phone-{light,dark}.png`, `u38-training-coordinator/s-sc12-06-attendance-e-sc12-06-attendance-sheet-confirmed-desktop-{light,dark}.png`, `u39-trainer/s-sc12-06-attendance-e-sc12-06-attendance-sheet-confirmed-{desktop,phone,tablet}-{light,dark}.png` |
| E-SC12-06 Attendance sheet | Complete | Badge "Complete"; final: read-only, no next state; the history shows how it got here | U09, U38, U39 | `u09-customer/s-sc12-06-attendance-e-sc12-06-attendance-sheet-complete-phone-{light,dark}.png`, `u38-training-coordinator/s-sc12-06-attendance-e-sc12-06-attendance-sheet-complete-desktop-{light,dark}.png`, `u39-trainer/s-sc12-06-attendance-e-sc12-06-attendance-sheet-complete-{desktop,phone,tablet}-{light,dark}.png` |

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

⬅️ [S-SC12-05 Invitations](../02-enrol-and-fund/s-sc12-05-invitations.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC12-07 E-learning](s-sc12-07-e-learning.md)
