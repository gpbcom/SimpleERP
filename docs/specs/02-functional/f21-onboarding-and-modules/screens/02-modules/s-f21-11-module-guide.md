🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🧭 [F21 Onboarding and module activation](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F21-02 Modules](README.md) › 🖥️ S-F21-11 Module guide

# 🖥️ S-F21-11 Module guide

**Status:** ✅ specified

## Personas

- [U07 Administrator](../../../../01-users/personas/u07-administrator.md)

## Purpose

Follow a module's short guide.

## Entry points

Onboarding and module activation in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F21-02 step 4, U07 | desktop | ![FL-F21-02 step 4, U07, light](../../images/02-modules/u07-administrator/4-module-guide-desktop-light.png) | ![FL-F21-02 step 4, U07, dark](../../images/02-modules/u07-administrator/4-module-guide-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f21-11-module-guide-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f21-11-module-guide-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f21-11-module-guide-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f21-11-module-guide-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f21-11-module-guide-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f21-11-module-guide-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f21-11-module-guide-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f21-11-module-guide-offline-desktop-dark.png) |

## Fields and columns

As its entities.

## Actions

As its use case's main flow.

## States

- Normal: the module's short guide.
- Empty: never empty.
- Loading: the frame and titles show at once with placeholder rows for the guide; within 1 second (D408) the data
  replaces them, and a longer load shows a progress line saying what loads.
- Error: the error message pattern (D122).
- Read-only: done guides read-only.
- Offline: not available offline: online. D38 keeps only today's schedule, time and intervention records offline. A
  banner says the connection is lost; what is on screen stays visible, every action is disabled and nothing is queued
  until the connection is back.

Shown entities (VD-15): [E-F21-18 Module guide](../../data/e-f21-18-module-guide.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F21-18 Module guide | Active | Badge "Active"; a new record starts here; next: Done (UC-F21-11); fields editable within the role | U07 | `u07-administrator/s-f21-11-module-guide-e-f21-18-module-guide-active-desktop-{light,dark}.png` |
| E-F21-18 Module guide | Done | Badge "Done"; final: read-only, no next state; the history shows how it got here | U07 | `u07-administrator/s-f21-11-module-guide-e-f21-18-module-guide-done-desktop-{light,dark}.png` |

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

- [FL-F21-02 Modules](../../flows/fl-f21-02-modules.md)

## Open questions

None.

---

⬅️ [S-F21-10 Connections](../03-team-and-data/s-f21-10-connections.md) · ⬆️ [Up](README.md) ·
➡️ [S-F21-12 Guide assistant](../01-first-run/s-f21-12-guide-assistant.md)
