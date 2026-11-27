🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) › 🤖 [F3 Assistant](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-F3-01 Ask the AI assistant](README.md) › 🖥️ S-F3-01 Assistant panel

# 🖥️ S-F3-01 Assistant panel

**Status:** ✅ specified

## Personas

Every internal persona (D142): [U01](../../../../01-users/personas/u01-employee.md),
[U02](../../../../01-users/personas/u02-manager.md), [U03](../../../../01-users/personas/u03-sales.md),
[U04](../../../../01-users/personas/u04-purchasing.md), [U05](../../../../01-users/personas/u05-accounting.md),
[U06](../../../../01-users/personas/u06-hr.md), [U07](../../../../01-users/personas/u07-administrator.md),
[U12](../../../../01-users/personas/u12-marketing.md), [U13](../../../../01-users/personas/u13-owner.md),
[U14](../../../../01-users/personas/u14-field-worker.md),
[U15](../../../../01-users/personas/u15-warehouse-operator.md),
[U16](../../../../01-users/personas/u16-office-worker.md).

## Purpose

Ask the AI assistant and read its answers, beside the current screen (D49).

## Entry points

The AI assistant button in the top bar of every screen; the keyboard shortcut Ctrl+K then "Ask"; on a phone, the
AI assistant tab (UC-F3-09).

## Wireframe

