🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🛟 [F20 Hosted support assistant (hosted edition)](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F20-01 Talk it through](README.md) › 🖥️ S-F20-03 Screenshots

# 🖥️ S-F20-03 Screenshots

**Status:** ✅ specified

## Personas

- [U07 Administrator](../../../../01-users/personas/u07-administrator.md)

## Purpose

Share screenshots when needed.

## Entry points

Hosted support assistant in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F20-01 step 3, U07 | desktop | ![FL-F20-01 step 3, U07, light](../../images/01-talk-it-through/u07-administrator/3-screenshot-desktop-light.png) | ![FL-F20-01 step 3, U07, dark](../../images/01-talk-it-through/u07-administrator/3-screenshot-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f20-03-screenshots-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f20-03-screenshots-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f20-03-screenshots-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f20-03-screenshots-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f20-03-screenshots-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f20-03-screenshots-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f20-03-screenshots-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f20-03-screenshots-offline-desktop-dark.png) |

## Fields and columns

As its entities.

## Actions

As its use case's main flow.

## States

- Normal: the screenshot request with the masked preview.
- Empty: "No screenshot needed".
- Loading: the frame and titles show at once with placeholder rows for the screenshot; within 1 second (D408) the data
  replaces them, and a longer load shows a progress line saying what loads.
- Error: the error message pattern (D122).
- Read-only: attached screenshots are read-only.
- Offline: not available offline: screenshots are taken online. D38 keeps only today's schedule, time and intervention
  records offline. A banner says the connection is lost; what is on screen stays visible, every action is disabled and
  nothing is queued until the connection is back.

Shown entities (VD-15): [E-F20-03 Screenshot](../../data/e-f20-03-screenshot.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F20-03 Screenshot | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U07 | `u07-administrator/s-f20-03-screenshots-e-f20-03-screenshot-active-desktop-{light,dark}.png` |

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

⬅️ [S-F20-02 Clarify](s-f20-02-clarify.md) · ⬆️ [Up](README.md) ·
➡️ [S-F20-04 Diagnosis](../02-diagnose-and-fix/s-f20-04-diagnosis.md)
