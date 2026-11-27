🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 💻 [SC14 IT and software](../../README.md) ›
🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-SC14-07 Hardware, licences, research tax credit and sponsorship](README.md) ›
🖥️ S-SC14-24 Research tax credit

# 🖥️ S-SC14-24 Research tax credit

**Status:** 🔄 waiting for the owner

## Personas

- [U13 Owner](../../../../01-users/personas/u13-owner.md): the projects, their description and the signature of the
  claim.
- [U05 Accounting](../../../../01-users/personas/u05-accounting.md): the expenses, the evidence file and the credit in
  the tax computation.

## Purpose

Define research projects, count the hours that the timesheets prove and prepare the expenses and the evidence file of
the year's tax credit.

## Entry points

IT and software › Research credit; a project's page; the year's closing checklist.

## Wireframe

```text
+--------------------------------------------------------------------------------------------------+
| Research credit: 2026                                            [New project] [Export evidence] |
| Project          Team  Hours claimed  Approved  Gap   Staff cost   Other     State               |
| Search engine    6     1,200          1,150     50    43,700.00    8,400.00  Tracked             |
| Offline sync     4     880            880       0     33,440.00    0.00      Evidenced           |
| Data model v2    3     410            410       0     15,580.00    2,100.00  Claimed             |
| Credit prepared: 2 projects, gap 50 hours                    [Cap at evidence] [Claim]           |
+--------------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC14-07 step 3, U13 | desktop | ![FL-SC14-07 step 3, U13, light](../../images/07-hardware-licences-and-tax-credits/u13-owner/3-research-tax-credit-desktop-light.png) | ![FL-SC14-07 step 3, U13, dark](../../images/07-hardware-licences-and-tax-credits/u13-owner/3-research-tax-credit-desktop-dark.png) |
| FL-SC14-07 step 3, U13 | phone | ![FL-SC14-07 step 3, U13, light](../../images/07-hardware-licences-and-tax-credits/u13-owner/3-research-tax-credit-phone-light.png) | ![FL-SC14-07 step 3, U13, dark](../../images/07-hardware-licences-and-tax-credits/u13-owner/3-research-tax-credit-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc14-24-research-tax-credit-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc14-24-research-tax-credit-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc14-24-research-tax-credit-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc14-24-research-tax-credit-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc14-24-research-tax-credit-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc14-24-research-tax-credit-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc14-24-research-tax-credit-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc14-24-research-tax-credit-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Project | E-SC14-19 project | link | no | yes |
| Uncertainty | E-SC14-19 uncertainty | text | yes while Defined | yes |
| Dates | E-SC14-19 start, end | dates | yes while Defined | yes |
| Hours claimed | E-SC14-19 hours claimed | number | yes while Tracked | yes |
| Hours approved | E-SC14-19 hours approved | number | no | no |
| Eligible expenses | E-SC14-19 expenses | amount in EUR | no | no |
| Evidence file | E-SC14-19 evidence file | file | no | yes to claim |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| New project | header | owner | a project in state Defined |
| Cap at evidence | project | accounting | the claimed hours are lowered to the approved hours |
| Export evidence | project | accounting | the file with the description, hours and expenses |
| Claim | header | owner | the projects are Claimed and added to the tax computation |

## States

- Normal: the projects with team, hours claimed and approved, gap, expenses and state.
- Empty: No research project yet, with New project.
- Loading: the headings and the table as placeholders; the values follow.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); hours without
  timesheet evidence, a project without its uncertainty, with the field to correct.
- Read-only: the record in a locked state: values shown, no action offered.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-SC14-19 R&D project](../../data/e-sc14-19-r-d-project.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC14-19 R&D project | Defined | Badge "Defined"; a new record starts here; next: Tracked (UC-SC14-24); fields editable within the role | U13, U05 | `u13-owner/s-sc14-24-research-tax-credit-e-sc14-19-r-d-project-defined-{desktop,phone}-{light,dark}.png`, `u05-accounting/s-sc14-24-research-tax-credit-e-sc14-19-r-d-project-defined-desktop-{light,dark}.png` |
| E-SC14-19 R&D project | Tracked | Badge "Tracked"; next: Evidenced (BR-SC14-18); fields editable within the role | U13, U05 | `u13-owner/s-sc14-24-research-tax-credit-e-sc14-19-r-d-project-tracked-{desktop,phone}-{light,dark}.png`, `u05-accounting/s-sc14-24-research-tax-credit-e-sc14-19-r-d-project-tracked-desktop-{light,dark}.png` |
| E-SC14-19 R&D project | Evidenced | Badge "Evidenced"; next: Claimed (UC-SC14-24); fields editable within the role | U13, U05 | `u13-owner/s-sc14-24-research-tax-credit-e-sc14-19-r-d-project-evidenced-{desktop,phone}-{light,dark}.png`, `u05-accounting/s-sc14-24-research-tax-credit-e-sc14-19-r-d-project-evidenced-desktop-{light,dark}.png` |
| E-SC14-19 R&D project | Claimed | Badge "Claimed"; next: Closed (UC-SC14-24); fields editable within the role | U13, U05 | `u13-owner/s-sc14-24-research-tax-credit-e-sc14-19-r-d-project-claimed-{desktop,phone}-{light,dark}.png`, `u05-accounting/s-sc14-24-research-tax-credit-e-sc14-19-r-d-project-claimed-desktop-{light,dark}.png` |
| E-SC14-19 R&D project | Closed | Badge "Closed"; final: read-only, no next state; the history shows how it got here | U13, U05 | `u13-owner/s-sc14-24-research-tax-credit-e-sc14-19-r-d-project-closed-{desktop,phone}-{light,dark}.png`, `u05-accounting/s-sc14-24-research-tax-credit-e-sc14-19-r-d-project-closed-desktop-{light,dark}.png` |

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

- [FL-SC14-07](../../flows/fl-sc14-07-hardware-licences-and-tax-credits.md)

## Open questions

None.

---

⬅️ [S-SC14-23 Licence reselling](s-sc14-23-licence-reselling.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC14-25 Sponsorship](s-sc14-25-sponsorship.md)
