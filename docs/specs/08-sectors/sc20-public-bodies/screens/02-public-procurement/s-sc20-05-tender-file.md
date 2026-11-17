🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🏛️ [SC20 Public bodies](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC20-02 Public procurement](README.md) › 🖥️ S-SC20-05 Tender file

# 🖥️ S-SC20-05 Tender file

**Status:** 🔄 waiting for the owner

## Personas

- [U54 Public finance officer](../../../../01-users/personas/u54-public-finance-officer.md): the files with their
  estimate, procedure, criteria and dates.

## Purpose

Prepare the tender file of a purchase with the procedure its value requires and its criteria.

## Entry points

Public bodies › Tender files; a purchase need.

## Wireframe

```text
+--------------------------------------------------------------------------------------------------+
| Tender file AO-2027-014: School catering                  State: Draft   [Check procedure]       |
| Kind: Services    Estimate: 190,000 EUR excl. VAT    Procedure: Formal (above threshold)         |
| Criteria          Weight        Deadline for bids: 12 May 2027 12:00                             |
| Price             50            Documents: specifications, draft contract                        |
| Quality           40            Approved by: -                                                   |
| Environment       10            [Attach documents] [Send for approval]                           |
+--------------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC20-02 step 1, U54 | desktop | ![FL-SC20-02 step 1, U54, light](../../images/02-public-procurement/u54-public-finance-officer/1-tender-file-desktop-light.png) | ![FL-SC20-02 step 1, U54, dark](../../images/02-public-procurement/u54-public-finance-officer/1-tender-file-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc20-05-tender-file-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc20-05-tender-file-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc20-05-tender-file-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc20-05-tender-file-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc20-05-tender-file-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc20-05-tender-file-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-sc20-05-tender-file-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-sc20-05-tender-file-offline-desktop-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Object | E-SC20-05 object | text | yes while Draft | yes |
| Kind | E-SC20-05 kind | works, supplies, services | yes while Draft | yes |
| Estimate | E-SC20-05 estimate | amount excl. VAT | yes while Draft | yes |
| Procedure | E-SC20-05 procedure | text from the thresholds | no | yes |
| Criteria | E-SC20-05 criteria | list of criterion and weight | yes while Draft | yes |
| Bid deadline | E-SC20-05 deadline | date and time | yes while Draft | yes |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Check procedure | header | public finance officer | the procedure of the value is shown |
| Attach documents | header | public finance officer | the specifications are added |
| Send for approval | header | public finance officer | the elected official is asked |

## States

- Normal: the file with object, kind, estimate, procedure, criteria, deadline and state.
- Empty: No tender file yet, with New file.
- Loading: the headings and the table as placeholders; the values follow.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); a procedure not
  matching the value, weights not adding to 100, with the field to correct.
- Read-only: the record in a locked state: values shown, no action offered.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-SC20-05 Tender file](../../data/e-sc20-05-tender-file.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC20-05 Tender file | Draft | Badge "Draft"; a new record starts here; next: Published (UC-SC20-06); fields editable within the role | U54 | `u54-public-finance-officer/s-sc20-05-tender-file-e-sc20-05-tender-file-draft-desktop-{light,dark}.png` |
| E-SC20-05 Tender file | Published | Badge "Published"; next: Analysed or Cancelled (UC-SC20-07, UC-SC20-06); fields editable within the role | U54 | `u54-public-finance-officer/s-sc20-05-tender-file-e-sc20-05-tender-file-published-desktop-{light,dark}.png` |
| E-SC20-05 Tender file | Analysed | Badge "Analysed"; next: Awarded or Cancelled (BR-SC20-07, UC-SC20-07); fields editable within the role | U54 | `u54-public-finance-officer/s-sc20-05-tender-file-e-sc20-05-tender-file-analysed-desktop-{light,dark}.png` |
| E-SC20-05 Tender file | Awarded | Badge "Awarded"; final: read-only, no next state; the history shows how it got here | U54 | `u54-public-finance-officer/s-sc20-05-tender-file-e-sc20-05-tender-file-awarded-desktop-{light,dark}.png` |
| E-SC20-05 Tender file | Cancelled | Badge "Cancelled"; final: read-only, no next state; the history shows how it got here | U54 | `u54-public-finance-officer/s-sc20-05-tender-file-e-sc20-05-tender-file-cancelled-desktop-{light,dark}.png` |

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

- [FL-SC20-02 Public procurement](../../flows/fl-sc20-02-public-procurement.md)

## Open questions

None.

---

⬅️ [S-SC20-04 Treasury exchange](../01-public-accounting/s-sc20-04-treasury-exchange.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC20-06 Tender publication](s-sc20-06-tender-publication.md)
