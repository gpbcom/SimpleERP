🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
💸 [F22 Unified platform cost management](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F22-08 Credits, SaaS subscriptions, carbon and routing](README.md) › 🖥️ S-F22-27 Credit packs

# 🖥️ S-F22-27 Credit packs

**Status:** 🔄 waiting for the owner

## Personas

- [U07 Administrator](../../../../01-users/personas/u07-administrator.md): every pack, its balance and its top-up rule.
- [U13 Owner](../../../../01-users/personas/u13-owner.md): the packs waiting for approval and the money spent.

## Purpose

Buy packs of prepaid units, set automatic top-up inside the budget and follow each balance.

## Entry points

Platform costs › Credit packs; a budget warning; the hosted quota screen.

## Wireframe

```text
+---------------------------------------------------------------------------------------------+
| Credit packs                                   Active 3   Low 1   Budget left 120 EUR  [+ Buy] |
|---------------------------------------------------------------------------------------------|
| KIND        PROVIDER     UNITS LEFT       PRICE   VALID UNTIL   AUTO TOP-UP     STATE        |
| AI tokens   provider A   4.1 M of 5 M     40 EUR  2027-11-14    on, max 2 a mo  Active       |
| Scraping    provider B   8,200 of 100,000 90 EUR  2027-06-30    off             Low          |
| [Buy a pack] [Set top-up] [Approve] [Open budget]                                           |
+---------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F22-08 step 1, U07 | desktop | ![FL-F22-08 step 1, U07, light](../../images/08-credits-saas-and-carbon/u07-administrator/1-credit-packs-desktop-light.png) | ![FL-F22-08 step 1, U07, dark](../../images/08-credits-saas-and-carbon/u07-administrator/1-credit-packs-desktop-dark.png) |
| Error E1, U07 | desktop | ![Error E1, U07, light](../../images/08-credits-saas-and-carbon/u07-administrator/e1-the-budget-is-reached-desktop-light.png) | ![Error E1, U07, dark](../../images/08-credits-saas-and-carbon/u07-administrator/e1-the-budget-is-reached-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f22-27-credit-packs-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f22-27-credit-packs-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f22-27-credit-packs-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f22-27-credit-packs-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f22-27-credit-packs-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f22-27-credit-packs-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f22-27-credit-packs-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f22-27-credit-packs-offline-desktop-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Kind and provider | E-F22-19 kind, provider | text | while Ordered | yes |
| Units bought and left | E-F22-19 units | two numbers | no | yes |
| Price and unit price | E-F22-19 price | amounts with currency | no | yes |
| Valid until | E-F22-19 valid until | date | no | yes |
| Automatic top-up | E-F22-19 top-up rule | on or off, threshold, monthly maximum | yes | no |
| Budget left | E-F22-06 amount left | amount with currency | no | no |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Buy a pack | header | administrator | orders the pack, after the owner's approval above the set amount |
| Set top-up | row | administrator | saves the threshold and the monthly maximum |
| Approve or refuse | row | owner | lets the purchase go on or cancels it |
| Open budget | row | administrator, owner | opens the budget of the pack's level |

## States

- Normal: the packs with kind, balance, price, expiry, top-up rule and state, and the budget left.
- Empty: No pack yet, with Buy a pack and the unit prices of the price list.
- Loading: the headings and the table as placeholders; the values follow.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); a purchase
  refused for budget shows the budget left, the pack's price and Raise the budget.
- Read-only: the record in a locked state: values shown, no action offered.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-F22-19 Credit pack](../../data/e-f22-19-credit-pack.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F22-19 Credit pack | Ordered | Badge "Ordered"; a new record starts here; next: Active or Cancelled (UC-F22-27); fields editable within the role | U07, U13 | `u07-administrator/s-f22-27-credit-packs-e-f22-19-credit-pack-ordered-desktop-{light,dark}.png`, `u13-owner/s-f22-27-credit-packs-e-f22-19-credit-pack-ordered-{desktop,phone}-{light,dark}.png` |
| E-F22-19 Credit pack | Active | Badge "Active"; next: Low, Used up or Expired (UC-F22-27); fields editable within the role | U07, U13 | `u07-administrator/s-f22-27-credit-packs-e-f22-19-credit-pack-active-desktop-{light,dark}.png`, `u13-owner/s-f22-27-credit-packs-e-f22-19-credit-pack-active-{desktop,phone}-{light,dark}.png` |
| E-F22-19 Credit pack | Cancelled | Badge "Cancelled"; final: read-only, no next state; the history shows how it got here | U07, U13 | `u07-administrator/s-f22-27-credit-packs-e-f22-19-credit-pack-cancelled-desktop-{light,dark}.png`, `u13-owner/s-f22-27-credit-packs-e-f22-19-credit-pack-cancelled-{desktop,phone}-{light,dark}.png` |
| E-F22-19 Credit pack | Low | Badge "Low"; next: Used up or Expired (UC-F22-27); fields editable within the role | U07, U13 | `u07-administrator/s-f22-27-credit-packs-e-f22-19-credit-pack-low-desktop-{light,dark}.png`, `u13-owner/s-f22-27-credit-packs-e-f22-19-credit-pack-low-{desktop,phone}-{light,dark}.png` |
| E-F22-19 Credit pack | Used up | Badge "Used up"; final: read-only, no next state; the history shows how it got here | U07, U13 | `u07-administrator/s-f22-27-credit-packs-e-f22-19-credit-pack-used-up-desktop-{light,dark}.png`, `u13-owner/s-f22-27-credit-packs-e-f22-19-credit-pack-used-up-{desktop,phone}-{light,dark}.png` |
| E-F22-19 Credit pack | Expired | Badge "Expired"; final: read-only, no next state; the history shows how it got here | U07, U13 | `u07-administrator/s-f22-27-credit-packs-e-f22-19-credit-pack-expired-desktop-{light,dark}.png`, `u13-owner/s-f22-27-credit-packs-e-f22-19-credit-pack-expired-{desktop,phone}-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop only; on a phone, the app asks to continue on a larger screen.

## Accessibility

Every control is reachable by keyboard; states and errors are announced to screen readers and never rely on colour
alone; each field has its visible label.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)
- [C-01 Button](../../../../04-ux/design-system/components/c-01-button.md)

## Shown in

- [FL-F22-08](../../flows/fl-f22-08-credits-saas-and-carbon.md)

## Open questions

None.

---

⬅️ [S-F22-26 Client statements](../07-it-provider-re-billing/s-f22-26-client-statements.md) · ⬆️ [Up](README.md) ·
➡️ [S-F22-28 SaaS subscriptions](s-f22-28-saas-subscriptions.md)
