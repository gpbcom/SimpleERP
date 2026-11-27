🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🛍️ [SC02 Retail](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC02-06 Books, furniture, second-hand and franchise](README.md) ›
🖥️ S-SC02-19 Franchise network

# 🖥️ S-SC02-19 Franchise network

**Status:** ✅ specified

## Personas

- [U13 Owner](../../../../01-users/personas/u13-owner.md): every franchisee, agreement and statement.
- [U23 Store manager](../../../../01-users/personas/u23-store-manager.md): the statements to check and issue.

## Purpose

Run the network: candidates, agreements, rates, monthly statements and invoices.

## Entry points

Retail › Franchisees; the owner's workspace; the AI assistant.

## Wireframe

```text
+--------------------------------------------------------------------------------------------------+
| Franchisee: Boutique Lyon 3 SAS                       Active   [Save] [End agreement]            |
| Territory Lyon 3   Agreement 2025-03-01 to 2030-02-28   Rate 5 %   Fund 1 %                      |
| Disclosure sent 2025-01-20   Signed 2025-03-01 (after 40 days)                                   |
| Month     Sales        Royalty     Fund      State                                               |
| 2026-10   84,000.00    4,200.00    840.00    Invoiced                                            |
| 2026-11   estimated    4,100.00    820.00    Estimated          [Issue]                          |
+--------------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC02-06 step 4, U13 | desktop | ![FL-SC02-06 step 4, U13, light](../../images/06-books-furniture-second-hand-franchise/u13-owner/4-franchise-network-desktop-light.png) | ![FL-SC02-06 step 4, U13, dark](../../images/06-books-furniture-second-hand-franchise/u13-owner/4-franchise-network-desktop-dark.png) |
| FL-SC02-06 step 4, U13 | phone | ![FL-SC02-06 step 4, U13, light](../../images/06-books-furniture-second-hand-franchise/u13-owner/4-franchise-network-phone-light.png) | ![FL-SC02-06 step 4, U13, dark](../../images/06-books-furniture-second-hand-franchise/u13-owner/4-franchise-network-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc02-19-franchise-network-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc02-19-franchise-network-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc02-19-franchise-network-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc02-19-franchise-network-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc02-19-franchise-network-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc02-19-franchise-network-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc02-19-franchise-network-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc02-19-franchise-network-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Franchisee | E-SC02-16 company | link to the company | yes while Candidate | yes |
| Territory | E-SC02-16 territory | text | yes while Candidate | yes |
| Agreement dates | E-SC02-16 agreement dates | two dates | yes while Candidate | yes |
| Rates | E-SC02-16 royalty, fund | percentages | yes while Candidate | yes |
| Disclosure date | E-SC02-16 disclosure date | date | yes while Candidate | yes |
| Statements | E-SC02-16 statements | month, sales, amounts | no | no |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Send disclosure document | candidate | owner | the date is recorded |
| Sign agreement | candidate | owner | the franchisee becomes Active |
| Issue statement | statement row | store manager | the royalty invoice is created |
| End agreement | franchisee | owner | the franchisee is Ended after the last statement |

## States

- Normal: the franchisee with its territory, agreement, rates, disclosure and its monthly statements.
- Empty: No franchisee yet, with New franchisee.
- Loading: the headings and the table as placeholders; the values follow.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); a signature
  before the delay or incomplete sales, with the date or the missing days.
- Read-only: the record in a locked state: values shown, no action offered.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-SC02-16 Franchisee](../../data/e-sc02-16-franchisee.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC02-16 Franchisee | Candidate | Badge "Candidate"; a new record starts here; next: Active or Ended (BR-SC02-19, UC-SC02-19); fields editable within the role | U13, U23 | `u13-owner/s-sc02-19-franchise-network-e-sc02-16-franchisee-candidate-{desktop,phone}-{light,dark}.png`, `u23-store-manager/s-sc02-19-franchise-network-e-sc02-16-franchisee-candidate-{desktop,phone,tablet}-{light,dark}.png` |
| E-SC02-16 Franchisee | Active | Badge "Active"; next: Ended (UC-SC02-19); fields editable within the role | U13, U23 | `u13-owner/s-sc02-19-franchise-network-e-sc02-16-franchisee-active-{desktop,phone}-{light,dark}.png`, `u23-store-manager/s-sc02-19-franchise-network-e-sc02-16-franchisee-active-{desktop,phone,tablet}-{light,dark}.png` |
| E-SC02-16 Franchisee | Ended | Badge "Ended"; final: read-only, no next state; the history shows how it got here | U13, U23 | `u13-owner/s-sc02-19-franchise-network-e-sc02-16-franchisee-ended-{desktop,phone}-{light,dark}.png`, `u23-store-manager/s-sc02-19-franchise-network-e-sc02-16-franchisee-ended-{desktop,phone,tablet}-{light,dark}.png` |

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

- [FL-SC02-06](../../flows/fl-sc02-06-books-furniture-second-hand-franchise.md)

## Open questions

None.

---

⬅️ [S-SC02-18 Second-hand](s-sc02-18-second-hand.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC02-L01 Stores](../00-lists/s-sc02-l01-stores.md)
