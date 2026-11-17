🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🛒 [F6 Customers and sales](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F6-06 Accounts and credit](README.md) › 🖥️ S-F6-15 Account

# 🖥️ S-F6-15 Account

**Status:** ✅ specified

## Personas

- [U03 Sales](../../../../01-users/personas/u03-sales.md)
- [U41 Customer success manager](../../../../01-users/personas/u41-customer-success-manager.md)
- [U02 Manager](../../../../01-users/personas/u02-manager.md)

## Purpose

Show a customer with its parent, branches and timeline.

## Entry points

Sales › Customers › a customer.

## Wireframe

```text
+------------------------------------------------------------------+
| Brasserie du Parc (group)   parent: -   4 branches   [+ Branch]  |
| Sales 2026 312,000 EUR   Open 18,000   Limit 20,000   On hold 1  |
|------------------------------------------------------------------|
| Timeline                                     [Email] [Note]      |
| 11-12 09:14  email   achats@: "Order for December"   [Reply]     |
| 11-10 15:00  meeting Monthly review (checked)                    |
| 11-08        invoice INV-2026-1184  1,240 EUR  disputed          |
+------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F6-06 step 1, U03 | desktop | ![FL-F6-06 step 1, U03, light](../../images/06-accounts-and-credit/u03-sales/1-account-desktop-light.png) | ![FL-F6-06 step 1, U03, dark](../../images/06-accounts-and-credit/u03-sales/1-account-desktop-dark.png) |
| FL-F6-06 step 1, U03 | phone | ![FL-F6-06 step 1, U03, light](../../images/06-accounts-and-credit/u03-sales/1-account-phone-light.png) | ![FL-F6-06 step 1, U03, dark](../../images/06-accounts-and-credit/u03-sales/1-account-phone-dark.png) |
| FL-F6-06 step 1, U03 | tablet | ![FL-F6-06 step 1, U03, light](../../images/06-accounts-and-credit/u03-sales/1-account-tablet-light.png) | ![FL-F6-06 step 1, U03, dark](../../images/06-accounts-and-credit/u03-sales/1-account-tablet-dark.png) |
| Error E1, U03 | desktop | ![Error E1, U03, light](../../images/06-accounts-and-credit/u03-sales/e1-account-refused-desktop-light.png) | ![Error E1, U03, dark](../../images/06-accounts-and-credit/u03-sales/e1-account-refused-desktop-dark.png) |
| Error E1, U03 | phone | ![Error E1, U03, light](../../images/06-accounts-and-credit/u03-sales/e1-account-refused-phone-light.png) | ![Error E1, U03, dark](../../images/06-accounts-and-credit/u03-sales/e1-account-refused-phone-dark.png) |
| Error E1, U03 | tablet | ![Error E1, U03, light](../../images/06-accounts-and-credit/u03-sales/e1-account-refused-tablet-light.png) | ![Error E1, U03, dark](../../images/06-accounts-and-credit/u03-sales/e1-account-refused-tablet-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f06-15-account-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f06-15-account-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f06-15-account-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f06-15-account-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f06-15-account-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f06-15-account-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f06-15-account-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f06-15-account-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Editable |
|---|---|---|
| Parent, branches, figures | E-F6-01 | parent |
| Timeline | E-F6-11 | no |

## Actions

| Action | Who | Result |
|---|---|---|
| Reply | sales | Email from the timeline |
| Attach branch | sales, managers | Parent set |

## States

- Normal: show a customer with its parent, branches and timeline.
- Empty: a new customer: "No activity yet" with Log a call and Send an email.
- Loading: skeleton entries in the timeline ([C-14](../../../../04-ux/design-system/components/c-14-timeline.md)).
- Error: the error message pattern (D122).
- Read-only: accounts outside the user's area: read only for managers.
- Offline: Readable offline for the rep's own customers loaded before leaving,
  [UC-F6-21](../../use-cases/09-sell-on-the-road-and-steer-sales/uc-f06-21-take-orders-offline-on-the-road.md); replies
  wait for the network.

Shown entities (VD-15): [E-F6-01 Customer record](../../data/e-f06-01-customer-record.md),
[E-F6-11 Timeline entry](../../data/e-f06-11-timeline-entry.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F6-01 Customer record | Accepted | Badge "Accepted"; a new record starts here; next: Active (UC-F6-11); fields editable within the role | U03 | `u03-sales/s-f06-15-account-e-f06-01-customer-record-accepted-{desktop,phone,tablet}-{light,dark}.png` |
| E-F6-01 Customer record | Active | Badge "Active"; final: read-only, no next state; the history shows how it got here | U03 | `u03-sales/s-f06-15-account-e-f06-01-customer-record-active-{desktop,phone,tablet}-{light,dark}.png` |
| E-F6-11 Timeline entry | Recorded | Badge "Recorded"; a new record starts here; no other state; fields editable within the role | U03 | `u03-sales/s-f06-15-account-e-f06-11-timeline-entry-recorded-{desktop,phone,tablet}-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop, tablet and phone: the timeline on a phone.

## Accessibility

Every status is a word, not only a colour; tables have headers; actions are buttons with labels.

## Components

- [C-14 Timeline](../../../../04-ux/design-system/components/c-14-timeline.md)
- [C-04 Card](../../../../04-ux/design-system/components/c-04-card.md)
- [C-01 Button](../../../../04-ux/design-system/components/c-01-button.md)

## Shown in

- [FL-F6-06 Accounts and credit](../../flows/fl-f06-06-accounts-and-credit.md)

## Open questions

None.

---

⬅️ [S-F6-14 Usage billing](../05-benchmark-additions/s-f06-14-usage-billing.md) · ⬆️ [Up](README.md) ·
➡️ [S-F6-16 Credit control](s-f06-16-credit-control.md)
