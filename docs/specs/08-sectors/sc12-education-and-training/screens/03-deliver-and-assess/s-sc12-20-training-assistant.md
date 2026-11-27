🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🎓 [SC12 Education and training](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC12-03 Deliver and assess](README.md) › 🖥️ S-SC12-20 Training assistant

# 🖥️ S-SC12-20 Training assistant

**Status:** 🔄 waiting for the owner

## Personas

- [U38 Training coordinator](../../../../01-users/personas/u38-training-coordinator.md)
- [U39 Trainer](../../../../01-users/personas/u39-trainer.md)

## Purpose

Used to ask the AI assistant ([UC-SC12-20](../../use-cases/03-deliver-and-assess/uc-sc12-20-ask-the-assistant.md)).

## Entry points

Education and training in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC12-03 step 5, U38 | desktop | ![FL-SC12-03 step 5, U38, light](../../images/03-deliver-and-assess/u38-training-coordinator/5-assistant-desktop-light.png) | ![FL-SC12-03 step 5, U38, dark](../../images/03-deliver-and-assess/u38-training-coordinator/5-assistant-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc12-20-training-assistant-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc12-20-training-assistant-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc12-20-training-assistant-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc12-20-training-assistant-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc12-20-training-assistant-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc12-20-training-assistant-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-sc12-20-training-assistant-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-sc12-20-training-assistant-offline-desktop-dark.png) |

## Fields and columns

The fields of [E-SC12-02 Course session](../../data/e-sc12-02-course-session.md),
[E-SC12-06 Attendance sheet](../../data/e-sc12-06-attendance-sheet.md), shown as the entity pages list them, with their
examples.

## Actions

- Ask: [UC-SC12-20](../../use-cases/03-deliver-and-assess/uc-sc12-20-ask-the-assistant.md), step 1.
- Confirm a draft: [UC-SC12-20](../../use-cases/03-deliver-and-assess/uc-sc12-20-ask-the-assistant.md), step 4.

## States

- Normal: the conversation with answers, links and drafts.
- Empty: suggested questions.
- Loading: the frame and titles show at once with placeholder rows; within 1 second
  ([D408](../../../../06-decisions/technical/d408-performance-and-profiles.md)) the data replaces them, and a longer
  load shows a progress line saying what loads.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)) says what failed
  and what to do; what was typed is kept. For example, an action beyond the user's rights: the AI assistant refuses.
- Read-only: answers only for roles that cannot act.
- Offline: not available offline: the AI assistant needs the network; the last answers stay readable.

Shown entities (VD-15): [E-SC12-02 Course session](../../data/e-sc12-02-course-session.md),
[E-SC12-06 Attendance sheet](../../data/e-sc12-06-attendance-sheet.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC12-02 Course session | Planned | Badge "Planned"; a new record starts here; next: Open (UC-SC12-02); fields editable within the role | U38, U39 | `u38-training-coordinator/s-sc12-20-training-assistant-e-sc12-02-course-session-planned-desktop-{light,dark}.png`, `u39-trainer/s-sc12-20-training-assistant-e-sc12-02-course-session-planned-{desktop,phone,tablet}-{light,dark}.png` |
| E-SC12-02 Course session | Open | Badge "Open"; final: read-only, no next state; the history shows how it got here | U38, U39 | `u38-training-coordinator/s-sc12-20-training-assistant-e-sc12-02-course-session-open-desktop-{light,dark}.png`, `u39-trainer/s-sc12-20-training-assistant-e-sc12-02-course-session-open-{desktop,phone,tablet}-{light,dark}.png` |
| E-SC12-06 Attendance sheet | Complete | Badge "Complete"; final: read-only, no next state; the history shows how it got here | U38, U39 | `u38-training-coordinator/s-sc12-20-training-assistant-e-sc12-06-attendance-sheet-complete-desktop-{light,dark}.png`, `u39-trainer/s-sc12-20-training-assistant-e-sc12-06-attendance-sheet-complete-{desktop,phone,tablet}-{light,dark}.png` |

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

- [FL-SC12-03 Deliver and assess](../../flows/fl-sc12-03-deliver-and-assess.md)

## Open questions

None.

---

⬅️ [S-SC12-19 School fees](../05-private-school/s-sc12-19-school-fees.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC12-21 Apprentice training centre](../06-apprentices-driving-nurseries-and-canteens/s-sc12-21-cfa.md)
