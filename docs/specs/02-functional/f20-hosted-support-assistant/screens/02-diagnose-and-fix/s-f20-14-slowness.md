🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🛟 [F20 Hosted support assistant (hosted edition)](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F20-02 Diagnose and fix](README.md) › 🖥️ S-F20-14 Slowness

# 🖥️ S-F20-14 Slowness

**Status:** ✅ specified

## Personas

- [U07 Administrator](../../../../01-users/personas/u07-administrator.md)

## Purpose

Investigate slowness.

## Entry points

Hosted support assistant in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F20-02 step 6, U07 | desktop | ![FL-F20-02 step 6, U07, light](../../images/02-diagnose-and-fix/u07-administrator/6-slowness-desktop-light.png) | ![FL-F20-02 step 6, U07, dark](../../images/02-diagnose-and-fix/u07-administrator/6-slowness-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f20-14-slowness-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f20-14-slowness-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f20-14-slowness-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f20-14-slowness-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f20-14-slowness-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f20-14-slowness-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f20-14-slowness-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f20-14-slowness-offline-desktop-dark.png) |

## Fields and columns

As its entities.

## Actions

As its use case's main flow.

## States

- Normal: measures of slowness with the advice.
- Empty: "No slowness reported".
- Loading: the frame and titles show at once with placeholder rows for the measures; within 1 second (D408) the data
  replaces them, and a longer load shows a progress line saying what loads.
- Error: the error message pattern (D122).
- Read-only: always read-only for customers.
- Offline: not available offline: measures run online. D38 keeps only today's schedule, time and intervention records
  offline. A banner says the connection is lost; what is on screen stays visible, every action is disabled and nothing
  is queued until the connection is back.

Shown entities (VD-15): [E-F20-05 Cluster reading](../../data/e-f20-05-cluster-reading.md),
[E-F20-04 Diagnosis](../../data/e-f20-04-diagnosis.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F20-05 Cluster reading | Recorded | Badge "Recorded"; a new record starts here; no other state; fields editable within the role | U07 | `u07-administrator/s-f20-14-slowness-e-f20-05-cluster-reading-recorded-desktop-{light,dark}.png` |
| E-F20-04 Diagnosis | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U07 | `u07-administrator/s-f20-14-slowness-e-f20-04-diagnosis-active-desktop-{light,dark}.png` |

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

- [FL-F20-02 Diagnose and fix](../../flows/fl-f20-02-diagnose-and-fix.md)

## Open questions

None.

---

⬅️ [S-F20-13 Restore](s-f20-13-restore.md) · ⬆️ [Up](README.md) ·
➡️ [S-F20-15 Security incident](../03-incidents/s-f20-15-security-incident.md)
