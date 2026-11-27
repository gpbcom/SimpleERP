🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) › 🤖 [F3 Assistant](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-F3-08 Manage and share conversations](README.md) ›
🖥️ S-F3-09 Conversation history

# 🖥️ S-F3-09 Conversation history

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

Find, organise and manage one's conversations (D180).

## Entry points

History in the AI assistant panel; Assistant › Conversations in full screen.

## Wireframe

```text
+------------------------------------------------------------------+
| Conversations      [Search...]   Folder [All v]  Tag [All v]      |
|------------------------------------------------------------------|
| * Turnover analysis      Sales review  #q4   shared (2)  14:20   |
|   Reminder for Durand    -             -                 Monday  |
|   Shared with me: Plan next week (Paul Martin)            Friday  |
|------------------------------------------------------------------|
| [Rename] [Pin] [Move] [Tag] [Share] [Export] [Delete]             |
+------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F3-08 step 1, U13 | desktop | ![FL-F3-08 step 1, U13, light](../../images/08-manage-and-share-conversations/u13-owner/1-history-desktop-light.png) | ![FL-F3-08 step 1, U13, dark](../../images/08-manage-and-share-conversations/u13-owner/1-history-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f03-09-conversation-history-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f03-09-conversation-history-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f03-09-conversation-history-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f03-09-conversation-history-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f03-09-conversation-history-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f03-09-conversation-history-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f03-09-conversation-history-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f03-09-conversation-history-offline-phone-dark.png) |

## Fields and columns

Title, folder, tags, shared with, last message; "Shared with me" apart.

## Actions

| Action | Who | Result |
|---|---|---|
| Search | owner | Matching conversations |
| Rename, pin, move, tag | owner | Organised |
| Share | owner | The share dialog |
| Export | owner | A document |
| Delete | owner | Deleted after confirmation |

## States

- Normal: Find, organise and manage one's conversations (D180), as the wireframe shows.
- Empty: "Your conversations will appear here."
- Loading: skeleton rows in place of the list ([C-03](../../../../04-ux/design-system/components/c-03-data-table.md));
  actions are disabled until it has loaded.
- Error: the error message pattern (D122).
- Read-only: conversations shared with the user, which they continue as a copy (BR-F3-25).
- Offline: The AI assistant says it is offline; questions are queued and answered when the network is back, with a
  notification, and changes still need confirmation then
  ([D182](../../../../06-decisions/f03-assistant/d182-offline-assistant.md)).
- A deletion warning on conversations due within a week.

Shown entities (VD-15): [E-F3-01 Conversation](../../data/e-f03-01-conversation.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F3-01 Conversation | Private | Badge "Private"; a new record starts here; next: Shared or Deleted (UC-F3-01, UC-F3-08); fields editable within the role | U13 | `u13-owner/s-f03-09-conversation-history-e-f03-01-conversation-private-{desktop,phone}-{light,dark}.png` |
| E-F3-01 Conversation | Deleted | Not shown: the record is gone in this state, so no screen shows it | U13 | None: system state, the user never sees it |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop: in the panel or full screen. Phone: full screen (UC-F3-09).

## Accessibility

A list with labelled actions; pinned is announced.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-10 Empty state](../../../../04-ux/design-system/components/c-10-empty-state.md)

## Shown in

- [FL-F3-08 Manage and share conversations](../../flows/fl-f03-08-manage-and-share-conversations.md)

## Open questions

None.

---

⬅️ [S-F3-08 Knowledge item editor](../07-manage-knowledge/s-f03-08-knowledge-item-editor.md) · ⬆️ [Up](README.md) ·
➡️ [S-F3-10 Share a conversation](s-f03-10-share-a-conversation.md)
