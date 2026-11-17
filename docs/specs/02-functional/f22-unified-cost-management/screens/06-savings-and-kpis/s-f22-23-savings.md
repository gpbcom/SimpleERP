🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
💸 [F22 Unified platform cost management](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F22-06 Savings and KPIs](README.md) › 🖥️ S-F22-23 Savings

# 🖥️ S-F22-23 Savings

**Status:** ✅ specified

## Personas

- [U13 Owner](../../../../01-users/personas/u13-owner.md)
- [U07 Administrator](../../../../01-users/personas/u07-administrator.md)

## Purpose

Show savings recommendations and their measured effect.

## Entry points

Costs, Savings; the monthly notice.

## Wireframe

```text
Savings                               Expected 54.00 EUR a month
-------------------------------------------------------------------------------
Feature      Change                 Expected   Quality      State
Summaries    local model            42.00      within bar   [Apply] [Dismiss]
Answers      cache identical        12.00      same         applied, saved 11.20
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F22-06 step 1, U13 | desktop | ![FL-F22-06 step 1, U13, light](../../images/06-savings-and-kpis/u13-owner/1-savings-desktop-light.png) | ![FL-F22-06 step 1, U13, dark](../../images/06-savings-and-kpis/u13-owner/1-savings-desktop-dark.png) |
| FL-F22-06 step 1, U13 | phone | ![FL-F22-06 step 1, U13, light](../../images/06-savings-and-kpis/u13-owner/1-savings-phone-light.png) | ![FL-F22-06 step 1, U13, dark](../../images/06-savings-and-kpis/u13-owner/1-savings-phone-dark.png) |
| Error E1, U13 | desktop | ![Error E1, U13, light](../../images/06-savings-and-kpis/u13-owner/e1-savings-refused-desktop-light.png) | ![Error E1, U13, dark](../../images/06-savings-and-kpis/u13-owner/e1-savings-refused-desktop-dark.png) |
| Error E1, U13 | phone | ![Error E1, U13, light](../../images/06-savings-and-kpis/u13-owner/e1-savings-refused-phone-light.png) | ![Error E1, U13, dark](../../images/06-savings-and-kpis/u13-owner/e1-savings-refused-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f22-23-savings-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f22-23-savings-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f22-23-savings-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f22-23-savings-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f22-23-savings-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f22-23-savings-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f22-23-savings-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f22-23-savings-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Feature | E-F22-16 | text | no | yes |
| Change | E-F22-16 | text | no | yes |
| Expected, measured | E-F22-16 | EUR | no | yes |
| State | E-F22-16 | list | yes (owner) | yes |

## Actions

| Action | Where | Who | Result |
|---|---|---|---|
| Apply | row | owner | administrator asked to change the setting |
| Dismiss | row | owner | reason kept |

## States

- Normal: recommendations with savings.
- Empty: "No saving found": usage is already efficient.
- Loading: the frame and titles show at once with placeholder rows for the recommendations; within 1 second (D408) the
  data replaces them, and a longer load shows a progress line saying what loads.
- Error: none beyond D122.
- Read-only: administrators read and apply when asked.
- Offline: Recommendations last loaded stay readable. Nothing else is queued: D38 keeps only today's schedule, time and
  intervention records offline; a banner says the connection is lost and the actions come back with it.

Shown entities (VD-15): [E-F22-16 Savings recommendation](../../data/e-f22-16-savings-recommendation.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F22-16 Savings recommendation | Proposed | Badge "Proposed"; a new record starts here; next: Applied or Dismissed (UC-F22-23); fields editable within the role | U07, U13 | `u07-administrator/s-f22-23-savings-e-f22-16-savings-recommendation-proposed-desktop-{light,dark}.png`, `u13-owner/s-f22-23-savings-e-f22-16-savings-recommendation-proposed-{desktop,phone}-{light,dark}.png` |
| E-F22-16 Savings recommendation | Applied | Badge "Applied"; next: Measured (UC-F22-23); fields editable within the role | U07, U13 | `u07-administrator/s-f22-23-savings-e-f22-16-savings-recommendation-applied-desktop-{light,dark}.png`, `u13-owner/s-f22-23-savings-e-f22-16-savings-recommendation-applied-{desktop,phone}-{light,dark}.png` |
| E-F22-16 Savings recommendation | Measured | Badge "Measured"; final: read-only, no next state; the history shows how it got here | U07, U13 | `u07-administrator/s-f22-23-savings-e-f22-16-savings-recommendation-measured-desktop-{light,dark}.png`, `u13-owner/s-f22-23-savings-e-f22-16-savings-recommendation-measured-{desktop,phone}-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop; phone for the owner.

## Accessibility

Keyboard order follows the reading order; every control has a visible label; amounts, states and icons are also given as
text; status changes are announced to screen readers.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-01 Button](../../../../04-ux/design-system/components/c-01-button.md)
- [C-10 Empty state](../../../../04-ux/design-system/components/c-10-empty-state.md)

## Shown in

- [FL-F22-06 Savings and KPIs](../../flows/fl-f22-06-savings-and-kpis.md)

## Open questions

None.

---

⬅️ [S-F22-22 Self-hosted compute](../01-see-and-set-up/s-f22-22-self-hosted-compute.md) · ⬆️ [Up](README.md) ·
➡️ [S-F22-24 Cost KPIs](s-f22-24-cost-kpis.md)
