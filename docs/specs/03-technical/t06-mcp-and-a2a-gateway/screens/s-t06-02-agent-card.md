🏠 [Specs](../../../README.md) › ⚙️ [Technical capabilities](../../README.md) ›
🛰️ [T6 MCP and A2A gateway](../README.md) › 🖥️ [Screens](README.md) › 🖥️ S-T06-02 Agent card

# 🖥️ S-T06-02 Agent card

**Status:** ✅ specified

## Personas

- [U07 Administrator](../../../01-users/personas/u07-administrator.md)

Each persona sees the fields and the actions its roles allow, as on
[S-T06-L02 Agent cards](00-lists/s-t06-l02-agent-cards.md): the record rules and field rules of T2.

## Purpose

See one [E-T06-02 Agent card](../data/e-t06-02-agent-card.md) and act on it: its fields, its state and the
changes its state allows. It is the page the rows of [S-T06-L02 Agent cards](00-lists/s-t06-l02-agent-cards.md) open
(VR-13).

## Entry points

- [S-T06-L02 Agent cards](00-lists/s-t06-l02-agent-cards.md) › a row's Open ›.
- A link to the record wherever another page names it, and global search.
- The flows of Shown in.

## Wireframe

```text
+--------------------------------------------------------------------------+
| < Agent cards   sales                                           [Active] |
|--------------------------------------------------------------------------|
| domain, skills, signat sales, quote, sig                                 |
|--------------------------------------------------------------------------|
| History: every change, by whom and when                                  |
|--------------------------------------------------------------------------|
| [Edit]   [Change state v]   [Ask the AI assistant]                       |
+--------------------------------------------------------------------------+
```

**Example images** (drawn from its wireframe, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| Active (Agent card), U07 | desktop | ![Active (Agent card), U07, light](../images/states/u07-administrator/s-t06-02-agent-card-e-t06-02-agent-card-active-desktop-light.png) | ![Active (Agent card), U07, dark](../images/states/u07-administrator/s-t06-02-agent-card-e-t06-02-agent-card-active-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../images/states/s-t06-02-agent-card-empty-desktop-light.png) | ![Empty, dark](../images/states/s-t06-02-agent-card-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../images/states/s-t06-02-agent-card-loading-desktop-light.png) | ![Loading, dark](../images/states/s-t06-02-agent-card-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../images/states/s-t06-02-agent-card-read-only-desktop-light.png) | ![Read-only, dark](../images/states/s-t06-02-agent-card-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../images/states/s-t06-02-agent-card-offline-desktop-light.png) | ![Offline, dark](../images/states/s-t06-02-agent-card-offline-desktop-dark.png) |

## Fields and columns

As [E-T06-02 Agent card](../data/e-t06-02-agent-card.md#fields). A field is read-only when the record's state
is final or the role's field rules lock it; personal-data fields show only to the roles that may read them (VR-12);
secrets never show.

## Actions

| Action | Who | Result |
|---|---|---|
| Edit | the personas whose roles may change it | saves the fields; audited |
| Change state | the personas whose roles may change it | one of the Lifecycle's transitions: none: the record has one state |
| Ask the AI assistant | every persona of the page | an answer about this record from the data the user may see, with its sources |
| Back to the list | every persona of the page | [S-T06-L02 Agent cards](00-lists/s-t06-l02-agent-cards.md) |

## States

- Normal: the record with its fields, its state badge and the actions its state allows, as the wireframe shows.
- Empty: never: a record page always has its record.
- Loading: placeholders in the layout of the wireframe; actions are disabled until the record has loaded.
- Error: the error message pattern (D122); what was typed stays.
- Read-only: a record in a final state, or a role that may only read it.
- Offline: not available offline: a back-office screen on live, shared data (D38). The app shows that it is offline and
  reloads the screen when the network is back.

Shown entities (VD-15): [E-T06-02 Agent card](../data/e-t06-02-agent-card.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-T06-02 Agent card | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U07 | `u07-administrator/s-t06-02-agent-card-e-t06-02-agent-card-active-desktop-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop and tablet; on a phone the fields stack in one column and the actions move to a menu.

## Accessibility

The state badge has its state as text; Change state is a menu of buttons named by the next state; the history is a list
whose length is announced.

## Components

- [C-01 Button](../../../04-ux/design-system/components/c-01-button.md)
- [C-02 Form field](../../../04-ux/design-system/components/c-02-form-field.md)
- [C-05 Modal](../../../04-ux/design-system/components/c-05-modal.md)
- [C-14 Timeline](../../../04-ux/design-system/components/c-14-timeline.md)

## Shown in

The list page whose rows open this page (Row opens), then the flows whose Entities and screens table names it:

- [S-T06-L02 Agent cards](00-lists/s-t06-l02-agent-cards.md)

## Open questions

None.

---

⬅️ [S-T06-01 Tool](s-t06-01-tool.md) · ⬆️ [Up](README.md) ·
➡️ [S-T06-03 Outside connection](s-t06-03-outside-connection.md)
