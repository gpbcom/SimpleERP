🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
💸 [F22 Unified platform cost management](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F22-06 Savings and KPIs](README.md) › 🖥️ S-F22-24 Cost KPIs

# 🖥️ S-F22-24 Cost KPIs

**Status:** ✅ specified

## Personas

- [U13 Owner](../../../../01-users/personas/u13-owner.md)
- [U05 Accounting](../../../../01-users/personas/u05-accounting.md)

## Purpose

Show the cost KPIs with trends.

## Entry points

Costs, KPIs; the owner's home card.

## Wireframe

```text
Cost KPIs            Period [November 2026]
-------------------------------------------------------------------------------
Cost per active user   3.12    (Oct 3.40)
Local model share      64 %    (Oct 51 %)
Budget use             78 %
Invoice gap            1.2 %
Savings made           11.20
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F22-06 step 2, U13 | desktop | ![FL-F22-06 step 2, U13, light](../../images/06-savings-and-kpis/u13-owner/2-cost-kpis-desktop-light.png) | ![FL-F22-06 step 2, U13, dark](../../images/06-savings-and-kpis/u13-owner/2-cost-kpis-desktop-dark.png) |
| FL-F22-06 step 2, U13 | phone | ![FL-F22-06 step 2, U13, light](../../images/06-savings-and-kpis/u13-owner/2-cost-kpis-phone-light.png) | ![FL-F22-06 step 2, U13, dark](../../images/06-savings-and-kpis/u13-owner/2-cost-kpis-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f22-24-cost-kpis-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f22-24-cost-kpis-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f22-24-cost-kpis-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f22-24-cost-kpis-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f22-24-cost-kpis-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f22-24-cost-kpis-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f22-24-cost-kpis-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f22-24-cost-kpis-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| KPI | computed | number | no | yes |
| Trend | computed | number | no | no |

## Actions

| Action | Where | Who | Result |
|---|---|---|---|
| Choose period | header | owner, accounting | refreshed |
| Export | header | owner, accounting | file |

## States

- Normal: KPIs with trends.
- Empty: "Not enough data yet".
- Loading: the frame and titles show at once with placeholder rows for the KPIs; within 1 second (D408) the data
  replaces them, and a longer load shows a progress line saying what loads.
- Error: none beyond D122.
- Read-only: always read-only.
- Offline: KPIs last loaded stay visible with their date. Nothing else is queued: D38 keeps only today's schedule, time
  and intervention records offline; a banner says the connection is lost and the actions come back with it.

Shown entities (VD-15): [E-F22-16 Savings recommendation](../../data/e-f22-16-savings-recommendation.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F22-16 Savings recommendation | Proposed | Badge "Proposed"; a new record starts here; next: Applied or Dismissed (UC-F22-23); fields editable within the role | U05, U13 | `u05-accounting/s-f22-24-cost-kpis-e-f22-16-savings-recommendation-proposed-desktop-{light,dark}.png`, `u13-owner/s-f22-24-cost-kpis-e-f22-16-savings-recommendation-proposed-{desktop,phone}-{light,dark}.png` |
| E-F22-16 Savings recommendation | Applied | Badge "Applied"; next: Measured (UC-F22-23); fields editable within the role | U05, U13 | `u05-accounting/s-f22-24-cost-kpis-e-f22-16-savings-recommendation-applied-desktop-{light,dark}.png`, `u13-owner/s-f22-24-cost-kpis-e-f22-16-savings-recommendation-applied-{desktop,phone}-{light,dark}.png` |
| E-F22-16 Savings recommendation | Measured | Badge "Measured"; final: read-only, no next state; the history shows how it got here | U05, U13 | `u05-accounting/s-f22-24-cost-kpis-e-f22-16-savings-recommendation-measured-desktop-{light,dark}.png`, `u13-owner/s-f22-24-cost-kpis-e-f22-16-savings-recommendation-measured-{desktop,phone}-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop and phone.

## Accessibility

Keyboard order follows the reading order; every control has a visible label; amounts, states and icons are also given as
text; status changes are announced to screen readers.

## Components

- [C-09 Chart](../../../../04-ux/design-system/components/c-09-chart.md)
- [C-04 Card](../../../../04-ux/design-system/components/c-04-card.md)
- [C-10 Empty state](../../../../04-ux/design-system/components/c-10-empty-state.md)

## Shown in

- [FL-F22-06 Savings and KPIs](../../flows/fl-f22-06-savings-and-kpis.md)

## Open questions

None.

---

⬅️ [S-F22-23 Savings](s-f22-23-savings.md) · ⬆️ [Up](README.md) ·
➡️ [S-F22-25 Re-billing rules](../07-it-provider-re-billing/s-f22-25-re-billing-rules.md)
