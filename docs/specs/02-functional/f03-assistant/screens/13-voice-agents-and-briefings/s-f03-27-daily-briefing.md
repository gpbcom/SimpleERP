🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) › 🤖 [F3 Assistant](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-F3-13 Voice, agents and briefings](README.md) › 🖥️ S-F3-27 Daily briefing

# 🖥️ S-F3-27 Daily briefing

**Status:** ✅ specified

## Personas

- - [U13 Owner](../../../../01-users/personas/u13-owner.md): their briefing, on a phone.
- - [U02 Manager](../../../../01-users/personas/u02-manager.md): their briefing and their team's.

## Purpose

Read the day's briefing, open its items and choose its sections, time and channel.

## Entry points

Home › Briefing; the notification or email of the briefing; Assistant settings › Briefing.

## Wireframe

```text
+---------------------------------------------------------------------------------------------+
| Daily briefing   Sat 14 Nov 2026      07:30   [Settings]                                    |
| ------------------------------------------------------------------------------------------- |
| TODAY  3 meetings: 09:00 Dupont, 11:00 team, 15:00 supplier           (Meetings)            |
| NEEDS YOU  2 approvals: leave Sonia M., purchase order 118            (Approvals)           |
| MONEY  5 invoices overdue, 12,400 EUR                                  Source: invoices     |
| STOCK  3 items under their minimum                                     [Done] [Snooze] [Not useful] |
+---------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F3-13 step 4, U13 | phone | ![FL-F3-13 step 4, U13, light](../../images/13-voice-agents-and-briefings/u13-owner/4-daily-briefing-phone-light.png) | ![FL-F3-13 step 4, U13, dark](../../images/13-voice-agents-and-briefings/u13-owner/4-daily-briefing-phone-dark.png) |
| FL-F3-13 step 4, U13 | desktop | ![FL-F3-13 step 4, U13, light](../../images/13-voice-agents-and-briefings/u13-owner/4-daily-briefing-desktop-light.png) | ![FL-F3-13 step 4, U13, dark](../../images/13-voice-agents-and-briefings/u13-owner/4-daily-briefing-desktop-dark.png) |
| FL-F3-13 step 4, U13 | phone | ![FL-F3-13 step 4, U13, light](../../images/13-voice-agents-and-briefings/u13-owner/4-daily-briefing-phone-light.png) | ![FL-F3-13 step 4, U13, dark](../../images/13-voice-agents-and-briefings/u13-owner/4-daily-briefing-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f03-27-daily-briefing-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f03-27-daily-briefing-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f03-27-daily-briefing-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f03-27-daily-briefing-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f03-27-daily-briefing-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f03-27-daily-briefing-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f03-27-daily-briefing-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f03-27-daily-briefing-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Section | E-F3-26 sections | headline | choose in settings | yes |
| Item | E-F3-26 items | text with its source | mark only | yes |
| Source | link to the record or query | link | no | yes |
| Time and channel | E-F3-26 delivery | time, app or email or chat | yes | yes |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Open an item | item | the reader | the record opens |
| Done, Snooze, Not useful | item | the reader | the item is marked and tunes the next briefing |
| Settings | header | the reader | sections, time and channel |
| Ask about this | item | the reader | the AI assistant panel opens on the item |

## States

- Normal: the sections of the day with their items and sources.
- Empty: Nothing needs you today.
- Loading: The headline shows first, the sections follow.
- Error: the error message pattern (D122); a missing section is named and the others show.
- Read-only: a briefing of a past day: its items, without marking.
- Offline: The last briefing downloaded is readable; items open when the network is back.

Shown entities (VD-15): [E-F3-26 Briefing](../../data/e-f03-26-briefing.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F3-26 Briefing | Planned | Badge "Planned"; a new record starts here; next: Generated or Skipped (UC-F3-23); fields editable within the role | U13, U02 | `u13-owner/s-f03-27-daily-briefing-e-f03-26-briefing-planned-{desktop,phone}-{light,dark}.png`, `u02-manager/s-f03-27-daily-briefing-e-f03-26-briefing-planned-{desktop,phone}-{light,dark}.png` |
| E-F3-26 Briefing | Generated | Badge "Generated"; next: Delivered or Failed (UC-F3-23); fields editable within the role | U13, U02 | `u13-owner/s-f03-27-daily-briefing-e-f03-26-briefing-generated-{desktop,phone}-{light,dark}.png`, `u02-manager/s-f03-27-daily-briefing-e-f03-26-briefing-generated-{desktop,phone}-{light,dark}.png` |
| E-F3-26 Briefing | Skipped | Badge "Skipped"; final: read-only, no next state; the history shows how it got here | U13, U02 | `u13-owner/s-f03-27-daily-briefing-e-f03-26-briefing-skipped-{desktop,phone}-{light,dark}.png`, `u02-manager/s-f03-27-daily-briefing-e-f03-26-briefing-skipped-{desktop,phone}-{light,dark}.png` |
| E-F3-26 Briefing | Delivered | Badge "Delivered"; next: Read (UC-F3-23); fields editable within the role | U13, U02 | `u13-owner/s-f03-27-daily-briefing-e-f03-26-briefing-delivered-{desktop,phone}-{light,dark}.png`, `u02-manager/s-f03-27-daily-briefing-e-f03-26-briefing-delivered-{desktop,phone}-{light,dark}.png` |
| E-F3-26 Briefing | Failed | Badge "Failed"; next: Delivered (UC-F3-23); fields editable within the role | U13, U02 | `u13-owner/s-f03-27-daily-briefing-e-f03-26-briefing-failed-{desktop,phone}-{light,dark}.png`, `u02-manager/s-f03-27-daily-briefing-e-f03-26-briefing-failed-{desktop,phone}-{light,dark}.png` |
| E-F3-26 Briefing | Read | Badge "Read"; final: read-only, no next state; the history shows how it got here | U13, U02 | `u13-owner/s-f03-27-daily-briefing-e-f03-26-briefing-read-{desktop,phone}-{light,dark}.png`, `u02-manager/s-f03-27-daily-briefing-e-f03-26-briefing-read-{desktop,phone}-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

On a phone, this is the main screen; on a desktop the same texts show in the AI assistant panel.

## Accessibility

Each section is a heading; the figures are text with their units; keyboard: next item, open, done.

## Components

- [C-01 Button](../../../../04-ux/design-system/components/c-01-button.md)
- [C-14 Timeline](../../../../04-ux/design-system/components/c-14-timeline.md)
- [C-16 KPI strip](../../../../04-ux/design-system/components/c-16-kpi-strip.md)
- [C-11 Chat panel](../../../../04-ux/design-system/components/c-11-chat-panel.md)

## Shown in

- [FL-F3-13 Voice, agents and briefings](../../flows/fl-f03-13-voice-agents-and-briefings.md)

## Open questions

None.

---

⬅️ [S-F3-26 Spreadsheet add-in](s-f03-26-spreadsheet-add-in.md) · ⬆️ [Up](README.md) ·
➡️ [S-F3-28 My to-dos](s-f03-28-my-to-dos.md)
