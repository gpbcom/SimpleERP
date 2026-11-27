🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🛡️ [F1 Administration](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F1-11 Team, delegation and access review](README.md) › 🖥️ S-F1-16 Delegation

# 🖥️ S-F1-16 Delegation

**Status:** ✅ specified

## Personas

- [U02 Manager](../../../../01-users/personas/u02-manager.md)
- [U13 Owner](../../../../01-users/personas/u13-owner.md)

## Purpose

Hand one's approvals to a deputy for dated period, and see the delegations in force.

## Entry points

My team › Delegation; the suggestion shown when a leave is approved.

## Wireframe

```text
+------------------------------------------------------------------+
| Delegation                                                       |
| Deputy     [ Paul Morel v ]                                      |
| From       [ 2026-12-21 ]   To [ 2027-01-04 ]                    |
| Approvals  [x] Leave [x] Purchases [x] Expenses                  |
|                                          [Cancel] [Save]         |
|------------------------------------------------------------------|
| In force: Paul Morel, all, 12-21 to 01-04, 3 approved   [End]    |
+------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F1-11 step 2, U02 | desktop | ![FL-F1-11 step 2, U02, light](../../images/11-team-delegation-and-access-review/u02-manager/2-delegation-desktop-light.png) | ![FL-F1-11 step 2, U02, dark](../../images/11-team-delegation-and-access-review/u02-manager/2-delegation-desktop-dark.png) |
| FL-F1-11 step 2, U02 | phone | ![FL-F1-11 step 2, U02, light](../../images/11-team-delegation-and-access-review/u02-manager/2-delegation-phone-light.png) | ![FL-F1-11 step 2, U02, dark](../../images/11-team-delegation-and-access-review/u02-manager/2-delegation-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f01-16-delegation-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f01-16-delegation-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f01-16-delegation-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f01-16-delegation-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f01-16-delegation-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f01-16-delegation-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f01-16-delegation-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f01-16-delegation-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Editable |
|---|---|---|
| Deputy | E-F1-13 deputy | yes |
| From, to | E-F1-13 start, end | yes |
| Approvals | E-F1-13 approvals | yes |

## Actions

| Action | Who | Result |
|---|---|---|
| Save | manager, owner | Delegation planned |
| End | manager | Requests go back to the manager at once |

## States

- Normal: the form and the delegations in force.
- Empty: no delegation: the form only.
- Loading: placeholders in the form while the team loads.
- Error: an overlap, a deputy without access (D122).
- Read-only: an ended delegation and what was approved under it.
- Offline: Not available offline ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md)); the offline banner
  shows.

Shown entities (VD-15): [E-F1-03 User](../../data/e-f01-03-user.md),
[E-F1-13 Approval delegation](../../data/e-f01-13-approval-delegation.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F1-03 User | Invited | Badge "Invited"; a new record starts here; next: Active (UC-F1-03); fields editable within the role | U02 | `u02-manager/s-f01-16-delegation-e-f01-03-user-invited-{desktop,phone}-{light,dark}.png` |
| E-F1-03 User | Active | Badge "Active"; next: Deactivated (UC-F1-05); fields editable within the role | U02 | `u02-manager/s-f01-16-delegation-e-f01-03-user-active-{desktop,phone}-{light,dark}.png` |
| E-F1-03 User | Deactivated | Badge "Deactivated"; next: Active (UC-F1-03); fields editable within the role | U02 | `u02-manager/s-f01-16-delegation-e-f01-03-user-deactivated-{desktop,phone}-{light,dark}.png` |
| E-F1-13 Approval delegation | Planned | Badge "Planned"; a new record starts here; next: Active or Cancelled (UC-F1-16); fields editable within the role | U02 | `u02-manager/s-f01-16-delegation-e-f01-13-approval-delegation-planned-{desktop,phone}-{light,dark}.png` |
| E-F1-13 Approval delegation | Active | Badge "Active"; next: Ended (UC-F1-16); fields editable within the role | U02 | `u02-manager/s-f01-16-delegation-e-f01-13-approval-delegation-active-{desktop,phone}-{light,dark}.png` |
| E-F1-13 Approval delegation | Cancelled | Badge "Cancelled"; final: read-only, no next state; the history shows how it got here | U02 | `u02-manager/s-f01-16-delegation-e-f01-13-approval-delegation-cancelled-{desktop,phone}-{light,dark}.png` |
| E-F1-13 Approval delegation | Ended | Badge "Ended"; final: read-only, no next state; the history shows how it got here | U02 | `u02-manager/s-f01-16-delegation-e-f01-13-approval-delegation-ended-{desktop,phone}-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop and phone.

## Accessibility

Every status is a word, not only a colour; tables have headers; actions are buttons with labels.

## Components

- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)
- [C-01 Button](../../../../04-ux/design-system/components/c-01-button.md)

## Shown in

- [FL-F1-11 Team, delegation and access review](../../flows/fl-f01-11-team-delegation-and-access-review.md)

## Open questions

None.

---

⬅️ [S-F1-15 My site's users](../10-bring-users-in-at-scale/s-f01-15-my-sites-users.md) · ⬆️ [Up](README.md) ·
➡️ [S-F1-17 My team](s-f01-17-my-team.md)
