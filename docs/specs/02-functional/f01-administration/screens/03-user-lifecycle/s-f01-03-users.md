🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🛡️ [F1 Administration](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F1-03 User lifecycle](README.md) › 🖥️ S-F1-03 Users

# 🖥️ S-F1-03 Users

**Status:** ✅ specified

## Personas

- [U07 Administrator](../../../../01-users/personas/u07-administrator.md)

## Purpose

List the company's users and invitations, invite, and open a user.

## Entry points

Administration › Users.

## Wireframe

```text
+------------------------------------------------------------------+
| Users                                   [search...]  [+ Invite]  |
| Filter: [All v] [Site v] [Role v]                                |
|------------------------------------------------------------------|
| Name          Email            Roles         Site       Status    |
| Marie Dupont  marie@acme.fr    Sales         Lyon yard  active    |
| -             paul@acme.fr     Employee      Head office invited  |
|                                        expires in 31 h [Resend]  |
| Luc Bernard   luc@acme.fr      Accounting    Head office deact.   |
+------------------------------------------------------------------+

Invite (panel)
  Email      [ paul@acme.fr          ]
  Roles      [Employee x] [+]
  Site       [ Head office v ]   Manager [ P. Martin v ]
  Language   [ Français v ]
  HR record  [ Paul Morel (F9) v ]
                                 [Cancel] [Send invitation]
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F1-03 step 1, U07 | desktop | ![FL-F1-03 step 1, U07, light](../../images/03-user-lifecycle/u07-administrator/1-invite-desktop-light.png) | ![FL-F1-03 step 1, U07, dark](../../images/03-user-lifecycle/u07-administrator/1-invite-desktop-dark.png) |
| Error E1, U07 | desktop | ![Error E1, U07, light](../../images/03-user-lifecycle/u07-administrator/e1-email-has-an-account-desktop-light.png) | ![Error E1, U07, dark](../../images/03-user-lifecycle/u07-administrator/e1-email-has-an-account-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f01-03-users-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f01-03-users-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f01-03-users-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f01-03-users-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f01-03-users-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f01-03-users-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f01-03-users-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f01-03-users-offline-desktop-dark.png) |

## Fields and columns

| Label | Data | Editable |
|---|---|---|
| Name | E-F1-03 name | no (from the user or the HR record) |
| Email | E-F1-03 email | at invitation |
| Roles | E-F1-03 roles | administrator |
| Site, manager | E-F1-03 site, manager | administrator |
| Language | E-F1-03 language | administrator, the user |
| Status | invited, active, deactivated | through actions |

## Actions

| Action | Who | Result |
|---|---|---|
| Invite | administrator | Invitation panel, then email (UC-F1-03) |
| Resend | administrator | New 48-hour link; the old one is cancelled |
| Open a user | administrator | User page (UC-F1-04, UC-F1-05) |

## States

- Normal: List the company's users and invitations, invite, and open a user, as the wireframe shows.
- Empty: only the first administrator.
- Loading: skeleton rows in place of the list ([C-03](../../../../04-ux/design-system/components/c-03-data-table.md));
  actions are disabled until it has loaded.
- Error: an email that already has an account (the existing user is shown).
- Read-only: none for the administrator.
- Offline: Not available offline: a back-office screen on live, shared data (D38: only today's schedule, time and
  intervention records work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-F1-03 User](../../data/e-f01-03-user.md),
[E-F1-04 Invitation](../../data/e-f01-04-invitation.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F1-03 User | Invited | Badge "Invited"; a new record starts here; next: Active (UC-F1-03); fields editable within the role | U01, U07 | `u01-employee/s-f01-03-users-e-f01-03-user-invited-{desktop,phone}-{light,dark}.png`, `u07-administrator/s-f01-03-users-e-f01-03-user-invited-desktop-{light,dark}.png` |
| E-F1-03 User | Active | Badge "Active"; next: Deactivated (UC-F1-05); fields editable within the role | U01, U07 | `u01-employee/s-f01-03-users-e-f01-03-user-active-{desktop,phone}-{light,dark}.png`, `u07-administrator/s-f01-03-users-e-f01-03-user-active-desktop-{light,dark}.png` |
| E-F1-03 User | Deactivated | Badge "Deactivated"; next: Active (UC-F1-03); fields editable within the role | U07 | `u07-administrator/s-f01-03-users-e-f01-03-user-deactivated-desktop-{light,dark}.png` |
| E-F1-04 Invitation | Sent | Badge "Sent"; a new record starts here; next: Accepted, Expired, Cancelled or Not delivered (UC-F1-03); fields editable within the role | U01, U07 | `u01-employee/s-f01-03-users-e-f01-04-invitation-sent-{desktop,phone}-{light,dark}.png`, `u07-administrator/s-f01-03-users-e-f01-04-invitation-sent-desktop-{light,dark}.png` |
| E-F1-04 Invitation | Accepted | Badge "Accepted"; final: read-only, no next state; the history shows how it got here | U01, U07 | `u01-employee/s-f01-03-users-e-f01-04-invitation-accepted-{desktop,phone}-{light,dark}.png`, `u07-administrator/s-f01-03-users-e-f01-04-invitation-accepted-desktop-{light,dark}.png` |
| E-F1-04 Invitation | Expired | Badge "Expired"; final: read-only, no next state; the history shows how it got here | U01, U07 | `u01-employee/s-f01-03-users-e-f01-04-invitation-expired-{desktop,phone}-{light,dark}.png`, `u07-administrator/s-f01-03-users-e-f01-04-invitation-expired-desktop-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop and tablet; on a phone, the list is readable and resending works.

## Accessibility

The status is a word, not only a colour; the remaining time is text.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)

## Shown in

- [FL-F1-03 User lifecycle](../../flows/fl-f01-03-user-lifecycle.md)

## Open questions

None.

---

⬅️ [S-F1-02 Sites](../02-manage-sites/s-f01-02-sites.md) · ⬆️ [Up](README.md) ·
➡️ [S-F1-04 User page](s-f01-04-user-page.md)
