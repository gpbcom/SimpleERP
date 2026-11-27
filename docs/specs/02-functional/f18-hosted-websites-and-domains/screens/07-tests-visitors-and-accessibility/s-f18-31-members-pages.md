🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🌐 [F18 Hosted websites and domains (hosted edition)](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F18-07 A/B tests, visitors, accessibility and members](README.md) › 🖥️ S-F18-31 Members pages

# 🖥️ S-F18-31 Members pages

**Status:** 🔄 waiting for the owner

## Personas

- [U12 Marketing and communication](../../../../01-users/personas/u12-marketing.md): the pages and their audiences.
- [U09 Customer](../../../../01-users/personas/u09-customer.md): the pages they may read, from their phone.

## Purpose

Choose who may read a page, check that it stays out of search engines, and read it as a member.

## Entry points

Hosted websites and domains › Members pages; a page's menu › Reserve this page; the customer portal.

## Wireframe

```text
+---------------------------------------------------------------------------------------------+
| Members pages                      [Reserve a page]       Live 4     Waiting for approval 1      |
|---------------------------------------------------------------------------------------------|
| PAGE               AUDIENCE                     INDEXED   IN SITEMAP   STATE      READS (30 d)  |
| Price list 2027    Customers with an account    No        No           Live       86            |
| Partner offers     Group: Partners              No        No           Draft      -             |
| Preview as: [Visitor] [Member]        Checks: not indexed OK, sitemap OK                      |
+---------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F18-07 step 4, U12 | desktop | ![FL-F18-07 step 4, U12, light](../../images/07-tests-visitors-and-accessibility/u12-marketing/4-members-pages-desktop-light.png) | ![FL-F18-07 step 4, U12, dark](../../images/07-tests-visitors-and-accessibility/u12-marketing/4-members-pages-desktop-dark.png) |
| FL-F18-07 step 4, U12 | phone | ![FL-F18-07 step 4, U12, light](../../images/07-tests-visitors-and-accessibility/u12-marketing/4-members-pages-phone-light.png) | ![FL-F18-07 step 4, U12, dark](../../images/07-tests-visitors-and-accessibility/u12-marketing/4-members-pages-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f18-31-members-pages-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f18-31-members-pages-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f18-31-members-pages-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f18-31-members-pages-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f18-31-members-pages-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f18-31-members-pages-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f18-31-members-pages-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f18-31-members-pages-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Page | E-F18-23 page | page | no | yes |
| Audience | E-F18-23 audience | all customers, a group, named people | yes while Draft or Live | yes |
| Indexed and in sitemap | E-F18-23 indexing | no, no | no: always no | yes |
| State | E-F18-23 state | badge | by marketing and owner | yes |
| Reads | E-F18-23 reads | number over 30 days | no | no |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Reserve a page | header | marketing | a page gets an audience and goes to the checks |
| Change audience | row | marketing | who may read changes at once |
| Withdraw | row | marketing, owner | the page leaves the site and keeps its history |
| Preview as visitor or member | header | marketing | shows both views before going live |

## States

- Normal: the members pages with their audience, state and reads.
- Empty: No members page yet, with Reserve a page.
- Loading: the headings and the table as placeholders; the values follow.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); a page held by
  the checks names the check and how to fix it.
- Read-only: the record in a locked state: values shown, no action offered.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-F18-23 Page audience](../../data/e-f18-23-page-audience.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F18-23 Page audience | Draft | Badge "Draft"; a new record starts here; next: Live or Withdrawn (BR-F18-05, UC-F18-31); fields editable within the role | U12, U09 | `u12-marketing/s-f18-31-members-pages-e-f18-23-page-audience-draft-{desktop,phone}-{light,dark}.png`, `u09-customer/s-f18-31-members-pages-e-f18-23-page-audience-draft-phone-{light,dark}.png` |
| E-F18-23 Page audience | Live | Badge "Live"; next: Draft or Withdrawn (UC-F18-31); fields editable within the role | U12, U09 | `u12-marketing/s-f18-31-members-pages-e-f18-23-page-audience-live-{desktop,phone}-{light,dark}.png`, `u09-customer/s-f18-31-members-pages-e-f18-23-page-audience-live-phone-{light,dark}.png` |
| E-F18-23 Page audience | Withdrawn | Badge "Withdrawn"; final: read-only, no next state; the history shows how it got here | U12, U09 | `u12-marketing/s-f18-31-members-pages-e-f18-23-page-audience-withdrawn-{desktop,phone}-{light,dark}.png`, `u09-customer/s-f18-31-members-pages-e-f18-23-page-audience-withdrawn-phone-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Marketing's screen is desktop only. A member reads a page on a phone: a sign-in, then the page in one column.

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

⬅️ [S-F18-30 Accessibility](s-f18-30-accessibility.md) · ⬆️ [Up](README.md) ·
➡️ [S-F18-L01 Hosted websites](../00-lists/s-f18-l01-hosted-websites.md)
