🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) › 🎙️ [F4 Meetings](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-F4-06 Set up meetings and calendars](README.md) ›
🖥️ S-F4-07 Meeting settings

# 🖥️ S-F4-07 Meeting settings

**Status:** ✅ specified

## Personas

- [U07 Administrator](../../../../01-users/personas/u07-administrator.md)

## Purpose

Connect meeting sources and calendars; set retention (UC-F4-08).

## Entry points

Administration › Meetings.

## Wireframe

```text
+------------------------------------------------------------------+
| Meetings                                               [Save]     |
| Calendars   Google Workspace  connected, 48 calendars in sync     |
|             Microsoft 365     [Connect]                           |
| Platforms   Teams Meet Zoom Webex [on] Jitsi BBB [off] |
| Phone       3CX  connected                                        |
| Recordings  keep [7 days v] after the meeting unless checked      |
| Summaries   templates: Site meeting, Sales call, HR review [Edit] |
+------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F4-06 step 1, U07 | desktop | ![FL-F4-06 step 1, U07, light](../../images/06-set-up-meetings-and-calendars/u07-administrator/1-sources-calendars-retention-desktop-light.png) | ![FL-F4-06 step 1, U07, dark](../../images/06-set-up-meetings-and-calendars/u07-administrator/1-sources-calendars-retention-desktop-dark.png) |
| Error E1, U07 | desktop | ![Error E1, U07, light](../../images/06-set-up-meetings-and-calendars/u07-administrator/e1-platform-refused-desktop-light.png) | ![Error E1, U07, dark](../../images/06-set-up-meetings-and-calendars/u07-administrator/e1-platform-refused-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f04-07-meeting-settings-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f04-07-meeting-settings-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f04-07-meeting-settings-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f04-07-meeting-settings-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f04-07-meeting-settings-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f04-07-meeting-settings-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f04-07-meeting-settings-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f04-07-meeting-settings-offline-desktop-dark.png) |

## Fields and columns

Calendar connections with sync state; platforms (Teams, Meet, Zoom, Webex, Jitsi, BigBlueButton); phone system and
softphone (D236); recording mode (audio and video, audio only, transcript only); custom vocabulary (company terms,
product names, per team); the bot's display name, fixed as "SimpleERP recorder" and shown
read-only ([BR-F4-01](../../business-rules/br-f04-01-every-recording-is-announced.md)); an administrator lock on
recording settings; retention; summary templates; scoring of candidates on or off (BR-F4-21).

## Actions

| Action | Who | Result |
|---|---|---|
| Connect | administrator | Sign-in at the provider |
| Save | administrator | Applied |

## States

- Normal: Connect meeting sources and calendars; set retention (UC-F4-08), as the wireframe shows.
- Empty: No source or calendar connected, with Connect.
- Loading: placeholders in the layout of the wireframe; actions are disabled until the record has loaded.
- Error: a refused connection (D122).
- Read-only: for users other than administrators.
- Offline: Not available offline: a back-office screen on live, shared data (D38: only today's schedule, time and
  intervention records work offline). The app shows that it is offline and reloads the screen when the network is back.
- Connected, not connected, failing.

Shown entities (VD-15): [E-F4-05 Calendar sync](../../data/e-f04-05-calendar-sync.md),
[E-F4-25 Meeting recording setting](../../data/e-f04-25-meeting-recording-setting.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F4-05 Calendar sync | In sync | Badge "In sync"; a new record starts here; next: To reconnect or Failing (UC-F4-08); fields editable within the role | U07 | `u07-administrator/s-f04-07-meeting-settings-e-f04-05-calendar-sync-in-sync-desktop-{light,dark}.png` |
| E-F4-05 Calendar sync | To reconnect | Badge "To reconnect"; next: In sync (UC-F4-08); fields editable within the role | U07 | `u07-administrator/s-f04-07-meeting-settings-e-f04-05-calendar-sync-to-reconnect-desktop-{light,dark}.png` |
| E-F4-05 Calendar sync | Failing | Badge "Failing"; next: In sync (UC-F4-08); fields editable within the role | U07 | `u07-administrator/s-f04-07-meeting-settings-e-f04-05-calendar-sync-failing-desktop-{light,dark}.png` |
| E-F4-25 Meeting recording setting | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U07 | `u07-administrator/s-f04-07-meeting-settings-e-f04-25-meeting-recording-setting-active-desktop-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop.

## Accessibility

Labelled switches; sync state as text.

## Components

- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)
- [C-04 Card](../../../../04-ux/design-system/components/c-04-card.md)

## Shown in

- [FL-F4-06 Set up meetings and calendars](../../flows/fl-f04-06-set-up-meetings-and-calendars.md)

## Open questions

None.

---

⬅️ [S-F4-06 Meetings](../04-find-and-reuse-meetings/s-f04-06-meetings.md) · ⬆️ [Up](README.md) ·
➡️ [S-F4-08 Meeting prep brief](../07-prepare-and-capture-anywhere/s-f04-08-meeting-prep-brief.md)
