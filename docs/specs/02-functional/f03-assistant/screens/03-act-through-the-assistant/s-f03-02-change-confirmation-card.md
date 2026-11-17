🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) › 🤖 [F3 Assistant](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-F3-03 Act through the AI assistant](README.md) ›
🖥️ S-F3-02 Change confirmation card

# 🖥️ S-F3-02 Change confirmation card

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

Show exactly what the AI assistant will change, and get the user's confirmation (D140).

## Entry points

Inside the AI assistant panel, after a change request.

## Wireframe

```text
+-------------------------------------------+
| I will change 12 tasks:                   |
|  Task        | Due date                   |
|  T-81 Visit  | 12 Nov  ->  19 Nov         |
|  T-82 Call   | 13 Nov  ->  20 Nov   [edit]|
|  ... 10 more [show all]                   |
|          [Cancel]  [Confirm 12 changes]   |
|-------------------------------------------|
| Done: 12 tasks moved.            [Undo]   |
+-------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F3-03 step 2, U02 | desktop | ![FL-F3-03 step 2, U02, light](../../images/03-act-through-the-assistant/u02-manager/2-confirmation-card-desktop-light.png) | ![FL-F3-03 step 2, U02, dark](../../images/03-act-through-the-assistant/u02-manager/2-confirmation-card-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f03-02-change-confirmation-card-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f03-02-change-confirmation-card-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f03-02-change-confirmation-card-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f03-02-change-confirmation-card-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f03-02-change-confirmation-card-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f03-02-change-confirmation-card-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f03-02-change-confirmation-card-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f03-02-change-confirmation-card-offline-phone-dark.png) |

## Fields and columns

Record, field, before, after; for a new record, its fields.

## Actions

| Action | Who | Result |
|---|---|---|
| Edit a value | the user | The card is updated |
| Confirm | the user | Changes made |
| Cancel | the user | Nothing changed |
| Undo | the user | Batch reverted, if untouched since |

## States

- Normal: Show exactly what the AI assistant will change, and get the user's confirmation (D140), as the wireframe
  shows.
- Empty: never: the card opens only with a change to confirm.
- Loading: skeleton rows in place of the list ([C-03](../../../../04-ux/design-system/components/c-03-data-table.md));
  actions are disabled until it has loaded.
- Error: the error message pattern (D122).
- Read-only: a done or undone batch.
- Offline: The AI assistant says it is offline; questions are queued and answered when the network is back, with a
  notification, and changes still need confirmation then
  ([D182](../../../../06-decisions/f03-assistant/d182-offline-assistant.md)).
- Waiting for confirmation.
- Done, with Undo.
- Partly done: skipped records and why.
- Undone.
- Undo unavailable: who changed what.

Shown entities (VD-15): [E-F3-22 AI assistant request](../../data/e-f03-22-ai-assistant-request.md),
[E-F3-04 Assistant change batch](../../data/e-f03-04-assistant-change-batch.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F3-22 AI assistant request | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U02, U03 | `u02-manager/s-f03-02-change-confirmation-card-e-f03-22-ai-assistant-request-active-{desktop,phone}-{light,dark}.png`, `u03-sales/s-f03-02-change-confirmation-card-e-f03-22-ai-assistant-request-active-{desktop,phone,tablet}-{light,dark}.png` |
| E-F3-04 Assistant change batch | Proposed | Badge "Proposed"; a new record starts here; next: Cancelled, Done or Partly done (UC-F3-03, BR-F3-09); fields editable within the role | U02, U03 | `u02-manager/s-f03-02-change-confirmation-card-e-f03-04-assistant-change-batch-proposed-{desktop,phone}-{light,dark}.png`, `u03-sales/s-f03-02-change-confirmation-card-e-f03-04-assistant-change-batch-proposed-{desktop,phone,tablet}-{light,dark}.png` |
| E-F3-04 Assistant change batch | Done | Badge "Done"; next: Undone (UC-F3-03); fields editable within the role | U02, U03 | `u02-manager/s-f03-02-change-confirmation-card-e-f03-04-assistant-change-batch-done-{desktop,phone}-{light,dark}.png`, `u03-sales/s-f03-02-change-confirmation-card-e-f03-04-assistant-change-batch-done-{desktop,phone,tablet}-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop: in the panel. Phone: full width, rows as cards.

## Accessibility

The card is a table with headers; Confirm states the number of changes.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-01 Button](../../../../04-ux/design-system/components/c-01-button.md)
- [C-11 Chat panel](../../../../04-ux/design-system/components/c-11-chat-panel.md)

## Shown in

- [FL-F3-03 Act through the AI assistant](../../flows/fl-f03-03-act-through-the-assistant.md)

## Open questions

None.

---

⬅️ [S-F3-01 Assistant panel](../01-ask-the-assistant/s-f03-01-assistant-panel.md) · ⬆️ [Up](README.md) ·
➡️ [S-F3-03 Writing style settings](../04-summarise-or-draft/s-f03-03-writing-style-settings.md)