```text
+-------------------------------------------+
| Assistant  (AI)          [History] [x]    |
|-------------------------------------------|
| You: Turnover with Durand this year?      |
|                                           |
| 48,200 EUR from 12 invoices to            |
| [Durand SA] in 2026.                      |
|  Month | Amount                           |
|  Jan   | 3,100 EUR  ...       [Export]    |
| Based on the records you can see.         |
| [How this was computed]    [Up] [Down]    |
| Sources: [Durand SA] [Invoices, 2026]     |
|-------------------------------------------|
| [Ask a question...]          [mic] [Send] |
+-------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F3-01 step 1, U01 | phone | ![FL-F3-01 step 1, U01, light](../../images/01-ask-the-assistant/u01-employee/1-ask-phone-light.png) | ![FL-F3-01 step 1, U01, dark](../../images/01-ask-the-assistant/u01-employee/1-ask-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f03-01-assistant-panel-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f03-01-assistant-panel-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f03-01-assistant-panel-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f03-01-assistant-panel-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f03-01-assistant-panel-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f03-01-assistant-panel-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f03-01-assistant-panel-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f03-01-assistant-panel-offline-phone-dark.png) |

## Fields and columns

Question box; answer with links, tables and charts; Sources; How this was computed; thumbs up and down under each
answer, with an optional reason (wrong, incomplete, out of date, too slow) and comment after a thumbs down
([E-F3-14 Answer feedback](../../data/e-f03-14-answer-feedback.md)).

## Actions

| Action | Who | Result |
|---|---|---|
| Send | every internal persona | The answer |
| Pick a choice | every internal persona | The clarified answer |
| Open a source | every internal persona | The record in the side panel |
| How this was computed | every internal persona | Record type, filters, period, fields, count |
| Export | every internal persona | A spreadsheet |
| Stop | every internal persona | The answer stops |
| Thumbs up or down | every internal persona | The feedback is saved and counted in the usage dashboard; a thumbs down on an answer that used a knowledge item notifies its owner (D186) |
| Change or remove my feedback | every internal persona | The feedback is changed or removed |

## States

- Normal: Ask the AI assistant and read its answers, beside the current screen (D49), as the wireframe shows.
- Empty: suggested questions for the record type and the user's role (D154).
- Loading: the answer appears word by word, with "Searching invoices...".
- Error: the error message pattern (D122).
- Read-only: never: the panel only proposes changes, which the user confirms.
- Offline: The AI assistant says it is offline; questions are queued and answered when the network is back, with a
  notification, and changes still need confirmation then
  ([D182](../../../../06-decisions/f03-assistant/d182-offline-assistant.md)).
- With context: a chip "About: Durand SA" or "About: 3 invoices", removable (BR-F3-05).
- Clarifying: choices as buttons.
- Not found: what was searched.
- Rated: the chosen thumb is highlighted; after a thumbs down, the reasons show as buttons and a comment box, both
  optional.

Shown entities (VD-15): [E-F3-02 Assistant answer](../../data/e-f03-02-assistant-answer.md),
[E-F3-14 Answer feedback](../../data/e-f03-14-answer-feedback.md),
[E-F3-03 Suggested question](../../data/e-f03-03-suggested-question.md),
[E-F3-22 AI assistant request](../../data/e-f03-22-ai-assistant-request.md),
[E-F3-04 Assistant change batch](../../data/e-f03-04-assistant-change-batch.md),
[E-F3-05 Company writing style](../../data/e-f03-05-company-writing-style.md),
[E-F3-06 Configuration request](../../data/e-f03-06-configuration-request.md),
[E-F3-08 Outside call](../../data/e-f03-08-outside-call.md),
[E-F3-01 Conversation](../../data/e-f03-01-conversation.md),
[E-F3-19 Injection alert](../../data/e-f03-19-injection-alert.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F3-02 Assistant answer | Recorded | Badge "Recorded"; a new record starts here; no other state; fields editable within the role | U01, U02, U03, U05, U06, U07, U13, U14, U16 | `u01-employee/s-f03-01-assistant-panel-e-f03-02-assistant-answer-recorded-{desktop,phone}-{light,dark}.png`, `u02-manager/s-f03-01-assistant-panel-e-f03-02-assistant-answer-recorded-{desktop,phone}-{light,dark}.png`, `u03-sales/s-f03-01-assistant-panel-e-f03-02-assistant-answer-recorded-{desktop,phone,tablet}-{light,dark}.png`, `u05-accounting/s-f03-01-assistant-panel-e-f03-02-assistant-answer-recorded-desktop-{light,dark}.png`, `u06-hr/s-f03-01-assistant-panel-e-f03-02-assistant-answer-recorded-desktop-{light,dark}.png`, `u07-administrator/s-f03-01-assistant-panel-e-f03-02-assistant-answer-recorded-desktop-{light,dark}.png`, `u13-owner/s-f03-01-assistant-panel-e-f03-02-assistant-answer-recorded-{desktop,phone}-{light,dark}.png`, `u14-field-worker/s-f03-01-assistant-panel-e-f03-02-assistant-answer-recorded-phone-{light,dark}.png`, `u16-office-worker/s-f03-01-assistant-panel-e-f03-02-assistant-answer-recorded-{desktop,phone}-{light,dark}.png` |
| E-F3-14 Answer feedback | Recorded | Badge "Recorded"; a new record starts here; no other state; fields editable within the role | U01, U03, U13 | `u01-employee/s-f03-01-assistant-panel-e-f03-14-answer-feedback-recorded-{desktop,phone}-{light,dark}.png`, `u03-sales/s-f03-01-assistant-panel-e-f03-14-answer-feedback-recorded-{desktop,phone,tablet}-{light,dark}.png`, `u13-owner/s-f03-01-assistant-panel-e-f03-14-answer-feedback-recorded-{desktop,phone}-{light,dark}.png` |
| E-F3-03 Suggested question | Draft | Badge "Draft"; a new record starts here; next: Published (UC-F3-02); fields editable within the role | U02, U03 | `u02-manager/s-f03-01-assistant-panel-e-f03-03-suggested-question-draft-{desktop,phone}-{light,dark}.png`, `u03-sales/s-f03-01-assistant-panel-e-f03-03-suggested-question-draft-{desktop,phone,tablet}-{light,dark}.png` |
| E-F3-03 Suggested question | Published | Badge "Published"; next: Shipped (UC-F3-02); fields editable within the role | U02, U03 | `u02-manager/s-f03-01-assistant-panel-e-f03-03-suggested-question-published-{desktop,phone}-{light,dark}.png`, `u03-sales/s-f03-01-assistant-panel-e-f03-03-suggested-question-published-{desktop,phone,tablet}-{light,dark}.png` |
| E-F3-03 Suggested question | Shipped | Badge "Shipped"; final: read-only, no next state; the history shows how it got here | U02, U03 | `u02-manager/s-f03-01-assistant-panel-e-f03-03-suggested-question-shipped-{desktop,phone}-{light,dark}.png`, `u03-sales/s-f03-01-assistant-panel-e-f03-03-suggested-question-shipped-{desktop,phone,tablet}-{light,dark}.png` |
| E-F3-22 AI assistant request | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U02, U03, U04 | `u02-manager/s-f03-01-assistant-panel-e-f03-22-ai-assistant-request-active-{desktop,phone}-{light,dark}.png`, `u03-sales/s-f03-01-assistant-panel-e-f03-22-ai-assistant-request-active-{desktop,phone,tablet}-{light,dark}.png`, `u04-purchasing/s-f03-01-assistant-panel-e-f03-22-ai-assistant-request-active-desktop-{light,dark}.png` |
| E-F3-04 Assistant change batch | Proposed | Badge "Proposed"; a new record starts here; next: Cancelled, Done or Partly done (UC-F3-03, BR-F3-09); fields editable within the role | U01, U02, U03, U04, U05, U06, U07, U12, U13, U14, U15, U16 | `u01-employee/s-f03-01-assistant-panel-e-f03-04-assistant-change-batch-proposed-{desktop,phone}-{light,dark}.png`, `u02-manager/s-f03-01-assistant-panel-e-f03-04-assistant-change-batch-proposed-{desktop,phone}-{light,dark}.png`, `u03-sales/s-f03-01-assistant-panel-e-f03-04-assistant-change-batch-proposed-{desktop,phone,tablet}-{light,dark}.png`, `u04-purchasing/s-f03-01-assistant-panel-e-f03-04-assistant-change-batch-proposed-desktop-{light,dark}.png`, `u05-accounting/s-f03-01-assistant-panel-e-f03-04-assistant-change-batch-proposed-desktop-{light,dark}.png`, `u06-hr/s-f03-01-assistant-panel-e-f03-04-assistant-change-batch-proposed-desktop-{light,dark}.png`, `u07-administrator/s-f03-01-assistant-panel-e-f03-04-assistant-change-batch-proposed-desktop-{light,dark}.png`, `u12-marketing/s-f03-01-assistant-panel-e-f03-04-assistant-change-batch-proposed-{desktop,phone}-{light,dark}.png`, `u13-owner/s-f03-01-assistant-panel-e-f03-04-assistant-change-batch-proposed-{desktop,phone}-{light,dark}.png`, `u14-field-worker/s-f03-01-assistant-panel-e-f03-04-assistant-change-batch-proposed-phone-{light,dark}.png`, `u15-warehouse-operator/s-f03-01-assistant-panel-e-f03-04-assistant-change-batch-proposed-{phone,tablet}-{light,dark}.png`, `u16-office-worker/s-f03-01-assistant-panel-e-f03-04-assistant-change-batch-proposed-{desktop,phone}-{light,dark}.png` |
| E-F3-05 Company writing style | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U03 | `u03-sales/s-f03-01-assistant-panel-e-f03-05-company-writing-style-active-{desktop,phone,tablet}-{light,dark}.png` |
| E-F3-06 Configuration request | Open | Badge "Open"; a new record starts here; next: Planned, Done or Declined (UC-F3-05); fields editable within the role | U04, U16 | `u04-purchasing/s-f03-01-assistant-panel-e-f03-06-configuration-request-open-desktop-{light,dark}.png`, `u16-office-worker/s-f03-01-assistant-panel-e-f03-06-configuration-request-open-{desktop,phone}-{light,dark}.png` |
| E-F3-06 Configuration request | Planned | Badge "Planned"; next: Done (UC-F3-05); fields editable within the role | U04, U16 | `u04-purchasing/s-f03-01-assistant-panel-e-f03-06-configuration-request-planned-desktop-{light,dark}.png`, `u16-office-worker/s-f03-01-assistant-panel-e-f03-06-configuration-request-planned-{desktop,phone}-{light,dark}.png` |
| E-F3-06 Configuration request | Done | Badge "Done"; final: read-only, no next state; the history shows how it got here | U04, U16 | `u04-purchasing/s-f03-01-assistant-panel-e-f03-06-configuration-request-done-desktop-{light,dark}.png`, `u16-office-worker/s-f03-01-assistant-panel-e-f03-06-configuration-request-done-{desktop,phone}-{light,dark}.png` |
| E-F3-06 Configuration request | Declined | Badge "Declined"; final: read-only, no next state; the history shows how it got here | U04, U16 | `u04-purchasing/s-f03-01-assistant-panel-e-f03-06-configuration-request-declined-desktop-{light,dark}.png`, `u16-office-worker/s-f03-01-assistant-panel-e-f03-06-configuration-request-declined-{desktop,phone}-{light,dark}.png` |
| E-F3-08 Outside call | Refused | Badge "Refused"; a new record starts here; no other state; fields editable within the role | U04 | `u04-purchasing/s-f03-01-assistant-panel-e-f03-08-outside-call-refused-desktop-{light,dark}.png` |
| E-F3-01 Conversation | Private | Badge "Private"; a new record starts here; next: Shared or Deleted (UC-F3-01, UC-F3-08); fields editable within the role | U02 | `u02-manager/s-f03-01-assistant-panel-e-f03-01-conversation-private-{desktop,phone}-{light,dark}.png` |
| E-F3-01 Conversation | Shared | Badge "Shared"; next: Private or Deleted (UC-F15-01, UC-F3-08); fields editable within the role | U02 | `u02-manager/s-f03-01-assistant-panel-e-f03-01-conversation-shared-{desktop,phone}-{light,dark}.png` |
| E-F3-01 Conversation | Deleted | Not shown: the record is gone in this state, so no screen shows it | U02 | None: system state, the user never sees it |
| E-F3-19 Injection alert | New | Badge "New"; a new record starts here; next: Harmless (UC-F3-15); fields editable within the role | U01 | `u01-employee/s-f03-01-assistant-panel-e-f03-19-injection-alert-new-{desktop,phone}-{light,dark}.png` |
| E-F3-19 Injection alert | Harmless | Badge "Harmless"; next: Confirmed (UC-F3-15); fields editable within the role | U01 | `u01-employee/s-f03-01-assistant-panel-e-f03-19-injection-alert-harmless-{desktop,phone}-{light,dark}.png` |
| E-F3-19 Injection alert | Confirmed | Badge "Confirmed"; final: read-only, no next state; the history shows how it got here | U01 | `u01-employee/s-f03-01-assistant-panel-e-f03-19-injection-alert-confirmed-{desktop,phone}-{light,dark}.png` |
| E-F3-04 Assistant change batch | Cancelled | Badge "Cancelled"; final: read-only, no next state; the history shows how it got here | U01, U02, U03, U04, U05, U06, U07, U12, U13, U14, U15, U16 | `u01-employee/s-f03-01-assistant-panel-e-f03-04-assistant-change-batch-cancelled-{desktop,phone}-{light,dark}.png`, `u02-manager/s-f03-01-assistant-panel-e-f03-04-assistant-change-batch-cancelled-{desktop,phone}-{light,dark}.png`, `u03-sales/s-f03-01-assistant-panel-e-f03-04-assistant-change-batch-cancelled-{desktop,phone,tablet}-{light,dark}.png`, `u04-purchasing/s-f03-01-assistant-panel-e-f03-04-assistant-change-batch-cancelled-desktop-{light,dark}.png`, `u05-accounting/s-f03-01-assistant-panel-e-f03-04-assistant-change-batch-cancelled-desktop-{light,dark}.png`, `u06-hr/s-f03-01-assistant-panel-e-f03-04-assistant-change-batch-cancelled-desktop-{light,dark}.png`, `u07-administrator/s-f03-01-assistant-panel-e-f03-04-assistant-change-batch-cancelled-desktop-{light,dark}.png`, `u12-marketing/s-f03-01-assistant-panel-e-f03-04-assistant-change-batch-cancelled-{desktop,phone}-{light,dark}.png`, `u13-owner/s-f03-01-assistant-panel-e-f03-04-assistant-change-batch-cancelled-{desktop,phone}-{light,dark}.png`, `u14-field-worker/s-f03-01-assistant-panel-e-f03-04-assistant-change-batch-cancelled-phone-{light,dark}.png`, `u15-warehouse-operator/s-f03-01-assistant-panel-e-f03-04-assistant-change-batch-cancelled-{phone,tablet}-{light,dark}.png`, `u16-office-worker/s-f03-01-assistant-panel-e-f03-04-assistant-change-batch-cancelled-{desktop,phone}-{light,dark}.png` |
| E-F3-04 Assistant change batch | Done | Badge "Done"; next: Undone (UC-F3-03); fields editable within the role | U01, U02, U03, U04, U05, U06, U07, U12, U13, U14, U15, U16 | `u01-employee/s-f03-01-assistant-panel-e-f03-04-assistant-change-batch-done-{desktop,phone}-{light,dark}.png`, `u02-manager/s-f03-01-assistant-panel-e-f03-04-assistant-change-batch-done-{desktop,phone}-{light,dark}.png`, `u03-sales/s-f03-01-assistant-panel-e-f03-04-assistant-change-batch-done-{desktop,phone,tablet}-{light,dark}.png`, `u04-purchasing/s-f03-01-assistant-panel-e-f03-04-assistant-change-batch-done-desktop-{light,dark}.png`, `u05-accounting/s-f03-01-assistant-panel-e-f03-04-assistant-change-batch-done-desktop-{light,dark}.png`, `u06-hr/s-f03-01-assistant-panel-e-f03-04-assistant-change-batch-done-desktop-{light,dark}.png`, `u07-administrator/s-f03-01-assistant-panel-e-f03-04-assistant-change-batch-done-desktop-{light,dark}.png`, `u12-marketing/s-f03-01-assistant-panel-e-f03-04-assistant-change-batch-done-{desktop,phone}-{light,dark}.png`, `u13-owner/s-f03-01-assistant-panel-e-f03-04-assistant-change-batch-done-{desktop,phone}-{light,dark}.png`, `u14-field-worker/s-f03-01-assistant-panel-e-f03-04-assistant-change-batch-done-phone-{light,dark}.png`, `u15-warehouse-operator/s-f03-01-assistant-panel-e-f03-04-assistant-change-batch-done-{phone,tablet}-{light,dark}.png`, `u16-office-worker/s-f03-01-assistant-panel-e-f03-04-assistant-change-batch-done-{desktop,phone}-{light,dark}.png` |
| E-F3-04 Assistant change batch | Partly done | Badge "Partly done"; next: Undone (UC-F3-03); fields editable within the role | U01, U02, U03, U04, U05, U06, U07, U12, U13, U14, U15, U16 | `u01-employee/s-f03-01-assistant-panel-e-f03-04-assistant-change-batch-partly-done-{desktop,phone}-{light,dark}.png`, `u02-manager/s-f03-01-assistant-panel-e-f03-04-assistant-change-batch-partly-done-{desktop,phone}-{light,dark}.png`, `u03-sales/s-f03-01-assistant-panel-e-f03-04-assistant-change-batch-partly-done-{desktop,phone,tablet}-{light,dark}.png`, `u04-purchasing/s-f03-01-assistant-panel-e-f03-04-assistant-change-batch-partly-done-desktop-{light,dark}.png`, `u05-accounting/s-f03-01-assistant-panel-e-f03-04-assistant-change-batch-partly-done-desktop-{light,dark}.png`, `u06-hr/s-f03-01-assistant-panel-e-f03-04-assistant-change-batch-partly-done-desktop-{light,dark}.png`, `u07-administrator/s-f03-01-assistant-panel-e-f03-04-assistant-change-batch-partly-done-desktop-{light,dark}.png`, `u12-marketing/s-f03-01-assistant-panel-e-f03-04-assistant-change-batch-partly-done-{desktop,phone}-{light,dark}.png`, `u13-owner/s-f03-01-assistant-panel-e-f03-04-assistant-change-batch-partly-done-{desktop,phone}-{light,dark}.png`, `u14-field-worker/s-f03-01-assistant-panel-e-f03-04-assistant-change-batch-partly-done-phone-{light,dark}.png`, `u15-warehouse-operator/s-f03-01-assistant-panel-e-f03-04-assistant-change-batch-partly-done-{phone,tablet}-{light,dark}.png`, `u16-office-worker/s-f03-01-assistant-panel-e-f03-04-assistant-change-batch-partly-done-{desktop,phone}-{light,dark}.png` |
| E-F3-04 Assistant change batch | Undone | Badge "Undone"; final: read-only, no next state; the history shows how it got here | U01, U02, U03, U04, U05, U06, U07, U12, U13, U14, U15, U16 | `u01-employee/s-f03-01-assistant-panel-e-f03-04-assistant-change-batch-undone-{desktop,phone}-{light,dark}.png`, `u02-manager/s-f03-01-assistant-panel-e-f03-04-assistant-change-batch-undone-{desktop,phone}-{light,dark}.png`, `u03-sales/s-f03-01-assistant-panel-e-f03-04-assistant-change-batch-undone-{desktop,phone,tablet}-{light,dark}.png`, `u04-purchasing/s-f03-01-assistant-panel-e-f03-04-assistant-change-batch-undone-desktop-{light,dark}.png`, `u05-accounting/s-f03-01-assistant-panel-e-f03-04-assistant-change-batch-undone-desktop-{light,dark}.png`, `u06-hr/s-f03-01-assistant-panel-e-f03-04-assistant-change-batch-undone-desktop-{light,dark}.png`, `u07-administrator/s-f03-01-assistant-panel-e-f03-04-assistant-change-batch-undone-desktop-{light,dark}.png`, `u12-marketing/s-f03-01-assistant-panel-e-f03-04-assistant-change-batch-undone-{desktop,phone}-{light,dark}.png`, `u13-owner/s-f03-01-assistant-panel-e-f03-04-assistant-change-batch-undone-{desktop,phone}-{light,dark}.png`, `u14-field-worker/s-f03-01-assistant-panel-e-f03-04-assistant-change-batch-undone-phone-{light,dark}.png`, `u15-warehouse-operator/s-f03-01-assistant-panel-e-f03-04-assistant-change-batch-undone-{phone,tablet}-{light,dark}.png`, `u16-office-worker/s-f03-01-assistant-panel-e-f03-04-assistant-change-batch-undone-{desktop,phone}-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop: a panel on the right, 400 px wide, resizable. Phone: full screen (UC-F3-09).

## Accessibility

Answers are announced to screen readers when complete; choices and sources are buttons and links reachable by keyboard;
charts have their table.

## Components

- [C-11 Chat panel](../../../../04-ux/design-system/components/c-11-chat-panel.md)
- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-09 Chart](../../../../04-ux/design-system/components/c-09-chart.md)
- [C-10 Empty state](../../../../04-ux/design-system/components/c-10-empty-state.md)

## Shown in

- [FL-F3-01 Ask the AI assistant](../../flows/fl-f03-01-ask-the-assistant.md)
- [FL-F3-02 Ask about the screen](../../flows/fl-f03-02-ask-about-the-screen.md)
- [FL-F3-11 Trust the answers](../../flows/fl-f03-11-trust-the-answers.md)

## Open questions

None.

---

⬆️ [Up](README.md) ·
➡️ [S-F3-02 Change confirmation card](../03-act-through-the-assistant/s-f03-02-change-confirmation-card.md)
