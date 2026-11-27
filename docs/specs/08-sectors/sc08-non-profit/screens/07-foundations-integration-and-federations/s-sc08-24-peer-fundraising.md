🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🤲 [SC08 Non-profit association](../../README.md) ›
🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-SC08-07 Foundations, integration, federations, peer fundraising](README.md) ›
🖥️ S-SC08-24 Peer-to-peer fundraising

# 🖥️ S-SC08-24 Peer-to-peer fundraising

**Status:** ✅ specified

## Personas

- [U12 Marketing and communication](../../../../01-users/personas/u12-marketing.md): the pages to review and the totals
  by campaign.
- [U09 Customer](../../../../01-users/personas/u09-customer.md): their own page, its link and the total raised.

## Purpose

Let supporters raise funds on their own page, review the pages and follow the gifts and receipts.

## Entry points

Non-profit association › Fundraising pages; a campaign's Pages tab; the supporter's link.

## Wireframe

```text
+--------------------------------------------------------------------------------------------------+
| Campaign Run for Health 2026   Pages 38   Raised 21,450   Donors 412         [Review pages]      |
| Page                  Owner       Goal    Raised   Donors  State                                 |
| Marathon for Arc      Julie M.    2,000   1,350    31      Published                             |
| Birthday gift         Karim B.    500     500      14      Closed                                |
| Sale of cakes         Sophie L.   800     0        0       Draft                                 |
| Page rules: purpose only the campaign   Funds go to: the association's account (fixed)           |
| Gifts without a receipt (address missing): 3          [Ask donors]                               |
+--------------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC08-07 step 4, U12 | desktop | ![FL-SC08-07 step 4, U12, light](../../images/07-foundations-integration-and-federations/u12-marketing/4-peer-fundraising-desktop-light.png) | ![FL-SC08-07 step 4, U12, dark](../../images/07-foundations-integration-and-federations/u12-marketing/4-peer-fundraising-desktop-dark.png) |
| FL-SC08-07 step 4, U12 | phone | ![FL-SC08-07 step 4, U12, light](../../images/07-foundations-integration-and-federations/u12-marketing/4-peer-fundraising-phone-light.png) | ![FL-SC08-07 step 4, U12, dark](../../images/07-foundations-integration-and-federations/u12-marketing/4-peer-fundraising-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc08-24-peer-fundraising-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc08-24-peer-fundraising-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc08-24-peer-fundraising-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc08-24-peer-fundraising-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc08-24-peer-fundraising-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc08-24-peer-fundraising-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc08-24-peer-fundraising-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc08-24-peer-fundraising-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Page title | E-SC08-19 title | text | yes while Draft | yes |
| Owner | E-SC08-19 owner | link | no | yes |
| Goal | E-SC08-19 goal | amount in EUR | yes while Draft | yes |
| Raised | E-SC08-19 raised | amount in EUR | no | no |
| Donors | E-SC08-19 donors | number | no | no |
| Campaign | E-SC08-19 campaign | link | yes while Draft | yes |
| End date | E-SC08-19 end date | date | yes | no |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Create page | campaign | supporter | a page in Draft with its link |
| Publish | page | marketing | the page is public and accepts gifts |
| Suspend | page | marketing | the page accepts no more gifts and the owner is told |
| Close | page | marketing, supporter | the page ends and the total is final |

## States

- Normal: the pages with their goal, total, donors and state.
- Empty: No page yet, with Create a page.
- Loading: the headings and the table as placeholders; the values follow.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); a purpose
  outside the campaign or a gift with no address, with the field to complete.
- Read-only: the record in a locked state: values shown, no action offered.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-SC08-19 Fundraising page](../../data/e-sc08-19-fundraising-page.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC08-19 Fundraising page | Draft | Badge "Draft"; a new record starts here; next: Published (UC-SC08-24); fields editable within the role | U12, U09 | `u12-marketing/s-sc08-24-peer-fundraising-e-sc08-19-fundraising-page-draft-{desktop,phone}-{light,dark}.png`, `u09-customer/s-sc08-24-peer-fundraising-e-sc08-19-fundraising-page-draft-phone-{light,dark}.png` |
| E-SC08-19 Fundraising page | Published | Badge "Published"; next: Suspended or Closed (UC-SC08-24, BR-SC08-19); fields editable within the role | U12, U09 | `u12-marketing/s-sc08-24-peer-fundraising-e-sc08-19-fundraising-page-published-{desktop,phone}-{light,dark}.png`, `u09-customer/s-sc08-24-peer-fundraising-e-sc08-19-fundraising-page-published-phone-{light,dark}.png` |
| E-SC08-19 Fundraising page | Suspended | Badge "Suspended"; next: Published (UC-SC08-24); fields editable within the role | U12, U09 | `u12-marketing/s-sc08-24-peer-fundraising-e-sc08-19-fundraising-page-suspended-{desktop,phone}-{light,dark}.png`, `u09-customer/s-sc08-24-peer-fundraising-e-sc08-19-fundraising-page-suspended-phone-{light,dark}.png` |
| E-SC08-19 Fundraising page | Closed | Badge "Closed"; final: read-only, no next state; the history shows how it got here | U12, U09 | `u12-marketing/s-sc08-24-peer-fundraising-e-sc08-19-fundraising-page-closed-{desktop,phone}-{light,dark}.png`, `u09-customer/s-sc08-24-peer-fundraising-e-sc08-19-fundraising-page-closed-phone-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop for marketing. The supporter and the donors use the phone: the page has a large Give button and the goal bar,
and the donor's form asks for the receipt details.

## Accessibility

Every control is reachable by keyboard; states and errors are announced to screen readers and never rely on colour
alone; each field has its visible label.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)
- [C-01 Button](../../../../04-ux/design-system/components/c-01-button.md)

## Shown in

- [FL-SC08-07](../../flows/fl-sc08-07-foundations-integration-and-federations.md)

## Open questions

None.

---

⬅️ [S-SC08-23 Federation](s-sc08-23-federation.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC08-L01 Members](../00-lists/s-sc08-l01-members.md)
