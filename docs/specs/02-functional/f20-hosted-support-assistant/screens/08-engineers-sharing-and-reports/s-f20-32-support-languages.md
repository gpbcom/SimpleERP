🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🛟 [F20 Hosted support assistant (hosted edition)](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F20-08 Engineers, screen sharing, reports and languages](README.md) › 🖥️ S-F20-32 Support languages

# 🖥️ S-F20-32 Support languages

**Status:** ✅ specified

## Personas

- [U07 Administrator](../../../../01-users/personas/u07-administrator.md): the languages of the company and their times.

## Purpose

Choose the support languages of the company and see that each has the plan's times.

## Entry points

Hosted support assistant › Languages; Settings › Languages; a request answered in English with a note.

## Wireframe

```text
+---------------------------------------------------------------------------------------------+
| Support languages               Plan: Business     Times: urgent 1 hour, others 1 working day  |
|---------------------------------------------------------------------------------------------|
| LANGUAGE   COVERED HOURS         CHOSEN   FIRST ANSWER   RESOLUTION    REQUESTS (30 DAYS)     |
| French     Mon-Fri 8:00-19:00    [x]      1 h / 1 day    1 day         14                     |
| English    Mon-Fri 8:00-19:00    [x]      1 h / 1 day    1 day         5                      |
| German     Mon-Fri 9:00-17:00    [x]      1 h / 1 day    1 day         2                      |
| Spanish    Not yet covered       [ ]      Ask to be told                                       |
+---------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F20-08 step 4, U07 | desktop | ![FL-F20-08 step 4, U07, light](../../images/08-engineers-sharing-and-reports/u07-administrator/4-support-languages-desktop-light.png) | ![FL-F20-08 step 4, U07, dark](../../images/08-engineers-sharing-and-reports/u07-administrator/4-support-languages-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f20-32-support-languages-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f20-32-support-languages-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f20-32-support-languages-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f20-32-support-languages-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f20-32-support-languages-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f20-32-support-languages-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f20-32-support-languages-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f20-32-support-languages-offline-desktop-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Language | supported list | text | no | yes |
| Covered hours | rota coverage | days and hours | no | yes |
| Chosen | company support languages | yes, no | by the administrator | yes |
| First answer and resolution | plan times | hours and days | no | yes |
| Requests over 30 days | counts by language | number | no | no |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Choose languages | list | administrator | saves the company's support languages |
| Ask to be told | language | administrator | an alert when the language is covered |
| Read the figures | header | administrator, owner | the requests and times by language |
| Change my language | user menu | every user | sets the user's own language |

## States

- Normal: the supported languages with their coverage, the plan's times and the company's choice.
- Empty: Only French and English are supported for now, with Ask to be told.
- Loading: the headings and the table as placeholders; the values follow.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); a language with
  lost coverage is flagged with the date it stops.
- Read-only: the record in a locked state: values shown, no action offered.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): none; no flow's Entities and screens table names an entity on this screen.

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

- [FL-F20-08](../../flows/fl-f20-08-engineers-sharing-and-reports.md)

## Open questions

None.

---

⬅️ [S-F20-31 Health report](s-f20-31-health-report.md) · ⬆️ [Up](README.md) ·
➡️ [S-F20-L01 Support requests](../00-lists/s-f20-l01-support-requests.md)
