🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🛟 [F20 Hosted support assistant (hosted edition)](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F20-01 Talk it through](README.md) › 🖥️ S-F20-12 How-to

# 🖥️ S-F20-12 How-to

**Status:** ✅ specified

## Personas

- [U01 Employee](../../../../01-users/personas/u01-employee.md)
- [U07 Administrator](../../../../01-users/personas/u07-administrator.md)

## Purpose

Answer how-to questions from the documentation.

## Entry points

Hosted support assistant in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F20-01 step 5, U01 | desktop | ![FL-F20-01 step 5, U01, light](../../images/01-talk-it-through/u01-employee/5-how-to-desktop-light.png) | ![FL-F20-01 step 5, U01, dark](../../images/01-talk-it-through/u01-employee/5-how-to-desktop-dark.png) |
| FL-F20-01 step 5, U01 | phone | ![FL-F20-01 step 5, U01, light](../../images/01-talk-it-through/u01-employee/5-how-to-phone-light.png) | ![FL-F20-01 step 5, U01, dark](../../images/01-talk-it-through/u01-employee/5-how-to-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f20-12-how-to-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f20-12-how-to-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f20-12-how-to-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f20-12-how-to-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f20-12-how-to-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f20-12-how-to-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f20-12-how-to-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f20-12-how-to-offline-phone-dark.png) |

## Fields and columns

As its entities.

## Actions

As its use case's main flow.

## States

- Normal: the answer with documentation links and rating.
- Empty: example questions.
- Loading: the frame and titles show at once with placeholder rows for the answer; within 1 second (D408) the data
  replaces them, and a longer load shows a progress line saying what loads.
- Error: the error message pattern (D122).
- Read-only: past answers read-only.
- Offline: the AI assistant says it is offline; questions are queued (D182).

Shown entities (VD-15): [E-F20-02 Message](../../data/e-f20-02-message.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F20-02 Message | Recorded | Badge "Recorded"; a new record starts here; no other state; fields editable within the role | U01, U07 | `u01-employee/s-f20-12-how-to-e-f20-02-message-recorded-{desktop,phone}-{light,dark}.png`, `u07-administrator/s-f20-12-how-to-e-f20-02-message-recorded-desktop-{light,dark}.png` |

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
- [C-10 Empty state](../../../../04-ux/design-system/components/c-10-empty-state.md)

## Shown in

- [FL-F20-01 Talk it through](../../flows/fl-f20-01-talk-it-through.md)

## Open questions

None.

---

⬅️ [S-F20-11 Proactive alerts](../03-incidents/s-f20-11-proactive-alerts.md) · ⬆️ [Up](README.md) ·
➡️ [S-F20-13 Restore](../02-diagnose-and-fix/s-f20-13-restore.md)
