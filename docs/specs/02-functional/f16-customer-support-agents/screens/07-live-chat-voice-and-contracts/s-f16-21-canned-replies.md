🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🎧 [F16 Customer support agents](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F16-07 Forum, live chat, voice and support contracts](README.md) › 🖥️ S-F16-21 Canned replies

# 🖥️ S-F16-21 Canned replies

**Status:** ✅ specified

## Personas

- [U16 Office worker](../../../../01-users/personas/u16-office-worker.md): the replies they use, and, for a support
  lead, the library.

## Purpose

Pick, fill and send a canned reply, and keep the library of replies and their variables.

## Entry points

The request in the agent workspace › Replies; Customer support agents › Canned replies.

## Wireframe

```text
+---------------------------------------------------------------------------------------------+
| Canned replies       Intent [Late delivery v]  Language [French v]            [+ New reply]  |
|---------------------------------------------------------------------------------------------|
| REPLY             LANG  VARIABLES                         USED   STATE                      |
| Late delivery     fr    first name, order, new date       412    Active                     |
| Refund sent       fr    first name, amount, refund date   388    Active                     |
| Preview: Bonjour Julien, votre commande 4821 arrivera le  [MISSING: new date]               |
| [Fill] [Send] [Flag as wrong] [Edit] [Retire]                                               |
+---------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F16-07 step 6, U16 | desktop | ![FL-F16-07 step 6, U16, light](../../images/07-live-chat-voice-and-contracts/u16-office-worker/6-canned-replies-desktop-light.png) | ![FL-F16-07 step 6, U16, dark](../../images/07-live-chat-voice-and-contracts/u16-office-worker/6-canned-replies-desktop-dark.png) |
| FL-F16-07 step 6, U16 | phone | ![FL-F16-07 step 6, U16, light](../../images/07-live-chat-voice-and-contracts/u16-office-worker/6-canned-replies-phone-light.png) | ![FL-F16-07 step 6, U16, dark](../../images/07-live-chat-voice-and-contracts/u16-office-worker/6-canned-replies-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f16-21-canned-replies-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f16-21-canned-replies-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f16-21-canned-replies-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f16-21-canned-replies-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f16-21-canned-replies-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f16-21-canned-replies-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f16-21-canned-replies-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f16-21-canned-replies-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Reply | E-F16-07 title, text | text with variables | support lead | yes |
| Languages | E-F16-07 languages | list | support lead | yes |
| Variables | E-F16-07 variables | list of names and sources | support lead | yes |
| Preview | request and records | text with filled values | agent | no |
| Used | E-F16-07 uses | number | no | no |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Fill | reply | office worker | fills each variable from the request and records |
| Send | reply | office worker | sends once no variable is missing |
| Flag as wrong | reply | office worker | asks the lead to review it |
| New or edit reply | header | support lead | changes the library |
| Retire | row | support lead | stops offering the reply |

## States

- Normal: the replies for the intent and the language, and the preview with its filled variables.
- Empty: No reply for this intent, with New reply.
- Loading: the headings and the table as placeholders; the values follow.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); a missing or
  restricted variable is highlighted and blocks sending.
- Read-only: the record in a locked state: values shown, no action offered.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-F16-07 Macro](../../data/e-f16-07-macro.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F16-07 Macro | Active | Badge "Active"; a new record starts here; next: Archived (UC-F16-23); fields editable within the role | U16 | `u16-office-worker/s-f16-21-canned-replies-e-f16-07-macro-active-{desktop,phone}-{light,dark}.png` |
| E-F16-07 Macro | Archived | Badge "Archived"; final: read-only, no next state; the history shows how it got here | U16 | `u16-office-worker/s-f16-21-canned-replies-e-f16-07-macro-archived-{desktop,phone}-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop only; on a phone, the app asks to continue on a larger screen.

## Accessibility

Every control is reachable by keyboard; states and errors are announced to screen readers and never rely on colour
alone; each field has its visible label.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)
- [C-01 Button](../../../../04-ux/design-system/components/c-01-button.md)

## Shown in

- [FL-F16-07](../../flows/fl-f16-07-live-chat-voice-and-contracts.md)

## Open questions

None.

---

⬅️ [S-F16-20 Support contracts](s-f16-20-support-contracts.md) · ⬆️ [Up](README.md) ·
➡️ [S-F16-L01 Customer requests](../00-lists/s-f16-l01-customer-requests.md)
