🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) › 🤖 [F3 Assistant](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-F3-07 Manage knowledge](README.md) › 🖥️ S-F3-08 Knowledge item editor

# 🖥️ S-F3-08 Knowledge item editor

**Status:** ✅ specified

## Personas

- [U06 HR](../../../../01-users/personas/u06-hr.md)
- [U07 Administrator](../../../../01-users/personas/u07-administrator.md)
- [U13 Owner](../../../../01-users/personas/u13-owner.md)
- Knowledge editors

## Purpose

Add or change one knowledge item, its audience and review.

## Entry points

Knowledge base › Add, or an item's Edit.

## Wireframe

```text
+------------------------------------------------------------------+
| Expense policy                          [Cancel]  [Publish]       |
|------------------------------------------------------------------|
| Source    (o) Upload [expense-policy.pdf]  ( ) Page  ( ) Sync     |
| Folder    [HR policies v]                                         |
| Audience  (o) Everyone ( ) Roles [ ] ( ) Sites or teams [ ]       |
| Owner     [Claire Petit v]   Review every [12 months v]           |
| Summary   [Refunds of travel, meals and ...] (suggested)          |
+------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F3-07 step 2, U06 | desktop | ![FL-F3-07 step 2, U06, light](../../images/07-manage-knowledge/u06-hr/2-add-an-item-desktop-light.png) | ![FL-F3-07 step 2, U06, dark](../../images/07-manage-knowledge/u06-hr/2-add-an-item-desktop-dark.png) |
| Error E1, U06 | desktop | ![Error E1, U06, light](../../images/07-manage-knowledge/u06-hr/e1-file-not-readable-desktop-light.png) | ![Error E1, U06, dark](../../images/07-manage-knowledge/u06-hr/e1-file-not-readable-desktop-dark.png) |
| Error E3, U06 | desktop | ![Error E3, U06, light](../../images/07-manage-knowledge/u06-hr/e3-file-too-large-desktop-light.png) | ![Error E3, U06, dark](../../images/07-manage-knowledge/u06-hr/e3-file-too-large-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f03-08-knowledge-item-editor-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f03-08-knowledge-item-editor-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f03-08-knowledge-item-editor-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f03-08-knowledge-item-editor-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f03-08-knowledge-item-editor-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f03-08-knowledge-item-editor-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f03-08-knowledge-item-editor-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f03-08-knowledge-item-editor-offline-desktop-dark.png) |

## Fields and columns

As [E-F3-09 Knowledge item](../../data/e-f03-09-knowledge-item.md#fields).

## Actions

| Action | Who | Result |
|---|---|---|
| Publish | managers, editors | Indexed for its audience |
| Cancel | managers, editors | Nothing saved |

## States

- Normal: Add or change one knowledge item, its audience and review, as the wireframe shows.
- Empty: a new item with its title, body and audience to fill.
- Loading: placeholders in the layout of the wireframe; actions are disabled until the record has loaded.
- Error: a file not readable, too large, the error message pattern (D122).
- Read-only: an approved item for non-editors, who Propose a change.
- Offline: Not available offline: a back-office screen on live, shared data (D38: only today's schedule, time and
  intervention records work offline). The app shows that it is offline and reloads the screen when the network is back.
- New, changed.

Shown entities (VD-15): [E-F3-09 Knowledge item](../../data/e-f03-09-knowledge-item.md),
[E-F3-10 Knowledge folder](../../data/e-f03-10-knowledge-folder.md),
[E-F3-11 Knowledge proposal](../../data/e-f03-11-knowledge-proposal.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F3-09 Knowledge item | Draft | Badge "Draft"; a new record starts here; next: Published (UC-F3-07); fields editable within the role | U06, U07, U13 | `u06-hr/s-f03-08-knowledge-item-editor-e-f03-09-knowledge-item-draft-desktop-{light,dark}.png`, `u07-administrator/s-f03-08-knowledge-item-editor-e-f03-09-knowledge-item-draft-desktop-{light,dark}.png`, `u13-owner/s-f03-08-knowledge-item-editor-e-f03-09-knowledge-item-draft-{desktop,phone}-{light,dark}.png` |
| E-F3-09 Knowledge item | Published | Badge "Published"; next: To review or Removed (UC-F3-07); fields editable within the role | U06, U07, U13 | `u06-hr/s-f03-08-knowledge-item-editor-e-f03-09-knowledge-item-published-desktop-{light,dark}.png`, `u07-administrator/s-f03-08-knowledge-item-editor-e-f03-09-knowledge-item-published-desktop-{light,dark}.png`, `u13-owner/s-f03-08-knowledge-item-editor-e-f03-09-knowledge-item-published-{desktop,phone}-{light,dark}.png` |
| E-F3-09 Knowledge item | To review | Badge "To review"; next: Published (UC-F3-07); fields editable within the role | U06, U07, U13 | `u06-hr/s-f03-08-knowledge-item-editor-e-f03-09-knowledge-item-to-review-desktop-{light,dark}.png`, `u07-administrator/s-f03-08-knowledge-item-editor-e-f03-09-knowledge-item-to-review-desktop-{light,dark}.png`, `u13-owner/s-f03-08-knowledge-item-editor-e-f03-09-knowledge-item-to-review-{desktop,phone}-{light,dark}.png` |
| E-F3-10 Knowledge folder | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U06, U07, U13 | `u06-hr/s-f03-08-knowledge-item-editor-e-f03-10-knowledge-folder-active-desktop-{light,dark}.png`, `u07-administrator/s-f03-08-knowledge-item-editor-e-f03-10-knowledge-folder-active-desktop-{light,dark}.png`, `u13-owner/s-f03-08-knowledge-item-editor-e-f03-10-knowledge-folder-active-{desktop,phone}-{light,dark}.png` |
| E-F3-11 Knowledge proposal | Open | Badge "Open"; a new record starts here; next: Approved or Declined (UC-F3-19, UC-F3-07); fields editable within the role | U06, U07, U13 | `u06-hr/s-f03-08-knowledge-item-editor-e-f03-11-knowledge-proposal-open-desktop-{light,dark}.png`, `u07-administrator/s-f03-08-knowledge-item-editor-e-f03-11-knowledge-proposal-open-desktop-{light,dark}.png`, `u13-owner/s-f03-08-knowledge-item-editor-e-f03-11-knowledge-proposal-open-{desktop,phone}-{light,dark}.png` |
| E-F3-11 Knowledge proposal | Declined | Badge "Declined"; final: read-only, no next state; the history shows how it got here | U06, U07, U13 | `u06-hr/s-f03-08-knowledge-item-editor-e-f03-11-knowledge-proposal-declined-desktop-{light,dark}.png`, `u07-administrator/s-f03-08-knowledge-item-editor-e-f03-11-knowledge-proposal-declined-desktop-{light,dark}.png`, `u13-owner/s-f03-08-knowledge-item-editor-e-f03-11-knowledge-proposal-declined-{desktop,phone}-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop.

## Accessibility

Labelled fields; the audience choices are a radio group.

## Components

- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)
- [C-12 File upload](../../../../04-ux/design-system/components/c-12-file-upload.md)

## Shown in

- [FL-F3-07 Manage knowledge](../../flows/fl-f03-07-manage-knowledge.md)

## Open questions

None.

---

⬅️ [S-F3-07 Knowledge base](s-f03-07-knowledge-base.md) · ⬆️ [Up](README.md) ·
➡️ [S-F3-09 Conversation history](../08-manage-and-share-conversations/s-f03-09-conversation-history.md)
