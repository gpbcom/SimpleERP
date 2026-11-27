🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
👥 [F9 HR and projects](../../README.md) › 🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-F9-15](README.md) ›
🖥️ S-F9-41 Headcount plan

# 🖥️ S-F9-41 Headcount plan

**Status:** ✅ specified

## Personas

- [U06 Human resources](../../../../01-users/personas/u06-hr.md): plans positions and follows the budget.
- [U13 Owner](../../../../01-users/personas/u13-owner.md): approves and freezes.

## Purpose

Plan positions against the budget, see headcount and cost by month and open jobs from positions.

## Entry points

HR and projects › Headcount plan; Recruitment › a job offer; the AI assistant
([BR-F3-34](../../../f03-assistant/business-rules/br-f03-34-every-capability-is-reachable-from-the-assistant.md)).

## Wireframe

```text
+---------------------------------------------------------------------------------------------+
| Headcount plan 2027                         Budget 1 480 000   Planned 1 534 000   [Add a position] |
| ------------------------------------------------------------------------------------------- |
| DEPARTMENT   POSITION            FTE   COST/YEAR   START     STATE                          |
| Sales        Sales manager        1    70 000      2027-01   Filled      Julien R.          |
| Sales        Account executive    1    52 000      2027-04   Approved    [Open an offer]    |
| Works        Site manager         1    62 000      2027-03   Open        Offer 14           |
| Works        Planner              1    48 000      2027-09   Planned     [Approve] [Freeze] |
| Sales is 4% over budget by 2027-12.  Frozen: 0   Open: 1   Planned: 1                       |
+---------------------------------------------------------------------------------------------+
```

Example images of the empty, loading, read-only and offline states, drawn in the image round
([D120](../../../../06-decisions/ux/d120-png-mockups.md)): `s-f09-41-headcount-plan-empty-desktop-{light,dark}.png`,
`s-f09-41-headcount-plan-loading-desktop-{light,dark}.png`, `s-f09-41-headcount-plan-offline-desktop-{light,dark}.png`,
`s-f09-41-headcount-plan-read-only-desktop-{light,dark}.png`.

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F9-15 step 2, U06 | desktop | ![FL-F9-15 step 2, U06, light](../../images/15-work-location-headcount-and-learning/u06-hr/2-headcount-plan-desktop-light.png) | ![FL-F9-15 step 2, U06, dark](../../images/15-work-location-headcount-and-learning/u06-hr/2-headcount-plan-desktop-dark.png) |
| FL-F9-15 step 2, U06 | desktop | ![FL-F9-15 step 2, U06, light](../../images/15-work-location-headcount-and-learning/u06-hr/2-headcount-plan-desktop-light.png) | ![FL-F9-15 step 2, U06, dark](../../images/15-work-location-headcount-and-learning/u06-hr/2-headcount-plan-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f09-41-headcount-plan-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f09-41-headcount-plan-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f09-41-headcount-plan-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f09-41-headcount-plan-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f09-41-headcount-plan-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f09-41-headcount-plan-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f09-41-headcount-plan-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f09-41-headcount-plan-offline-desktop-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Department and title | E-F9-49 department and title | text | yes | yes |
| Cost and FTE | E-F9-49 yearly cost and FTE | money and number | yes | yes |
| Start | E-F9-49 start month | month | yes | yes |
| Budget gap | E-F8-16 and E-F9-49 | money and percent | no | yes |
| State | E-F9-49 state | badge | by action | yes |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Add a position | header | HR | a Planned position (UC-F9-44) |
| Approve | row | the owner | the position is Approved |
| Freeze | row | the owner | the position cannot be opened |
| Open an offer | row | HR, the manager | a job offer is created and the position is Open |
| Cancel | row | HR, the owner | the position is Cancelled |

## States

- Normal: the positions by department with their cost and state, and the comparison with the budget.
- Empty: No position planned for the year: a hint to add the first or copy last year's.
- Loading: The positions as placeholders, then the budget comparison.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); an offer
  without a free headcount says so
  ([BR-F9-43](../../business-rules/br-f09-43-a-requisition-needs-a-budgeted-position.md)).
