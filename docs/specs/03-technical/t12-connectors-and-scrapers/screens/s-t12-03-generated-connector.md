🏠 [Specs](../../../README.md) › ⚙️ [Technical capabilities](../../README.md) ›
🕸️ [T12 Connectors and scrapers](../README.md) › 🖥️ [Screens](README.md) › 🖥️ S-T12-03 Generated connector

# 🖥️ S-T12-03 Generated connector

**Status:** 🔄 (Proposed) drawn in step 36j from its entity and list page; waits for the owner

## Personas

- [U07 Administrator](../../../01-users/personas/u07-administrator.md)

(Proposed) Each persona sees the fields and the actions its roles allow, as on
[S-T12-L03 Generated connectors](00-lists/s-t12-l03-generated-connectors.md): the record rules and field rules of T2.

## Purpose

(Proposed) See one [E-T12-03 Generated connector](../data/e-t12-03-generated-connector.md) and act on it: its fields,
its state and the changes its state allows. It is the page the rows of
[S-T12-L03 Generated connectors](00-lists/s-t12-l03-generated-connectors.md) open (VR-13).

## Entry points

- [S-T12-L03 Generated connectors](00-lists/s-t12-l03-generated-connectors.md) › a row's Open ›.
- (Proposed) A link to the record wherever another page names it, and global search.
- The flows of Shown in.

## Wireframe

```text
+--------------------------------------------------------------------------+
| < Generated connectors   https://portal.example                    [New] |
|--------------------------------------------------------------------------|
| target                 https://portal.example                            |
| attempts               3                                                 |
| cost                   0.40 EUR                                          |
| tests                  passed                                            |
| review                 approved                                          |
|--------------------------------------------------------------------------|
| History: every change, by whom and when                                  |
|--------------------------------------------------------------------------|
| [Edit]   [Change state v]   [Ask the AI assistant]                       |
+--------------------------------------------------------------------------+
```

**Example images** (drawn from its wireframe, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| New (Generated connector), U07 | desktop | ![New (Generated connector), U07, light](../images/states/u07-administrator/s-t12-03-generated-connector-e-t12-03-generated-connector-new-desktop-light.png) | ![New (Generated connector), U07, dark](../images/states/u07-administrator/s-t12-03-generated-connector-e-t12-03-generated-connector-new-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../images/states/s-t12-03-generated-connector-empty-desktop-light.png) | ![Empty, dark](../images/states/s-t12-03-generated-connector-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../images/states/s-t12-03-generated-connector-loading-desktop-light.png) | ![Loading, dark](../images/states/s-t12-03-generated-connector-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../images/states/s-t12-03-generated-connector-read-only-desktop-light.png) | ![Read-only, dark](../images/states/s-t12-03-generated-connector-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../images/states/s-t12-03-generated-connector-offline-desktop-light.png) | ![Offline, dark](../images/states/s-t12-03-generated-connector-offline-desktop-dark.png) |

## Fields and columns

As [E-T12-03 Generated connector](../data/e-t12-03-generated-connector.md#fields). (Proposed) A field is read-only when
the record's state is final or the role's field rules lock it; personal-data fields show only to the roles that may read
them (VR-12); secrets never show.

## Actions

| Action | Who | Result |
|---|---|---|
| Edit | the personas whose roles may change it | (Proposed) saves the fields; audited |
| Change state | the personas whose roles may change it | (Proposed) one of the Lifecycle's transitions: New to Available (REQ-T12-01) |
| Ask the AI assistant | every persona of the page | (Proposed) an answer about this record from the data the user may see, with its sources |
| Back to the list | every persona of the page | [S-T12-L03 Generated connectors](00-lists/s-t12-l03-generated-connectors.md) |

## States

- Normal: the record with its fields, its state badge and the actions its state allows, as the wireframe shows.
- Empty: never: a record page always has its record.
- Loading: placeholders in the layout of the wireframe; actions are disabled until the record has loaded.
- Error: the error message pattern (D122); what was typed stays.
- Read-only: a record in a final state, or a role that may only read it.
- Offline: not available offline: a back-office screen on live, shared data (D38). The app shows that it is offline and
  reloads the screen when the network is back.

Shown entities (VD-15): [E-T12-03 Generated connector](../data/e-t12-03-generated-connector.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-T12-03 Generated connector | New | Badge "New"; a new record starts here; next: Available (REQ-T12-01); fields editable within the role | U07 | `u07-administrator/s-t12-03-generated-connector-e-t12-03-generated-connector-new-desktop-{light,dark}.png` |
| E-T12-03 Generated connector | Available | Badge "Available"; final: read-only, no next state; the history shows how it got here | U07 | `u07-administrator/s-t12-03-generated-connector-e-t12-03-generated-connector-available-desktop-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

(Proposed) Desktop and tablet; on a phone the fields stack in one column and the actions move to a menu.

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

- [S-T12-L03 Generated connectors](00-lists/s-t12-l03-generated-connectors.md)

## Open questions

None.

---

⬅️ [S-T12-02 Credential](s-t12-02-credential.md) · ⬆️ [Up](README.md) ·
➡️ [S-T12-04 Connector run](s-t12-04-connector-run.md)
