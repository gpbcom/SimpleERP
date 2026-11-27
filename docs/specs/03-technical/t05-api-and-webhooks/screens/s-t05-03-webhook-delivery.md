🏠 [Specs](../../../README.md) › ⚙️ [Technical capabilities](../../README.md) › 🔗 [T5 API and webhooks](../README.md) ›
🖥️ [Screens](README.md) › 🖥️ S-T05-03 Webhook delivery

# 🖥️ S-T05-03 Webhook delivery

**Status:** 🔄 (Proposed) drawn in step 36j from its entity and list page; waits for the owner

## Personas

- [U07 Administrator](../../../01-users/personas/u07-administrator.md)

(Proposed) Each persona sees the fields and the actions its roles allow, as on
[S-T05-L03 Webhook deliveries](00-lists/s-t05-l03-webhook-deliveries.md): the record rules and field rules of T2.

## Purpose

(Proposed) See one [E-T05-03 Webhook delivery](../data/e-t05-03-webhook-delivery.md) and act on it: its fields, its
state and the changes its state allows. It is the page the rows of
[S-T05-L03 Webhook deliveries](00-lists/s-t05-l03-webhook-deliveries.md) open (VR-13).

## Entry points

- [S-T05-L03 Webhook deliveries](00-lists/s-t05-l03-webhook-deliveries.md) › a row's Open ›.
- (Proposed) A link to the record wherever another page names it, and global search.
- The flows of Shown in.

## Wireframe

```text
+--------------------------------------------------------------------------+
| < Webhook deliveries   S-3                                    [Recorded] |
|--------------------------------------------------------------------------|
| subscription, event, a S-3, E-77, 2, 200                                 |
|--------------------------------------------------------------------------|
| History: every change, by whom and when                                  |
|--------------------------------------------------------------------------|
| [Edit]   [Change state v]   [Ask the AI assistant]                       |
+--------------------------------------------------------------------------+
```

**Example images** (drawn from its wireframe, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| Recorded (Webhook delivery), U07 | desktop | ![Recorded (Webhook delivery), U07, light](../images/states/u07-administrator/s-t05-03-webhook-delivery-e-t05-03-webhook-delivery-recorded-desktop-light.png) | ![Recorded (Webhook delivery), U07, dark](../images/states/u07-administrator/s-t05-03-webhook-delivery-e-t05-03-webhook-delivery-recorded-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../images/states/s-t05-03-webhook-delivery-empty-desktop-light.png) | ![Empty, dark](../images/states/s-t05-03-webhook-delivery-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../images/states/s-t05-03-webhook-delivery-loading-desktop-light.png) | ![Loading, dark](../images/states/s-t05-03-webhook-delivery-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../images/states/s-t05-03-webhook-delivery-read-only-desktop-light.png) | ![Read-only, dark](../images/states/s-t05-03-webhook-delivery-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../images/states/s-t05-03-webhook-delivery-offline-desktop-light.png) | ![Offline, dark](../images/states/s-t05-03-webhook-delivery-offline-desktop-dark.png) |

## Fields and columns

As [E-T05-03 Webhook delivery](../data/e-t05-03-webhook-delivery.md#fields). (Proposed) A field is read-only when the
record's state is final or the role's field rules lock it; personal-data fields show only to the roles that may read
them (VR-12); secrets never show.

## Actions

| Action | Who | Result |
|---|---|---|
| Edit | the personas whose roles may change it | (Proposed) saves the fields; audited |
| Change state | the personas whose roles may change it | (Proposed) one of the Lifecycle's transitions: none: the record has one state |
| Ask the AI assistant | every persona of the page | (Proposed) an answer about this record from the data the user may see, with its sources |
| Back to the list | every persona of the page | [S-T05-L03 Webhook deliveries](00-lists/s-t05-l03-webhook-deliveries.md) |

## States

- Normal: the record with its fields, its state badge and the actions its state allows, as the wireframe shows.
- Empty: never: a record page always has its record.
- Loading: placeholders in the layout of the wireframe; actions are disabled until the record has loaded.
- Error: the error message pattern (D122); what was typed stays.
- Read-only: a record in a final state, or a role that may only read it.
- Offline: not available offline: a back-office screen on live, shared data (D38). The app shows that it is offline and
  reloads the screen when the network is back.

Shown entities (VD-15): [E-T05-03 Webhook delivery](../data/e-t05-03-webhook-delivery.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-T05-03 Webhook delivery | Recorded | Badge "Recorded"; a new record starts here; no other state; fields editable within the role | U07 | `u07-administrator/s-t05-03-webhook-delivery-e-t05-03-webhook-delivery-recorded-desktop-{light,dark}.png` |

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

- [S-T05-L03 Webhook deliveries](00-lists/s-t05-l03-webhook-deliveries.md)

## Open questions

None.

---

⬅️ [S-T05-02 Webhook subscription](s-t05-02-webhook-subscription.md) · ⬆️ [Up](README.md) ·
➡️ [S-T05-04 Idempotency key](s-t05-04-idempotency-key.md)
