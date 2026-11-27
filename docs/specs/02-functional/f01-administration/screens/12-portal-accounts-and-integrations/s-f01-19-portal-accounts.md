🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🛡️ [F1 Administration](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F1-12 Portal accounts and integrations](README.md) › 🖥️ S-F1-19 Portal accounts

# 🖥️ S-F1-19 Portal accounts

**Status:** ✅ specified

## Personas

- [U07 Administrator](../../../../01-users/personas/u07-administrator.md)
- [U09 Customer](../../../../01-users/personas/u09-customer.md)
- [U10 Supplier](../../../../01-users/personas/u10-supplier.md)

## Purpose

The outside people with a portal account: invite, block, reset, audit; and the portal sign-in they see.

## Entry points

Administration › Portal accounts; Invite to the portal on a record.

## Wireframe

```text
+------------------------------------------------------------------+
| Portal accounts            [Portal: all v] [Status v] [search]   |
| Email              Linked to             Status   Last sign-in   |
| claire@durand.fr   Customer Durand SA    active   11-10 18:20    |
| ventes@lemoine.fr  Supplier Lemoine      blocked  10-02          |
| m.roche@mail.fr    Recipient J. Roche    invited  -              |
|                     [Block] [Reset] [See activity]               |
+------------------------------------------------------------------+
Portal sign-in (outside person, phone)
  Email [            ]  Password [        ]  [Sign in]
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F1-12 step 1, U07 | desktop | ![FL-F1-12 step 1, U07, light](../../images/12-portal-accounts-and-integrations/u07-administrator/1-portal-accounts-desktop-light.png) | ![FL-F1-12 step 1, U07, dark](../../images/12-portal-accounts-and-integrations/u07-administrator/1-portal-accounts-desktop-dark.png) |
| Error E1, U07 | desktop | ![Error E1, U07, light](../../images/12-portal-accounts-and-integrations/u07-administrator/e1-portal-accounts-refused-desktop-light.png) | ![Error E1, U07, dark](../../images/12-portal-accounts-and-integrations/u07-administrator/e1-portal-accounts-refused-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f01-19-portal-accounts-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f01-19-portal-accounts-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f01-19-portal-accounts-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f01-19-portal-accounts-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f01-19-portal-accounts-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f01-19-portal-accounts-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f01-19-portal-accounts-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f01-19-portal-accounts-offline-desktop-dark.png) |

## Fields and columns

| Label | Data | Editable |
|---|---|---|
| Email, linked records, status, last sign-in | E-F1-17 | status through actions |

## Actions

| Action | Who | Result |
|---|---|---|
| Invite | administrator, users with the portal right | Invitation valid 48 hours |
| Block, unblock | administrator | Sessions end at once |
| Reset | administrator | Password or two-factor reset link |
| See activity | administrator | Sign-ins and actions |

## States

- Normal: the portal accounts.
- Empty: no portal account yet: "Invite from a customer, supplier or record".
- Loading: skeleton rows ([C-03](../../../../04-ux/design-system/components/c-03-data-table.md)).
- Error: a record without an email (D122).
- Read-only: for users with the portal right but not the administration right: invite only.
- Offline: Not available offline: the portal is served live to outside people
  ([D407](../../../../06-decisions/technical/d407-front-end.md)).

Shown entities (VD-15): [E-F1-17 Portal account](../../data/e-f01-17-portal-account.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F1-17 Portal account | Invited | Badge "Invited"; a new record starts here; next: Active (UC-F1-19); fields editable within the role | U07, U09, U10 | `u07-administrator/s-f01-19-portal-accounts-e-f01-17-portal-account-invited-desktop-{light,dark}.png`, `u09-customer/s-f01-19-portal-accounts-e-f01-17-portal-account-invited-phone-{light,dark}.png`, `u10-supplier/s-f01-19-portal-accounts-e-f01-17-portal-account-invited-phone-{light,dark}.png` |
| E-F1-17 Portal account | Active | Badge "Active"; next: Blocked or Deactivated (UC-F1-19); fields editable within the role | U07, U09, U10 | `u07-administrator/s-f01-19-portal-accounts-e-f01-17-portal-account-active-desktop-{light,dark}.png`, `u09-customer/s-f01-19-portal-accounts-e-f01-17-portal-account-active-phone-{light,dark}.png`, `u10-supplier/s-f01-19-portal-accounts-e-f01-17-portal-account-active-phone-{light,dark}.png` |
| E-F1-17 Portal account | Blocked | Badge "Blocked"; next: Active (UC-F1-19); fields editable within the role | U07, U09, U10 | `u07-administrator/s-f01-19-portal-accounts-e-f01-17-portal-account-blocked-desktop-{light,dark}.png`, `u09-customer/s-f01-19-portal-accounts-e-f01-17-portal-account-blocked-phone-{light,dark}.png`, `u10-supplier/s-f01-19-portal-accounts-e-f01-17-portal-account-blocked-phone-{light,dark}.png` |
| E-F1-17 Portal account | Deactivated | Badge "Deactivated"; final: read-only, no next state; the history shows how it got here | U07, U09, U10 | `u07-administrator/s-f01-19-portal-accounts-e-f01-17-portal-account-deactivated-desktop-{light,dark}.png`, `u09-customer/s-f01-19-portal-accounts-e-f01-17-portal-account-deactivated-phone-{light,dark}.png`, `u10-supplier/s-f01-19-portal-accounts-e-f01-17-portal-account-deactivated-phone-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

The list on desktop and tablet; the portal sign-in on a phone.

## Accessibility

Every status is a word, not only a colour; tables have headers; actions are buttons with labels.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)
- [C-01 Button](../../../../04-ux/design-system/components/c-01-button.md)

## Shown in

- [FL-F1-12 Portal accounts and integrations](../../flows/fl-f01-12-portal-accounts-and-integrations.md)

## Open questions

None.

---

⬅️ [S-F1-18 Access reviews](../11-team-delegation-and-access-review/s-f01-18-access-reviews.md) · ⬆️ [Up](README.md) ·
➡️ [S-F1-20 API tokens](s-f01-20-api-tokens.md)
