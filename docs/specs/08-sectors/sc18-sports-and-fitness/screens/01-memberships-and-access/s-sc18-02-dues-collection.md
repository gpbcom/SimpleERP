🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🏋️ [SC18 Sports and fitness](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC18-01 Memberships and access](README.md) › 🖥️ S-SC18-02 Dues collection

# 🖥️ S-SC18-02 Dues collection

**Status:** 🔄 waiting for the owner

## Personas

- [U31 Treasurer](../../../../01-users/personas/u31-treasurer.md): the dues, mandates and rejections of the club.

## Purpose

Collect the dues by direct debit from signed mandates and follow the rejections.

## Entry points

Sports and fitness › Dues mandates; the treasurer's workspace; the AI assistant.

## Wireframe

```text
+--------------------------------------------------------------------------------------------------+
| Dues collection: December                                          Run on 2026-12-01             |
| Due 200 members   With an active mandate 198   Without 2   Total 7,720.00 EUR                    |
| Member        Mandate           Amount   State                                                   |
| Mia L.        RUM-2026-0881     39.00    Active                                                  |
| Jules P.      -                 39.00    No mandate: contact                                     |
| [Send the debit file]  [Contact the members without a mandate]  [Retry the rejected]             |
+--------------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC18-01 step 2, U31 | desktop | ![FL-SC18-01 step 2, U31, light](../../images/01-memberships-and-access/u31-treasurer/2-dues-collection-desktop-light.png) | ![FL-SC18-01 step 2, U31, dark](../../images/01-memberships-and-access/u31-treasurer/2-dues-collection-desktop-dark.png) |
| FL-SC18-01 step 2, U31 | phone | ![FL-SC18-01 step 2, U31, light](../../images/01-memberships-and-access/u31-treasurer/2-dues-collection-phone-light.png) | ![FL-SC18-01 step 2, U31, dark](../../images/01-memberships-and-access/u31-treasurer/2-dues-collection-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc18-02-dues-collection-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc18-02-dues-collection-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc18-02-dues-collection-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc18-02-dues-collection-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc18-02-dues-collection-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc18-02-dues-collection-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc18-02-dues-collection-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc18-02-dues-collection-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Member | E-SC18-02 member | link | no | yes |
| Mandate reference | E-SC18-02 reference | text | no | yes |
| Signed on | E-SC18-02 signed on | date and time | no | yes |
| Account | E-SC18-02 account | masked IBAN | yes while Pending | yes |
| Amount and date | E-F6-05 invoice | amount and date | no | yes |
| State | E-SC18-02 state | badge | no | no |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Collect a mandate | member | member | a mandate is created Pending then Active when signed |
| Send the debit file | header | treasurer | the dues with an active mandate are sent |
| Revoke | mandate row | treasurer, member | the mandate becomes Revoked |
| Retry | rejected row | treasurer | the due is sent again on the next date |

## States

- Normal: the dues of the run with the mandate of each member and the amount.
- Empty: No due in this run.
- Loading: the headings and the table as placeholders; the values follow.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); a due with no
  mandate, or a rejected payment, with the reason.
- Read-only: the record in a locked state: values shown, no action offered.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-SC18-02 Dues mandate](../../data/e-sc18-02-dues-mandate.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC18-02 Dues mandate | Pending | Badge "Pending"; a new record starts here; next: Active or Expired (BR-SC18-02, UC-SC18-02); fields editable within the role | U31 | `u31-treasurer/s-sc18-02-dues-collection-e-sc18-02-dues-mandate-pending-{desktop,phone}-{light,dark}.png` |
| E-SC18-02 Dues mandate | Active | Badge "Active"; next: Suspended or Revoked (UC-SC18-02); fields editable within the role | U31 | `u31-treasurer/s-sc18-02-dues-collection-e-sc18-02-dues-mandate-active-{desktop,phone}-{light,dark}.png` |
| E-SC18-02 Dues mandate | Suspended | Badge "Suspended"; next: Active (UC-SC18-02); fields editable within the role | U31 | `u31-treasurer/s-sc18-02-dues-collection-e-sc18-02-dues-mandate-suspended-{desktop,phone}-{light,dark}.png` |
| E-SC18-02 Dues mandate | Revoked | Badge "Revoked"; final: read-only, no next state; the history shows how it got here | U31 | `u31-treasurer/s-sc18-02-dues-collection-e-sc18-02-dues-mandate-revoked-{desktop,phone}-{light,dark}.png` |
| E-SC18-02 Dues mandate | Expired | Badge "Expired"; final: read-only, no next state; the history shows how it got here | U31 | `u31-treasurer/s-sc18-02-dues-collection-e-sc18-02-dues-mandate-expired-{desktop,phone}-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop first; the member signs the mandate on a phone.

## Accessibility

Every control is reachable by keyboard; states and errors are announced to screen readers and never rely on colour
alone; each field has its visible label.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)
- [C-01 Button](../../../../04-ux/design-system/components/c-01-button.md)

## Shown in

- [FL-SC18-01 Memberships and access](../../flows/fl-sc18-01-memberships-and-access.md)

## Open questions

None.

---

⬅️ [S-SC18-01 Membership sale](s-sc18-01-membership-sale.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC18-03 Door access](s-sc18-03-door-access.md)
