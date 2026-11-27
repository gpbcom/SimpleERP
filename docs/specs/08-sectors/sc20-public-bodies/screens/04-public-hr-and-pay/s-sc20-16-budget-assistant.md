🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🏛️ [SC20 Public bodies](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC20-04 Public-sector HR and pay](README.md) ›
🖥️ S-SC20-16 Budget assistant

# 🖥️ S-SC20-16 Budget assistant

**Status:** ✅ specified

## Personas

- [U55 Elected official](../../../../01-users/personas/u55-elected-official.md): my questions about the budget, with the
  figures and their sources, on the phone.

## Purpose

Let an elected official ask about the budget in plain words and see the figure with its sources.

## Entry points

Public bodies › Ask about the budget; the AI assistant button on any budget screen.

## Wireframe

```text
+--------------------------------------------------------------------------------------------------+
| Ask about the budget                                         Elected official: Mme Faure         |
| You: How much credit is left on roads                                                            |
| AI assistant: 300,000 EUR left of 900,000 on 'Roads and networks' on 14 March.                   |
| Sources: commitments 2027-0398 (60,000 used), budget 2027 chapter 21     [Open] [Chart]          |
| [Type a question...]                                                [Send]                       |
+--------------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC20-04 step 4, U55 | desktop | ![FL-SC20-04 step 4, U55, light](../../images/04-public-hr-and-pay/u55-elected-official/4-budget-assistant-desktop-light.png) | ![FL-SC20-04 step 4, U55, dark](../../images/04-public-hr-and-pay/u55-elected-official/4-budget-assistant-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc20-16-budget-assistant-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc20-16-budget-assistant-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc20-16-budget-assistant-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc20-16-budget-assistant-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc20-16-budget-assistant-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc20-16-budget-assistant-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-sc20-16-budget-assistant-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-sc20-16-budget-assistant-offline-desktop-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Question | E-F3-01 message | text | yes | yes |
| Answer | E-F3-02 answer | text with figures | no | no |
| Sources | E-F3-02 sources | list of links | no | no |
| Chart | E-F3-02 chart | chart | no | no |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Send | form | elected official | the question is asked |
| Open a source | answer | elected official | the record behind the figure opens |
| Chart | answer | elected official | the figures are shown as a chart |

## States

- Normal: the conversation with the answers, their figures and sources.
- Empty: No question yet, with examples of questions.
- Loading: the headings and the table as placeholders; the values follow.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); a data source
  unavailable, a question refused for the role, with the reason.
- Read-only: the record in a locked state: values shown, no action offered.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): none; no flow's Entities and screens table names an entity on this screen.

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

- [FL-SC20-04 Public-sector HR and pay](../../flows/fl-sc20-04-public-hr-and-pay.md)

## Open questions

None.

---

⬅️ [S-SC20-15 Public contributions](s-sc20-15-public-contributions.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC20-17 Council meetings](../05-council-registry-permits-and-assets/s-sc20-17-council-meetings.md)
