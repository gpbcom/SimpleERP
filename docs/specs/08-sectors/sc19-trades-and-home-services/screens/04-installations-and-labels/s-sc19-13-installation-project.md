🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) ›
🔧 [SC19 Trades and home services](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-SC19-04 Installations and labels](README.md) › 🖥️ S-SC19-13 Installation project

# 🖥️ S-SC19-13 Installation project

**Status:** 🔄 waiting for the owner

## Personas

- [U22 Site manager](../../../../01-users/personas/u22-site-manager.md): the installations with their steps, dates and
  documents.
- [U14 Field worker](../../../../01-users/personas/u14-field-worker.md): the steps assigned, to close on the phone.

## Purpose

Follow an installation from the accepted quote to the signed commissioning, with the grant check before works.

## Entry points

Trades and home services › Installations; an accepted quote's page.

## Wireframe

```text
+--------------------------------------------------------------------------------------------------+
| Installation N-0210: Heat pump, Lambert                    State: Planned   [Start works]        |
| Step               Technician   Planned     Documents   State                                    |
| Survey             Leroy        5 Feb       3 photos    Closed                                   |
| Grant request      Office       8 Feb       receipt     Filed                                    |
| Works              Petit        20 Feb      -           Planned                                  |
| Commissioning      Petit        22 Feb      -           Planned                                  |
+--------------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC19-04 step 1, U22 | desktop | ![FL-SC19-04 step 1, U22, light](../../images/04-installations-and-labels/u22-site-manager/1-installation-project-desktop-light.png) | ![FL-SC19-04 step 1, U22, dark](../../images/04-installations-and-labels/u22-site-manager/1-installation-project-desktop-dark.png) |
| FL-SC19-04 step 1, U22 | phone | ![FL-SC19-04 step 1, U22, light](../../images/04-installations-and-labels/u22-site-manager/1-installation-project-phone-light.png) | ![FL-SC19-04 step 1, U22, dark](../../images/04-installations-and-labels/u22-site-manager/1-installation-project-phone-dark.png) |
| FL-SC19-04 step 1, U22 | tablet | ![FL-SC19-04 step 1, U22, light](../../images/04-installations-and-labels/u22-site-manager/1-installation-project-tablet-light.png) | ![FL-SC19-04 step 1, U22, dark](../../images/04-installations-and-labels/u22-site-manager/1-installation-project-tablet-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc19-13-installation-project-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc19-13-installation-project-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc19-13-installation-project-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc19-13-installation-project-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc19-13-installation-project-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc19-13-installation-project-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc19-13-installation-project-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc19-13-installation-project-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Quote | E-SC19-07 quote | link | no | yes |
| Kind | E-SC19-07 kind | heat pump, solar, electrical board, other | yes while Planned | yes |
| Steps | E-SC19-07 steps | list of name, technician, date, documents and state | yes | yes |
| Grant | E-SC19-07 grant | link to the grant file | no | no |
| Commissioned on | E-SC19-07 commissioned | date | no | no |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Assign step | row | site manager | a technician and a date are set |
| Close step | row | technician | the step is closed with its documents |
| Start works | header | site manager | the works step starts after the grant check |

## States

- Normal: the installations with kind, steps, technicians, dates, documents and state.
- Empty: No installation yet, with Create from a quote.
- Loading: the headings and the table as placeholders; the values follow.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); a grant request
  not filed, a document missing, with the step named.
- Read-only: the record in a locked state: values shown, no action offered.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-SC19-07 Installation](../../data/e-sc19-07-installation.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC19-07 Installation | Planned | Badge "Planned"; a new record starts here; next: In progress or Cancelled (BR-SC19-13, UC-SC19-13); fields editable within the role | U22, U14 | `u22-site-manager/s-sc19-13-installation-project-e-sc19-07-installation-planned-{desktop,phone,tablet}-{light,dark}.png`, `u14-field-worker/s-sc19-13-installation-project-e-sc19-07-installation-planned-phone-{light,dark}.png` |
| E-SC19-07 Installation | In progress | Badge "In progress"; next: Completed (UC-SC19-13); fields editable within the role | U22, U14 | `u22-site-manager/s-sc19-13-installation-project-e-sc19-07-installation-in-progress-{desktop,phone,tablet}-{light,dark}.png`, `u14-field-worker/s-sc19-13-installation-project-e-sc19-07-installation-in-progress-phone-{light,dark}.png` |
| E-SC19-07 Installation | Completed | Badge "Completed"; next: Commissioned (UC-SC19-13); fields editable within the role | U22, U14 | `u22-site-manager/s-sc19-13-installation-project-e-sc19-07-installation-completed-{desktop,phone,tablet}-{light,dark}.png`, `u14-field-worker/s-sc19-13-installation-project-e-sc19-07-installation-completed-phone-{light,dark}.png` |
| E-SC19-07 Installation | Commissioned | Badge "Commissioned"; final: read-only, no next state; the history shows how it got here | U22, U14 | `u22-site-manager/s-sc19-13-installation-project-e-sc19-07-installation-commissioned-{desktop,phone,tablet}-{light,dark}.png`, `u14-field-worker/s-sc19-13-installation-project-e-sc19-07-installation-commissioned-phone-{light,dark}.png` |
| E-SC19-07 Installation | Cancelled | Badge "Cancelled"; final: read-only, no next state; the history shows how it got here | U22, U14 | `u22-site-manager/s-sc19-13-installation-project-e-sc19-07-installation-cancelled-{desktop,phone,tablet}-{light,dark}.png`, `u14-field-worker/s-sc19-13-installation-project-e-sc19-07-installation-cancelled-phone-{light,dark}.png` |

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

⬅️ [S-SC19-12 Immediate advance](../03-home-services-tax-credit/s-sc19-12-immediate-advance.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC19-14 Installation grants](s-sc19-14-installation-grants.md)
