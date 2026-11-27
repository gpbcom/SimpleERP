🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) › 🎙️ [F4 Meetings](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-F4-11 Insights and accessibility](README.md) ›
🖥️ S-F4-20 Transcription accuracy

# 🖥️ S-F4-20 Transcription accuracy

**Status:** ✅ specified

## Personas

- [U07 Administrator](../../../../01-users/personas/u07-administrator.md)

## Purpose

Compare transcription accuracy per language and model.

## Entry points

Meeting settings › Accuracy.

## Wireframe

```text
+------------------------------------------------------------------+
| Transcription accuracy   [Last 3 months v]                       |
| Language  Model               Meetings  Words right  Trend       |
| French    local speech model  120       96 %         stable      |
| Spanish   local speech model  34        87 %  below  -2 pts      |
| German    -                   8         not enough data          |
|                                   [Test another model]           |
+------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F4-11 step 3, U07 | desktop | ![FL-F4-11 step 3, U07, light](../../images/11-insights-and-accessibility/u07-administrator/3-transcription-accuracy-desktop-light.png) | ![FL-F4-11 step 3, U07, dark](../../images/11-insights-and-accessibility/u07-administrator/3-transcription-accuracy-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f04-20-transcription-accuracy-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f04-20-transcription-accuracy-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f04-20-transcription-accuracy-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f04-20-transcription-accuracy-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f04-20-transcription-accuracy-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f04-20-transcription-accuracy-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f04-20-transcription-accuracy-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f04-20-transcription-accuracy-offline-desktop-dark.png) |

## Fields and columns

| Label | Data | Editable |
|---|---|---|
| Language, model, meetings, words right | E-F4-15 | no |

## Actions

| Action | Who | Result |
|---|---|---|
| Test another model | administrator | Sample meetings run on it |

## States

- Normal: compare transcription accuracy per language and model.
- Empty: no reviewed meeting yet: "Accuracy shows once meetings are reviewed".
- Loading: skeleton rows in place of the list ([C-03](../../../../04-ux/design-system/components/c-03-data-table.md));
  actions disabled until it has loaded.
- Error: the error message pattern (D122).
- Read-only: always: figures are computed.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md)); the app shows that it is offline and reloads the
  screen when the network is back.

Shown entities (VD-15): [E-F4-15 Accuracy measure](../../data/e-f04-15-accuracy-measure.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F4-15 Accuracy measure | Recorded | Badge "Recorded"; a new record starts here; no other state; fields editable within the role | U07 | `u07-administrator/s-f04-20-transcription-accuracy-e-f04-15-accuracy-measure-recorded-desktop-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop.

## Accessibility

Every status is a word, not only a colour; tables have headers; actions are buttons with labels.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-09 Chart](../../../../04-ux/design-system/components/c-09-chart.md)

## Shown in

- [FL-F4-11 Insights and accessibility](../../flows/fl-f04-11-insights-and-accessibility.md)

## Open questions

None.

---

⬅️ [S-F4-19 Room booking](../12-rooms-and-client-video/s-f04-19-room-booking.md) · ⬆️ [Up](README.md) ·
➡️ [S-F4-21 Client video meeting](../12-rooms-and-client-video/s-f04-21-client-video-meeting.md)
