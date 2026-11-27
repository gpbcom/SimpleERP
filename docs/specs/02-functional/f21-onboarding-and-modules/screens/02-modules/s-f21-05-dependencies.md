🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🧭 [F21 Onboarding and module activation](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F21-02 Modules](README.md) › 🖥️ S-F21-05 Dependencies

# 🖥️ S-F21-05 Dependencies

**Status:** ✅ specified

## Personas

- [U07 Administrator](../../../../01-users/personas/u07-administrator.md)

## Purpose

Understand a module's dependencies.

## Entry points

Onboarding and module activation in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F21-02 step 2, U07 | desktop | ![FL-F21-02 step 2, U07, light](../../images/02-modules/u07-administrator/2-dependencies-desktop-light.png) | ![FL-F21-02 step 2, U07, dark](../../images/02-modules/u07-administrator/2-dependencies-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f21-05-dependencies-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f21-05-dependencies-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f21-05-dependencies-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f21-05-dependencies-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f21-05-dependencies-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f21-05-dependencies-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f21-05-dependencies-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f21-05-dependencies-offline-desktop-dark.png) |

## Fields and columns

As its entities.

## Actions

As its use case's main flow.

## States

- Normal: the module's needs explained.
- Empty: "No dependency".
- Loading: the frame and titles show at once with placeholder rows for the dependencies; within 1 second (D408) the data
  replaces them, and a longer load shows a progress line saying what loads.
- Error: the error message pattern (D122).
- Read-only: always read-only.
- Offline: not available offline: read online. D38 keeps only today's schedule, time and intervention records offline. A
  banner says the connection is lost; what is on screen stays visible, every action is disabled and nothing is queued
  until the connection is back.

Shown entities (VD-15): [E-F21-05 Module dependency](../../data/e-f21-05-module-dependency.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F21-05 Module dependency | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U07 | `u07-administrator/s-f21-05-dependencies-e-f21-05-module-dependency-active-desktop-{light,dark}.png` |

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

⬅️ [S-F21-04 Modules](s-f21-04-modules.md) · ⬆️ [Up](README.md) · ➡️ [S-F21-06 Switch off](s-f21-06-switch-off.md)
