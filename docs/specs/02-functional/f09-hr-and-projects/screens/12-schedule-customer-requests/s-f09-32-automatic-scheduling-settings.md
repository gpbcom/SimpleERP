🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
👥 [F9 HR and projects](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F9-12 Schedule customer requests](README.md) › 🖥️ S-F9-32 Automatic scheduling settings

# 🖥️ S-F9-32 Automatic scheduling settings

**Status:** 🔄 draft (GH-2 step S4b, from VD-33 / D515)

## Personas

- [U02 Manager](../../../../01-users/personas/u02-manager.md), the planners' manager: their teams (D517).
- [U07 Administrator](../../../../01-users/personas/u07-administrator.md): every team (D517).
- [U25 Care coordinator](../../../../01-users/personas/u25-care-coordinator.md) and
  [U29 Dispatcher](../../../../01-users/personas/u29-dispatcher.md): read.

## Purpose

Switch the fully automatic mode on or off, by hand, per team and request type, and say what stops it and who is told.

## Entry points

HR and projects › Scheduling › Settings; "Settings" on the scheduling board (S-F9-30); the notification of a stop.

## Wireframe

```text
+---------------------------------------------------------------------------------------------+
| Automatic scheduling                                                                        |
|---------------------------------------------------------------------------------------------|
| TEAM                    MODE         REQUEST TYPES                    SINCE        BY        |
| Night deliveries        On           Standard delivery                2026-11-02   M. Durand |
| Home care north         Off          -                                 -            -         |
| Home care south         On           Bathing help, Meal help          2026-11-10   M. Durand |
|   Last stop 2026-11-13 07:12: no eligible carer for WR-2219            [Open]                |
|---------------------------------------------------------------------------------------------|
| Night deliveries                                                                            |
|   Request types   [x] Standard delivery  [ ] Dangerous goods (not allowed by its type)       |
|   Stops on        [x] No candidate  [x] Legal conflict  [x] Window missed                    |
|                   [x] Cost over [ 120 EUR ]  [x] Overlap                                     |
|   Notify          [Dispatcher: K. Benali v] [+ Add]   by [in the app v]                      |
|   Mode            ( ) Off  (o) On                       [Save]  -> "Switch on? Confirm"       |
+---------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F9-12 step 5, U02 | desktop | ![FL-F9-12 step 5, U02, light](../../images/12-schedule-customer-requests/u02-manager/5-automatic-scheduling-settings-desktop-light.png) | ![FL-F9-12 step 5, U02, dark](../../images/12-schedule-customer-requests/u02-manager/5-automatic-scheduling-settings-desktop-dark.png) |
| FL-F9-12 step 5, U02 | phone | ![FL-F9-12 step 5, U02, light](../../images/12-schedule-customer-requests/u02-manager/5-automatic-scheduling-settings-phone-light.png) | ![FL-F9-12 step 5, U02, dark](../../images/12-schedule-customer-requests/u02-manager/5-automatic-scheduling-settings-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f09-32-automatic-scheduling-settings-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f09-32-automatic-scheduling-settings-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f09-32-automatic-scheduling-settings-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f09-32-automatic-scheduling-settings-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f09-32-automatic-scheduling-settings-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f09-32-automatic-scheduling-settings-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f09-32-automatic-scheduling-settings-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f09-32-automatic-scheduling-settings-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Team | E-F9-33 team | name | no | yes |
| Mode | E-F9-33 state | off, on | switch, with a confirmation | yes |
| Request types | E-F9-33 request types (E-F2-25 allowing it) | ticks | yes | when on |
| Stops on | E-F9-33 stopping problems | ticks; every problem ticked by default | each may be unticked except the legal conflict (Proposed) | yes |
| Cost limit | E-F9-33 cost limit | amount | yes | when "cost over" is ticked |
| Notify | E-F9-33 planners notified, notice channel | people; in the app, email, phone | yes | yes, one at least |
| Last stop | the latest E-F9-28 proposal Stopped for the team | date, work request, problem | no | no |
| Since, by | E-F9-33 switched on at, by | date, name | no | when on |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Switch on | team | the planners' manager, the administrator (D517) | confirmation, then on; recorded with who and when |
| Switch off | team | the same | off at once; assignments made stay |
| Open | last stop line | the same, and planners | the proposal waiting (S-F9-31) |

## States

- Normal: every team with its mode.
- Empty: no team yet: a link to the teams.
- Loading: skeleton rows.
- Error: the error message pattern (D122); the mode is unchanged.
- Read-only: planners.
- Offline: not available offline.

Shown entities (VD-15): [E-F9-33 Automatic scheduling setting](../../data/e-f09-33-automatic-scheduling-setting.md),
[E-F9-28 Assignment proposal](../../data/e-f09-28-assignment-proposal.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F9-33 Automatic scheduling setting | Off | "Off"; Switch on | U02, U07 | `u02-manager/s-f09-32-automatic-scheduling-settings-e-f09-33-automatic-scheduling-setting-off-{desktop,phone}-{light,dark}.png`, `u07-administrator/s-f09-32-automatic-scheduling-settings-e-f09-33-automatic-scheduling-setting-off-desktop-{light,dark}.png` |
| E-F9-33 Automatic scheduling setting | On | "On", since, by; Switch off | U02, U07 | `u02-manager/s-f09-32-automatic-scheduling-settings-e-f09-33-automatic-scheduling-setting-on-{desktop,phone}-{light,dark}.png`, `u07-administrator/s-f09-32-automatic-scheduling-settings-e-f09-33-automatic-scheduling-setting-on-desktop-{light,dark}.png` |
| E-F9-28 Assignment proposal | Stopped | "Last stop" line with the problem and its time; Open | U02, U07, U29 | `u02-manager/s-f09-32-automatic-scheduling-settings-e-f09-28-assignment-proposal-stopped-{desktop,phone}-{light,dark}.png`, `u07-administrator/s-f09-32-automatic-scheduling-settings-e-f09-28-assignment-proposal-stopped-desktop-{light,dark}.png`, `u29-dispatcher/s-f09-32-automatic-scheduling-settings-e-f09-28-assignment-proposal-stopped-{desktop,phone}-{light,dark}.png` |

The states are those of the entity drafts; the setting stays on after a stop (D517, E-F9-33).

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none.

## Responsive behaviour

Desktop first; on a phone the list of teams with their mode and the last stop, read-only otherwise.

## Accessibility

The mode is a word, not only a colour; switching on asks for a confirmation that names the team and the request types;
a new stop is announced.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)
- [C-05 Modal](../../../../04-ux/design-system/components/c-05-modal.md)

## Shown in

- [FL-F9-12 Schedule customer requests](../../flows/fl-f09-12-schedule-customer-requests.md)

## Open questions

None.

---

⬅️ [S-F9-31 Proposal review](s-f09-31-proposal-review.md) · ⬆️ [Up](README.md) ·
➡️ [S-F9-33 Planning map](s-f09-33-planning-map.md)
