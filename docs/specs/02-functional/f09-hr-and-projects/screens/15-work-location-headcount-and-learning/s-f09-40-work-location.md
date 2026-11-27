🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
👥 [F9 HR and projects](../../README.md) › 🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-F9-15](README.md) ›
🖥️ S-F9-40 Work location

# 🖥️ S-F9-40 Work location

**Status:** ✅ specified

## Personas

- [U01 Employee](../../../../01-users/personas/u01-employee.md): their own week, on a phone.
- [U02 Manager](../../../../01-users/personas/u02-manager.md): the week of their team, on a desktop.

## Purpose

Declare where one works each day, see the quota and the allowance, and validate the team's days.

## Entry points

HR and projects › Work location; the employee home screen; the AI assistant
([BR-F3-34](../../../f03-assistant/business-rules/br-f03-34-every-capability-is-reachable-from-the-assistant.md)).

## Wireframe

```text
+---------------------------------------------------------------------------------------------+
| Work location        Week 47                                      Quota 2 home days   used 2 |
| ------------------------------------------------------------------------------------------- |
| EMPLOYEE        MON      TUE      WED      THU      FRI      ALLOWANCE   STATE              |
| Claire P.       Office   Office   Home     Home     Office   20.00       Declared           |
| Marc D.         Office   Home     Office   Office   Home     20.00       Validated          |
| Sonia M.        Home     Home     Home     Office   Office   10.00       Over quota: exception |
| [Declare a pattern]  [Validate the team's week]  [Refuse with a reason]                     |
+---------------------------------------------------------------------------------------------+
```

