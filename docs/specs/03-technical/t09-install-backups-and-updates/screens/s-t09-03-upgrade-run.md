🏠 [Specs](../../../README.md) › ⚙️ [Technical capabilities](../../README.md) ›
🚀 [T9 Install, backups and updates](../README.md) › 🖥️ [Screens](README.md) › 🖥️ S-T09-03 Upgrade run

# 🖥️ S-T09-03 Upgrade run

**Status:** ✅ specified

## Personas

- [U07 Administrator](../../../01-users/personas/u07-administrator.md)
- [U48 Hosting engineer](../../../01-users/personas/u48-hosting-engineer.md)

Each persona sees the fields and the actions its roles allow, as on
[S-T09-L03 Upgrade runs](00-lists/s-t09-l03-upgrade-runs.md): the record rules and field rules of T2.

## Purpose

See one [E-T09-03 Upgrade run](../data/e-t09-03-upgrade-run.md) and act on it: its fields, its state and the
changes its state allows. It is the page the rows of [S-T09-L03 Upgrade runs](00-lists/s-t09-l03-upgrade-runs.md) open
(VR-13).

## Entry points

- [S-T09-L03 Upgrade runs](00-lists/s-t09-l03-upgrade-runs.md) › a row's Open ›.
- A link to the record wherever another page names it, and global search.
- The flows of Shown in.

## Wireframe

```text
+--------------------------------------------------------------------------+
| < Upgrade runs   3.3                                          [Recorded] |
|--------------------------------------------------------------------------|
| from, to, copy result, 3.3, 3.4, passed, passed                          |
|--------------------------------------------------------------------------|
| History: every change, by whom and when                                  |
|--------------------------------------------------------------------------|
| [Edit]   [Change state v]   [Ask the AI assistant]                       |
+--------------------------------------------------------------------------+
```

**Example images** (drawn from its wireframe, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| Recorded (Upgrade run), U07 | desktop | ![Recorded (Upgrade run), U07, light](../images/states/u07-administrator/s-t09-03-upgrade-run-e-t09-03-upgrade-run-recorded-desktop-light.png) | ![Recorded (Upgrade run), U07, dark](../images/states/u07-administrator/s-t09-03-upgrade-run-e-t09-03-upgrade-run-recorded-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../images/states/s-t09-03-upgrade-run-empty-desktop-light.png) | ![Empty, dark](../images/states/s-t09-03-upgrade-run-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../images/states/s-t09-03-upgrade-run-loading-desktop-light.png) | ![Loading, dark](../images/states/s-t09-03-upgrade-run-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../images/states/s-t09-03-upgrade-run-read-only-desktop-light.png) | ![Read-only, dark](../images/states/s-t09-03-upgrade-run-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../images/states/s-t09-03-upgrade-run-offline-desktop-light.png) | ![Offline, dark](../images/states/s-t09-03-upgrade-run-offline-desktop-dark.png) |

## Fields and columns

As [E-T09-03 Upgrade run](../data/e-t09-03-upgrade-run.md#fields). A field is read-only when the record's
state is final or the role's field rules lock it; personal-data fields show only to the roles that may read them
(VR-12); secrets never show.

## Actions

| Action | Who | Result |
|---|---|---|
| Edit | the personas whose roles may change it | saves the fields; audited |
| Change state | the personas whose roles may change it | one of the Lifecycle's transitions: none: the record has one state |
| Ask the AI assistant | every persona of the page | an answer about this record from the data the user may see, with its sources |
| Back to the list | every persona of the page | [S-T09-L03 Upgrade runs](00-lists/s-t09-l03-upgrade-runs.md) |

## States

- Normal: the record with its fields, its state badge and the actions its state allows, as the wireframe shows.
- Empty: never: a record page always has its record.
- Loading: placeholders in the layout of the wireframe; actions are disabled until the record has loaded.
- Error: the error message pattern (D122); what was typed stays.
- Read-only: a record in a final state, or a role that may only read it.
- Offline: not available offline: a back-office screen on live, shared data (D38). The app shows that it is offline and
  reloads the screen when the network is back.

Shown entities (VD-15): [E-T09-03 Upgrade run](../data/e-t09-03-upgrade-run.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-T09-03 Upgrade run | Recorded | Badge "Recorded"; a new record starts here; no other state; fields editable within the role | U07, U48 | `u07-administrator/s-t09-03-upgrade-run-e-t09-03-upgrade-run-recorded-desktop-{light,dark}.png`, `u48-hosting-engineer/s-t09-03-upgrade-run-e-t09-03-upgrade-run-recorded-{desktop,phone}-{light,dark}.png` |

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

- [S-T09-L03 Upgrade runs](00-lists/s-t09-l03-upgrade-runs.md)
- [FL-F20-05 Maintenance and releases](../../../02-functional/f20-hosted-support-assistant/flows/fl-f20-05-maintenance-and-releases.md)

## Open questions

None.

---

⬅️ [S-T09-02 Restore point](s-t09-02-restore-point.md) · ⬆️ [Up](README.md) ·
➡️ [S-T09-04 Namespace access grant](s-t09-04-namespace-access-grant.md)
