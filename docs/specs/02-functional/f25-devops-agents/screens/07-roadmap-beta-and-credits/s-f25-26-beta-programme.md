🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🤖 [F25 DevOps agents (hosted edition)](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F25-07 Roadmap, beta, credits and changelog](README.md) › 🖥️ S-F25-26 Beta programme

# 🖥️ S-F25-26 Beta programme

**Status:** ✅ specified

## Personas

- [U07 Administrator](../../../../01-users/personas/u07-administrator.md): the beta features, their enrolments and their
  copies.

## Purpose

Join the beta of a feature on a sandbox copy, choose who enters and give feedback.

## Entry points

DevOps agents › Beta programme; the roadmap's Try it in beta action.

## Wireframe

```text
+---------------------------------------------------------------------------------------------+
| Beta programme                                   Open betas 3   My enrolments 1      [Join]  |
|---------------------------------------------------------------------------------------------|
| FEATURE              MODULE      WARNING                         ENROLMENT       COPY        |
| New stock counts     Stock       may change before release       Active          2026-11-30  |
| Payslip export       Payroll     reads payroll data of the copy  Requested       -           |
| Copy: masked personal data, 3 colleagues, ends 2026-11-30                                    |
| [Join] [Send feedback] [Add a colleague] [Leave and delete the copy]                         |
+---------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F25-07 step 2, U07 | desktop | ![FL-F25-07 step 2, U07, light](../../images/07-roadmap-beta-and-credits/u07-administrator/2-beta-programme-desktop-light.png) | ![FL-F25-07 step 2, U07, dark](../../images/07-roadmap-beta-and-credits/u07-administrator/2-beta-programme-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f25-26-beta-programme-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f25-26-beta-programme-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f25-26-beta-programme-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f25-26-beta-programme-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f25-26-beta-programme-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f25-26-beta-programme-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f25-26-beta-programme-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f25-26-beta-programme-offline-desktop-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Feature and module | E-F25-17 feature, module | text | no | yes |
| Warning | beta terms | text | no | yes |
| Enrolment | E-F25-17 state | badge | no | yes |
| Colleagues | E-F25-17 colleagues | list of users | yes | no |
| Copy ends on | E-F25-17 end date | date | no | no |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Join | feature | administrator | asks to enter the beta on a copy |
| Send feedback | copy | administrator, chosen colleagues | sends a note with a screenshot |
| Add a colleague | enrolment | administrator | lets a colleague enter the copy |
| Leave | enrolment | administrator | ends the enrolment and deletes the copy |

## States

- Normal: the open beta features with warnings, and the company's enrolments with their copy dates.
- Empty: No beta open now, with the roadmap link.
- Loading: the headings and the table as placeholders; the values follow.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); a copy that
  cannot be made shows the reason and keeps the enrolment as Requested.
- Read-only: the record in a locked state: values shown, no action offered.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-F25-17 Beta enrolment](../../data/e-f25-17-beta-enrolment.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F25-17 Beta enrolment | Requested | Badge "Requested"; a new record starts here; next: Active or Declined (UC-F25-26); fields editable within the role | U07 | `u07-administrator/s-f25-26-beta-programme-e-f25-17-beta-enrolment-requested-desktop-{light,dark}.png` |
| E-F25-17 Beta enrolment | Active | Badge "Active"; next: Ended or Withdrawn (UC-F25-26); fields editable within the role | U07 | `u07-administrator/s-f25-26-beta-programme-e-f25-17-beta-enrolment-active-desktop-{light,dark}.png` |
| E-F25-17 Beta enrolment | Declined | Badge "Declined"; final: read-only, no next state; the history shows how it got here | U07 | `u07-administrator/s-f25-26-beta-programme-e-f25-17-beta-enrolment-declined-desktop-{light,dark}.png` |
| E-F25-17 Beta enrolment | Ended | Badge "Ended"; final: read-only, no next state; the history shows how it got here | U07 | `u07-administrator/s-f25-26-beta-programme-e-f25-17-beta-enrolment-ended-desktop-{light,dark}.png` |
| E-F25-17 Beta enrolment | Withdrawn | Badge "Withdrawn"; final: read-only, no next state; the history shows how it got here | U07 | `u07-administrator/s-f25-26-beta-programme-e-f25-17-beta-enrolment-withdrawn-desktop-{light,dark}.png` |

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

- [FL-F25-07](../../flows/fl-f25-07-roadmap-beta-and-credits.md)

## Open questions

None.

---

⬅️ [S-F25-25 Public roadmap](s-f25-25-public-roadmap.md) · ⬆️ [Up](README.md) ·
➡️ [S-F25-27 Report credits](s-f25-27-report-credits.md)
