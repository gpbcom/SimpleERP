🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🔌 [F24 Integrations hub](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F24-02 Office suites](README.md) › 🖥️ S-F24-09 Suite API

# 🖥️ S-F24-09 Suite API

**Status:** ✅ specified

## Personas

- [U07 Administrator](../../../../01-users/personas/u07-administrator.md)

## Purpose

Use the suites' full read and write API.

## Entry points

Integrations hub in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F24-02 step 7, U07 | desktop | ![FL-F24-02 step 7, U07, light](../../images/02-office-suites/u07-administrator/7-api-desktop-light.png) | ![FL-F24-02 step 7, U07, dark](../../images/02-office-suites/u07-administrator/7-api-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f24-09-suite-api-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f24-09-suite-api-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f24-09-suite-api-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f24-09-suite-api-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f24-09-suite-api-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f24-09-suite-api-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f24-09-suite-api-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f24-09-suite-api-offline-desktop-dark.png) |

## Fields and columns

As its entities.

## Actions

As its use case's main flow.

## States

- Normal: components enabled with their scopes.
- Empty: "No component enabled".
- Loading: the frame and titles show at once with placeholder rows for the components; within 1 second (D408) the data
  replaces them, and a longer load shows a progress line saying what loads.
- Error: the error message pattern (D122).
- Read-only: the owner reads.
- Offline: not available offline: set online. D38 keeps only today's schedule, time and intervention records offline. A
  banner says the connection is lost; what is on screen stays visible, every action is disabled and nothing is queued
  until the connection is back.

Shown entities (VD-15): [E-F24-03 Suite component](../../data/e-f24-03-suite-component.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F24-03 Suite component | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U07 | `u07-administrator/s-f24-09-suite-api-e-f24-03-suite-component-active-desktop-{light,dark}.png` |

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

- [FL-F24-02 Office suites](../../flows/fl-f24-02-office-suites.md)

## Open questions

None.

---

⬅️ [S-F24-08 Suite projects](s-f24-08-suite-projects.md) · ⬆️ [Up](README.md) ·
➡️ [S-F24-10 CRM sync](../03-crm-and-ats/s-f24-10-crm-sync.md)
