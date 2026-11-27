🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
👥 [F9 HR and projects](../../README.md) › 🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-F9-03 Time](README.md) ›
🖥️ S-F9-16 Timesheets

# 🖥️ S-F9-16 Timesheets

**Status:** ✅ specified

## Personas

- [U01 Employee](../../../../01-users/personas/u01-employee.md)
- [U14 Field worker](../../../../01-users/personas/u14-field-worker.md)
- [U02 Manager](../../../../01-users/personas/u02-manager.md)

## Purpose

Record and validate timesheets.

## Entry points

HR and projects in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F9-03 step 3, U01 | desktop | ![FL-F9-03 step 3, U01, light](../../images/03-time/u01-employee/3-timesheets-desktop-light.png) | ![FL-F9-03 step 3, U01, dark](../../images/03-time/u01-employee/3-timesheets-desktop-dark.png) |
| FL-F9-03 step 3, U01 | phone | ![FL-F9-03 step 3, U01, light](../../images/03-time/u01-employee/3-timesheets-phone-light.png) | ![FL-F9-03 step 3, U01, dark](../../images/03-time/u01-employee/3-timesheets-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f09-16-timesheets-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f09-16-timesheets-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f09-16-timesheets-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f09-16-timesheets-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f09-16-timesheets-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f09-16-timesheets-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f09-16-timesheets-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f09-16-timesheets-offline-phone-dark.png) |

## Fields and columns

As its entities.

## Actions

As its use case's main flow.

## States

- Normal: Record and validate timesheets, as the wireframe shows.
- Empty: No timesheet line yet, with Add time.
- Loading: skeleton rows in place of the list ([C-03](../../../../04-ux/design-system/components/c-03-data-table.md));
  actions are disabled until it has loaded.
- Error: the error message pattern (D122).
- Read-only: validated or signed records; other employees' records outside the user's record rules.
- Offline: Works offline ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md)): today's schedule, time and
  intervention records stay on the phone and their changes wait in a queue, sent when the network is back; everything
  else waits for the network.

Shown entities (VD-15): [E-F9-17 Timesheet line](../../data/e-f09-17-timesheet-line.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F9-17 Timesheet line | Draft | Badge "Draft"; a new record starts here; next: Submitted (UC-F9-16); fields editable within the role | U01, U02, U14 | `u01-employee/s-f09-16-timesheets-e-f09-17-timesheet-line-draft-{desktop,phone}-{light,dark}.png`, `u02-manager/s-f09-16-timesheets-e-f09-17-timesheet-line-draft-{desktop,phone}-{light,dark}.png`, `u14-field-worker/s-f09-16-timesheets-e-f09-17-timesheet-line-draft-phone-{light,dark}.png` |
| E-F9-17 Timesheet line | Submitted | Badge "Submitted"; next: Validated (UC-F9-16); fields editable within the role | U02, U14 | `u02-manager/s-f09-16-timesheets-e-f09-17-timesheet-line-submitted-{desktop,phone}-{light,dark}.png`, `u14-field-worker/s-f09-16-timesheets-e-f09-17-timesheet-line-submitted-phone-{light,dark}.png` |
| E-F9-17 Timesheet line | Validated | Badge "Validated"; next: Billed (UC-F9-16); fields editable within the role | U02, U14 | `u02-manager/s-f09-16-timesheets-e-f09-17-timesheet-line-validated-{desktop,phone}-{light,dark}.png`, `u14-field-worker/s-f09-16-timesheets-e-f09-17-timesheet-line-validated-phone-{light,dark}.png` |
| E-F9-17 Timesheet line | Billed | Badge "Billed"; final: read-only, no next state; the history shows how it got here | U02, U14 | `u02-manager/s-f09-16-timesheets-e-f09-17-timesheet-line-billed-{desktop,phone}-{light,dark}.png`, `u14-field-worker/s-f09-16-timesheets-e-f09-17-timesheet-line-billed-phone-{light,dark}.png` |

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

## Shown in

- [FL-F9-03 Time](../../flows/fl-f09-03-time.md)

## Open questions

None.

---

⬅️ [S-F9-15 Planning](../06-plan-and-deliver-work/s-f09-15-planning.md) · ⬆️ [Up](README.md) ·
➡️ [S-F9-17 Projects](../06-plan-and-deliver-work/s-f09-17-projects.md)
