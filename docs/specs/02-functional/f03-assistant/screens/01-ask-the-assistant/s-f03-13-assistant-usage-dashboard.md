🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) › 🤖 [F3 Assistant](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-F3-01 Ask the AI assistant](README.md) ›
🖥️ S-F3-13 Assistant usage dashboard

# 🖥️ S-F3-13 Assistant usage dashboard

**Status:** ✅ specified

## Personas

- [U07 Administrator](../../../../01-users/personas/u07-administrator.md)
- [U13 Owner](../../../../01-users/personas/u13-owner.md)

## Purpose

See how the AI assistant is used, what it costs and how answers are rated (D185, D186).

## Entry points

Administration › Assistant › Usage.

## Wireframe

```text
+------------------------------------------------------------------+
| Assistant usage     [This month v]  [All teams v]    [Export]     |
| [Usage] [Call log]                                                |
|------------------------------------------------------------------|
| Questions 1,284 | Changes 312 (undone 9) | Outside calls 840      |
| Local 92 % | External 8 %, 14.20 EUR | Thumbs up 87 %            |
|------------------------------------------------------------------|
| [chart: questions per day, by feature]                            |
| Thumbs down reasons: out of date 21, incomplete 12, wrong 5       |
| Caps: Shipping tool 812 / 1,000 (81 %)                            |
+------------------------------------------------------------------+
```

The call log tab (administrator only, D517):

```text
+------------------------------------------------------------------+
| Assistant usage     [This month v]  [All teams v]    [Export]    |
| [Usage] [Call log]                                               |
|------------------------------------------------------------------|
| AT           USER         CONNECTION    OPERATION SENT     STATUS|
| 10 Nov 15:40 Marie Dupont Shipping tool track     business done  |
| 10 Nov 15:12 Paul Martin  Shipping tool label     business capped|
| 10 Nov 11:03 Marie Dupont Bank feed     balance   none     failed|
| 3 of 840 calls; what was sent is never shown                     |
+------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F3-01 step 5, U07 | desktop | ![FL-F3-01 step 5, U07, light](../../images/01-ask-the-assistant/u07-administrator/5-usage-dashboard-desktop-light.png) | ![FL-F3-01 step 5, U07, dark](../../images/01-ask-the-assistant/u07-administrator/5-usage-dashboard-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f03-13-assistant-usage-dashboard-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f03-13-assistant-usage-dashboard-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f03-13-assistant-usage-dashboard-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f03-13-assistant-usage-dashboard-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f03-13-assistant-usage-dashboard-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f03-13-assistant-usage-dashboard-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f03-13-assistant-usage-dashboard-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f03-13-assistant-usage-dashboard-offline-desktop-dark.png) |

## Fields and columns

Questions, changes confirmed and undone, outside calls and caps, provider share and cost, feedback; by period, role or
team, feature.

Call log tab: one row per outside call
([E-F3-08 Outside call](../../data/e-f03-08-outside-call.md)): at, user, connection, operation, categories sent,
status; filters by period, connection, user and status. The content sent is never shown.

## Actions

| Action | Who | Result |
|---|---|---|
| Filter | administrator, owner | Period, role or team, feature |
| Export | administrator, owner | A spreadsheet of the counts |
| Open the call log | administrator (D517) | The outside calls of the period, newest first |
| Export the call log | administrator | A spreadsheet of the calls shown, audited |

## States

- Normal: See how the AI assistant is used, what it costs and how answers are rated (D185, D186), as the wireframe
  shows.
- Empty: "No questions yet this period."
- Loading: skeleton charts ([C-09](../../../../04-ux/design-system/components/c-09-chart.md)) in place of the figures;
  filters are disabled until they have loaded.
- Error: the error message pattern (D122).
- Read-only: always: the dashboard reads usage, never content (BR-F3-33).
- Offline: Not available offline: a back-office screen on live, shared data (D38: only today's schedule, time and
  intervention records work offline). The app shows that it is offline and reloads the screen when the network is back.
- A cap over 80 % highlighted.
- Call log empty: "No outside calls this period."
- Call log, owner without the administrator role: the tab is not shown (D517).

Shown entities (VD-15): [E-F3-08 Outside call](../../data/e-f03-08-outside-call.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F3-08 Outside call | Done | Badge "Done"; a new record starts here; no other state; fields editable within the role | U07 | `u07-administrator/s-f03-13-assistant-usage-dashboard-e-f03-08-outside-call-done-desktop-{light,dark}.png` |
| E-F3-08 Outside call | Refused | Badge "Refused"; a new record starts here; no other state; fields editable within the role | U07 | `u07-administrator/s-f03-13-assistant-usage-dashboard-e-f03-08-outside-call-refused-desktop-{light,dark}.png` |
| E-F3-08 Outside call | Failed | Badge "Failed"; a new record starts here; no other state; fields editable within the role | U07 | `u07-administrator/s-f03-13-assistant-usage-dashboard-e-f03-08-outside-call-failed-desktop-{light,dark}.png` |
| E-F3-08 Outside call | Capped | Badge "Capped"; a new record starts here; no other state; fields editable within the role | U07 | `u07-administrator/s-f03-13-assistant-usage-dashboard-e-f03-08-outside-call-capped-desktop-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop; read on a tablet.

## Accessibility

Each chart has its table; colours are never the only cue.

## Components

- [C-09 Chart](../../../../04-ux/design-system/components/c-09-chart.md)
- [C-04 Card](../../../../04-ux/design-system/components/c-04-card.md)
- [C-10 Empty state](../../../../04-ux/design-system/components/c-10-empty-state.md)
- [C-07 Tabs](../../../../04-ux/design-system/components/c-07-tabs.md)
- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)

## Shown in

- [Reports](../../reports.md)

## Open questions

None.

---

⬅️ [S-F3-12 Assistant settings](../03-act-through-the-assistant/s-f03-12-assistant-settings.md) · ⬆️ [Up](README.md) ·
➡️ [S-F3-14 Agents](../10-benchmark-additions/s-f03-14-agents.md)
