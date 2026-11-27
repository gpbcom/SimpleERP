🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🛡️ [F1 Administration](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F1-03 User lifecycle](README.md) › 🖥️ S-F1-05 Offboarding

# 🖥️ S-F1-05 Offboarding

**Status:** ✅ specified

## Personas

- [U07 Administrator](../../../../01-users/personas/u07-administrator.md)

## Purpose

Hand a leaver's open items over and deactivate them.

## Entry points

User page (S-F1-04) › Deactivate and hand over.

## Wireframe

```text
+------------------------------------------------------------------+
| Deactivate Luc Bernard                                       [x] |
|------------------------------------------------------------------|
| Open items to hand over                                          |
|   12 customers, 4 open quotes, 2 pending approvals, 3 tasks      |
| Hand over to   [ Marie Dupont v ]   (suggested by the assistant) |
| Deactivate     (o) at once  ( ) at the end of [ 30/11/2026 ]     |
|                                                                  |
| Luc keeps read-only access to his payslips and HR papers.        |
|                              [Cancel]  [Hand over and deactivate]|
+------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F1-03 step 5, U07 | desktop | ![FL-F1-03 step 5, U07, light](../../images/03-user-lifecycle/u07-administrator/5-offboard-desktop-light.png) | ![FL-F1-03 step 5, U07, dark](../../images/03-user-lifecycle/u07-administrator/5-offboard-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f01-05-offboarding-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f01-05-offboarding-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f01-05-offboarding-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f01-05-offboarding-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f01-05-offboarding-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f01-05-offboarding-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f01-05-offboarding-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f01-05-offboarding-offline-desktop-dark.png) |

## Fields and columns

| Label | Data | Editable |
|---|---|---|
| Open items | counts by kind | no |
| Hand over to | an active user | yes |
| Deactivate | at once or a date | yes |

## Actions

| Action | Who | Result |
|---|---|---|
| Hand over and deactivate | administrator | UC-F1-05 main flow |
| Cancel | administrator | Nothing changes |

## States

- Normal: Hand a leaver's open items over and deactivate them, as the wireframe shows.
- Empty: No open item: the hand-over field is hidden and only the date and Deactivate remain.
- Loading: placeholders in the layout of the wireframe; actions are disabled until the record has loaded.
- Error: the colleague is the leaver or deactivated; the leaver is the only administrator.
- Read-only: a deactivated user's hand-over, shown as it was done.
- Offline: Not available offline: a back-office screen on live, shared data (D38: only today's schedule, time and
  intervention records work offline). The app shows that it is offline and reloads the screen when the network is back.
- No open item: the hand-over field is hidden.

Shown entities (VD-15): [E-F1-06 Role](../../data/e-f01-06-role.md),
[E-F1-02 Company site](../../data/e-f01-02-company-site.md), [E-F1-03 User](../../data/e-f01-03-user.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F1-06 Role | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U07 | `u07-administrator/s-f01-05-offboarding-e-f01-06-role-active-desktop-{light,dark}.png` |
| E-F1-02 Company site | Open | Badge "Open"; a new record starts here; next: Closed (UC-F1-02); fields editable within the role | U07 | `u07-administrator/s-f01-05-offboarding-e-f01-02-company-site-open-desktop-{light,dark}.png` |
| E-F1-02 Company site | Closed | Badge "Closed"; next: Open (UC-F1-02); fields editable within the role | U07 | `u07-administrator/s-f01-05-offboarding-e-f01-02-company-site-closed-desktop-{light,dark}.png` |
| E-F1-03 User | Active | Badge "Active"; next: Deactivated (UC-F1-05); fields editable within the role | U07 | `u07-administrator/s-f01-05-offboarding-e-f01-03-user-active-desktop-{light,dark}.png` |
| E-F1-03 User | Deactivated | Badge "Deactivated"; next: Active (UC-F1-03); fields editable within the role | U07 | `u07-administrator/s-f01-05-offboarding-e-f01-03-user-deactivated-desktop-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop and tablet.

## Accessibility

A modal dialog with a title and focus on its first field; Escape cancels.

## Components

- [C-05 Modal](../../../../04-ux/design-system/components/c-05-modal.md)
- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)

## Shown in

- [FL-F1-03 User lifecycle](../../flows/fl-f01-03-user-lifecycle.md)

## Open questions

None.

---

⬅️ [S-F1-04 User page](s-f01-04-user-page.md) · ⬆️ [Up](README.md) ·
➡️ [S-F1-06 Role editor](../04-edit-a-role/s-f01-06-role-editor.md)
