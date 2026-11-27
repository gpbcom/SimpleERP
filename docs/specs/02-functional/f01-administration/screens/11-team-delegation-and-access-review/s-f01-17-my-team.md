🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🛡️ [F1 Administration](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F1-11 Team, delegation and access review](README.md) › 🖥️ S-F1-17 My team

# 🖥️ S-F1-17 My team

**Status:** ✅ specified

## Personas

- [U02 Manager](../../../../01-users/personas/u02-manager.md)

## Purpose

A manager's view of their team's accounts and of the requests waiting for them.

## Entry points

My team in the manager's menu; a notification of a waiting request.

## Wireframe

```text
+------------------------------------------------------------------+
| My team (6)                          [Delegation] [Ask a change] |
| Name         Roles      Site        Last sign-in   Status        |
| Lea Roux     Seller     Lyon shop   today          active        |
| Tom Petit    Seller     Lyon shop   -              invited       |
|------------------------------------------------------------------|
| Waiting for me (4)                                               |
| Leave  Lea Roux   12-23 to 12-27   2 days ago  [Approve][Refuse] |
| Expense Tom Petit 240 EUR          today       [Approve][Refuse] |
+------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F1-11 step 1, U02 | desktop | ![FL-F1-11 step 1, U02, light](../../images/11-team-delegation-and-access-review/u02-manager/1-my-team-desktop-light.png) | ![FL-F1-11 step 1, U02, dark](../../images/11-team-delegation-and-access-review/u02-manager/1-my-team-desktop-dark.png) |
| FL-F1-11 step 1, U02 | phone | ![FL-F1-11 step 1, U02, light](../../images/11-team-delegation-and-access-review/u02-manager/1-my-team-phone-light.png) | ![FL-F1-11 step 1, U02, dark](../../images/11-team-delegation-and-access-review/u02-manager/1-my-team-phone-dark.png) |
| Error E1, U02 | desktop | ![Error E1, U02, light](../../images/11-team-delegation-and-access-review/u02-manager/e1-my-team-refused-desktop-light.png) | ![Error E1, U02, dark](../../images/11-team-delegation-and-access-review/u02-manager/e1-my-team-refused-desktop-dark.png) |
| Error E1, U02 | phone | ![Error E1, U02, light](../../images/11-team-delegation-and-access-review/u02-manager/e1-my-team-refused-phone-light.png) | ![Error E1, U02, dark](../../images/11-team-delegation-and-access-review/u02-manager/e1-my-team-refused-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f01-17-my-team-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f01-17-my-team-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f01-17-my-team-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f01-17-my-team-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f01-17-my-team-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f01-17-my-team-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f01-17-my-team-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f01-17-my-team-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Editable |
|---|---|---|
| Team | E-F1-03 for the users the manager manages | no |
| Waiting for me | requests of the approval engine | approve or refuse |

## Actions

| Action | Who | Result |
|---|---|---|
| Approve, refuse | manager | As the request's own use case |
| Ask a change | manager | Task for the administrator |
| Delegation | manager | Opens S-F1-16 |

## States

- Normal: the team and what waits.
- Empty: "Nothing waits for you" when no request waits; "No team member yet" without a team.
- Loading: skeleton rows ([C-03](../../../../04-ux/design-system/components/c-03-data-table.md)).
- Error: a request withdrawn meanwhile (D122).
- Read-only: accounts are always read-only here.
- Offline: Not available offline ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md)); the offline banner
  shows.

Shown entities (VD-15): [E-F1-03 User](../../data/e-f01-03-user.md),
[E-F1-13 Approval delegation](../../data/e-f01-13-approval-delegation.md),
[E-F2-24 Approval chain](../../../f02-no-code-configuration/data/e-f02-24-approval-chain.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F1-03 User | Invited | Badge "Invited"; a new record starts here; next: Active (UC-F1-03); fields editable within the role | U02 | `u02-manager/s-f01-17-my-team-e-f01-03-user-invited-{desktop,phone}-{light,dark}.png` |
| E-F1-03 User | Active | Badge "Active"; next: Deactivated (UC-F1-05); fields editable within the role | U02 | `u02-manager/s-f01-17-my-team-e-f01-03-user-active-{desktop,phone}-{light,dark}.png` |
| E-F1-03 User | Deactivated | Badge "Deactivated"; next: Active (UC-F1-03); fields editable within the role | U02 | `u02-manager/s-f01-17-my-team-e-f01-03-user-deactivated-{desktop,phone}-{light,dark}.png` |
| E-F1-13 Approval delegation | Planned | Badge "Planned"; a new record starts here; next: Active or Cancelled (UC-F1-16); fields editable within the role | U02 | `u02-manager/s-f01-17-my-team-e-f01-13-approval-delegation-planned-{desktop,phone}-{light,dark}.png` |
| E-F1-13 Approval delegation | Active | Badge "Active"; next: Ended (UC-F1-16); fields editable within the role | U02 | `u02-manager/s-f01-17-my-team-e-f01-13-approval-delegation-active-{desktop,phone}-{light,dark}.png` |
| E-F1-13 Approval delegation | Cancelled | Badge "Cancelled"; final: read-only, no next state; the history shows how it got here | U02 | `u02-manager/s-f01-17-my-team-e-f01-13-approval-delegation-cancelled-{desktop,phone}-{light,dark}.png` |
| E-F1-13 Approval delegation | Ended | Badge "Ended"; final: read-only, no next state; the history shows how it got here | U02 | `u02-manager/s-f01-17-my-team-e-f01-13-approval-delegation-ended-{desktop,phone}-{light,dark}.png` |
| E-F2-24 Approval chain | Draft | Badge "Draft"; a new record starts here; next: Published (UC-F2-29); fields editable within the role | U02 | `u02-manager/s-f01-17-my-team-e-f02-24-approval-chain-draft-{desktop,phone}-{light,dark}.png` |
| E-F2-24 Approval chain | Published | Badge "Published"; final: read-only, no next state; the history shows how it got here | U02 | `u02-manager/s-f01-17-my-team-e-f02-24-approval-chain-published-{desktop,phone}-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop and phone: cards on a phone.

## Accessibility

Every status is a word, not only a colour; tables have headers; actions are buttons with labels.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-10 Empty state](../../../../04-ux/design-system/components/c-10-empty-state.md)
- [C-01 Button](../../../../04-ux/design-system/components/c-01-button.md)

## Shown in

- [FL-F1-11 Team, delegation and access review](../../flows/fl-f01-11-team-delegation-and-access-review.md)
- [FL-F2-11 Rights, translations and approvals](../../../f02-no-code-configuration/flows/fl-f02-11-rights-translations-and-approvals.md)

## Open questions

None.

---

⬅️ [S-F1-16 Delegation](s-f01-16-delegation.md) · ⬆️ [Up](README.md) ·
➡️ [S-F1-18 Access reviews](s-f01-18-access-reviews.md)
