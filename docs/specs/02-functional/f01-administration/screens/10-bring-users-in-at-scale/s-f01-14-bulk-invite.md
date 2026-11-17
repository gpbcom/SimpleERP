🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🛡️ [F1 Administration](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F1-10 Bring users in at scale](README.md) › 🖥️ S-F1-14 Bulk invite

# 🖥️ S-F1-14 Bulk invite

**Status:** ✅ specified

## Personas

- [U07 Administrator](../../../../01-users/personas/u07-administrator.md)
- [U11 IT provider administrator](../../../../01-users/personas/u11-provider-admin.md)
- [U23 Store manager](../../../../01-users/personas/u23-store-manager.md)

## Purpose

Paste or import a list of people, check each line and send the invitations.

## Entry points

Users › Invite in bulk; My site › Users › Invite in bulk for a site administrator.

## Wireframe

```text
+------------------------------------------------------------------+
| Invite in bulk               [Paste a list] [Import a file]      |
| 42 lines: 40 valid, 2 in error                                   |
|------------------------------------------------------------------|
| Email            Name        Role     Site        Check          |
| lea@acme.fr      Lea Roux    Seller   Lyon shop   valid          |
| hugo@acme.fr     Hugo Blanc  Seller   Nice        site not found |
| paul@acme.fr     Paul Morel  Cashier  Lyon shop   has an account |
|                       [Skip errors]  [Send 40 invitations]       |
+------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F1-10 step 2, U07 | desktop | ![FL-F1-10 step 2, U07, light](../../images/10-bring-users-in-at-scale/u07-administrator/2-bulk-invite-desktop-light.png) | ![FL-F1-10 step 2, U07, dark](../../images/10-bring-users-in-at-scale/u07-administrator/2-bulk-invite-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f01-14-bulk-invite-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f01-14-bulk-invite-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f01-14-bulk-invite-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f01-14-bulk-invite-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f01-14-bulk-invite-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f01-14-bulk-invite-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f01-14-bulk-invite-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f01-14-bulk-invite-offline-desktop-dark.png) |

## Fields and columns

| Label | Data | Editable |
|---|---|---|
| Email, name, role, site, manager, language | E-F1-15 lines | yes, per line |
| Check | E-F1-15 line status | no |

## Actions

| Action | Who | Result |
|---|---|---|
| Import a file | administrator | Columns mapped, lines checked |
| Skip errors | administrator | Lines in error set aside |
| Send | administrator | One invitation per valid line |
| Resend expired | administrator | New links for the expired lines |

## States

- Normal: the batch's lines with their check.
- Empty: no list yet: Paste a list or Import a file, with the column names expected.
- Loading: "Checking 42 lines" with a progress bar.
- Error: a file that cannot be read, with the reason (D122).
- Read-only: a sent batch: only Resend expired.
- Offline: Not available offline: an administration screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md)); the app shows that it is offline and reloads the
  screen when the network is back.

Shown entities (VD-15): [E-F1-03 User](../../data/e-f01-03-user.md),
[E-F1-15 Bulk invitation batch](../../data/e-f01-15-bulk-invitation-batch.md),
[E-F1-04 Invitation](../../data/e-f01-04-invitation.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F1-03 User | Invited | Badge "Invited"; a new record starts here; next: Active (UC-F1-03); fields editable within the role | U07 | `u07-administrator/s-f01-14-bulk-invite-e-f01-03-user-invited-desktop-{light,dark}.png` |
| E-F1-03 User | Active | Badge "Active"; next: Deactivated (UC-F1-05); fields editable within the role | U07 | `u07-administrator/s-f01-14-bulk-invite-e-f01-03-user-active-desktop-{light,dark}.png` |
| E-F1-15 Bulk invitation batch | Draft | Badge "Draft"; a new record starts here; next: Sent (UC-F1-14); fields editable within the role | U07 | `u07-administrator/s-f01-14-bulk-invite-e-f01-15-bulk-invitation-batch-draft-desktop-{light,dark}.png` |
| E-F1-15 Bulk invitation batch | Sent | Badge "Sent"; next: Done (UC-F1-14); fields editable within the role | U07 | `u07-administrator/s-f01-14-bulk-invite-e-f01-15-bulk-invitation-batch-sent-desktop-{light,dark}.png` |
| E-F1-04 Invitation | Sent | Badge "Sent"; a new record starts here; next: Accepted, Expired, Cancelled or Not delivered (UC-F1-03); fields editable within the role | U07 | `u07-administrator/s-f01-14-bulk-invite-e-f01-04-invitation-sent-desktop-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop and tablet.

## Accessibility

Every status is a word, not only a colour; tables have headers; actions are buttons with labels.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-12 File upload](../../../../04-ux/design-system/components/c-12-file-upload.md)
- [C-01 Button](../../../../04-ux/design-system/components/c-01-button.md)

## Shown in

- [FL-F1-10 Bring users in at scale](../../flows/fl-f01-10-bring-users-in-at-scale.md)

## Open questions

None.

---

⬅️ [S-F1-13 Automatic provisioning](s-f01-13-automatic-provisioning.md) · ⬆️ [Up](README.md) ·
➡️ [S-F1-15 My site's users](s-f01-15-my-sites-users.md)
