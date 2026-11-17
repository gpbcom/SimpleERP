🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🛡️ [F1 Administration](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F1-11 Team, delegation and access review](README.md) › 🖥️ S-F1-18 Access reviews

# 🖥️ S-F1-18 Access reviews

**Status:** ✅ specified

## Personas

- [U07 Administrator](../../../../01-users/personas/u07-administrator.md)
- [U02 Manager](../../../../01-users/personas/u02-manager.md)
- [U13 Owner](../../../../01-users/personas/u13-owner.md)

## Purpose

Launch and close access review campaigns, and review a team's rights.

## Entry points

Administration › Access reviews; the manager's notification.

## Wireframe

```text
+------------------------------------------------------------------+
| Access review Q4 2026        deadline 2026-12-15     72 % done   |
|------------------------------------------------------------------|
| User       Right               Last used    Decision             |
| Lea Roux   Seller (role)       today        [Certify] [Remove]   |
| Lea Roux   Accounting (role)   120 days     unused  [Remove]     |
| Tom Petit  Outside tool CRM    never        [Certify] [Remove]   |
|                                       [Confirm my decisions]     |
+------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F1-11 step 3, U07 | desktop | ![FL-F1-11 step 3, U07, light](../../images/11-team-delegation-and-access-review/u07-administrator/3-access-reviews-desktop-light.png) | ![FL-F1-11 step 3, U07, dark](../../images/11-team-delegation-and-access-review/u07-administrator/3-access-reviews-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f01-18-access-reviews-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f01-18-access-reviews-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f01-18-access-reviews-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f01-18-access-reviews-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f01-18-access-reviews-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f01-18-access-reviews-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f01-18-access-reviews-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f01-18-access-reviews-offline-desktop-dark.png) |

## Fields and columns

| Label | Data | Editable |
|---|---|---|
| Lines | E-F1-16 lines | decision and comment |
| Progress | computed | no |

## Actions

| Action | Who | Result |
|---|---|---|
| Launch, close | administrator | Campaign opened or closed with its report |
| Certify, remove | manager | Decision on the line |
| Export the report | administrator, owner | PDF or CSV |

## States

- Normal: the lines to review and the progress.
- Empty: no campaign yet: Launch a campaign.
- Loading: skeleton rows ([C-03](../../../../04-ux/design-system/components/c-03-data-table.md)).
- Error: removing the last administrator's rights (D122).
- Read-only: a closed campaign and its report.
- Offline: Not available offline: an administration screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md)); the app shows that it is offline and reloads the
  screen when the network is back.

Shown entities (VD-15): [E-F1-03 User](../../data/e-f01-03-user.md),
[E-F1-16 Access review campaign](../../data/e-f01-16-access-review-campaign.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F1-03 User | Invited | Badge "Invited"; a new record starts here; next: Active (UC-F1-03); fields editable within the role | U02, U07 | `u02-manager/s-f01-18-access-reviews-e-f01-03-user-invited-{desktop,phone}-{light,dark}.png`, `u07-administrator/s-f01-18-access-reviews-e-f01-03-user-invited-desktop-{light,dark}.png` |
| E-F1-03 User | Active | Badge "Active"; next: Deactivated (UC-F1-05); fields editable within the role | U02, U07 | `u02-manager/s-f01-18-access-reviews-e-f01-03-user-active-{desktop,phone}-{light,dark}.png`, `u07-administrator/s-f01-18-access-reviews-e-f01-03-user-active-desktop-{light,dark}.png` |
| E-F1-03 User | Deactivated | Badge "Deactivated"; next: Active (UC-F1-03); fields editable within the role | U02, U07 | `u02-manager/s-f01-18-access-reviews-e-f01-03-user-deactivated-{desktop,phone}-{light,dark}.png`, `u07-administrator/s-f01-18-access-reviews-e-f01-03-user-deactivated-desktop-{light,dark}.png` |
| E-F1-16 Access review campaign | Open | Badge "Open"; a new record starts here; next: Closed (UC-F1-18); fields editable within the role | U02, U07 | `u02-manager/s-f01-18-access-reviews-e-f01-16-access-review-campaign-open-{desktop,phone}-{light,dark}.png`, `u07-administrator/s-f01-18-access-reviews-e-f01-16-access-review-campaign-open-desktop-{light,dark}.png` |
| E-F1-16 Access review campaign | Closed | Badge "Closed"; final: read-only, no next state; the history shows how it got here | U02, U07 | `u02-manager/s-f01-18-access-reviews-e-f01-16-access-review-campaign-closed-{desktop,phone}-{light,dark}.png`, `u07-administrator/s-f01-18-access-reviews-e-f01-16-access-review-campaign-closed-desktop-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop and tablet; managers can review on a phone.

## Accessibility

Every status is a word, not only a colour; tables have headers; actions are buttons with labels.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-01 Button](../../../../04-ux/design-system/components/c-01-button.md)

## Shown in

- [FL-F1-11 Team, delegation and access review](../../flows/fl-f01-11-team-delegation-and-access-review.md)

## Open questions

None.

---

⬅️ [S-F1-17 My team](s-f01-17-my-team.md) · ⬆️ [Up](README.md) ·
➡️ [S-F1-19 Portal accounts](../12-portal-accounts-and-integrations/s-f01-19-portal-accounts.md)
