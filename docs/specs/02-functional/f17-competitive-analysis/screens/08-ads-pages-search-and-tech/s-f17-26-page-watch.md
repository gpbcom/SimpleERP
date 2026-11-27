🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🔭 [F17 Competitive analysis](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F17-08 Ads, pages, search and technologies](README.md) › 🖥️ S-F17-26 Watched pages

# 🖥️ S-F17-26 Watched pages

**Status:** ✅ specified

## Personas

- [U12 Marketing and communication](../../../../01-users/personas/u12-marketing.md): every watched page and its changes.
- [U13 Owner](../../../../01-users/personas/u13-owner.md): the changes marked important, from their phone.

## Purpose

Add a competitor's public page to watch, read what changed and mark what matters.

## Entry points

Competitive analysis › Watched pages; a competitor's profile › Pages; the alert on a phone.

## Wireframe

```text
+---------------------------------------------------------------------------------------------+
| Watched pages                 [Add page]        Changed this week 3     Blocked 1             |
|---------------------------------------------------------------------------------------------|
| PAGE                              COMPETITOR   RHYTHM  LAST CHECK   STATE     LAST CHANGE     |
| northwind.example/pricing         Northwind    Daily   2026-11-14   Changed   2026-11-13      |
| contoso.example/offers            Contoso      Weekly  2026-11-10   Watching  2026-10-21      |
| Robots rules: reading allowed, 1 read every 10 seconds                                       |
| Change: "Pro 49 EUR per month" became "Pro 59 EUR per month"   [Important] [Note] [Card]     |
+---------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F17-08 step 2, U12 | desktop | ![FL-F17-08 step 2, U12, light](../../images/08-ads-pages-search-and-tech/u12-marketing/2-page-watch-desktop-light.png) | ![FL-F17-08 step 2, U12, dark](../../images/08-ads-pages-search-and-tech/u12-marketing/2-page-watch-desktop-dark.png) |
| FL-F17-08 step 2, U12 | phone | ![FL-F17-08 step 2, U12, light](../../images/08-ads-pages-search-and-tech/u12-marketing/2-page-watch-phone-light.png) | ![FL-F17-08 step 2, U12, dark](../../images/08-ads-pages-search-and-tech/u12-marketing/2-page-watch-phone-dark.png) |
| Error E1, U12 | desktop | ![Error E1, U12, light](../../images/08-ads-pages-search-and-tech/u12-marketing/e1-the-source-blocks-the-collection-desktop-light.png) | ![Error E1, U12, dark](../../images/08-ads-pages-search-and-tech/u12-marketing/e1-the-source-blocks-the-collection-desktop-dark.png) |
| Error E1, U12 | phone | ![Error E1, U12, light](../../images/08-ads-pages-search-and-tech/u12-marketing/e1-the-source-blocks-the-collection-phone-light.png) | ![Error E1, U12, dark](../../images/08-ads-pages-search-and-tech/u12-marketing/e1-the-source-blocks-the-collection-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f17-26-page-watch-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f17-26-page-watch-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f17-26-page-watch-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f17-26-page-watch-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f17-26-page-watch-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f17-26-page-watch-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f17-26-page-watch-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f17-26-page-watch-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Page address | E-F17-22 address | link | by marketing while Draft or Watching | yes |
| Competitor | E-F17-22 competitor | name | by marketing | yes |
| Rhythm | E-F17-22 rhythm | daily, weekly | by marketing | yes |
| Robots rules | E-F17-22 rules read | allowed or forbidden, rate | no | no |
| Last check and state | E-F17-22 state | date and badge | no | yes |
| Change | E-F17-22 snapshots | old and new text | no | no |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Add page | header | marketing | checks the robots rules and takes the first snapshot |
| Mark important | change | marketing | alerts the owner and sales |
| Pause or remove | row | marketing | stops the checks and keeps the history |
| Send to a battle card | change | marketing | adds the change as evidence |

## States

- Normal: the watched pages with their state and, for a changed page, the highlighted difference.
- Empty: No page watched yet, with Add page and the rules that apply.
- Loading: the headings and the table as placeholders; the values follow.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); a forbidden or
  blocked page shows the rule or the answer of the site.
- Read-only: the record in a locked state: values shown, no action offered.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-F17-22 Watched page](../../data/e-f17-22-watched-page.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F17-22 Watched page | Watching | Badge "Watching"; a new record starts here; next: Changed, Blocked or Removed (UC-F17-27, BR-F17-18); fields editable within the role | U12, U13 | `u12-marketing/s-f17-26-page-watch-e-f17-22-watched-page-watching-{desktop,phone}-{light,dark}.png`, `u13-owner/s-f17-26-page-watch-e-f17-22-watched-page-watching-{desktop,phone}-{light,dark}.png` |
| E-F17-22 Watched page | Changed | Badge "Changed"; next: Watching (UC-F17-27); fields editable within the role | U12, U13 | `u12-marketing/s-f17-26-page-watch-e-f17-22-watched-page-changed-{desktop,phone}-{light,dark}.png`, `u13-owner/s-f17-26-page-watch-e-f17-22-watched-page-changed-{desktop,phone}-{light,dark}.png` |
| E-F17-22 Watched page | Blocked | Badge "Blocked"; next: Watching (UC-F17-27); fields editable within the role | U12, U13 | `u12-marketing/s-f17-26-page-watch-e-f17-22-watched-page-blocked-{desktop,phone}-{light,dark}.png`, `u13-owner/s-f17-26-page-watch-e-f17-22-watched-page-blocked-{desktop,phone}-{light,dark}.png` |
| E-F17-22 Watched page | Removed | Badge "Removed"; final: read-only, no next state; the history shows how it got here | U12, U13 | `u12-marketing/s-f17-26-page-watch-e-f17-22-watched-page-removed-{desktop,phone}-{light,dark}.png`, `u13-owner/s-f17-26-page-watch-e-f17-22-watched-page-removed-{desktop,phone}-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Marketing's table is desktop only. The owner reads a change and its two texts on a phone: the page, the old and new
text, and an Important button.

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

⬅️ [S-F17-25 Competitor ads](s-f17-25-competitor-ads.md) · ⬆️ [Up](README.md) ·
➡️ [S-F17-27 Search overlap](s-f17-27-search-overlap.md)
