🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
⚖️ [F15 Legal assistant](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F15-07 Equity, contracts, meetings and disputes](README.md) › 🖥️ S-F15-18 Litigation

# 🖥️ S-F15-18 Litigation

**Status:** ✅ specified

## Personas

- [U36 Professional](../../../../01-users/personas/u36-professional.md): every dispute and its facts.
- [U05 Accounting](../../../../01-users/personas/u05-accounting.md): the risk and the estimate of each, and the
  provision proposals.

## Purpose

Keep each dispute with its hearings and risk, and send a probable loss to accounting.

## Entry points

Administration › Company records › Litigation; the compliance calendar.

## Wireframe

```text
+---------------------------------------------------------------------------------------------+
| Litigation                              Open 3   Probable 1   Provision proposed 30,000   [+ Add] |
|---------------------------------------------------------------------------------------------|
| COUNTERPARTY   COURT              CLAIMED   RISK       ESTIMATE  PROVISION   STATE          |
| Supplier Roth  Commercial court   48,000    Probable   30,000    Proposed    Proceedings    |
| Former client  Labour court       9,000     Possible   -         -           Open           |
| Next hearing: 2026-12-02 Commercial court                                                   |
| [Assess risk] [Propose provision] [Documents] [Hearings]                                    |
+---------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F15-07 step 7, U36 | desktop | ![FL-F15-07 step 7, U36, light](../../images/07-equity-contracts-and-disputes/u36-professional/7-litigation-desktop-light.png) | ![FL-F15-07 step 7, U36, dark](../../images/07-equity-contracts-and-disputes/u36-professional/7-litigation-desktop-dark.png) |
| FL-F15-07 step 7, U36 | phone | ![FL-F15-07 step 7, U36, light](../../images/07-equity-contracts-and-disputes/u36-professional/7-litigation-phone-light.png) | ![FL-F15-07 step 7, U36, dark](../../images/07-equity-contracts-and-disputes/u36-professional/7-litigation-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f15-18-litigation-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f15-18-litigation-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f15-18-litigation-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f15-18-litigation-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f15-18-litigation-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f15-18-litigation-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f15-18-litigation-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f15-18-litigation-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Counterparty and subject | E-F15-21 counterparty, subject | text | yes | yes |
| Court and lawyer | E-F15-21 court, lawyer | text | yes | no |
| Amount claimed | E-F15-21 claimed | amount | yes | yes |
| Risk and estimate | E-F15-21 risk, estimate | badge and amount | yes | yes |
| Provision | E-F15-21 provision | amount and badge | no | no |
| Hearings | E-F15-21 hearings | list of dates | yes | no |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Add dispute | header | professional | a dispute is created |
| Assess risk | row | professional, lawyer | sets the risk and its reason |
| Propose provision | row | professional | sends the estimate to accounting |
| Close | row | professional | the case ends with its outcome |

## States

- Normal: the disputes with risk, estimate, provision and next hearing.
- Empty: No dispute, with Add a dispute.
- Loading: the headings and the table as placeholders; the values follow.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); a refused
  proposal shows the missing estimate.
- Read-only: the record in a locked state: values shown, no action offered.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-F15-21 Dispute](../../data/e-f15-21-dispute.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F15-21 Dispute | Open | Badge "Open"; a new record starts here; next: Proceedings or Settled (UC-F15-20); fields editable within the role | U36, U05 | `u36-professional/s-f15-18-litigation-e-f15-21-dispute-open-{desktop,phone}-{light,dark}.png`, `u05-accounting/s-f15-18-litigation-e-f15-21-dispute-open-desktop-{light,dark}.png` |
| E-F15-21 Dispute | Proceedings | Badge "Proceedings"; next: Judged or Settled (UC-F15-20); fields editable within the role | U36, U05 | `u36-professional/s-f15-18-litigation-e-f15-21-dispute-proceedings-{desktop,phone}-{light,dark}.png`, `u05-accounting/s-f15-18-litigation-e-f15-21-dispute-proceedings-desktop-{light,dark}.png` |
| E-F15-21 Dispute | Settled | Badge "Settled"; next: Closed (UC-F15-20); fields editable within the role | U36, U05 | `u36-professional/s-f15-18-litigation-e-f15-21-dispute-settled-{desktop,phone}-{light,dark}.png`, `u05-accounting/s-f15-18-litigation-e-f15-21-dispute-settled-desktop-{light,dark}.png` |
| E-F15-21 Dispute | Judged | Badge "Judged"; next: Proceedings or Closed (UC-F15-20); fields editable within the role | U36, U05 | `u36-professional/s-f15-18-litigation-e-f15-21-dispute-judged-{desktop,phone}-{light,dark}.png`, `u05-accounting/s-f15-18-litigation-e-f15-21-dispute-judged-desktop-{light,dark}.png` |
| E-F15-21 Dispute | Closed | Badge "Closed"; final: read-only, no next state; the history shows how it got here | U36, U05 | `u36-professional/s-f15-18-litigation-e-f15-21-dispute-closed-{desktop,phone}-{light,dark}.png`, `u05-accounting/s-f15-18-litigation-e-f15-21-dispute-closed-desktop-{light,dark}.png` |

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

- [FL-F15-07](../../flows/fl-f15-07-equity-contracts-and-disputes.md)

## Open questions

None.

---

⬅️ [S-F15-17 IP portfolio](s-f15-17-ip-portfolio.md) · ⬆️ [Up](README.md) ·
➡️ [S-F15-L01 Law packs](../00-lists/s-f15-l01-law-packs.md)
