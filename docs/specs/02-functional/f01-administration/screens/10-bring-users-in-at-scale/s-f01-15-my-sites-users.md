🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🛡️ [F1 Administration](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F1-10 Bring users in at scale](README.md) › 🖥️ S-F1-15 My site's users

# 🖥️ S-F1-15 My site's users

**Status:** ✅ specified

## Personas

- [U23 Store manager](../../../../01-users/personas/u23-store-manager.md)
- [U02 Manager](../../../../01-users/personas/u02-manager.md)

## Purpose

The users of the sites a manager administers: invite, change within the allowed roles, deactivate.

## Entry points

My site › Users.

## Wireframe

```text
+------------------------------------------------------------------+
| My site: Lyon shop › Users                   [+ Invite] [Bulk]   |
|------------------------------------------------------------------|
| Name         Role      Last sign-in   Status                     |
| Lea Roux     Seller    today 08:10    active                     |
| Hugo Blanc   Seller    2026-11-09     active   last day 11-30    |
| -            Cashier   -              invited  expires in 20 h   |
| Roles you may give: Seller, Cashier                              |
+------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F1-10 step 3, U23 | desktop | ![FL-F1-10 step 3, U23, light](../../images/10-bring-users-in-at-scale/u23-store-manager/3-my-sites-users-desktop-light.png) | ![FL-F1-10 step 3, U23, dark](../../images/10-bring-users-in-at-scale/u23-store-manager/3-my-sites-users-desktop-dark.png) |
| FL-F1-10 step 3, U23 | phone | ![FL-F1-10 step 3, U23, light](../../images/10-bring-users-in-at-scale/u23-store-manager/3-my-sites-users-phone-light.png) | ![FL-F1-10 step 3, U23, dark](../../images/10-bring-users-in-at-scale/u23-store-manager/3-my-sites-users-phone-dark.png) |
| FL-F1-10 step 3, U23 | tablet | ![FL-F1-10 step 3, U23, light](../../images/10-bring-users-in-at-scale/u23-store-manager/3-my-sites-users-tablet-light.png) | ![FL-F1-10 step 3, U23, dark](../../images/10-bring-users-in-at-scale/u23-store-manager/3-my-sites-users-tablet-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f01-15-my-sites-users-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f01-15-my-sites-users-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f01-15-my-sites-users-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f01-15-my-sites-users-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f01-15-my-sites-users-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f01-15-my-sites-users-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f01-15-my-sites-users-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f01-15-my-sites-users-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Editable |
|---|---|---|
| Name, role, status | E-F1-03 | role within the allowed list |
| Last day | E-F1-03 last day | yes |

## Actions

| Action | Who | Result |
|---|---|---|
| Invite | site administrator | Invitation with the site preset |
| Change role | site administrator | Within the allowed roles |
| Deactivate | site administrator | Hand-over to a colleague of the site |

## States

- Normal: the site's users only.
- Empty: only the manager: "Invite your first colleague".
- Loading: skeleton rows ([C-03](../../../../04-ux/design-system/components/c-03-data-table.md)).
- Error: a role outside the list, the site's only manager (D122).
- Read-only: users who also work at another site: changed by the administrator only.
- Offline: Not available offline ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md)): on the phone, the
  offline banner replaces the actions until the network is back.

Shown entities (VD-15): [E-F1-03 User](../../data/e-f01-03-user.md),
[E-F1-02 Company site](../../data/e-f01-02-company-site.md), [E-F1-06 Role](../../data/e-f01-06-role.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F1-03 User | Invited | Badge "Invited"; a new record starts here; next: Active (UC-F1-03); fields editable within the role | U23 | `u23-store-manager/s-f01-15-my-sites-users-e-f01-03-user-invited-{desktop,phone,tablet}-{light,dark}.png` |
| E-F1-03 User | Active | Badge "Active"; next: Deactivated (UC-F1-05); fields editable within the role | U23 | `u23-store-manager/s-f01-15-my-sites-users-e-f01-03-user-active-{desktop,phone,tablet}-{light,dark}.png` |
| E-F1-03 User | Deactivated | Badge "Deactivated"; next: Active (UC-F1-03); fields editable within the role | U23 | `u23-store-manager/s-f01-15-my-sites-users-e-f01-03-user-deactivated-{desktop,phone,tablet}-{light,dark}.png` |
| E-F1-02 Company site | Open | Badge "Open"; a new record starts here; next: Closed (UC-F1-02); fields editable within the role | U23 | `u23-store-manager/s-f01-15-my-sites-users-e-f01-02-company-site-open-{desktop,phone,tablet}-{light,dark}.png` |
| E-F1-02 Company site | Closed | Badge "Closed"; next: Open (UC-F1-02); fields editable within the role | U23 | `u23-store-manager/s-f01-15-my-sites-users-e-f01-02-company-site-closed-{desktop,phone,tablet}-{light,dark}.png` |
| E-F1-06 Role | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U23 | `u23-store-manager/s-f01-15-my-sites-users-e-f01-06-role-active-{desktop,phone,tablet}-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop, tablet and phone: on a phone the list becomes cards.

## Accessibility

Every status is a word, not only a colour; tables have headers; actions are buttons with labels.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-01 Button](../../../../04-ux/design-system/components/c-01-button.md)
- [C-05 Modal](../../../../04-ux/design-system/components/c-05-modal.md)

## Shown in

- [FL-F1-10 Bring users in at scale](../../flows/fl-f01-10-bring-users-in-at-scale.md)

## Open questions

None.

---

⬅️ [S-F1-14 Bulk invite](s-f01-14-bulk-invite.md) · ⬆️ [Up](README.md) ·
➡️ [S-F1-16 Delegation](../11-team-delegation-and-access-review/s-f01-16-delegation.md)
