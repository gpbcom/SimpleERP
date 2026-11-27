🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
⚖️ [F15 Legal assistant](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F15-07 Equity, contracts, meetings and disputes](README.md) › 🖥️ S-F15-12 Cap table

# 🖥️ S-F15-12 Cap table

**Status:** ✅ specified

## Personas

- [U13 Owner](../../../../01-users/personas/u13-owner.md): the register, every movement and every holder.
- [U50 Shareholder](../../../../01-users/personas/u50-shareholder.md): their own holding and history, from a phone.

## Purpose

See who holds what, record a movement, collect the signatures and write the register entry.

## Entry points

Administration › Company records › Cap table; the shareholder's portal.

## Wireframe

```text
+---------------------------------------------------------------------------------------------+
| Cap table: Atelier Verdier SAS                         Capital 100,000   10,000 shares      |
|---------------------------------------------------------------------------------------------|
| HOLDER           CLASS     SHARES   % CAPITAL  % VOTES   SINCE        LAST ENTRY             |
| Anne Verdier     Ordinary  6,000    60.0       60.0      2018-03-02   2026-009               |
| Marc Leroy       Ordinary  2,200    22.0       22.0      2026-11-10   2026-014 (pending)     |
| Investor fund    Ordinary  1,800    18.0       18.0      2024-06-15   2024-004               |
| [New movement] [Statement] [Register] [Export]                                              |
+---------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F15-07 step 1, U13 | desktop | ![FL-F15-07 step 1, U13, light](../../images/07-equity-contracts-and-disputes/u13-owner/1-cap-table-desktop-light.png) | ![FL-F15-07 step 1, U13, dark](../../images/07-equity-contracts-and-disputes/u13-owner/1-cap-table-desktop-dark.png) |
| FL-F15-07 step 1, U13 | phone | ![FL-F15-07 step 1, U13, light](../../images/07-equity-contracts-and-disputes/u13-owner/1-cap-table-phone-light.png) | ![FL-F15-07 step 1, U13, dark](../../images/07-equity-contracts-and-disputes/u13-owner/1-cap-table-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f15-12-cap-table-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f15-12-cap-table-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f15-12-cap-table-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f15-12-cap-table-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f15-12-cap-table-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f15-12-cap-table-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f15-12-cap-table-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f15-12-cap-table-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Holder | E-F15-15 holder | name | no | yes |
| Class and shares | E-F15-15 class, quantity | text and number | by a movement | yes |
| Percentage of capital and votes | E-F15-15 computed | two percentages | no | yes |
| Since | E-F15-15 registered on | date | no | no |
| Last entry | E-F15-15 entry number | text | no | yes |
| Movement | E-F15-15 movement | issue, transfer, cancellation | while Proposed | yes |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| New movement | header | owner | a line of the register is proposed |
| Sign | phone | shareholder | the holder signs their transfer |
| Register | row | owner | writes the entry and updates the table |
| Statement | row | owner, shareholder | a dated statement of the holding |
| Cancel | row | owner | cancels a Proposed or Approved line |

## States

- Normal: the holders, classes, shares and percentages, with pending movements marked.
- Empty: No share issued yet, with Record the first issue.
- Loading: the headings and the table as placeholders; the values follow.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); a refused
  movement shows the missing decision or the signature.
- Read-only: the record in a locked state: values shown, no action offered.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-F15-15 Shareholding](../../data/e-f15-15-shareholding.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F15-15 Shareholding | Proposed | Badge "Proposed"; a new record starts here; next: Approved or Cancelled (UC-F15-14); fields editable within the role | U13, U50 | `u13-owner/s-f15-12-cap-table-e-f15-15-shareholding-proposed-{desktop,phone}-{light,dark}.png`, `u50-shareholder/s-f15-12-cap-table-e-f15-15-shareholding-proposed-{desktop,phone}-{light,dark}.png` |
| E-F15-15 Shareholding | Approved | Badge "Approved"; next: Registered or Cancelled (BR-F15-18, UC-F15-14); fields editable within the role | U13, U50 | `u13-owner/s-f15-12-cap-table-e-f15-15-shareholding-approved-{desktop,phone}-{light,dark}.png`, `u50-shareholder/s-f15-12-cap-table-e-f15-15-shareholding-approved-{desktop,phone}-{light,dark}.png` |
| E-F15-15 Shareholding | Registered | Badge "Registered"; final: read-only, no next state; the history shows how it got here | U13, U50 | `u13-owner/s-f15-12-cap-table-e-f15-15-shareholding-registered-{desktop,phone}-{light,dark}.png`, `u50-shareholder/s-f15-12-cap-table-e-f15-15-shareholding-registered-{desktop,phone}-{light,dark}.png` |
| E-F15-15 Shareholding | Cancelled | Badge "Cancelled"; final: read-only, no next state; the history shows how it got here | U13, U50 | `u13-owner/s-f15-12-cap-table-e-f15-15-shareholding-cancelled-{desktop,phone}-{light,dark}.png`, `u50-shareholder/s-f15-12-cap-table-e-f15-15-shareholding-cancelled-{desktop,phone}-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

The owner's table is desktop only. The shareholder opens their holding on a phone: shares, percentage, history and the
transfers to sign.

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

⬅️ [S-F15-11 Lawyer hand-off](../01-ask-a-legal-question/s-f15-11-lawyer-hand-off.md) · ⬆️ [Up](README.md) ·
➡️ [S-F15-13 Employee equity](s-f15-13-employee-equity.md)
