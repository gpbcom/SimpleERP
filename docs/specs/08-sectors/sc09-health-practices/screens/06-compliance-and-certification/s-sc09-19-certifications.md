🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🩺 [SC09 Health practices](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC09-06 Compliance and certification](README.md) ›
🖥️ S-SC09-19 Certifications

# 🖥️ S-SC09-19 Certifications

**Status:** ✅ specified

## Personas

- [U11 IT provider administrator](../../../../01-users/personas/u11-provider-admin.md)
- [U07 Administrator](../../../../01-users/personas/u07-administrator.md)

## Purpose

Keep each certified module's approvals (such as SESAM-Vitale) and its Ségur referencing current: an expired approval
disables the module, while a lapsed Ségur referencing, a State funding scheme and not an obligation of the practice,
only warns the provider ([BR-SC09-15](../../business-rules/br-sc09-15-certifications-kept-current.md),
[UC-SC09-19](../../use-cases/06-compliance-and-certification/uc-sc09-19-keep-the-software-s-certifications-current.md)).

## Entry points

Health practices in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC09-06 step 3, U11 | desktop | ![FL-SC09-06 step 3, U11, light](../../images/06-compliance-and-certification/u11-provider-admin/3-certifications-desktop-light.png) | ![FL-SC09-06 step 3, U11, dark](../../images/06-compliance-and-certification/u11-provider-admin/3-certifications-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc09-19-certifications-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc09-19-certifications-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc09-19-certifications-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc09-19-certifications-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc09-19-certifications-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc09-19-certifications-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-sc09-19-certifications-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-sc09-19-certifications-offline-desktop-dark.png) |

## Fields and columns

The fields of [E-SC09-13 Certified module](../../data/e-sc09-13-certified-module.md), shown as the entity pages list
them, with their examples.

## Actions

- Track versions:
  [UC-SC09-19](../../use-cases/06-compliance-and-certification/uc-sc09-19-keep-the-software-s-certifications-current.md)).
  step 1.
- Renew approvals:
  [UC-SC09-19](../../use-cases/06-compliance-and-certification/uc-sc09-19-keep-the-software-s-certifications-current.md)).
  step 2.
- Update practices:
  [UC-SC09-19](../../use-cases/06-compliance-and-certification/uc-sc09-19-keep-the-software-s-certifications-current.md)).
  step 3.
- Check:
  [UC-SC09-19](../../use-cases/06-compliance-and-certification/uc-sc09-19-keep-the-software-s-certifications-current.md)).
  step 4.

## States

- Normal: certified modules with version, approval or Ségur referencing, and validity; a referencing that lapses soon
  shows a warning, the module stays on.
- Empty: "No certified module".
- Loading: the frame and titles show at once with placeholder rows; within 1 second
  ([D408](../../../../06-decisions/technical/d408-performance-and-profiles.md)) the data replaces them, and a longer
  load shows a progress line saying what loads.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)) says what failed
  and what to do; what was typed is kept. For example, an expired approval: the module is disabled
  ([BR-SC09-15](../../business-rules/br-sc09-15-certifications-kept-current.md)); a lapsed Ségur referencing is a
  warning, not an error.
- Read-only: practices read the state only.
- Offline: not available offline: work on health data that stays on certified hosting. Offline work is kept for the
  phone forms of the field, [D38](../../../../06-decisions/ux/d38-offline-field-tasks.md),
  [UC-F2-22](../../../../02-functional/f02-no-code-configuration/use-cases/09-portals-and-offline-forms/uc-f02-22-fill-a-form-offline-on-the-phone.md).
  A banner says the connection is lost; what is on screen stays visible, every action is disabled and nothing is queued
  until the connection is back.

Shown entities (VD-15): [E-SC09-13 Certified module](../../data/e-sc09-13-certified-module.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC09-13 Certified module | Approved | Badge "Approved"; a new record starts here; next: Certified (UC-SC09-19); fields editable within the role | U07, U11 | `u07-administrator/s-sc09-19-certifications-e-sc09-13-certified-module-approved-desktop-{light,dark}.png`, `u11-provider-admin/s-sc09-19-certifications-e-sc09-13-certified-module-approved-desktop-{light,dark}.png` |
| E-SC09-13 Certified module | Certified | Badge "Certified"; next: Expired (UC-SC09-19); fields editable within the role | U07, U11 | `u07-administrator/s-sc09-19-certifications-e-sc09-13-certified-module-certified-desktop-{light,dark}.png`, `u11-provider-admin/s-sc09-19-certifications-e-sc09-13-certified-module-certified-desktop-{light,dark}.png` |
| E-SC09-13 Certified module | Expired | Badge "Expired"; final: read-only, no next state; the history shows how it got here | U07, U11 | `u07-administrator/s-sc09-19-certifications-e-sc09-13-certified-module-expired-desktop-{light,dark}.png`, `u11-provider-admin/s-sc09-19-certifications-e-sc09-13-certified-module-expired-desktop-{light,dark}.png` |

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

## Shown in

- [FL-SC09-06 Compliance and certification](../../flows/fl-sc09-06-compliance-and-certification.md)

## Open questions

None.

---

⬅️ [S-SC09-18 Quality indicator](s-sc09-18-quality-indicator.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC09-20 Practice assistant](../01-appointments/s-sc09-20-practice-assistant.md)
