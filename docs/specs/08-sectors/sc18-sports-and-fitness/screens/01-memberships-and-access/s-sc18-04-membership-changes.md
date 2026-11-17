🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🏋️ [SC18 Sports and fitness](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC18-01 Memberships and access](README.md) ›
🖥️ S-SC18-04 Membership changes

# 🖥️ S-SC18-04 Membership changes

**Status:** 🔄 waiting for the owner

## Personas

- [U13 Owner](../../../../01-users/personas/u13-owner.md): every freeze and cancellation.
- [U09 Customer](../../../../01-users/personas/u09-customer.md): their own membership.

## Purpose

Freeze or cancel a membership and show the effect date, the last due and any fee.

## Entry points

The member's app › My membership; Sports and fitness › Club memberships; the AI assistant.

## Wireframe

```text
+--------------------------------------------------------------------------------------------------+
| My membership: Annual adult                                                Active                |
| Commitment ended 2026-11-30   Notice 1 month                                                     |
| [ ] Freeze for  [ 2 months v ]       [x] Cancel                                                  |
| Asked on 2026-12-10   Ends on 2027-01-10   Last due 2027-01-01   Fee 0.00 EUR                    |
| Reason (optional) [ moving to another city                      ]                                |
| [Confirm]  [Withdraw the request]                                                                |
+--------------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC18-01 step 4, U13 | desktop | ![FL-SC18-01 step 4, U13, light](../../images/01-memberships-and-access/u13-owner/4-membership-changes-desktop-light.png) | ![FL-SC18-01 step 4, U13, dark](../../images/01-memberships-and-access/u13-owner/4-membership-changes-desktop-dark.png) |
| FL-SC18-01 step 4, U13 | phone | ![FL-SC18-01 step 4, U13, light](../../images/01-memberships-and-access/u13-owner/4-membership-changes-phone-light.png) | ![FL-SC18-01 step 4, U13, dark](../../images/01-memberships-and-access/u13-owner/4-membership-changes-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc18-04-membership-changes-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc18-04-membership-changes-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc18-04-membership-changes-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc18-04-membership-changes-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc18-04-membership-changes-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc18-04-membership-changes-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc18-04-membership-changes-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc18-04-membership-changes-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Membership | E-SC18-01 plan | link | no | yes |
| Request | E-SC18-01 request | freeze or cancel | yes | yes |
| Length | E-SC18-01 freeze months | number | yes | no |
| Effect date | E-SC18-01 notice ends on | date | no | no |
| Last due | E-F6-07 next due | date | no | no |
| Reason | E-SC18-01 reason | text | yes | no |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Confirm | footer | member, owner | the membership becomes Frozen or has Notice given |
| Withdraw the request | footer | member, owner | a request not yet in effect is withdrawn |
| Waive the fee | footer | owner | a fee is waived with a reason |

## States

- Normal: the request, its effect date, the last due and any fee.
- Empty: The membership has no request.
- Loading: the headings and the table as placeholders; the values follow.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); a notice too
  short or a commitment not ended, with the earliest date.
- Read-only: the record in a locked state: values shown, no action offered.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): none; no flow's Entities and screens table names an entity on this screen.

## Responsive behaviour

The coach and the member use the phone, the owner and the treasurer a desktop, with the same actions in one column.

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

⬅️ [S-SC18-03 Door access](s-sc18-03-door-access.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC18-05 Class timetable](../02-classes-and-waiting-lists/s-sc18-05-class-timetable.md)
