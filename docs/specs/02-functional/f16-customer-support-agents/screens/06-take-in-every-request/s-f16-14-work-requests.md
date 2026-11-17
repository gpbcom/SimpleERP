🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🎧 [F16 Customer support agents](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F16-06 Take in every request](README.md) › 🖥️ S-F16-14 Work requests

# 🖥️ S-F16-14 Work requests

**Status:** 🔄 draft (GH-2 step S4b, from VD-18 to VD-20, VD-30, VD-31 / D501, D502, D512, D513)

## Personas

- [U29 Dispatcher](../../../../01-users/personas/u29-dispatcher.md) and
  [U25 Care coordinator](../../../../01-users/personas/u25-care-coordinator.md), as planners (D517):
  the work requests of their teams, list and map layouts, "Propose".
- [U02 Manager](../../../../01-users/personas/u02-manager.md): the same for the teams they manage, with the KPI strip
  and the chart by area.
- [U16 Office worker](../../../../01-users/personas/u16-office-worker.md): the drafts to confirm, list layout only (no
  map right), the source beside each draft.

## Purpose

See every work request, whatever its channel, with its state, place and window; confirm drafts; send ready ones to
scheduling.

## Entry points

Customer support › Work requests; HR and projects › Scheduling › Work requests; the planner's and the office worker's
workspaces; global search; the AI assistant; the notification "drafts to confirm".

## Wireframe

The [aggregated list view](../../../../04-ux/design-system/patterns/aggregated-list-view.md) with a map layout for
roles with the map right ([C-17 Map](../../../../04-ux/design-system/components/c-17-map.md)).

