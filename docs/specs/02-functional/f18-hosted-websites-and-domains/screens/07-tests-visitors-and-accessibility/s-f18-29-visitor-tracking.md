🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🌐 [F18 Hosted websites and domains (hosted edition)](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F18-07 A/B tests, visitors, accessibility and members](README.md) › 🖥️ S-F18-29 Visitor tracking

# 🖥️ S-F18-29 Visitor tracking

**Status:** 🔄 waiting for the owner

## Personas

- [U03 Sales](../../../../01-users/personas/u03-sales.md): the known visitors of their contacts and accounts.
- [U12 Marketing and communication](../../../../01-users/personas/u12-marketing.md): the visits by page and source, as
  totals.

## Purpose

See which known contacts visit the site and which pages they read, only for visits they accepted.

## Entry points

Hosted websites and domains › Visitors; a contact's timeline; Customers and sales › Contacts.

## Wireframe

```text
+---------------------------------------------------------------------------------------------+
| Visitors (accepted tracking)     Last 7 days [v]      Known 12     Anonymous 340     [Settings] |
|---------------------------------------------------------------------------------------------|
| CONTACT       COMPANY        VISITS  LAST VISIT        PAGES                         CONSENT   |
| Claire P.     Atelier Nord   3       2026-11-14 09:12  pricing, plans, contact       Yes       |
| Marc D.       Bois & Fils    1       2026-11-13 16:40  careers                       Yes       |
| [Open contact] [Create a call task]            Retention 13 months    Refused: not recorded  |
+---------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F18-07 step 2, U03 | desktop | ![FL-F18-07 step 2, U03, light](../../images/07-tests-visitors-and-accessibility/u03-sales/2-visitor-tracking-desktop-light.png) | ![FL-F18-07 step 2, U03, dark](../../images/07-tests-visitors-and-accessibility/u03-sales/2-visitor-tracking-desktop-dark.png) |
| FL-F18-07 step 2, U03 | phone | ![FL-F18-07 step 2, U03, light](../../images/07-tests-visitors-and-accessibility/u03-sales/2-visitor-tracking-phone-light.png) | ![FL-F18-07 step 2, U03, dark](../../images/07-tests-visitors-and-accessibility/u03-sales/2-visitor-tracking-phone-dark.png) |
| FL-F18-07 step 2, U03 | tablet | ![FL-F18-07 step 2, U03, light](../../images/07-tests-visitors-and-accessibility/u03-sales/2-visitor-tracking-tablet-light.png) | ![FL-F18-07 step 2, U03, dark](../../images/07-tests-visitors-and-accessibility/u03-sales/2-visitor-tracking-tablet-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f18-29-visitor-tracking-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f18-29-visitor-tracking-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f18-29-visitor-tracking-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f18-29-visitor-tracking-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f18-29-visitor-tracking-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f18-29-visitor-tracking-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f18-29-visitor-tracking-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f18-29-visitor-tracking-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Contact and company | E-F18-21 contact | name | no | no |
| Visits and last visit | E-F18-21 visits | number and date | no | yes |
| Pages | E-F18-21 pages seen | list of pages | no | yes |
| Source | E-F18-21 source | search, link, campaign, direct | no | no |
| Consent | E-F18-21 consent state | yes, withdrawn | no | yes |
| Retention | E-F18-21 erase on | date | owner | yes |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Open contact | row | sales | the contact's record with its timeline |
| Create a call task | row | sales | a task to call, with the pages as a note |
| Erase visits | row | owner, administrator | the visits of one person are erased on request |
| Change retention | settings | owner | the months visits are kept |

## States

- Normal: the known visitors of the period with their visits and pages, and the anonymous total.
- Empty: No visit recorded yet, with the state of the consent banner.
- Loading: the headings and the table as placeholders; the values follow.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); a banner that
  is not live shows that nothing is recorded and why.
- Read-only: the record in a locked state: values shown, no action offered.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-F18-21 Visit](../../data/e-f18-21-visit.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F18-21 Visit | Anonymous | Badge "Anonymous"; a new record starts here; next: Identified or Erased (UC-F18-29, BR-F18-23); fields editable within the role | U03, U12 | `u03-sales/s-f18-29-visitor-tracking-e-f18-21-visit-anonymous-{desktop,phone,tablet}-{light,dark}.png`, `u12-marketing/s-f18-29-visitor-tracking-e-f18-21-visit-anonymous-{desktop,phone}-{light,dark}.png` |
| E-F18-21 Visit | Identified | Badge "Identified"; next: Erased (BR-F18-23); fields editable within the role | U03, U12 | `u03-sales/s-f18-29-visitor-tracking-e-f18-21-visit-identified-{desktop,phone,tablet}-{light,dark}.png`, `u12-marketing/s-f18-29-visitor-tracking-e-f18-21-visit-identified-{desktop,phone}-{light,dark}.png` |
| E-F18-21 Visit | Erased | Badge "Erased"; final: read-only, no next state; the history shows how it got here | U03, U12 | `u03-sales/s-f18-29-visitor-tracking-e-f18-21-visit-erased-{desktop,phone,tablet}-{light,dark}.png`, `u12-marketing/s-f18-29-visitor-tracking-e-f18-21-visit-erased-{desktop,phone}-{light,dark}.png` |

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

⬅️ [S-F18-28 Page A/B test](s-f18-28-page-ab-test.md) · ⬆️ [Up](README.md) ·
➡️ [S-F18-30 Accessibility](s-f18-30-accessibility.md)
