🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🔮 [F23 What-if simulation and impact](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F23-06 Goals and financing](README.md) › 🖥️ S-F23-21 Goal seeking

# 🖥️ S-F23-21 Goal seeking

**Status:** ✅ specified

## Personas

- [U13 Owner](../../../../01-users/personas/u13-owner.md)
- [U05 Accounting](../../../../01-users/personas/u05-accounting.md)

## Purpose

Seek a goal or the break-even point with chosen levers.

## Entry points

Simulation, Goals; the AI assistant ("what must change to reach").

## Wireframe

```text
Goal seeking         [Goal] [Break-even]
-------------------------------------------------------------------------------
Goal: margin [12 %] by [2027-06-30]
Levers: price [0 to +5 %]  purchases [-5 to 0 %]  staff [not used]
Result: price +2.5 %, purchases -3 %  -> margin 12.0 %       [Save as scenario]
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F23-06 step 1, U13 | desktop | ![FL-F23-06 step 1, U13, light](../../images/06-goals-and-financing/u13-owner/1-goal-seeking-desktop-light.png) | ![FL-F23-06 step 1, U13, dark](../../images/06-goals-and-financing/u13-owner/1-goal-seeking-desktop-dark.png) |
| FL-F23-06 step 1, U13 | phone | ![FL-F23-06 step 1, U13, light](../../images/06-goals-and-financing/u13-owner/1-goal-seeking-phone-light.png) | ![FL-F23-06 step 1, U13, dark](../../images/06-goals-and-financing/u13-owner/1-goal-seeking-phone-dark.png) |
| Error E1, U13 | desktop | ![Error E1, U13, light](../../images/06-goals-and-financing/u13-owner/e1-goal-seeking-refused-desktop-light.png) | ![Error E1, U13, dark](../../images/06-goals-and-financing/u13-owner/e1-goal-seeking-refused-desktop-dark.png) |
| Error E1, U13 | phone | ![Error E1, U13, light](../../images/06-goals-and-financing/u13-owner/e1-goal-seeking-refused-phone-light.png) | ![Error E1, U13, dark](../../images/06-goals-and-financing/u13-owner/e1-goal-seeking-refused-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f23-21-goal-seeking-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f23-21-goal-seeking-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f23-21-goal-seeking-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f23-21-goal-seeking-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f23-21-goal-seeking-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f23-21-goal-seeking-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f23-21-goal-seeking-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f23-21-goal-seeking-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Measure, target, date | E-F23-11 | list, value, date | yes | yes |
| Levers | E-F23-11 levers | bounds | yes | yes |
| Result | E-F23-11 result | text | no | no |

## Actions

| Action | Where | Who | Result |
|---|---|---|---|
| Seek | footer | owner, accounting | search runs on a copy |
| Save as scenario | footer | owner | scenario saved |

## States

- Normal: goal, levers and result.
- Empty: "Set a goal": examples of goals.
- Loading: the frame and titles show at once with placeholder rows for the result; within 1 second (D408) the data
  replaces them, and a longer load shows a progress line saying what loads.
- Error: a lever without bounds; an unreachable goal with its gap.
- Read-only: shared readers see results within their rights.
- Offline: not available offline: the engine runs on the server. D38 keeps only today's schedule, time and intervention
  records offline. A banner says the connection is lost; what is on screen stays visible, every action is disabled and
  nothing is queued until the connection is back.

Shown entities (VD-15): [E-F23-11 Goal](../../data/e-f23-11-goal.md),
[E-F23-02 Scenario](../../data/e-f23-02-scenario.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F23-11 Goal | Set | Badge "Set"; a new record starts here; next: Reached or Not reached (UC-F23-21); fields editable within the role | U05, U13 | `u05-accounting/s-f23-21-goal-seeking-e-f23-11-goal-set-desktop-{light,dark}.png`, `u13-owner/s-f23-21-goal-seeking-e-f23-11-goal-set-{desktop,phone}-{light,dark}.png` |
| E-F23-11 Goal | Reached | Badge "Reached"; final: read-only, no next state; the history shows how it got here | U05, U13 | `u05-accounting/s-f23-21-goal-seeking-e-f23-11-goal-reached-desktop-{light,dark}.png`, `u13-owner/s-f23-21-goal-seeking-e-f23-11-goal-reached-{desktop,phone}-{light,dark}.png` |
| E-F23-11 Goal | Not reached | Badge "Not reached"; final: read-only, no next state; the history shows how it got here | U05, U13 | `u05-accounting/s-f23-21-goal-seeking-e-f23-11-goal-not-reached-desktop-{light,dark}.png`, `u13-owner/s-f23-21-goal-seeking-e-f23-11-goal-not-reached-{desktop,phone}-{light,dark}.png` |
| E-F23-02 Scenario | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U05, U13 | `u05-accounting/s-f23-21-goal-seeking-e-f23-02-scenario-active-desktop-{light,dark}.png`, `u13-owner/s-f23-21-goal-seeking-e-f23-02-scenario-active-{desktop,phone}-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop.

## Accessibility

Keyboard order follows the reading order; every control has a visible label; amounts, states and icons are also given as
text; status changes are announced to screen readers.

## Components

- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)
- [C-09 Chart](../../../../04-ux/design-system/components/c-09-chart.md)
- [C-10 Empty state](../../../../04-ux/design-system/components/c-10-empty-state.md)

## Shown in

- [FL-F23-06 Goals and financing](../../flows/fl-f23-06-goals-and-financing.md)

## Open questions

None.

---

⬅️ [S-F23-20 What-if assistant](../02-run/s-f23-20-what-if-assistant.md) · ⬆️ [Up](README.md) ·
➡️ [S-F23-22 Financing](s-f23-22-financing.md)
