🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🏋️ [SC18 Sports and fitness](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC18-03 Licences and competitions](README.md) ›
🖥️ S-SC18-11 Teams and competitions

# 🖥️ S-SC18-11 Teams and competitions

**Status:** ✅ specified

## Personas

- [U53 Coach](../../../../01-users/personas/u53-coach.md): the teams they coach and their calendars.

## Purpose

Build teams from licensed players, register them in competitions and send the calendar.

## Entry points

Sports and fitness › Teams; a competition's page; the AI assistant.

## Wireframe

```text
+--------------------------------------------------------------------------------------------------+
| Team: U15 football                                                      Registered               |
| Competition  District league U15   Matches 18   Captain Lena T.                                  |
| Player       Licence      Category   Certificate   State                                         |
| Lena T.      F-440012     U15        valid         ok                                            |
| Tom R.       F-440031     U16        expired       cannot play                                   |
| [Add a player]  [Register]  [Send the calendar]                                                  |
+--------------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC18-03 step 3, U53 | phone | ![FL-SC18-03 step 3, U53, light](../../images/03-licences-and-competitions/u53-coach/3-teams-and-competitions-phone-light.png) | ![FL-SC18-03 step 3, U53, dark](../../images/03-licences-and-competitions/u53-coach/3-teams-and-competitions-phone-dark.png) |
| Empty | phone | ![Empty, light](../../images/states/s-sc18-11-teams-and-competitions-empty-phone-light.png) | ![Empty, dark](../../images/states/s-sc18-11-teams-and-competitions-empty-phone-dark.png) |
| Loading | phone | ![Loading, light](../../images/states/s-sc18-11-teams-and-competitions-loading-phone-light.png) | ![Loading, dark](../../images/states/s-sc18-11-teams-and-competitions-loading-phone-dark.png) |
| Read-only | phone | ![Read-only, light](../../images/states/s-sc18-11-teams-and-competitions-read-only-phone-light.png) | ![Read-only, dark](../../images/states/s-sc18-11-teams-and-competitions-read-only-phone-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc18-11-teams-and-competitions-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc18-11-teams-and-competitions-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Team | E-SC18-08 name | text | yes while Forming | yes |
| Category | E-SC18-08 category | choice | yes while Forming | yes |
| Competition | E-SC18-08 competition | link | yes while Forming | yes |
| Players | E-SC18-08 players | list of members | yes while Forming | yes |
| Captain | E-SC18-08 captain | member | yes while Forming | no |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Add a player | header | coach | a licensed player joins the team |
| Register | header | coach | the team becomes Registered |
| Withdraw | header | coach, owner | the team becomes Withdrawn |
| Send the calendar | header | coach | the matches go to the players |

## States

- Normal: the team with its players, their licences, categories and certificates.
- Empty: No team yet, with New team.
- Loading: the headings and the table as placeholders; the values follow.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); a player with
  no licence, a wrong category or an expired certificate, with the reason.
- Read-only: the record in a locked state: values shown, no action offered.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-SC18-08 Sports team](../../data/e-sc18-08-team.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC18-08 Sports team | Forming | Badge "Forming"; a new record starts here; next: Registered or Withdrawn (BR-SC18-11, UC-SC18-11); fields editable within the role | U53 | `u53-coach/s-sc18-11-teams-and-competitions-e-sc18-08-team-forming-phone-{light,dark}.png` |
| E-SC18-08 Sports team | Registered | Badge "Registered"; next: Withdrawn or Archived (UC-SC18-11); fields editable within the role | U53 | `u53-coach/s-sc18-11-teams-and-competitions-e-sc18-08-team-registered-phone-{light,dark}.png` |
| E-SC18-08 Sports team | Withdrawn | Badge "Withdrawn"; final: read-only, no next state; the history shows how it got here | U53 | `u53-coach/s-sc18-11-teams-and-competitions-e-sc18-08-team-withdrawn-phone-{light,dark}.png` |
| E-SC18-08 Sports team | Archived | Badge "Archived"; final: read-only, no next state; the history shows how it got here | U53 | `u53-coach/s-sc18-11-teams-and-competitions-e-sc18-08-team-archived-phone-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

The coach and the member use the phone, the owner and the treasurer a desktop, with the same actions in one column.

## Accessibility

Every control is reachable by keyboard; states and errors are announced to screen readers and never rely on colour
alone; each field has its visible label.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)
- [C-01 Button](../../../../04-ux/design-system/components/c-01-button.md)

## Shown in

- [FL-SC18-03 Licences and competitions](../../flows/fl-sc18-03-licences-and-competitions.md)

## Open questions

None.

---

⬅️ [S-SC18-10 Medical certificates](s-sc18-10-medical-certificates.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC18-12 Results](s-sc18-12-results.md)
