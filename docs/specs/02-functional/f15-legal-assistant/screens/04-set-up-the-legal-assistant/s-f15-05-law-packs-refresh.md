🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
⚖️ [F15 Legal assistant](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F15-04 Set up the legal assistant](README.md) › 🖥️ S-F15-05 Law packs refresh

# 🖥️ S-F15-05 Law packs refresh

**Status:** ✅ specified

## Personas

- [U07 Administrator](../../../../01-users/personas/u07-administrator.md)

## Purpose

Show each official source of the installed law packs, its last pull, what changed and the country rules flagged.

## Entry points

Legal assistant settings, "Law packs"; the monthly digest; the "source unreachable" notification.

## Wireframe

```text
Law packs, France                                  Last full refresh 2026-11-12 03:10
-------------------------------------------------------------------------------
Source                    Schedule   Last pull          Changes   State
Légifrance codes          daily      2026-11-12 03:00   4         ok
Collective agreements     weekly     2026-11-10 03:00   1         ok
Service-public pages      weekly     2026-11-09 03:00   0         unreachable 1 day
-------------------------------------------------------------------------------
Changes: L3141-3 new version from 2026-11-01   flags CR-FR-044      [Open]
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F15-04 step 3, U07 | desktop | ![FL-F15-04 step 3, U07, light](../../images/04-set-up-the-legal-assistant/u07-administrator/3-law-packs-refresh-desktop-light.png) | ![FL-F15-04 step 3, U07, dark](../../images/04-set-up-the-legal-assistant/u07-administrator/3-law-packs-refresh-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f15-05-law-packs-refresh-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f15-05-law-packs-refresh-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f15-05-law-packs-refresh-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f15-05-law-packs-refresh-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f15-05-law-packs-refresh-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f15-05-law-packs-refresh-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f15-05-law-packs-refresh-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f15-05-law-packs-refresh-offline-desktop-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Source | E-F15-01 source | name | no | yes |
| Schedule | E-F15-01 pull schedule | daily, weekly | no | yes |
| Last pull | E-F15-01 last pull | date and time | no | yes |
| Changes | computed | count and list | no | no |
| Rules flagged | country-pack rules | IDs | no | no |

## Actions

| Action | Where | Who | Result |
|---|---|---|---|
| Open a change | changes list | administrator | the article's old and new versions side by side |
| Open a flagged rule | changes list | administrator | the country rule page |

## States

- Normal: each source with its schedule, last pull and changes, and the list of changes with the rules they flag.
- Empty: "No change since the last pull": shown when every source is up to date.
- Loading: the frame and titles show at once with placeholder rows for the sources; within 1 second (D408) the data
  replaces them, and a longer load shows a progress line saying what loads.
- Error: a source unreachable for a day: a banner, the last copy used.
- Read-only: always read-only: pulls run with no human validation (BR-F15-09).
- Offline: not available offline: pulls run on the server. D38 keeps only today's schedule, time and intervention
  records offline. A banner says the connection is lost; what is on screen stays visible, every action is disabled and
  nothing is queued until the connection is back.

Shown entities (VD-15): [E-F15-01 Law pack](../../data/e-f15-01-law-pack.md),
[E-F15-12 Legal source](../../data/e-f15-12-legal-source.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F15-01 Law pack | Scheduled | Badge "Scheduled"; a new record starts here; no other state; fields editable within the role | U07 | `u07-administrator/s-f15-05-law-packs-refresh-e-f15-01-law-pack-scheduled-desktop-{light,dark}.png` |
| E-F15-12 Legal source | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U07 | `u07-administrator/s-f15-05-law-packs-refresh-e-f15-12-legal-source-active-desktop-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop; tablet in one column.

## Accessibility

Keyboard order follows the reading order; every control has a visible label; amounts, states and icons are also given as
text; status changes are announced to screen readers.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-14 Timeline](../../../../04-ux/design-system/components/c-14-timeline.md)
- [C-10 Empty state](../../../../04-ux/design-system/components/c-10-empty-state.md)

## Shown in

- [FL-F15-04 Set up the legal assistant](../../flows/fl-f15-04-set-up-the-legal-assistant.md)

## Open questions

None.

---

⬅️ [S-F15-04 Legal assistant settings](s-f15-04-legal-assistant-settings.md) · ⬆️ [Up](README.md) ·
➡️ [S-F15-06 Standards register](s-f15-06-standards-register.md)
