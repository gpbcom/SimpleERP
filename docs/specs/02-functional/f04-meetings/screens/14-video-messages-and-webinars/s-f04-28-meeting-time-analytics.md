🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) › 🎙️ [F4 Meetings](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-F4-14 Video messages, webinars and templates](README.md) ›
🖥️ S-F4-28 Meeting time analytics

# 🖥️ S-F4-28 Meeting time analytics

**Status:** ✅ specified

## Personas

- - [U02 Manager](../../../../01-users/personas/u02-manager.md): their teams.
- - [U13 Owner](../../../../01-users/personas/u13-owner.md): the whole company.

## Purpose

See the time spent in meetings by group, kind and series, with small groups protected.

## Entry points

Meetings › Meeting time; the AI assistant ("how much time do we spend in meetings?").

## Wireframe

```text
+---------------------------------------------------------------------------------------------+
| Meeting time        Period: Q3 2026   By: team   [Compare with Q2] [Export]                 |
| ------------------------------------------------------------------------------------------- |
| TEAM        PEOPLE   HOURS / WEEK / PERSON   MEETINGS   RECURRING   WITH OUTSIDERS          |
| Sales       11       6.4                     212        58 %        41 %                    |
| Support     8        4.1                     130        72 %        19 %                    |
| Other groups (groups under 5 people are not shown separately)        5.0                    |
| TOP SERIES  Weekly sales meeting  45 min  11 people  61 % produced actions                  |
+---------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F4-14 step 4, U02 | desktop | ![FL-F4-14 step 4, U02, light](../../images/14-video-messages-and-webinars/u02-manager/4-meeting-time-analytics-desktop-light.png) | ![FL-F4-14 step 4, U02, dark](../../images/14-video-messages-and-webinars/u02-manager/4-meeting-time-analytics-desktop-dark.png) |
| FL-F4-14 step 4, U02 | desktop | ![FL-F4-14 step 4, U02, light](../../images/14-video-messages-and-webinars/u02-manager/4-meeting-time-analytics-desktop-light.png) | ![FL-F4-14 step 4, U02, dark](../../images/14-video-messages-and-webinars/u02-manager/4-meeting-time-analytics-desktop-dark.png) |
| FL-F4-14 step 4, U02 | phone | ![FL-F4-14 step 4, U02, light](../../images/14-video-messages-and-webinars/u02-manager/4-meeting-time-analytics-phone-light.png) | ![FL-F4-14 step 4, U02, dark](../../images/14-video-messages-and-webinars/u02-manager/4-meeting-time-analytics-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f04-28-meeting-time-analytics-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f04-28-meeting-time-analytics-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f04-28-meeting-time-analytics-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f04-28-meeting-time-analytics-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f04-28-meeting-time-analytics-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f04-28-meeting-time-analytics-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f04-28-meeting-time-analytics-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f04-28-meeting-time-analytics-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Group | team, site or kind | text | choose | yes |
| People | number of people in the group | number | no | yes |
| Hours per week per person | computed | number | no | yes |
| Recurring, with outsiders | computed | percent | no | yes |
| Series | recurring meetings | name, length, frequency, attendees | no | no |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Compare | header | the reader | two periods side by side |
| Open a series | series list | the reader | its length, frequency and actions |
| Export | header | the reader | the figures shown, with the group minimum applied |
| Pin chart | chart | the reader | the chart appears on the home screen |

## States

- Normal: the groups with their figures, the line Other groups, the top series and the chart.
- Empty: No meeting in this period.
- Loading: The groups appear as they are computed.
- Error: the error message pattern (D122); all groups under five people show the total and the reason.
- Read-only: a past period: the figures, without the live comparison.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): none; no flow's Entities and screens table names an entity on this
screen.

## Responsive behaviour

Desktop; on a phone, the groups and the chart can be read, the series list scrolls sideways.

## Accessibility

Charts have a table with the same figures; the reason a group is hidden is text; keyboard: next group, open series.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-09 Chart](../../../../04-ux/design-system/components/c-09-chart.md)
- [C-16 KPI strip](../../../../04-ux/design-system/components/c-16-kpi-strip.md)
- [C-01 Button](../../../../04-ux/design-system/components/c-01-button.md)

## Shown in

- [FL-F4-14 Video messages, webinars and templates](../../flows/fl-f04-14-video-messages-and-webinars.md)

## Open questions

None.

---

⬅️ [S-F4-27 Note templates](s-f04-27-note-templates.md) · ⬆️ [Up](README.md) ·
➡️ [S-F4-L01 Meetings](../00-lists/s-f04-l01-meetings.md)
