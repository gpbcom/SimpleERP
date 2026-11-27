🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
👥 [F9 HR and projects](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F9-12 Schedule customer requests](README.md) › 🖥️ S-F9-30 Scheduling board

# 🖥️ S-F9-30 Scheduling board

**Status:** ✅ specified

## Personas

- [U25 Care coordinator](../../../../01-users/personas/u25-care-coordinator.md) and
  [U29 Dispatcher](../../../../01-users/personas/u29-dispatcher.md), as planners (D517): their
  teams, the proposals waiting, the map beside.
- [U02 Manager](../../../../01-users/personas/u02-manager.md): the teams they manage; sees whether the automatic mode
  is on, and where it stopped.

## Purpose

Plan the day: people by day with the work assigned, the work requests waiting, the proposals to review, and the map
and routes beside.

## Entry points

HR and projects › Scheduling; the planner's workspace; the notification of a stop of the automatic mode; a work
request's
"Propose" (S-F16-14).

## Wireframe

The map half follows [C-17 Map](../../../../04-ux/design-system/components/c-17-map.md), for roles with the map right;
without it, the same half lists the addresses. The routes are the rounds of
[S-F9-27 Rounds](../11-capacity-rounds-and-partners/s-f09-27-rounds.md), ordered by the route optimiser
(BR-F9-22); the board does not compute its own.

