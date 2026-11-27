🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🔌 [F24 Integrations hub](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F24-04 Run and control](README.md) › 🖥️ S-F24-16 API changes

# 🖥️ S-F24-16 API changes

**Status:** ✅ specified

## Personas

- [U07 Administrator](../../../../01-users/personas/u07-administrator.md)
- [U47 SimpleERP maintainer](../../../../01-users/personas/u47-simpleerp-maintainer.md)

## Purpose

Handle an outside API change or error.

## Entry points

Integrations hub in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F24-04 step 3, U07 | desktop | ![FL-F24-04 step 3, U07, light](../../images/04-run-and-control/u07-administrator/3-api-change-desktop-light.png) | ![FL-F24-04 step 3, U07, dark](../../images/04-run-and-control/u07-administrator/3-api-change-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f24-16-api-changes-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f24-16-api-changes-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f24-16-api-changes-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f24-16-api-changes-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f24-16-api-changes-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f24-16-api-changes-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f24-16-api-changes-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f24-16-api-changes-offline-desktop-dark.png) |

## Fields and columns

As its entities.

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Icon | E-F24-12, or the category's icon (BR-F24-16) | tile sized by BR-F24-16, name as accessible name | no | yes |

## Actions

As its use case's main flow.

## States

- Normal: API changes and errors with their repair state.
- Empty: "No incident".
- Loading: the frame and titles show at once with placeholder rows for the incidents; within 1 second (D408) the data
  replaces them, and a longer load shows a progress line saying what loads.
- Error: the error message pattern (D122).
- Read-only: administrators read; maintainers repair.
- Offline: not available offline: handled online. D38 keeps only today's schedule, time and intervention records
  offline. A banner says the connection is lost; what is on screen stays visible, every action is disabled and nothing
  is queued until the connection is back.

Shown entities (VD-15): [E-F24-10 Connector incident](../../data/e-f24-10-connector-incident.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F24-10 Connector incident | Repaired | Badge "Repaired"; a new record starts here; next: Paused, Flagged or Failed (BR-F24-09, UC-F24-16, UC-F24-15); fields editable within the role | U07, U47 | `u07-administrator/s-f24-16-api-changes-e-f24-10-connector-incident-repaired-desktop-{light,dark}.png`, `u47-simpleerp-maintainer/s-f24-16-api-changes-e-f24-10-connector-incident-repaired-{desktop,phone}-{light,dark}.png` |
| E-F24-10 Connector incident | Paused | Badge "Paused"; next: Repaired (UC-F24-16); fields editable within the role | U07, U47 | `u07-administrator/s-f24-16-api-changes-e-f24-10-connector-incident-paused-desktop-{light,dark}.png`, `u47-simpleerp-maintainer/s-f24-16-api-changes-e-f24-10-connector-incident-paused-{desktop,phone}-{light,dark}.png` |
| E-F24-10 Connector incident | Flagged | Badge "Flagged"; next: Repaired (UC-F24-16); fields editable within the role | U07, U47 | `u07-administrator/s-f24-16-api-changes-e-f24-10-connector-incident-flagged-desktop-{light,dark}.png`, `u47-simpleerp-maintainer/s-f24-16-api-changes-e-f24-10-connector-incident-flagged-{desktop,phone}-{light,dark}.png` |
| E-F24-10 Connector incident | Failed | Badge "Failed"; final: read-only, no next state; the history shows how it got here | U07, U47 | `u07-administrator/s-f24-16-api-changes-e-f24-10-connector-incident-failed-desktop-{light,dark}.png`, `u47-simpleerp-maintainer/s-f24-16-api-changes-e-f24-10-connector-incident-failed-{desktop,phone}-{light,dark}.png` |

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

- [FL-F24-04 Run and control](../../flows/fl-f24-04-run-and-control.md)

## Open questions

None.

---

⬅️ [S-F24-15 Health](s-f24-15-health.md) · ⬆️ [Up](README.md) · ➡️ [S-F24-17 Disconnect](s-f24-17-disconnect.md)
