🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) › 🎙️ [F4 Meetings](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-F4-11 Insights and accessibility](README.md) › 🖥️ S-F4-18 Topics

# 🖥️ S-F4-18 Topics

**Status:** ✅ specified

## Personas

- [U13 Owner](../../../../01-users/personas/u13-owner.md)
- [U02 Manager](../../../../01-users/personas/u02-manager.md)
- [U03 Sales](../../../../01-users/personas/u03-sales.md)

## Purpose

Show what many calls say together: objections, competitors, requests and themes, with their trend.

## Entry points

Meetings › Topics; the weekly digest.

## Wireframe

```text
+------------------------------------------------------------------+
| Topics   [Last quarter v] [Sales calls v] [Team v]               |
| Topic                 Kind        Calls   Trend                  |
| Price objection       objection   42      +30 %                  |
| Competitor X          competitor  18      +5 %   [To F17]        |
| Offline mode          request     11      new    [To F25]        |
| > Price objection: "too expensive for 3 users" (Meeting 812 14:32)|
+------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F4-11 step 1, U13 | desktop | ![FL-F4-11 step 1, U13, light](../../images/11-insights-and-accessibility/u13-owner/1-topics-desktop-light.png) | ![FL-F4-11 step 1, U13, dark](../../images/11-insights-and-accessibility/u13-owner/1-topics-desktop-dark.png) |
| FL-F4-11 step 1, U13 | phone | ![FL-F4-11 step 1, U13, light](../../images/11-insights-and-accessibility/u13-owner/1-topics-phone-light.png) | ![FL-F4-11 step 1, U13, dark](../../images/11-insights-and-accessibility/u13-owner/1-topics-phone-dark.png) |
| Error E1, U13 | desktop | ![Error E1, U13, light](../../images/11-insights-and-accessibility/u13-owner/e1-topics-refused-desktop-light.png) | ![Error E1, U13, dark](../../images/11-insights-and-accessibility/u13-owner/e1-topics-refused-desktop-dark.png) |
| Error E1, U13 | phone | ![Error E1, U13, light](../../images/11-insights-and-accessibility/u13-owner/e1-topics-refused-phone-light.png) | ![Error E1, U13, dark](../../images/11-insights-and-accessibility/u13-owner/e1-topics-refused-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f04-18-topics-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f04-18-topics-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f04-18-topics-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f04-18-topics-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f04-18-topics-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f04-18-topics-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f04-18-topics-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f04-18-topics-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Editable |
|---|---|---|
| Topic, kind, count, trend, passages | E-F4-13 | no |

## Actions

| Action | Who | Result |
|---|---|---|
| Open | readers | Quoted passages |
| Send to F17 or F25 | owner, managers | Item created there |

## States

- Normal: show what many calls say together: objections, competitors, requests and themes, with their trend.
- Empty: fewer than 10 checked calls: "Not enough calls for trends yet".
- Loading: skeleton rows in place of the list ([C-03](../../../../04-ux/design-system/components/c-03-data-table.md));
  actions disabled until it has loaded.
- Error: the error message pattern (D122).
- Read-only: always: topics are computed.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md)); the app shows that it is offline and reloads the
  screen when the network is back.

Shown entities (VD-15): [E-F4-01 Meeting](../../data/e-f04-01-meeting.md),
[E-F4-13 Call topic](../../data/e-f04-13-call-topic.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F4-01 Meeting | Planned | Badge "Planned"; a new record starts here; next: Live (UC-F4-01); fields editable within the role | U13 | `u13-owner/s-f04-18-topics-e-f04-01-meeting-planned-{desktop,phone}-{light,dark}.png` |
| E-F4-01 Meeting | Live | Badge "Live"; next: Ended (UC-F4-02); fields editable within the role | U13 | `u13-owner/s-f04-18-topics-e-f04-01-meeting-live-{desktop,phone}-{light,dark}.png` |
| E-F4-01 Meeting | Ended | Badge "Ended"; next: Waiting for review (UC-F4-01); fields editable within the role | U13 | `u13-owner/s-f04-18-topics-e-f04-01-meeting-ended-{desktop,phone}-{light,dark}.png` |
| E-F4-01 Meeting | Waiting for review | Badge "Waiting for review"; next: Checked (UC-F4-05); fields editable within the role | U13 | `u13-owner/s-f04-18-topics-e-f04-01-meeting-waiting-for-review-{desktop,phone}-{light,dark}.png` |
| E-F4-01 Meeting | Checked | Badge "Checked"; final: read-only, no next state; the history shows how it got here | U13 | `u13-owner/s-f04-18-topics-e-f04-01-meeting-checked-{desktop,phone}-{light,dark}.png` |
| E-F4-13 Call topic | Recorded | Badge "Recorded"; a new record starts here; no other state; fields editable within the role | U02, U03, U13 | `u02-manager/s-f04-18-topics-e-f04-13-call-topic-recorded-{desktop,phone}-{light,dark}.png`, `u03-sales/s-f04-18-topics-e-f04-13-call-topic-recorded-{desktop,phone,tablet}-{light,dark}.png`, `u13-owner/s-f04-18-topics-e-f04-13-call-topic-recorded-{desktop,phone}-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop and tablet.

## Accessibility

Every status is a word, not only a colour; tables have headers; actions are buttons with labels.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-09 Chart](../../../../04-ux/design-system/components/c-09-chart.md)
- [C-01 Button](../../../../04-ux/design-system/components/c-01-button.md)

## Shown in

- [FL-F4-11 Insights and accessibility](../../flows/fl-f04-11-insights-and-accessibility.md)

## Open questions

None.

---

⬅️ [S-F4-17 Call routing](../10-benchmark-additions/s-f04-17-call-routing.md) · ⬆️ [Up](README.md) ·
➡️ [S-F4-19 Room booking](../12-rooms-and-client-video/s-f04-19-room-booking.md)
