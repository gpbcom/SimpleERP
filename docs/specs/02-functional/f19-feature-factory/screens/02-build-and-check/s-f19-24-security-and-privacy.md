🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🏭 [F19 Feature factory (hosted edition)](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F19-02 Build and check](README.md) › 🖥️ S-F19-24 Security and privacy

# 🖥️ S-F19-24 Security and privacy

**Status:** ✅ specified

## Personas

- [U48 Hosting engineer](../../../../01-users/personas/u48-hosting-engineer.md)
- [U07 Administrator](../../../../01-users/personas/u07-administrator.md)

## Purpose

Record the security and privacy review of a generated version before signing.

## Entry points

The review queue; the "answers needed" notification for the administrator.

## Wireframe

```text
Gate booking 1.2, security and privacy
-------------------------------------------------------------------------------
Permissions: visitors (read, write)   Outside calls: none   Secrets: none
Personal data: names, plates          Purpose: [gate access]   Retention: [30 days]
Impact assessment: not needed
-------------------------------------------------------------------------------
[Ask the administrator] [Pass] [Ask changes] [Reject]
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F19-02 step 5, U48 | desktop | ![FL-F19-02 step 5, U48, light](../../images/02-build-and-check/u48-hosting-engineer/5-security-and-privacy-desktop-light.png) | ![FL-F19-02 step 5, U48, dark](../../images/02-build-and-check/u48-hosting-engineer/5-security-and-privacy-desktop-dark.png) |
| FL-F19-02 step 5, U48 | phone | ![FL-F19-02 step 5, U48, light](../../images/02-build-and-check/u48-hosting-engineer/5-security-and-privacy-phone-light.png) | ![FL-F19-02 step 5, U48, dark](../../images/02-build-and-check/u48-hosting-engineer/5-security-and-privacy-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f19-24-security-and-privacy-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f19-24-security-and-privacy-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f19-24-security-and-privacy-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f19-24-security-and-privacy-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f19-24-security-and-privacy-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f19-24-security-and-privacy-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f19-24-security-and-privacy-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f19-24-security-and-privacy-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Permissions, outside calls | E-F19-14 | lists | no | yes |
| Personal data | E-F19-14 personal data | list | no | yes |
| Purpose, retention | E-F19-14 | text | yes (administrator) | if personal data |
| Impact assessment | E-F19-14 | list | no | yes |
| Decision | E-F19-14 decision | list | yes (engineer) | yes |

## Actions

| Action | Where | Who | Result |
|---|---|---|---|
| Ask the administrator | footer | engineer | questions sent |
| Pass, ask changes, reject | footer | engineer | decision recorded |

## States

- Normal: the version's security facts and personal data with answers.
- Empty: "No personal data": privacy part shown as not needed.
- Loading: the frame and titles show at once with placeholder rows for the review; within 1 second (D408) the data
  replaces them, and a longer load shows a progress line saying what loads.
- Error: missing retention, the review waits.
- Read-only: the administrator answers only; decided reviews are read-only.
- Offline: not available offline: reviews are made online. D38 keeps only today's schedule, time and intervention
  records offline. A banner says the connection is lost; what is on screen stays visible, every action is disabled and
  nothing is queued until the connection is back.

Shown entities (VD-15): [E-F19-14 Security and privacy review](../../data/e-f19-14-security-and-privacy-review.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F19-14 Security and privacy review | Open | Badge "Open"; a new record starts here; next: Passed, Changes or Rejected (UC-F19-06); fields editable within the role | U07, U48 | `u07-administrator/s-f19-24-security-and-privacy-e-f19-14-security-and-privacy-review-open-desktop-{light,dark}.png`, `u48-hosting-engineer/s-f19-24-security-and-privacy-e-f19-14-security-and-privacy-review-open-{desktop,phone}-{light,dark}.png` |
| E-F19-14 Security and privacy review | Passed | Badge "Passed"; final: read-only, no next state; the history shows how it got here | U07, U48 | `u07-administrator/s-f19-24-security-and-privacy-e-f19-14-security-and-privacy-review-passed-desktop-{light,dark}.png`, `u48-hosting-engineer/s-f19-24-security-and-privacy-e-f19-14-security-and-privacy-review-passed-{desktop,phone}-{light,dark}.png` |
| E-F19-14 Security and privacy review | Changes | Badge "Changes"; next: Open (UC-F19-06); fields editable within the role | U07, U48 | `u07-administrator/s-f19-24-security-and-privacy-e-f19-14-security-and-privacy-review-changes-desktop-{light,dark}.png`, `u48-hosting-engineer/s-f19-24-security-and-privacy-e-f19-14-security-and-privacy-review-changes-{desktop,phone}-{light,dark}.png` |
| E-F19-14 Security and privacy review | Rejected | Badge "Rejected"; final: read-only, no next state; the history shows how it got here | U07, U48 | `u07-administrator/s-f19-24-security-and-privacy-e-f19-14-security-and-privacy-review-rejected-desktop-{light,dark}.png`, `u48-hosting-engineer/s-f19-24-security-and-privacy-e-f19-14-security-and-privacy-review-rejected-{desktop,phone}-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop.

## Accessibility

Keyboard order follows the reading order; every control has a visible label; amounts, states and icons are also given as
text; status changes are announced to screen readers.

## Components

- [C-04 Card](../../../../04-ux/design-system/components/c-04-card.md)
- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)
- [C-10 Empty state](../../../../04-ux/design-system/components/c-10-empty-state.md)

## Shown in

- [FL-F19-02 Build and check](../../flows/fl-f19-02-build-and-check.md)

## Open questions

None.

---

⬅️ [S-F19-23 Ownership](../03-try-install-and-maintain/s-f19-23-ownership.md) · ⬆️ [Up](README.md) ·
➡️ [S-F19-25 Factory accounting](../05-bill-and-credit/s-f19-25-factory-accounting.md)
