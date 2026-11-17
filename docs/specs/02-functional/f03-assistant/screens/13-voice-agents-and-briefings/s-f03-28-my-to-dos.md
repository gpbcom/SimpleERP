🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) › 🤖 [F3 Assistant](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-F3-13 Voice, agents and briefings](README.md) › 🖥️ S-F3-28 My to-dos

# 🖥️ S-F3-28 My to-dos

**Status:** ✅ specified

## Personas

- - [U01 Employee](../../../../01-users/personas/u01-employee.md): on a phone.
- - [U16 Office worker](../../../../01-users/personas/u16-office-worker.md): on a desktop.

## Purpose

Keep, find, tick and share a personal list of to-dos and memos.

## Entry points

Home › My to-dos; the add button on any screen; the AI assistant panel.

## Wireframe

```text
+---------------------------------------------------------------------------------------------+
| My to-dos                  [+ Add]   Today  Later  Memos  Shared with me  Done              |
| ------------------------------------------------------------------------------------------- |
| [ ] Call Dupont about the quote            Fri 20 Nov   Quote 2031   private                |
| [ ] Send the leave form                    Mon 23 Nov                private                |
| [x] Book the room for Tuesday              done                      shared with Claire P.  |
| Suggested from today's meeting: [Add 'Send the new price list'] [Add 'Invite the supplier'] |
+---------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F3-13 step 5, U01 | phone | ![FL-F3-13 step 5, U01, light](../../images/13-voice-agents-and-briefings/u01-employee/5-my-to-dos-phone-light.png) | ![FL-F3-13 step 5, U01, dark](../../images/13-voice-agents-and-briefings/u01-employee/5-my-to-dos-phone-dark.png) |
| FL-F3-13 step 5, U01 | desktop | ![FL-F3-13 step 5, U01, light](../../images/13-voice-agents-and-briefings/u01-employee/5-my-to-dos-desktop-light.png) | ![FL-F3-13 step 5, U01, dark](../../images/13-voice-agents-and-briefings/u01-employee/5-my-to-dos-desktop-dark.png) |
| FL-F3-13 step 5, U01 | phone | ![FL-F3-13 step 5, U01, light](../../images/13-voice-agents-and-briefings/u01-employee/5-my-to-dos-phone-light.png) | ![FL-F3-13 step 5, U01, dark](../../images/13-voice-agents-and-briefings/u01-employee/5-my-to-dos-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f03-28-my-to-dos-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f03-28-my-to-dos-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f03-28-my-to-dos-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f03-28-my-to-dos-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f03-28-my-to-dos-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f03-28-my-to-dos-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f03-28-my-to-dos-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f03-28-my-to-dos-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Title | E-F3-27 title | text | yes | yes |
| Due | E-F3-27 due date | date | yes | no |
| Linked record | E-F3-27 record | link | yes | no |
| Shared with | E-F3-27 shared with | list of people | yes | no |
| State | E-F3-27 state | check box | yes | yes |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Add | header | the owner | a to-do or memo is saved |
| Tick, Drop | row | the owner, a person it is shared with | the to-do is done or dropped |
| Share | row | the owner | the chosen colleagues see it (BR-F3-47) |
| Accept a suggestion | suggestions | the owner | a to-do is created |

## States

- Normal: the lists Today, Later, Memos, Shared with me and Done, with the suggestions below.
- Empty: No to-do yet. Type or say one.
- Loading: The list loads first; the suggestions follow.
- Error: the error message pattern (D122); an empty title is refused under its field.
- Read-only: the archive of done items: read only.
- Offline: To-dos can be added and ticked offline on the phone and sync when the network is back.

Shown entities (VD-15): [E-F3-27 To-do](../../data/e-f03-27-to-do.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F3-27 To-do | Open | Badge "Open"; a new record starts here; next: Done or Dropped (UC-F3-24); fields editable within the role | U01, U16 | `u01-employee/s-f03-28-my-to-dos-e-f03-27-to-do-open-{desktop,phone}-{light,dark}.png`, `u16-office-worker/s-f03-28-my-to-dos-e-f03-27-to-do-open-{desktop,phone}-{light,dark}.png` |
| E-F3-27 To-do | Done | Badge "Done"; next: Open (UC-F3-24); fields editable within the role | U01, U16 | `u01-employee/s-f03-28-my-to-dos-e-f03-27-to-do-done-{desktop,phone}-{light,dark}.png`, `u16-office-worker/s-f03-28-my-to-dos-e-f03-27-to-do-done-{desktop,phone}-{light,dark}.png` |
| E-F3-27 To-do | Dropped | Badge "Dropped"; next: Open (UC-F3-24); fields editable within the role | U01, U16 | `u01-employee/s-f03-28-my-to-dos-e-f03-27-to-do-dropped-{desktop,phone}-{light,dark}.png`, `u16-office-worker/s-f03-28-my-to-dos-e-f03-27-to-do-dropped-{desktop,phone}-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

On a phone, this is the main screen; on a desktop the same texts show in the AI assistant panel.

## Accessibility

The check box has a text label; due dates are text; keyboard: next to-do, tick, add.

## Components

- [C-01 Button](../../../../04-ux/design-system/components/c-01-button.md)
- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-14 Timeline](../../../../04-ux/design-system/components/c-14-timeline.md)
- [C-11 Chat panel](../../../../04-ux/design-system/components/c-11-chat-panel.md)

## Shown in

- [FL-F3-13 Voice, agents and briefings](../../flows/fl-f03-13-voice-agents-and-briefings.md)

## Open questions

None.

---

⬅️ [S-F3-27 Daily briefing](s-f03-27-daily-briefing.md) · ⬆️ [Up](README.md) ·
➡️ [S-F3-L01 Conversations](../00-lists/s-f03-l01-conversations.md)
