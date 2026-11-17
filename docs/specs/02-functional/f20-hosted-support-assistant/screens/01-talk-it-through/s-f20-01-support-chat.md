🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🛟 [F20 Hosted support assistant (hosted edition)](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F20-01 Talk it through](README.md) › 🖥️ S-F20-01 Support chat

# 🖥️ S-F20-01 Support chat

**Status:** ✅ specified

## Personas

- [U07 Administrator](../../../../01-users/personas/u07-administrator.md)
- [U01 Employee](../../../../01-users/personas/u01-employee.md)

## Purpose

Report a problem in plain words.

## Entry points

Hosted support assistant in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F20-01 step 1, U07 | desktop | ![FL-F20-01 step 1, U07, light](../../images/01-talk-it-through/u07-administrator/1-report-desktop-light.png) | ![FL-F20-01 step 1, U07, dark](../../images/01-talk-it-through/u07-administrator/1-report-desktop-dark.png) |
| Error E1, U07 | desktop | ![Error E1, U07, light](../../images/01-talk-it-through/u07-administrator/e1-known-incident-desktop-light.png) | ![Error E1, U07, dark](../../images/01-talk-it-through/u07-administrator/e1-known-incident-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f20-01-support-chat-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f20-01-support-chat-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f20-01-support-chat-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f20-01-support-chat-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f20-01-support-chat-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f20-01-support-chat-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f20-01-support-chat-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f20-01-support-chat-offline-desktop-dark.png) |

## Fields and columns

As its entities.

## Actions

As its use case's main flow.

## States

- Normal: the conversation with status and the human option.
- Empty: "Tell us what is wrong": examples.
- Loading: the frame and titles show at once with placeholder rows for the conversation; within 1 second (D408) the data
  replaces them, and a longer load shows a progress line saying what loads.
- Error: the error message pattern (D122).
- Read-only: closed requests are read-only.
- Offline: the AI assistant says it is offline; the question is queued and answered when the network is back, with a
  notification (D182).

Shown entities (VD-15): [E-F20-01 Support request](../../data/e-f20-01-support-request.md),
[E-F20-02 Message](../../data/e-f20-02-message.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F20-01 Support request | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U01, U07 | `u01-employee/s-f20-01-support-chat-e-f20-01-support-request-active-{desktop,phone}-{light,dark}.png`, `u07-administrator/s-f20-01-support-chat-e-f20-01-support-request-active-desktop-{light,dark}.png` |
| E-F20-02 Message | Recorded | Badge "Recorded"; a new record starts here; no other state; fields editable within the role | U01, U07 | `u01-employee/s-f20-01-support-chat-e-f20-02-message-recorded-{desktop,phone}-{light,dark}.png`, `u07-administrator/s-f20-01-support-chat-e-f20-02-message-recorded-desktop-{light,dark}.png` |

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

⬆️ [Up](README.md) · ➡️ [S-F20-02 Clarify](s-f20-02-clarify.md)
