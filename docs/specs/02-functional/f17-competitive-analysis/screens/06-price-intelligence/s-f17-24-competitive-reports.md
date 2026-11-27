🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🔭 [F17 Competitive analysis](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F17-06 Price intelligence](README.md) › 🖥️ S-F17-24 Competitive reports

# 🖥️ S-F17-24 Competitive reports

**Status:** ✅ specified

## Personas

- [U13 Owner](../../../../01-users/personas/u13-owner.md)
- [U12 Marketing and communication](../../../../01-users/personas/u12-marketing.md)

## Purpose

Show share of voice and the price-index trend with sources and export.

## Entry points

Competition menu, Reports; the digest.

## Wireframe

```text
Competitive reports       Period [November 2026]                [Export]
-------------------------------------------------------------------------------
Share of voice: ours 18 %  Rival SA 41 %  Other Co 22 %  others 19 %
Price-index trend: Plans 108 -> 104   Services 97 -> 99   (24 months)
-------------------------------------------------------------------------------
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F17-06 step 3, U13 | desktop | ![FL-F17-06 step 3, U13, light](../../images/06-price-intelligence/u13-owner/3-competitive-reports-desktop-light.png) | ![FL-F17-06 step 3, U13, dark](../../images/06-price-intelligence/u13-owner/3-competitive-reports-desktop-dark.png) |
| FL-F17-06 step 3, U13 | phone | ![FL-F17-06 step 3, U13, light](../../images/06-price-intelligence/u13-owner/3-competitive-reports-phone-light.png) | ![FL-F17-06 step 3, U13, dark](../../images/06-price-intelligence/u13-owner/3-competitive-reports-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f17-24-competitive-reports-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f17-24-competitive-reports-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f17-24-competitive-reports-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f17-24-competitive-reports-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f17-24-competitive-reports-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f17-24-competitive-reports-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f17-24-competitive-reports-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f17-24-competitive-reports-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Share of voice | computed from E-F17-08 | percent per competitor | no | yes |
| Index trend | E-F17-17 | number per month | no | yes |

## Actions

| Action | Where | Who | Result |
|---|---|---|---|
| Choose period | header | owner, marketing | reports refreshed |
| Open a point | chart | owner, marketing | facts and sources |
| Export | header | owner, marketing | Excel or PDF |

## States

- Normal: share of voice and index trend charts for the period.
- Empty: "Not enough data": shown below the minimum of mentions.
- Loading: the frame and titles show at once with placeholder rows for the reports; within 1 second (D408) the data
  replaces them, and a longer load shows a progress line saying what loads.
- Error: a period with too few mentions, said.
- Read-only: always read-only.
- Offline: The reports last loaded stay visible with their date. Nothing else is queued: D38 keeps only today's
  schedule, time and intervention records offline; a banner says the connection is lost and the actions come back with
  it.

Shown entities (VD-15): [E-F17-17 Price index](../../data/e-f17-17-price-index.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F17-17 Price index | Computed | Badge "Computed"; a new record starts here; next: Superseded (BR-F17-08); fields editable within the role | U12, U13 | `u12-marketing/s-f17-24-competitive-reports-e-f17-17-price-index-computed-{desktop,phone}-{light,dark}.png`, `u13-owner/s-f17-24-competitive-reports-e-f17-17-price-index-computed-{desktop,phone}-{light,dark}.png` |
| E-F17-17 Price index | Superseded | Badge "Superseded"; final: read-only, no next state; the history shows how it got here | U12, U13 | `u12-marketing/s-f17-24-competitive-reports-e-f17-17-price-index-superseded-{desktop,phone}-{light,dark}.png`, `u13-owner/s-f17-24-competitive-reports-e-f17-17-price-index-superseded-{desktop,phone}-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop; charts readable on a phone.

## Accessibility

Keyboard order follows the reading order; every control has a visible label; amounts, states and icons are also given as
text; status changes are announced to screen readers.

## Components

- [C-09 Chart](../../../../04-ux/design-system/components/c-09-chart.md)
- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-10 Empty state](../../../../04-ux/design-system/components/c-10-empty-state.md)

## Shown in

- [FL-F17-06 Price intelligence](../../flows/fl-f17-06-price-intelligence.md)

## Open questions

None.

---

⬅️ [S-F17-23 Price suggestions](s-f17-23-price-suggestions.md) · ⬆️ [Up](README.md) ·
➡️ [S-F17-25 Competitor ads](../08-ads-pages-search-and-tech/s-f17-25-competitor-ads.md)
