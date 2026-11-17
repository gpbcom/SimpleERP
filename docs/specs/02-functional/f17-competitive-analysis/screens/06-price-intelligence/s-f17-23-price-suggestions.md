🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🔭 [F17 Competitive analysis](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F17-06 Price intelligence](README.md) › 🖥️ S-F17-23 Price suggestions

# 🖥️ S-F17-23 Price suggestions

**Status:** ✅ specified

## Personas

- [U13 Owner](../../../../01-users/personas/u13-owner.md), who approves
- [U03 Sales](../../../../01-users/personas/u03-sales.md), who reads

## Purpose

Show the price index per family and the suggestions for F6 price lists, with their evidence.

## Entry points

Competition menu, Price index; the suggestion notification.

## Wireframe

```text
Price index                   Family [Plans v]     Index 104   (24-month chart)
-------------------------------------------------------------------------------
Suggestion: Plan Pro 49.00 -> 47.00 from 2026-12-01      margin -4.1 %
Evidence: Rival SA Pro 46.00 (2026-11-10), Other Co Pro 47.50 (2026-11-09) ...
[Approve] [Refuse: reason] [What-if]
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F17-06 step 2, U13 | desktop | ![FL-F17-06 step 2, U13, light](../../images/06-price-intelligence/u13-owner/2-price-suggestions-desktop-light.png) | ![FL-F17-06 step 2, U13, dark](../../images/06-price-intelligence/u13-owner/2-price-suggestions-desktop-dark.png) |
| FL-F17-06 step 2, U13 | phone | ![FL-F17-06 step 2, U13, light](../../images/06-price-intelligence/u13-owner/2-price-suggestions-phone-light.png) | ![FL-F17-06 step 2, U13, dark](../../images/06-price-intelligence/u13-owner/2-price-suggestions-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f17-23-price-suggestions-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f17-23-price-suggestions-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f17-23-price-suggestions-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f17-23-price-suggestions-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f17-23-price-suggestions-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f17-23-price-suggestions-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f17-23-price-suggestions-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f17-23-price-suggestions-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Family | E-F17-17 family | list | yes | yes |
| Index | E-F17-17 index | number | no | yes |
| Current, proposed | E-F17-18 | EUR | proposed editable by the owner | yes |
| From | E-F17-18 from | date | yes | yes |
| Evidence | E-F17-18 evidence | price points with dates | no | yes |

## Actions

| Action | Where | Who | Result |
|---|---|---|---|
| Approve | suggestion | owner | F6 price list from the date |
| Refuse | suggestion | owner | closed with the reason |
| What-if | suggestion | owner | F23 simulation opened |

## States

- Normal: the index chart and open suggestions with evidence.
- Empty: "No suggestion": the index is within the threshold.
- Loading: the frame and titles show at once with placeholder rows for the index; within 1 second (D408) the data
  replaces them, and a longer load shows a progress line saying what loads.
- Error: a family with too few pairs, shown without an index.
- Read-only: sales and marketing read; decided suggestions are read-only.
- Offline: not available offline: the index is computed on the server. D38 keeps only today's schedule, time and
  intervention records offline. A banner says the connection is lost; what is on screen stays visible, every action is
  disabled and nothing is queued until the connection is back.

Shown entities (VD-15): [E-F17-17 Price index](../../data/e-f17-17-price-index.md),
[E-F17-18 Price suggestion](../../data/e-f17-18-price-suggestion.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F17-17 Price index | Computed | Badge "Computed"; a new record starts here; next: Superseded (BR-F17-08); fields editable within the role | U03, U13 | `u03-sales/s-f17-23-price-suggestions-e-f17-17-price-index-computed-{desktop,phone,tablet}-{light,dark}.png`, `u13-owner/s-f17-23-price-suggestions-e-f17-17-price-index-computed-{desktop,phone}-{light,dark}.png` |
| E-F17-17 Price index | Superseded | Badge "Superseded"; final: read-only, no next state; the history shows how it got here | U03, U13 | `u03-sales/s-f17-23-price-suggestions-e-f17-17-price-index-superseded-{desktop,phone,tablet}-{light,dark}.png`, `u13-owner/s-f17-23-price-suggestions-e-f17-17-price-index-superseded-{desktop,phone}-{light,dark}.png` |
| E-F17-18 Price suggestion | Proposed | Badge "Proposed"; a new record starts here; next: Approved or Refused (UC-F17-23); fields editable within the role | U03, U13 | `u03-sales/s-f17-23-price-suggestions-e-f17-18-price-suggestion-proposed-{desktop,phone,tablet}-{light,dark}.png`, `u13-owner/s-f17-23-price-suggestions-e-f17-18-price-suggestion-proposed-{desktop,phone}-{light,dark}.png` |
| E-F17-18 Price suggestion | Approved | Badge "Approved"; next: Applied (UC-F17-23); fields editable within the role | U03, U13 | `u03-sales/s-f17-23-price-suggestions-e-f17-18-price-suggestion-approved-{desktop,phone,tablet}-{light,dark}.png`, `u13-owner/s-f17-23-price-suggestions-e-f17-18-price-suggestion-approved-{desktop,phone}-{light,dark}.png` |
| E-F17-18 Price suggestion | Refused | Badge "Refused"; final: read-only, no next state; the history shows how it got here | U03, U13 | `u03-sales/s-f17-23-price-suggestions-e-f17-18-price-suggestion-refused-{desktop,phone,tablet}-{light,dark}.png`, `u13-owner/s-f17-23-price-suggestions-e-f17-18-price-suggestion-refused-{desktop,phone}-{light,dark}.png` |
| E-F17-18 Price suggestion | Applied | Badge "Applied"; final: read-only, no next state; the history shows how it got here | U03, U13 | `u03-sales/s-f17-23-price-suggestions-e-f17-18-price-suggestion-applied-{desktop,phone,tablet}-{light,dark}.png`, `u13-owner/s-f17-23-price-suggestions-e-f17-18-price-suggestion-applied-{desktop,phone}-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop; the owner approves on a phone.

## Accessibility

Keyboard order follows the reading order; every control has a visible label; amounts, states and icons are also given as
text; status changes are announced to screen readers.

## Components

- [C-09 Chart](../../../../04-ux/design-system/components/c-09-chart.md)
- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-01 Button](../../../../04-ux/design-system/components/c-01-button.md)
- [C-10 Empty state](../../../../04-ux/design-system/components/c-10-empty-state.md)

## Shown in

- [FL-F17-06 Price intelligence](../../flows/fl-f17-06-price-intelligence.md)

## Open questions

None.

---

⬅️ [S-F17-22 Data costs](../01-set-up-and-profiles/s-f17-22-data-costs.md) · ⬆️ [Up](README.md) ·
➡️ [S-F17-24 Competitive reports](s-f17-24-competitive-reports.md)
