🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🌐 [F18 Hosted websites and domains (hosted edition)](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F18-01 Build the site](README.md) › 🖥️ S-F18-01 Site builder

# 🖥️ S-F18-01 Site builder

**Status:** ✅ specified

## Personas

- [U13 Owner](../../../../01-users/personas/u13-owner.md)
- [U12 Marketing](../../../../01-users/personas/u12-marketing.md)

## Purpose

Build the site with the guide.

## Entry points

Hosted websites and domains in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F18-01 step 1, U13 | desktop | ![FL-F18-01 step 1, U13, light](../../images/01-build-the-site/u13-owner/1-guide-desktop-light.png) | ![FL-F18-01 step 1, U13, dark](../../images/01-build-the-site/u13-owner/1-guide-desktop-dark.png) |
| FL-F18-01 step 1, U13 | phone | ![FL-F18-01 step 1, U13, light](../../images/01-build-the-site/u13-owner/1-guide-phone-light.png) | ![FL-F18-01 step 1, U13, dark](../../images/01-build-the-site/u13-owner/1-guide-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f18-01-site-builder-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f18-01-site-builder-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f18-01-site-builder-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f18-01-site-builder-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f18-01-site-builder-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f18-01-site-builder-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f18-01-site-builder-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f18-01-site-builder-offline-phone-dark.png) |

## Fields and columns

As its entities.

## Actions

As its use case's main flow.

## States

- Normal: the guide's questions with the live preview next to them.
- Empty: "Start your site": the first question.
- Loading: the frame and titles show at once with placeholder rows for the preview; within 1 second (D408) the data
  replaces them, and a longer load shows a progress line saying what loads.
- Error: the error message pattern (D122).
- Read-only: other roles see the preview only.
- Offline: not available offline: the builder works online. D38 keeps only today's schedule, time and intervention
  records offline. A banner says the connection is lost; what is on screen stays visible, every action is disabled and
  nothing is queued until the connection is back.

Shown entities (VD-15): [E-F18-01 Hosted website](../../data/e-f18-01-hosted-website.md),
[E-F18-02 Page](../../data/e-f18-02-page.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F18-01 Hosted website | New | Badge "New"; a new record starts here; next: Live (UC-F18-13); fields editable within the role | U12, U13 | `u12-marketing/s-f18-01-site-builder-e-f18-01-hosted-website-new-{desktop,phone}-{light,dark}.png`, `u13-owner/s-f18-01-site-builder-e-f18-01-hosted-website-new-{desktop,phone}-{light,dark}.png` |
| E-F18-01 Hosted website | Live | Badge "Live"; final: read-only, no next state; the history shows how it got here | U12, U13 | `u12-marketing/s-f18-01-site-builder-e-f18-01-hosted-website-live-{desktop,phone}-{light,dark}.png`, `u13-owner/s-f18-01-site-builder-e-f18-01-hosted-website-live-{desktop,phone}-{light,dark}.png` |
| E-F18-02 Page | Published | Badge "Published"; a new record starts here; next: Live (UC-F18-08); fields editable within the role | U12, U13 | `u12-marketing/s-f18-01-site-builder-e-f18-02-page-published-{desktop,phone}-{light,dark}.png`, `u13-owner/s-f18-01-site-builder-e-f18-02-page-published-{desktop,phone}-{light,dark}.png` |
| E-F18-02 Page | Live | Badge "Live"; next: Held (UC-F18-25); fields editable within the role | U12, U13 | `u12-marketing/s-f18-01-site-builder-e-f18-02-page-live-{desktop,phone}-{light,dark}.png`, `u13-owner/s-f18-01-site-builder-e-f18-02-page-live-{desktop,phone}-{light,dark}.png` |
| E-F18-02 Page | Held | Badge "Held"; next: Live (UC-F18-08); fields editable within the role | U12, U13 | `u12-marketing/s-f18-01-site-builder-e-f18-02-page-held-{desktop,phone}-{light,dark}.png`, `u13-owner/s-f18-01-site-builder-e-f18-02-page-held-{desktop,phone}-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop; approvals and receipts also on the phone.

## Accessibility

Labelled controls; amounts and states as text.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)
- [C-10 Empty state](../../../../04-ux/design-system/components/c-10-empty-state.md)

## Shown in

- [FL-F18-01 Build the site](../../flows/fl-f18-01-build-the-site.md)

## Open questions

None.

---

⬆️ [Up](README.md) · ➡️ [S-F18-02 Identity](s-f18-02-identity.md)
