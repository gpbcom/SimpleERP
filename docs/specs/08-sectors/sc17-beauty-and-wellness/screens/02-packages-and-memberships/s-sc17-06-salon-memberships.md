🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 💇 [SC17 Beauty and wellness](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC17-02 Packages and memberships](README.md) ›
🖥️ S-SC17-06 Salon memberships

# 🖥️ S-SC17-06 Salon memberships

**Status:** 🔄 waiting for the owner

## Personas

- [U23 Store manager](../../../../01-users/personas/u23-store-manager.md): the plans, the members and the dues.
- [U09 Customer](../../../../01-users/personas/u09-customer.md): their own membership.

## Purpose

Set membership plans, sign members up, and follow the dues and the cancellations.

## Entry points

Beauty and wellness › Salon memberships; a customer's page; the AI assistant.

## Wireframe

```text
+--------------------------------------------------------------------------------------------------+
| Memberships                                                      Members 84   Dues paid 96%      |
| Plan   Fee/month   Included                    Members                                           |
| Glow   39.00 EUR   1 facial a month, 10% off   52                                                |
| Calm   59.00 EUR   1 massage a month, 15% off  32                                                |
| Member        Plan   Next due     State                                                          |
| Camille R.    Glow   2026-12-21   Active          [Pause] [Cancel]                               |
+--------------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC17-02 step 2, U23 | desktop | ![FL-SC17-02 step 2, U23, light](../../images/02-packages-and-memberships/u23-store-manager/2-salon-memberships-desktop-light.png) | ![FL-SC17-02 step 2, U23, dark](../../images/02-packages-and-memberships/u23-store-manager/2-salon-memberships-desktop-dark.png) |
| FL-SC17-02 step 2, U23 | phone | ![FL-SC17-02 step 2, U23, light](../../images/02-packages-and-memberships/u23-store-manager/2-salon-memberships-phone-light.png) | ![FL-SC17-02 step 2, U23, dark](../../images/02-packages-and-memberships/u23-store-manager/2-salon-memberships-phone-dark.png) |
| FL-SC17-02 step 2, U23 | tablet | ![FL-SC17-02 step 2, U23, light](../../images/02-packages-and-memberships/u23-store-manager/2-salon-memberships-tablet-light.png) | ![FL-SC17-02 step 2, U23, dark](../../images/02-packages-and-memberships/u23-store-manager/2-salon-memberships-tablet-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc17-06-salon-memberships-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc17-06-salon-memberships-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc17-06-salon-memberships-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc17-06-salon-memberships-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc17-06-salon-memberships-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc17-06-salon-memberships-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc17-06-salon-memberships-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc17-06-salon-memberships-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Plan | E-SC17-05 plan | name, fee, included services | yes while Active | yes |
| Member | E-SC17-05 member | link | no | yes |
| Start date | E-SC17-05 starts on | date | no | yes |
| Next due | E-SC17-05 next due | date | no | no |
| Terms accepted on | E-SC17-05 terms accepted on | date and time | no | no |
| Subscription | E-F6-07 subscription contract | link | no | no |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Sign up | header | beautician | a membership is created Active |
| Pause | member row | manager, member | the membership becomes Paused |
| Cancel | member row | manager, member | the membership ends at the date of the notice |
| Resume | member row | manager, member | a paused membership becomes Active |

## States

- Normal: the plans, the members with their next due and state, and the income of the month.
- Empty: No plan yet, with New plan.
- Loading: the headings and the table as placeholders; the values follow.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); a failed due or
  terms not accepted, with what to do.
- Read-only: the record in a locked state: values shown, no action offered.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-SC17-05 Salon membership](../../data/e-sc17-05-salon-membership.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC17-05 Salon membership | Active | Badge "Active"; a new record starts here; next: Paused or Cancelled (UC-SC17-06, BR-SC17-06); fields editable within the role | U23, U09 | `u23-store-manager/s-sc17-06-salon-memberships-e-sc17-05-salon-membership-active-{desktop,phone,tablet}-{light,dark}.png`, `u09-customer/s-sc17-06-salon-memberships-e-sc17-05-salon-membership-active-phone-{light,dark}.png` |
| E-SC17-05 Salon membership | Paused | Badge "Paused"; next: Active or Cancelled (UC-SC17-06, BR-SC17-06); fields editable within the role | U23, U09 | `u23-store-manager/s-sc17-06-salon-memberships-e-sc17-05-salon-membership-paused-{desktop,phone,tablet}-{light,dark}.png`, `u09-customer/s-sc17-06-salon-memberships-e-sc17-05-salon-membership-paused-phone-{light,dark}.png` |
| E-SC17-05 Salon membership | Cancelled | Badge "Cancelled"; next: Ended (BR-SC17-06); fields editable within the role | U23, U09 | `u23-store-manager/s-sc17-06-salon-memberships-e-sc17-05-salon-membership-cancelled-{desktop,phone,tablet}-{light,dark}.png`, `u09-customer/s-sc17-06-salon-memberships-e-sc17-05-salon-membership-cancelled-phone-{light,dark}.png` |
| E-SC17-05 Salon membership | Ended | Badge "Ended"; final: read-only, no next state; the history shows how it got here | U23, U09 | `u23-store-manager/s-sc17-06-salon-memberships-e-sc17-05-salon-membership-ended-{desktop,phone,tablet}-{light,dark}.png`, `u09-customer/s-sc17-06-salon-memberships-e-sc17-05-salon-membership-ended-phone-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

The beautician works on the tablet at the chair, the manager on a desktop and the customer on a phone, with the same
actions in one column.

## Accessibility

Every control is reachable by keyboard; states and errors are announced to screen readers and never rely on colour
alone; each field has its visible label.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)
- [C-01 Button](../../../../04-ux/design-system/components/c-01-button.md)

## Shown in

- [FL-SC17-02 Packages and memberships](../../flows/fl-sc17-02-packages-and-memberships.md)

## Open questions

None.

---

⬅️ [S-SC17-05 Packages](s-sc17-05-packages.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC17-07 Gift vouchers](s-sc17-07-gift-vouchers.md)
