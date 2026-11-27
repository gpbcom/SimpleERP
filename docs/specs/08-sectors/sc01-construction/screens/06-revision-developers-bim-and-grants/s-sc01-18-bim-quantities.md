🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🏗️ [SC01 Construction](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC01-06 Price revision, off-plan sales, BIM and grants](README.md) ›
🖥️ S-SC01-18 BIM quantities

# 🖥️ S-SC01-18 BIM quantities

**Status:** ✅ specified

## Personas

- [U22 Site manager](../../../../01-users/personas/u22-site-manager.md): the imports of their quotes and sites.

## Purpose

Import a model, map its groups to quote lots and review the quantities that change between versions.

## Entry points

Construction › BIM imports; the quote's lots tab; the AI assistant (upload a model).

## Wireframe

```text
+--------------------------------------------------------------------------------------------------+
| Import: Residence Les Tilleuls, version 4                          Compared   [Accept all] [Revi |
| Group             Lot            Unit   Version 3   Version 4   Change                           |
| Slab, floors 1-4  03.01 Slabs     m2     412.6       428.1       +15.5                           |
| Walls, outer      04.02 Walls     m      318.0       318.0       0                               |
| Doors             08.01 Doors     each   64          62          -2                              |
| Unmapped elements 5   [Map]            Lines to review 3                                         |
+--------------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC01-06 step 3, U22 | desktop | ![FL-SC01-06 step 3, U22, light](../../images/06-revision-developers-bim-and-grants/u22-site-manager/3-bim-quantities-desktop-light.png) | ![FL-SC01-06 step 3, U22, dark](../../images/06-revision-developers-bim-and-grants/u22-site-manager/3-bim-quantities-desktop-dark.png) |
| FL-SC01-06 step 3, U22 | phone | ![FL-SC01-06 step 3, U22, light](../../images/06-revision-developers-bim-and-grants/u22-site-manager/3-bim-quantities-phone-light.png) | ![FL-SC01-06 step 3, U22, dark](../../images/06-revision-developers-bim-and-grants/u22-site-manager/3-bim-quantities-phone-dark.png) |
| FL-SC01-06 step 3, U22 | tablet | ![FL-SC01-06 step 3, U22, light](../../images/06-revision-developers-bim-and-grants/u22-site-manager/3-bim-quantities-tablet-light.png) | ![FL-SC01-06 step 3, U22, dark](../../images/06-revision-developers-bim-and-grants/u22-site-manager/3-bim-quantities-tablet-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc01-18-bim-quantities-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc01-18-bim-quantities-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc01-18-bim-quantities-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc01-18-bim-quantities-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc01-18-bim-quantities-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc01-18-bim-quantities-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc01-18-bim-quantities-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc01-18-bim-quantities-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Model file | E-SC01-17 file | file name | no | yes |
| Version | E-SC01-17 version | text | yes while Draft | yes |
| Quote | E-SC01-17 quote | link | yes while Draft | yes |
| Groups and mapping | E-SC01-17 groups | group, lot, unit | yes while Mapped | no |
| Quantities | E-SC01-17 quantities | numbers | no | no |
| Changes | E-SC01-17 changes | old, new, difference | no | no |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Upload | header | site manager | a new import in Draft |
| Map | group row | site manager | the group is linked to a lot and a unit |
| Accept changes | header | site manager | the quantities enter the lots, lines are flagged |
| Refuse changes | change row | site manager | the version in use stays |

## States

- Normal: the groups with their lot, unit and quantities for the version in use and the version compared.
- Empty: No import yet, with Upload a model.
- Loading: the headings and the table as placeholders; the values follow.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); an unreadable
  file or a missing measure, with the group concerned.
- Read-only: the record in a locked state: values shown, no action offered.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-SC01-17 BIM import](../../data/e-sc01-17-bim-import.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC01-17 BIM import | Draft | Badge "Draft"; a new record starts here; next: Mapped (UC-SC01-18); fields editable within the role | U22 | `u22-site-manager/s-sc01-18-bim-quantities-e-sc01-17-bim-import-draft-{desktop,phone,tablet}-{light,dark}.png` |
| E-SC01-17 BIM import | Mapped | Badge "Mapped"; next: Applied (BR-SC01-18); fields editable within the role | U22 | `u22-site-manager/s-sc01-18-bim-quantities-e-sc01-17-bim-import-mapped-{desktop,phone,tablet}-{light,dark}.png` |
| E-SC01-17 BIM import | Applied | Badge "Applied"; next: Superseded (UC-SC01-18); fields editable within the role | U22 | `u22-site-manager/s-sc01-18-bim-quantities-e-sc01-17-bim-import-applied-{desktop,phone,tablet}-{light,dark}.png` |
| E-SC01-17 BIM import | Superseded | Badge "Superseded"; final: read-only, no next state; the history shows how it got here | U22 | `u22-site-manager/s-sc01-18-bim-quantities-e-sc01-17-bim-import-superseded-{desktop,phone,tablet}-{light,dark}.png` |

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

⬅️ [S-SC01-17 Off-plan sales](s-sc01-17-off-plan-sales.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC01-19 Renovation grants](s-sc01-19-renovation-grants.md)
