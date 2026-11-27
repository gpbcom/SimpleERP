🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🔭 [F17 Competitive analysis](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F17-08 Ads, pages, search and technologies](README.md) › 🖥️ S-F17-27 Search overlap

# 🖥️ S-F17-27 Search overlap

**Status:** ✅ specified

## Personas

- [U12 Marketing and communication](../../../../01-users/personas/u12-marketing.md): the keywords, the positions and the
  gaps.

## Purpose

Compare the company's search positions with its competitors', keyword by keyword, and follow the gap.

## Entry points

Competitive analysis › Search overlap; a competitor's profile › Keywords.

## Wireframe

```text
+---------------------------------------------------------------------------------------------+
| Search overlap: France, French    Us vs Northwind, Contoso     Provider: Search data A  2026-11 |
|---------------------------------------------------------------------------------------------|
| Shared 12     Gaps (only them) 9     Only us 5       [Add keywords] [Propose keywords]        |
| KEYWORD                  VOLUME   US    NORTHWIND  CONTOSO   TREND   PURSUE                   |
| invoicing software       8,100    14    3          7         up      [x]                      |
| small business erp       2,400    -     5          9         flat    [ ]                      |
| Figures: provider Search data A, read 2026-11-03. Older figures are grey.                    |
+---------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F17-08 step 3, U12 | desktop | ![FL-F17-08 step 3, U12, light](../../images/08-ads-pages-search-and-tech/u12-marketing/3-search-overlap-desktop-light.png) | ![FL-F17-08 step 3, U12, dark](../../images/08-ads-pages-search-and-tech/u12-marketing/3-search-overlap-desktop-dark.png) |
| FL-F17-08 step 3, U12 | phone | ![FL-F17-08 step 3, U12, light](../../images/08-ads-pages-search-and-tech/u12-marketing/3-search-overlap-phone-light.png) | ![FL-F17-08 step 3, U12, dark](../../images/08-ads-pages-search-and-tech/u12-marketing/3-search-overlap-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f17-27-search-overlap-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f17-27-search-overlap-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f17-27-search-overlap-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f17-27-search-overlap-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f17-27-search-overlap-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f17-27-search-overlap-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f17-27-search-overlap-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f17-27-search-overlap-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Keyword | E-F17-23 keyword | text | by marketing | yes |
| Search volume | E-F17-23 volume | number per month | no | no |
| Position of each site | E-F17-23 positions | numbers or dash | no | yes |
| Provider and date | E-F17-23 provider, read on | text and date | no | yes |
| Trend | E-F17-23 earlier positions | up, flat, down | no | no |
| Pursue | E-F17-23 pursue | yes or no | by marketing | no |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Add keywords | header | marketing | keywords are added to the monthly refresh |
| Propose keywords | header | marketing | keywords suggested from the sites' titles, to confirm |
| Mark to pursue | row | marketing | the keyword goes to the search basics of the site |
| Drop | row | marketing | the keyword leaves the refresh and keeps its history |

## States

- Normal: the keywords with the positions, the gaps and the trend, each with its provider and date.
- Empty: No keyword yet, with Add keywords and the provider to connect.
- Loading: the headings and the table as placeholders; the values follow.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); a provider
  error shows its message and the date of the last good figures.
- Read-only: the record in a locked state: values shown, no action offered.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-F17-23 Keyword](../../data/e-f17-23-keyword.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F17-23 Keyword | Proposed | Badge "Proposed"; a new record starts here; next: Followed or Dropped (UC-F17-28); fields editable within the role | U12 | `u12-marketing/s-f17-27-search-overlap-e-f17-23-keyword-proposed-{desktop,phone}-{light,dark}.png` |
| E-F17-23 Keyword | Followed | Badge "Followed"; next: Pursued or Dropped (UC-F17-28); fields editable within the role | U12 | `u12-marketing/s-f17-27-search-overlap-e-f17-23-keyword-followed-{desktop,phone}-{light,dark}.png` |
| E-F17-23 Keyword | Pursued | Badge "Pursued"; next: Followed (UC-F17-28); fields editable within the role | U12 | `u12-marketing/s-f17-27-search-overlap-e-f17-23-keyword-pursued-{desktop,phone}-{light,dark}.png` |
| E-F17-23 Keyword | Dropped | Badge "Dropped"; final: read-only, no next state; the history shows how it got here | U12 | `u12-marketing/s-f17-27-search-overlap-e-f17-23-keyword-dropped-{desktop,phone}-{light,dark}.png` |

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

⬅️ [S-F17-26 Watched pages](s-f17-26-page-watch.md) · ⬆️ [Up](README.md) ·
➡️ [S-F17-28 Technology detection](s-f17-28-tech-detection.md)
