🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) ›
🔧 [SC19 Trades and home services](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-SC19-04 Installations and labels](README.md) › 🖥️ S-SC19-15 RGE evidence

# 🖥️ S-SC19-15 RGE evidence

**Status:** 🔄 waiting for the owner

## Personas

- [U13 Owner](../../../../01-users/personas/u13-owner.md): the labels with their scopes, validity, people and audit
  dates.

## Purpose

Keep the evidence of the company's environmental label and plan its audits before expiry.

## Entry points

Trades and home services › Labels; the reminder of an audit; a quote that checks the label.

## Wireframe

```text
+--------------------------------------------------------------------------------------------------+
| Labels                                                              [Add a label]                |
| Label     Body        Number     Scopes                   Valid until   Next audit  State        |
| Env-Heat  Body A      H-42817    Heat pump, boiler        30 Jun 2028   30 Apr 2028 Active       |
| Env-Solar Body B      S-10244    Solar panels             15 Feb 2027   15 Dec 2026 Audit due    |
| People: Leroy (heat pump), Petit (boiler)                          [Change people]               |
+--------------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC19-04 step 3, U13 | desktop | ![FL-SC19-04 step 3, U13, light](../../images/04-installations-and-labels/u13-owner/3-rge-evidence-desktop-light.png) | ![FL-SC19-04 step 3, U13, dark](../../images/04-installations-and-labels/u13-owner/3-rge-evidence-desktop-dark.png) |
| FL-SC19-04 step 3, U13 | phone | ![FL-SC19-04 step 3, U13, light](../../images/04-installations-and-labels/u13-owner/3-rge-evidence-phone-light.png) | ![FL-SC19-04 step 3, U13, dark](../../images/04-installations-and-labels/u13-owner/3-rge-evidence-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc19-15-rge-evidence-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc19-15-rge-evidence-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc19-15-rge-evidence-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc19-15-rge-evidence-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc19-15-rge-evidence-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc19-15-rge-evidence-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc19-15-rge-evidence-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc19-15-rge-evidence-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Label | E-SC19-09 name | text | yes | yes |
| Body and number | E-SC19-09 body | text | yes | yes |
| Scopes | E-SC19-09 scopes | list from the pack | yes | yes |
| Qualified people | E-SC19-09 people | users with a qualification | yes | yes |
| Valid until | E-SC19-09 valid until | date | yes | yes |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Add a label | header | owner | a label is created with its evidence |
| Record audit | row | owner | the new validity is saved |
| Change people | row | owner | the qualified people of a scope are changed |

## States

- Normal: the labels with body, number, scopes, validity, audit date and state.
- Empty: No label yet, with Add a label.
- Loading: the headings and the table as placeholders; the values follow.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); a missing
  validity, a scope without a person, with the label named.
- Read-only: the record in a locked state: values shown, no action offered.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-SC19-09 Label](../../data/e-sc19-09-label.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC19-09 Label | Active | Badge "Active"; a new record starts here; next: Audit due or Expired (BR-SC19-15, UC-SC19-15); fields editable within the role | U13 | `u13-owner/s-sc19-15-rge-evidence-e-sc19-09-label-active-{desktop,phone}-{light,dark}.png` |
| E-SC19-09 Label | Audit due | Badge "Audit due"; next: Active or Expired (BR-SC19-15, UC-SC19-15); fields editable within the role | U13 | `u13-owner/s-sc19-15-rge-evidence-e-sc19-09-label-audit-due-{desktop,phone}-{light,dark}.png` |
| E-SC19-09 Label | Expired | Badge "Expired"; next: Active (UC-SC19-15); fields editable within the role | U13 | `u13-owner/s-sc19-15-rge-evidence-e-sc19-09-label-expired-{desktop,phone}-{light,dark}.png` |

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

- [FL-SC19-04 Installations and labels](../../flows/fl-sc19-04-installations-and-labels.md)

## Open questions

None.

---

⬅️ [S-SC19-14 Installation grants](s-sc19-14-installation-grants.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC19-16 Regulated records](s-sc19-16-regulated-records.md)
