🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🔭 [F17 Competitive analysis](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F17-08 Ads, pages, search and technologies](README.md) › 🖥️ S-F17-25 Competitor ads

# 🖥️ S-F17-25 Competitor ads

**Status:** ✅ specified

## Personas

- [U12 Marketing and communication](../../../../01-users/personas/u12-marketing.md): every ad record of the competitors
  they follow.

## Purpose

Read what a competitor advertises, where and for how long, from the public ad libraries.

## Entry points

Competitive analysis › Competitor ads; a competitor's profile › Ads.

## Wireframe

```text
+---------------------------------------------------------------------------------------------+
| Competitor ads: Northwind Ltd      Period [last 90 days v]   Channel [All v]   Country [FR v]  |
|---------------------------------------------------------------------------------------------|
| Running 14   Started in 30 days 3   Ended 2            Most repeated: "free delivery", "-20%" |
| HEADLINE                    CHANNEL  COUNTRIES  FIRST SEEN   LAST SEEN   STATE   SOURCE        |
| Free delivery all June      Search   FR, BE     2026-06-02   2026-11-10  Active  Library A  >  |
| Summer sale -20%            Social   FR         2026-06-14   2026-08-31  Ended   Library B  >  |
| [Open] [Group by campaign] [Pin to profile] [To battle card]                                |
+---------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F17-08 step 1, U12 | desktop | ![FL-F17-08 step 1, U12, light](../../images/08-ads-pages-search-and-tech/u12-marketing/1-competitor-ads-desktop-light.png) | ![FL-F17-08 step 1, U12, dark](../../images/08-ads-pages-search-and-tech/u12-marketing/1-competitor-ads-desktop-dark.png) |
| FL-F17-08 step 1, U12 | phone | ![FL-F17-08 step 1, U12, light](../../images/08-ads-pages-search-and-tech/u12-marketing/1-competitor-ads-phone-light.png) | ![FL-F17-08 step 1, U12, dark](../../images/08-ads-pages-search-and-tech/u12-marketing/1-competitor-ads-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f17-25-competitor-ads-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f17-25-competitor-ads-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f17-25-competitor-ads-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f17-25-competitor-ads-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f17-25-competitor-ads-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f17-25-competitor-ads-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f17-25-competitor-ads-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f17-25-competitor-ads-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Competitor | E-F17-21 competitor | name | no | yes |
| Headline and text | E-F17-21 headline, text | text | no | yes |
| Channel and format | E-F17-21 channel, format | search, social, display, video | no | yes |
| Countries and languages | E-F17-21 countries | list | no | no |
| Dates seen | E-F17-21 first seen, last seen | two dates | no | yes |
| Source | E-F17-21 library and address | text and link | no | yes |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Open | row | marketing, sales, owner | the full ad with its source link |
| Group by campaign | toolbar | marketing | ads with the same text or landing address together |
| Pin to profile | row | marketing | the ad appears on the competitor's profile |
| Send to a battle card | row | marketing | the ad is added as evidence to a battle card |

## States

- Normal: the ad records of the competitor and period, with the counts and the repeated words.
- Empty: No ad found yet, with the libraries read and the date of the last read.
- Loading: the headings and the table as placeholders; the values follow.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); a failed
  library is named with its reason; the other libraries' ads are still shown.
- Read-only: the record in a locked state: values shown, no action offered.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-F17-21 Ad record](../../data/e-f17-21-ad-record.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F17-21 Ad record | Active | Badge "Active"; a new record starts here; next: Ended or Withdrawn (UC-F17-26, BR-F17-17); fields editable within the role | U12 | `u12-marketing/s-f17-25-competitor-ads-e-f17-21-ad-record-active-{desktop,phone}-{light,dark}.png` |
| E-F17-21 Ad record | Ended | Badge "Ended"; final: read-only, no next state; the history shows how it got here | U12 | `u12-marketing/s-f17-25-competitor-ads-e-f17-21-ad-record-ended-{desktop,phone}-{light,dark}.png` |
| E-F17-21 Ad record | Withdrawn | Badge "Withdrawn"; final: read-only, no next state; the history shows how it got here | U12 | `u12-marketing/s-f17-25-competitor-ads-e-f17-21-ad-record-withdrawn-{desktop,phone}-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop only; on a phone, the app asks to continue on a larger screen.

## Accessibility

Every control is reachable by keyboard; states and errors are announced to screen readers and never rely on colour
alone; each field has its visible label.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)
- [C-01 Button](../../../../04-ux/design-system/components/c-01-button.md)

## Shown in

- [FL-F17-08](../../flows/fl-f17-08-ads-pages-search-and-tech.md)

## Open questions

None.

---

⬅️ [S-F17-24 Competitive reports](../06-price-intelligence/s-f17-24-competitive-reports.md) · ⬆️ [Up](README.md) ·
➡️ [S-F17-26 Watched pages](s-f17-26-page-watch.md)
