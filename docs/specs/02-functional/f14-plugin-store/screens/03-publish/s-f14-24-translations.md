🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🧰 [F14 Plugin store](../../README.md) › 🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-F14-03 Publish](README.md) ›
🖥️ S-F14-24 Translations

# 🖥️ S-F14-24 Translations

**Status:** ✅ specified

## Personas

- [U46 Plugin publisher](../../../../01-users/personas/u46-plugin-publisher.md)

## Purpose

Add and keep the listing's and plugin's texts in other languages.

## Entry points

The publisher portal's listing, "Translations".

## Wireframe

```text
Gate Booking, translations                         [Add language] [Import]
-------------------------------------------------------------------------------
Language   Source     Status       Texts
English    original   published    12 of 12
French     human      published    12 of 12
German     machine    outdated     11 of 12   [Review]
-------------------------------------------------------------------------------
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F14-03 step 6, U46 | desktop | ![FL-F14-03 step 6, U46, light](../../images/03-publish/u46-plugin-publisher/6-translations-desktop-light.png) | ![FL-F14-03 step 6, U46, dark](../../images/03-publish/u46-plugin-publisher/6-translations-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f14-24-translations-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f14-24-translations-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f14-24-translations-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f14-24-translations-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f14-24-translations-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f14-24-translations-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f14-24-translations-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f14-24-translations-offline-desktop-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Language | E-F14-18 language | name | yes | yes |
| Source | E-F14-18 source | human, machine | no | yes |
| Status | E-F14-18 status | draft, published, outdated | no | yes |
| Texts | E-F14-18 texts | count translated | yes | yes |

## Actions

| Action | Where | Who | Result |
|---|---|---|---|
| Add language | header | publisher | draft created |
| Import | header | publisher | file read, unknown keys listed |
| Machine translate | language row | publisher | draft marked machine translated |
| Publish | language row | publisher | published with the next version |

## States

- Normal: each language with its source, status and completeness.
- Empty: "English only": shown before a first translation, with "Add language".
- Loading: the frame and titles show at once with placeholder rows for the languages; within 1 second (D408) the data
  replaces them, and a longer load shows a progress line saying what loads.
- Error: an import file with unknown keys, listed.
- Read-only: published translations of a past version are read-only.
- Offline: not available offline: publishing is done in the portal. D38 keeps only today's schedule, time and
  intervention records offline. A banner says the connection is lost; what is on screen stays visible, every action is
  disabled and nothing is queued until the connection is back.

Shown entities (VD-15): none; no flow's Entities and screens table names an entity on this screen.

## Responsive behaviour

Desktop.

## Accessibility

Keyboard order follows the reading order; every control has a visible label; amounts, states and icons are also given as
text; status changes are announced to screen readers.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-12 File upload](../../../../04-ux/design-system/components/c-12-file-upload.md)
- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)
- [C-10 Empty state](../../../../04-ux/design-system/components/c-10-empty-state.md)

## Shown in

- [FL-F14-03 Publish](../../flows/fl-f14-03-publish.md)

## Open questions

None.

---

⬅️ [S-F14-23 Release channels](../06-release-channels-and-rollback/s-f14-23-release-channels.md) · ⬆️ [Up](README.md) ·
➡️ [S-F14-25 Support terms](../02-buy-and-licence/s-f14-25-support-terms.md)
