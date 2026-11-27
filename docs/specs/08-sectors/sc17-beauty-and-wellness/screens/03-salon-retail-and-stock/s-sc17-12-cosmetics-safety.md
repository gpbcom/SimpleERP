🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 💇 [SC17 Beauty and wellness](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC17-03 Salon retail and stock](README.md) ›
🖥️ S-SC17-12 Cosmetics safety

# 🖥️ S-SC17-12 Cosmetics safety

**Status:** ✅ specified

## Personas

- [U23 Store manager](../../../../01-users/personas/u23-store-manager.md): the safety records of every product of the
  salon.

## Purpose

Keep each product's safety sheet, batch and supplier, and block and trace a recalled batch.

## Entry points

Beauty and wellness › Safety records; the stock list; the AI assistant.

## Wireframe

```text
+--------------------------------------------------------------------------------------------------+
| Safety records                                                       1 batch recalled            |
| Product          Batch     Expiry     Supplier            State                                  |
| Colour 6.3       L-7782    2028-03    Beta Hair Supply    Recalled                               |
| Facial cream     L-9120    2027-08    Lune Cosmetics      Current                                |
| Recalled batch L-7782: 14 visits, 12 clients, stock blocked                                      |
| [Contact the clients]  [Attach a sheet]  [Mark as recalled]                                      |
+--------------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC17-03 step 4, U23 | desktop | ![FL-SC17-03 step 4, U23, light](../../images/03-salon-retail-and-stock/u23-store-manager/4-cosmetics-safety-desktop-light.png) | ![FL-SC17-03 step 4, U23, dark](../../images/03-salon-retail-and-stock/u23-store-manager/4-cosmetics-safety-desktop-dark.png) |
| FL-SC17-03 step 4, U23 | phone | ![FL-SC17-03 step 4, U23, light](../../images/03-salon-retail-and-stock/u23-store-manager/4-cosmetics-safety-phone-light.png) | ![FL-SC17-03 step 4, U23, dark](../../images/03-salon-retail-and-stock/u23-store-manager/4-cosmetics-safety-phone-dark.png) |
| FL-SC17-03 step 4, U23 | tablet | ![FL-SC17-03 step 4, U23, light](../../images/03-salon-retail-and-stock/u23-store-manager/4-cosmetics-safety-tablet-light.png) | ![FL-SC17-03 step 4, U23, dark](../../images/03-salon-retail-and-stock/u23-store-manager/4-cosmetics-safety-tablet-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc17-12-cosmetics-safety-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc17-12-cosmetics-safety-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc17-12-cosmetics-safety-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc17-12-cosmetics-safety-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc17-12-cosmetics-safety-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc17-12-cosmetics-safety-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc17-12-cosmetics-safety-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc17-12-cosmetics-safety-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Product | E-SC17-08 product | link | no | yes |
| Batch | E-SC17-08 batch | text | yes while Current | yes |
| Expiry | E-SC17-08 expiry | month | yes while Current | yes |
| Safety sheet | E-SC17-08 safety sheet | document | yes while Current | yes |
| Responsible company | E-SC17-08 responsible company | text | yes while Current | yes |
| Recall notice | E-SC17-08 recall notice | document | yes | no |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Attach a sheet | product row | manager | the sheet is stored with the product |
| Mark as recalled | batch row | manager | the batch becomes Recalled and stock is blocked |
| Contact the clients | recall | manager | a message is prepared for each client listed |
| Archive | batch row | manager | an expired batch leaves the list |

## States

- Normal: the products with their batch, expiry, sheet and state.
- Empty: No record yet, with Attach a sheet.
- Loading: the headings and the table as placeholders; the values follow.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); a label without
  a batch or a responsible company, with what to do.
- Read-only: the record in a locked state: values shown, no action offered.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-SC17-08 Safety record](../../data/e-sc17-08-safety-record.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC17-08 Safety record | Current | Badge "Current"; a new record starts here; next: Recalled or Expired (BR-SC17-12, UC-SC17-12); fields editable within the role | U23 | `u23-store-manager/s-sc17-12-cosmetics-safety-e-sc17-08-safety-record-current-{desktop,phone,tablet}-{light,dark}.png` |
| E-SC17-08 Safety record | Recalled | Badge "Recalled"; next: Archived (UC-SC17-12); fields editable within the role | U23 | `u23-store-manager/s-sc17-12-cosmetics-safety-e-sc17-08-safety-record-recalled-{desktop,phone,tablet}-{light,dark}.png` |
| E-SC17-08 Safety record | Expired | Badge "Expired"; next: Archived (UC-SC17-12); fields editable within the role | U23 | `u23-store-manager/s-sc17-12-cosmetics-safety-e-sc17-08-safety-record-expired-{desktop,phone,tablet}-{light,dark}.png` |
| E-SC17-08 Safety record | Archived | Badge "Archived"; final: read-only, no next state; the history shows how it got here | U23 | `u23-store-manager/s-sc17-12-cosmetics-safety-e-sc17-08-safety-record-archived-{desktop,phone,tablet}-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop first; the tablet shows the records of the products at the chair.

## Accessibility

Every control is reachable by keyboard; states and errors are announced to screen readers and never rely on colour
alone; each field has its visible label.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)
- [C-01 Button](../../../../04-ux/design-system/components/c-01-button.md)

## Shown in

- [FL-SC17-03 Salon retail and stock](../../flows/fl-sc17-03-salon-retail-and-stock.md)

## Open questions

None.

---

⬅️ [S-SC17-11 Salon replenishment](s-sc17-11-salon-replenishment.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC17-13 Commission plans](../04-commissions-and-tips/s-sc17-13-commission-plans.md)
