🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🛡️ [F1 Administration](../../README.md) › 🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-F1-02 Manage sites](README.md) ›
🖥️ S-F1-02 Sites

# 🖥️ S-F1-02 Sites

**Status:** ✅ specified

## Personas

- [U07 Administrator](../../../../01-users/personas/u07-administrator.md): every site and action.
- [U02 Manager](../../../../01-users/personas/u02-manager.md): their own site, hours and contacts only.

## Purpose

List the company's sites and change them.

## Entry points

Administration › Sites; the site switcher's "Manage sites" link (administrator only).

## Wireframe

```text
+------------------------------------------------------------------+
| Sites                                             [+ Add a site] |
| Numbering: (o) company-wide  ( ) one series per site              |
|------------------------------------------------------------------|
| Name          Address                Stock  Manager    Status    |
| Head office * 12 rue des Lilas, Lyon  no    P. Martin  open      |
| Lyon yard     4 chemin du Port, Lyon  yes   M. Dupont  open  [..] |
| Paris agency  8 bd Voltaire, Paris    no    -          closed    |
+------------------------------------------------------------------+
[..] = Change, Make head office, Close
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F1-02 step 1, U07 | desktop | ![FL-F1-02 step 1, U07, light](../../images/02-manage-sites/u07-administrator/1-add-a-site-desktop-light.png) | ![FL-F1-02 step 1, U07, dark](../../images/02-manage-sites/u07-administrator/1-add-a-site-desktop-dark.png) |
| Error E1, U07 | desktop | ![Error E1, U07, light](../../images/02-manage-sites/u07-administrator/e1-site-still-holds-stock-desktop-light.png) | ![Error E1, U07, dark](../../images/02-manage-sites/u07-administrator/e1-site-still-holds-stock-desktop-dark.png) |
| Error E2, U07 | desktop | ![Error E2, U07, light](../../images/02-manage-sites/u07-administrator/e2-head-office-cannot-close-desktop-light.png) | ![Error E2, U07, dark](../../images/02-manage-sites/u07-administrator/e2-head-office-cannot-close-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f01-02-sites-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f01-02-sites-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f01-02-sites-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f01-02-sites-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f01-02-sites-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f01-02-sites-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f01-02-sites-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f01-02-sites-offline-desktop-dark.png) |

## Fields and columns

| Label | Data | Editable |
|---|---|---|
| Name | E-F1-02 name | administrator |
| Address | E-F1-02 address | administrator |
| Opening hours | E-F1-02 opening hours | administrator, the site's manager |
| Stock | E-F1-02 holds stock | administrator |
| Manager | E-F1-02 manager | administrator |
| Status | open or closed | through Close |
| Numbering | company setting (BR-F1-05) | administrator |

## Actions

| Action | Who | Result |
|---|---|---|
| Add a site | administrator | New site form |
| Change | administrator; manager on hours and contacts | Site form |
| Make head office | administrator | Confirmation, then dated change |
| Close | administrator | Closed, or refused with the list (BR-F1-04) |

## States

- Normal: List the company's sites and change them, as the wireframe shows.
- Empty: never (the head office always exists).
- Loading: skeleton rows in place of the list ([C-03](../../../../04-ux/design-system/components/c-03-data-table.md));
  actions are disabled until it has loaded.
- Error: closing refused, with the list of stock and staff left.
- Read-only: everything but hours and contacts for a site's manager.
- Offline: Not available offline: a back-office screen on live, shared data (D38: only today's schedule, time and
  intervention records work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-F1-02 Company site](../../data/e-f01-02-company-site.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F1-02 Company site | Open | Badge "Open"; a new record starts here; next: Closed (UC-F1-02); fields editable within the role | U02, U07 | `u02-manager/s-f01-02-sites-e-f01-02-company-site-open-{desktop,phone}-{light,dark}.png`, `u07-administrator/s-f01-02-sites-e-f01-02-company-site-open-desktop-{light,dark}.png` |
| E-F1-02 Company site | Closed | Badge "Closed"; next: Open (UC-F1-02); fields editable within the role | U02, U07 | `u02-manager/s-f01-02-sites-e-f01-02-company-site-closed-{desktop,phone}-{light,dark}.png`, `u07-administrator/s-f01-02-sites-e-f01-02-company-site-closed-desktop-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

The list becomes cards on a phone; a manager can change their site's hours from a phone.

## Accessibility

The table has column headers; actions have accessible names ("Close Lyon yard").

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)
- [C-05 Modal](../../../../04-ux/design-system/components/c-05-modal.md)

## Shown in

- [FL-F1-02 Manage sites](../../flows/fl-f01-02-manage-sites.md)

## Open questions

None.

---

⬅️ [S-F1-01 Setup wizard](../01-guided-setup/s-f01-01-setup-wizard.md) · ⬆️ [Up](README.md) ·
➡️ [S-F1-03 Users](../03-user-lifecycle/s-f01-03-users.md)
