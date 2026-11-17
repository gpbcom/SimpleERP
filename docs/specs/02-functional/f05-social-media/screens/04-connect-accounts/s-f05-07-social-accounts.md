🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
📣 [F5 Social media and marketing](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F5-04 Connect accounts](README.md) › 🖥️ S-F5-07 Social accounts

# 🖥️ S-F5-07 Social accounts

**Status:** ✅ specified

## Personas

- [U07 Administrator](../../../../01-users/personas/u07-administrator.md)
- [U12 Marketing](../../../../01-users/personas/u12-marketing.md)

## Purpose

Connect the company's accounts.

## Entry points

Social media in the menu.

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F5-04 step 1, U07 | desktop | ![FL-F5-04 step 1, U07, light](../../images/04-connect-accounts/u07-administrator/1-connect-accounts-desktop-light.png) | ![FL-F5-04 step 1, U07, dark](../../images/04-connect-accounts/u07-administrator/1-connect-accounts-desktop-dark.png) |
| Error E1, U07 | desktop | ![Error E1, U07, light](../../images/04-connect-accounts/u07-administrator/e1-app-not-reviewed-desktop-light.png) | ![Error E1, U07, dark](../../images/04-connect-accounts/u07-administrator/e1-app-not-reviewed-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f05-07-social-accounts-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f05-07-social-accounts-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f05-07-social-accounts-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f05-07-social-accounts-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f05-07-social-accounts-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f05-07-social-accounts-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f05-07-social-accounts-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f05-07-social-accounts-offline-desktop-dark.png) |

## Fields and columns

As its use case.

## Actions

As its use case's main flow.

## States

- Normal: Connect the company's accounts, as the wireframe shows.
- Empty: No connected account yet, with Connect an account.
- Loading: skeleton rows in place of the list ([C-03](../../../../04-ux/design-system/components/c-03-data-table.md));
  actions are disabled until it has loaded.
- Error: the error message pattern (D122).
- Read-only: for users without the marketing right; published items.
- Offline: Not available offline: a back-office screen on live, shared data (D38: only today's schedule, time and
  intervention records work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-F5-02 Social account](../../data/e-f05-02-social-account.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F5-02 Social account | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U07, U12 | `u07-administrator/s-f05-07-social-accounts-e-f05-02-social-account-active-desktop-{light,dark}.png`, `u12-marketing/s-f05-07-social-accounts-e-f05-02-social-account-active-{desktop,phone}-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop; the inbox and approvals also on the phone.

## Accessibility

Labelled controls; states as text.

## Components

- [C-04 Card](../../../../04-ux/design-system/components/c-04-card.md)
- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)

## Shown in

- [FL-F5-04 Connect accounts](../../flows/fl-f05-04-connect-accounts.md)

## Open questions

None.

---

⬅️ [S-F5-06 Social statistics](../03-inbox-and-statistics/s-f05-06-social-statistics.md) · ⬆️ [Up](README.md) ·
➡️ [S-F5-08 Email campaign](../05-benchmark-additions/s-f05-08-email-campaign.md)
