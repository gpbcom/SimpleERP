🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
👥 [F9 HR and projects](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F9-07 Fair pay and speaking up](README.md) › 🖥️ S-F9-21 Whistleblowing

# 🖥️ S-F9-21 Whistleblowing

**Status:** ✅ specified

## Personas

- [U01 Employee](../../../../01-users/personas/u01-employee.md)
- [U06 Human resources](../../../../01-users/personas/u06-hr.md)
- [U13 Owner](../../../../01-users/personas/u13-owner.md)

## Purpose

Make a report, follow it by its code, and handle it.

## Entry points

The intranet or the public link (reporters); HR › Whistleblowing (handlers).

## Wireframe

```text
Reporter (any device)
  Facts [                               ]  Files [+]
  ( ) Give my name  (x) Stay anonymous           [Send]
  Your code: 7KQ2-M9  [Follow my report]
Handler (desktop)
| Code     Received   Acknowledge by  Feedback by  Status        |
| 7KQ2-M9  11-12      11-19           2027-02-12   acknowledged  |
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F9-07 step 3, U01 | desktop | ![FL-F9-07 step 3, U01, light](../../images/07-fair-pay-and-speaking-up/u01-employee/3-whistleblowing-desktop-light.png) | ![FL-F9-07 step 3, U01, dark](../../images/07-fair-pay-and-speaking-up/u01-employee/3-whistleblowing-desktop-dark.png) |
| FL-F9-07 step 3, U01 | phone | ![FL-F9-07 step 3, U01, light](../../images/07-fair-pay-and-speaking-up/u01-employee/3-whistleblowing-phone-light.png) | ![FL-F9-07 step 3, U01, dark](../../images/07-fair-pay-and-speaking-up/u01-employee/3-whistleblowing-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f09-21-whistleblowing-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f09-21-whistleblowing-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f09-21-whistleblowing-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f09-21-whistleblowing-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f09-21-whistleblowing-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f09-21-whistleblowing-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f09-21-whistleblowing-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f09-21-whistleblowing-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Editable |
|---|---|---|
| Facts, files, identity | E-F9-21 | reporter |
| Dates, status | E-F9-21 | handler |

## Actions

| Action | Who | Result |
|---|---|---|
| Send | anyone | Report with a code |
| Acknowledge, give feedback | handlers | Dates kept |

## States

- Normal: make a report, follow it by its code, and handle it.
- Empty: no report: "No report received".
- Loading: skeleton rows in place of the list ([C-03](../../../../04-ux/design-system/components/c-03-data-table.md));
  actions disabled until it has loaded.
- Error: the error message pattern (D122).
- Read-only: for the owner: counts only.
- Offline: Not available offline: reports go straight to the server, never kept on a device.

Shown entities (VD-15): [E-F9-21 Whistleblowing report](../../data/e-f09-21-whistleblowing-report.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F9-21 Whistleblowing report | Received | Badge "Received"; a new record starts here; next: Acknowledged (UC-F9-24); fields editable within the role | U01, U06 | `u01-employee/s-f09-21-whistleblowing-e-f09-21-whistleblowing-report-received-{desktop,phone}-{light,dark}.png`, `u06-hr/s-f09-21-whistleblowing-e-f09-21-whistleblowing-report-received-desktop-{light,dark}.png` |
| E-F9-21 Whistleblowing report | Acknowledged | Badge "Acknowledged"; next: Closed (UC-F9-24); fields editable within the role | U01, U06 | `u01-employee/s-f09-21-whistleblowing-e-f09-21-whistleblowing-report-acknowledged-{desktop,phone}-{light,dark}.png`, `u06-hr/s-f09-21-whistleblowing-e-f09-21-whistleblowing-report-acknowledged-desktop-{light,dark}.png` |
| E-F9-21 Whistleblowing report | Closed | Badge "Closed"; final: read-only, no next state; the history shows how it got here | U01, U06 | `u01-employee/s-f09-21-whistleblowing-e-f09-21-whistleblowing-report-closed-{desktop,phone}-{light,dark}.png`, `u06-hr/s-f09-21-whistleblowing-e-f09-21-whistleblowing-report-closed-desktop-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Reporter page on any device; handler on desktop.

## Accessibility

Every status is a word, not only a colour; tables have headers; actions are buttons with labels.

## Components

- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)
- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-01 Button](../../../../04-ux/design-system/components/c-01-button.md)

## Shown in

- [FL-F9-07 Fair pay and speaking up](../../flows/fl-f09-07-fair-pay-and-speaking-up.md)

## Open questions

None.

---

⬅️ [S-F9-20 Equality and pay transparency](s-f09-20-equality-and-pay-transparency.md) · ⬆️ [Up](README.md) ·
➡️ [S-F9-22 Training plan](../09-train-and-protect/s-f09-22-training-plan.md)
