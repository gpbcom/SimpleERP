🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
⚖️ [F15 Legal assistant](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F15-01 Ask a legal question](README.md) › 🖥️ S-F15-01 Legal answer

# 🖥️ S-F15-01 Legal answer

**Status:** ✅ specified

## Personas

Every internal persona

## Purpose

The legal mode of the AI assistant panel: cited answers for the person's situation.

## Entry points

The Legal tab of the AI assistant panel (S-F3-01); a legal question asked in the AI assistant.

## Wireframe

```text
+-------------------------------------------+
| Assistant  [General] [Legal]   (AI) [x]  |
|-------------------------------------------|
| Under French law  [change]                 |
| Facts used: full time, 4 years, IDCC 1597 |
|   [general answer only]                    |
| You have 12.5 days of paid leave left...  |
| L3141-3, in force since 22/04/2024 [open] |
| This is legal information, not legal      |
| advice.                                   |
+-------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F15-01 step 1, U01 | desktop | ![FL-F15-01 step 1, U01, light](../../images/01-ask-a-legal-question/u01-employee/1-ask-with-facts-desktop-light.png) | ![FL-F15-01 step 1, U01, dark](../../images/01-ask-a-legal-question/u01-employee/1-ask-with-facts-desktop-dark.png) |
| FL-F15-01 step 1, U01 | phone | ![FL-F15-01 step 1, U01, light](../../images/01-ask-a-legal-question/u01-employee/1-ask-with-facts-phone-light.png) | ![FL-F15-01 step 1, U01, dark](../../images/01-ask-a-legal-question/u01-employee/1-ask-with-facts-phone-dark.png) |
| Error E1, U01 | desktop | ![Error E1, U01, light](../../images/01-ask-a-legal-question/u01-employee/e1-no-law-pack-desktop-light.png) | ![Error E1, U01, dark](../../images/01-ask-a-legal-question/u01-employee/e1-no-law-pack-desktop-dark.png) |
| Error E1, U01 | phone | ![Error E1, U01, light](../../images/01-ask-a-legal-question/u01-employee/e1-no-law-pack-phone-light.png) | ![Error E1, U01, dark](../../images/01-ask-a-legal-question/u01-employee/e1-no-law-pack-phone-dark.png) |
| Error E2, U01 | phone | ![Error E2, U01, light](../../images/01-ask-a-legal-question/u01-employee/e2-sensitive-referral-phone-light.png) | ![Error E2, U01, dark](../../images/01-ask-a-legal-question/u01-employee/e2-sensitive-referral-phone-dark.png) |
| Error E2, U01 | desktop | ![Error E2, U01, light](../../images/01-ask-a-legal-question/u01-employee/e2-sensitive-referral-desktop-light.png) | ![Error E2, U01, dark](../../images/01-ask-a-legal-question/u01-employee/e2-sensitive-referral-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f15-01-legal-answer-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f15-01-legal-answer-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f15-01-legal-answer-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f15-01-legal-answer-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f15-01-legal-answer-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f15-01-legal-answer-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f15-01-legal-answer-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f15-01-legal-answer-offline-phone-dark.png) |

## Fields and columns

Country; facts used; answer; citations with versions and dates; notice or referral.

## Actions

As the flow's steps.

## States

- Normal: the answer with the facts used, each statement's article, version and date, its confidence and the closing
  notice.
- Facts used listed, switch to general.
- As of a past date.
- Referral for sensitive topics.
- I don't know.
- Empty: "Ask a legal question": example questions for the user's role, and "general answer only".
- Loading: the frame and titles show at once with placeholder rows for the answer; within 1 second (D408) the data
  replaces them, and a longer load shows a progress line saying what loads.
- Error: the error message pattern (D122).
- Read-only: a past conversation is read-only; facts are those the asker may see (D191).
- Offline: the AI assistant says it is offline; the question is queued and answered when the network is back, with a
  notification (D182).

Shown entities (VD-15): [E-F3-01 Conversation](../../../f03-assistant/data/e-f03-01-conversation.md),
[E-F15-10 Lawyer hand-off](../../data/e-f15-10-lawyer-hand-off.md),
[E-F15-01 Law pack](../../data/e-f15-01-law-pack.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F3-01 Conversation | Private | Badge "Private"; a new record starts here; next: Shared or Deleted (UC-F3-01, UC-F3-08); fields editable within the role | U01, U02, U05, U06, U08, U13, U14 | `u01-employee/s-f15-01-legal-answer-e-f03-01-conversation-private-{desktop,phone}-{light,dark}.png`, `u02-manager/s-f15-01-legal-answer-e-f03-01-conversation-private-{desktop,phone}-{light,dark}.png`, `u05-accounting/s-f15-01-legal-answer-e-f03-01-conversation-private-desktop-{light,dark}.png`, `u06-hr/s-f15-01-legal-answer-e-f03-01-conversation-private-desktop-{light,dark}.png`, `u08-external-accountant/s-f15-01-legal-answer-e-f03-01-conversation-private-desktop-{light,dark}.png`, `u13-owner/s-f15-01-legal-answer-e-f03-01-conversation-private-{desktop,phone}-{light,dark}.png`, `u14-field-worker/s-f15-01-legal-answer-e-f03-01-conversation-private-phone-{light,dark}.png` |
| E-F3-01 Conversation | Shared | Badge "Shared"; next: Private or Deleted (UC-F15-01, UC-F3-08); fields editable within the role | U01, U02, U05, U06, U08, U13, U14 | `u01-employee/s-f15-01-legal-answer-e-f03-01-conversation-shared-{desktop,phone}-{light,dark}.png`, `u02-manager/s-f15-01-legal-answer-e-f03-01-conversation-shared-{desktop,phone}-{light,dark}.png`, `u05-accounting/s-f15-01-legal-answer-e-f03-01-conversation-shared-desktop-{light,dark}.png`, `u06-hr/s-f15-01-legal-answer-e-f03-01-conversation-shared-desktop-{light,dark}.png`, `u08-external-accountant/s-f15-01-legal-answer-e-f03-01-conversation-shared-desktop-{light,dark}.png`, `u13-owner/s-f15-01-legal-answer-e-f03-01-conversation-shared-{desktop,phone}-{light,dark}.png`, `u14-field-worker/s-f15-01-legal-answer-e-f03-01-conversation-shared-phone-{light,dark}.png` |
| E-F3-01 Conversation | Deleted | Not shown: the record is gone in this state, so no screen shows it | U01, U02, U05, U06, U08, U13, U14 | None: system state, the user never sees it |
| E-F15-10 Lawyer hand-off | Draft | Badge "Draft"; a new record starts here; next: Sent or Discarded (UC-F15-12); fields editable within the role | U01, U02, U05, U06, U08, U13, U14 | `u01-employee/s-f15-01-legal-answer-e-f15-10-lawyer-hand-off-draft-{desktop,phone}-{light,dark}.png`, `u02-manager/s-f15-01-legal-answer-e-f15-10-lawyer-hand-off-draft-{desktop,phone}-{light,dark}.png`, `u05-accounting/s-f15-01-legal-answer-e-f15-10-lawyer-hand-off-draft-desktop-{light,dark}.png`, `u06-hr/s-f15-01-legal-answer-e-f15-10-lawyer-hand-off-draft-desktop-{light,dark}.png`, `u08-external-accountant/s-f15-01-legal-answer-e-f15-10-lawyer-hand-off-draft-desktop-{light,dark}.png`, `u13-owner/s-f15-01-legal-answer-e-f15-10-lawyer-hand-off-draft-{desktop,phone}-{light,dark}.png`, `u14-field-worker/s-f15-01-legal-answer-e-f15-10-lawyer-hand-off-draft-phone-{light,dark}.png` |
| E-F15-10 Lawyer hand-off | Sent | Badge "Sent"; final: read-only, no next state; the history shows how it got here | U01, U02, U05, U06, U08, U13, U14 | `u01-employee/s-f15-01-legal-answer-e-f15-10-lawyer-hand-off-sent-{desktop,phone}-{light,dark}.png`, `u02-manager/s-f15-01-legal-answer-e-f15-10-lawyer-hand-off-sent-{desktop,phone}-{light,dark}.png`, `u05-accounting/s-f15-01-legal-answer-e-f15-10-lawyer-hand-off-sent-desktop-{light,dark}.png`, `u06-hr/s-f15-01-legal-answer-e-f15-10-lawyer-hand-off-sent-desktop-{light,dark}.png`, `u08-external-accountant/s-f15-01-legal-answer-e-f15-10-lawyer-hand-off-sent-desktop-{light,dark}.png`, `u13-owner/s-f15-01-legal-answer-e-f15-10-lawyer-hand-off-sent-{desktop,phone}-{light,dark}.png`, `u14-field-worker/s-f15-01-legal-answer-e-f15-10-lawyer-hand-off-sent-phone-{light,dark}.png` |
| E-F15-10 Lawyer hand-off | Discarded | Badge "Discarded"; final: read-only, no next state; the history shows how it got here | U01, U02, U05, U06, U08, U13, U14 | `u01-employee/s-f15-01-legal-answer-e-f15-10-lawyer-hand-off-discarded-{desktop,phone}-{light,dark}.png`, `u02-manager/s-f15-01-legal-answer-e-f15-10-lawyer-hand-off-discarded-{desktop,phone}-{light,dark}.png`, `u05-accounting/s-f15-01-legal-answer-e-f15-10-lawyer-hand-off-discarded-desktop-{light,dark}.png`, `u06-hr/s-f15-01-legal-answer-e-f15-10-lawyer-hand-off-discarded-desktop-{light,dark}.png`, `u08-external-accountant/s-f15-01-legal-answer-e-f15-10-lawyer-hand-off-discarded-desktop-{light,dark}.png`, `u13-owner/s-f15-01-legal-answer-e-f15-10-lawyer-hand-off-discarded-{desktop,phone}-{light,dark}.png`, `u14-field-worker/s-f15-01-legal-answer-e-f15-10-lawyer-hand-off-discarded-phone-{light,dark}.png` |
| E-F15-01 Law pack | Scheduled | Badge "Scheduled"; a new record starts here; no other state; fields editable within the role | U01, U02, U05, U06, U08, U13, U14 | `u01-employee/s-f15-01-legal-answer-e-f15-01-law-pack-scheduled-{desktop,phone}-{light,dark}.png`, `u02-manager/s-f15-01-legal-answer-e-f15-01-law-pack-scheduled-{desktop,phone}-{light,dark}.png`, `u05-accounting/s-f15-01-legal-answer-e-f15-01-law-pack-scheduled-desktop-{light,dark}.png`, `u06-hr/s-f15-01-legal-answer-e-f15-01-law-pack-scheduled-desktop-{light,dark}.png`, `u08-external-accountant/s-f15-01-legal-answer-e-f15-01-law-pack-scheduled-desktop-{light,dark}.png`, `u13-owner/s-f15-01-legal-answer-e-f15-01-law-pack-scheduled-{desktop,phone}-{light,dark}.png`, `u14-field-worker/s-f15-01-legal-answer-e-f15-01-law-pack-scheduled-phone-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop: in the panel. Phone: full screen.

## Accessibility

Citations are links; warnings use an icon and text, never colour alone.

## Components

- [C-11 Chat panel](../../../../04-ux/design-system/components/c-11-chat-panel.md)
- [C-04 Card](../../../../04-ux/design-system/components/c-04-card.md)
- [C-10 Empty state](../../../../04-ux/design-system/components/c-10-empty-state.md)

## Shown in

- [FL-F15-01 Ask a legal question](../../flows/fl-f15-01-ask-a-legal-question.md)

## Open questions

None.

---

⬆️ [Up](README.md) · ➡️ [S-F15-02 Legal warning](../02-receive-a-legal-warning/s-f15-02-legal-warning.md)
