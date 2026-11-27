🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🛟 [F20 Hosted support assistant (hosted edition)](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F20-08 Engineers, screen sharing, reports and languages](README.md) › 🖥️ S-F20-30 Consented access

# 🖥️ S-F20-30 Consented access

**Status:** ✅ specified

## Personas

- [U07 Administrator](../../../../01-users/personas/u07-administrator.md): the requests to answer and the accesses
  running.
- [U48 Hosting engineer](../../../../01-users/personas/u48-hosting-engineer.md): the accesses they ask for.

## Purpose

Let an engineer see the problem for a limited time, with the customer's consent and a record.

## Entry points

Hosted support assistant › Access; the call's page; the notification of a request.

## Wireframe

```text
+---------------------------------------------------------------------------------------------+
| Consented access                                              Running now 1     Requests 1     |
|---------------------------------------------------------------------------------------------|
| REQUEST: Mehdi K. asks a read-only view as Accounting, 30 minutes, for request 4127            |
| Why: see the posting screen error     Personal data: masked     Data changes: none            |
| [Grant 30 min] [Grant 15 min] [Refuse]                                                       |
| RUNNING: Mehdi K., read-only as Accounting, until 14:30 (12 min left)           [Stop now]    |
| ENDED: 2026-11-12 screen share, 20 min, 6 pages seen                                          |
+---------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F20-08 step 2, U07 | desktop | ![FL-F20-08 step 2, U07, light](../../images/08-engineers-sharing-and-reports/u07-administrator/2-consented-access-desktop-light.png) | ![FL-F20-08 step 2, U07, dark](../../images/08-engineers-sharing-and-reports/u07-administrator/2-consented-access-desktop-dark.png) |
| Error E1, U07 | desktop | ![Error E1, U07, light](../../images/08-engineers-sharing-and-reports/u07-administrator/e1-the-access-has-expired-desktop-light.png) | ![Error E1, U07, dark](../../images/08-engineers-sharing-and-reports/u07-administrator/e1-the-access-has-expired-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f20-30-consented-access-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f20-30-consented-access-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f20-30-consented-access-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f20-30-consented-access-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f20-30-consented-access-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f20-30-consented-access-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f20-30-consented-access-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f20-30-consented-access-offline-desktop-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Engineer and reason | E-F20-20 engineer, reason | name and text | no | yes |
| Kind | E-F20-20 kind | screen share, read-only view | no | yes |
| Role seen | E-F20-20 role | a role of the company | by the administrator | when a view |
| Limit | E-F20-20 limit | minutes, at most 240 | by the administrator | yes |
| State | E-F20-20 state | badge | no | yes |
| Pages seen | E-F20-20 record | list | no | no |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Ask for access | request | hosting engineer | sends the request to the administrator |
| Grant or shorten | request | administrator | opens the access for the limit |
| Refuse | request | administrator | the engineer is told |
| Stop now | running access | administrator, engineer | ends it at once |

## States

- Normal: the requests, the access running and the ended ones with their record.
- Empty: No access asked or granted yet.
- Loading: the headings and the table as placeholders; the values follow.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); an expired
  access says it ended at its limit and shows nothing more.
- Read-only: the record in a locked state: values shown, no action offered.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-F20-20 Access grant](../../data/e-f20-20-access-grant.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F20-20 Access grant | Requested | Badge "Requested"; a new record starts here; next: Granted or Refused (UC-F20-30); fields editable within the role | U07, U48 | `u07-administrator/s-f20-30-consented-access-e-f20-20-access-grant-requested-desktop-{light,dark}.png`, `u48-hosting-engineer/s-f20-30-consented-access-e-f20-20-access-grant-requested-{desktop,phone}-{light,dark}.png` |
| E-F20-20 Access grant | Granted | Badge "Granted"; next: Active or Ended (UC-F20-30, BR-F20-21); fields editable within the role | U07, U48 | `u07-administrator/s-f20-30-consented-access-e-f20-20-access-grant-granted-desktop-{light,dark}.png`, `u48-hosting-engineer/s-f20-30-consented-access-e-f20-20-access-grant-granted-{desktop,phone}-{light,dark}.png` |
| E-F20-20 Access grant | Refused | Badge "Refused"; final: read-only, no next state; the history shows how it got here | U07, U48 | `u07-administrator/s-f20-30-consented-access-e-f20-20-access-grant-refused-desktop-{light,dark}.png`, `u48-hosting-engineer/s-f20-30-consented-access-e-f20-20-access-grant-refused-{desktop,phone}-{light,dark}.png` |
| E-F20-20 Access grant | Active | Badge "Active"; next: Ended (BR-F20-21); fields editable within the role | U07, U48 | `u07-administrator/s-f20-30-consented-access-e-f20-20-access-grant-active-desktop-{light,dark}.png`, `u48-hosting-engineer/s-f20-30-consented-access-e-f20-20-access-grant-active-{desktop,phone}-{light,dark}.png` |
| E-F20-20 Access grant | Ended | Badge "Ended"; final: read-only, no next state; the history shows how it got here | U07, U48 | `u07-administrator/s-f20-30-consented-access-e-f20-20-access-grant-ended-desktop-{light,dark}.png`, `u48-hosting-engineer/s-f20-30-consented-access-e-f20-20-access-grant-ended-{desktop,phone}-{light,dark}.png` |

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

- [FL-F20-08](../../flows/fl-f20-08-engineers-sharing-and-reports.md)

## Open questions

None.

---

⬅️ [S-F20-29 Engineer booking](s-f20-29-engineer-booking.md) · ⬆️ [Up](README.md) ·
➡️ [S-F20-31 Health report](s-f20-31-health-report.md)
