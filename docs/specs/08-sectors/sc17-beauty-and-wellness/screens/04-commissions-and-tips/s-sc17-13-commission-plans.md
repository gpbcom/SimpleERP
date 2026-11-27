🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 💇 [SC17 Beauty and wellness](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC17-04 Commissions and tips](README.md) › 🖥️ S-SC17-13 Commission plans

# 🖥️ S-SC17-13 Commission plans

**Status:** ✅ specified

## Personas

- [U23 Store manager](../../../../01-users/personas/u23-store-manager.md): the plans and the commission lines of every
  employee.

## Purpose

Create commission plans, assign them to staff and see the commission lines they produce.

## Entry points

Beauty and wellness › Commission plans; the staff page; the AI assistant.

## Wireframe

```text
+--------------------------------------------------------------------------------------------------+
| Commission plans                                                        [New plan]               |
| Plan     Services   Products   Tiers                       Staff   State                         |
| Spring   8%         12%        +2% above 6,000 EUR/month   3       In force                      |
| Winter   7%         10%        none                        3       Ended                         |
| Assigned to  Ines B.  Louis T.  Sana M.                                                          |
| [Assign]  [End the plan]                                                                         |
+--------------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC17-04 step 1, U23 | desktop | ![FL-SC17-04 step 1, U23, light](../../images/04-commissions-and-tips/u23-store-manager/1-commission-plans-desktop-light.png) | ![FL-SC17-04 step 1, U23, dark](../../images/04-commissions-and-tips/u23-store-manager/1-commission-plans-desktop-dark.png) |
| FL-SC17-04 step 1, U23 | phone | ![FL-SC17-04 step 1, U23, light](../../images/04-commissions-and-tips/u23-store-manager/1-commission-plans-phone-light.png) | ![FL-SC17-04 step 1, U23, dark](../../images/04-commissions-and-tips/u23-store-manager/1-commission-plans-phone-dark.png) |
| FL-SC17-04 step 1, U23 | tablet | ![FL-SC17-04 step 1, U23, light](../../images/04-commissions-and-tips/u23-store-manager/1-commission-plans-tablet-light.png) | ![FL-SC17-04 step 1, U23, dark](../../images/04-commissions-and-tips/u23-store-manager/1-commission-plans-tablet-dark.png) |
| Error E1, U23 | desktop | ![Error E1, U23, light](../../images/04-commissions-and-tips/u23-store-manager/e1-no-commission-plan-is-in-force-desktop-light.png) | ![Error E1, U23, dark](../../images/04-commissions-and-tips/u23-store-manager/e1-no-commission-plan-is-in-force-desktop-dark.png) |
| Error E1, U23 | phone | ![Error E1, U23, light](../../images/04-commissions-and-tips/u23-store-manager/e1-no-commission-plan-is-in-force-phone-light.png) | ![Error E1, U23, dark](../../images/04-commissions-and-tips/u23-store-manager/e1-no-commission-plan-is-in-force-phone-dark.png) |
| Error E1, U23 | tablet | ![Error E1, U23, light](../../images/04-commissions-and-tips/u23-store-manager/e1-no-commission-plan-is-in-force-tablet-light.png) | ![Error E1, U23, dark](../../images/04-commissions-and-tips/u23-store-manager/e1-no-commission-plan-is-in-force-tablet-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc17-13-commission-plans-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc17-13-commission-plans-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc17-13-commission-plans-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc17-13-commission-plans-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc17-13-commission-plans-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc17-13-commission-plans-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc17-13-commission-plans-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc17-13-commission-plans-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Plan | E-SC17-09 name | text | yes while Draft | yes |
| Service rate | E-SC17-09 service rate | percent | yes while Draft | yes |
| Product rate | E-SC17-09 product rate | percent | yes while Draft | yes |
| Tiers | E-SC17-09 tiers | thresholds and rates | yes while Draft | no |
| Dates | E-SC17-09 starts and ends | two dates | yes while Draft | yes |
| Staff | E-SC17-09 staff | list | yes | yes |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| New plan | header | manager | a plan is created Draft |
| Put in force | plan row | manager | the plan becomes In force at its start date |
| End the plan | plan row | manager | the plan becomes Ended at the date given |
| Assign | plan row | manager | the plan applies to the staff chosen |

## States

- Normal: the plans with their rates, dates and staff.
- Empty: No plan yet, with New plan.
- Loading: the headings and the table as placeholders; the values follow.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); overlapping
  dates or a sale with no plan, with the people and dates.
- Read-only: the record in a locked state: values shown, no action offered.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-SC17-09 Salon commission plan](../../data/e-sc17-09-commission-plan.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC17-09 Salon commission plan | Draft | Badge "Draft"; a new record starts here; next: In force or Cancelled (BR-SC17-13, UC-SC17-13); fields editable within the role | U23 | `u23-store-manager/s-sc17-13-commission-plans-e-sc17-09-commission-plan-draft-{desktop,phone,tablet}-{light,dark}.png` |
| E-SC17-09 Salon commission plan | In force | Badge "In force"; next: Ended (UC-SC17-13); fields editable within the role | U23 | `u23-store-manager/s-sc17-13-commission-plans-e-sc17-09-commission-plan-in-force-{desktop,phone,tablet}-{light,dark}.png` |
| E-SC17-09 Salon commission plan | Ended | Badge "Ended"; final: read-only, no next state; the history shows how it got here | U23 | `u23-store-manager/s-sc17-13-commission-plans-e-sc17-09-commission-plan-ended-{desktop,phone,tablet}-{light,dark}.png` |
| E-SC17-09 Salon commission plan | Cancelled | Badge "Cancelled"; final: read-only, no next state; the history shows how it got here | U23 | `u23-store-manager/s-sc17-13-commission-plans-e-sc17-09-commission-plan-cancelled-{desktop,phone,tablet}-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop first; the staff member reads their own plan on the tablet.

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

⬅️ [S-SC17-12 Cosmetics safety](../03-salon-retail-and-stock/s-sc17-12-cosmetics-safety.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC17-14 Salon tips](s-sc17-14-salon-tips.md)
