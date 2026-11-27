🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🏛️ [SC20 Public bodies](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC20-04 Public-sector HR and pay](README.md) ›
🖥️ S-SC20-13 Grades and steps

# 🖥️ S-SC20-13 Grades and steps

**Status:** ✅ specified

## Personas

- [U06 Human resources](../../../../01-users/personas/u06-hr.md): the grades, the placement of each employee and the
  step changes due.

## Purpose

Keep the grades and steps of the body's staff and move each employee at the date the statute allows.

## Entry points

Public bodies › Grades; an employee's page; the monthly list of step changes.

## Wireframe

```text
+--------------------------------------------------------------------------------------------------+
| Grades                                               [Place an employee] [Step changes due]      |
| Grade       Category   Step   Index number   Time in step   Employees   State                    |
| Technician  B          4      410            2 years        6           Active                   |
| Technician  B          5      430            2 years        3           Active                   |
| Admin. 2    C          2      364            1 year         9           Active                   |
| Due this month: 3     Mismatch: 1 (Roux, grade B, post category C)                               |
+--------------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC20-04 step 1, U06 | desktop | ![FL-SC20-04 step 1, U06, light](../../images/04-public-hr-and-pay/u06-hr/1-grades-and-steps-desktop-light.png) | ![FL-SC20-04 step 1, U06, dark](../../images/04-public-hr-and-pay/u06-hr/1-grades-and-steps-desktop-dark.png) |
| Error E1, U06 | desktop | ![Error E1, U06, light](../../images/04-public-hr-and-pay/u06-hr/e1-the-grade-does-not-match-the-post-desktop-light.png) | ![Error E1, U06, dark](../../images/04-public-hr-and-pay/u06-hr/e1-the-grade-does-not-match-the-post-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc20-13-grades-and-steps-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc20-13-grades-and-steps-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc20-13-grades-and-steps-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc20-13-grades-and-steps-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc20-13-grades-and-steps-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc20-13-grades-and-steps-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-sc20-13-grades-and-steps-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-sc20-13-grades-and-steps-offline-desktop-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Grade | E-SC20-11 grade | text | yes while Draft | yes |
| Category | E-SC20-11 category | text from the pack | yes while Draft | yes |
| Step | E-SC20-11 step | number | yes while Draft | yes |
| Index number | E-SC20-11 index number | number | yes while Draft | yes |
| Time in step | E-SC20-11 time | duration | yes while Draft | yes |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Place an employee | header | HR | an employee is placed in a grade and a step |
| Approve step changes | header | HR | the due changes are made and sent to payroll |
| Close grade | row | HR | a grade is closed to new placements |

## States

- Normal: the grades with category, step, index number, time in step, employees and state.
- Empty: No grade yet, with Load the pack's grades.
- Loading: the headings and the table as placeholders; the values follow.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); a grade not
  matching the post, a change before the minimum time, with the employee named.
- Read-only: the record in a locked state: values shown, no action offered.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-SC20-11 Grade](../../data/e-sc20-11-grade.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC20-11 Grade | Draft | Badge "Draft"; a new record starts here; next: Active (UC-SC20-13); fields editable within the role | U06 | `u06-hr/s-sc20-13-grades-and-steps-e-sc20-11-grade-draft-desktop-{light,dark}.png` |
| E-SC20-11 Grade | Active | Badge "Active"; next: Closed (UC-SC20-13); fields editable within the role | U06 | `u06-hr/s-sc20-13-grades-and-steps-e-sc20-11-grade-active-desktop-{light,dark}.png` |
| E-SC20-11 Grade | Closed | Badge "Closed"; final: read-only, no next state; the history shows how it got here | U06 | `u06-hr/s-sc20-13-grades-and-steps-e-sc20-11-grade-closed-desktop-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop only; on a phone, the app asks to continue on a larger screen.

## Accessibility

Every control is reachable by keyboard; states and errors are announced to screen readers and never rely on colour
alone; each field has its visible label.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)
- [C-01 Button](../../../../04-ux/design-system/components/c-01-button.md)

## Shown in

- [FL-SC20-04 Public-sector HR and pay](../../flows/fl-sc20-04-public-hr-and-pay.md)

## Open questions

None.

---

⬅️ [S-SC20-12 Council decisions](../03-citizen-services/s-sc20-12-council-decisions.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC20-14 Statutory pay](s-sc20-14-statutory-pay.md)
