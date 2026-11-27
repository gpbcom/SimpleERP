🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
💶 [F13 Payroll (plugin)](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F13-10 Special contracts and outsourced payroll](README.md) › 🖥️ S-F13-28 Posted workers

# 🖥️ S-F13-28 Posted workers

**Status:** ✅ specified

## Personas

- [U45 Payroll officer](../../../../01-users/personas/u45-payroll-officer.md): every posting of the company and its
  papers.

## Purpose

Record a posting with its A1 certificate or declaration receipt, check the host minimum and set the allowances.

## Entry points

Payroll (plugin) › Postings; the pay run's list of blocked employees.

## Wireframe

```text
+---------------------------------------------------------------------------------------------+
| Posting: Lea M., Belgium                            Draft   [Save] [Confirm posting]        |
|---------------------------------------------------------------------------------------------|
| Direction  Posted abroad     Dates  2026-12-01 to 2027-02-28    Place  Antwerp site         |
| Paper      A1 certificate  No. A1-26-0412   valid 2026-12-01 to 2027-06-30    OK            |
| Host minimum  12.80 EUR/h   Employee rate  14.10 EUR/h   Gap  none                          |
| Allowances  Accommodation 620 EUR/month   Travel 140 EUR/month                              |
| Days to start  17                                                                           |
+---------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F13-10 step 1, U45 | desktop | ![FL-F13-10 step 1, U45, light](../../images/10-special-contracts-and-outsourcing/u45-payroll-officer/1-posted-workers-desktop-light.png) | ![FL-F13-10 step 1, U45, dark](../../images/10-special-contracts-and-outsourcing/u45-payroll-officer/1-posted-workers-desktop-dark.png) |
| Error E1, U45 | desktop | ![Error E1, U45, light](../../images/10-special-contracts-and-outsourcing/u45-payroll-officer/e1-the-a1-certificate-is-missing-desktop-light.png) | ![Error E1, U45, dark](../../images/10-special-contracts-and-outsourcing/u45-payroll-officer/e1-the-a1-certificate-is-missing-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f13-28-posted-workers-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f13-28-posted-workers-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f13-28-posted-workers-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f13-28-posted-workers-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f13-28-posted-workers-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f13-28-posted-workers-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f13-28-posted-workers-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f13-28-posted-workers-offline-desktop-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Employee | E-F13-28 employee | name | no | yes |
| Direction | E-F13-28 direction | posted abroad, posted to France | yes while Draft | yes |
| Host country and place | E-F13-28 host | text | yes while Draft | yes |
| Dates | E-F13-28 start and end | two dates | yes while Draft | yes |
| Paper | E-F13-28 A1 number or receipt | text and dates | yes while Draft | yes |
| Host minimum and gap | E-F13-28 minimum check | amount and flag | no | no |
| Allowances | E-F13-28 allowances | amounts per month | yes while Draft or Documented | no |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Confirm posting | header | payroll officer | the posting becomes Documented |
| Extend | posting | payroll officer | a new end date, with the paper renewed |
| Close | posting | payroll officer | the posting ends and its allowances stop |
| Cancel | posting | payroll officer | a Draft or Documented posting that will not happen |

## States

- Normal: the posting with its paper, its host minimum check and its allowances.
- Empty: No posting yet, with New posting.
- Loading: the headings and the table as placeholders; the values follow.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); a missing or
  short paper shows what is missing and the days not covered.
- Read-only: the record in a locked state: values shown, no action offered.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-F13-28 Posting](../../data/e-f13-28-posting.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F13-28 Posting | Draft | Badge "Draft"; a new record starts here; next: Documented or Cancelled (BR-F13-25, UC-F13-35); fields editable within the role | U45 | `u45-payroll-officer/s-f13-28-posted-workers-e-f13-28-posting-draft-desktop-{light,dark}.png` |
| E-F13-28 Posting | Documented | Badge "Documented"; next: Active or Cancelled (UC-F13-35); fields editable within the role | U45 | `u45-payroll-officer/s-f13-28-posted-workers-e-f13-28-posting-documented-desktop-{light,dark}.png` |
| E-F13-28 Posting | Active | Badge "Active"; next: Ended (UC-F13-35); fields editable within the role | U45 | `u45-payroll-officer/s-f13-28-posted-workers-e-f13-28-posting-active-desktop-{light,dark}.png` |
| E-F13-28 Posting | Ended | Badge "Ended"; final: read-only, no next state; the history shows how it got here | U45 | `u45-payroll-officer/s-f13-28-posted-workers-e-f13-28-posting-ended-desktop-{light,dark}.png` |
| E-F13-28 Posting | Cancelled | Badge "Cancelled"; final: read-only, no next state; the history shows how it got here | U45 | `u45-payroll-officer/s-f13-28-posted-workers-e-f13-28-posting-cancelled-desktop-{light,dark}.png` |

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

- [FL-F13-10](../../flows/fl-f13-10-special-contracts-and-outsourcing.md)

## Open questions

None.

---

⬅️ [S-F13-27 Payroll analytics](../05-reports-and-rules/s-f13-27-payroll-analytics.md) · ⬆️ [Up](README.md) ·
➡️ [S-F13-29 Days-based contracts](s-f13-29-days-based-contracts.md)
