🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) › 🤖 [F3 Assistant](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-F3-13 Voice, agents and briefings](README.md) › 🖥️ S-F3-24 Voice mode

# 🖥️ S-F3-24 Voice mode

**Status:** ✅ specified

## Personas

- - [U14 Field worker](../../../../01-users/personas/u14-field-worker.md): on a site or on the road.
- - [U13 Owner](../../../../01-users/personas/u13-owner.md): on the move.

## Purpose

Speak to the AI assistant, hear the answer, and confirm an action aloud.

## Entry points

The phone app › AI assistant › microphone; the wake word when the company enabled it.

## Wireframe

```text
+---------------------------------------------------------------------------------------------+
| Voice mode                                                          [Stop]                  |
| ------------------------------------------------------------------------------------------- |
| You said: Create a visit report for Dupont tomorrow at nine                                 |
| Assistant: I will create a visit report for Dupont tomorrow at 9:00.                        |
|            Say confirm or cancel.                                                           |
| (( listening ))                                       [Confirm] [Cancel] [Type instead]     |
+---------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F3-13 step 1, U14 | phone | ![FL-F3-13 step 1, U14, light](../../images/13-voice-agents-and-briefings/u14-field-worker/1-voice-mode-phone-light.png) | ![FL-F3-13 step 1, U14, dark](../../images/13-voice-agents-and-briefings/u14-field-worker/1-voice-mode-phone-dark.png) |
| FL-F3-13 step 1, U14 | phone | ![FL-F3-13 step 1, U14, light](../../images/13-voice-agents-and-briefings/u14-field-worker/1-voice-mode-phone-light.png) | ![FL-F3-13 step 1, U14, dark](../../images/13-voice-agents-and-briefings/u14-field-worker/1-voice-mode-phone-dark.png) |
| Error E1, U14 | phone | ![Error E1, U14, light](../../images/13-voice-agents-and-briefings/u14-field-worker/e1-the-voice-is-not-understood-phone-light.png) | ![Error E1, U14, dark](../../images/13-voice-agents-and-briefings/u14-field-worker/e1-the-voice-is-not-understood-phone-dark.png) |
| Empty | phone | ![Empty, light](../../images/states/s-f03-24-voice-mode-empty-phone-light.png) | ![Empty, dark](../../images/states/s-f03-24-voice-mode-empty-phone-dark.png) |
| Loading | phone | ![Loading, light](../../images/states/s-f03-24-voice-mode-loading-phone-light.png) | ![Loading, dark](../../images/states/s-f03-24-voice-mode-loading-phone-dark.png) |
| Read-only | phone | ![Read-only, light](../../images/states/s-f03-24-voice-mode-read-only-phone-light.png) | ![Read-only, dark](../../images/states/s-f03-24-voice-mode-read-only-phone-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f03-24-voice-mode-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f03-24-voice-mode-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| You said | E-F3-01 the user's turn | text | yes, before confirming | yes |
| Answer | E-F3-02 the AI assistant's answer | text and speech | no | yes |
| Read-back | the prepared action | text and speech | no | for an action |
| Listening | microphone state | icon and word | no | yes |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Confirm | read-back | the user | the action is saved (BR-F3-43) |
| Cancel | read-back | the user | nothing is saved |
| Type instead | footer | the user | the keyboard opens with the same text |
| Stop | header | the user | voice mode ends |

## States

- Normal: what was heard, the answer, and the read-back with the Confirm and Cancel buttons.
- Empty: Tap the microphone and speak. Try: What is on my schedule this afternoon?
- Loading: Listening and thinking are shown by word and icon, not by sound only.
- Error: the error message pattern (D122); a sentence not understood is shown with what was heard.
- Read-only: voice mode switched off by the administrator: the typed AI assistant stays.
- Offline: The question waits for the network
  ([BR-F3-29](../../business-rules/br-f03-29-offline-questions-wait-for-the-network.md)); the screen says it is offline
  and speaks it once.

Shown entities (VD-15): none; no flow's Entities and screens table names an entity on this
screen.

## Responsive behaviour

On a phone, this is the main screen; on a desktop the same texts show in the AI assistant panel.

## Accessibility

Everything said is also on screen; the confirmation can be tapped; captions of the spoken answer follow the text size;
keyboard: confirm, cancel.

## Components

- [C-01 Button](../../../../04-ux/design-system/components/c-01-button.md)
- [C-14 Timeline](../../../../04-ux/design-system/components/c-14-timeline.md)
- [C-11 Chat panel](../../../../04-ux/design-system/components/c-11-chat-panel.md)

## Shown in

- [FL-F3-13 Voice, agents and briefings](../../flows/fl-f03-13-voice-agents-and-briefings.md)

## Open questions

None.

---

⬅️ [S-F3-23 Unanswered topics](../12-personal-cost-aware-and-learning/s-f03-23-unanswered-topics.md) ·
⬆️ [Up](README.md) · ➡️ [S-F3-25 Agent catalogue](s-f03-25-agent-catalogue.md)
