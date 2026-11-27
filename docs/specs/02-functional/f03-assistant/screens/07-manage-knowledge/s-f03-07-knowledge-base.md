🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) › 🤖 [F3 Assistant](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-F3-07 Manage knowledge](README.md) › 🖥️ S-F3-07 Knowledge base

# 🖥️ S-F3-07 Knowledge base

**Status:** ✅ specified

## Personas

- [U06 HR](../../../../01-users/personas/u06-hr.md)
- [U07 Administrator](../../../../01-users/personas/u07-administrator.md)
- [U13 Owner](../../../../01-users/personas/u13-owner.md)
- Knowledge editors they name per folder (D176)
- Every internal persona proposes items and fixes (D176)

## Purpose

Browse, add, review and approve the company's knowledge.

## Entry points

Assistant › Knowledge base; a review reminder; a proposal notification.

## Wireframe

```text
+------------------------------------------------------------------+
| Knowledge base         [Search...]  [+ Add]  [Proposals (2)]      |
|------------------------------------------------------------------|
| Folders          | Item                  | Audience | Review     |
| > HR policies    | Expense policy        | Everyone | 2027-03    |
| > Procedures     | Returns               | Sales    | TO REVIEW  |
| > Lyon site (S)  | Site safety (synced)  | Lyon     | 2027-01    |
|------------------------------------------------------------------|
| [Propose an item]                                                 |
+------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F3-07 step 1, U06 | desktop | ![FL-F3-07 step 1, U06, light](../../images/07-manage-knowledge/u06-hr/1-browse-desktop-light.png) | ![FL-F3-07 step 1, U06, dark](../../images/07-manage-knowledge/u06-hr/1-browse-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f03-07-knowledge-base-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f03-07-knowledge-base-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f03-07-knowledge-base-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f03-07-knowledge-base-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f03-07-knowledge-base-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f03-07-knowledge-base-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f03-07-knowledge-base-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f03-07-knowledge-base-offline-desktop-dark.png) |

## Fields and columns

Folders; items with audience, review date, owner, origin (uploaded, page, synced).

## Actions

| Action | Who | Result |
|---|---|---|
| Add | managers, editors | The item editor |
| Propose an item or fix | every internal persona | A proposal to the editors |
| Approve, decline | managers, editors | The proposer is told |
| Mark reviewed | the item's owner | A new review date |
| Name editors | HR, administrators, owner | Editors of a folder |

## States

- Normal: Browse, add, review and approve the company's knowledge, as the wireframe shows.
- Empty: "Add your first procedure, or sync a shared folder."
- Loading: skeleton rows in place of the list ([C-03](../../../../04-ux/design-system/components/c-03-data-table.md));
  actions are disabled until it has loaded.
- Error: the error message pattern (D122).
- Read-only: for users without the right to change it.
- Offline: Not available offline (D38): on a phone or a computer, the offline banner replaces the actions and nothing is
  changed until the network is back; nothing is queued.
- Items to review highlighted.
- A sync failed: a banner.
- Read only for users who are not editors, with Propose.

Shown entities (VD-15): [E-F3-11 Knowledge proposal](../../data/e-f03-11-knowledge-proposal.md),
[E-F3-09 Knowledge item](../../data/e-f03-09-knowledge-item.md),
[E-F3-10 Knowledge folder](../../data/e-f03-10-knowledge-folder.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F3-11 Knowledge proposal | Open | Badge "Open"; a new record starts here; next: Approved or Declined (UC-F3-19, UC-F3-07); fields editable within the role | U06, U07, U13 | `u06-hr/s-f03-07-knowledge-base-e-f03-11-knowledge-proposal-open-desktop-{light,dark}.png`, `u07-administrator/s-f03-07-knowledge-base-e-f03-11-knowledge-proposal-open-desktop-{light,dark}.png`, `u13-owner/s-f03-07-knowledge-base-e-f03-11-knowledge-proposal-open-{desktop,phone}-{light,dark}.png` |
| E-F3-11 Knowledge proposal | Approved | Badge "Approved"; final: read-only, no next state; the history shows how it got here | U06, U07, U13 | `u06-hr/s-f03-07-knowledge-base-e-f03-11-knowledge-proposal-approved-desktop-{light,dark}.png`, `u07-administrator/s-f03-07-knowledge-base-e-f03-11-knowledge-proposal-approved-desktop-{light,dark}.png`, `u13-owner/s-f03-07-knowledge-base-e-f03-11-knowledge-proposal-approved-{desktop,phone}-{light,dark}.png` |
| E-F3-11 Knowledge proposal | Declined | Badge "Declined"; final: read-only, no next state; the history shows how it got here | U06, U07, U13 | `u06-hr/s-f03-07-knowledge-base-e-f03-11-knowledge-proposal-declined-desktop-{light,dark}.png`, `u07-administrator/s-f03-07-knowledge-base-e-f03-11-knowledge-proposal-declined-desktop-{light,dark}.png`, `u13-owner/s-f03-07-knowledge-base-e-f03-11-knowledge-proposal-declined-{desktop,phone}-{light,dark}.png` |
| E-F3-09 Knowledge item | Draft | Badge "Draft"; a new record starts here; next: Published (UC-F3-07); fields editable within the role | U06, U07, U13 | `u06-hr/s-f03-07-knowledge-base-e-f03-09-knowledge-item-draft-desktop-{light,dark}.png`, `u07-administrator/s-f03-07-knowledge-base-e-f03-09-knowledge-item-draft-desktop-{light,dark}.png`, `u13-owner/s-f03-07-knowledge-base-e-f03-09-knowledge-item-draft-{desktop,phone}-{light,dark}.png` |
| E-F3-09 Knowledge item | Published | Badge "Published"; next: To review or Removed (UC-F3-07); fields editable within the role | U06, U07, U13 | `u06-hr/s-f03-07-knowledge-base-e-f03-09-knowledge-item-published-desktop-{light,dark}.png`, `u07-administrator/s-f03-07-knowledge-base-e-f03-09-knowledge-item-published-desktop-{light,dark}.png`, `u13-owner/s-f03-07-knowledge-base-e-f03-09-knowledge-item-published-{desktop,phone}-{light,dark}.png` |
| E-F3-09 Knowledge item | To review | Badge "To review"; next: Published (UC-F3-07); fields editable within the role | U06, U07, U13 | `u06-hr/s-f03-07-knowledge-base-e-f03-09-knowledge-item-to-review-desktop-{light,dark}.png`, `u07-administrator/s-f03-07-knowledge-base-e-f03-09-knowledge-item-to-review-desktop-{light,dark}.png`, `u13-owner/s-f03-07-knowledge-base-e-f03-09-knowledge-item-to-review-{desktop,phone}-{light,dark}.png` |
| E-F3-10 Knowledge folder | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U06, U07, U13 | `u06-hr/s-f03-07-knowledge-base-e-f03-10-knowledge-folder-active-desktop-{light,dark}.png`, `u07-administrator/s-f03-07-knowledge-base-e-f03-10-knowledge-folder-active-desktop-{light,dark}.png`, `u13-owner/s-f03-07-knowledge-base-e-f03-10-knowledge-folder-active-{desktop,phone}-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop; read and propose on a phone.

## Accessibility

A tree and a table, both keyboard-navigable; "to review" is text, not colour alone.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-08 Navigation](../../../../04-ux/design-system/components/c-08-navigation.md)
- [C-10 Empty state](../../../../04-ux/design-system/components/c-10-empty-state.md)

## Shown in

- [FL-F3-07 Manage knowledge](../../flows/fl-f03-07-manage-knowledge.md)

## Open questions

None.

---

⬅️ [S-F3-06 My connections](../06-use-an-outside-tool/s-f03-06-my-connections.md) · ⬆️ [Up](README.md) ·
➡️ [S-F3-08 Knowledge item editor](s-f03-08-knowledge-item-editor.md)