- Read-only: a closed year, or a role that may only read: shown, with no action.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-F9-49 Position](../../data/e-f09-49-position.md),
[E-F9-03 Department](../../data/e-f09-03-department.md), [E-F9-06 Job position](../../data/e-f09-06-job-position.md),
[E-F9-01 Employee record](../../data/e-f09-01-employee-record.md),
[E-F8-16 Budget plan](../../../f08-accounting/data/e-f08-16-budget-plan.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F9-49 Position | Planned | Badge "Planned"; a new record starts here; next: Approved or Cancelled (UC-F9-44); fields editable within the role | U06, U13 | `u06-hr/s-f09-41-headcount-plan-e-f09-49-position-planned-desktop-{light,dark}.png`; `u13-owner/s-f09-41-headcount-plan-e-f09-49-position-planned-{desktop,phone}-{light,dark}.png` |
| E-F9-49 Position | Approved | Badge "Approved"; next: Open or Frozen (BR-F9-43, UC-F9-44); fields editable within the role | U06, U13 | `u06-hr/s-f09-41-headcount-plan-e-f09-49-position-approved-desktop-{light,dark}.png`; `u13-owner/s-f09-41-headcount-plan-e-f09-49-position-approved-{desktop,phone}-{light,dark}.png` |
| E-F9-49 Position | Cancelled | Badge "Cancelled"; final state, read-only | U06, U13 | `u06-hr/s-f09-41-headcount-plan-e-f09-49-position-cancelled-desktop-{light,dark}.png`; `u13-owner/s-f09-41-headcount-plan-e-f09-49-position-cancelled-{desktop,phone}-{light,dark}.png` |
| E-F9-49 Position | Open | Badge "Open"; next: Filled or Approved (UC-F9-44); fields editable within the role | U06, U13 | `u06-hr/s-f09-41-headcount-plan-e-f09-49-position-open-desktop-{light,dark}.png`; `u13-owner/s-f09-41-headcount-plan-e-f09-49-position-open-{desktop,phone}-{light,dark}.png` |
| E-F9-49 Position | Filled | Badge "Filled"; next: Approved (UC-F9-44); fields editable within the role | U06, U13 | `u06-hr/s-f09-41-headcount-plan-e-f09-49-position-filled-desktop-{light,dark}.png`; `u13-owner/s-f09-41-headcount-plan-e-f09-49-position-filled-{desktop,phone}-{light,dark}.png` |
| E-F9-49 Position | Frozen | Badge "Frozen"; next: Approved (UC-F9-44); fields editable within the role | U06, U13 | `u06-hr/s-f09-41-headcount-plan-e-f09-49-position-frozen-desktop-{light,dark}.png`; `u13-owner/s-f09-41-headcount-plan-e-f09-49-position-frozen-{desktop,phone}-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per persona, device and theme; the
image round draws them. Rows are derived from each entity's Lifecycle: the badge is the state's name, the next states
are its transitions, and a final state is read-only.

## Responsive behaviour

Desktop only; on a phone, the owner sees the positions to approve as a list.

## Accessibility

States are words; the budget gap is read as a sentence; keyboard: next row, approve, freeze.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-16 KPI strip](../../../../04-ux/design-system/components/c-16-kpi-strip.md)
- [C-14 Timeline](../../../../04-ux/design-system/components/c-14-timeline.md)
- [C-01 Button](../../../../04-ux/design-system/components/c-01-button.md)

## Shown in

- [FL-F9-15 Work location, headcount, careers and learning](../../flows/fl-f09-15-work-location-headcount-and-learning.md)

## Open questions

None.

---

⬅️ [S-F9-40 Work location](s-f09-40-work-location.md) · ⬆️ [Up](README.md) ·
➡️ [S-F9-42 Careers and succession](s-f09-42-careers-and-succession.md)
