🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
⚖️ [F15 Legal assistant](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F15-07 Equity, contracts, meetings and disputes](README.md) › 🖥️ S-F15-15 Contract drafting

# 🖥️ S-F15-15 Contract drafting

**Status:** ✅ specified

## Personas

- [U36 Professional](../../../../01-users/personas/u36-professional.md): their drafts and the library.
- [U13 Owner](../../../../01-users/personas/u13-owner.md): the clauses waiting for their approval.

## Purpose

Build a contract from approved clauses, see what departs from them and get it approved.

## Entry points

Administration › Contracts › New contract; the library under Clauses.

## Wireframe

```text
+---------------------------------------------------------------------------------------------+
| Contract: Service agreement, Atelier Verdier and Norte SL    Draft   [Ask approval] [Export] |
|---------------------------------------------------------------------------------------------|
| CLAUSE                 SOURCE        STATE               LAW CHECK                          |
| 1 Parties              Standard      Standard            OK                                 |
| 4 Payment terms        Variant 45 d  Standard            Within the late-payment limit      |
| 7 Liability            Edited        Non-standard        To approve                         |
| 9 Governing law        Standard      Standard            OK                                 |
| Non-standard: 1   Approved: 0   [Open clause] [Compare with the library]                    |
+---------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F15-07 step 4, U36 | desktop | ![FL-F15-07 step 4, U36, light](../../images/07-equity-contracts-and-disputes/u36-professional/4-contract-drafting-desktop-light.png) | ![FL-F15-07 step 4, U36, dark](../../images/07-equity-contracts-and-disputes/u36-professional/4-contract-drafting-desktop-dark.png) |
| FL-F15-07 step 4, U36 | phone | ![FL-F15-07 step 4, U36, light](../../images/07-equity-contracts-and-disputes/u36-professional/4-contract-drafting-phone-light.png) | ![FL-F15-07 step 4, U36, dark](../../images/07-equity-contracts-and-disputes/u36-professional/4-contract-drafting-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f15-15-contract-drafting-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f15-15-contract-drafting-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f15-15-contract-drafting-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f15-15-contract-drafting-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f15-15-contract-drafting-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f15-15-contract-drafting-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f15-15-contract-drafting-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f15-15-contract-drafting-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Contract kind and language | E-F15-06 kind, language | list | while Draft | yes |
| Clause | E-F15-18 title, text | text | within the draft | yes |
| Source | E-F15-18 source | standard, variant, edited, added | no | yes |
| State | E-F15-18 state | badge | by the approver | yes |
| Law check | E-F15-18 law check | text | no | no |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Add clause | header | professional | a clause of the library joins the draft |
| Edit clause | row | professional | the clause becomes non-standard |
| Ask approval | header | professional | sends the non-standard clauses to the approver |
| Approve | row | owner, lawyer | the clause is approved for this contract |
| Export | header | professional | the contract for signature, when nothing is waiting |

## States

- Normal: the draft's clauses with their source, state and law check.
- Empty: No clause in the draft, with Add a clause.
- Loading: the headings and the table as placeholders; the values follow.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); a refused
  export lists the clauses still waiting.
- Read-only: the record in a locked state: values shown, no action offered.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-F15-18 Clause](../../data/e-f15-18-clause.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F15-18 Clause | Draft | Badge "Draft"; a new record starts here; next: Pending (BR-F15-21); fields editable within the role | U36, U13 | `u36-professional/s-f15-15-contract-drafting-e-f15-18-clause-draft-{desktop,phone}-{light,dark}.png`, `u13-owner/s-f15-15-contract-drafting-e-f15-18-clause-draft-{desktop,phone}-{light,dark}.png` |
| E-F15-18 Clause | Pending | Badge "Pending"; next: Approved or Rejected (BR-F15-21); fields editable within the role | U36, U13 | `u36-professional/s-f15-15-contract-drafting-e-f15-18-clause-pending-{desktop,phone}-{light,dark}.png`, `u13-owner/s-f15-15-contract-drafting-e-f15-18-clause-pending-{desktop,phone}-{light,dark}.png` |
| E-F15-18 Clause | Approved | Badge "Approved"; next: Retired (UC-F15-17); fields editable within the role | U36, U13 | `u36-professional/s-f15-15-contract-drafting-e-f15-18-clause-approved-{desktop,phone}-{light,dark}.png`, `u13-owner/s-f15-15-contract-drafting-e-f15-18-clause-approved-{desktop,phone}-{light,dark}.png` |
| E-F15-18 Clause | Rejected | Badge "Rejected"; next: Draft (UC-F15-17); fields editable within the role | U36, U13 | `u36-professional/s-f15-15-contract-drafting-e-f15-18-clause-rejected-{desktop,phone}-{light,dark}.png`, `u13-owner/s-f15-15-contract-drafting-e-f15-18-clause-rejected-{desktop,phone}-{light,dark}.png` |
| E-F15-18 Clause | Retired | Badge "Retired"; final: read-only, no next state; the history shows how it got here | U36, U13 | `u36-professional/s-f15-15-contract-drafting-e-f15-18-clause-retired-{desktop,phone}-{light,dark}.png`, `u13-owner/s-f15-15-contract-drafting-e-f15-18-clause-retired-{desktop,phone}-{light,dark}.png` |

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

⬅️ [S-F15-14 Dilution](s-f15-14-dilution.md) · ⬆️ [Up](README.md) ·
➡️ [S-F15-16 Shareholder meetings](s-f15-16-shareholder-meetings.md)
