🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🛡️ [F1 Administration](../../README.md) › 🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-F1-04 Edit a role](README.md) ›
🖥️ S-F1-06 Role editor

# 🖥️ S-F1-06 Role editor

**Status:** ✅ specified

## Personas

- [U07 Administrator](../../../../01-users/personas/u07-administrator.md)

## Purpose

Copy, edit and compare roles.

## Entry points

Administration › Roles.

## Wireframe

```text
+------------------------------------------------------------------+
| Roles > Sales Lyon (copy of Sales)        4 users   [Save]      |
|------------------------------------------------------------------|
|              See Create Change Delete Approve Export  Rules      |
| Customers    [x]  [x]    [x]    [ ]    [ ]     [ ]   own site    |
| Quotes       [x]  [x]    [x]    [ ]    [x]     [x]   <= 5,000 EUR|
| Invoices     [x]  [ ]    [ ]    [ ]    [ ]     [ ]   own site    |
| Stock        [x]  [ ]    [ ]    [ ]    [ ]     [ ]   -           |
|  ... one row per capability (plugins add theirs)                  |
|                                       [Explain this role (AI)]   |
+------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F1-04 step 1, U07 | desktop | ![FL-F1-04 step 1, U07, light](../../images/04-edit-a-role/u07-administrator/1-copy-a-ready-made-role-desktop-light.png) | ![FL-F1-04 step 1, U07, dark](../../images/04-edit-a-role/u07-administrator/1-copy-a-ready-made-role-desktop-dark.png) |
| Error E1, U07 | desktop | ![Error E1, U07, light](../../images/04-edit-a-role/u07-administrator/e1-ready-made-role-locked-desktop-light.png) | ![Error E1, U07, dark](../../images/04-edit-a-role/u07-administrator/e1-ready-made-role-locked-desktop-dark.png) |
| Error E2, U07 | desktop | ![Error E2, U07, light](../../images/04-edit-a-role/u07-administrator/e2-role-in-use-desktop-light.png) | ![Error E2, U07, dark](../../images/04-edit-a-role/u07-administrator/e2-role-in-use-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f01-06-role-editor-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f01-06-role-editor-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f01-06-role-editor-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f01-06-role-editor-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f01-06-role-editor-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f01-06-role-editor-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f01-06-role-editor-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f01-06-role-editor-offline-desktop-dark.png) |

## Fields and columns

| Column | Data |
|---|---|
| Row | a capability (F...) |
| See, Create, Change, Delete, Approve, Export | allowed or not |
| Rules | record rules of the row (BR-F1-12) |

## Actions

| Action | Who | Result |
|---|---|---|
| Copy | administrator | A new role from this one |
| Save | administrator | Rights change at once |
| Delete | administrator | Refused while users hold it |
| Explain this role | administrator | The AI assistant describes it in plain words |

## States

- Normal: Copy, edit and compare roles, as the wireframe shows.
- Empty: never: the ready-made roles are always there (BR-F1-11).
- Loading: skeleton rows in place of the list ([C-03](../../../../04-ux/design-system/components/c-03-data-table.md));
  actions are disabled until it has loaded.
- Error: deleting a role in use; removing the last administration rights.
- Read-only: for users without the right to change it.
- Offline: Not available offline: a back-office screen on live, shared data (D38: only today's schedule, time and
  intervention records work offline). The app shows that it is offline and reloads the screen when the network is back.
- Ready-made role: read-only, with Copy.

Shown entities (VD-15): [E-F1-06 Role](../../data/e-f01-06-role.md),
[E-F1-07 Record rule](../../data/e-f01-07-record-rule.md),
[E-F1-08 Agent connection](../../data/e-f01-08-agent-connection.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F1-06 Role | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U07 | `u07-administrator/s-f01-06-role-editor-e-f01-06-role-active-desktop-{light,dark}.png` |
| E-F1-07 Record rule | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U07 | `u07-administrator/s-f01-06-role-editor-e-f01-07-record-rule-active-desktop-{light,dark}.png` |
| E-F1-08 Agent connection | Off | Badge "Off"; a new record starts here; next: On (UC-F1-07); fields editable within the role | U07 | `u07-administrator/s-f01-06-role-editor-e-f01-08-agent-connection-off-desktop-{light,dark}.png` |
| E-F1-08 Agent connection | On | Badge "On"; next: Off (UC-F1-07); fields editable within the role | U07 | `u07-administrator/s-f01-06-role-editor-e-f01-08-agent-connection-on-desktop-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop only: the matrix needs the width.

## Accessibility

The matrix is a table with row and column headers; each checkbox is named ("Quotes, Approve").

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-11 Chat panel](../../../../04-ux/design-system/components/c-11-chat-panel.md)

## Shown in

- [FL-F1-04 Edit a role](../../flows/fl-f01-04-edit-a-role.md)

## Open questions

None.

---

⬅️ [S-F1-05 Offboarding](../03-user-lifecycle/s-f01-05-offboarding.md) · ⬆️ [Up](README.md) ·
➡️ [S-F1-07 Connections](../05-connect-an-external-tool/s-f01-07-connections.md)
