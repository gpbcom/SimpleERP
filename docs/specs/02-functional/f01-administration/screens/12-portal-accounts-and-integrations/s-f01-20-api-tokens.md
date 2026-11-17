🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🛡️ [F1 Administration](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F1-12 Portal accounts and integrations](README.md) › 🖥️ S-F1-20 API tokens

# 🖥️ S-F1-20 API tokens

**Status:** ✅ specified

## Personas

- [U07 Administrator](../../../../01-users/personas/u07-administrator.md)
- [U11 IT provider administrator](../../../../01-users/personas/u11-provider-admin.md)

## Purpose

Service accounts and their tokens: create, scope, see use, revoke.

## Entry points

Administration › API tokens.

## Wireframe

```text
+------------------------------------------------------------------+
| API tokens                               [+ Service account]     |
| Service account  Role         Token   Scopes        Ends   Use   |
| EDI Lemoine      Sales        ..7f3a  orders write  06-30  1,240 |
| Reporting BI     Read only    ..a91c  all read      03-31  88    |
|                                 [New token] [Revoke]             |
+------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F1-12 step 4, U07 | desktop | ![FL-F1-12 step 4, U07, light](../../images/12-portal-accounts-and-integrations/u07-administrator/4-api-tokens-desktop-light.png) | ![FL-F1-12 step 4, U07, dark](../../images/12-portal-accounts-and-integrations/u07-administrator/4-api-tokens-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f01-20-api-tokens-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f01-20-api-tokens-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f01-20-api-tokens-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f01-20-api-tokens-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f01-20-api-tokens-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f01-20-api-tokens-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f01-20-api-tokens-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f01-20-api-tokens-offline-desktop-dark.png) |

## Fields and columns

| Label | Data | Editable |
|---|---|---|
| Service account, role | E-F1-18 service account | yes |
| Scopes, end date, allowed IPs | E-F1-18 | at creation |
| Last use, calls | E-F1-18 last use | no |

## Actions

| Action | Who | Result |
|---|---|---|
| New token | administrator | Shown once |
| Revoke | administrator | Calls refused at once |

## States

- Normal: service accounts and tokens.
- Empty: no service account: "Create one for each integration".
- Loading: skeleton rows ([C-03](../../../../04-ux/design-system/components/c-03-data-table.md)).
- Error: scopes beyond the role (D122).
- Read-only: revoked and expired tokens.
- Offline: Not available offline: an administration screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md)); the app shows that it is offline and reloads the
  screen when the network is back.

Shown entities (VD-15): [E-F1-18 API token](../../data/e-f01-18-api-token.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F1-18 API token | Active | Badge "Active"; a new record starts here; next: Revoked or Expired (UC-F1-20); fields editable within the role | U07 | `u07-administrator/s-f01-20-api-tokens-e-f01-18-api-token-active-desktop-{light,dark}.png` |
| E-F1-18 API token | Expired | Badge "Expired"; final: read-only, no next state; the history shows how it got here | U07 | `u07-administrator/s-f01-20-api-tokens-e-f01-18-api-token-expired-desktop-{light,dark}.png` |
| E-F1-18 API token | Revoked | Badge "Revoked"; final: read-only, no next state; the history shows how it got here | U07 | `u07-administrator/s-f01-20-api-tokens-e-f01-18-api-token-revoked-desktop-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop.

## Accessibility

Every status is a word, not only a colour; tables have headers; actions are buttons with labels.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-05 Modal](../../../../04-ux/design-system/components/c-05-modal.md)
- [C-01 Button](../../../../04-ux/design-system/components/c-01-button.md)

## Shown in

- [FL-F1-12 Portal accounts and integrations](../../flows/fl-f01-12-portal-accounts-and-integrations.md)

## Open questions

None.

---

⬅️ [S-F1-19 Portal accounts](s-f01-19-portal-accounts.md) · ⬆️ [Up](README.md) ·
➡️ [S-F1-21 Security policies](../13-security-and-audit/s-f01-21-security-policies.md)
