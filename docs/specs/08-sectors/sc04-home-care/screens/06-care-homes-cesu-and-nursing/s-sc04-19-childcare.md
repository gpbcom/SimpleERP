🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🏠 [SC04 Home care](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC04-06 Care homes, CESU, agent mode, childcare and nursing](README.md) ›
🖥️ S-SC04-19 Childcare

# 🖥️ S-SC04-19 Childcare

**Status:** ✅ specified

## Personas

- [U25 Care coordinator](../../../../01-users/personas/u25-care-coordinator.md): every childcare contract and statement.
- [U26 Carer](../../../../01-users/personas/u26-carer.md): the contracts of the children they look after.

## Purpose

Agree the childcare contract, compute the aid and the parents' share, and follow the carer's visits.

## Entry points

Home care › Childcare contracts; the family's page; the carer's day list on the phone.

## Wireframe

```text
+--------------------------------------------------------------------------------------------------+
| Contract: Lea M. (3 years), parents Nadia and Karim M.                   Active   [Save] [Amend] |
| Carer Aisha T.   Schedule Mon-Fri 08:30-14:30   30 h a week   Rate 10.00 EUR/h                   |
| Month 2026-11   Hours 120   Cost 1,200.00 EUR   Aid 480.00 EUR   Parents' share 720.00 EUR       |
| Aid table  2026 v2   Family resources recorded 2026-10-04                                        |
| Visits  Mon 2 Nov 08:31-14:28 done   Tue 3 Nov 08:29-14:33 done                                  |
| Statement  to issue 2026-12-01                                   [Issue statement]               |
+--------------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC04-06 step 4, U25 | desktop | ![FL-SC04-06 step 4, U25, light](../../images/06-care-homes-cesu-and-nursing/u25-care-coordinator/4-childcare-desktop-light.png) | ![FL-SC04-06 step 4, U25, dark](../../images/06-care-homes-cesu-and-nursing/u25-care-coordinator/4-childcare-desktop-dark.png) |
| FL-SC04-06 step 4, U25 | phone | ![FL-SC04-06 step 4, U25, light](../../images/06-care-homes-cesu-and-nursing/u25-care-coordinator/4-childcare-phone-light.png) | ![FL-SC04-06 step 4, U25, dark](../../images/06-care-homes-cesu-and-nursing/u25-care-coordinator/4-childcare-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc04-19-childcare-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc04-19-childcare-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc04-19-childcare-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc04-19-childcare-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc04-19-childcare-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc04-19-childcare-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc04-19-childcare-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc04-19-childcare-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Child | E-SC04-17 child | link | no | yes |
| Parents | E-SC04-17 parents | customer links | no | yes |
| Carer | E-SC04-17 carer | link | yes while Draft | yes |
| Schedule and rate | E-SC04-17 schedule, rate | hours and amount | yes while Draft | yes |
| Aid and share | E-SC04-17 aid, share | amounts | no | no |
| Aid table version | E-SC04-17 table version | text | no | no |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Compute the aid | header | coordinator | the aid and the parents' share |
| Send for signature | header | coordinator | the parents sign on the phone |
| Amend | contract | coordinator | an amendment, the aid recomputed from its date |
| Issue statement | month row | coordinator | the parents' share is invoiced |

## States

- Normal: the contract with the child, the carer, the schedule, the aid computed and the visits of the month.
- Empty: No contract yet, with New contract.
- Loading: the headings and the table as placeholders; the values follow.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); missing family
  resources or a carer without the qualification, with what to do.
- Read-only: the record in a locked state: values shown, no action offered.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-SC04-17 Childcare contract](../../data/e-sc04-17-childcare-contract.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC04-17 Childcare contract | Draft | Badge "Draft"; a new record starts here; next: Active (UC-SC04-19); fields editable within the role | U25, U26 | `u25-care-coordinator/s-sc04-19-childcare-e-sc04-17-childcare-contract-draft-{desktop,phone}-{light,dark}.png`, `u26-carer/s-sc04-19-childcare-e-sc04-17-childcare-contract-draft-phone-{light,dark}.png` |
| E-SC04-17 Childcare contract | Active | Badge "Active"; next: Suspended or Ended (UC-SC04-19); fields editable within the role | U25, U26 | `u25-care-coordinator/s-sc04-19-childcare-e-sc04-17-childcare-contract-active-{desktop,phone}-{light,dark}.png`, `u26-carer/s-sc04-19-childcare-e-sc04-17-childcare-contract-active-phone-{light,dark}.png` |
| E-SC04-17 Childcare contract | Suspended | Badge "Suspended"; next: Active (UC-SC04-19); fields editable within the role | U25, U26 | `u25-care-coordinator/s-sc04-19-childcare-e-sc04-17-childcare-contract-suspended-{desktop,phone}-{light,dark}.png`, `u26-carer/s-sc04-19-childcare-e-sc04-17-childcare-contract-suspended-phone-{light,dark}.png` |
| E-SC04-17 Childcare contract | Ended | Badge "Ended"; final: read-only, no next state; the history shows how it got here | U25, U26 | `u25-care-coordinator/s-sc04-19-childcare-e-sc04-17-childcare-contract-ended-{desktop,phone}-{light,dark}.png`, `u26-carer/s-sc04-19-childcare-e-sc04-17-childcare-contract-ended-phone-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

The coordinator works on a desktop; the carer and the family use the phone, with the same actions in one column.

## Accessibility

Every control is reachable by keyboard; states and errors are announced to screen readers and never rely on colour
alone; each field has its visible label.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)
- [C-01 Button](../../../../04-ux/design-system/components/c-01-button.md)

## Shown in

- [FL-SC04-06](../../flows/fl-sc04-06-care-homes-cesu-and-nursing.md)

## Open questions

None.

---

⬅️ [S-SC04-18 Agent mode](s-sc04-18-agent-mode.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC04-20 Home nursing](s-sc04-20-home-nursing.md)
