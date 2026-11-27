🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 💇 [SC17 Beauty and wellness](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC17-05 Rentals, care records, client files and loyalty](README.md) ›
🖥️ S-SC17-20 Salon loyalty

# 🖥️ S-SC17-20 Salon loyalty

**Status:** 🔄 waiting for the owner

## Personas

- [U23 Store manager](../../../../01-users/personas/u23-store-manager.md): the programme, its rates and its results.
- [U09 Customer](../../../../01-users/personas/u09-customer.md): their own points and referrals.

## Purpose

Set the salon's earning rates, follow the points and rewards and record referrals.

## Entry points

Beauty and wellness › Loyalty; the till; the AI assistant.

## Wireframe

```text
+--------------------------------------------------------------------------------------------------+
| Loyalty: Rue Verte salon                                              Members 412                |
| Earning   Services 1 point per euro    Products 2 points per euro                                |
| Reward    200 points = 10 EUR on a service      Referral: 10 EUR for both                        |
| Client        Points   Next reward   Referred by                                                 |
| Camille R.    120      80 points     -                                                           |
| Noor A.       30       170 points    Camille R.                                                  |
+--------------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC17-05 step 4, U23 | desktop | ![FL-SC17-05 step 4, U23, light](../../images/05-rentals-care-records-and-loyalty/u23-store-manager/4-salon-loyalty-desktop-light.png) | ![FL-SC17-05 step 4, U23, dark](../../images/05-rentals-care-records-and-loyalty/u23-store-manager/4-salon-loyalty-desktop-dark.png) |
| FL-SC17-05 step 4, U23 | phone | ![FL-SC17-05 step 4, U23, light](../../images/05-rentals-care-records-and-loyalty/u23-store-manager/4-salon-loyalty-phone-light.png) | ![FL-SC17-05 step 4, U23, dark](../../images/05-rentals-care-records-and-loyalty/u23-store-manager/4-salon-loyalty-phone-dark.png) |
| FL-SC17-05 step 4, U23 | tablet | ![FL-SC17-05 step 4, U23, light](../../images/05-rentals-care-records-and-loyalty/u23-store-manager/4-salon-loyalty-tablet-light.png) | ![FL-SC17-05 step 4, U23, dark](../../images/05-rentals-care-records-and-loyalty/u23-store-manager/4-salon-loyalty-tablet-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc17-20-salon-loyalty-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc17-20-salon-loyalty-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc17-20-salon-loyalty-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc17-20-salon-loyalty-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc17-20-salon-loyalty-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc17-20-salon-loyalty-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc17-20-salon-loyalty-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc17-20-salon-loyalty-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Earning rate | E-F10-10 earning rule | points per euro | yes | yes |
| Reward | E-F10-10 reward | points and value | yes | yes |
| Client | E-F10-10 holder | link | no | yes |
| Points | E-F10-10 points | number | no | no |
| Referrer | E-F5-18 contact | link | yes at first booking | no |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Set the rates | header | manager | the earning rates change from the next sale |
| Record a referral | booking | beautician | the new client is linked to the referrer |
| Give the reward | referral row | manager | the reward is added to both cards |

## States

- Normal: the rates, the clients' points and the referrals.
- Empty: No client with points yet.
- Loading: the headings and the table as placeholders; the values follow.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); a self-referral
  or points above the balance, with the reason.
- Read-only: the record in a locked state: values shown, no action offered.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): none; no flow's Entities and screens table names an entity on this screen.

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

- [FL-SC17-05](../../flows/fl-sc17-05-rentals-care-records-and-loyalty.md)

## Open questions

None.

---

⬅️ [S-SC17-19 Client file](s-sc17-19-client-file.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC17-L01 Cabins](../00-lists/s-sc17-l01-cabins.md)
