🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🔭 [F17 Competitive analysis](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F17-01 Set up and profiles](README.md) › 🖥️ S-F17-22 Data costs

# 🖥️ S-F17-22 Data costs

**Status:** ✅ specified

## Personas

- [U13 Owner](../../../../01-users/personas/u13-owner.md)
- [U07 Administrator](../../../../01-users/personas/u07-administrator.md)

## Purpose

Show each paid data provider's spend against its budget, with warnings and stops.

## Entry points

Competition settings, Data costs; the budget warning.

## Wireframe

```text
Data costs, November 2026
-------------------------------------------------------------------------------
Provider     Calls    Spend     Budget    Used    State
Provider P   8 200    410.00    500.00    82 %    warned
Provider Q   1 100     44.00    100.00    44 %    within
-------------------------------------------------------------------------------
[Raise budget in F22]
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F17-01 step 5, U13 | desktop | ![FL-F17-01 step 5, U13, light](../../images/01-set-up-and-profiles/u13-owner/5-data-costs-desktop-light.png) | ![FL-F17-01 step 5, U13, dark](../../images/01-set-up-and-profiles/u13-owner/5-data-costs-desktop-dark.png) |
| FL-F17-01 step 5, U13 | phone | ![FL-F17-01 step 5, U13, light](../../images/01-set-up-and-profiles/u13-owner/5-data-costs-phone-light.png) | ![FL-F17-01 step 5, U13, dark](../../images/01-set-up-and-profiles/u13-owner/5-data-costs-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f17-22-data-costs-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f17-22-data-costs-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f17-22-data-costs-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f17-22-data-costs-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f17-22-data-costs-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f17-22-data-costs-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f17-22-data-costs-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f17-22-data-costs-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Provider | E-F17-19 provider | name | no | yes |
| Calls | E-F17-19 calls | number | no | yes |
| Spend | E-F17-19 amount | EUR | no | yes |
| Budget | E-F17-19 budget | EUR | no (set in F22) | yes |
| State | E-F17-19 state | within, warned, stopped | no | yes |

## Actions

| Action | Where | Who | Result |
|---|---|---|---|
| Raise budget | footer | owner | opens F22's budget |
| Open month | row | owner, administrator | the month's calls |

## States

- Normal: providers with spend, budget and state for the month.
- Empty: "No paid provider": shown when only free sources are used.
- Loading: the frame and titles show at once with placeholder rows for the providers; within 1 second (D408) the data
  replaces them, and a longer load shows a progress line saying what loads.
- Error: a bill that differs from the meter, with both amounts.
- Read-only: always read-only here; budgets are changed in F22.
- Offline: not available offline: spend is counted on the server. D38 keeps only today's schedule, time and intervention
  records offline. A banner says the connection is lost; what is on screen stays visible, every action is disabled and
  nothing is queued until the connection is back.

Shown entities (VD-15): [E-F17-09 Data provider](../../data/e-f17-09-data-provider.md),
[E-F17-19 Data cost line](../../data/e-f17-19-data-cost-line.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F17-09 Data provider | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U07, U13 | `u07-administrator/s-f17-22-data-costs-e-f17-09-data-provider-active-desktop-{light,dark}.png`, `u13-owner/s-f17-22-data-costs-e-f17-09-data-provider-active-{desktop,phone}-{light,dark}.png` |
| E-F17-19 Data cost line | Within | Badge "Within"; a new record starts here; next: Warned (UC-F17-22); fields editable within the role | U07, U13 | `u07-administrator/s-f17-22-data-costs-e-f17-19-data-cost-line-within-desktop-{light,dark}.png`, `u13-owner/s-f17-22-data-costs-e-f17-19-data-cost-line-within-{desktop,phone}-{light,dark}.png` |
| E-F17-19 Data cost line | Warned | Badge "Warned"; next: Stopped (UC-F17-10); fields editable within the role | U07, U13 | `u07-administrator/s-f17-22-data-costs-e-f17-19-data-cost-line-warned-desktop-{light,dark}.png`, `u13-owner/s-f17-22-data-costs-e-f17-19-data-cost-line-warned-{desktop,phone}-{light,dark}.png` |
| E-F17-19 Data cost line | Stopped | Badge "Stopped"; next: Within (UC-F17-10); fields editable within the role | U07, U13 | `u07-administrator/s-f17-22-data-costs-e-f17-19-data-cost-line-stopped-desktop-{light,dark}.png`, `u13-owner/s-f17-22-data-costs-e-f17-19-data-cost-line-stopped-{desktop,phone}-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop; the owner reads on a phone.

## Accessibility

Keyboard order follows the reading order; every control has a visible label; amounts, states and icons are also given as
text; status changes are announced to screen readers.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-09 Chart](../../../../04-ux/design-system/components/c-09-chart.md)
- [C-10 Empty state](../../../../04-ux/design-system/components/c-10-empty-state.md)

## Shown in

- [FL-F17-01 Set up and profiles](../../flows/fl-f17-01-set-up-and-profiles.md)

## Open questions

None.

---

⬅️ [S-F17-21 Tender watch](../05-tender-watch/s-f17-21-tender-watch.md) · ⬆️ [Up](README.md) ·
➡️ [S-F17-23 Price suggestions](../06-price-intelligence/s-f17-23-price-suggestions.md)
