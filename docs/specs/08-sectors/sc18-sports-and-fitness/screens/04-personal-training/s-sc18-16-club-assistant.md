🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🏋️ [SC18 Sports and fitness](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC18-04 Personal training](README.md) › 🖥️ S-SC18-16 Club AI assistant

# 🖥️ S-SC18-16 Club AI assistant

**Status:** ✅ specified

## Personas

- [U13 Owner](../../../../01-users/personas/u13-owner.md): the answers and actions within their role.

## Purpose

Ask the AI assistant about the club and confirm the actions it prepares.

## Entry points

Sports and fitness › Ask the AI assistant; the phone's home screen.

## Wireframe

```text
+--------------------------------------------------------------------------------------------------+
| Ask about the club                                                                               |
| You: Which classes are below their minimum this week?                                            |
| AI assistant: 2 classes. Cycling Tuesday 07:00 (3 of 5), Pilates Friday 12:00 (2 of 5).          |
| Sources: classes, class bookings (2 rows)                                                        |
| Prepared: tell the 5 booked members the classes are cancelled      [Confirm]  [Change]           |
| [ Type your question                                        ]                                    |
+--------------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC18-04 step 4, U13 | phone | ![FL-SC18-04 step 4, U13, light](../../images/04-personal-training/u13-owner/4-club-assistant-phone-light.png) | ![FL-SC18-04 step 4, U13, dark](../../images/04-personal-training/u13-owner/4-club-assistant-phone-dark.png) |
| FL-SC18-04 step 4, U13 | desktop | ![FL-SC18-04 step 4, U13, light](../../images/04-personal-training/u13-owner/4-club-assistant-desktop-light.png) | ![FL-SC18-04 step 4, U13, dark](../../images/04-personal-training/u13-owner/4-club-assistant-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc18-16-club-assistant-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc18-16-club-assistant-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc18-16-club-assistant-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc18-16-club-assistant-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc18-16-club-assistant-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc18-16-club-assistant-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc18-16-club-assistant-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc18-16-club-assistant-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Question | F3 question | text or voice | yes | yes |
| Answer | F3 answer | text, list or figure | no | no |
| Sources | F3 sources | list of records | no | no |
| Prepared action | F3 prepared action | action and records | yes | no |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Ask | footer | owner | an answer from the data the owner may see |
| Confirm | action | owner | the prepared action is done |
| Change | action | owner | the action is edited before it is confirmed |

## States

- Normal: the conversation with the answers, the sources and the prepared actions.
- Empty: No question yet, with examples.
- Loading: the headings and the table as placeholders; the values follow.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); an answer
  refused for rights or missing data, with the reason.
- Read-only: the record in a locked state: values shown, no action offered.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): none; no flow's Entities and screens table names an entity on this screen.

## Responsive behaviour

Phone first: one column, the sources folded.

## Accessibility

Every control is reachable by keyboard; states and errors are announced to screen readers and never rely on colour
alone; each field has its visible label.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)
- [C-01 Button](../../../../04-ux/design-system/components/c-01-button.md)

## Shown in

- [FL-SC18-04 Personal training](../../flows/fl-sc18-04-personal-training.md)

## Open questions

None.

---

⬅️ [S-SC18-15 Progress](s-sc18-15-progress.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC18-17 Court booking](../05-facilities-events-camps-and-rentals/s-sc18-17-court-booking.md)
