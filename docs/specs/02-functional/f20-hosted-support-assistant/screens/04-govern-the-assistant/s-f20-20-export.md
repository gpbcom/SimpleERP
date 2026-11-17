🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🛟 [F20 Hosted support assistant (hosted edition)](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F20-04 Govern the AI assistant](README.md) › 🖥️ S-F20-20 Export

# 🖥️ S-F20-20 Export

**Status:** ✅ specified

## Personas

- [U07 Administrator](../../../../01-users/personas/u07-administrator.md)

## Purpose

Export a support conversation.

## Entry points

Hosted support assistant in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F20-04 step 5, U07 | desktop | ![FL-F20-04 step 5, U07, light](../../images/04-govern-the-assistant/u07-administrator/5-export-desktop-light.png) | ![FL-F20-04 step 5, U07, dark](../../images/04-govern-the-assistant/u07-administrator/5-export-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f20-20-export-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f20-20-export-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f20-20-export-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f20-20-export-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f20-20-export-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f20-20-export-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f20-20-export-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f20-20-export-offline-desktop-dark.png) |

## Fields and columns

As its entities.

## Actions

As its use case's main flow.

## States

- Normal: the conversation to export with its screenshots.
- Empty: "No conversation".
- Loading: the frame and titles show at once with placeholder rows for the export; within 1 second (D408) the data
  replaces them, and a longer load shows a progress line saying what loads.
- Error: the error message pattern (D122).
- Read-only: exports are read-only.
- Offline: not available offline: exports run online. D38 keeps only today's schedule, time and intervention records
  offline. A banner says the connection is lost; what is on screen stays visible, every action is disabled and nothing
  is queued until the connection is back.

Shown entities (VD-15): [E-F20-18 Support conversation export](../../data/e-f20-18-support-conversation-export.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F20-18 Support conversation export | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U07 | `u07-administrator/s-f20-20-export-e-f20-18-support-conversation-export-active-desktop-{light,dark}.png` |

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

- [FL-F20-04 Govern the AI assistant](../../flows/fl-f20-04-govern-the-assistant.md)

## Open questions

None.

---

⬅️ [S-F20-19 Support plans](s-f20-19-support-plans.md) · ⬆️ [Up](README.md) ·
➡️ [S-F20-21 Maintenance notices](../05-maintenance-and-releases/s-f20-21-maintenance-notices.md)
