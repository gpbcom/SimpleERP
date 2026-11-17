🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🌐 [F18 Hosted websites and domains (hosted edition)](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F18-03 Domain and DNS](README.md) › 🖥️ S-F18-23 Mailboxes

# 🖥️ S-F18-23 Mailboxes

**Status:** ✅ specified

## Personas

- [U07 Administrator](../../../../01-users/personas/u07-administrator.md)
- [U01 Employee](../../../../01-users/personas/u01-employee.md)

## Purpose

Create and close mailboxes and shared addresses on the domain.

## Entry points

Domain, Mailboxes; a user invited in F1.

## Wireframe

```text
Mailboxes on restaurant.example                       [New mailbox]
-------------------------------------------------------------------------------
Address                 Owner         Kind       Used     State
marie@                  Marie         personal   2.1 GB   active
contact@                3 members     shared     0.4 GB   active
paul@                   Paul (left)   forward    -        until 2027-01-31
-------------------------------------------------------------------------------
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F18-03 step 6, U07 | desktop | ![FL-F18-03 step 6, U07, light](../../images/03-domain-and-dns/u07-administrator/6-mailboxes-desktop-light.png) | ![FL-F18-03 step 6, U07, dark](../../images/03-domain-and-dns/u07-administrator/6-mailboxes-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f18-23-mailboxes-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f18-23-mailboxes-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f18-23-mailboxes-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f18-23-mailboxes-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f18-23-mailboxes-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f18-23-mailboxes-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f18-23-mailboxes-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f18-23-mailboxes-offline-desktop-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Address | E-F18-15 address | email | yes at creation | yes |
| Owner | E-F18-15 owner | user or members | yes | yes |
| Kind | E-F18-15 kind | personal, shared, forward | yes | yes |
| Used | E-F18-15 size | GB | no | no |
| State | E-F18-15 status | active, forwarding, closed | no | yes |

## Actions

| Action | Where | Who | Result |
|---|---|---|---|
| New mailbox | header | administrator | mailbox created |
| Close | row | administrator | closed, mail exported |

## States

- Normal: mailboxes with owners, use and state.
- Empty: "No mailbox": a link to set the mail records first.
- Loading: the frame and titles show at once with placeholder rows for the mailboxes; within 1 second (D408) the data
  replaces them, and a longer load shows a progress line saying what loads.
- Error: an address already taken, or broken mail records.
- Read-only: users see only their own mailbox's details.
- Offline: not available offline: mailboxes are managed on the server. D38 keeps only today's schedule, time and
  intervention records offline. A banner says the connection is lost; what is on screen stays visible, every action is
  disabled and nothing is queued until the connection is back.

Shown entities (VD-15): [E-F18-15 Mailbox](../../data/e-f18-15-mailbox.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F18-15 Mailbox | Active | Badge "Active"; a new record starts here; next: Forwarding or Closed (UC-F18-23); fields editable within the role | U01, U07 | `u01-employee/s-f18-23-mailboxes-e-f18-15-mailbox-active-{desktop,phone}-{light,dark}.png`, `u07-administrator/s-f18-23-mailboxes-e-f18-15-mailbox-active-desktop-{light,dark}.png` |
| E-F18-15 Mailbox | Forwarding | Badge "Forwarding"; next: Closed (UC-F18-23); fields editable within the role | U01, U07 | `u01-employee/s-f18-23-mailboxes-e-f18-15-mailbox-forwarding-{desktop,phone}-{light,dark}.png`, `u07-administrator/s-f18-23-mailboxes-e-f18-15-mailbox-forwarding-desktop-{light,dark}.png` |
| E-F18-15 Mailbox | Closed | Badge "Closed"; final: read-only, no next state; the history shows how it got here | U01, U07 | `u01-employee/s-f18-23-mailboxes-e-f18-15-mailbox-closed-{desktop,phone}-{light,dark}.png`, `u07-administrator/s-f18-23-mailboxes-e-f18-15-mailbox-closed-desktop-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop.

## Accessibility

Keyboard order follows the reading order; every control has a visible label; amounts, states and icons are also given as
text; status changes are announced to screen readers.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)
- [C-10 Empty state](../../../../04-ux/design-system/components/c-10-empty-state.md)

## Shown in

- [FL-F18-03 Domain and DNS](../../flows/fl-f18-03-domain-and-dns.md)

## Open questions

None.

---

⬅️ [S-F18-22 Redirects](s-f18-22-redirects.md) · ⬆️ [Up](README.md) ·
➡️ [S-F18-24 Form protection](../01-build-the-site/s-f18-24-form-protection.md)
