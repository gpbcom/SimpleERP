🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🏭 [F12 Manufacturing (plugin)](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F12-05 Subcontracting and costs](README.md) › 🖥️ S-F12-26 Work in progress

# 🖥️ S-F12-26 Work in progress

**Status:** ✅ specified

## Personas

- [U05 Accounting](../../../../01-users/personas/u05-accounting.md)
- [U21 Production planner](../../../../01-users/personas/u21-production-planner.md)

## Purpose

Value open orders at month end and post the entry.

## Entry points

Accounting › Work in progress.

## Wireframe

```text
+------------------------------------------------------------------+
| Work in progress at 2026-11-30                                    |
| Order    Components  Labour  Machine  Total                       |
| MO-412   2,100       640     480      3,220                       |
| MO-415   4,800       1,200   0 (no rate!)  6,000                 |
| Total 38,400 EUR                                [Post]            |
+------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F12-05 step 4, U05 | desktop | ![FL-F12-05 step 4, U05, light](../../images/05-subcontracting-and-costs/u05-accounting/4-work-in-progress-desktop-light.png) | ![FL-F12-05 step 4, U05, dark](../../images/05-subcontracting-and-costs/u05-accounting/4-work-in-progress-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f12-26-work-in-progress-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f12-26-work-in-progress-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f12-26-work-in-progress-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f12-26-work-in-progress-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f12-26-work-in-progress-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f12-26-work-in-progress-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f12-26-work-in-progress-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f12-26-work-in-progress-offline-desktop-dark.png) |

## Fields and columns

| Label | Data | Editable |
|---|---|---|
| Orders, costs, total | E-F12-21 | no |

## Actions

| Action | Who | Result |
|---|---|---|
| Post | accounting | Entry, reversed next month |

## States

- Normal: value open orders at month end and post the entry.
- Empty: no open order at month end: "Nothing in progress".
- Loading: skeleton rows in place of the list ([C-03](../../../../04-ux/design-system/components/c-03-data-table.md));
  actions disabled until it has loaded.
- Error: the error message pattern (D122).
- Read-only: posted months.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md)); the app shows that it is offline and reloads the
  screen when the network is back.

Shown entities (VD-15): [E-F12-04 Manufacturing order](../../data/e-f12-04-manufacturing-order.md),
[E-F12-21 Work-in-progress valuation](../../data/e-f12-21-work-in-progress-valuation.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F12-04 Manufacturing order | Draft | Badge "Draft"; a new record starts here; next: Confirmed or Cancelled (UC-F12-04, BR-F12-02); fields editable within the role | U05 | `u05-accounting/s-f12-26-work-in-progress-e-f12-04-manufacturing-order-draft-desktop-{light,dark}.png` |
| E-F12-04 Manufacturing order | Confirmed | Badge "Confirmed"; next: In progress or Cancelled (UC-F12-27, BR-F12-02); fields editable within the role | U05 | `u05-accounting/s-f12-26-work-in-progress-e-f12-04-manufacturing-order-confirmed-desktop-{light,dark}.png` |
| E-F12-04 Manufacturing order | In progress | Badge "In progress"; next: Done or Cancelled (UC-F12-04, BR-F12-02); fields editable within the role | U05 | `u05-accounting/s-f12-26-work-in-progress-e-f12-04-manufacturing-order-in-progress-desktop-{light,dark}.png` |
| E-F12-04 Manufacturing order | Done | Badge "Done"; final: read-only, no next state; the history shows how it got here | U05 | `u05-accounting/s-f12-26-work-in-progress-e-f12-04-manufacturing-order-done-desktop-{light,dark}.png` |
| E-F12-21 Work-in-progress valuation | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U05 | `u05-accounting/s-f12-26-work-in-progress-e-f12-21-work-in-progress-valuation-active-desktop-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop.

## Accessibility

Every status is a word, not only a colour; tables have headers; actions are buttons with labels.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-01 Button](../../../../04-ux/design-system/components/c-01-button.md)

## Shown in

- [FL-F12-13 Energy, passport and work in progress](../../flows/fl-f12-13-energy-passport-and-work-in-progress.md)

## Open questions

None.

---

⬅️ [S-F12-25 Control chart](../12-quality-engineering/s-f12-25-control-chart.md) · ⬆️ [Up](README.md) ·
➡️ [S-F12-27 Work instructions](../10-people-and-tools/s-f12-27-work-instructions.md)
