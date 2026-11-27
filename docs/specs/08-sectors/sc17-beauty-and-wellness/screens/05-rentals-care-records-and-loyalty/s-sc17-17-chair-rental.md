🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 💇 [SC17 Beauty and wellness](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC17-05 Rentals, care records, client files and loyalty](README.md) ›
🖥️ S-SC17-17 Chair rental

# 🖥️ S-SC17-17 Chair rental

**Status:** ✅ specified

## Personas

- [U23 Store manager](../../../../01-users/personas/u23-store-manager.md): every contract and rent of the salon.
- [U52 Beautician](../../../../01-users/personas/u52-beautician.md): their own contract when they rent a chair.

## Purpose

Sign a rental contract with an independent, bill the rent and give the renter their own calendar and invoices.

## Entry points

Beauty and wellness › Rental contracts; the cabin's page; the AI assistant.

## Wireframe

```text
+--------------------------------------------------------------------------------------------------+
| Rental contract RC-2026-07: Lea D., chair 2                              Active                  |
| Period 2026-09-01 to 2027-08-31   Rent 380.00 EUR a month   Notice 2 months                      |
| Identity SIRET 123 456 789 00012 checked   Insurance valid to 2027-06-30                         |
| Renter sets own hours, prices and clients: yes   Warning: none                                   |
| Next rent 2026-12-01     Own invoice series LD-    Own calendar: Chair 2                         |
| [Invoice the rent]  [End the contract]                                                           |
+--------------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC17-05 step 1, U23 | desktop | ![FL-SC17-05 step 1, U23, light](../../images/05-rentals-care-records-and-loyalty/u23-store-manager/1-chair-rental-desktop-light.png) | ![FL-SC17-05 step 1, U23, dark](../../images/05-rentals-care-records-and-loyalty/u23-store-manager/1-chair-rental-desktop-dark.png) |
| FL-SC17-05 step 1, U23 | phone | ![FL-SC17-05 step 1, U23, light](../../images/05-rentals-care-records-and-loyalty/u23-store-manager/1-chair-rental-phone-light.png) | ![FL-SC17-05 step 1, U23, dark](../../images/05-rentals-care-records-and-loyalty/u23-store-manager/1-chair-rental-phone-dark.png) |
| FL-SC17-05 step 1, U23 | tablet | ![FL-SC17-05 step 1, U23, light](../../images/05-rentals-care-records-and-loyalty/u23-store-manager/1-chair-rental-tablet-light.png) | ![FL-SC17-05 step 1, U23, dark](../../images/05-rentals-care-records-and-loyalty/u23-store-manager/1-chair-rental-tablet-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc17-17-chair-rental-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc17-17-chair-rental-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc17-17-chair-rental-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc17-17-chair-rental-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc17-17-chair-rental-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc17-17-chair-rental-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc17-17-chair-rental-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc17-17-chair-rental-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Renter | E-SC17-11 renter | link | no | yes |
| Place | E-SC17-11 place | chair or cabin | yes while Draft | yes |
| Period and rent | E-SC17-11 period, rent | dates and amount | yes while Draft | yes |
| Identity and insurance | E-SC17-11 identity, insurance | numbers and date | yes while Draft | yes |
| Notice | E-SC17-11 notice | months | yes while Draft | yes |
| Independence checks | E-SC17-11 independence checks | yes or no list | yes while Draft | yes |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| New contract | header | manager | a contract is created Draft |
| Send to sign | contract | manager | the renter signs electronically |
| Invoice the rent | contract | manager | the rent is invoiced on the due date |
| End the contract | contract | manager | the contract becomes Ended at the date of the notice |
| Terminate | contract | manager | the contract becomes Terminated with a reason |

## States

- Normal: the contract with the renter, place, rent, checks and next due date.
- Empty: No contract yet, with New contract.
- Loading: the headings and the table as placeholders; the values follow.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); a missing
  identity or insurance, or an independence warning, with what to do.
- Read-only: the record in a locked state: values shown, no action offered.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-SC17-11 Rental contract](../../data/e-sc17-11-rental-contract.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC17-11 Rental contract | Draft | Badge "Draft"; a new record starts here; next: Signed or Cancelled (UC-SC17-17); fields editable within the role | U23, U52 | `u23-store-manager/s-sc17-17-chair-rental-e-sc17-11-rental-contract-draft-{desktop,phone,tablet}-{light,dark}.png`, `u52-beautician/s-sc17-17-chair-rental-e-sc17-11-rental-contract-draft-{phone,tablet}-{light,dark}.png` |
| E-SC17-11 Rental contract | Signed | Badge "Signed"; next: Active (UC-SC17-17); fields editable within the role | U23, U52 | `u23-store-manager/s-sc17-17-chair-rental-e-sc17-11-rental-contract-signed-{desktop,phone,tablet}-{light,dark}.png`, `u52-beautician/s-sc17-17-chair-rental-e-sc17-11-rental-contract-signed-{phone,tablet}-{light,dark}.png` |
| E-SC17-11 Rental contract | Active | Badge "Active"; next: Ended or Terminated (UC-SC17-17, BR-SC17-17); fields editable within the role | U23, U52 | `u23-store-manager/s-sc17-17-chair-rental-e-sc17-11-rental-contract-active-{desktop,phone,tablet}-{light,dark}.png`, `u52-beautician/s-sc17-17-chair-rental-e-sc17-11-rental-contract-active-{phone,tablet}-{light,dark}.png` |
| E-SC17-11 Rental contract | Ended | Badge "Ended"; final: read-only, no next state; the history shows how it got here | U23, U52 | `u23-store-manager/s-sc17-17-chair-rental-e-sc17-11-rental-contract-ended-{desktop,phone,tablet}-{light,dark}.png`, `u52-beautician/s-sc17-17-chair-rental-e-sc17-11-rental-contract-ended-{phone,tablet}-{light,dark}.png` |
| E-SC17-11 Rental contract | Terminated | Badge "Terminated"; final: read-only, no next state; the history shows how it got here | U23, U52 | `u23-store-manager/s-sc17-17-chair-rental-e-sc17-11-rental-contract-terminated-{desktop,phone,tablet}-{light,dark}.png`, `u52-beautician/s-sc17-17-chair-rental-e-sc17-11-rental-contract-terminated-{phone,tablet}-{light,dark}.png` |
| E-SC17-11 Rental contract | Cancelled | Badge "Cancelled"; final: read-only, no next state; the history shows how it got here | U23, U52 | `u23-store-manager/s-sc17-17-chair-rental-e-sc17-11-rental-contract-cancelled-{desktop,phone,tablet}-{light,dark}.png`, `u52-beautician/s-sc17-17-chair-rental-e-sc17-11-rental-contract-cancelled-{phone,tablet}-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop first; the renter reads their contract on a phone.

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

⬅️ [S-SC17-16 Salon AI assistant](../04-commissions-and-tips/s-sc17-16-salon-assistant.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC17-18 Regulated care](s-sc17-18-regulated-care.md)
