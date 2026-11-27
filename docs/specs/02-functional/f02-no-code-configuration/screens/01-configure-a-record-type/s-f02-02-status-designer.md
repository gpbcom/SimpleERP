🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🔧 [F2 No-code configuration](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F2-01 Configure a record type](README.md) › 🖥️ S-F2-02 Status designer

# 🖥️ S-F2-02 Status designer

**Status:** ✅ specified

## Personas

- [U07 Administrator](../../../../01-users/personas/u07-administrator.md)
- Users with the Configurator role (D96, D98)

## Purpose

Draw a record type's statuses and transitions.

## Entry points

Record type editor (S-F2-01) › Statuses.

## Wireframe

```text
+------------------------------------------------------------------+
| Quotes > Statuses          DRAFT        [Preview] [Publish]      |
|------------------------------------------------------------------|
|  (Draft) --> (Waiting for site visit) --> (Sent)* --> (Accepted)* |
|                                  |               \--> (Refused)* |
|  * core status (locked)                                          |
|------------------------------------------------------------------|
| Transition Waiting -> Sent                                       |
|   Needs role [ Manager v ]   Needs fields [ Site visit date x ]   |
|   Colour [indigo]  Icon [send]                                   |
+------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F2-01 step 2, U07 | desktop | ![FL-F2-01 step 2, U07, light](../../images/01-configure-a-record-type/u07-administrator/2-statuses-and-transitions-desktop-light.png) | ![FL-F2-01 step 2, U07, dark](../../images/01-configure-a-record-type/u07-administrator/2-statuses-and-transitions-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f02-02-status-designer-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f02-02-status-designer-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f02-02-status-designer-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f02-02-status-designer-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f02-02-status-designer-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f02-02-status-designer-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f02-02-status-designer-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f02-02-status-designer-offline-desktop-dark.png) |

## Fields and columns

As [E-F2-02 Status and transition](../../data/e-f02-02-status-and-transition.md#fields).

## Actions

| Action | Who | Result |
|---|---|---|
| Add, rename, reorder | configurator | Draft |
| Draw a transition, set conditions | configurator | Draft |
| Remove | configurator | BR-F2-05, BR-F2-06 |
| Publish | configurator | UC-F2-09 |

## States

- Normal: Draw a record type's statuses and transitions, as the wireframe shows.
- Empty: only the record type's start status, with Add status.
- Loading: placeholders in the layout of the wireframe; actions are disabled until the record has loaded.
- Error: the error message pattern (D122).
- Read-only: core statuses are locked (BR-F2-05).
- Offline: Not available offline: a back-office screen on live, shared data (D38: only today's schedule, time and
  intervention records work offline). The app shows that it is offline and reloads the screen when the network is back.
- Draft banner.
- Warning: a status no transition reaches.

Shown entities (VD-15): [E-F2-02 Status and transition](../../data/e-f02-02-status-and-transition.md),
[E-F2-26 Configuration draft](../../data/e-f02-26-configuration-draft.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F2-02 Status and transition | Draft | Badge "Draft"; a new record starts here; next: Published (UC-F2-02); fields editable within the role | U07 | `u07-administrator/s-f02-02-status-designer-e-f02-02-status-and-transition-draft-desktop-{light,dark}.png` |
| E-F2-02 Status and transition | Published | Badge "Published"; final: read-only, no next state; the history shows how it got here | U07 | `u07-administrator/s-f02-02-status-designer-e-f02-02-status-and-transition-published-desktop-{light,dark}.png` |
| E-F2-26 Configuration draft | Open | Badge "Open"; a new record starts here; next: Published or Discarded (UC-F2-09); fields editable within the role | U07 | `u07-administrator/s-f02-02-status-designer-e-f02-26-configuration-draft-open-desktop-{light,dark}.png` |
| E-F2-26 Configuration draft | Published | Badge "Published"; final: read-only, no next state; the history shows how it got here | U07 | `u07-administrator/s-f02-02-status-designer-e-f02-26-configuration-draft-published-desktop-{light,dark}.png` |
| E-F2-26 Configuration draft | Discarded | Badge "Discarded"; final: read-only, no next state; the history shows how it got here | U07 | `u07-administrator/s-f02-02-status-designer-e-f02-26-configuration-draft-discarded-desktop-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop.

## Accessibility

The diagram has a list alternative: each status with its next statuses.

## Components

- [C-07 Tabs](../../../../04-ux/design-system/components/c-07-tabs.md)
- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)

## Shown in

- [FL-F2-01 Configure a record type](../../flows/fl-f02-01-configure-a-record-type.md)

## Open questions

None.

---

⬅️ [S-F2-01 Record type editor](s-f02-01-record-type-editor.md) · ⬆️ [Up](README.md) ·
➡️ [S-F2-03 Form designer](s-f02-03-form-designer.md)
