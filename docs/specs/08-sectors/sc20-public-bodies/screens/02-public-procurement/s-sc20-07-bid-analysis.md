🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🏛️ [SC20 Public bodies](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC20-02 Public procurement](README.md) › 🖥️ S-SC20-07 Bid analysis

# 🖥️ S-SC20-07 Bid analysis

**Status:** ✅ specified

## Personas

- [U54 Public finance officer](../../../../01-users/personas/u54-public-finance-officer.md): the bids with admission,
  scores and rank.
- [U55 Elected official](../../../../01-users/personas/u55-elected-official.md): the ranking to review and the award to
  approve.

## Purpose

Analyse the bids against the published criteria, rank them and approve the award.

## Entry points

Public bodies › Tender files › Bids; the deadline passed reminder.

## Wireframe

```text
+--------------------------------------------------------------------------------------------------+
| Bids: AO-2027-014                                    Deadline 12 May 12:00   [Score] [Award]     |
| Bidder             Received          Price   Quality   Env.   Total   State                      |
| Cantine Plus       11 May 16:20      45      38        9      92      Admitted                   |
| Repas Val          12 May 11:58      50      30        8      88      Admitted                   |
| Menu Express       12 May 12:04      -       -         -      -       Late                       |
| Awarded to: -                                          [Approve award]                           |
+--------------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC20-02 step 3, U54 | desktop | ![FL-SC20-02 step 3, U54, light](../../images/02-public-procurement/u54-public-finance-officer/3-bid-analysis-desktop-light.png) | ![FL-SC20-02 step 3, U54, dark](../../images/02-public-procurement/u54-public-finance-officer/3-bid-analysis-desktop-dark.png) |
| Error E1, U54 | desktop | ![Error E1, U54, light](../../images/02-public-procurement/u54-public-finance-officer/e1-a-bid-is-late-desktop-light.png) | ![Error E1, U54, dark](../../images/02-public-procurement/u54-public-finance-officer/e1-a-bid-is-late-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc20-07-bid-analysis-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc20-07-bid-analysis-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc20-07-bid-analysis-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc20-07-bid-analysis-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc20-07-bid-analysis-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc20-07-bid-analysis-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-sc20-07-bid-analysis-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-sc20-07-bid-analysis-offline-desktop-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Bidder | E-SC20-06 bidder | link | no | yes |
| Received | E-SC20-06 received | date and time | no | yes |
| Scores | E-SC20-06 scores | list of criterion and score | yes while Admitted | yes |
| Total | E-SC20-06 total | number | no | no |
| Admission | E-SC20-06 admission | admitted, rejected with reason | yes | yes |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Admit or reject | row | public finance officer | the admission of a bid is decided |
| Score | row | public finance officer | the scores are saved and the ranking computed |
| Approve award | header | elected official | the award is recorded and bidders are told |

## States

- Normal: the bids with received time, scores, total, admission and state.
- Empty: No bid received.
- Loading: the headings and the table as placeholders; the values follow.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); a late bid
  opened, a criterion not scored, with the bid named.
- Read-only: the record in a locked state: values shown, no action offered.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-SC20-06 Bid](../../data/e-sc20-06-bid.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC20-06 Bid | Received | Badge "Received"; a new record starts here; next: Admitted or Rejected (UC-SC20-07); fields editable within the role | U54, U55 | `u54-public-finance-officer/s-sc20-07-bid-analysis-e-sc20-06-bid-received-desktop-{light,dark}.png`, `u55-elected-official/s-sc20-07-bid-analysis-e-sc20-06-bid-received-desktop-{light,dark}.png` |
| E-SC20-06 Bid | Late | Badge "Late"; a new record starts here; no other state; fields editable within the role | U54, U55 | `u54-public-finance-officer/s-sc20-07-bid-analysis-e-sc20-06-bid-late-desktop-{light,dark}.png`, `u55-elected-official/s-sc20-07-bid-analysis-e-sc20-06-bid-late-desktop-{light,dark}.png` |
| E-SC20-06 Bid | Admitted | Badge "Admitted"; next: Awarded or Not selected (BR-SC20-07); fields editable within the role | U54, U55 | `u54-public-finance-officer/s-sc20-07-bid-analysis-e-sc20-06-bid-admitted-desktop-{light,dark}.png`, `u55-elected-official/s-sc20-07-bid-analysis-e-sc20-06-bid-admitted-desktop-{light,dark}.png` |
| E-SC20-06 Bid | Rejected | Badge "Rejected"; final: read-only, no next state; the history shows how it got here | U54, U55 | `u54-public-finance-officer/s-sc20-07-bid-analysis-e-sc20-06-bid-rejected-desktop-{light,dark}.png`, `u55-elected-official/s-sc20-07-bid-analysis-e-sc20-06-bid-rejected-desktop-{light,dark}.png` |
| E-SC20-06 Bid | Awarded | Badge "Awarded"; final: read-only, no next state; the history shows how it got here | U54, U55 | `u54-public-finance-officer/s-sc20-07-bid-analysis-e-sc20-06-bid-awarded-desktop-{light,dark}.png`, `u55-elected-official/s-sc20-07-bid-analysis-e-sc20-06-bid-awarded-desktop-{light,dark}.png` |
| E-SC20-06 Bid | Not selected | Badge "Not selected"; final: read-only, no next state; the history shows how it got here | U54, U55 | `u54-public-finance-officer/s-sc20-07-bid-analysis-e-sc20-06-bid-not-selected-desktop-{light,dark}.png`, `u55-elected-official/s-sc20-07-bid-analysis-e-sc20-06-bid-not-selected-desktop-{light,dark}.png` |

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

⬅️ [S-SC20-06 Tender publication](s-sc20-06-tender-publication.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC20-08 Public contract](s-sc20-08-public-contract.md)
