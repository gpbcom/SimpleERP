🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) › 🎙️ [F4 Meetings](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-F4-01 Record an online meeting](README.md) › 🖥️ S-F4-02 Live transcript

# 🖥️ S-F4-02 Live transcript

**Status:** ✅ specified

## Personas

- Any internal participant (D218)

## Purpose

Follow the meeting as it is spoken, and ask the AI assistant about it (D219).

## Entry points

The meeting record while it is live; a notification "Meeting being recorded".

## Wireframe

```text
+-------------------------------------------+
| (o) LIVE  Durand SA, kitchen project      |
| 14:12 Léa Moreau: so we agree on 1,240... |
| 14:12 J. Durand: yes, 1,240 works.        |
| [Mark as decision] [Mark as action]       |
|-------------------------------------------|
| [Ask about this meeting...]               |
+-------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F4-01 step 2, U02 | desktop | ![FL-F4-01 step 2, U02, light](../../images/01-record-an-online-meeting/u02-manager/2-live-transcript-desktop-light.png) | ![FL-F4-01 step 2, U02, dark](../../images/01-record-an-online-meeting/u02-manager/2-live-transcript-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f04-02-live-transcript-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f04-02-live-transcript-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f04-02-live-transcript-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f04-02-live-transcript-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f04-02-live-transcript-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f04-02-live-transcript-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f04-02-live-transcript-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f04-02-live-transcript-offline-phone-dark.png) |

## Fields and columns

Time, speaker, text; the AI assistant's answers with their passages.

## Actions

| Action | Who | Result |
|---|---|---|
| Ask about this meeting | participant | Answer at 70 % confidence or more |
| Mark a moment | participant | A decision or action to review |
| Stop recording | anyone | Stopped |

## States

- Normal: Follow the meeting as it is spoken, and ask the AI assistant about it (D219), as the wireframe shows.
- Empty: nothing spoken yet: "Waiting for the first words."
- Loading: placeholders in the layout of the wireframe; actions are disabled until the record has loaded.
- Error: the error message pattern (D122).
- Read-only: always: the live transcript is not edited while it runs.
- Offline: Not available offline (D38): on a phone or a computer, the offline banner replaces the actions and nothing is
  changed until the network is back; nothing is queued.
- Live, paused, stopped.
- The AI assistant not sure (under 70 %).

Shown entities (VD-15): [E-F4-01 Meeting](../../data/e-f04-01-meeting.md),
[E-F4-18 Recording notice](../../data/e-f04-18-recording-notice.md),
[E-F4-02 Transcript](../../data/e-f04-02-transcript.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F4-01 Meeting | Planned | Badge "Planned"; a new record starts here; next: Live (UC-F4-01); fields editable within the role | U02, U03 | `u02-manager/s-f04-02-live-transcript-e-f04-01-meeting-planned-{desktop,phone}-{light,dark}.png`, `u03-sales/s-f04-02-live-transcript-e-f04-01-meeting-planned-{desktop,phone,tablet}-{light,dark}.png` |
| E-F4-01 Meeting | Live | Badge "Live"; next: Ended (UC-F4-02); fields editable within the role | U02, U03 | `u02-manager/s-f04-02-live-transcript-e-f04-01-meeting-live-{desktop,phone}-{light,dark}.png`, `u03-sales/s-f04-02-live-transcript-e-f04-01-meeting-live-{desktop,phone,tablet}-{light,dark}.png` |
| E-F4-01 Meeting | Ended | Badge "Ended"; next: Waiting for review (UC-F4-01); fields editable within the role | U02, U03 | `u02-manager/s-f04-02-live-transcript-e-f04-01-meeting-ended-{desktop,phone}-{light,dark}.png`, `u03-sales/s-f04-02-live-transcript-e-f04-01-meeting-ended-{desktop,phone,tablet}-{light,dark}.png` |
| E-F4-01 Meeting | Waiting for review | Badge "Waiting for review"; next: Checked (UC-F4-05); fields editable within the role | U02, U03 | `u02-manager/s-f04-02-live-transcript-e-f04-01-meeting-waiting-for-review-{desktop,phone}-{light,dark}.png`, `u03-sales/s-f04-02-live-transcript-e-f04-01-meeting-waiting-for-review-{desktop,phone,tablet}-{light,dark}.png` |
| E-F4-18 Recording notice | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U02, U03 | `u02-manager/s-f04-02-live-transcript-e-f04-18-recording-notice-active-{desktop,phone}-{light,dark}.png`, `u03-sales/s-f04-02-live-transcript-e-f04-18-recording-notice-active-{desktop,phone,tablet}-{light,dark}.png` |
| E-F4-02 Transcript | Live | Badge "Live"; a new record starts here; next: Complete (BR-F4-03); fields editable within the role | U02, U03 | `u02-manager/s-f04-02-live-transcript-e-f04-02-transcript-live-{desktop,phone}-{light,dark}.png`, `u03-sales/s-f04-02-live-transcript-e-f04-02-transcript-live-{desktop,phone,tablet}-{light,dark}.png` |
| E-F4-02 Transcript | Checked | Badge "Checked"; final: read-only, no next state; the history shows how it got here | U02, U03, U06 | `u02-manager/s-f04-02-live-transcript-e-f04-02-transcript-checked-{desktop,phone}-{light,dark}.png`, `u03-sales/s-f04-02-live-transcript-e-f04-02-transcript-checked-{desktop,phone,tablet}-{light,dark}.png`, `u06-hr/s-f04-02-live-transcript-e-f04-02-transcript-checked-desktop-{light,dark}.png` |
| E-F4-01 Meeting | Checked | Badge "Checked"; final: read-only, no next state; the history shows how it got here | U03 | `u03-sales/s-f04-02-live-transcript-e-f04-01-meeting-checked-{desktop,phone,tablet}-{light,dark}.png` |
| E-F4-02 Transcript | Complete | Badge "Complete"; next: Checked (BR-F4-03); fields editable within the role | U03 | `u03-sales/s-f04-02-live-transcript-e-f04-02-transcript-complete-{desktop,phone,tablet}-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop: beside the call; phone: full screen.

## Accessibility

New lines announced politely to screen readers; text size adjustable.

## Components

- [C-11 Chat panel](../../../../04-ux/design-system/components/c-11-chat-panel.md)
- [C-14 Timeline](../../../../04-ux/design-system/components/c-14-timeline.md)

## Shown in

- [FL-F4-01 Record an online meeting](../../flows/fl-f04-01-record-an-online-meeting.md)
- [FL-F4-11 Insights and accessibility](../../flows/fl-f04-11-insights-and-accessibility.md)

## Open questions

None.

---

⬅️ [S-F4-01 Meeting](s-f04-01-meeting.md) · ⬆️ [Up](README.md) ·
➡️ [S-F4-03 Phone recorder](../02-record-in-person-or-by-phone/s-f04-03-phone-recorder.md)
