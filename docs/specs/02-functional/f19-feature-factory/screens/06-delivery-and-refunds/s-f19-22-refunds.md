🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🏭 [F19 Feature factory (hosted edition)](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F19-06 Delivery and refunds](README.md) › 🖥️ S-F19-22 Refunds

# 🖥️ S-F19-22 Refunds

**Status:** ✅ specified

## Personas

- [U05 Accounting](../../../../01-users/personas/u05-accounting.md)
- [U13 Owner](../../../../01-users/personas/u13-owner.md)

## Purpose

Propose, confirm or refuse refunds of features that failed acceptance or were unusable.

## Entry points

Factory billing, Refunds; a proposal notification.

## Wireframe

```text
Refunds
-------------------------------------------------------------------------------
Feature        Kind              Period    Amount     State
Gate booking   month credited    2027-02   300.00     proposed   [Confirm] [Refuse]
X export       closed, no charge -         -          issued
-------------------------------------------------------------------------------
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F19-06 step 2, U05 | desktop | ![FL-F19-06 step 2, U05, light](../../images/06-delivery-and-refunds/u05-accounting/2-refunds-desktop-light.png) | ![FL-F19-06 step 2, U05, dark](../../images/06-delivery-and-refunds/u05-accounting/2-refunds-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f19-22-refunds-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f19-22-refunds-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f19-22-refunds-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f19-22-refunds-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f19-22-refunds-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f19-22-refunds-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f19-22-refunds-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f19-22-refunds-offline-desktop-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Feature | E-F19-12 feature | name | no | yes |
| Kind | E-F19-12 kind | list | no | yes |
| Period | E-F19-12 period | month | no | for credits |
| Amount | E-F19-12 amount | EUR excl. VAT | no | yes |
| State | E-F19-12 | proposed, issued, refused | no | yes |

## Actions

| Action | Where | Who | Result |
|---|---|---|---|
| Confirm | row | accounting | credit note issued |
| Refuse | row | accounting | refused with the reason |

## States

- Normal: proposals and issued refunds.
- Empty: "No refund".
- Loading: the frame and titles show at once with placeholder rows for the refunds; within 1 second (D408) the data
  replaces them, and a longer load shows a progress line saying what loads.
- Error: a refusal without reason, refused.
- Read-only: the owner reads.
- Offline: not available offline: credit notes are issued online. D38 keeps only today's schedule, time and intervention
  records offline. A banner says the connection is lost; what is on screen stays visible, every action is disabled and
  nothing is queued until the connection is back.

Shown entities (VD-15): [E-F19-12 Feature refund](../../data/e-f19-12-feature-refund.md),
[E-F19-16 Feature defect](../../data/e-f19-16-feature-defect.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F19-12 Feature refund | Proposed | Badge "Proposed"; a new record starts here; next: Issued or Refused (UC-F19-22); fields editable within the role | U05, U13 | `u05-accounting/s-f19-22-refunds-e-f19-12-feature-refund-proposed-desktop-{light,dark}.png`, `u13-owner/s-f19-22-refunds-e-f19-12-feature-refund-proposed-{desktop,phone}-{light,dark}.png` |
| E-F19-12 Feature refund | Issued | Badge "Issued"; final: read-only, no next state; the history shows how it got here | U05, U13 | `u05-accounting/s-f19-22-refunds-e-f19-12-feature-refund-issued-desktop-{light,dark}.png`, `u13-owner/s-f19-22-refunds-e-f19-12-feature-refund-issued-{desktop,phone}-{light,dark}.png` |
| E-F19-12 Feature refund | Refused | Badge "Refused"; final: read-only, no next state; the history shows how it got here | U05, U13 | `u05-accounting/s-f19-22-refunds-e-f19-12-feature-refund-refused-desktop-{light,dark}.png`, `u13-owner/s-f19-22-refunds-e-f19-12-feature-refund-refused-{desktop,phone}-{light,dark}.png` |
| E-F19-16 Feature defect | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U05, U13 | `u05-accounting/s-f19-22-refunds-e-f19-16-feature-defect-active-desktop-{light,dark}.png`, `u13-owner/s-f19-22-refunds-e-f19-16-feature-defect-active-{desktop,phone}-{light,dark}.png` |

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

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-01 Button](../../../../04-ux/design-system/components/c-01-button.md)
- [C-10 Empty state](../../../../04-ux/design-system/components/c-10-empty-state.md)

## Shown in

- [FL-F19-06 Delivery and refunds](../../flows/fl-f19-06-delivery-and-refunds.md)

## Open questions

None.

---

⬅️ [S-F19-21 Delivery plan](../01-describe-and-order/s-f19-21-delivery-plan.md) · ⬆️ [Up](README.md) ·
➡️ [S-F19-23 Ownership](../03-try-install-and-maintain/s-f19-23-ownership.md)
