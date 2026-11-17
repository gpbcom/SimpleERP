🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🔌 [F24 Integrations hub](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F24-03 CRM and ATS](README.md) › 🖥️ S-F24-12 Mapping

# 🖥️ S-F24-12 Mapping

**Status:** ✅ specified

## Personas

- [U07 Administrator](../../../../01-users/personas/u07-administrator.md)

## Purpose

Map fields and resolve conflicts.

## Entry points

Integrations hub in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F24-03 step 3, U07 | desktop | ![FL-F24-03 step 3, U07, light](../../images/03-crm-and-ats/u07-administrator/3-mapping-desktop-light.png) | ![FL-F24-03 step 3, U07, dark](../../images/03-crm-and-ats/u07-administrator/3-mapping-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f24-12-mapping-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f24-12-mapping-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f24-12-mapping-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f24-12-mapping-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f24-12-mapping-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f24-12-mapping-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f24-12-mapping-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f24-12-mapping-offline-desktop-dark.png) |

## Fields and columns

As its entities.

## Actions

As its use case's main flow.

## States

- Normal: fields with owners and conflicts.
- Empty: "No mapping yet".
- Loading: the frame and titles show at once with placeholder rows for the mapping; within 1 second (D408) the data
  replaces them, and a longer load shows a progress line saying what loads.
- Error: the error message pattern (D122).
- Read-only: other roles read.
- Offline: not available offline: set online. D38 keeps only today's schedule, time and intervention records offline. A
  banner says the connection is lost; what is on screen stays visible, every action is disabled and nothing is queued
  until the connection is back.

Shown entities (VD-15): [E-F24-07 Field mapping](../../data/e-f24-07-field-mapping.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F24-07 Field mapping | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U07 | `u07-administrator/s-f24-12-mapping-e-f24-07-field-mapping-active-desktop-{light,dark}.png` |

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

- [FL-F24-03 CRM and ATS](../../flows/fl-f24-03-crm-and-ats.md)

## Open questions

None.

---

⬅️ [S-F24-11 ATS sync](s-f24-11-ats-sync.md) · ⬆️ [Up](README.md) ·
➡️ [S-F24-13 History import](s-f24-13-history-import.md)