Example images of the empty, loading, read-only and offline states, drawn in the image round
([D120](../../../../06-decisions/ux/d120-png-mockups.md)): `s-f09-40-work-location-empty-desktop-{light,dark}.png`,
`s-f09-40-work-location-empty-phone-{light,dark}.png`, `s-f09-40-work-location-loading-desktop-{light,dark}.png`,
`s-f09-40-work-location-loading-phone-{light,dark}.png`, `s-f09-40-work-location-offline-desktop-{light,dark}.png`,
`s-f09-40-work-location-offline-phone-{light,dark}.png`, `s-f09-40-work-location-read-only-desktop-{light,dark}.png`,
`s-f09-40-work-location-read-only-phone-{light,dark}.png`.

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F9-15 step 1, U01 | phone | ![FL-F9-15 step 1, U01, light](../../images/15-work-location-headcount-and-learning/u01-employee/1-work-location-phone-light.png) | ![FL-F9-15 step 1, U01, dark](../../images/15-work-location-headcount-and-learning/u01-employee/1-work-location-phone-dark.png) |
| FL-F9-15 step 1, U01 | desktop | ![FL-F9-15 step 1, U01, light](../../images/15-work-location-headcount-and-learning/u01-employee/1-work-location-desktop-light.png) | ![FL-F9-15 step 1, U01, dark](../../images/15-work-location-headcount-and-learning/u01-employee/1-work-location-desktop-dark.png) |
| FL-F9-15 step 1, U01 | phone | ![FL-F9-15 step 1, U01, light](../../images/15-work-location-headcount-and-learning/u01-employee/1-work-location-phone-light.png) | ![FL-F9-15 step 1, U01, dark](../../images/15-work-location-headcount-and-learning/u01-employee/1-work-location-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f09-40-work-location-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f09-40-work-location-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f09-40-work-location-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f09-40-work-location-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f09-40-work-location-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f09-40-work-location-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f09-40-work-location-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f09-40-work-location-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Day and location | E-F9-48 date and location | one choice per day | yes | yes |
| Other site | E-F9-48 other site | text | when other site | no |
| Quota used | agreement and E-F9-48 | n of m days | no | yes |
| Allowance | E-F9-48 allowance | money | no | no |
| State | E-F9-48 state | badge | no | yes |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Declare | day cell | the employee | the day is declared (UC-F9-43) |
| Declare a pattern | header | the employee | the days of the next 3 months are created |
| Validate | team row, header | the manager | the days are validated and counted |
| Refuse | team row | the manager | the day is refused with the reason |
| Withdraw | day cell | the employee | the day is withdrawn |

## States

- Normal: the week with one cell per day, the quota used and the allowance of each home day.
- Empty: No day declared this week: a hint to declare the first day and the agreement's quota.
- Loading: The week's cells as placeholders, then the quota.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); a day over the
  quota says so under its cell.
- Read-only: a closed month or a validated day passed to pay: shown, with no action.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-F9-48 Work location day](../../data/e-f09-48-work-location-day.md),
[E-F9-01 Employee record](../../data/e-f09-01-employee-record.md), [E-F9-02 Contract](../../data/e-f09-02-contract.md),
[E-F9-09 Time-off request](../../data/e-f09-09-time-off-request.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F9-48 Work location day | Declared | Badge "Declared"; a new record starts here; next: Validated or Refused or Withdrawn (UC-F9-43); fields editable within the role | U01, U02 | `u01-employee/s-f09-40-work-location-e-f09-48-work-location-day-declared-{desktop,phone}-{light,dark}.png`; `u02-manager/s-f09-40-work-location-e-f09-48-work-location-day-declared-{desktop,phone}-{light,dark}.png` |
| E-F9-48 Work location day | Validated | Badge "Validated"; next: Passed to pay or Withdrawn (BR-F9-42, UC-F9-43); fields editable within the role | U01, U02 | `u01-employee/s-f09-40-work-location-e-f09-48-work-location-day-validated-{desktop,phone}-{light,dark}.png`; `u02-manager/s-f09-40-work-location-e-f09-48-work-location-day-validated-{desktop,phone}-{light,dark}.png` |
| E-F9-48 Work location day | Refused | Badge "Refused"; final state, read-only | U01, U02 | `u01-employee/s-f09-40-work-location-e-f09-48-work-location-day-refused-{desktop,phone}-{light,dark}.png`; `u02-manager/s-f09-40-work-location-e-f09-48-work-location-day-refused-{desktop,phone}-{light,dark}.png` |
| E-F9-48 Work location day | Withdrawn | Badge "Withdrawn"; final state, read-only | U01, U02 | `u01-employee/s-f09-40-work-location-e-f09-48-work-location-day-withdrawn-{desktop,phone}-{light,dark}.png`; `u02-manager/s-f09-40-work-location-e-f09-48-work-location-day-withdrawn-{desktop,phone}-{light,dark}.png` |
| E-F9-48 Work location day | Passed to pay | Badge "Passed to pay"; final state, read-only | U01, U02 | `u01-employee/s-f09-40-work-location-e-f09-48-work-location-day-passed-to-pay-{desktop,phone}-{light,dark}.png`; `u02-manager/s-f09-40-work-location-e-f09-48-work-location-day-passed-to-pay-{desktop,phone}-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per persona, device and theme; the
image round draws them. Rows are derived from each entity's Lifecycle: the badge is the state's name, the next states
are its transitions, and a final state is read-only.

## Responsive behaviour

On a phone, the week is a list of five days with a location choice each; the team view is desktop.

## Accessibility

Each location is a word and an icon; the quota is read as a sentence; keyboard: next day, choose, validate.

## Components

- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)
- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-14 Timeline](../../../../04-ux/design-system/components/c-14-timeline.md)
- [C-01 Button](../../../../04-ux/design-system/components/c-01-button.md)

## Shown in

- [FL-F9-15 Work location, headcount, careers and learning](../../flows/fl-f09-15-work-location-headcount-and-learning.md)

## Open questions

None.

---

⬅️ [S-F9-39 Prospect conversations](../02-recruit/s-f09-39-prospect-conversations.md) · ⬆️ [Up](README.md) ·
➡️ [S-F9-41 Headcount plan](s-f09-41-headcount-plan.md)
