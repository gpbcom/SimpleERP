🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🛟 [F20 Hosted support assistant (hosted edition)](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F20-08 Engineers, screen sharing, reports and languages](README.md) › 🖥️ S-F20-31 Health report

# 🖥️ S-F20-31 Health report

**Status:** ✅ specified

## Personas

- [U07 Administrator](../../../../01-users/personas/u07-administrator.md): the report of each month.
- [U13 Owner](../../../../01-users/personas/u13-owner.md): the one-page summary, from their phone.

## Purpose

Read the month's health of the hosted environment and the advice that follows.

## Entry points

Hosted support assistant › Health reports; the monthly email; the owner's home page.

## Wireframe

```text
+---------------------------------------------------------------------------------------------+
| Health report: October 2026                         Sent 2026-11-02     Month [Oct 2026 v]       |
|---------------------------------------------------------------------------------------------|
| Availability 99.92 % (target 99.9 %) OK      Incidents 1 (42 min)      Slowest report 3.1 s      |
| Backups: daily, last restore test 2026-10-20 OK       Storage 71 % of the quota                |
| Support: 6 requests, first answer within target 6 of 6      Credits due: none                |
| ADVICE: 1 Storage will be full in about 5 months.  2 The sales report is slow on Mondays.     |
| [Download PDF] [Ask the AI assistant about this report]                                       |
+---------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F20-08 step 3, U07 | desktop | ![FL-F20-08 step 3, U07, light](../../images/08-engineers-sharing-and-reports/u07-administrator/3-health-report-desktop-light.png) | ![FL-F20-08 step 3, U07, dark](../../images/08-engineers-sharing-and-reports/u07-administrator/3-health-report-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f20-31-health-report-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f20-31-health-report-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f20-31-health-report-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f20-31-health-report-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f20-31-health-report-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f20-31-health-report-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f20-31-health-report-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f20-31-health-report-offline-desktop-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Month | E-F20-21 month | month | no | yes |
| Availability and incidents | E-F20-21 availability, incidents | percent, minutes | no | yes |
| Speed | E-F20-21 slowest report | seconds | no | no |
| Backups and restore test | E-F20-21 backups | text and date | no | yes |
| Storage and quota | E-F20-21 storage used | percent | no | yes |
| Support and credits | E-F20-21 requests, credits | numbers | no | yes |
| Advice | E-F20-21 advice | up to five lines | by the engineer while held | no |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Open another month | header | administrator, owner | shows the archived report |
| Download PDF | header | administrator, owner | the report as a PDF |
| Ask the AI assistant | header | administrator, owner | a question about the report's figures |
| Edit and release | held report | hosting engineer | removes what the check found and sends |

## States

- Normal: the month's figures against the plan's targets, with the advice.
- Empty: No report yet: the first one comes on the first working day of next month.
- Loading: the headings and the table as placeholders; the values follow.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); a held report
  says that it is being checked and when it will be sent.
- Read-only: the record in a locked state: values shown, no action offered.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-F20-21 Health report](../../data/e-f20-21-health-report.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F20-21 Health report | Generated | Badge "Generated"; a new record starts here; next: Sent or Held (BR-F20-22); fields editable within the role | U07, U13 | `u07-administrator/s-f20-31-health-report-e-f20-21-health-report-generated-desktop-{light,dark}.png`, `u13-owner/s-f20-31-health-report-e-f20-21-health-report-generated-{desktop,phone}-{light,dark}.png` |
| E-F20-21 Health report | Sent | Badge "Sent"; next: Read (UC-F20-31); fields editable within the role | U07, U13 | `u07-administrator/s-f20-31-health-report-e-f20-21-health-report-sent-desktop-{light,dark}.png`, `u13-owner/s-f20-31-health-report-e-f20-21-health-report-sent-{desktop,phone}-{light,dark}.png` |
| E-F20-21 Health report | Held | Badge "Held"; next: Sent (UC-F20-31); fields editable within the role | U07, U13 | `u07-administrator/s-f20-31-health-report-e-f20-21-health-report-held-desktop-{light,dark}.png`, `u13-owner/s-f20-31-health-report-e-f20-21-health-report-held-{desktop,phone}-{light,dark}.png` |
| E-F20-21 Health report | Read | Badge "Read"; final: read-only, no next state; the history shows how it got here | U07, U13 | `u07-administrator/s-f20-31-health-report-e-f20-21-health-report-read-desktop-{light,dark}.png`, `u13-owner/s-f20-31-health-report-e-f20-21-health-report-read-{desktop,phone}-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

The administrator reads the full report on a computer. The owner reads a one-page summary on a phone: availability,
incidents, credits due and the top advice.

## Accessibility

Every control is reachable by keyboard; states and errors are announced to screen readers and never rely on colour
alone; each field has its visible label.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)
- [C-01 Button](../../../../04-ux/design-system/components/c-01-button.md)

## Shown in

- [FL-F20-08](../../flows/fl-f20-08-engineers-sharing-and-reports.md)

## Open questions

None.

---

⬅️ [S-F20-30 Consented access](s-f20-30-consented-access.md) · ⬆️ [Up](README.md) ·
➡️ [S-F20-32 Support languages](s-f20-32-support-languages.md)
