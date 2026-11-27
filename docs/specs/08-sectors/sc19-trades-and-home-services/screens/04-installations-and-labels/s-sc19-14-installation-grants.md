🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) ›
🔧 [SC19 Trades and home services](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-SC19-04 Installations and labels](README.md) › 🖥️ S-SC19-14 Installation grants

# 🖥️ S-SC19-14 Installation grants

**Status:** ✅ specified

## Personas

- [U22 Site manager](../../../../01-users/personas/u22-site-manager.md): the grants the installation opens, the label
  check and the filing.

## Purpose

Prepare and file the grant file of an installation and follow its answer and payment.

## Entry points

Trades and home services › Grant files; an installation's page.

## Wireframe

```text
+--------------------------------------------------------------------------------------------------+
| Grant file G-0118: Heat pump, Lambert                    State: Draft   [File request]           |
| Grant              Body           Amount    Label check      Documents   State                   |
| Renovation grant   State body     4,000     Covered          4 of 5      Draft                   |
| Energy bonus       Supplier       1,200     Covered          2 of 2      Draft                   |
| Missing: tax notice of the customer                          [Attach] [Drop a grant]             |
+--------------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC19-04 step 2, U22 | desktop | ![FL-SC19-04 step 2, U22, light](../../images/04-installations-and-labels/u22-site-manager/2-installation-grants-desktop-light.png) | ![FL-SC19-04 step 2, U22, dark](../../images/04-installations-and-labels/u22-site-manager/2-installation-grants-desktop-dark.png) |
| FL-SC19-04 step 2, U22 | phone | ![FL-SC19-04 step 2, U22, light](../../images/04-installations-and-labels/u22-site-manager/2-installation-grants-phone-light.png) | ![FL-SC19-04 step 2, U22, dark](../../images/04-installations-and-labels/u22-site-manager/2-installation-grants-phone-dark.png) |
| FL-SC19-04 step 2, U22 | tablet | ![FL-SC19-04 step 2, U22, light](../../images/04-installations-and-labels/u22-site-manager/2-installation-grants-tablet-light.png) | ![FL-SC19-04 step 2, U22, dark](../../images/04-installations-and-labels/u22-site-manager/2-installation-grants-tablet-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc19-14-installation-grants-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc19-14-installation-grants-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc19-14-installation-grants-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc19-14-installation-grants-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc19-14-installation-grants-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc19-14-installation-grants-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc19-14-installation-grants-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc19-14-installation-grants-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Installation | E-SC19-08 installation | link | no | yes |
| Grants | E-SC19-08 grants | list of grant, body and amount | yes while Draft | yes |
| Label check | E-SC19-08 label check | covered, not covered | no | yes |
| Documents | E-SC19-08 documents | list with state | yes | yes |
| Filed on | E-SC19-08 filed | date | no | no |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Attach | documents | site manager | a document is added to the file |
| Drop a grant | row | site manager | the grant leaves the file with its reason |
| File request | header | site manager | the request is filed and its receipt kept |

## States

- Normal: the file with its grants, label check, documents and state.
- Empty: No grant file yet, with Create from an installation.
- Loading: the headings and the table as placeholders; the values follow.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); a label not
  covering the work, a document missing, with the grant named.
- Read-only: the record in a locked state: values shown, no action offered.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-SC19-08 Grant file](../../data/e-sc19-08-grant-file.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC19-08 Grant file | Draft | Badge "Draft"; a new record starts here; next: Filed (BR-SC19-14); fields editable within the role | U22 | `u22-site-manager/s-sc19-14-installation-grants-e-sc19-08-grant-file-draft-{desktop,phone,tablet}-{light,dark}.png` |
| E-SC19-08 Grant file | Filed | Badge "Filed"; next: Accepted, Refused or Draft (UC-SC19-14); fields editable within the role | U22 | `u22-site-manager/s-sc19-14-installation-grants-e-sc19-08-grant-file-filed-{desktop,phone,tablet}-{light,dark}.png` |
| E-SC19-08 Grant file | Accepted | Badge "Accepted"; next: Paid (UC-SC19-14); fields editable within the role | U22 | `u22-site-manager/s-sc19-14-installation-grants-e-sc19-08-grant-file-accepted-{desktop,phone,tablet}-{light,dark}.png` |
| E-SC19-08 Grant file | Refused | Badge "Refused"; final: read-only, no next state; the history shows how it got here | U22 | `u22-site-manager/s-sc19-14-installation-grants-e-sc19-08-grant-file-refused-{desktop,phone,tablet}-{light,dark}.png` |
| E-SC19-08 Grant file | Paid | Badge "Paid"; final: read-only, no next state; the history shows how it got here | U22 | `u22-site-manager/s-sc19-14-installation-grants-e-sc19-08-grant-file-paid-{desktop,phone,tablet}-{light,dark}.png` |

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

⬅️ [S-SC19-13 Installation project](s-sc19-13-installation-project.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC19-15 RGE evidence](s-sc19-15-rge-evidence.md)
