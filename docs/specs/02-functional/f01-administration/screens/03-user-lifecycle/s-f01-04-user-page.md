🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🛡️ [F1 Administration](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F1-03 User lifecycle](README.md) › 🖥️ S-F1-04 User page

# 🖥️ S-F1-04 User page

**Status:** ✅ specified

## Personas

- [U07 Administrator](../../../../01-users/personas/u07-administrator.md)

## Purpose

See and change one user: roles, site, manager, language, HR link, status, dated changes.

## Entry points

Users list (S-F1-03) › a user; a user's name anywhere, for the administrator.

## Wireframe

```text
+------------------------------------------------------------------+
| < Users   Marie Dupont   marie@acme.fr          active          |
|------------------------------------------------------------------|
| Roles      [Sales x] [Manager x] [+]                             |
| Site       [ Lyon yard v ]     Manager [ P. Martin v ]           |
| Language   [ Français v ]      HR record [ Marie Dupont (F9) ]   |
| Applies    (o) at once   ( ) from [ 01/12/2026 ]                 |
|                                                [Save changes]    |
|------------------------------------------------------------------|
| Planned changes                                                  |
|  1 Dec 2026: site -> Paris agency                    [Cancel]    |
|------------------------------------------------------------------|
| [Reset two-factor]                 [Deactivate and hand over...] |
+------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F1-03 step 4, U07 | desktop | ![FL-F1-03 step 4, U07, light](../../images/03-user-lifecycle/u07-administrator/4-change-role-or-site-desktop-light.png) | ![FL-F1-03 step 4, U07, dark](../../images/03-user-lifecycle/u07-administrator/4-change-role-or-site-desktop-dark.png) |
| Error E3, U07 | desktop | ![Error E3, U07, light](../../images/03-user-lifecycle/u07-administrator/e3-last-administrator-desktop-light.png) | ![Error E3, U07, dark](../../images/03-user-lifecycle/u07-administrator/e3-last-administrator-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f01-04-user-page-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f01-04-user-page-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f01-04-user-page-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f01-04-user-page-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f01-04-user-page-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f01-04-user-page-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f01-04-user-page-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f01-04-user-page-offline-desktop-dark.png) |

## Fields and columns

As [E-F1-03 User](../../data/e-f01-03-user.md#fields), plus "Applies" (at once or a date).

## Actions

| Action | Who | Result |
|---|---|---|
| Save changes | administrator | At once or dated (UC-F1-04) |
| Cancel a planned change | administrator | Removed before its date |
| Reset two-factor | administrator | The user sets it again at next sign-in |
| Deactivate and hand over | administrator | UC-F1-05 |

## States

- Normal: See and change one user: roles, site, manager, language, HR link, status, dated changes, as the wireframe
  shows.
- Empty: never: a user page always has its user.
- Loading: placeholders in the layout of the wireframe; actions are disabled until the record has loaded.
- Error: last administrator, manager is the user (UC-F1-04 error flows).
- Read-only: a deactivated user, except "Reactivate".
- Offline: Not available offline: a back-office screen on live, shared data (D38: only today's schedule, time and
  intervention records work offline). The app shows that it is offline and reloads the screen when the network is back.
- Planned changes: shown until their date.

Shown entities (VD-15): [E-F1-03 User](../../data/e-f01-03-user.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F1-03 User | Active | Badge "Active"; next: Deactivated (UC-F1-05); fields editable within the role | U07 | `u07-administrator/s-f01-04-user-page-e-f01-03-user-active-desktop-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop and tablet.

## Accessibility

Role chips are buttons with names ("Remove Manager role"); the date field has its format as text.

## Components

- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)
- [C-05 Modal](../../../../04-ux/design-system/components/c-05-modal.md)

## Shown in

- [FL-F1-03 User lifecycle](../../flows/fl-f01-03-user-lifecycle.md)

## Open questions

None.

---

⬅️ [S-F1-03 Users](s-f01-03-users.md) · ⬆️ [Up](README.md) · ➡️ [S-F1-05 Offboarding](s-f01-05-offboarding.md)
