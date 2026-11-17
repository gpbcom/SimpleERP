🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
👥 [F9 HR and projects](../../README.md) › 🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-F9-03 Time](README.md) ›
🖥️ S-F9-09 Time off

# 🖥️ S-F9-09 Time off

**Status:** ✅ specified

## Personas

- [U01 Employee](../../../../01-users/personas/u01-employee.md)
- [U02 Manager](../../../../01-users/personas/u02-manager.md)
- [U06 HR](../../../../01-users/personas/u06-hr.md)

## Purpose

Request and approve time off.

## Entry points

HR and projects in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F9-03 step 1, U01 | desktop | ![FL-F9-03 step 1, U01, light](../../images/03-time/u01-employee/1-time-off-desktop-light.png) | ![FL-F9-03 step 1, U01, dark](../../images/03-time/u01-employee/1-time-off-desktop-dark.png) |
| FL-F9-03 step 1, U01 | phone | ![FL-F9-03 step 1, U01, light](../../images/03-time/u01-employee/1-time-off-phone-light.png) | ![FL-F9-03 step 1, U01, dark](../../images/03-time/u01-employee/1-time-off-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f09-09-time-off-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f09-09-time-off-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f09-09-time-off-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f09-09-time-off-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f09-09-time-off-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f09-09-time-off-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f09-09-time-off-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f09-09-time-off-offline-phone-dark.png) |

## Fields and columns

As its entities.

## Actions

As its use case's main flow.

## States

- Normal: Request and approve time off, as the wireframe shows.
- Empty: No time-off request yet, with Request time off.
- Loading: skeleton rows in place of the list ([C-03](../../../../04-ux/design-system/components/c-03-data-table.md));
  actions are disabled until it has loaded.
- Error: the error message pattern (D122).
- Read-only: validated or signed records; other employees' records outside the user's record rules.
- Offline: Not available offline (D38): on a phone or a computer, the offline banner replaces the actions and nothing is
  changed until the network is back; nothing is queued.

Shown entities (VD-15): [E-F9-09 Time-off request](../../data/e-f09-09-time-off-request.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F9-09 Time-off request | To approve | Badge "To approve"; a new record starts here; next: Approved, Refused or Cancelled (UC-F9-09, UC-F9-35); fields editable within the role | U01, U02, U06 | `u01-employee/s-f09-09-time-off-e-f09-09-time-off-request-to-approve-{desktop,phone}-{light,dark}.png`, `u02-manager/s-f09-09-time-off-e-f09-09-time-off-request-to-approve-{desktop,phone}-{light,dark}.png`, `u06-hr/s-f09-09-time-off-e-f09-09-time-off-request-to-approve-desktop-{light,dark}.png` |
| E-F9-09 Time-off request | Approved | Badge "Approved"; final: read-only, no next state; the history shows how it got here | U01, U02, U06 | `u01-employee/s-f09-09-time-off-e-f09-09-time-off-request-approved-{desktop,phone}-{light,dark}.png`, `u02-manager/s-f09-09-time-off-e-f09-09-time-off-request-approved-{desktop,phone}-{light,dark}.png`, `u06-hr/s-f09-09-time-off-e-f09-09-time-off-request-approved-desktop-{light,dark}.png` |
| E-F9-09 Time-off request | Refused | Badge "Refused"; final: read-only, no next state; the history shows how it got here | U01, U02, U06 | `u01-employee/s-f09-09-time-off-e-f09-09-time-off-request-refused-{desktop,phone}-{light,dark}.png`, `u02-manager/s-f09-09-time-off-e-f09-09-time-off-request-refused-{desktop,phone}-{light,dark}.png`, `u06-hr/s-f09-09-time-off-e-f09-09-time-off-request-refused-desktop-{light,dark}.png` |
| E-F9-09 Time-off request | Cancelled | Badge "Cancelled"; final: read-only, no next state; the history shows how it got here | U01, U02, U06 | `u01-employee/s-f09-09-time-off-e-f09-09-time-off-request-cancelled-{desktop,phone}-{light,dark}.png`, `u02-manager/s-f09-09-time-off-e-f09-09-time-off-request-cancelled-{desktop,phone}-{light,dark}.png`, `u06-hr/s-f09-09-time-off-e-f09-09-time-off-request-cancelled-desktop-{light,dark}.png` |

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

⬅️ [S-F9-08 Referrals](../02-recruit/s-f09-08-referrals.md) · ⬆️ [Up](README.md) ·
➡️ [S-F9-10 Attendance](s-f09-10-attendance.md)