```text
+------------------------------------------------------------------------------------------------+
| Work requests                         Customer support › Work requests      [+ New work request] |
|------------------------------------------------------------------------------------------------|
| [64 open] [11 to confirm] [5 blocked] [9 due today]                [ chart: count by state ]   |
|------------------------------------------------------------------------------------------------|
| FACETS          | [View: Ready for my teams v] [* Describe what you want to see...] [Filter]    |
| State           | [Chart] [Export] [Ask about this list]          Layout: (List) ( Map )          |
| [ ] To confirm 11| (State: Ready x) (Area: Lyon north x)                        23 of 64 results |
| [x] Ready     23| [ ] REQUEST  TYPE           CUSTOMER    PLACE          WINDOW         STATE     |
| [ ] Blocked    5|  [ ] WR-2207 Bathing help   Mme Roche   Villeurbanne   Tue 08:00-09:00 (Ready) >|
| Request type    |  [ ] WR-2210 Delivery       Durand SA   Lyon 6e        Tue 10:00-12:00 (Ready) >|
| Channel         |  [ ] WR-2214 Repair         M. Blanc    Caluire        Tue 14:00-16:00 (Ready) >|
| Area            |  ...                                       2 selected · Propose · Assign · Tag  |
| Related records | Counts, totals, facets and the chart use only the records you may see.        |
+------------------------------------------------------------------------------------------------+

Map layout (map right only):
+------------------------------------------------------------------------------------------------+
| FACETS          | [ map: 23 markers by state, clusters, team areas ]   | WR-2207 Bathing help    |
| (as above)      |                                                     | Mme Roche, Villeurbanne |
|                 |   Not on the map: 1 (address to confirm)            | Tue 08:00-09:00 [Propose]|
+------------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F9-12 step 1, U29 | desktop | ![FL-F9-12 step 1, U29, light](../../../f09-hr-and-projects/images/12-schedule-customer-requests/u29-dispatcher/1-work-requests-desktop-light.png) | ![FL-F9-12 step 1, U29, dark](../../../f09-hr-and-projects/images/12-schedule-customer-requests/u29-dispatcher/1-work-requests-desktop-dark.png) |
| FL-F9-12 step 1, U29 | phone | ![FL-F9-12 step 1, U29, light](../../../f09-hr-and-projects/images/12-schedule-customer-requests/u29-dispatcher/1-work-requests-phone-light.png) | ![FL-F9-12 step 1, U29, dark](../../../f09-hr-and-projects/images/12-schedule-customer-requests/u29-dispatcher/1-work-requests-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f16-14-work-requests-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f16-14-work-requests-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f16-14-work-requests-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f16-14-work-requests-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f16-14-work-requests-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f16-14-work-requests-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f16-14-work-requests-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f16-14-work-requests-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Request | E-F16-12 number | WR-nnnn | no | yes |
| Type | E-F16-12 request type (E-F2-25) | name | inline, while to confirm | yes |
| Customer | E-F16-12 customer | name | no | yes |
| Place | E-F16-12 place (E-T13-01) | town, or address on the record page | while to confirm | for work at a place |
| Window | E-F16-12 time window | day and times | inline, while to confirm or ready | yes |
| State | E-F16-12 state | word and colour | by actions only | yes |
| Channel | E-F16-12 channel | portal, email, phone, chat, order, contract, care plan, API | no | yes |
| Priority | E-F16-12 priority | normal, urgent | inline | yes |

Facets: state, request type, channel, area, team, priority. Related-record filters: "customer has an open order", "work
requests of a care plan". KPI strip: open, to confirm, blocked, due today. Default chart: count by state.

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Confirm | row, record page | office workers, planners | draft becomes ready |
| Propose | row, bulk bar, map side panel | planners | proposal opened on S-F9-31 |
| Assign | bulk bar | planners | proposal for each, reviewed one by one |
| Cancel | record page | office workers, planners | cancelled with a reason, customer told |
| Layout: Map | toolbar | roles with the map right | map layout of the same rows |
| Export | toolbar | as the view (VD-06) | CSV or XLSX of visible rows, audited |
| Open | row | everyone who sees the row | the work request's own page |

## States

- Normal: the work requests the user may see, list or map.
- Empty: "No work request yet": a link to the request types and the channels.
- Loading: skeleton rows; on the map, the tiles grey with "Loading".
- Error: the error message pattern (D122); the list stays if only the map fails.
- Read-only: done and cancelled work requests.
- Offline: the list last loaded stays readable; actions come back with the connection.

Shown entities (VD-15): [E-F16-12 Work request](../../data/e-f16-12-work-request.md),
[E-F2-25 Request type](../../../f02-no-code-configuration/data/e-f02-25-request-type.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F16-12 Work request | Drafted | Grey badge "Drafting"; no action | U16 | `u16-office-worker/s-f16-14-work-requests-e-f16-12-work-request-drafted-{desktop,phone}-{light,dark}.png` |
| E-F16-12 Work request | To confirm | Amber badge; the source beside the draft; fields unsure underlined; Confirm | U16 | `u16-office-worker/s-f16-14-work-requests-e-f16-12-work-request-to-confirm-{desktop,phone}-{light,dark}.png` |
| E-F16-12 Work request | Ready | Blue badge; Propose; on the map as a marker | U29, U25, U02 | `u29-dispatcher/s-f16-14-work-requests-e-f16-12-work-request-ready-{desktop,phone}-{light,dark}.png`, `u25-care-coordinator/s-f16-14-work-requests-e-f16-12-work-request-ready-{desktop,phone}-{light,dark}.png`, `u02-manager/s-f16-14-work-requests-e-f16-12-work-request-ready-{desktop,phone}-{light,dark}.png` |
| E-F16-12 Work request | Proposed | Badge "Proposed"; Open proposal | U29, U25 | `u29-dispatcher/s-f16-14-work-requests-e-f16-12-work-request-proposed-{desktop,phone}-{light,dark}.png`, `u25-care-coordinator/s-f16-14-work-requests-e-f16-12-work-request-proposed-{desktop,phone}-{light,dark}.png` |
| E-F16-12 Work request | Blocked | Red badge with the reason count; Open proposal | U29, U25, U02 | `u29-dispatcher/s-f16-14-work-requests-e-f16-12-work-request-blocked-{desktop,phone}-{light,dark}.png`, `u25-care-coordinator/s-f16-14-work-requests-e-f16-12-work-request-blocked-{desktop,phone}-{light,dark}.png`, `u02-manager/s-f16-14-work-requests-e-f16-12-work-request-blocked-{desktop,phone}-{light,dark}.png` |
| E-F16-12 Work request | Scheduled | Green badge with the person's first name and time | U29, U25, U02 | `u29-dispatcher/s-f16-14-work-requests-e-f16-12-work-request-scheduled-{desktop,phone}-{light,dark}.png`, `u25-care-coordinator/s-f16-14-work-requests-e-f16-12-work-request-scheduled-{desktop,phone}-{light,dark}.png`, `u02-manager/s-f16-14-work-requests-e-f16-12-work-request-scheduled-{desktop,phone}-{light,dark}.png` |
| E-F16-12 Work request | In progress | Badge "In progress" from check-in | U29, U25, U02 | `u29-dispatcher/s-f16-14-work-requests-e-f16-12-work-request-in-progress-{desktop,phone}-{light,dark}.png`, `u25-care-coordinator/s-f16-14-work-requests-e-f16-12-work-request-in-progress-{desktop,phone}-{light,dark}.png`, `u02-manager/s-f16-14-work-requests-e-f16-12-work-request-in-progress-{desktop,phone}-{light,dark}.png` |
| E-F16-12 Work request | Done | Read-only, check-out time | U29, U25, U02 | `u29-dispatcher/s-f16-14-work-requests-e-f16-12-work-request-done-{desktop,phone}-{light,dark}.png`, `u25-care-coordinator/s-f16-14-work-requests-e-f16-12-work-request-done-{desktop,phone}-{light,dark}.png`, `u02-manager/s-f16-14-work-requests-e-f16-12-work-request-done-{desktop,phone}-{light,dark}.png` |
| E-F16-12 Work request | Cancelled | Read-only, struck through, the reason | U16, U29, U25, U02 | `u16-office-worker/s-f16-14-work-requests-e-f16-12-work-request-cancelled-{desktop,phone}-{light,dark}.png`, `u29-dispatcher/s-f16-14-work-requests-e-f16-12-work-request-cancelled-{desktop,phone}-{light,dark}.png`, `u25-care-coordinator/s-f16-14-work-requests-e-f16-12-work-request-cancelled-{desktop,phone}-{light,dark}.png`, `u02-manager/s-f16-14-work-requests-e-f16-12-work-request-cancelled-{desktop,phone}-{light,dark}.png` |
| E-F2-25 Request type | Published | Badge "Published"; next: Draft or Retired (UC-F2-30); fields editable within the role | U16, U29 | `u16-office-worker/s-f16-14-work-requests-e-f02-25-request-type-published-{desktop,phone}-{light,dark}.png`, `u29-dispatcher/s-f16-14-work-requests-e-f02-25-request-type-published-{desktop,phone}-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Phone: the table scrolls sideways, facets in a drawer, the KPI strip kept (VD-08); the map layout fills the screen
with the list as a bottom sheet.

## Accessibility

Every marker is also a row of the list; the layout switch is a labelled control; states are words, not only colours;
the map has a text summary ("23 work requests, 1 not on the map").

## Components

- [Aggregated list view](../../../../04-ux/design-system/patterns/aggregated-list-view.md)
- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-15 Facet panel](../../../../04-ux/design-system/components/c-15-facet-panel.md)
- [C-16 KPI strip](../../../../04-ux/design-system/components/c-16-kpi-strip.md)
- [C-17 Map](../../../../04-ux/design-system/components/c-17-map.md)
- [C-09 Chart](../../../../04-ux/design-system/components/c-09-chart.md)

## Shown in

- [FL-F16-06 Take in every request](../../flows/fl-f16-06-take-in-every-request.md)
- [FL-F9-12 Schedule customer requests](../../../f09-hr-and-projects/flows/fl-f09-12-schedule-customer-requests.md)

## Open questions

None.

---

⬅️ [S-F16-13 Fraud signals](../03-review-and-monitor/s-f16-13-fraud-signals.md) · ⬆️ [Up](README.md) ·
➡️ [S-F16-15 Arrival of your visit](s-f16-15-arrival-of-your-visit.md)
