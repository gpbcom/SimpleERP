🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🌐 [F18 Hosted websites and domains (hosted edition)](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F18-07 A/B tests, visitors, accessibility and members](README.md) › 🖥️ S-F18-28 Page A/B test

# 🖥️ S-F18-28 Page A/B test

**Status:** 🔄 waiting for the owner

## Personas

- [U12 Marketing and communication](../../../../01-users/personas/u12-marketing.md): the tests of every page of the
  site.

## Purpose

Compare two versions of a page on the visitors who accepted tracking, and publish the better one with the owner's yes.

## Entry points

Hosted websites and domains › Page tests; a page's menu › Test this page.

## Wireframe

```text
+---------------------------------------------------------------------------------------------+
| Page test: Home page title        Running since 2026-11-24     Ends 2026-12-15   [Pause][Stop] |
|---------------------------------------------------------------------------------------------|
| Goal: contact form sent       Split: A 50 percent, B 50 percent       Consent banner: live    |
| VERSION        VISITORS   GOALS   RATE     VERSUS A     SURE                                  |
| A (original)   1,204      31      2.6 %    -            -                                     |
| B "Plans from 29 EUR"  1,187   46   3.9 %   +1.3 points   96 %                                |
| Minimum: 500 visitors each, 7 days    Checks: A passed, B passed                             |
+---------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F18-07 step 1, U12 | desktop | ![FL-F18-07 step 1, U12, light](../../images/07-tests-visitors-and-accessibility/u12-marketing/1-page-ab-test-desktop-light.png) | ![FL-F18-07 step 1, U12, dark](../../images/07-tests-visitors-and-accessibility/u12-marketing/1-page-ab-test-desktop-dark.png) |
| FL-F18-07 step 1, U12 | phone | ![FL-F18-07 step 1, U12, light](../../images/07-tests-visitors-and-accessibility/u12-marketing/1-page-ab-test-phone-light.png) | ![FL-F18-07 step 1, U12, dark](../../images/07-tests-visitors-and-accessibility/u12-marketing/1-page-ab-test-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f18-28-page-ab-test-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f18-28-page-ab-test-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f18-28-page-ab-test-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f18-28-page-ab-test-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f18-28-page-ab-test-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f18-28-page-ab-test-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f18-28-page-ab-test-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f18-28-page-ab-test-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Page and versions | E-F18-20 page, versions | page and two versions | yes while Draft | yes |
| Goal | E-F18-20 goal | form sent, click, next page | yes while Draft | yes |
| Split and dates | E-F18-20 split, start, end | percent and dates | yes while Draft | yes |
| Visitors and goals | E-F18-20 counts per version | numbers | no | no |
| Rate and how sure | E-F18-20 rate, significance | percent | no | no |
| Minimum | E-F18-20 minimum visitors, days | numbers | yes while Draft | yes |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Start | header | marketing | the test runs after the checks passed |
| Pause or stop | header | marketing | visitors see the original again |
| Publish the winner | result | owner, administrator | the winning version goes through the publication approval |
| Keep the original | result | marketing, owner | the test is closed with no change |

## States

- Normal: the running test with the figures per version and how sure the difference is.
- Empty: No test yet, with Test this page.
- Loading: the headings and the table as placeholders; the values follow.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); a failed check
  or a stopped measurement is named, with what to do.
- Read-only: the record in a locked state: values shown, no action offered.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-F18-20 Page test](../../data/e-f18-20-page-test.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F18-20 Page test | Draft | Badge "Draft"; a new record starts here; next: Running or Dropped (BR-F18-04, UC-F18-28); fields editable within the role | U12 | `u12-marketing/s-f18-28-page-ab-test-e-f18-20-page-test-draft-{desktop,phone}-{light,dark}.png` |
| E-F18-20 Page test | Running | Badge "Running"; next: Paused or Ended (UC-F18-28, BR-F18-22); fields editable within the role | U12 | `u12-marketing/s-f18-28-page-ab-test-e-f18-20-page-test-running-{desktop,phone}-{light,dark}.png` |
| E-F18-20 Page test | Paused | Badge "Paused"; next: Running or Ended (UC-F18-28); fields editable within the role | U12 | `u12-marketing/s-f18-28-page-ab-test-e-f18-20-page-test-paused-{desktop,phone}-{light,dark}.png` |
| E-F18-20 Page test | Ended | Badge "Ended"; next: Applied or Dropped (BR-F18-05, UC-F18-28); fields editable within the role | U12 | `u12-marketing/s-f18-28-page-ab-test-e-f18-20-page-test-ended-{desktop,phone}-{light,dark}.png` |
| E-F18-20 Page test | Applied | Badge "Applied"; final: read-only, no next state; the history shows how it got here | U12 | `u12-marketing/s-f18-28-page-ab-test-e-f18-20-page-test-applied-{desktop,phone}-{light,dark}.png` |
| E-F18-20 Page test | Dropped | Badge "Dropped"; final: read-only, no next state; the history shows how it got here | U12 | `u12-marketing/s-f18-28-page-ab-test-e-f18-20-page-test-dropped-{desktop,phone}-{light,dark}.png` |

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

⬅️ [S-F18-27 Backups](../05-run-the-site/s-f18-27-backups.md) · ⬆️ [Up](README.md) ·
➡️ [S-F18-29 Visitor tracking](s-f18-29-visitor-tracking.md)
