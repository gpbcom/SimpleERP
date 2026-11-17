🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
👥 [F9 HR and projects](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F9-10 Listen to employees](README.md) › 🖥️ S-F9-25 Surveys and exit interviews

# 🖥️ S-F9-25 Surveys and exit interviews

**Status:** ✅ specified

## Personas

- [U06 Human resources](../../../../01-users/personas/u06-hr.md)
- [U01 Employee](../../../../01-users/personas/u01-employee.md)
- [U13 Owner](../../../../01-users/personas/u13-owner.md)

## Purpose

Send engagement surveys, read results by group, and record exit interviews.

## Entry points

HR › Surveys.

## Wireframe

```text
+------------------------------------------------------------------+
| Engagement 2026   48 answers of 60                                |
| Group        Answers  Score  Trend                               |
| Lyon         31       7.2    +0.4                                 |
| Vienne       4        hidden (fewer than 5)                       |
| Exit reasons 2026: workload 5, pay 3, move 2   [Record interview] |
+------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F9-10 step 1, U06 | desktop | ![FL-F9-10 step 1, U06, light](../../images/10-listen-to-employees/u06-hr/1-surveys-and-exit-interviews-desktop-light.png) | ![FL-F9-10 step 1, U06, dark](../../images/10-listen-to-employees/u06-hr/1-surveys-and-exit-interviews-desktop-dark.png) |
| Error E1, U06 | desktop | ![Error E1, U06, light](../../images/10-listen-to-employees/u06-hr/e1-surveys-and-exit-interviews-refused-desktop-light.png) | ![Error E1, U06, dark](../../images/10-listen-to-employees/u06-hr/e1-surveys-and-exit-interviews-refused-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f09-25-surveys-and-exit-interviews-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f09-25-surveys-and-exit-interviews-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f09-25-surveys-and-exit-interviews-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f09-25-surveys-and-exit-interviews-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f09-25-surveys-and-exit-interviews-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f09-25-surveys-and-exit-interviews-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f09-25-surveys-and-exit-interviews-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f09-25-surveys-and-exit-interviews-offline-desktop-dark.png) |

## Fields and columns

| Label | Data | Editable |
|---|---|---|
| Groups, scores, exit reasons | E-F5-08, E-F9-01 | interviews |

## Actions

| Action | Who | Result |
|---|---|---|
| Send survey | HR | Survey sent |
| Record interview | HR | Reasons coded |

## States

- Normal: send engagement surveys, read results by group, and record exit interviews.
- Empty: no survey yet: Create a survey.
- Loading: skeleton rows in place of the list ([C-03](../../../../04-ux/design-system/components/c-03-data-table.md));
  actions disabled until it has loaded.
- Error: the error message pattern (D122).
- Read-only: for managers: their group above the threshold.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md)); the app shows that it is offline and reloads the
  screen when the network is back.

Shown entities (VD-15): [E-F5-08 Survey](../../../f05-social-media/data/e-f05-08-survey.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F5-08 Survey | Draft | Badge "Draft"; a new record starts here; next: Sent (UC-F5-12); fields editable within the role | U01, U06 | `u01-employee/s-f09-25-surveys-and-exit-interviews-e-f05-08-survey-draft-{desktop,phone}-{light,dark}.png`, `u06-hr/s-f09-25-surveys-and-exit-interviews-e-f05-08-survey-draft-desktop-{light,dark}.png` |
| E-F5-08 Survey | Sent | Badge "Sent"; next: Closed (UC-F5-12); fields editable within the role | U01, U06 | `u01-employee/s-f09-25-surveys-and-exit-interviews-e-f05-08-survey-sent-{desktop,phone}-{light,dark}.png`, `u06-hr/s-f09-25-surveys-and-exit-interviews-e-f05-08-survey-sent-desktop-{light,dark}.png` |
| E-F5-08 Survey | Closed | Badge "Closed"; final: read-only, no next state; the history shows how it got here | U01, U06 | `u01-employee/s-f09-25-surveys-and-exit-interviews-e-f05-08-survey-closed-{desktop,phone}-{light,dark}.png`, `u06-hr/s-f09-25-surveys-and-exit-interviews-e-f05-08-survey-closed-desktop-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop; answers on any device.

## Accessibility

Every status is a word, not only a colour; tables have headers; actions are buttons with labels.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-09 Chart](../../../../04-ux/design-system/components/c-09-chart.md)
- [C-01 Button](../../../../04-ux/design-system/components/c-01-button.md)

## Shown in

- [FL-F9-10 Listen to employees](../../flows/fl-f09-10-listen-to-employees.md)

## Open questions

None.

---

⬅️ [S-F9-24 Risk assessment](../09-train-and-protect/s-f09-24-risk-assessment.md) · ⬆️ [Up](README.md) ·
➡️ [S-F9-26 Capacity planning](../11-capacity-rounds-and-partners/s-f09-26-capacity-planning.md)
