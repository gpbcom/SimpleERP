🏠 [Specs](../../../README.md) › ⚙️ [Technical capabilities](../../README.md) ›
🌐 [T10 Translations and notifications](../README.md) › 🖥️ [Screens](README.md) › 🖥️ S-T10-02 Notification

# 🖥️ S-T10-02 Notification

**Status:** 🔄 (Proposed) drawn in step 36j from its entity and list page; waits for the owner

## Personas

- [U07 Administrator](../../../01-users/personas/u07-administrator.md)

(Proposed) Each persona sees the fields and the actions its roles allow, as on
[S-T10-L02 Notifications](00-lists/s-t10-l02-notifications.md): the record rules and field rules of T2.

## Purpose

(Proposed) See one [E-T10-02 Notification](../data/e-t10-02-notification.md) and act on it: its fields, its state and
the changes its state allows. It is the page the rows of [S-T10-L02 Notifications](00-lists/s-t10-l02-notifications.md)
open (VR-13).

## Entry points

- [S-T10-L02 Notifications](00-lists/s-t10-l02-notifications.md) › a row's Open ›.
- (Proposed) A link to the record wherever another page names it, and global search.
- The flows of Shown in.

## Wireframe

```text
+--------------------------------------------------------------------------+
| < Notifications   U-9                                           [Active] |
|--------------------------------------------------------------------------|
| user, event, channels, U-9, quote approved, chat, 10:03                  |
|--------------------------------------------------------------------------|
| History: every change, by whom and when                                  |
|--------------------------------------------------------------------------|
| [Edit]   [Change state v]   [Ask the AI assistant]                       |
+--------------------------------------------------------------------------+
```

**Example images** (drawn from its wireframe, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| Active (Notification), U07 | desktop | ![Active (Notification), U07, light](../images/states/u07-administrator/s-t10-02-notification-e-t10-02-notification-active-desktop-light.png) | ![Active (Notification), U07, dark](../images/states/u07-administrator/s-t10-02-notification-e-t10-02-notification-active-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../images/states/s-t10-02-notification-empty-desktop-light.png) | ![Empty, dark](../images/states/s-t10-02-notification-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../images/states/s-t10-02-notification-loading-desktop-light.png) | ![Loading, dark](../images/states/s-t10-02-notification-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../images/states/s-t10-02-notification-read-only-desktop-light.png) | ![Read-only, dark](../images/states/s-t10-02-notification-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../images/states/s-t10-02-notification-offline-desktop-light.png) | ![Offline, dark](../images/states/s-t10-02-notification-offline-desktop-dark.png) |

## Fields and columns

As [E-T10-02 Notification](../data/e-t10-02-notification.md#fields). (Proposed) A field is read-only when the record's
state is final or the role's field rules lock it; personal-data fields show only to the roles that may read them
(VR-12); secrets never show.

## Actions

| Action | Who | Result |
|---|---|---|
| Edit | the personas whose roles may change it | (Proposed) saves the fields; audited |
| Change state | the personas whose roles may change it | (Proposed) one of the Lifecycle's transitions: none: the record has one state |
| Ask the AI assistant | every persona of the page | (Proposed) an answer about this record from the data the user may see, with its sources |
| Back to the list | every persona of the page | [S-T10-L02 Notifications](00-lists/s-t10-l02-notifications.md) |

## States

- Normal: the record with its fields, its state badge and the actions its state allows, as the wireframe shows.
- Empty: never: a record page always has its record.
- Loading: placeholders in the layout of the wireframe; actions are disabled until the record has loaded.
- Error: the error message pattern (D122); what was typed stays.
- Read-only: a record in a final state, or a role that may only read it.
- Offline: not available offline: a back-office screen on live, shared data (D38). The app shows that it is offline and
  reloads the screen when the network is back.

Shown entities (VD-15): [E-T10-02 Notification](../data/e-t10-02-notification.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-T10-02 Notification | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U07 | `u07-administrator/s-t10-02-notification-e-t10-02-notification-active-desktop-{light,dark}.png` |

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

- [S-T10-L02 Notifications](00-lists/s-t10-l02-notifications.md)
- [FL-F1-11 Team, delegation and access review](../../../02-functional/f01-administration/flows/fl-f01-11-team-delegation-and-access-review.md)
- [FL-F3-09 Assistant on a phone](../../../02-functional/f03-assistant/flows/fl-f03-09-assistant-on-a-phone.md)
- [FL-F4-03 Review a meeting](../../../02-functional/f04-meetings/flows/fl-f04-03-review-a-meeting.md)
- [FL-F4-12 Rooms and client video](../../../02-functional/f04-meetings/flows/fl-f04-12-rooms-and-client-video.md)
- [FL-F9-04 Grow](../../../02-functional/f09-hr-and-projects/flows/fl-f09-04-grow.md)
- [FL-F9-05 Workplace services](../../../02-functional/f09-hr-and-projects/flows/fl-f09-05-workplace-services.md)
- [FL-F11-02 Shop and check out](../../../02-functional/f11-online-shop/flows/fl-f11-02-shop-and-check-out.md)
- [FL-F20-03 Incidents](../../../02-functional/f20-hosted-support-assistant/flows/fl-f20-03-incidents.md)
- [FL-SC11-04 Deadlines and filings](../../../08-sectors/sc11-professional-firms/flows/fl-sc11-04-deadlines-and-filings.md)

## Open questions

None.

---

⬅️ [S-T10-01 Translation string](s-t10-01-translation-string.md) · ⬆️ [Up](README.md) ·
➡️ [S-T10-03 User preferences](s-t10-03-user-preferences.md)
