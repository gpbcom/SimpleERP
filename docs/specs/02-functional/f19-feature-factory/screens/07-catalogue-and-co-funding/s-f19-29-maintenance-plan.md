🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🏭 [F19 Feature factory (hosted edition)](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F19-07 Similar features, catalogue, co-funding and maintenance](README.md) ›
🖥️ S-F19-29 Maintenance plan

# 🖥️ S-F19-29 Maintenance plan

**Status:** ✅ specified

## Personas

- [U13 Owner](../../../../01-users/personas/u13-owner.md): their features with or without a plan.

## Purpose

Keep a feature working across upgrades with a monthly plan, and see what it covers and costs.

Prices come from the hosted edition's price catalogue, a data file kept by the SimpleERP team, never from the
specification
([D566](../../../../06-decisions/foundations/d566-answers-of-2026-11-15-after-the-benchmark-gap-round.md)); the amounts
on this page are examples.

## Entry points

Feature factory › Maintenance plans; a feature's page; the hand-over of a source.

## Wireframe

```text
+---------------------------------------------------------------------------------------------+
| Maintenance plans                                    Features with a plan 2     Without 3      |
|---------------------------------------------------------------------------------------------|
| FEATURE                   HOW BOUGHT         PLAN        PRICE (excl. VAT)   NEXT UPGRADE      |
| Quote form field          Fixed price        Active      20 EUR a month      2.4 on 2026-12-03 |
| Lease reminders           Co-funded          None        20 EUR a month      2.4 on 2026-12-03 |
| Covers: adaptation to each upgrade, security fixes. Not covered: new functions.              |
| [Subscribe] [Cancel at month end]                                                            |
+---------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F19-07 step 4, U13 | desktop | ![FL-F19-07 step 4, U13, light](../../images/07-catalogue-and-co-funding/u13-owner/4-maintenance-plan-desktop-light.png) | ![FL-F19-07 step 4, U13, dark](../../images/07-catalogue-and-co-funding/u13-owner/4-maintenance-plan-desktop-dark.png) |
| FL-F19-07 step 4, U13 | phone | ![FL-F19-07 step 4, U13, light](../../images/07-catalogue-and-co-funding/u13-owner/4-maintenance-plan-phone-light.png) | ![FL-F19-07 step 4, U13, dark](../../images/07-catalogue-and-co-funding/u13-owner/4-maintenance-plan-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f19-29-maintenance-plan-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f19-29-maintenance-plan-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f19-29-maintenance-plan-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f19-29-maintenance-plan-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f19-29-maintenance-plan-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f19-29-maintenance-plan-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f19-29-maintenance-plan-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f19-29-maintenance-plan-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Feature | E-F19-19 feature | text | no | yes |
| How bought | E-F19-19 origin | fixed price, co-funded, source | no | yes |
| Plan state | E-F19-19 state | badge | by the owner | yes |
| Monthly price | E-F19-19 price | amount excluding VAT | no | yes |
| Covers | E-F19-19 covers | upgrades, security fixes | no | yes |
| Next upgrade | E-F19-19 next upgrade | version and date | no | no |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Subscribe | row | owner | starts the plan the next day and bills the first month |
| Cancel at month end | row | owner | the plan ends at the end of the month |
| Keep the plan | row | owner | undoes a cancellation before the month ends |
| Read the upgrade report | row | owner, administrator | what was tested and adapted |

## States

- Normal: the features with their plan, price and next upgrade.
- Empty: No feature to maintain: every feature is on the monthly price that includes upkeep.
- Loading: the headings and the table as placeholders; the values follow.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); a suspended
  plan shows the failed payment and what stops being adapted.
- Read-only: the record in a locked state: values shown, no action offered.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-F19-19 Feature maintenance plan](../../data/e-f19-19-feature-maintenance-plan.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F19-19 Feature maintenance plan | Offered | Badge "Offered"; a new record starts here; next: Active or Declined (UC-F19-30); fields editable within the role | U13 | `u13-owner/s-f19-29-maintenance-plan-e-f19-19-feature-maintenance-plan-offered-{desktop,phone}-{light,dark}.png` |
| E-F19-19 Feature maintenance plan | Active | Badge "Active"; next: Ending (BR-F19-23); fields editable within the role | U13 | `u13-owner/s-f19-29-maintenance-plan-e-f19-19-feature-maintenance-plan-active-{desktop,phone}-{light,dark}.png` |
| E-F19-19 Feature maintenance plan | Declined | Badge "Declined"; final: read-only, no next state; the history shows how it got here | U13 | `u13-owner/s-f19-29-maintenance-plan-e-f19-19-feature-maintenance-plan-declined-{desktop,phone}-{light,dark}.png` |
| E-F19-19 Feature maintenance plan | Ending | Badge "Ending"; next: Active or Ended (UC-F19-30, BR-F19-23); fields editable within the role | U13 | `u13-owner/s-f19-29-maintenance-plan-e-f19-19-feature-maintenance-plan-ending-{desktop,phone}-{light,dark}.png` |
| E-F19-19 Feature maintenance plan | Ended | Badge "Ended"; final: read-only, no next state; the history shows how it got here | U13 | `u13-owner/s-f19-29-maintenance-plan-e-f19-19-feature-maintenance-plan-ended-{desktop,phone}-{light,dark}.png` |

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

- [FL-F19-07](../../flows/fl-f19-07-catalogue-and-co-funding.md)

## Open questions

None.

---

⬅️ [S-F19-28 Co-funding](s-f19-28-co-funding.md) · ⬆️ [Up](README.md) ·
➡️ [S-F19-L01 Feature requests](../00-lists/s-f19-l01-feature-requests.md)
