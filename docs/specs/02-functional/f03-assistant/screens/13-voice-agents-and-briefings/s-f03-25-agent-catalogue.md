🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) › 🤖 [F3 Assistant](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-F3-13 Voice, agents and briefings](README.md) ›
🖥️ S-F3-25 Agent catalogue

# 🖥️ S-F3-25 Agent catalogue

**Status:** ✅ specified

## Personas

- - [U07 Administrator](../../../../01-users/personas/u07-administrator.md): all templates.
- - [U05 Accounting](../../../../01-users/personas/u05-accounting.md): the templates of accounting.

## Purpose

Browse the ready-made agents, read what each does and switch one on in suggestion mode.

## Entry points

Assistant › Agents › Catalogue; the AI assistant's suggestion of an agent.

## Wireframe

```text
+---------------------------------------------------------------------------------------------+
| Agent catalogue          Filter: [Accounting v]                              [Search]       |
| ------------------------------------------------------------------------------------------- |
| TEMPLATE                      READS               MAY DO ALONE LATER          START MODE    |
| Chase overdue invoices        invoices, customers  drafts reminders           Suggestion   [Switch on] |
| Triage supplier invoices      mailbox, invoices    codes and matches          Suggestion   [Switch on] |
| Weekly stock check            stock                raises purchase proposals  Suggestion   [Switch on] |
| Thresholds: reminders after [30] days, at most [50] a day      Approver: Claire P.          |
+---------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F3-13 step 2, U07 | desktop | ![FL-F3-13 step 2, U07, light](../../images/13-voice-agents-and-briefings/u07-administrator/2-agent-catalogue-desktop-light.png) | ![FL-F3-13 step 2, U07, dark](../../images/13-voice-agents-and-briefings/u07-administrator/2-agent-catalogue-desktop-dark.png) |
| FL-F3-13 step 2, U07 | desktop | ![FL-F3-13 step 2, U07, light](../../images/13-voice-agents-and-briefings/u07-administrator/2-agent-catalogue-desktop-light.png) | ![FL-F3-13 step 2, U07, dark](../../images/13-voice-agents-and-briefings/u07-administrator/2-agent-catalogue-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f03-25-agent-catalogue-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f03-25-agent-catalogue-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f03-25-agent-catalogue-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f03-25-agent-catalogue-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f03-25-agent-catalogue-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f03-25-agent-catalogue-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f03-25-agent-catalogue-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f03-25-agent-catalogue-offline-desktop-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Template | E-F3-24 name and purpose | text | no | yes |
| Reads | E-F3-24 data read | list | no | yes |
| May do alone later | E-F3-24 actions | list | no | yes |
| Thresholds | E-F3-24 default thresholds | numbers | yes | yes |
| Start mode | E-F3-24 default mode | Suggestion | no | yes |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Switch on | row | the administrator, the user who may create agents | an agent is created in suggestion mode (BR-F3-44) |
| Copy and change | row | the same | a company agent to edit (UC-F3-10) |
| Read what it does | row | every user of the screen | the template's page |

## States

- Normal: the templates of the chosen filter with what each reads and may do.
- Empty: No template for this capability yet.
- Loading: The catalogue loads first; the counts of agents using each template follow.
- Error: the error message pattern (D122); a template that needs another capability says which.
- Read-only: a withdrawn template: its description and the agents already using it.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-F3-24 Agent template](../../data/e-f03-24-agent-template.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F3-24 Agent template | Draft | Badge "Draft"; a new record starts here; next: Published (UC-F3-21); fields editable within the role | U07, U05 | `u07-administrator/s-f03-25-agent-catalogue-e-f03-24-agent-template-draft-desktop-{light,dark}.png`, `u05-accounting/s-f03-25-agent-catalogue-e-f03-24-agent-template-draft-desktop-{light,dark}.png` |
| E-F3-24 Agent template | Published | Badge "Published"; next: Withdrawn (UC-F3-21); fields editable within the role | U07, U05 | `u07-administrator/s-f03-25-agent-catalogue-e-f03-24-agent-template-published-desktop-{light,dark}.png`, `u05-accounting/s-f03-25-agent-catalogue-e-f03-24-agent-template-published-desktop-{light,dark}.png` |
| E-F3-24 Agent template | Withdrawn | Badge "Withdrawn"; final: read-only, no next state; the history shows how it got here | U07, U05 | `u07-administrator/s-f03-25-agent-catalogue-e-f03-24-agent-template-withdrawn-desktop-{light,dark}.png`, `u05-accounting/s-f03-25-agent-catalogue-e-f03-24-agent-template-withdrawn-desktop-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop; on a phone, the templates can be read and an agent switched on with the default thresholds.

## Accessibility

Each template is a table row with its limits in words; keyboard: next template, switch on.

## Components

- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)
- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-14 Timeline](../../../../04-ux/design-system/components/c-14-timeline.md)
- [C-01 Button](../../../../04-ux/design-system/components/c-01-button.md)

## Shown in

- [FL-F3-13 Voice, agents and briefings](../../flows/fl-f03-13-voice-agents-and-briefings.md)

## Open questions

None.

---

⬅️ [S-F3-24 Voice mode](s-f03-24-voice-mode.md) · ⬆️ [Up](README.md) ·
➡️ [S-F3-26 Spreadsheet add-in](s-f03-26-spreadsheet-add-in.md)
