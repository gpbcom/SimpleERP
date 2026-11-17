🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) › 🤖 [F3 Assistant](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-F3-09 Assistant on a phone](README.md) › 🖥️ S-F3-11 Phone assistant

# 🖥️ S-F3-11 Phone assistant

**Status:** ✅ specified

## Personas

- [U14 Field worker](../../../../01-users/personas/u14-field-worker.md)
- [U01 Employee](../../../../01-users/personas/u01-employee.md)
- Every internal persona using a phone (D34)

## Purpose

The AI assistant on a phone: voice, photos, offline queue (D181 to D184).

## Entry points

The Assistant tab of the phone app; the AI assistant button on a task or visit.

## Wireframe

```text
+------------------------------+
| < Assistant        [hands-free]|
| [About: Visit V-212, today x]|
|------------------------------|
| You: what did we fit last    |
| time?                        |
| On 3 Sept: boiler valve,     |
| ref. VX-20 [visit V-180]     |
|------------------------------|
| [camera]   ( MIC )   [type]  |
|------------------------------|
| Today | Tasks | Assist | Me  |
+------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F3-09 step 1, U14 | phone | ![FL-F3-09 step 1, U14, light](../../images/09-assistant-on-a-phone/u14-field-worker/1-ask-by-voice-phone-light.png) | ![FL-F3-09 step 1, U14, dark](../../images/09-assistant-on-a-phone/u14-field-worker/1-ask-by-voice-phone-dark.png) |
| Error E1, U14 | phone | ![Error E1, U14, light](../../images/09-assistant-on-a-phone/u14-field-worker/e1-speech-not-understood-phone-light.png) | ![Error E1, U14, dark](../../images/09-assistant-on-a-phone/u14-field-worker/e1-speech-not-understood-phone-dark.png) |
| Error E2, U14 | phone | ![Error E2, U14, light](../../images/09-assistant-on-a-phone/u14-field-worker/e2-photo-not-readable-phone-light.png) | ![Error E2, U14, dark](../../images/09-assistant-on-a-phone/u14-field-worker/e2-photo-not-readable-phone-dark.png) |
| Error E3, U14 | phone | ![Error E3, U14, light](../../images/09-assistant-on-a-phone/u14-field-worker/e3-queued-failed-phone-light.png) | ![Error E3, U14, dark](../../images/09-assistant-on-a-phone/u14-field-worker/e3-queued-failed-phone-dark.png) |
| Empty | phone | ![Empty, light](../../images/states/s-f03-11-phone-assistant-empty-phone-light.png) | ![Empty, dark](../../images/states/s-f03-11-phone-assistant-empty-phone-dark.png) |
| Loading | phone | ![Loading, light](../../images/states/s-f03-11-phone-assistant-loading-phone-light.png) | ![Loading, dark](../../images/states/s-f03-11-phone-assistant-loading-phone-dark.png) |
| Read-only | phone | ![Read-only, light](../../images/states/s-f03-11-phone-assistant-read-only-phone-light.png) | ![Read-only, dark](../../images/states/s-f03-11-phone-assistant-read-only-phone-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f03-11-phone-assistant-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f03-11-phone-assistant-offline-phone-dark.png) |

## Fields and columns

Context chip; conversation; camera, microphone, keyboard; hands-free switch.

## Actions

| Action | Who | Result |
|---|---|---|
| Microphone | the user | Speech to question |
| Camera | the user | Photo read |
| Hands-free | the user | Answers and confirmations aloud |
| Remove chip | the user | No context |

## States

- Normal: The AI assistant on a phone: voice, photos, offline queue (D181 to D184), as the wireframe shows.
- Empty: no question yet: the microphone button and three suggestions for the task at hand.
- Loading: placeholders in the layout of the wireframe; actions are disabled until the record has loaded.
- Error: the error message pattern (D122).
- Read-only: answers already given.
- Offline: Works offline with a banner: questions are queued and answered when the network is back,
  [BR-F3-29](../../business-rules/br-f03-29-offline-questions-wait-for-the-network.md),
  [D182](../../../../06-decisions/f03-assistant/d182-offline-assistant.md); offline task screens work as usual (D38).
- Online, offline (a banner "Offline: your question will be answered when you are back online").
- Listening, reading a photo, answering.
- Queued questions with their status.

Shown entities (VD-15): none; no flow's Entities and screens table names an entity on this screen.

## Responsive behaviour

Phone, 390 x 844 and up (D121).

## Accessibility

The microphone button is 64 px; hands-free helps users who cannot type; every action has a text label for screen
readers.

## Components

- [C-11 Chat panel](../../../../04-ux/design-system/components/c-11-chat-panel.md)
- [C-12 File upload](../../../../04-ux/design-system/components/c-12-file-upload.md)
- [C-08 Navigation](../../../../04-ux/design-system/components/c-08-navigation.md)

## Shown in

- [FL-F3-09 Assistant on a phone](../../flows/fl-f03-09-assistant-on-a-phone.md)

## Open questions

None.

---

⬅️ [S-F3-10 Share a conversation](../08-manage-and-share-conversations/s-f03-10-share-a-conversation.md) ·
⬆️ [Up](README.md) · ➡️ [S-F3-12 Assistant settings](../03-act-through-the-assistant/s-f03-12-assistant-settings.md)
