🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) › 🎙️ [F4 Meetings](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-F4-01 Record an online meeting](README.md) › 🖥️ S-F4-01 Meeting

# 🖥️ S-F4-01 Meeting

**Status:** ✅ specified

## Personas

- [U02 Manager](../../../../01-users/personas/u02-manager.md)
- [U03 Sales](../../../../01-users/personas/u03-sales.md)
- [U13 Owner](../../../../01-users/personas/u13-owner.md)
- Any internal participant (D218)

## Purpose

A meeting's record: recording switch and source, then transcript, summary, decisions and actions.

## Entry points

Meetings in the menu; a calendar event; a linked record's Meetings tab.

## Wireframe

```text
+------------------------------------------------------------------+
| Durand SA, kitchen project      Tue 10 Nov 14:00 · Teams          |
| Recording [on]   Source (o) Bot  ( ) Teams transcript             |
| Linked to: [Durand SA] [Project Kitchen 2027]                     |
|------------------------------------------------------------------|
| [Summary] [Transcript] [Decisions and actions]                    |
| ...                                                               |
+------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F4-01 step 1, U02 | desktop | ![FL-F4-01 step 1, U02, light](../../images/01-record-an-online-meeting/u02-manager/1-recording-on-desktop-light.png) | ![FL-F4-01 step 1, U02, dark](../../images/01-record-an-online-meeting/u02-manager/1-recording-on-desktop-dark.png) |
| FL-F4-01 step 1, U02 | phone | ![FL-F4-01 step 1, U02, light](../../images/01-record-an-online-meeting/u02-manager/1-recording-on-phone-light.png) | ![FL-F4-01 step 1, U02, dark](../../images/01-record-an-online-meeting/u02-manager/1-recording-on-phone-dark.png) |
| Error E3, U02 | desktop | ![Error E3, U02, light](../../images/01-record-an-online-meeting/u02-manager/e3-connection-dropped-desktop-light.png) | ![Error E3, U02, dark](../../images/01-record-an-online-meeting/u02-manager/e3-connection-dropped-desktop-dark.png) |
| Error E3, U02 | phone | ![Error E3, U02, light](../../images/01-record-an-online-meeting/u02-manager/e3-connection-dropped-phone-light.png) | ![Error E3, U02, dark](../../images/01-record-an-online-meeting/u02-manager/e3-connection-dropped-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f04-01-meeting-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f04-01-meeting-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f04-01-meeting-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f04-01-meeting-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f04-01-meeting-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f04-01-meeting-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f04-01-meeting-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f04-01-meeting-offline-phone-dark.png) |

## Fields and columns

As [E-F4-01 Meeting](../../data/e-f04-01-meeting.md#fields).

## Actions

| Action | Who | Result |
|---|---|---|
| Recording on or off | any internal participant | BR-F4-06, BR-F4-08 |
| Source | organiser | BR-F4-07 |
| Send the bot now | any internal participant | The bot joins |

## States

- Normal: A meeting's record: recording switch and source, then transcript, summary, decisions and actions, as the
  wireframe shows.
- Empty: a planned meeting with no recording yet, with Start recording.
- Loading: placeholders in the layout of the wireframe; actions are disabled until the record has loaded.
- Error: bot refused, no transcript (D122).
- Read-only: a checked meeting for users who were not its organiser.
- Offline: Works offline only when recorded on the phone
  ([D220](../../../../06-decisions/f04-meetings/d220-offline-recording.md)); the record itself waits for the network.
- Planned, live, ended, waiting for review, checked.

Shown entities (VD-15): [E-F4-01 Meeting](../../data/e-f04-01-meeting.md),
[E-F4-18 Recording notice](../../data/e-f04-18-recording-notice.md),
[E-F4-02 Transcript](../../data/e-f04-02-transcript.md),
[E-F4-17 Meeting summary](../../data/e-f04-17-meeting-summary.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F4-01 Meeting | Planned | Badge "Planned"; a new record starts here; next: Live (UC-F4-01); fields editable within the role | U01, U02, U03, U06, U13 | `u01-employee/s-f04-01-meeting-e-f04-01-meeting-planned-{desktop,phone}-{light,dark}.png`, `u02-manager/s-f04-01-meeting-e-f04-01-meeting-planned-{desktop,phone}-{light,dark}.png`, `u03-sales/s-f04-01-meeting-e-f04-01-meeting-planned-{desktop,phone,tablet}-{light,dark}.png`, `u06-hr/s-f04-01-meeting-e-f04-01-meeting-planned-desktop-{light,dark}.png`, `u13-owner/s-f04-01-meeting-e-f04-01-meeting-planned-{desktop,phone}-{light,dark}.png` |
| E-F4-01 Meeting | Ended | Badge "Ended"; next: Waiting for review (UC-F4-01); fields editable within the role | U02, U03, U13 | `u02-manager/s-f04-01-meeting-e-f04-01-meeting-ended-{desktop,phone}-{light,dark}.png`, `u03-sales/s-f04-01-meeting-e-f04-01-meeting-ended-{desktop,phone,tablet}-{light,dark}.png`, `u13-owner/s-f04-01-meeting-e-f04-01-meeting-ended-{desktop,phone}-{light,dark}.png` |
| E-F4-01 Meeting | Waiting for review | Badge "Waiting for review"; next: Checked (UC-F4-05); fields editable within the role | U02, U03, U13 | `u02-manager/s-f04-01-meeting-e-f04-01-meeting-waiting-for-review-{desktop,phone}-{light,dark}.png`, `u03-sales/s-f04-01-meeting-e-f04-01-meeting-waiting-for-review-{desktop,phone,tablet}-{light,dark}.png`, `u13-owner/s-f04-01-meeting-e-f04-01-meeting-waiting-for-review-{desktop,phone}-{light,dark}.png` |
| E-F4-18 Recording notice | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U02, U03, U13 | `u02-manager/s-f04-01-meeting-e-f04-18-recording-notice-active-{desktop,phone}-{light,dark}.png`, `u03-sales/s-f04-01-meeting-e-f04-18-recording-notice-active-{desktop,phone,tablet}-{light,dark}.png`, `u13-owner/s-f04-01-meeting-e-f04-18-recording-notice-active-{desktop,phone}-{light,dark}.png` |
| E-F4-02 Transcript | Live | Badge "Live"; a new record starts here; next: Complete (BR-F4-03); fields editable within the role | U01, U02, U06 | `u01-employee/s-f04-01-meeting-e-f04-02-transcript-live-{desktop,phone}-{light,dark}.png`, `u02-manager/s-f04-01-meeting-e-f04-02-transcript-live-{desktop,phone}-{light,dark}.png`, `u06-hr/s-f04-01-meeting-e-f04-02-transcript-live-desktop-{light,dark}.png` |
| E-F4-02 Transcript | Complete | Badge "Complete"; next: Checked (BR-F4-03); fields editable within the role | U01, U02, U06 | `u01-employee/s-f04-01-meeting-e-f04-02-transcript-complete-{desktop,phone}-{light,dark}.png`, `u02-manager/s-f04-01-meeting-e-f04-02-transcript-complete-{desktop,phone}-{light,dark}.png`, `u06-hr/s-f04-01-meeting-e-f04-02-transcript-complete-desktop-{light,dark}.png` |
| E-F4-02 Transcript | Checked | Badge "Checked"; final: read-only, no next state; the history shows how it got here | U01, U02, U06 | `u01-employee/s-f04-01-meeting-e-f04-02-transcript-checked-{desktop,phone}-{light,dark}.png`, `u02-manager/s-f04-01-meeting-e-f04-02-transcript-checked-{desktop,phone}-{light,dark}.png`, `u06-hr/s-f04-01-meeting-e-f04-02-transcript-checked-desktop-{light,dark}.png` |
| E-F4-17 Meeting summary | Draft | Badge "Draft"; a new record starts here; next: Published or Not checked (UC-F4-05, BR-F4-15); fields editable within the role | U01, U02, U06 | `u01-employee/s-f04-01-meeting-e-f04-17-meeting-summary-draft-{desktop,phone}-{light,dark}.png`, `u02-manager/s-f04-01-meeting-e-f04-17-meeting-summary-draft-{desktop,phone}-{light,dark}.png`, `u06-hr/s-f04-01-meeting-e-f04-17-meeting-summary-draft-desktop-{light,dark}.png` |
| E-F4-17 Meeting summary | Published | Badge "Published"; final: read-only, no next state; the history shows how it got here | U01, U02, U06 | `u01-employee/s-f04-01-meeting-e-f04-17-meeting-summary-published-{desktop,phone}-{light,dark}.png`, `u02-manager/s-f04-01-meeting-e-f04-17-meeting-summary-published-{desktop,phone}-{light,dark}.png`, `u06-hr/s-f04-01-meeting-e-f04-17-meeting-summary-published-desktop-{light,dark}.png` |
| E-F4-17 Meeting summary | Not checked | Badge "Not checked"; final: read-only, no next state; the history shows how it got here | U01, U02, U06 | `u01-employee/s-f04-01-meeting-e-f04-17-meeting-summary-not-checked-{desktop,phone}-{light,dark}.png`, `u02-manager/s-f04-01-meeting-e-f04-17-meeting-summary-not-checked-{desktop,phone}-{light,dark}.png`, `u06-hr/s-f04-01-meeting-e-f04-17-meeting-summary-not-checked-desktop-{light,dark}.png` |
| E-F4-01 Meeting | Checked | Badge "Checked"; final: read-only, no next state; the history shows how it got here | U02, U03, U13 | `u02-manager/s-f04-01-meeting-e-f04-01-meeting-checked-{desktop,phone}-{light,dark}.png`, `u03-sales/s-f04-01-meeting-e-f04-01-meeting-checked-{desktop,phone,tablet}-{light,dark}.png`, `u13-owner/s-f04-01-meeting-e-f04-01-meeting-checked-{desktop,phone}-{light,dark}.png` |
| E-F4-01 Meeting | Live | Badge "Live"; next: Ended (UC-F4-02); fields editable within the role | U02, U03, U13 | `u02-manager/s-f04-01-meeting-e-f04-01-meeting-live-{desktop,phone}-{light,dark}.png`, `u03-sales/s-f04-01-meeting-e-f04-01-meeting-live-{desktop,phone,tablet}-{light,dark}.png`, `u13-owner/s-f04-01-meeting-e-f04-01-meeting-live-{desktop,phone}-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop and phone.

## Accessibility

Tabs and switches labelled.

## Components

- [C-07 Tabs](../../../../04-ux/design-system/components/c-07-tabs.md)
- [C-04 Card](../../../../04-ux/design-system/components/c-04-card.md)

## Shown in

- [FL-F4-01 Record an online meeting](../../flows/fl-f04-01-record-an-online-meeting.md)

## Open questions

None.

---

⬆️ [Up](README.md) · ➡️ [S-F4-02 Live transcript](s-f04-02-live-transcript.md)
