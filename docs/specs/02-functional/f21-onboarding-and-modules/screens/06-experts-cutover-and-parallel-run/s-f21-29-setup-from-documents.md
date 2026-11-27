🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🧭 [F21 Onboarding and module activation](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F21-06 Experts, cutover, parallel run and set-up from documents](README.md) ›
🖥️ S-F21-29 Set up from documents

# 🖥️ S-F21-29 Set up from documents

**Status:** ✅ specified

## Personas

- [U13 Owner](../../../../01-users/personas/u13-owner.md): the documents, the proposals and their choices.

## Purpose

Propose the company's settings from last year's documents, and apply only what the owner confirms.

## Entry points

Onboarding and module activation › Set up from my documents; the first-run guide's choice at the start.

## Wireframe

```text
+---------------------------------------------------------------------------------------------+
| Set up from documents      3 documents read      14 proposals      Confirmed 11              |
|---------------------------------------------------------------------------------------------|
| SETTING          PROPOSED VALUE      SOURCE                            SURE    YOUR CHOICE    |
| Financial year   1 July - 30 June    Accounts 2025, page 2             High    [Accept][Edit] |
| VAT regime       Real, monthly       Invoice 2026-0412, footer         High    [Accept][Edit] |
| Payment terms    30 days             Invoices, 5 of 5                  High    [Accept][Edit] |
| Main customer    Atelier Nord        Accounts 2025, page 7             Medium  [Accept][Reject] |
| [Apply the confirmed lines]     Documents: delete after the set-up [x]                        |
+---------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F21-06 step 4, U13 | desktop | ![FL-F21-06 step 4, U13, light](../../images/06-experts-cutover-and-parallel-run/u13-owner/4-setup-from-documents-desktop-light.png) | ![FL-F21-06 step 4, U13, dark](../../images/06-experts-cutover-and-parallel-run/u13-owner/4-setup-from-documents-desktop-dark.png) |
| FL-F21-06 step 4, U13 | phone | ![FL-F21-06 step 4, U13, light](../../images/06-experts-cutover-and-parallel-run/u13-owner/4-setup-from-documents-phone-light.png) | ![FL-F21-06 step 4, U13, dark](../../images/06-experts-cutover-and-parallel-run/u13-owner/4-setup-from-documents-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f21-29-setup-from-documents-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f21-29-setup-from-documents-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f21-29-setup-from-documents-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f21-29-setup-from-documents-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f21-29-setup-from-documents-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f21-29-setup-from-documents-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f21-29-setup-from-documents-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f21-29-setup-from-documents-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Documents | uploaded files | file and kind | by the owner | yes |
| Setting | proposal setting | text | no | yes |
| Proposed value | proposal value | text | by the owner on Edit | yes |
| Source | document and passage | text and page | no | yes |
| How sure | proposal confidence | high, medium, low | no | yes |
| Choice | owner's decision | accept, edit, reject | by the owner | yes |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Upload | header | owner | adds a document to read |
| Accept, edit or reject | row | owner | decides a proposal |
| Apply the confirmed lines | footer | owner | applies only the accepted and edited lines |
| Delete the documents | footer | owner | removes the files after the set-up |

## States

- Normal: the documents read and the proposals with their sources, confidence and choices.
- Empty: No document yet, with Upload.
- Loading: the headings and the table as placeholders; the values follow.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); an unreadable
  document is listed as not read, with why.
- Read-only: the record in a locked state: values shown, no action offered.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): none; no flow's Entities and screens table names an entity on this screen.

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

- [FL-F21-06](../../flows/fl-f21-06-experts-cutover-and-parallel-run.md)

## Open questions

None.

---

⬅️ [S-F21-28 Parallel run](s-f21-28-parallel-run.md) · ⬆️ [Up](README.md) ·
➡️ [S-F21-L01 Onboarding progresses](../00-lists/s-f21-l01-onboarding-progresses.md)
