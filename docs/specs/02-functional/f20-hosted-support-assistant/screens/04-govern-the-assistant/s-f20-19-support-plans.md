🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🛟 [F20 Hosted support assistant (hosted edition)](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F20-04 Govern the AI assistant](README.md) › 🖥️ S-F20-19 Support plans

# 🖥️ S-F20-19 Support plans

**Status:** ✅ specified

## Personas

- [U13 Owner](../../../../01-users/personas/u13-owner.md)

## Purpose

Choose a support plan and see its times.

## Entry points

Hosted support assistant in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F20-04 step 4, U13 | desktop | ![FL-F20-04 step 4, U13, light](../../images/04-govern-the-assistant/u13-owner/4-plans-desktop-light.png) | ![FL-F20-04 step 4, U13, dark](../../images/04-govern-the-assistant/u13-owner/4-plans-desktop-dark.png) |
| FL-F20-04 step 4, U13 | phone | ![FL-F20-04 step 4, U13, light](../../images/04-govern-the-assistant/u13-owner/4-plans-phone-light.png) | ![FL-F20-04 step 4, U13, dark](../../images/04-govern-the-assistant/u13-owner/4-plans-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f20-19-support-plans-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f20-19-support-plans-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f20-19-support-plans-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f20-19-support-plans-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f20-19-support-plans-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f20-19-support-plans-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f20-19-support-plans-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f20-19-support-plans-offline-phone-dark.png) |

## Fields and columns

As its entities.

## Actions

As its use case's main flow.

## States

- Normal: plans with their times and the targets met, and the credits.
- Empty: never empty: the single hosted offer is shown.
- Loading: the frame and titles show at once with placeholder rows for the plan; within 1 second (D408) the data
  replaces them, and a longer load shows a progress line saying what loads.
- Error: the error message pattern (D122).
- Read-only: administrators read.
- Offline: The plan last loaded stays visible. Nothing else is queued: D38 keeps only today's schedule, time and
  intervention records offline; a banner says the connection is lost and the actions come back with it.

Shown entities (VD-15): [E-F20-12 Support plan](../../data/e-f20-12-support-plan.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F20-12 Support plan | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U13 | `u13-owner/s-f20-19-support-plans-e-f20-12-support-plan-active-{desktop,phone}-{light,dark}.png` |

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

⬅️ [S-F20-18 Masking](s-f20-18-masking.md) · ⬆️ [Up](README.md) · ➡️ [S-F20-20 Export](s-f20-20-export.md)
