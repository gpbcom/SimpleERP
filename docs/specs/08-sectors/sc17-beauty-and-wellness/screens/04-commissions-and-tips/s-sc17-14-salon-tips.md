🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 💇 [SC17 Beauty and wellness](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC17-04 Commissions and tips](README.md) › 🖥️ S-SC17-14 Salon tips

# 🖥️ S-SC17-14 Salon tips

**Status:** ✅ specified

## Personas

- [U23 Store manager](../../../../01-users/personas/u23-store-manager.md): the tips and the sharing of the salon.
- [U52 Beautician](../../../../01-users/personas/u52-beautician.md): their own tips and shares.

## Purpose

Record tips, share them in full among the staff in contact with customers by the rule the salon posted, and give each
person a statement ([BR-SC17-14](../../business-rules/br-sc17-14-tips-are-shared-per-the-posted-rule.md),
[CR-FR-113](../../../../10-country-packs/france/labour/cr-fr-113-tips-sharing.md): the law sets no sharing key).

## Entry points

Beauty and wellness › Tips; the sale's page; the AI assistant.

## Wireframe

```text
+--------------------------------------------------------------------------------------------------+
| Tips: week 46            Rule: by hours worked, among the staff in contact with customers        |
| Date        Amount   Sale         Given to      State                                            |
| 2026-11-16  5.00     O-2026-5601  the team      Received                                         |
| 2026-11-17  3.00     O-2026-5632  Ines B.       Received                                         |
| Total 62.00 EUR   Ines B. 18.40   Louis T. 15.80   Sana M. 15.80   Lea D. 12.00                  |
| [Share the tips]  [Pay the shares]                                                               |
+--------------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC17-04 step 2, U23 | desktop | ![FL-SC17-04 step 2, U23, light](../../images/04-commissions-and-tips/u23-store-manager/2-salon-tips-desktop-light.png) | ![FL-SC17-04 step 2, U23, dark](../../images/04-commissions-and-tips/u23-store-manager/2-salon-tips-desktop-dark.png) |
| FL-SC17-04 step 2, U23 | phone | ![FL-SC17-04 step 2, U23, light](../../images/04-commissions-and-tips/u23-store-manager/2-salon-tips-phone-light.png) | ![FL-SC17-04 step 2, U23, dark](../../images/04-commissions-and-tips/u23-store-manager/2-salon-tips-phone-dark.png) |
| FL-SC17-04 step 2, U23 | tablet | ![FL-SC17-04 step 2, U23, light](../../images/04-commissions-and-tips/u23-store-manager/2-salon-tips-tablet-light.png) | ![FL-SC17-04 step 2, U23, dark](../../images/04-commissions-and-tips/u23-store-manager/2-salon-tips-tablet-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc17-14-salon-tips-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc17-14-salon-tips-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc17-14-salon-tips-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc17-14-salon-tips-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc17-14-salon-tips-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc17-14-salon-tips-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc17-14-salon-tips-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc17-14-salon-tips-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Date | E-SC17-10 received on | date | no | yes |
| Amount | E-SC17-10 amount | amount | no | yes |
| Sale | E-SC17-10 sale | link | no | yes |
| Given to | E-SC17-10 given to | the team or a person | yes while Received | no |
| Share | E-SC17-10 share | amount per person | no | no |
| Rule | E-SC17-10 rule | text: the salon's posted key, among the staff in contact with customers only | no | no |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Share the tips | header | manager | the tips of the period become Shared |
| Pay the shares | header | manager | the shares become Paid and go to payroll |
| Reverse | tip row | manager | the tip of a refunded sale is reversed |

## States

- Normal: the tips of the period, the posted rule and the shares.
- Empty: No tip in the period.
- Loading: the headings and the table as placeholders; the values follow.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); a sharing with
  no rule posted, or a refunded sale, with what to do.
- Read-only: the record in a locked state: values shown, no action offered.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-SC17-10 Tip](../../data/e-sc17-10-tip.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC17-10 Tip | Received | Badge "Received"; a new record starts here; next: Shared or Reversed (BR-SC17-14, UC-SC17-14); fields editable within the role | U23, U52 | `u23-store-manager/s-sc17-14-salon-tips-e-sc17-10-tip-received-{desktop,phone,tablet}-{light,dark}.png`, `u52-beautician/s-sc17-14-salon-tips-e-sc17-10-tip-received-{phone,tablet}-{light,dark}.png` |
| E-SC17-10 Tip | Shared | Badge "Shared"; next: Paid or Reversed (UC-SC17-14); fields editable within the role | U23, U52 | `u23-store-manager/s-sc17-14-salon-tips-e-sc17-10-tip-shared-{desktop,phone,tablet}-{light,dark}.png`, `u52-beautician/s-sc17-14-salon-tips-e-sc17-10-tip-shared-{phone,tablet}-{light,dark}.png` |
| E-SC17-10 Tip | Paid | Badge "Paid"; final: read-only, no next state; the history shows how it got here | U23, U52 | `u23-store-manager/s-sc17-14-salon-tips-e-sc17-10-tip-paid-{desktop,phone,tablet}-{light,dark}.png`, `u52-beautician/s-sc17-14-salon-tips-e-sc17-10-tip-paid-{phone,tablet}-{light,dark}.png` |
| E-SC17-10 Tip | Reversed | Badge "Reversed"; final: read-only, no next state; the history shows how it got here | U23, U52 | `u23-store-manager/s-sc17-14-salon-tips-e-sc17-10-tip-reversed-{desktop,phone,tablet}-{light,dark}.png`, `u52-beautician/s-sc17-14-salon-tips-e-sc17-10-tip-reversed-{phone,tablet}-{light,dark}.png` |

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

- [FL-SC17-04 Commissions and tips](../../flows/fl-sc17-04-commissions-and-tips.md)

## Open questions

None.

---

⬅️ [S-SC17-13 Commission plans](s-sc17-13-commission-plans.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC17-15 Staff targets](s-sc17-15-staff-targets.md)
