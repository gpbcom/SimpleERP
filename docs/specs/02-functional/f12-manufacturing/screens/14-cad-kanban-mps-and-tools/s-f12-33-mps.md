🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🏭 [F12 Manufacturing (plugin)](../../README.md) › 🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-F12-14](README.md) ›
🖥️ S-F12-33 MPS

# 🖥️ S-F12-33 MPS

**Status:** ✅ specified

## Personas

- [U21 Production planner](../../../../01-users/personas/u21-production-planner.md): builds, firms and releases the
  schedule, on a desktop.

## Purpose

Plan each product's production by week against capacity and release it.

## Entry points

Manufacturing › Master production schedule; the weekly planning meeting view.

## Wireframe

```text
+---------------------------------------------------------------------------------------------+
| MPS                     Kettle K2                  Horizon: weeks 47 to 58         [Propose] [Release] |
| ------------------------------------------------------------------------------------------- |
| WEEK    FORECAST   FIRM   PLANNED   PROMISE   LOAD / CAPACITY    STATE                      |
| W47     600        560    560       0         96 / 100           Released (frozen)          |
| W48     600        420    500       80        94 / 100           Firm                       |
| W49     650        300    550       250       112 / 100          Draft   12 hours over  [Note] |
| W50     650        120    500       380       88 / 100           Draft                      |
| Weeks over capacity: 1   Frozen until W47   Release fence: W48                              |
+---------------------------------------------------------------------------------------------+
```

Example images of the empty, loading, read-only and offline states, drawn in the image round
([D120](../../../../06-decisions/ux/d120-png-mockups.md)): `s-f12-33-mps-empty-desktop-{light,dark}.png`,
`s-f12-33-mps-loading-desktop-{light,dark}.png`, `s-f12-33-mps-offline-desktop-{light,dark}.png`,
`s-f12-33-mps-read-only-desktop-{light,dark}.png`.

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F12-14 step 3, U21 | desktop | ![FL-F12-14 step 3, U21, light](../../images/14-cad-kanban-mps-and-tools/u21-production-planner/3-mps-desktop-light.png) | ![FL-F12-14 step 3, U21, dark](../../images/14-cad-kanban-mps-and-tools/u21-production-planner/3-mps-desktop-dark.png) |
| FL-F12-14 step 3, U21 | desktop | ![FL-F12-14 step 3, U21, light](../../images/14-cad-kanban-mps-and-tools/u21-production-planner/3-mps-desktop-light.png) | ![FL-F12-14 step 3, U21, dark](../../images/14-cad-kanban-mps-and-tools/u21-production-planner/3-mps-desktop-dark.png) |
| FL-F12-14 step 3, U21 | phone | ![FL-F12-14 step 3, U21, light](../../images/14-cad-kanban-mps-and-tools/u21-production-planner/3-mps-phone-light.png) | ![FL-F12-14 step 3, U21, dark](../../images/14-cad-kanban-mps-and-tools/u21-production-planner/3-mps-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f12-33-mps-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f12-33-mps-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f12-33-mps-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f12-33-mps-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f12-33-mps-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f12-33-mps-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f12-33-mps-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f12-33-mps-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Week | E-F12-32 week | week | no | yes |
| Forecast and firm | E-F12-32 forecast, firm orders | numbers | forecast | yes |
| Planned | E-F12-32 planned production | number | yes | yes |
| Promise | E-F12-32 available to promise | number | no | yes |
| Load and capacity | E-F12-32 load, capacity plan | hours | no | yes |
| State | E-F12-32 state | badge | by action | yes |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Propose | header | the planner | draft lines from the plan lines (UC-F12-34) |
| Firm | row | the planner | the line is firm, within capacity or with a note |
| Release | header | the planner | production orders are created for the firm lines |
| Reopen | row | the planner | a firm line returns to Draft |
| Add a note | row | the planner | the over-capacity note is saved |

## States

- Normal: the weeks of the horizon with forecast, firm orders, planned quantity, promise, load against capacity and
  state.
- Empty: No line for this horizon: a hint to propose the lines from the plan.
- Loading: The weeks as placeholders, then the loads.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); firming a week
  over capacity says so with the hours missing.
- Read-only: a closed period or a frozen week: shown, with no action but a reason-backed change.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-F12-32 MPS line](../../data/e-f12-32-mps-line.md),
[E-F12-12 Master plan line](../../data/e-f12-12-master-plan-line.md),
[E-F12-02 Work centre](../../data/e-f12-02-work-centre.md),
[E-F12-04 Manufacturing order](../../data/e-f12-04-manufacturing-order.md),
[E-F7-21 Demand forecast](../../../f07-purchasing-and-stock/data/e-f07-21-demand-forecast.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F12-32 MPS line | Draft | Badge "Draft"; a new record starts here; next: Firm or Cancelled (BR-F12-29, UC-F12-34); fields editable within the role | U21 | `u21-production-planner/s-f12-33-mps-e-f12-32-mps-line-draft-{desktop,phone}-{light,dark}.png` |
| E-F12-32 MPS line | Firm | Badge "Firm"; next: Released or Draft (UC-F12-34); fields editable within the role | U21 | `u21-production-planner/s-f12-33-mps-e-f12-32-mps-line-firm-{desktop,phone}-{light,dark}.png` |
| E-F12-32 MPS line | Released | Badge "Released"; next: Closed (UC-F12-34); fields editable within the role | U21 | `u21-production-planner/s-f12-33-mps-e-f12-32-mps-line-released-{desktop,phone}-{light,dark}.png` |
| E-F12-32 MPS line | Closed | Badge "Closed"; final state, read-only | U21 | `u21-production-planner/s-f12-33-mps-e-f12-32-mps-line-closed-{desktop,phone}-{light,dark}.png` |
| E-F12-32 MPS line | Cancelled | Badge "Cancelled"; final state, read-only | U21 | `u21-production-planner/s-f12-33-mps-e-f12-32-mps-line-cancelled-{desktop,phone}-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per persona, device and theme; the
image round draws them. Rows are derived from each entity's Lifecycle: the badge is the state's name, the next states
are its transitions, and a final state is read-only.

## Responsive behaviour

Desktop only; on a tablet the table scrolls sideways with the week column fixed.

## Accessibility

Over capacity is a word and a number of hours, not only a colour; keyboard: next week, firm, release.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-16 KPI strip](../../../../04-ux/design-system/components/c-16-kpi-strip.md)
- [C-14 Timeline](../../../../04-ux/design-system/components/c-14-timeline.md)
- [C-01 Button](../../../../04-ux/design-system/components/c-01-button.md)

## Shown in

- [FL-F12-14 CAD, kanban, MPS and tools](../../flows/fl-f12-14-cad-kanban-mps-and-tools.md)

## Open questions

None.

---

⬅️ [S-F12-32 Kanban](s-f12-32-kanban.md) · ⬆️ [Up](README.md) ·
➡️ [S-F12-34 Tools and moulds](s-f12-34-tools-and-moulds.md)
