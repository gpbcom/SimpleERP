🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🌐 [F18 Hosted websites and domains (hosted edition)](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F18-06 Content and search](README.md) › 🖥️ S-F18-25 Sector templates

# 🖥️ S-F18-25 Sector templates

**Status:** ✅ specified

## Personas

- [U13 Owner](../../../../01-users/personas/u13-owner.md)
- [U12 Marketing and communication](../../../../01-users/personas/u12-marketing.md)

## Purpose

Add the pages of the sector's template, filled from the ERP with the sector's mandatory information.

## Entry points

Site builder, Pages, "From your sector".

## Wireframe

```text
Sector templates: Restaurants (SC06)
-------------------------------------------------------------------------------
Page            Filled from         Mandatory            State
Menu            recipes, prices     allergens            held: 1 dish missing
Opening hours   sites (F1)          -                    ready
Booking         booking (F2)        -                    ready
-------------------------------------------------------------------------------
[Add pages]
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F18-06 step 2, U13 | desktop | ![FL-F18-06 step 2, U13, light](../../images/06-content-and-search/u13-owner/2-sector-templates-desktop-light.png) | ![FL-F18-06 step 2, U13, dark](../../images/06-content-and-search/u13-owner/2-sector-templates-desktop-dark.png) |
| FL-F18-06 step 2, U13 | phone | ![FL-F18-06 step 2, U13, light](../../images/06-content-and-search/u13-owner/2-sector-templates-phone-light.png) | ![FL-F18-06 step 2, U13, dark](../../images/06-content-and-search/u13-owner/2-sector-templates-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f18-25-sector-templates-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f18-25-sector-templates-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f18-25-sector-templates-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f18-25-sector-templates-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f18-25-sector-templates-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f18-25-sector-templates-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f18-25-sector-templates-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f18-25-sector-templates-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Page | E-F18-17 pages | name | no | yes |
| Filled from | E-F18-17 | ERP data | no | yes |
| Mandatory | E-F18-17 mandatory | rules | no | yes |
| State | E-F18-02 | ready, held | no | yes |

## Actions

| Action | Where | Who | Result |
|---|---|---|---|
| Add pages | footer | owner, marketing | pages on the preview |
| Open missing | row | owner, marketing | the ERP records to complete |

## States

- Normal: the sector's template pages with their state.
- Empty: "No template for your sector yet": general pages only.
- Loading: the frame and titles show at once with placeholder rows for the template pages; within 1 second (D408) the
  data replaces them, and a longer load shows a progress line saying what loads.
- Error: mandatory information missing, listed per page.
- Read-only: content comes from the ERP; change it there.
- Offline: not available offline: the builder works online. D38 keeps only today's schedule, time and intervention
  records offline. A banner says the connection is lost; what is on screen stays visible, every action is disabled and
  nothing is queued until the connection is back.

Shown entities (VD-15): [E-F18-17 Sector template](../../data/e-f18-17-sector-template.md),
[E-F18-02 Page](../../data/e-f18-02-page.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F18-17 Sector template | Published | Badge "Published"; a new record starts here; next: Updated (UC-F18-25); fields editable within the role | U12, U13 | `u12-marketing/s-f18-25-sector-templates-e-f18-17-sector-template-published-{desktop,phone}-{light,dark}.png`, `u13-owner/s-f18-25-sector-templates-e-f18-17-sector-template-published-{desktop,phone}-{light,dark}.png` |
| E-F18-17 Sector template | Updated | Badge "Updated"; next: Published (UC-F18-25); fields editable within the role | U12, U13 | `u12-marketing/s-f18-25-sector-templates-e-f18-17-sector-template-updated-{desktop,phone}-{light,dark}.png`, `u13-owner/s-f18-25-sector-templates-e-f18-17-sector-template-updated-{desktop,phone}-{light,dark}.png` |
| E-F18-02 Page | Published | Badge "Published"; a new record starts here; next: Live (UC-F18-08); fields editable within the role | U12, U13 | `u12-marketing/s-f18-25-sector-templates-e-f18-02-page-published-{desktop,phone}-{light,dark}.png`, `u13-owner/s-f18-25-sector-templates-e-f18-02-page-published-{desktop,phone}-{light,dark}.png` |
| E-F18-02 Page | Live | Badge "Live"; next: Held (UC-F18-25); fields editable within the role | U12, U13 | `u12-marketing/s-f18-25-sector-templates-e-f18-02-page-live-{desktop,phone}-{light,dark}.png`, `u13-owner/s-f18-25-sector-templates-e-f18-02-page-live-{desktop,phone}-{light,dark}.png` |
| E-F18-02 Page | Held | Badge "Held"; next: Live (UC-F18-08); fields editable within the role | U12, U13 | `u12-marketing/s-f18-25-sector-templates-e-f18-02-page-held-{desktop,phone}-{light,dark}.png`, `u13-owner/s-f18-25-sector-templates-e-f18-02-page-held-{desktop,phone}-{light,dark}.png` |

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
- [C-04 Card](../../../../04-ux/design-system/components/c-04-card.md)
- [C-10 Empty state](../../../../04-ux/design-system/components/c-10-empty-state.md)

## Shown in

- [FL-F18-06 Content and search](../../flows/fl-f18-06-content-and-search.md)

## Open questions

None.

---

⬅️ [S-F18-24 Form protection](../01-build-the-site/s-f18-24-form-protection.md) · ⬆️ [Up](README.md) ·
➡️ [S-F18-26 Search basics](s-f18-26-search-basics.md)
