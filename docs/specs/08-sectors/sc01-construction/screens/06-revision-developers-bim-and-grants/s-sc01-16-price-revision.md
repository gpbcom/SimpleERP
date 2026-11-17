🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🏗️ [SC01 Construction](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC01-06 Price revision, off-plan sales, BIM and grants](README.md) ›
🖥️ S-SC01-16 Price revision

# 🖥️ S-SC01-16 Price revision

**Status:** 🔄 waiting for the owner

## Personas

- [U22 Site manager](../../../../01-users/personas/u22-site-manager.md): the formula of each site and its revisions.
- [U05 Accounting](../../../../01-users/personas/u05-accounting.md): the bills to revise and to correct.

## Purpose

Enter the formula of a contract, see the revision of each progress bill and correct provisional revisions when the index
is published.

## Entry points

Construction › Revision formulas; the site's Bills tab; the reminder of a provisional revision.

## Wireframe

```text
+--------------------------------------------------------------------------------------------------+
| Formula: Site S-14, BT01                                          Active   [Save] [Close]        |
| Base month  2025-10   Base index 130.4   Fixed part 15 %   Weight 85 %   Cap  +8 %               |
| Bill        Month     Index    Provisional  Unrevised    Revision   Revised                      |
| Bill 3      2026-03   134.2    no           40,000.00    +990.80    40,990.80                    |
| Bill 4      2026-04   134.2    yes          38,500.00    +948.45    39,448.45                    |
| Next index due 2026-05-12                       [Correct provisional bills]                      |
+--------------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC01-06 step 1, U22 | desktop | ![FL-SC01-06 step 1, U22, light](../../images/06-revision-developers-bim-and-grants/u22-site-manager/1-price-revision-desktop-light.png) | ![FL-SC01-06 step 1, U22, dark](../../images/06-revision-developers-bim-and-grants/u22-site-manager/1-price-revision-desktop-dark.png) |
| FL-SC01-06 step 1, U22 | phone | ![FL-SC01-06 step 1, U22, light](../../images/06-revision-developers-bim-and-grants/u22-site-manager/1-price-revision-phone-light.png) | ![FL-SC01-06 step 1, U22, dark](../../images/06-revision-developers-bim-and-grants/u22-site-manager/1-price-revision-phone-dark.png) |
| FL-SC01-06 step 1, U22 | tablet | ![FL-SC01-06 step 1, U22, light](../../images/06-revision-developers-bim-and-grants/u22-site-manager/1-price-revision-tablet-light.png) | ![FL-SC01-06 step 1, U22, dark](../../images/06-revision-developers-bim-and-grants/u22-site-manager/1-price-revision-tablet-dark.png) |
| Error E1, U22 | desktop | ![Error E1, U22, light](../../images/06-revision-developers-bim-and-grants/u22-site-manager/e1-the-index-is-not-published-desktop-light.png) | ![Error E1, U22, dark](../../images/06-revision-developers-bim-and-grants/u22-site-manager/e1-the-index-is-not-published-desktop-dark.png) |
| Error E1, U22 | phone | ![Error E1, U22, light](../../images/06-revision-developers-bim-and-grants/u22-site-manager/e1-the-index-is-not-published-phone-light.png) | ![Error E1, U22, dark](../../images/06-revision-developers-bim-and-grants/u22-site-manager/e1-the-index-is-not-published-phone-dark.png) |
| Error E1, U22 | tablet | ![Error E1, U22, light](../../images/06-revision-developers-bim-and-grants/u22-site-manager/e1-the-index-is-not-published-tablet-light.png) | ![Error E1, U22, dark](../../images/06-revision-developers-bim-and-grants/u22-site-manager/e1-the-index-is-not-published-tablet-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc01-16-price-revision-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc01-16-price-revision-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc01-16-price-revision-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc01-16-price-revision-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc01-16-price-revision-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc01-16-price-revision-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc01-16-price-revision-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc01-16-price-revision-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Site and contract | E-SC01-15 site | link | no | yes |
| Index series | E-SC01-15 index series | BT or TP series code | yes while Draft | yes |
| Base month and index | E-SC01-15 base month, base index | month and number | yes while Draft | yes |
| Fixed part and weights | E-SC01-15 weights | percentages adding to 100 | yes while Draft | yes |
| Cap or floor | E-SC01-15 cap | percentage | yes while Draft | no |
| Bills revised | E-SC01-15 bills revised | number | no | no |
| Provisional bills | E-SC01-15 provisional bills | number | no | no |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Confirm formula | header | accounting | the formula becomes Active |
| Correct provisional bills | bills table | accounting | a correction line per bill, to check before it is issued |
| Enter an index by hand | index line | accounting | a value with its source, used until the country pack has it |
| Close | header | accounting | the formula is Closed after the last revision |

## States

- Normal: the formula, its weights and each progress bill with its index, month and revision.
- Empty: No formula yet, with New formula.
- Loading: the headings and the table as placeholders; the values follow.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); a missing index
  series or a bill month before the base month, with the field to correct.
- Read-only: the record in a locked state: values shown, no action offered.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-SC01-15 Revision formula](../../data/e-sc01-15-revision-formula.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC01-15 Revision formula | Draft | Badge "Draft"; a new record starts here; next: Active (BR-SC01-16); fields editable within the role | U22, U05 | `u22-site-manager/s-sc01-16-price-revision-e-sc01-15-revision-formula-draft-{desktop,phone,tablet}-{light,dark}.png`, `u05-accounting/s-sc01-16-price-revision-e-sc01-15-revision-formula-draft-desktop-{light,dark}.png` |
| E-SC01-15 Revision formula | Active | Badge "Active"; next: Closed (UC-SC01-16); fields editable within the role | U22, U05 | `u22-site-manager/s-sc01-16-price-revision-e-sc01-15-revision-formula-active-{desktop,phone,tablet}-{light,dark}.png`, `u05-accounting/s-sc01-16-price-revision-e-sc01-15-revision-formula-active-desktop-{light,dark}.png` |
| E-SC01-15 Revision formula | Closed | Badge "Closed"; final: read-only, no next state; the history shows how it got here | U22, U05 | `u22-site-manager/s-sc01-16-price-revision-e-sc01-15-revision-formula-closed-{desktop,phone,tablet}-{light,dark}.png`, `u05-accounting/s-sc01-16-price-revision-e-sc01-15-revision-formula-closed-desktop-{light,dark}.png` |

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

- [FL-SC01-06](../../flows/fl-sc01-06-revision-developers-bim-and-grants.md)

## Open questions

None.

---

⬅️ [S-SC01-15 Site assistant](../03-run-the-site/s-sc01-15-site-assistant.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC01-17 Off-plan sales](s-sc01-17-off-plan-sales.md)
