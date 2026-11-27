🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🌐 [F18 Hosted websites and domains (hosted edition)](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F18-06 Content and search](README.md) › 🖥️ S-F18-26 Search basics

# 🖥️ S-F18-26 Search basics

**Status:** ✅ specified

## Personas

- [U12 Marketing and communication](../../../../01-users/personas/u12-marketing.md)

## Purpose

Review and edit titles, descriptions, the sitemap and structured data.

## Entry points

Site builder, Search.

## Wireframe

```text
Search basics           Sitemap: 12 pages (1 not indexed)     Last check: passed
-------------------------------------------------------------------------------
Page        Title (60)                 Description (160)            Indexed
/           Bistro Lyon, local food    Seasonal cooking in ...       yes
/menu       Winter menu                Our dishes and allergens ...  yes
/thank-you  -                          -                             no
-------------------------------------------------------------------------------
Structured data: organisation, opening hours, menu, job postings
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F18-06 step 3, U12 | desktop | ![FL-F18-06 step 3, U12, light](../../images/06-content-and-search/u12-marketing/3-search-basics-desktop-light.png) | ![FL-F18-06 step 3, U12, dark](../../images/06-content-and-search/u12-marketing/3-search-basics-desktop-dark.png) |
| FL-F18-06 step 3, U12 | phone | ![FL-F18-06 step 3, U12, light](../../images/06-content-and-search/u12-marketing/3-search-basics-phone-light.png) | ![FL-F18-06 step 3, U12, dark](../../images/06-content-and-search/u12-marketing/3-search-basics-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f18-26-search-basics-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f18-26-search-basics-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f18-26-search-basics-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f18-26-search-basics-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f18-26-search-basics-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f18-26-search-basics-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f18-26-search-basics-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f18-26-search-basics-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Title | E-F18-18 titles | text | yes | yes |
| Description | E-F18-18 descriptions | text | yes | yes |
| Indexed | E-F18-18 not indexed | yes, no | yes | yes |
| Structured data | E-F18-18 structured data | list | no | yes |

## Actions

| Action | Where | Who | Result |
|---|---|---|---|
| Edit | row | marketing | title or description saved |
| Propose | row | marketing | AI assistant proposes a title |
| Validate | header | marketing | checks run |

## States

- Normal: pages with titles, descriptions and indexing, and the structured data kinds.
- Empty: "No page yet".
- Loading: the frame and titles show at once with placeholder rows for the pages; within 1 second (D408) the data
  replaces them, and a longer load shows a progress line saying what loads.
- Error: invalid structured data with the field, or a title too long.
- Read-only: generated values are shown until edited.
- Offline: not available offline: validation runs online. D38 keeps only today's schedule, time and intervention records
  offline. A banner says the connection is lost; what is on screen stays visible, every action is disabled and nothing
  is queued until the connection is back.

Shown entities (VD-15): [E-F18-18 Search settings](../../data/e-f18-18-search-settings.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F18-18 Search settings | Generated | Badge "Generated"; a new record starts here; next: Edited (UC-F18-26); fields editable within the role | U12 | `u12-marketing/s-f18-26-search-basics-e-f18-18-search-settings-generated-{desktop,phone}-{light,dark}.png` |
| E-F18-18 Search settings | Edited | Badge "Edited"; next: Generated (UC-F18-26); fields editable within the role | U12 | `u12-marketing/s-f18-26-search-basics-e-f18-18-search-settings-edited-{desktop,phone}-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop.

## Accessibility

Keyboard order follows the reading order; every control has a visible label; amounts, states and icons are also given as
text; status changes are announced to screen readers.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)
- [C-10 Empty state](../../../../04-ux/design-system/components/c-10-empty-state.md)

## Shown in

- [FL-F18-06 Content and search](../../flows/fl-f18-06-content-and-search.md)

## Open questions

None.

---

⬅️ [S-F18-25 Sector templates](s-f18-25-sector-templates.md) · ⬆️ [Up](README.md) ·
➡️ [S-F18-27 Backups](../05-run-the-site/s-f18-27-backups.md)
