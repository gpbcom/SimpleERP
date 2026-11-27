🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) › 🤖 [F3 Assistant](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-F3-08 Manage and share conversations](README.md) ›
🖥️ S-F3-10 Share a conversation

# 🖥️ S-F3-10 Share a conversation

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

Choose who sees a conversation, and stop sharing (D178).

## Entry points

Share in the history or the panel.

## Wireframe

```text
+-------------------------------------------+
| Share "Turnover analysis"                 |
|-------------------------------------------|
| [Add colleagues or a team...]             |
|  Paul Martin                    [Remove]  |
|  Team Sales                     [Remove]  |
| They will see this conversation as you    |
| saw it, including its figures.            |
|         [Stop sharing]   [Done]           |
+-------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F3-08 step 2, U13 | desktop | ![FL-F3-08 step 2, U13, light](../../images/08-manage-and-share-conversations/u13-owner/2-share-desktop-light.png) | ![FL-F3-08 step 2, U13, dark](../../images/08-manage-and-share-conversations/u13-owner/2-share-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f03-10-share-a-conversation-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f03-10-share-a-conversation-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f03-10-share-a-conversation-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f03-10-share-a-conversation-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f03-10-share-a-conversation-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f03-10-share-a-conversation-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f03-10-share-a-conversation-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f03-10-share-a-conversation-offline-phone-dark.png) |

## Fields and columns

Colleagues and teams; the warning of D144.

## Actions

| Action | Who | Result |
|---|---|---|
| Add | owner | Shared, colleague notified |
| Remove | owner | Closed for that colleague |
| Stop sharing | owner | Closed for all |

## States

- Normal: Choose who sees a conversation, and stop sharing (D178), as the wireframe shows.
- Empty: Not shared: only the owner sees it.
- Loading: placeholders in the layout of the wireframe; actions are disabled until the record has loaded.
- Error: the error message pattern (D122).
- Read-only: for colleagues the conversation is shared with.
- Offline: Not available offline (D38): on a phone or a computer, the offline banner replaces the actions and nothing is
  changed until the network is back; nothing is queued.
- Not shared, shared.

Shown entities (VD-15): [E-F3-01 Conversation](../../data/e-f03-01-conversation.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F3-01 Conversation | Private | Badge "Private"; a new record starts here; next: Shared or Deleted (UC-F3-01, UC-F3-08); fields editable within the role | U13 | `u13-owner/s-f03-10-share-a-conversation-e-f03-01-conversation-private-{desktop,phone}-{light,dark}.png` |
| E-F3-01 Conversation | Shared | Badge "Shared"; next: Private or Deleted (UC-F15-01, UC-F3-08); fields editable within the role | U13 | `u13-owner/s-f03-10-share-a-conversation-e-f03-01-conversation-shared-{desktop,phone}-{light,dark}.png` |
| E-F3-01 Conversation | Deleted | Not shown: the record is gone in this state, so no screen shows it | U13 | None: system state, the user never sees it |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop and phone.

## Accessibility

A modal with focus kept inside; the warning is read first.

## Components

- [C-05 Modal](../../../../04-ux/design-system/components/c-05-modal.md)
- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)

## Shown in

- [FL-F3-08 Manage and share conversations](../../flows/fl-f03-08-manage-and-share-conversations.md)

## Open questions

None.

---

⬅️ [S-F3-09 Conversation history](s-f03-09-conversation-history.md) · ⬆️ [Up](README.md) ·
➡️ [S-F3-11 Phone assistant](../09-assistant-on-a-phone/s-f03-11-phone-assistant.md)
