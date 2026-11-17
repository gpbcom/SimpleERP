🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
👥 [F9 HR and projects](../../README.md) › 🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-F9-03 Time](README.md) ›
🖥️ S-F9-10 Attendance

# 🖥️ S-F9-10 Attendance

**Status:** ✅ specified

## Personas

- [U01 Employee](../../../../01-users/personas/u01-employee.md)
- [U14 Field worker](../../../../01-users/personas/u14-field-worker.md)
- [U02 Manager](../../../../01-users/personas/u02-manager.md)

## Purpose

Record attendance and overtime.

## Entry points

HR and projects in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F9-03 step 2, U01 | desktop | ![FL-F9-03 step 2, U01, light](../../images/03-time/u01-employee/2-attendance-desktop-light.png) | ![FL-F9-03 step 2, U01, dark](../../images/03-time/u01-employee/2-attendance-desktop-dark.png) |
| FL-F9-03 step 2, U01 | phone | ![FL-F9-03 step 2, U01, light](../../images/03-time/u01-employee/2-attendance-phone-light.png) | ![FL-F9-03 step 2, U01, dark](../../images/03-time/u01-employee/2-attendance-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f09-10-attendance-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f09-10-attendance-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f09-10-attendance-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f09-10-attendance-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f09-10-attendance-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f09-10-attendance-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f09-10-attendance-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f09-10-attendance-offline-phone-dark.png) |

## Fields and columns

As its entities.

## Actions

As its use case's main flow.

## States

- Normal: Record attendance and overtime, as the wireframe shows.
- Empty: No attendance today yet, with Check in.
- Loading: skeleton rows in place of the list ([C-03](../../../../04-ux/design-system/components/c-03-data-table.md));
  actions are disabled until it has loaded.
- Error: the error message pattern (D122).
- Read-only: validated or signed records; other employees' records outside the user's record rules.
- Offline: Works offline ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md)): today's schedule, time and
  intervention records stay on the phone and their changes wait in a queue, sent when the network is back; everything
  else waits for the network.

Shown entities (VD-15): [E-F9-10 Attendance](../../data/e-f09-10-attendance.md),
[E-F9-34 Attendance kiosk](../../data/e-f09-34-attendance-kiosk.md),
[E-F9-35 Employee badge](../../data/e-f09-35-employee-badge.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F9-10 Attendance | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U01, U02, U14 | `u01-employee/s-f09-10-attendance-e-f09-10-attendance-active-{desktop,phone}-{light,dark}.png`, `u02-manager/s-f09-10-attendance-e-f09-10-attendance-active-{desktop,phone}-{light,dark}.png`, `u14-field-worker/s-f09-10-attendance-e-f09-10-attendance-active-phone-{light,dark}.png` |
| E-F9-34 Attendance kiosk | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U01, U02, U14 | `u01-employee/s-f09-10-attendance-e-f09-34-attendance-kiosk-active-{desktop,phone}-{light,dark}.png`, `u02-manager/s-f09-10-attendance-e-f09-34-attendance-kiosk-active-{desktop,phone}-{light,dark}.png`, `u14-field-worker/s-f09-10-attendance-e-f09-34-attendance-kiosk-active-phone-{light,dark}.png` |
| E-F9-35 Employee badge | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U01, U02, U14 | `u01-employee/s-f09-10-attendance-e-f09-35-employee-badge-active-{desktop,phone}-{light,dark}.png`, `u02-manager/s-f09-10-attendance-e-f09-35-employee-badge-active-{desktop,phone}-{light,dark}.png`, `u14-field-worker/s-f09-10-attendance-e-f09-35-employee-badge-active-phone-{light,dark}.png` |

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

⬅️ [S-F9-09 Time off](s-f09-09-time-off.md) · ⬆️ [Up](README.md) ·
➡️ [S-F9-11 Appraisals and skills](../04-grow/s-f09-11-appraisals-and-skills.md)
