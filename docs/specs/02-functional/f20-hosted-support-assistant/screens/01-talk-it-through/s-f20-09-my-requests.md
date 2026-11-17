🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🛟 [F20 Hosted support assistant (hosted edition)](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F20-01 Talk it through](README.md) › 🖥️ S-F20-09 My requests

# 🖥️ S-F20-09 My requests

**Status:** ✅ specified

## Personas

- [U07 Administrator](../../../../01-users/personas/u07-administrator.md)
- [U13 Owner](../../../../01-users/personas/u13-owner.md)

## Purpose

Follow the request.

## Entry points

Hosted support assistant in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F20-01 step 4, U07 | desktop | ![FL-F20-01 step 4, U07, light](../../images/01-talk-it-through/u07-administrator/4-follow-desktop-light.png) | ![FL-F20-01 step 4, U07, dark](../../images/01-talk-it-through/u07-administrator/4-follow-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f20-09-my-requests-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f20-09-my-requests-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f20-09-my-requests-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f20-09-my-requests-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f20-09-my-requests-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f20-09-my-requests-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f20-09-my-requests-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f20-09-my-requests-offline-desktop-dark.png) |

## Fields and columns

As its entities.

## Actions

As its use case's main flow.

## States

- Normal: the customer's requests with status and timeline.
- Empty: "No request yet".
- Loading: the frame and titles show at once with placeholder rows for the requests; within 1 second (D408) the data
  replaces them, and a longer load shows a progress line saying what loads.
- Error: the error message pattern (D122).
- Read-only: employees see their own.
- Offline: Requests last loaded stay readable. Nothing else is queued: D38 keeps only today's schedule, time and
  intervention records offline; a banner says the connection is lost and the actions come back with it.

Shown entities (VD-15): [E-F20-01 Support request](../../data/e-f20-01-support-request.md),
[E-F20-02 Message](../../data/e-f20-02-message.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F20-01 Support request | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U07, U13 | `u07-administrator/s-f20-09-my-requests-e-f20-01-support-request-active-desktop-{light,dark}.png`, `u13-owner/s-f20-09-my-requests-e-f20-01-support-request-active-{desktop,phone}-{light,dark}.png` |
| E-F20-02 Message | Recorded | Badge "Recorded"; a new record starts here; no other state; fields editable within the role | U07, U13 | `u07-administrator/s-f20-09-my-requests-e-f20-02-message-recorded-desktop-{light,dark}.png`, `u13-owner/s-f20-09-my-requests-e-f20-02-message-recorded-{desktop,phone}-{light,dark}.png` |

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

⬅️ [S-F20-08 Escalation](../03-incidents/s-f20-08-escalation.md) · ⬆️ [Up](README.md) ·
➡️ [S-F20-10 Status page](../03-incidents/s-f20-10-status-page.md)
