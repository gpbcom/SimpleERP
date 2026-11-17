🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
👥 [F9 HR and projects](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F9-12 Schedule customer requests](README.md) › 🖥️ S-F9-33 Planning map

# 🖥️ S-F9-33 Planning map

**Status:** 🔄 draft (GH-2 step S4b, from VD-18 to VD-22 / D501 to D504)

## Personas

- [U02 Manager](../../../../01-users/personas/u02-manager.md): the teams they manage.
- [U25 Care coordinator](../../../../01-users/personas/u25-care-coordinator.md) and
  [U29 Dispatcher](../../../../01-users/personas/u29-dispatcher.md), as planners (D517): their teams.

Only roles with the map right open it
[BR-F1-32](../../../f01-administration/business-rules/br-f01-32-map-right-for-planners-and-managers.md).

## Purpose

See the day's work, places, routes and shared positions on one map.

## Entry points

HR and projects › Scheduling › Map; the map half of the scheduling board (S-F9-30); the map layout of the work requests
(S-F16-14).

## Wireframe

Follows [C-17 Map](../../../../04-ux/design-system/components/c-17-map.md): markers by state, clusters, team areas,
routes, a list beside the map that mirrors every marker.

```text
+------------------------------------------------------------------------------------------------+
| Planning map   Tue 9 Dec   Team: Home care north v   Layers: [x] Work [x] Routes [x] Check-ins  |
|                                                       [x] Live positions (team option on)       |
|------------------------------------------------------------------------------------------------|
| [ map ]                                                          | LIST (42)                    |
|   o  ready work request        * scheduled                       | WR-2207 Roche  08:00 Lea  *  |
|   x  blocked                   - route of a round                | WR-2214 Blanc  14:00 -    o  |
|   [] check-in position         > live position (shared)          | Lea: paused at 12:00         |
|   ...                                                            | Not on the map (1): WR-2230 |
|------------------------------------------------------------------------------------------------|
| Selected: Lea Martin · round 9 visits · last shared position 08:12 · next: Mme Roche 08:20     |
|                                                         [Open round] [Open person]            |
+------------------------------------------------------------------------------------------------+
Without the map right: the LIST only, with addresses; no map, no positions.
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F9-12 step 8, U02 | desktop | ![FL-F9-12 step 8, U02, light](../../images/12-schedule-customer-requests/u02-manager/8-planning-map-desktop-light.png) | ![FL-F9-12 step 8, U02, dark](../../images/12-schedule-customer-requests/u02-manager/8-planning-map-desktop-dark.png) |
| FL-F9-12 step 8, U02 | phone | ![FL-F9-12 step 8, U02, light](../../images/12-schedule-customer-requests/u02-manager/8-planning-map-phone-light.png) | ![FL-F9-12 step 8, U02, dark](../../images/12-schedule-customer-requests/u02-manager/8-planning-map-phone-dark.png) |
| Error E4, U02 | desktop | ![Error E4, U02, light](../../images/12-schedule-customer-requests/u02-manager/e4-no-map-right-desktop-light.png) | ![Error E4, U02, dark](../../images/12-schedule-customer-requests/u02-manager/e4-no-map-right-desktop-dark.png) |
| Error E4, U02 | phone | ![Error E4, U02, light](../../images/12-schedule-customer-requests/u02-manager/e4-no-map-right-phone-light.png) | ![Error E4, U02, dark](../../images/12-schedule-customer-requests/u02-manager/e4-no-map-right-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f09-33-planning-map-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f09-33-planning-map-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f09-33-planning-map-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f09-33-planning-map-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f09-33-planning-map-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f09-33-planning-map-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f09-33-planning-map-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f09-33-planning-map-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Work | E-F16-12 place, window, state | marker and row | no | yes |
| Routes | E-F9-26, E-T13-02 | line per round | no (on S-F9-27) | for work at a place |
| Check-in positions | E-F9-10 Attendance (BR-F9-06) | marker | no | where the team setting is on |
| Live positions | E-F9-32 | marker with its time | no | where the team option is on, in working hours |
| Layers | E-T13-03 Map layer | ticks | yes | no |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Select a marker or a row | map, list | roles with the map right | side panel with the record |
| Open round, open person, open work request | side panel | as each record's rights | the record's own page |
| Propose | side panel of a ready work request | planners | proposal (S-F9-31) |
| Filter | header, layers | roles with the map right | map and list follow |

## States

- Normal: the day's markers, routes and positions the user may see.
- Empty: nothing on that day: "No work for this team on Tuesday".
- Loading: tiles grey with "Loading"; the list shows first.
- Error: the tiles fail: the list stays, with "Map not available" (D122).
- Read-only: always; changes are made on the board or the rounds.
- Offline: not available offline.

Shown entities (VD-15): [E-F16-12 Work request](../../../f16-customer-support-agents/data/e-f16-12-work-request.md),
[E-F9-26 Round](../../data/e-f09-26-round.md), [E-F9-32 Live position](../../data/e-f09-32-live-position.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F16-12 Work request | Ready | Hollow marker; Propose in the side panel | U02, U25, U29 | `u02-manager/s-f09-33-planning-map-e-f16-12-work-request-ready-{desktop,phone}-{light,dark}.png`, `u25-care-coordinator/s-f09-33-planning-map-e-f16-12-work-request-ready-{desktop,phone}-{light,dark}.png`, `u29-dispatcher/s-f09-33-planning-map-e-f16-12-work-request-ready-{desktop,phone}-{light,dark}.png` |
| E-F16-12 Work request | Blocked | Cross marker; the reason count | U02, U25, U29 | `u02-manager/s-f09-33-planning-map-e-f16-12-work-request-blocked-{desktop,phone}-{light,dark}.png`, `u25-care-coordinator/s-f09-33-planning-map-e-f16-12-work-request-blocked-{desktop,phone}-{light,dark}.png`, `u29-dispatcher/s-f09-33-planning-map-e-f16-12-work-request-blocked-{desktop,phone}-{light,dark}.png` |
| E-F16-12 Work request | Scheduled | Solid marker on its round's route | U02, U25, U29 | `u02-manager/s-f09-33-planning-map-e-f16-12-work-request-scheduled-{desktop,phone}-{light,dark}.png`, `u25-care-coordinator/s-f09-33-planning-map-e-f16-12-work-request-scheduled-{desktop,phone}-{light,dark}.png`, `u29-dispatcher/s-f09-33-planning-map-e-f16-12-work-request-scheduled-{desktop,phone}-{light,dark}.png` |
| E-F16-12 Work request | In progress | Marker outlined with the check-in time | U02, U25, U29 | `u02-manager/s-f09-33-planning-map-e-f16-12-work-request-in-progress-{desktop,phone}-{light,dark}.png`, `u25-care-coordinator/s-f09-33-planning-map-e-f16-12-work-request-in-progress-{desktop,phone}-{light,dark}.png`, `u29-dispatcher/s-f09-33-planning-map-e-f16-12-work-request-in-progress-{desktop,phone}-{light,dark}.png` |
| E-F16-12 Work request | Done | Marker greyed | U02, U25, U29 | `u02-manager/s-f09-33-planning-map-e-f16-12-work-request-done-{desktop,phone}-{light,dark}.png`, `u25-care-coordinator/s-f09-33-planning-map-e-f16-12-work-request-done-{desktop,phone}-{light,dark}.png`, `u29-dispatcher/s-f09-33-planning-map-e-f16-12-work-request-done-{desktop,phone}-{light,dark}.png` |
| E-F9-26 Round | Published | Route drawn | U02, U25, U29 | `u02-manager/s-f09-33-planning-map-e-f09-26-round-published-{desktop,phone}-{light,dark}.png`, `u25-care-coordinator/s-f09-33-planning-map-e-f09-26-round-published-{desktop,phone}-{light,dark}.png`, `u29-dispatcher/s-f09-33-planning-map-e-f09-26-round-published-{desktop,phone}-{light,dark}.png` |
| E-F9-26 Round | Draft or changed | Route dashed, "not published" | U25, U29 | `u25-care-coordinator/s-f09-33-planning-map-e-f09-26-round-draft-or-changed-{desktop,phone}-{light,dark}.png`, `u29-dispatcher/s-f09-33-planning-map-e-f09-26-round-draft-or-changed-{desktop,phone}-{light,dark}.png` |
| E-F9-32 Live position | Sharing | Arrow marker with its time | U02, U25, U29 | `u02-manager/s-f09-33-planning-map-e-f09-32-live-position-sharing-{desktop,phone}-{light,dark}.png`, `u25-care-coordinator/s-f09-33-planning-map-e-f09-32-live-position-sharing-{desktop,phone}-{light,dark}.png`, `u29-dispatcher/s-f09-33-planning-map-e-f09-32-live-position-sharing-{desktop,phone}-{light,dark}.png` |
| E-F9-32 Live position | Paused | Last check-in marker, "position paused" | U02, U25, U29 | `u02-manager/s-f09-33-planning-map-e-f09-32-live-position-paused-{desktop,phone}-{light,dark}.png`, `u25-care-coordinator/s-f09-33-planning-map-e-f09-32-live-position-paused-{desktop,phone}-{light,dark}.png`, `u29-dispatcher/s-f09-33-planning-map-e-f09-32-live-position-paused-{desktop,phone}-{light,dark}.png` |
| E-F9-32 Live position | Off | No live marker; check-ins only | U02, U25, U29 | `u02-manager/s-f09-33-planning-map-e-f09-32-live-position-off-{desktop,phone}-{light,dark}.png`, `u25-care-coordinator/s-f09-33-planning-map-e-f09-32-live-position-off-{desktop,phone}-{light,dark}.png`, `u29-dispatcher/s-f09-33-planning-map-e-f09-32-live-position-off-{desktop,phone}-{light,dark}.png` |
| E-F9-26 Round | Draft | Badge "Draft"; a new record starts here; next: Published (UC-F9-30); fields editable within the role | U02 | `u02-manager/s-f09-33-planning-map-e-f09-26-round-draft-{desktop,phone}-{light,dark}.png` |
| E-F9-26 Round | Changed | Badge "Changed"; final: read-only, no next state; the history shows how it got here | U02 | `u02-manager/s-f09-33-planning-map-e-f09-26-round-changed-{desktop,phone}-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Phone: the map full screen with the list as a bottom sheet; layers in a drawer. Field workers have no map; an address on
their phone opens their own navigation app (D517).

## Accessibility

Every marker is a row of the list, reachable by keyboard; markers differ by shape, not only colour; the map has a text
summary ("42 work requests, 14 routes, 6 live positions, 1 not on the map").

## Components

- [C-17 Map](../../../../04-ux/design-system/components/c-17-map.md)
- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-04 Card](../../../../04-ux/design-system/components/c-04-card.md)

## Shown in

- [FL-F9-12 Schedule customer requests](../../flows/fl-f09-12-schedule-customer-requests.md)

## Open questions

None.

---

⬅️ [S-F9-32 Automatic scheduling settings](s-f09-32-automatic-scheduling-settings.md) · ⬆️ [Up](README.md) ·
➡️ [S-F9-34 My position](s-f09-34-my-position.md)
