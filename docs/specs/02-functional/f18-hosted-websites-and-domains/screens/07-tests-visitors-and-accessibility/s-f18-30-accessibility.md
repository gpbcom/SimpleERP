🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🌐 [F18 Hosted websites and domains (hosted edition)](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F18-07 A/B tests, visitors, accessibility and members](README.md) › 🖥️ S-F18-30 Accessibility

# 🖥️ S-F18-30 Accessibility

**Status:** 🔄 waiting for the owner

## Personas

- [U12 Marketing and communication](../../../../01-users/personas/u12-marketing.md): the checks, the draft and the
  published statement.
- [U07 Administrator](../../../../01-users/personas/u07-administrator.md): the findings to fix on pages and templates.

## Purpose

Check the site's accessibility, fix the gaps and publish an honest accessibility statement.

## Entry points

Hosted websites and domains › Accessibility; the publication checks; the shop connection.

## Wireframe

```text
+---------------------------------------------------------------------------------------------+
| Accessibility: atelier-nord.example   Last check 2026-11-10   Level: partly accessible [Check]  |
|---------------------------------------------------------------------------------------------|
| Automatic: 17 findings on 6 pages    Manual checks: 9 of 12 done    Statement: Draft           |
| PAGE         FINDING                          HOW TO FIX                         STATE          |
| /shop        Image without a text alternative  Add a description                 Open           |
| /contact     Form field without a label        Name the field                    Fixed          |
| Statement: standard, level, gaps, contact, complaint route        [Edit] [Ask approval]        |
+---------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F18-07 step 3, U12 | desktop | ![FL-F18-07 step 3, U12, light](../../images/07-tests-visitors-and-accessibility/u12-marketing/3-accessibility-desktop-light.png) | ![FL-F18-07 step 3, U12, dark](../../images/07-tests-visitors-and-accessibility/u12-marketing/3-accessibility-desktop-dark.png) |
| FL-F18-07 step 3, U12 | phone | ![FL-F18-07 step 3, U12, light](../../images/07-tests-visitors-and-accessibility/u12-marketing/3-accessibility-phone-light.png) | ![FL-F18-07 step 3, U12, dark](../../images/07-tests-visitors-and-accessibility/u12-marketing/3-accessibility-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f18-30-accessibility-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f18-30-accessibility-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f18-30-accessibility-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f18-30-accessibility-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f18-30-accessibility-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f18-30-accessibility-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f18-30-accessibility-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f18-30-accessibility-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Site and last check | E-F18-22 site, checked on | link and date | no | yes |
| Level reached | E-F18-22 level | accessible, partly, not | computed, then editable by marketing | yes |
| Findings | E-F18-22 findings | page, finding, state | state by administrator | no |
| Known gaps | E-F18-22 gaps and reasons | text | by marketing | yes |
| Contact and complaint route | E-F18-22 contact | email and text | by marketing | yes |
| Statement text and address | E-F18-22 text, address | text and link | by marketing while Draft | yes |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Check | header | marketing, administrator | runs the automatic criteria on every page |
| Record a manual check | list | marketing, administrator | the result is saved with the page |
| Ask approval | statement | marketing | the owner approves or returns it |
| Publish | statement | owner | the statement goes live at its fixed address |

## States

- Normal: the findings, the manual checks and the draft or published statement.
- Empty: No check yet, with Check the site.
- Loading: the headings and the table as placeholders; the values follow.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); a page that
  cannot be checked is named with the reason.
- Read-only: the record in a locked state: values shown, no action offered.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-F18-22 Accessibility statement](../../data/e-f18-22-accessibility-statement.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F18-22 Accessibility statement | Draft | Badge "Draft"; a new record starts here; next: Published (BR-F18-24); fields editable within the role | U12, U07 | `u12-marketing/s-f18-30-accessibility-e-f18-22-accessibility-statement-draft-{desktop,phone}-{light,dark}.png`, `u07-administrator/s-f18-30-accessibility-e-f18-22-accessibility-statement-draft-desktop-{light,dark}.png` |
| E-F18-22 Accessibility statement | Published | Badge "Published"; next: Outdated or Replaced (BR-F18-24, UC-F18-30); fields editable within the role | U12, U07 | `u12-marketing/s-f18-30-accessibility-e-f18-22-accessibility-statement-published-{desktop,phone}-{light,dark}.png`, `u07-administrator/s-f18-30-accessibility-e-f18-22-accessibility-statement-published-desktop-{light,dark}.png` |
| E-F18-22 Accessibility statement | Outdated | Badge "Outdated"; next: Draft (UC-F18-30); fields editable within the role | U12, U07 | `u12-marketing/s-f18-30-accessibility-e-f18-22-accessibility-statement-outdated-{desktop,phone}-{light,dark}.png`, `u07-administrator/s-f18-30-accessibility-e-f18-22-accessibility-statement-outdated-desktop-{light,dark}.png` |
| E-F18-22 Accessibility statement | Replaced | Badge "Replaced"; final: read-only, no next state; the history shows how it got here | U12, U07 | `u12-marketing/s-f18-30-accessibility-e-f18-22-accessibility-statement-replaced-{desktop,phone}-{light,dark}.png`, `u07-administrator/s-f18-30-accessibility-e-f18-22-accessibility-statement-replaced-desktop-{light,dark}.png` |

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

- [FL-F18-07](../../flows/fl-f18-07-tests-visitors-and-accessibility.md)

## Open questions

None.

---

⬅️ [S-F18-29 Visitor tracking](s-f18-29-visitor-tracking.md) · ⬆️ [Up](README.md) ·
➡️ [S-F18-31 Members pages](s-f18-31-members-pages.md)
