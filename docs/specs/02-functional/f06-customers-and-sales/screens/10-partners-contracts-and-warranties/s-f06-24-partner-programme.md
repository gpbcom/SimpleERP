🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🛒 [F6 Customers and sales](../../README.md) › 🖥️ [Screens](../README.md) › 🖥️ S-F6-24 Partner programme

# 🖥️ S-F6-24 Partner programme

**Status:** ✅ specified

## Personas

- [U03 Sales](../../../../01-users/personas/u03-sales.md): the partners, their leads and their tiers.
- [U51 Reseller partner](../../../../01-users/personas/u51-reseller-partner.md): their own leads, deals and commissions
  in the partner portal.

## Purpose

Manage the partners, forward leads to them, and follow their deals and commissions.

## Entry points

Customers and sales › Partners; a lead's Forward to a partner action; the partner portal.

## Wireframe

```text
+---------------------------------------------------------------------------------------------+
| Partner programme       Partners 14   Leads forwarded 38   Commissions due 6,420 EUR         |
|---------------------------------------------------------------------------------------------|
| PARTNER             TIER    TERRITORY   LEADS  DEALS  REVENUE   COMMISSION   STATE          |
| Nord Distribution   Gold    Hauts-de-F  9      4      86,000    4,300        Active         |
| Sud Solutions       Silver  Occitanie   5      1      12,000    600          Active         |
| [Forward a lead] [Invite a partner] [Change tier] [Suspend]                                 |
+---------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F6-10 step 1, U03 | desktop | ![FL-F6-10 step 1, U03, light](../../images/10-partners-contracts-and-warranties/u03-sales/1-partner-programme-desktop-light.png) | ![FL-F6-10 step 1, U03, dark](../../images/10-partners-contracts-and-warranties/u03-sales/1-partner-programme-desktop-dark.png) |
| FL-F6-10 step 1, U03 | phone | ![FL-F6-10 step 1, U03, light](../../images/10-partners-contracts-and-warranties/u03-sales/1-partner-programme-phone-light.png) | ![FL-F6-10 step 1, U03, dark](../../images/10-partners-contracts-and-warranties/u03-sales/1-partner-programme-phone-dark.png) |
| FL-F6-10 step 1, U03 | tablet | ![FL-F6-10 step 1, U03, light](../../images/10-partners-contracts-and-warranties/u03-sales/1-partner-programme-tablet-light.png) | ![FL-F6-10 step 1, U03, dark](../../images/10-partners-contracts-and-warranties/u03-sales/1-partner-programme-tablet-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f06-24-partner-programme-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f06-24-partner-programme-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f06-24-partner-programme-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f06-24-partner-programme-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f06-24-partner-programme-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f06-24-partner-programme-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f06-24-partner-programme-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f06-24-partner-programme-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Partner | E-F6-23 name | text | yes while Applied | yes |
| Tier | E-F6-23 tier | badge | yes | yes |
| Territory | E-F6-23 territory | text | yes | no |
| Leads and deals | E-F6-20, E-F6-02 | two counts | no | yes |
| Revenue | E-F6-05 of the partner's deals | amount with currency | no | yes |
| Commission | E-F6-19 | amount with currency | no | yes |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Forward a lead | lead, header | sales | the lead changes owner and leaves its pipeline |
| Invite a partner | header | sales | an application link goes to the partner |
| Change tier | row | sales | the commission plan and the protection period change |
| Suspend | row | sales | open leads return to their owners |

## States

- Normal: the partners with their counts and the commissions due; the partner portal shows the same for one partner.
- Empty: No partner yet, with Invite a partner.
- Loading: the headings and the table as placeholders; the values follow.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); a lead that
  cannot be forwarded shows the partner who holds it.
- Read-only: the record in a locked state: values shown, no action offered.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-F6-23 Partner](../../data/e-f06-23-partner.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F6-23 Partner | Applied | Badge "Applied"; a new record starts here; next: Active or Refused (UC-F6-27); fields editable within the role | U03, U51 | `u03-sales/s-f06-24-partner-programme-e-f06-23-partner-applied-{desktop,phone,tablet}-{light,dark}.png`, `u51-reseller-partner/s-f06-24-partner-programme-e-f06-23-partner-applied-desktop-{light,dark}.png` |
| E-F6-23 Partner | Active | Badge "Active"; next: Suspended or Ended (UC-F6-27); fields editable within the role | U03, U51 | `u03-sales/s-f06-24-partner-programme-e-f06-23-partner-active-{desktop,phone,tablet}-{light,dark}.png`, `u51-reseller-partner/s-f06-24-partner-programme-e-f06-23-partner-active-desktop-{light,dark}.png` |
| E-F6-23 Partner | Refused | Badge "Refused"; final: read-only, no next state; the history shows how it got here | U03, U51 | `u03-sales/s-f06-24-partner-programme-e-f06-23-partner-refused-{desktop,phone,tablet}-{light,dark}.png`, `u51-reseller-partner/s-f06-24-partner-programme-e-f06-23-partner-refused-desktop-{light,dark}.png` |
| E-F6-23 Partner | Suspended | Badge "Suspended"; next: Active or Ended (UC-F6-27); fields editable within the role | U03, U51 | `u03-sales/s-f06-24-partner-programme-e-f06-23-partner-suspended-{desktop,phone,tablet}-{light,dark}.png`, `u51-reseller-partner/s-f06-24-partner-programme-e-f06-23-partner-suspended-desktop-{light,dark}.png` |
| E-F6-23 Partner | Ended | Badge "Ended"; final: read-only, no next state; the history shows how it got here | U03, U51 | `u03-sales/s-f06-24-partner-programme-e-f06-23-partner-ended-{desktop,phone,tablet}-{light,dark}.png`, `u51-reseller-partner/s-f06-24-partner-programme-e-f06-23-partner-ended-desktop-{light,dark}.png` |

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

- [FL-F6-10](../../flows/fl-f06-10-partners-contracts-and-warranties.md)

## Open questions

None.

---

⬅️ [S-F6-23 Pro-forma invoice](../07-special-invoicing/s-f06-23-pro-forma-invoice.md) · ⬆️ [Up](README.md) ·
➡️ [S-F6-25 Company identifiers](s-f06-25-company-identifiers.md)
