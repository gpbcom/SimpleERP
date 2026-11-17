🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🏗️ [SC01 Construction](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC01-06 Price revision, off-plan sales, BIM and grants](README.md) ›
🖥️ S-SC01-17 Off-plan sales

# 🖥️ S-SC01-17 Off-plan sales

**Status:** 🔄 waiting for the owner

## Personas

- [U35 Real-estate agent](../../../../01-users/personas/u35-real-estate-agent.md): every lot of the programmes they
  sell.
- [U09 Customer](../../../../01-users/personas/u09-customer.md): their own lot, stages and calls.

## Purpose

Follow the lots of a programme, reserve and sell them, and see each call for funds against the stage that releases it.

## Entry points

Construction › Off-plan lots; the programme's site page; the customer portal for the buyer.

## Wireframe

```text
+--------------------------------------------------------------------------------------------------+
| Programme: Les Tilleuls            Lots 24   Sold 11   Reserved 3   Available 10                 |
| Lot A-12  3 rooms  62 m2  300,000.00 EUR   Sold    Buyer: Amir K.                                |
| Stage             Cap    Called    Paid      State                                               |
| Foundations       35 %   105,000   105,000   Paid                                                |
| Watertight        70 %   105,000   0         Due 2026-12-01                                      |
| Completion        95 %   0         0         Waiting                                             |
| Delivery balance   5 %   0         0         Waiting         [Call for funds]                    |
+--------------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC01-06 step 2, U35 | desktop | ![FL-SC01-06 step 2, U35, light](../../images/06-revision-developers-bim-and-grants/u35-real-estate-agent/2-off-plan-sales-desktop-light.png) | ![FL-SC01-06 step 2, U35, dark](../../images/06-revision-developers-bim-and-grants/u35-real-estate-agent/2-off-plan-sales-desktop-dark.png) |
| FL-SC01-06 step 2, U35 | phone | ![FL-SC01-06 step 2, U35, light](../../images/06-revision-developers-bim-and-grants/u35-real-estate-agent/2-off-plan-sales-phone-light.png) | ![FL-SC01-06 step 2, U35, dark](../../images/06-revision-developers-bim-and-grants/u35-real-estate-agent/2-off-plan-sales-phone-dark.png) |
| FL-SC01-06 step 2, U35 | tablet | ![FL-SC01-06 step 2, U35, light](../../images/06-revision-developers-bim-and-grants/u35-real-estate-agent/2-off-plan-sales-tablet-light.png) | ![FL-SC01-06 step 2, U35, dark](../../images/06-revision-developers-bim-and-grants/u35-real-estate-agent/2-off-plan-sales-tablet-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc01-17-off-plan-sales-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc01-17-off-plan-sales-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc01-17-off-plan-sales-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc01-17-off-plan-sales-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc01-17-off-plan-sales-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc01-17-off-plan-sales-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc01-17-off-plan-sales-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc01-17-off-plan-sales-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Lot | E-SC01-16 lot | text | yes while Available | yes |
| Programme | E-SC01-16 programme | link to the site | no | yes |
| Price | E-SC01-16 price | amount | yes while Available or Reserved | yes |
| Buyer | E-SC01-16 buyer | customer link | yes while Reserved | no |
| Deed date | E-SC01-16 deed date | date | yes while Reserved | no |
| Stage and cap | E-SC01-16 stage schedule | stage, percentage | no | no |
| Called and paid | E-SC01-16 called, paid | amounts | no | no |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Reserve | lot | real estate agent | the lot becomes Reserved with its deposit |
| Record the deed | lot | real estate agent | the lot becomes Sold and its schedule is built |
| Call for funds | stage row | accounting | the call within the cap, invoiced to the buyer |
| Deliver | lot | site manager | the balance is called and the lot becomes Delivered |
| Withdraw | lot | real estate agent | the lot becomes Available when the buyer withdraws in time |

## States

- Normal: the lots of the programme, and for one lot its schedule of stages, caps, calls and payments.
- Empty: No lot yet, with New lot.
- Loading: the headings and the table as placeholders; the values follow.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); a call above
  its cap or a missing guarantee, with the amount allowed.
- Read-only: the record in a locked state: values shown, no action offered.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-SC01-16 Off-plan lot](../../data/e-sc01-16-off-plan-lot.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC01-16 Off-plan lot | Available | Badge "Available"; a new record starts here; next: Reserved (UC-SC01-17); fields editable within the role | U35, U09 | `u35-real-estate-agent/s-sc01-17-off-plan-sales-e-sc01-16-off-plan-lot-available-{desktop,phone,tablet}-{light,dark}.png`, `u09-customer/s-sc01-17-off-plan-sales-e-sc01-16-off-plan-lot-available-phone-{light,dark}.png` |
| E-SC01-16 Off-plan lot | Reserved | Badge "Reserved"; next: Available or Sold (UC-SC01-17, BR-SC01-17); fields editable within the role | U35, U09 | `u35-real-estate-agent/s-sc01-17-off-plan-sales-e-sc01-16-off-plan-lot-reserved-{desktop,phone,tablet}-{light,dark}.png`, `u09-customer/s-sc01-17-off-plan-sales-e-sc01-16-off-plan-lot-reserved-phone-{light,dark}.png` |
| E-SC01-16 Off-plan lot | Sold | Badge "Sold"; next: Delivered (UC-SC01-17); fields editable within the role | U35, U09 | `u35-real-estate-agent/s-sc01-17-off-plan-sales-e-sc01-16-off-plan-lot-sold-{desktop,phone,tablet}-{light,dark}.png`, `u09-customer/s-sc01-17-off-plan-sales-e-sc01-16-off-plan-lot-sold-phone-{light,dark}.png` |
| E-SC01-16 Off-plan lot | Delivered | Badge "Delivered"; final: read-only, no next state; the history shows how it got here | U35, U09 | `u35-real-estate-agent/s-sc01-17-off-plan-sales-e-sc01-16-off-plan-lot-delivered-{desktop,phone,tablet}-{light,dark}.png`, `u09-customer/s-sc01-17-off-plan-sales-e-sc01-16-off-plan-lot-delivered-phone-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop for the agent; the buyer's view on the phone shows the stage reached, the call due and the payment button.

## Accessibility

Every control is reachable by keyboard; states and errors are announced to screen readers and never rely on colour
alone; each field has its visible label.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)
- [C-01 Button](../../../../04-ux/design-system/components/c-01-button.md)

## Shown in

- [FL-SC01-06](../../flows/fl-sc01-06-revision-developers-bim-and-grants.md)

## Open questions

None.

---

⬅️ [S-SC01-16 Price revision](s-sc01-16-price-revision.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC01-18 BIM quantities](s-sc01-18-bim-quantities.md)
