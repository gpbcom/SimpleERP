🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🧰 [F14 Plugin store](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F14-07 Plugin end of life](README.md) › 🖥️ S-F14-22 Plugin lifecycle

# 🖥️ S-F14-22 Plugin lifecycle

**Status:** ✅ specified

## Personas

- [U46 Plugin publisher](../../../../01-users/personas/u46-plugin-publisher.md), who announces an end of life or asks to
  take over
- [U11 IT provider administrator](../../../../01-users/personas/u11-provider-admin.md), who marks plugins abandoned and
  approves transfers
- [U07 Administrator](../../../../01-users/personas/u07-administrator.md), who reads notices and consents

## Purpose

Announce a plugin's end of life, mark it abandoned, and move it to a new maintainer.

## Entry points

The publisher portal's listing; the store operator's moderation; an administrator's installed plugins.

## Wireframe

```text
Old Sync, lifecycle                                  Status: end of life announced
-------------------------------------------------------------------------------
Announced 2026-12-01   End 2027-06-30   Reason: publisher stops the product
Alternatives: New Sync                               [Export data] (administrator)
-------------------------------------------------------------------------------
Take-over requests: Partner Q, review passed        [Approve] (store operator)
Consents: 41 of 52 companies
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F14-07 step 1, U46 | desktop | ![FL-F14-07 step 1, U46, light](../../images/07-plugin-end-of-life/u46-plugin-publisher/1-plugin-lifecycle-desktop-light.png) | ![FL-F14-07 step 1, U46, dark](../../images/07-plugin-end-of-life/u46-plugin-publisher/1-plugin-lifecycle-desktop-dark.png) |
| Error E1, U46 | desktop | ![Error E1, U46, light](../../images/07-plugin-end-of-life/u46-plugin-publisher/e1-plugin-lifecycle-refused-desktop-light.png) | ![Error E1, U46, dark](../../images/07-plugin-end-of-life/u46-plugin-publisher/e1-plugin-lifecycle-refused-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f14-22-plugin-lifecycle-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f14-22-plugin-lifecycle-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f14-22-plugin-lifecycle-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f14-22-plugin-lifecycle-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f14-22-plugin-lifecycle-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f14-22-plugin-lifecycle-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f14-22-plugin-lifecycle-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f14-22-plugin-lifecycle-offline-desktop-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| End date | E-F14-15 end date | date | yes (publisher) | yes |
| Reason | E-F14-15 reason | text | yes | yes |
| Alternatives | E-F14-15 alternatives | listings | yes | no |
| Transfer | E-F14-16 status | asked, approved, done | no | no |
| Consents | E-F14-16 consents | count | no | no |

## Actions

| Action | Where | Who | Result |
|---|---|---|---|
| Announce end of life | header | publisher | notice published, installers warned |
| Mark abandoned | header | store operator | listing shows "looking for a maintainer" |
| Ask to take over | listing | verified publisher | request sent |
| Approve transfer | requests | store operator | installers asked to consent |
| Consent | notice | administrator | company receives the new maintainer's versions |

## States

- Normal: the plugin's lifecycle status, notice, alternatives, take-over requests and consents.
- Empty: "Maintained": shown when the plugin has no notice and no request.
- Loading: the frame and titles show at once with placeholder rows for the lifecycle; within 1 second (D408) the data
  replaces them, and a longer load shows a progress line saying what loads.
- Error: a notice shorter than the minimum, or an unverified candidate, next to the field.
- Read-only: administrators read the notice and only consent; an ended plugin's notice is read-only.
- Offline: not available offline: lifecycle changes are made on the store's servers. D38 keeps only today's schedule,
  time and intervention records offline. A banner says the connection is lost; what is on screen stays visible, every
  action is disabled and nothing is queued until the connection is back.

Shown entities (VD-15): [E-F14-15 End-of-life notice](../../data/e-f14-15-end-of-life-notice.md),
[E-F14-01 Store listing](../../data/e-f14-01-store-listing.md),
[E-F14-16 Maintainer transfer](../../data/e-f14-16-maintainer-transfer.md),
[E-F14-21 Plugin security review](../../data/e-f14-21-plugin-security-review.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F14-15 End-of-life notice | Announced | Badge "Announced"; a new record starts here; next: Ended or Taken over (UC-F14-22, BR-F14-17); fields editable within the role | U07, U11, U46 | `u07-administrator/s-f14-22-plugin-lifecycle-e-f14-15-end-of-life-notice-announced-desktop-{light,dark}.png`, `u11-provider-admin/s-f14-22-plugin-lifecycle-e-f14-15-end-of-life-notice-announced-desktop-{light,dark}.png`, `u46-plugin-publisher/s-f14-22-plugin-lifecycle-e-f14-15-end-of-life-notice-announced-desktop-{light,dark}.png` |
| E-F14-01 Store listing | New | Badge "New"; a new record starts here; next: Paid or Refused (BR-F14-09); fields editable within the role | U07, U11, U46 | `u07-administrator/s-f14-22-plugin-lifecycle-e-f14-01-store-listing-new-desktop-{light,dark}.png`, `u11-provider-admin/s-f14-22-plugin-lifecycle-e-f14-01-store-listing-new-desktop-{light,dark}.png`, `u46-plugin-publisher/s-f14-22-plugin-lifecycle-e-f14-01-store-listing-new-desktop-{light,dark}.png` |
| E-F14-01 Store listing | Paid | Badge "Paid"; next: Complete or Refused (UC-F14-08, BR-F14-09); fields editable within the role | U07, U11, U46 | `u07-administrator/s-f14-22-plugin-lifecycle-e-f14-01-store-listing-paid-desktop-{light,dark}.png`, `u11-provider-admin/s-f14-22-plugin-lifecycle-e-f14-01-store-listing-paid-desktop-{light,dark}.png`, `u46-plugin-publisher/s-f14-22-plugin-lifecycle-e-f14-01-store-listing-paid-desktop-{light,dark}.png` |
| E-F14-01 Store listing | Refused | Badge "Refused"; final: read-only, no next state; the history shows how it got here | U07, U11, U46 | `u07-administrator/s-f14-22-plugin-lifecycle-e-f14-01-store-listing-refused-desktop-{light,dark}.png`, `u11-provider-admin/s-f14-22-plugin-lifecycle-e-f14-01-store-listing-refused-desktop-{light,dark}.png`, `u46-plugin-publisher/s-f14-22-plugin-lifecycle-e-f14-01-store-listing-refused-desktop-{light,dark}.png` |
| E-F14-16 Maintainer transfer | Asked | Badge "Asked"; a new record starts here; next: Approved or Refused (UC-F14-23); fields editable within the role | U07, U11, U46 | `u07-administrator/s-f14-22-plugin-lifecycle-e-f14-16-maintainer-transfer-asked-desktop-{light,dark}.png`, `u11-provider-admin/s-f14-22-plugin-lifecycle-e-f14-16-maintainer-transfer-asked-desktop-{light,dark}.png`, `u46-plugin-publisher/s-f14-22-plugin-lifecycle-e-f14-16-maintainer-transfer-asked-desktop-{light,dark}.png` |
| E-F14-16 Maintainer transfer | Refused | Badge "Refused"; final: read-only, no next state; the history shows how it got here | U07, U11, U46 | `u07-administrator/s-f14-22-plugin-lifecycle-e-f14-16-maintainer-transfer-refused-desktop-{light,dark}.png`, `u11-provider-admin/s-f14-22-plugin-lifecycle-e-f14-16-maintainer-transfer-refused-desktop-{light,dark}.png`, `u46-plugin-publisher/s-f14-22-plugin-lifecycle-e-f14-16-maintainer-transfer-refused-desktop-{light,dark}.png` |
| E-F14-21 Plugin security review | Active | Badge "Active"; a new record starts here; next: Approved, Changes asked or Rejected (UC-F14-10); fields editable within the role | U07, U11, U46 | `u07-administrator/s-f14-22-plugin-lifecycle-e-f14-21-plugin-security-review-active-desktop-{light,dark}.png`, `u11-provider-admin/s-f14-22-plugin-lifecycle-e-f14-21-plugin-security-review-active-desktop-{light,dark}.png`, `u46-plugin-publisher/s-f14-22-plugin-lifecycle-e-f14-21-plugin-security-review-active-desktop-{light,dark}.png` |
| E-F14-21 Plugin security review | Approved | Badge "Approved"; final: read-only, no next state; the history shows how it got here | U07, U11, U46 | `u07-administrator/s-f14-22-plugin-lifecycle-e-f14-21-plugin-security-review-approved-desktop-{light,dark}.png`, `u11-provider-admin/s-f14-22-plugin-lifecycle-e-f14-21-plugin-security-review-approved-desktop-{light,dark}.png`, `u46-plugin-publisher/s-f14-22-plugin-lifecycle-e-f14-21-plugin-security-review-approved-desktop-{light,dark}.png` |
| E-F14-21 Plugin security review | Changes asked | Badge "Changes asked"; final: read-only, no next state; the history shows how it got here | U07, U11, U46 | `u07-administrator/s-f14-22-plugin-lifecycle-e-f14-21-plugin-security-review-changes-asked-desktop-{light,dark}.png`, `u11-provider-admin/s-f14-22-plugin-lifecycle-e-f14-21-plugin-security-review-changes-asked-desktop-{light,dark}.png`, `u46-plugin-publisher/s-f14-22-plugin-lifecycle-e-f14-21-plugin-security-review-changes-asked-desktop-{light,dark}.png` |
| E-F14-21 Plugin security review | Rejected | Badge "Rejected"; final: read-only, no next state; the history shows how it got here | U07, U11, U46 | `u07-administrator/s-f14-22-plugin-lifecycle-e-f14-21-plugin-security-review-rejected-desktop-{light,dark}.png`, `u11-provider-admin/s-f14-22-plugin-lifecycle-e-f14-21-plugin-security-review-rejected-desktop-{light,dark}.png`, `u46-plugin-publisher/s-f14-22-plugin-lifecycle-e-f14-21-plugin-security-review-rejected-desktop-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop; administrators read notices and consent on a phone.

## Accessibility

Keyboard order follows the reading order; every control has a visible label; amounts, states and icons are also given as
text; status changes are announced to screen readers.

## Components

- [C-04 Card](../../../../04-ux/design-system/components/c-04-card.md)
- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)
- [C-05 Modal](../../../../04-ux/design-system/components/c-05-modal.md)
- [C-10 Empty state](../../../../04-ux/design-system/components/c-10-empty-state.md)

## Shown in

- [FL-F14-07 Plugin end of life](../../flows/fl-f14-07-plugin-end-of-life.md)

## Open questions

None.

---

⬅️ [S-F14-21 Dependency report](../03-publish/s-f14-21-dependency-report.md) · ⬆️ [Up](README.md) ·
➡️ [S-F14-23 Release channels](../06-release-channels-and-rollback/s-f14-23-release-channels.md)