```text
+------------------------------------------------------------------------------------------------+
| Scheduling  Tue 9 Dec  Team: Home care north v   Automatic mode: off      [Rounds >] [Settings] |
|------------------------------------------------------------------------------------------------|
| WAITING (18)                | PEOPLE         07   08   09   10   11   12   13   14   15   16    |
| ! To re-plan (3): Lea absent | Lea  (absent) ------------------------------------------------- |
| WR-2207 Bathing help        | Marc         [Roche][Blanc]   [Faure]         [Petit]           |
|   Mme Roche 08:00-09:00     | Sofia        [Dupuis]  [Garnier][Morel]  [Leroy]                |
|   [Propose]                 | Karim        [Bernard]      [Lambert][  proposed: Roche  ]      |
| WR-2214 Repair              |------------------------------------------------------------------|
|   M. Blanc 14:00-16:00      | [ map: today's routes by person, waiting work as hollow markers ]|
| Blocked (1)                 |                                                                  |
|   WR-2219: no carer free    | 14 rounds · 312 visits · 3 unplaced          [Publish rounds >]   |
+------------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F9-12 step 2, U25 | desktop | ![FL-F9-12 step 2, U25, light](../../images/12-schedule-customer-requests/u25-care-coordinator/2-scheduling-board-desktop-light.png) | ![FL-F9-12 step 2, U25, dark](../../images/12-schedule-customer-requests/u25-care-coordinator/2-scheduling-board-desktop-dark.png) |
| FL-F9-12 step 2, U25 | phone | ![FL-F9-12 step 2, U25, light](../../images/12-schedule-customer-requests/u25-care-coordinator/2-scheduling-board-phone-light.png) | ![FL-F9-12 step 2, U25, dark](../../images/12-schedule-customer-requests/u25-care-coordinator/2-scheduling-board-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f09-30-scheduling-board-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f09-30-scheduling-board-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f09-30-scheduling-board-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f09-30-scheduling-board-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f09-30-scheduling-board-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f09-30-scheduling-board-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f09-30-scheduling-board-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f09-30-scheduling-board-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Waiting | E-F16-12 in Ready, Proposed, Blocked | list by priority and window | no | yes |
| People | E-F9-01, E-F9-16 Shift, E-F9-09 Time-off request | rows by person | no | yes |
| Work assigned | E-F16-12 Scheduled, In progress | blocks on the time line | drag to another time or person, then a new proposal | yes |
| Rounds and routes | E-F9-26, E-T13-02 | map | no (on S-F9-27) | for work at a place |
| Automatic mode | E-F9-33 | off, on | on S-F9-32 | yes |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Propose | waiting item | planners | proposal opened (S-F9-31) |
| Propose for all | waiting header | planners | a proposal for each, reviewed one by one |
| Move | work block, by drag or keyboard | planners | a new proposal for the new time or person; an override if not the best |
| Publish rounds | footer | planners | opens S-F9-27 |
| Settings | header | the planners' manager, the administrator (D517) | opens S-F9-32 |

## States

- Normal: the day's people, work and waiting list, the map beside.
- Empty: nothing to plan that day: "No work request for this team".
- Loading: the time line greyed with "Computing" while proposals or routes compute.
- Error: the error message pattern (D122); assigning by hand stays possible, logged as an override.
- Read-only: past days; managers without the planner role.
- Offline: not available offline; the last loaded board stays readable with a banner.

Shown entities (VD-15): [E-F16-12 Work request](../../../f16-customer-support-agents/data/e-f16-12-work-request.md),
[E-F9-33 Automatic scheduling setting](../../data/e-f09-33-automatic-scheduling-setting.md),
[E-F9-28 Assignment proposal](../../data/e-f09-28-assignment-proposal.md),
[E-F9-16 Shift](../../data/e-f09-16-shift.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F16-12 Work request | Ready | In the waiting list; Propose | U25, U29 | `u25-care-coordinator/s-f09-30-scheduling-board-e-f16-12-work-request-ready-{desktop,phone}-{light,dark}.png`, `u29-dispatcher/s-f09-30-scheduling-board-e-f16-12-work-request-ready-{desktop,phone}-{light,dark}.png` |
| E-F16-12 Work request | Proposed | Hollow block on the proposed person's line; "Review" | U25, U29 | `u25-care-coordinator/s-f09-30-scheduling-board-e-f16-12-work-request-proposed-{desktop,phone}-{light,dark}.png`, `u29-dispatcher/s-f09-30-scheduling-board-e-f16-12-work-request-proposed-{desktop,phone}-{light,dark}.png` |
| E-F16-12 Work request | Blocked | In "Blocked" with the reason count; "Open" | U25, U29, U02 | `u25-care-coordinator/s-f09-30-scheduling-board-e-f16-12-work-request-blocked-{desktop,phone}-{light,dark}.png`, `u29-dispatcher/s-f09-30-scheduling-board-e-f16-12-work-request-blocked-{desktop,phone}-{light,dark}.png`, `u02-manager/s-f09-30-scheduling-board-e-f16-12-work-request-blocked-{desktop,phone}-{light,dark}.png` |
| E-F16-12 Work request | Scheduled | Solid block with the customer's name; "automatic" tag if the engine assigned it | U25, U29, U02 | `u25-care-coordinator/s-f09-30-scheduling-board-e-f16-12-work-request-scheduled-{desktop,phone}-{light,dark}.png`, `u29-dispatcher/s-f09-30-scheduling-board-e-f16-12-work-request-scheduled-{desktop,phone}-{light,dark}.png`, `u02-manager/s-f09-30-scheduling-board-e-f16-12-work-request-scheduled-{desktop,phone}-{light,dark}.png` |
| E-F16-12 Work request | In progress | Block outlined, check-in time | U25, U29, U02 | `u25-care-coordinator/s-f09-30-scheduling-board-e-f16-12-work-request-in-progress-{desktop,phone}-{light,dark}.png`, `u29-dispatcher/s-f09-30-scheduling-board-e-f16-12-work-request-in-progress-{desktop,phone}-{light,dark}.png`, `u02-manager/s-f09-30-scheduling-board-e-f16-12-work-request-in-progress-{desktop,phone}-{light,dark}.png` |
| E-F16-12 Work request | Done | Block greyed | U25, U29, U02 | `u25-care-coordinator/s-f09-30-scheduling-board-e-f16-12-work-request-done-{desktop,phone}-{light,dark}.png`, `u29-dispatcher/s-f09-30-scheduling-board-e-f16-12-work-request-done-{desktop,phone}-{light,dark}.png`, `u02-manager/s-f09-30-scheduling-board-e-f16-12-work-request-done-{desktop,phone}-{light,dark}.png` |
| E-F9-33 Automatic scheduling setting | Off | Header "Automatic mode: off" | U25, U29, U02 | `u25-care-coordinator/s-f09-30-scheduling-board-e-f09-33-automatic-scheduling-setting-off-{desktop,phone}-{light,dark}.png`, `u29-dispatcher/s-f09-30-scheduling-board-e-f09-33-automatic-scheduling-setting-off-{desktop,phone}-{light,dark}.png`, `u02-manager/s-f09-30-scheduling-board-e-f09-33-automatic-scheduling-setting-off-{desktop,phone}-{light,dark}.png` |
| E-F9-33 Automatic scheduling setting | On | Header "Automatic mode: on"; automatic blocks tagged | U29, U02 | `u29-dispatcher/s-f09-30-scheduling-board-e-f09-33-automatic-scheduling-setting-on-{desktop,phone}-{light,dark}.png`, `u02-manager/s-f09-30-scheduling-board-e-f09-33-automatic-scheduling-setting-on-{desktop,phone}-{light,dark}.png` |
| E-F9-28 Assignment proposal | Applied | Block tagged "automatic" | U29, U02 | `u29-dispatcher/s-f09-30-scheduling-board-e-f09-28-assignment-proposal-applied-{desktop,phone}-{light,dark}.png`, `u02-manager/s-f09-30-scheduling-board-e-f09-28-assignment-proposal-applied-{desktop,phone}-{light,dark}.png` |
| E-F9-28 Assignment proposal | Stopped | Red banner "stopped on WR-nnnn" with the problem; Review | U29, U02 | `u29-dispatcher/s-f09-30-scheduling-board-e-f09-28-assignment-proposal-stopped-{desktop,phone}-{light,dark}.png`, `u02-manager/s-f09-30-scheduling-board-e-f09-28-assignment-proposal-stopped-{desktop,phone}-{light,dark}.png` |
| E-F9-28 Assignment proposal | No candidate | In "Blocked" with the reasons | U25, U29, U02 | `u25-care-coordinator/s-f09-30-scheduling-board-e-f09-28-assignment-proposal-no-candidate-{desktop,phone}-{light,dark}.png`, `u29-dispatcher/s-f09-30-scheduling-board-e-f09-28-assignment-proposal-no-candidate-{desktop,phone}-{light,dark}.png`, `u02-manager/s-f09-30-scheduling-board-e-f09-28-assignment-proposal-no-candidate-{desktop,phone}-{light,dark}.png` |
| E-F9-28 Assignment proposal | Superseded | Not shown; a new proposal replaces it | U25, U29 | `u25-care-coordinator/s-f09-30-scheduling-board-e-f09-28-assignment-proposal-superseded-{desktop,phone}-{light,dark}.png`, `u29-dispatcher/s-f09-30-scheduling-board-e-f09-28-assignment-proposal-superseded-{desktop,phone}-{light,dark}.png` |
| E-F16-12 Work request | Cancelled | Badge "Cancelled"; final: read-only, no next state; the history shows how it got here | U25, U29 | `u25-care-coordinator/s-f09-30-scheduling-board-e-f16-12-work-request-cancelled-{desktop,phone}-{light,dark}.png`, `u29-dispatcher/s-f09-30-scheduling-board-e-f16-12-work-request-cancelled-{desktop,phone}-{light,dark}.png` |
| E-F9-28 Assignment proposal | Waiting | Badge "Waiting"; a new record starts here; next: Confirmed, Overridden or Superseded (UC-F9-33, BR-F9-34, UC-F9-35); fields editable within the role | U25, U29 | `u25-care-coordinator/s-f09-30-scheduling-board-e-f09-28-assignment-proposal-waiting-{desktop,phone}-{light,dark}.png`, `u29-dispatcher/s-f09-30-scheduling-board-e-f09-28-assignment-proposal-waiting-{desktop,phone}-{light,dark}.png` |
| E-F9-28 Assignment proposal | Overridden | Badge "Overridden"; next: Superseded (UC-F9-35); fields editable within the role | U25, U29 | `u25-care-coordinator/s-f09-30-scheduling-board-e-f09-28-assignment-proposal-overridden-{desktop,phone}-{light,dark}.png`, `u29-dispatcher/s-f09-30-scheduling-board-e-f09-28-assignment-proposal-overridden-{desktop,phone}-{light,dark}.png` |
| E-F9-16 Shift | Draft | Badge "Draft"; a new record starts here; next: Published (UC-F9-15); fields editable within the role | U02, U25, U29 | `u02-manager/s-f09-30-scheduling-board-e-f09-16-shift-draft-{desktop,phone}-{light,dark}.png`, `u25-care-coordinator/s-f09-30-scheduling-board-e-f09-16-shift-draft-{desktop,phone}-{light,dark}.png`, `u29-dispatcher/s-f09-30-scheduling-board-e-f09-16-shift-draft-{desktop,phone}-{light,dark}.png` |
| E-F9-16 Shift | Published | Badge "Published"; final: read-only, no next state; the history shows how it got here | U02, U25, U29 | `u02-manager/s-f09-30-scheduling-board-e-f09-16-shift-published-{desktop,phone}-{light,dark}.png`, `u25-care-coordinator/s-f09-30-scheduling-board-e-f09-16-shift-published-{desktop,phone}-{light,dark}.png`, `u29-dispatcher/s-f09-30-scheduling-board-e-f09-16-shift-published-{desktop,phone}-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop: board and map side by side. Tablet: the map below. Phone: one person's day at a time, swiped; the waiting list
in a drawer; the map on a tab.

## Accessibility

Moving a block works with the keyboard (select, then choose a person and time); every block is also a row in a list
view of the day; colours of states are also words; the automatic-mode banner is announced.

## Components

- [C-17 Map](../../../../04-ux/design-system/components/c-17-map.md)
- [C-14 Timeline](../../../../04-ux/design-system/components/c-14-timeline.md)
- [C-04 Card](../../../../04-ux/design-system/components/c-04-card.md)
- [C-01 Button](../../../../04-ux/design-system/components/c-01-button.md)

## Shown in

- [FL-F9-12 Schedule customer requests](../../flows/fl-f09-12-schedule-customer-requests.md)

## Open questions

None.

---

⬅️ [S-F9-29 Subcontractors](../11-capacity-rounds-and-partners/s-f09-29-subcontractors.md) · ⬆️ [Up](README.md) ·
➡️ [S-F9-31 Proposal review](s-f09-31-proposal-review.md)
