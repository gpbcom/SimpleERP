🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🧰 [F14 Plugin store](../../README.md) › 🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-F14-03 Publish](README.md) ›
🖥️ S-F14-21 Dependency report

# 🖥️ S-F14-21 Dependency report

**Status:** ✅ specified

## Personas

- [U46 Plugin publisher](../../../../01-users/personas/u46-plugin-publisher.md), who reads their own reports
- [U11 IT provider administrator](../../../../01-users/personas/u11-provider-admin.md), who reads every report in the
  security review

## Purpose

Show a version's bill of materials with each dependency's licence, compatibility and vulnerabilities.

## Entry points

The automated checks of a submission; the security review; a rescan notification.

## Wireframe

```text
Gate Booking 2.4.0, dependencies           84 components   [Download CycloneDX]
-------------------------------------------------------------------------------
Component          Version    Licence        Compatible   Vulnerabilities
fastapi            0.115.2    MIT            yes          -
pdfgen-pro         3.1        Proprietary    NO           -
yaml-lib           6.0.1      MIT            yes          CVE-2026-1234 (high)
-------------------------------------------------------------------------------
Result: rejected, 1 licence incompatible, 1 vulnerability
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F14-03 step 5, U46 | desktop | ![FL-F14-03 step 5, U46, light](../../images/03-publish/u46-plugin-publisher/5-dependency-report-desktop-light.png) | ![FL-F14-03 step 5, U46, dark](../../images/03-publish/u46-plugin-publisher/5-dependency-report-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f14-21-dependency-report-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f14-21-dependency-report-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f14-21-dependency-report-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f14-21-dependency-report-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f14-21-dependency-report-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f14-21-dependency-report-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f14-21-dependency-report-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f14-21-dependency-report-offline-desktop-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Component | E-F14-14 component | name | no | yes |
| Version | E-F14-14 component | version | no | yes |
| Licence | E-F14-14 licence | SPDX identifier | no | yes |
| Compatible | E-F14-14 compatible | yes, no | no | yes |
| Vulnerabilities | E-F14-14 vulnerabilities | identifiers and severity | no | no |

## Actions

| Action | Where | Who | Result |
|---|---|---|---|
| Download | header | publisher, store operator | the bill of materials file |
| Filter | header | publisher, store operator | only incompatible or vulnerable components |

## States

- Normal: the version's components with their licence check and vulnerabilities, and the overall result.
- Empty: "No dependency": shown for a plugin with no third-party component.
- Loading: the frame and titles show at once with placeholder rows for the components; within 1 second (D408) the data
  replaces them, and a longer load shows a progress line saying what loads.
- Error: a bill of materials that differs from the lock files, with the components that differ.
- Read-only: always read-only: the report comes from the checks and cannot be edited.
- Offline: not available offline: the report is read from the store's servers. D38 keeps only today's schedule, time and
  intervention records offline. A banner says the connection is lost; what is on screen stays visible, every action is
  disabled and nothing is queued until the connection is back.

Shown entities (VD-15): [E-F14-07 Plugin check report](../../data/e-f14-07-plugin-check-report.md),
[E-F14-14 Software bill of materials](../../data/e-f14-14-software-bill-of-materials.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F14-07 Plugin check report | Recorded | Badge "Recorded"; a new record starts here; no other state; fields editable within the role | U11, U46 | `u11-provider-admin/s-f14-21-dependency-report-e-f14-07-plugin-check-report-recorded-desktop-{light,dark}.png`, `u46-plugin-publisher/s-f14-21-dependency-report-e-f14-07-plugin-check-report-recorded-desktop-{light,dark}.png` |
| E-F14-14 Software bill of materials | Generated | Badge "Generated"; a new record starts here; next: Checked (UC-F14-21); fields editable within the role | U11, U46 | `u11-provider-admin/s-f14-21-dependency-report-e-f14-14-software-bill-of-materials-generated-desktop-{light,dark}.png`, `u46-plugin-publisher/s-f14-21-dependency-report-e-f14-14-software-bill-of-materials-generated-desktop-{light,dark}.png` |
| E-F14-14 Software bill of materials | Checked | Badge "Checked"; next: Published (UC-F14-21); fields editable within the role | U11, U46 | `u11-provider-admin/s-f14-21-dependency-report-e-f14-14-software-bill-of-materials-checked-desktop-{light,dark}.png`, `u46-plugin-publisher/s-f14-21-dependency-report-e-f14-14-software-bill-of-materials-checked-desktop-{light,dark}.png` |
| E-F14-14 Software bill of materials | Published | Badge "Published"; next: Rescanned (BR-F14-16); fields editable within the role | U11, U46 | `u11-provider-admin/s-f14-21-dependency-report-e-f14-14-software-bill-of-materials-published-desktop-{light,dark}.png`, `u46-plugin-publisher/s-f14-21-dependency-report-e-f14-14-software-bill-of-materials-published-desktop-{light,dark}.png` |
| E-F14-14 Software bill of materials | Rescanned | Badge "Rescanned"; next: Published (UC-F14-21); fields editable within the role | U11, U46 | `u11-provider-admin/s-f14-21-dependency-report-e-f14-14-software-bill-of-materials-rescanned-desktop-{light,dark}.png`, `u46-plugin-publisher/s-f14-21-dependency-report-e-f14-14-software-bill-of-materials-rescanned-desktop-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop; tablet in one column; not on a phone.

## Accessibility

Keyboard order follows the reading order; every control has a visible label; amounts, states and icons are also given as
text; status changes are announced to screen readers.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-01 Button](../../../../04-ux/design-system/components/c-01-button.md)
- [C-10 Empty state](../../../../04-ux/design-system/components/c-10-empty-state.md)

## Shown in

- [FL-F14-03 Publish](../../flows/fl-f14-03-publish.md)

## Open questions

None.

---

⬅️ [S-F14-20 Store assistant](../01-find-and-install/s-f14-20-store-assistant.md) · ⬆️ [Up](README.md) ·
➡️ [S-F14-22 Plugin lifecycle](../07-plugin-end-of-life/s-f14-22-plugin-lifecycle.md)
