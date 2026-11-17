🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🛡️ [F1 Administration](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F1-08 The provider and its client companies](README.md) › 🖥️ S-F1-10 Client companies

# 🖥️ S-F1-10 Client companies

**Status:** ✅ specified

## Personas

- [U11 IT provider administrator](../../../../01-users/personas/u11-provider-admin.md)

## Purpose

The provider's list of client companies and templates: create, enter, watch.

## Entry points

The provider platform's home.

## Wireframe

```text
+------------------------------------------------------------------+
| Client companies               [search...]   [+ New from template]|
|------------------------------------------------------------------|
| Company        Template       Users  Version  Health   Actions    |
| Acme Bâtiment  Construction    24    1.3.0    ok      [Enter]    |
| Café Lumière   Hospitality     11    1.3.0    backup! [Enter]    |
| (T) Construction  template      -     1.3.0    -       [Edit]    |
+------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F1-08 step 1, U11 | desktop | ![FL-F1-08 step 1, U11, light](../../images/08-provider-and-client-companies/u11-provider-admin/1-new-from-template-desktop-light.png) | ![FL-F1-08 step 1, U11, dark](../../images/08-provider-and-client-companies/u11-provider-admin/1-new-from-template-desktop-dark.png) |
| Error E1, U11 | desktop | ![Error E1, U11, light](../../images/08-provider-and-client-companies/u11-provider-admin/e1-database-not-created-desktop-light.png) | ![Error E1, U11, dark](../../images/08-provider-and-client-companies/u11-provider-admin/e1-database-not-created-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f01-10-client-companies-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f01-10-client-companies-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f01-10-client-companies-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f01-10-client-companies-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f01-10-client-companies-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f01-10-client-companies-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f01-10-client-companies-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f01-10-client-companies-offline-desktop-dark.png) |

## Fields and columns

| Label | Data |
|---|---|
| Company | E-F1-01 name |
| Template | E-F1-11 |
| Users | count |
| Version | simple-ERP version |
| Health | backups and errors |

## Actions

| Action | Who | Result |
|---|---|---|
| New from template | provider | UC-F1-10 |
| Enter | provider | UC-F1-11 |

## States

- Normal: The provider's list of client companies and templates: create, enter, watch, as the wireframe shows.
- Empty: no client yet.
- Loading: skeleton rows in place of the list ([C-03](../../../../04-ux/design-system/components/c-03-data-table.md));
  actions are disabled until it has loaded.
- Error: the error message pattern (D122).
- Read-only: a client company's details while a session of another provider administrator is live.
- Offline: Not available offline: a back-office screen on live, shared data (D38: only today's schedule, time and
  intervention records work offline). The app shows that it is offline and reloads the screen when the network is back.
- Warning: a client with a failed backup.

Shown entities (VD-15): [E-F1-11 Company template](../../data/e-f01-11-company-template.md),
[E-F1-01 Company](../../data/e-f01-01-company.md), [E-F1-12 Provider session](../../data/e-f01-12-provider-session.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F1-11 Company template | Template | Badge "Template"; a new record starts here; no other state; fields editable within the role | U07, U11 | `u07-administrator/s-f01-10-client-companies-e-f01-11-company-template-template-desktop-{light,dark}.png`, `u11-provider-admin/s-f01-10-client-companies-e-f01-11-company-template-template-desktop-{light,dark}.png` |
| E-F1-01 Company | In setup | Badge "In setup"; a new record starts here; next: Active (UC-F1-23); fields editable within the role | U07, U11 | `u07-administrator/s-f01-10-client-companies-e-f01-01-company-in-setup-desktop-{light,dark}.png`, `u11-provider-admin/s-f01-10-client-companies-e-f01-01-company-in-setup-desktop-{light,dark}.png` |
| E-F1-01 Company | Active | Badge "Active"; final: read-only, no next state; the history shows how it got here | U07, U11 | `u07-administrator/s-f01-10-client-companies-e-f01-01-company-active-desktop-{light,dark}.png`, `u11-provider-admin/s-f01-10-client-companies-e-f01-01-company-active-desktop-{light,dark}.png` |
| E-F1-12 Provider session | Live | Badge "Live"; a new record starts here; next: Closed (UC-F1-11); fields editable within the role | U07, U11 | `u07-administrator/s-f01-10-client-companies-e-f01-12-provider-session-live-desktop-{light,dark}.png`, `u11-provider-admin/s-f01-10-client-companies-e-f01-12-provider-session-live-desktop-{light,dark}.png` |
| E-F1-12 Provider session | Closed | Badge "Closed"; final: read-only, no next state; the history shows how it got here | U07, U11 | `u07-administrator/s-f01-10-client-companies-e-f01-12-provider-session-closed-desktop-{light,dark}.png`, `u11-provider-admin/s-f01-10-client-companies-e-f01-12-provider-session-closed-desktop-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop.

## Accessibility

Health is a word and an icon.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)

## Shown in

- [FL-F1-08 The provider and its client companies](../../flows/fl-f01-08-provider-and-client-companies.md)

## Open questions

None.

---

⬅️ [S-F1-09 Single sign-on](../07-set-up-single-sign-on/s-f01-09-single-sign-on.md) · ⬆️ [Up](README.md) ·
➡️ [S-F1-11 Provider access log](s-f01-11-provider-access-log.md)
