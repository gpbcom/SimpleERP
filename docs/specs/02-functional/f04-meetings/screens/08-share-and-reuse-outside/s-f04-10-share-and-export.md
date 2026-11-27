🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) › 🎙️ [F4 Meetings](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-F4-08 Share and reuse outside](README.md) › 🖥️ S-F4-10 Share and export

# 🖥️ S-F4-10 Share and export

**Status:** ✅ specified

## Personas

See its use case.

## Purpose

Share and export a meeting (UC-F4-11).

## Entry points

Share on the meeting.

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F4-08 step 1, U03 | desktop | ![FL-F4-08 step 1, U03, light](../../images/08-share-and-reuse-outside/u03-sales/1-share-and-export-desktop-light.png) | ![FL-F4-08 step 1, U03, dark](../../images/08-share-and-reuse-outside/u03-sales/1-share-and-export-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f04-10-share-and-export-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f04-10-share-and-export-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f04-10-share-and-export-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f04-10-share-and-export-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f04-10-share-and-export-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f04-10-share-and-export-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f04-10-share-and-export-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f04-10-share-and-export-offline-phone-dark.png) |

## Fields and columns

Formats, channels, key moments, clips, chapters.

## Actions

As its use case's main flow.

## States

- Normal: Share and export a meeting (UC-F4-11), as the wireframe shows.
- Empty: not shared yet: only the participants see the meeting.
- Loading: skeleton rows in place of the list ([C-03](../../../../04-ux/design-system/components/c-03-data-table.md));
  actions are disabled until it has loaded.
- Error: the error message pattern (D122).
- Read-only: a share link's settings for non-owners.
- Offline: Not available offline (D38): on a phone or a computer, the offline banner replaces the actions and nothing is
  changed until the network is back; nothing is queued.

Shown entities (VD-15): none; no flow's Entities and screens table names an entity on this screen.

## Responsive behaviour

Desktop; phone where the use case says so.

## Accessibility

Labelled controls; scores and states as text, never colour alone.

## Components

- [C-04 Card](../../../../04-ux/design-system/components/c-04-card.md)
- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)

## Shown in

- [FL-F4-08 Share and reuse outside](../../flows/fl-f04-08-share-and-reuse-outside.md)

## Open questions

None.

---

⬅️ [S-F4-09 Desktop recorder](../07-prepare-and-capture-anywhere/s-f04-09-desktop-recorder.md) · ⬆️ [Up](README.md) ·
➡️ [S-F4-11 Call scorecard](../09-score-calls-and-interviews/s-f04-11-call-scorecard.md)
