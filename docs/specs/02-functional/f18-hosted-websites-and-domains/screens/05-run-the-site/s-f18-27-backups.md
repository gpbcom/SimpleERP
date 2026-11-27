🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🌐 [F18 Hosted websites and domains (hosted edition)](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F18-05 Run the site](README.md) › 🖥️ S-F18-27 Backups

# 🖥️ S-F18-27 Backups

**Status:** ✅ specified

## Personas

- [U13 Owner](../../../../01-users/personas/u13-owner.md)
- [U48 Hosting engineer](../../../../01-users/personas/u48-hosting-engineer.md)

## Purpose

Show the site's daily backups and restore one to the preview.

## Entry points

Site settings, Backups; site health.

## Wireframe

```text
Backups of restaurant site            Kept 30 days
-------------------------------------------------------------------------------
Date                Size
2026-11-12 03:00    84 MB    [Restore to preview]
2026-11-11 03:00    84 MB    [Restore to preview]
-------------------------------------------------------------------------------
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F18-05 step 3, U13 | desktop | ![FL-F18-05 step 3, U13, light](../../images/05-run-the-site/u13-owner/3-backups-desktop-light.png) | ![FL-F18-05 step 3, U13, dark](../../images/05-run-the-site/u13-owner/3-backups-desktop-dark.png) |
| FL-F18-05 step 3, U13 | phone | ![FL-F18-05 step 3, U13, light](../../images/05-run-the-site/u13-owner/3-backups-phone-light.png) | ![FL-F18-05 step 3, U13, dark](../../images/05-run-the-site/u13-owner/3-backups-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f18-27-backups-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f18-27-backups-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f18-27-backups-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f18-27-backups-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f18-27-backups-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f18-27-backups-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f18-27-backups-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f18-27-backups-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Date | E-F18-19 taken | date and time | no | yes |
| Size | E-F18-19 size | MB | no | yes |
| Expires | E-F18-19 expires | date | no | yes |

## Actions

| Action | Where | Who | Result |
|---|---|---|---|
| Restore to preview | row | owner, hosting engineer on request | preview replaced by the backup |

## States

- Normal: daily backups with size and expiry.
- Empty: "No backup yet": the first runs tonight.
- Loading: the frame and titles show at once with placeholder rows for the backups; within 1 second (D408) the data
  replaces them, and a longer load shows a progress line saying what loads.
- Error: an expired backup, not offered.
- Read-only: marketing reads; only the owner restores.
- Offline: not available offline: backups are on the server. D38 keeps only today's schedule, time and intervention
  records offline. A banner says the connection is lost; what is on screen stays visible, every action is disabled and
  nothing is queued until the connection is back.

Shown entities (VD-15): none; no flow's Entities and screens table names an entity on this screen.

## Responsive behaviour

Desktop.

## Accessibility

Keyboard order follows the reading order; every control has a visible label; amounts, states and icons are also given as
text; status changes are announced to screen readers.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-05 Modal](../../../../04-ux/design-system/components/c-05-modal.md)
- [C-10 Empty state](../../../../04-ux/design-system/components/c-10-empty-state.md)

## Shown in

- [FL-F18-05 Run the site](../../flows/fl-f18-05-run-the-site.md)

## Open questions

None.

---

⬅️ [S-F18-26 Search basics](../06-content-and-search/s-f18-26-search-basics.md) · ⬆️ [Up](README.md) ·
➡️ [S-F18-28 Page A/B test](../07-tests-visitors-and-accessibility/s-f18-28-page-ab-test.md)
