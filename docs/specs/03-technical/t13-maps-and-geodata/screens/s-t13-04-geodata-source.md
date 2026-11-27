🏠 [Specs](../../../README.md) › ⚙️ [Technical capabilities](../../README.md) › 🗺️ [T13 Maps and geodata](../README.md) ›
🖥️ [Screens](README.md) › 🖥️ S-T13-04 Geodata source

# 🖥️ S-T13-04 Geodata source

**Status:** ✅ specified

## Personas

- [U07 Administrator](../../../01-users/personas/u07-administrator.md)

Each persona sees the fields and the actions its roles allow, as on
[S-T13-L04 Geodata sources](00-lists/s-t13-l04-geodata-sources.md): the record rules and field rules of T2.

## Purpose

See one [E-T13-04 Geodata source](../data/e-t13-04-geodata-source.md) and act on it: its fields, its state
and the changes its state allows. It is the page the rows of
[S-T13-L04 Geodata sources](00-lists/s-t13-l04-geodata-sources.md) open (VR-13).

## Entry points

- [S-T13-L04 Geodata sources](00-lists/s-t13-l04-geodata-sources.md) › a row's Open ›.
- A link to the record wherever another page names it, and global search.
- The flows of Shown in.

## Wireframe

```text
+--------------------------------------------------------------------------+
| < Geodata sources   OpenStreetMap France extract             [Importing] |
|--------------------------------------------------------------------------|
| name                   OpenStreetMap France extract                      |
| kind                   tiles                                             |
| coverage               FR                                                |
| origin                 the publisher's download page                     |
| licence                ODbL                                              |
| attribution            © OpenStreetMap contributors                      |
| version                2026-11-04                                        |
| update period          30                                                |
| hosted                 self-hosted                                       |
|--------------------------------------------------------------------------|
| History: every change, by whom and when                                  |
|--------------------------------------------------------------------------|
| [Edit]   [Change state v]   [Ask the AI assistant]                       |
+--------------------------------------------------------------------------+
```

**Example images** (drawn from its wireframe, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| Importing (Geodata source), U07 | desktop | ![Importing (Geodata source), U07, light](../images/states/u07-administrator/s-t13-04-geodata-source-e-t13-04-geodata-source-importing-desktop-light.png) | ![Importing (Geodata source), U07, dark](../images/states/u07-administrator/s-t13-04-geodata-source-e-t13-04-geodata-source-importing-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../images/states/s-t13-04-geodata-source-empty-desktop-light.png) | ![Empty, dark](../images/states/s-t13-04-geodata-source-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../images/states/s-t13-04-geodata-source-loading-desktop-light.png) | ![Loading, dark](../images/states/s-t13-04-geodata-source-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../images/states/s-t13-04-geodata-source-read-only-desktop-light.png) | ![Read-only, dark](../images/states/s-t13-04-geodata-source-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../images/states/s-t13-04-geodata-source-offline-desktop-light.png) | ![Offline, dark](../images/states/s-t13-04-geodata-source-offline-desktop-dark.png) |

## Fields and columns

As [E-T13-04 Geodata source](../data/e-t13-04-geodata-source.md#fields). A field is read-only when the
record's state is final or the role's field rules lock it; personal-data fields show only to the roles that may read
them (VR-12); secrets never show.

## Actions

| Action | Who | Result |
|---|---|---|
| Edit | the personas whose roles may change it | saves the fields; audited |
| Change state | the personas whose roles may change it | one of the Lifecycle's transitions: Importing to Active (REQ-T13-01); Importing to Failed (REQ-T13-01); Failed to Importing (REQ-T13-01); Active to Outdated (REQ-T13-01); Outdated to Importing (REQ-T13-01); Active to Retired (REQ-T13-01); Outdated to Retired (REQ-T13-01) |
| Ask the AI assistant | every persona of the page | an answer about this record from the data the user may see, with its sources |
| Back to the list | every persona of the page | [S-T13-L04 Geodata sources](00-lists/s-t13-l04-geodata-sources.md) |

## States

- Normal: the record with its fields, its state badge and the actions its state allows, as the wireframe shows.
- Empty: never: a record page always has its record.
- Loading: placeholders in the layout of the wireframe; actions are disabled until the record has loaded.
- Error: the error message pattern (D122); what was typed stays.
- Read-only: a record in a final state, or a role that may only read it.
- Offline: not available offline: a back-office screen on live, shared data (D38). The app shows that it is offline and
  reloads the screen when the network is back.

Shown entities (VD-15): [E-T13-04 Geodata source](../data/e-t13-04-geodata-source.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-T13-04 Geodata source | Importing | Badge "Importing"; a new record starts here; next: Active or Failed (REQ-T13-01); fields editable within the role | U07 | `u07-administrator/s-t13-04-geodata-source-e-t13-04-geodata-source-importing-desktop-{light,dark}.png` |
| E-T13-04 Geodata source | Active | Badge "Active"; next: Outdated or Retired (REQ-T13-01); fields editable within the role | U07 | `u07-administrator/s-t13-04-geodata-source-e-t13-04-geodata-source-active-desktop-{light,dark}.png` |
| E-T13-04 Geodata source | Failed | Badge "Failed"; next: Importing (REQ-T13-01); fields editable within the role | U07 | `u07-administrator/s-t13-04-geodata-source-e-t13-04-geodata-source-failed-desktop-{light,dark}.png` |
| E-T13-04 Geodata source | Outdated | Badge "Outdated"; next: Importing or Retired (REQ-T13-01); fields editable within the role | U07 | `u07-administrator/s-t13-04-geodata-source-e-t13-04-geodata-source-outdated-desktop-{light,dark}.png` |
| E-T13-04 Geodata source | Retired | Badge "Retired"; final: read-only, no next state; the history shows how it got here | U07 | `u07-administrator/s-t13-04-geodata-source-e-t13-04-geodata-source-retired-desktop-{light,dark}.png` |

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

- [S-T13-L04 Geodata sources](00-lists/s-t13-l04-geodata-sources.md)

## Open questions

None.

---

⬆️ [Up](README.md)
