🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🧭 [F21 Onboarding and module activation](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F21-03 Team and data](README.md) › 🖥️ S-F21-23 Invite your accountant

# 🖥️ S-F21-23 Invite your accountant

**Status:** ✅ specified

## Personas

- [U13 Owner](../../../../01-users/personas/u13-owner.md)
- [U08 External accountant](../../../../01-users/personas/u08-external-accountant.md)

## Purpose

Invite the external accountant with the accountant role.

## Entry points

Guide, Team.

## Wireframe

```text
Invite your accountant
-------------------------------------------------------------------------------
Email: [compta@cabinet.example]   Firm: [Cabinet A]
Role: accountant (this company only)                 [Send]
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F21-03 step 4, U13 | desktop | ![FL-F21-03 step 4, U13, light](../../images/03-team-and-data/u13-owner/4-invite-your-accountant-desktop-light.png) | ![FL-F21-03 step 4, U13, dark](../../images/03-team-and-data/u13-owner/4-invite-your-accountant-desktop-dark.png) |
| FL-F21-03 step 4, U13 | phone | ![FL-F21-03 step 4, U13, light](../../images/03-team-and-data/u13-owner/4-invite-your-accountant-phone-light.png) | ![FL-F21-03 step 4, U13, dark](../../images/03-team-and-data/u13-owner/4-invite-your-accountant-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f21-23-invite-your-accountant-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f21-23-invite-your-accountant-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f21-23-invite-your-accountant-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f21-23-invite-your-accountant-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f21-23-invite-your-accountant-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f21-23-invite-your-accountant-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f21-23-invite-your-accountant-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f21-23-invite-your-accountant-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Email | E-F21-06 email | email | yes | yes |
| Firm | E-F21-06 | text | yes | no |

## Actions

| Action | Where | Who | Result |
|---|---|---|---|
| Send | footer | owner, administrator | invitation sent |

## States

- Normal: the form and the invitation's state.
- Empty: "No accountant yet".
- Loading: the frame and titles show at once with placeholder rows for the invitation; within 1 second (D408) the data
  replaces them, and a longer load shows a progress line saying what loads.
- Error: a bounced email.
- Read-only: the role is fixed.
- Offline: not available offline: invitations are sent online. D38 keeps only today's schedule, time and intervention
  records offline. A banner says the connection is lost; what is on screen stays visible, every action is disabled and
  nothing is queued until the connection is back.

Shown entities (VD-15): none; no flow's Entities and screens table names an entity on this screen.

## Responsive behaviour

Desktop and phone.

## Accessibility

Keyboard order follows the reading order; every control has a visible label; amounts, states and icons are also given as
text; status changes are announced to screen readers.

## Components

- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)
- [C-01 Button](../../../../04-ux/design-system/components/c-01-button.md)
- [C-10 Empty state](../../../../04-ux/design-system/components/c-10-empty-state.md)

## Shown in

- [FL-F21-03 Team and data](../../flows/fl-f21-03-team-and-data.md)

## Open questions

None.

---

⬅️ [S-F21-22 Opening balance check](../05-migration-from-another-tool/s-f21-22-opening-balance-check.md) ·
⬆️ [Up](README.md) · ➡️ [S-F21-24 Languages](../01-first-run/s-f21-24-languages.md)
