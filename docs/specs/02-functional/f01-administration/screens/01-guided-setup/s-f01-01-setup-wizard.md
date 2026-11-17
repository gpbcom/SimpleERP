🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🛡️ [F1 Administration](../../README.md) › 🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-F1-01 Guided setup](README.md) ›
🖥️ S-F1-01 Setup wizard

# 🖥️ S-F1-01 Setup wizard

**Status:** ✅ specified

## Personas

- [U07 Administrator](../../../../01-users/personas/u07-administrator.md)
- [U13 Owner](../../../../01-users/personas/u13-owner.md)

## Purpose

Take a brand-new company through the seven setup steps.

## Entry points

The first sign-in to a new company, and every sign-in until the setup is done.

## Wireframe

```text
+------------------------------------------------------------------+
| simple-ERP                Setup of Acme Bâtiment        [Save, leave]|
+------------------------------------------------------------------+
| (1)--(2)--(3)--(4)--(5)--(6)--(7)                                 |
| Identity Money Sites Pack Users Import Done                        |
|                                                                  |
| 1. Company identity                                              |
|   SIREN      [ 552 100 554 ]  [Look up]   (SIRENE lookup: on)     |
|   Name       [ Acme Bâtiment SAS            ]                      |
|   Legal form [ SAS                     v ]                         |
|   VAT number [ FR40 552100554            ]                         |
|   Address    [ 12 rue des Lilas, 69003 Lyon ]                      |
|   Logo       [ Upload... ]                                         |
|                                                                  |
|   Ask the assistant, or let it prefill this step: [AI]           |
|                                      [Back]  [Save and continue] |
+------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F1-01 step 1, U07 | desktop | ![FL-F1-01 step 1, U07, light](../../images/01-guided-setup/u07-administrator/1-company-identity-desktop-light.png) | ![FL-F1-01 step 1, U07, dark](../../images/01-guided-setup/u07-administrator/1-company-identity-desktop-dark.png) |
| Error E1, U07 | desktop | ![Error E1, U07, light](../../images/01-guided-setup/u07-administrator/e1-siren-not-found-desktop-light.png) | ![Error E1, U07, dark](../../images/01-guided-setup/u07-administrator/e1-siren-not-found-desktop-dark.png) |
| Error E2, U07 | desktop | ![Error E2, U07, light](../../images/01-guided-setup/u07-administrator/e2-vat-mismatch-desktop-light.png) | ![Error E2, U07, dark](../../images/01-guided-setup/u07-administrator/e2-vat-mismatch-desktop-dark.png) |
| Error E3, U07 | desktop | ![Error E3, U07, light](../../images/01-guided-setup/u07-administrator/e3-import-errors-desktop-light.png) | ![Error E3, U07, dark](../../images/01-guided-setup/u07-administrator/e3-import-errors-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f01-01-setup-wizard-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f01-01-setup-wizard-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f01-01-setup-wizard-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f01-01-setup-wizard-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f01-01-setup-wizard-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f01-01-setup-wizard-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f01-01-setup-wizard-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f01-01-setup-wizard-offline-desktop-dark.png) |

## Fields and columns

| Step | Fields |
|---|---|
| 1 Identity | SIREN, name, legal form, VAT number, address, logo |
| 2 Money | Currency, fiscal year start, VAT regime |
| 3 Sites | Per site: name, address, hours, holds stock, manager |
| 4 Sector pack | One of eight packs, or none |
| 5 Users | Email invitations with role and site, or single sign-on settings |
| 6 Import | Source (template, FEC, other ERP), file, result |
| 7 Done | Checklist |

## Actions

| Action | Where | Who | Result |
|---|---|---|---|
| Look up | Step 1 | Administrator | Prefills from SIRENE (D60) |
| Save and continue | Every step | Administrator | Saves the step, opens the next |
| Back | Steps 2 to 7 | Administrator | Opens the previous step, kept as saved |
| Save, leave | Every step | Administrator | Saves and signs out; resumes here (D54) |
| Finish | Step 7 | Administrator | Opens the home screen (D59) |

## States

- Normal: Take a brand-new company through the seven setup steps, as the wireframe shows.
- Empty: step 1 with nothing filled.
- Loading: during the SIRENE lookup and imports.
- Error: a field or an import line in error, with its message next to it.
- Read-only: none.
- Offline: Not available offline: a back-office screen on live, shared data (D38: only today's schedule, time and
  intervention records work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-F1-01 Company](../../data/e-f01-01-company.md),
[E-F1-02 Company site](../../data/e-f01-02-company-site.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F1-01 Company | In setup | Badge "In setup"; a new record starts here; next: Active (UC-F1-23); fields editable within the role | U07, U13 | `u07-administrator/s-f01-01-setup-wizard-e-f01-01-company-in-setup-desktop-{light,dark}.png`, `u13-owner/s-f01-01-setup-wizard-e-f01-01-company-in-setup-{desktop,phone}-{light,dark}.png` |
| E-F1-01 Company | Active | Badge "Active"; final: read-only, no next state; the history shows how it got here | U07, U13 | `u07-administrator/s-f01-01-setup-wizard-e-f01-01-company-active-desktop-{light,dark}.png`, `u13-owner/s-f01-01-setup-wizard-e-f01-01-company-active-{desktop,phone}-{light,dark}.png` |
| E-F1-02 Company site | Open | Badge "Open"; a new record starts here; next: Closed (UC-F1-02); fields editable within the role | U07, U13 | `u07-administrator/s-f01-01-setup-wizard-e-f01-02-company-site-open-desktop-{light,dark}.png`, `u13-owner/s-f01-01-setup-wizard-e-f01-02-company-site-open-{desktop,phone}-{light,dark}.png` |
| E-F1-02 Company site | Closed | Badge "Closed"; next: Open (UC-F1-02); fields editable within the role | U07, U13 | `u07-administrator/s-f01-01-setup-wizard-e-f01-02-company-site-closed-desktop-{light,dark}.png`, `u13-owner/s-f01-01-setup-wizard-e-f01-02-company-site-closed-{desktop,phone}-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop and tablet; on a phone, a message asks to continue on a larger screen.

## Accessibility

The stepper is a list with the current step marked `aria-current`; errors are linked to their field and announced; every
action is reachable by keyboard.

## Components

- [C-13 Stepper](../../../../04-ux/design-system/components/c-13-stepper.md)
- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)
- [C-12 File upload](../../../../04-ux/design-system/components/c-12-file-upload.md)
- [C-11 Chat panel](../../../../04-ux/design-system/components/c-11-chat-panel.md)

## Shown in

- [FL-F1-01 Guided setup](../../flows/fl-f01-01-guided-setup.md)

## Open questions

None.

---

⬆️ [Up](README.md) · ➡️ [S-F1-02 Sites](../02-manage-sites/s-f01-02-sites.md)
