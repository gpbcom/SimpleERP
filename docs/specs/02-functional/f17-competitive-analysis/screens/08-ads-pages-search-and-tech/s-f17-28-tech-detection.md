🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🔭 [F17 Competitive analysis](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F17-08 Ads, pages, search and technologies](README.md) › 🖥️ S-F17-28 Technology detection

# 🖥️ S-F17-28 Technology detection

**Status:** 🔄 waiting for the owner

## Personas

- [U03 Sales](../../../../01-users/personas/u03-sales.md): the technologies of the sites they follow, before a call.

## Purpose

See which technologies a competitor's or prospect's public site runs, and how sure the detection is.

## Entry points

Competitive analysis › Technology detection; a competitor's or a prospect's record › Technologies.

## Wireframe

```text
+---------------------------------------------------------------------------------------------+
| Technology detection: northwind.example       Detected 2026-11-14       [Detect again] [Compare] |
|---------------------------------------------------------------------------------------------|
| CATEGORY    TECHNOLOGY        CONFIDENCE  EVIDENCE                      STATE      [Confirm]    |
| Shop        Shop platform A   Sure        home page, generator tag      Seen       [Reject]     |
| Analytics   Analytics tool B  Probable    script address on 4 pages     Seen                    |
| Chat        Chat widget C     Possible    one script, also used by D    Seen                    |
| Payment     Payment tool E    Sure        checkout page link            Gone since 2026-08      |
+---------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F17-08 step 4, U03 | desktop | ![FL-F17-08 step 4, U03, light](../../images/08-ads-pages-search-and-tech/u03-sales/4-tech-detection-desktop-light.png) | ![FL-F17-08 step 4, U03, dark](../../images/08-ads-pages-search-and-tech/u03-sales/4-tech-detection-desktop-dark.png) |
| FL-F17-08 step 4, U03 | phone | ![FL-F17-08 step 4, U03, light](../../images/08-ads-pages-search-and-tech/u03-sales/4-tech-detection-phone-light.png) | ![FL-F17-08 step 4, U03, dark](../../images/08-ads-pages-search-and-tech/u03-sales/4-tech-detection-phone-dark.png) |
| FL-F17-08 step 4, U03 | tablet | ![FL-F17-08 step 4, U03, light](../../images/08-ads-pages-search-and-tech/u03-sales/4-tech-detection-tablet-light.png) | ![FL-F17-08 step 4, U03, dark](../../images/08-ads-pages-search-and-tech/u03-sales/4-tech-detection-tablet-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f17-28-tech-detection-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f17-28-tech-detection-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f17-28-tech-detection-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f17-28-tech-detection-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f17-28-tech-detection-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f17-28-tech-detection-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f17-28-tech-detection-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f17-28-tech-detection-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Site | E-F17-24 site | link | by sales | yes |
| Category and technology | E-F17-24 category, technology | text | by sales (corrections) | yes |
| Confidence | E-F17-24 confidence | sure, probable, possible | no | yes |
| Evidence | E-F17-24 page, mark | text | no | yes |
| First and last seen | E-F17-24 dates | two dates | no | yes |
| State | E-F17-24 state | badge | by sales | yes |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Detect again | header | sales | reads the public pages again within the rules |
| Confirm or reject | row | sales | the finding is confirmed or rejected, with the reason |
| Add by hand | header | sales | a technology learned from the customer, marked as stated |
| Compare | header | sales | a grid of the technologies of several sites |

## States

- Normal: the technologies of the site by category with their confidence and evidence.
- Empty: No detection yet, with Detect technologies and the pages that will be read.
- Loading: the headings and the table as placeholders; the values follow.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); a blocked read
  or a forbidden site shows the reason and what was not read.
- Read-only: the record in a locked state: values shown, no action offered.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-F17-24 Technology record](../../data/e-f17-24-technology-record.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F17-24 Technology record | Seen | Badge "Seen"; a new record starts here; next: Confirmed, Rejected or Gone (UC-F17-29); fields editable within the role | U03 | `u03-sales/s-f17-28-tech-detection-e-f17-24-technology-record-seen-{desktop,phone,tablet}-{light,dark}.png` |
| E-F17-24 Technology record | Confirmed | Badge "Confirmed"; next: Gone (UC-F17-29); fields editable within the role | U03 | `u03-sales/s-f17-28-tech-detection-e-f17-24-technology-record-confirmed-{desktop,phone,tablet}-{light,dark}.png` |
| E-F17-24 Technology record | Rejected | Badge "Rejected"; final: read-only, no next state; the history shows how it got here | U03 | `u03-sales/s-f17-28-tech-detection-e-f17-24-technology-record-rejected-{desktop,phone,tablet}-{light,dark}.png` |
| E-F17-24 Technology record | Gone | Badge "Gone"; next: Seen (UC-F17-29); fields editable within the role | U03 | `u03-sales/s-f17-28-tech-detection-e-f17-24-technology-record-gone-{desktop,phone,tablet}-{light,dark}.png` |

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

⬅️ [S-F17-27 Search overlap](s-f17-27-search-overlap.md) · ⬆️ [Up](README.md) ·
➡️ [S-F17-L01 Competitors](../00-lists/s-f17-l01-competitors.md)
