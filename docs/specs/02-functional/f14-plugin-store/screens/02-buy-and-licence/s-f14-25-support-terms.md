🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🧰 [F14 Plugin store](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F14-02 Buy and licence](README.md) › 🖥️ S-F14-25 Support terms

# 🖥️ S-F14-25 Support terms

**Status:** ✅ specified

## Personas

- [U46 Plugin publisher](../../../../01-users/personas/u46-plugin-publisher.md), who sets terms and answers
- [U07 Administrator](../../../../01-users/personas/u07-administrator.md), who opens requests

## Purpose

State each paid plan's support terms and follow requests against them.

## Entry points

The publisher portal's plans; the installed plugin's "Get support" for administrators.

## Wireframe

```text
Gate Booking, support terms                    Record: 94 % within the term
-------------------------------------------------------------------------------
Plan    Channels   Languages      Hours              First response
team    email      FR, EN         weekdays 9 to 18   1 business day
pro     email,chat FR, EN         weekdays 8 to 20   4 business hours
-------------------------------------------------------------------------------
Open requests: 3   (1 due in 2 h)
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F14-02 step 5, U46 | desktop | ![FL-F14-02 step 5, U46, light](../../images/02-buy-and-licence/u46-plugin-publisher/5-support-terms-desktop-light.png) | ![FL-F14-02 step 5, U46, dark](../../images/02-buy-and-licence/u46-plugin-publisher/5-support-terms-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f14-25-support-terms-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f14-25-support-terms-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f14-25-support-terms-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f14-25-support-terms-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f14-25-support-terms-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f14-25-support-terms-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f14-25-support-terms-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f14-25-support-terms-offline-desktop-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Plan | E-F14-19 plan | name | no | yes |
| Channels | E-F14-19 channels | list | yes | yes |
| Languages | E-F14-19 languages | list | yes | yes |
| Hours | E-F14-19 hours | text | yes | yes |
| First response | E-F14-19 first response | duration | yes | yes |
| Record | E-F14-19 record | percent | no | no |

## Actions

| Action | Where | Who | Result |
|---|---|---|---|
| Set terms | plan row | publisher | terms saved, shown on the purchase screen |
| Open a request | installed plugin | administrator | request sent to the publisher |
| Answer | open requests | publisher | first response measured |

## States

- Normal: each plan's terms, the record and the open requests with their due times.
- Empty: "No paid plan": shown for a free plugin; "No open request" in the requests list.
- Loading: the frame and titles show at once with placeholder rows for the plans and requests; within 1 second (D408)
  the data replaces them, and a longer load shows a progress line saying what loads.
- Error: a paid plan without terms, refused at publishing.
- Read-only: administrators see the terms and their own requests; terms of past versions are read-only.
- Offline: not available offline: support requests need the network. D38 keeps only today's schedule, time and
  intervention records offline. A banner says the connection is lost; what is on screen stays visible, every action is
  disabled and nothing is queued until the connection is back.

Shown entities (VD-15): [E-F14-19 Support terms](../../data/e-f14-19-support-terms.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F14-19 Support terms | Published | Badge "Published"; a new record starts here; next: Changed (UC-F14-27); fields editable within the role | U07, U46 | `u07-administrator/s-f14-25-support-terms-e-f14-19-support-terms-published-desktop-{light,dark}.png`, `u46-plugin-publisher/s-f14-25-support-terms-e-f14-19-support-terms-published-desktop-{light,dark}.png` |
| E-F14-19 Support terms | Changed | Badge "Changed"; next: Published (UC-F14-27); fields editable within the role | U07, U46 | `u07-administrator/s-f14-25-support-terms-e-f14-19-support-terms-changed-desktop-{light,dark}.png`, `u46-plugin-publisher/s-f14-25-support-terms-e-f14-19-support-terms-changed-desktop-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop; administrators open requests on a phone.

## Accessibility

Keyboard order follows the reading order; every control has a visible label; amounts, states and icons are also given as
text; status changes are announced to screen readers.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)
- [C-10 Empty state](../../../../04-ux/design-system/components/c-10-empty-state.md)

## Shown in

- [FL-F14-02 Buy and licence](../../flows/fl-f14-02-buy-and-licence.md)

## Open questions

None.

---

⬅️ [S-F14-24 Translations](../03-publish/s-f14-24-translations.md) · ⬆️ [Up](README.md) ·
➡️ [S-F14-26 Version history](../06-release-channels-and-rollback/s-f14-26-version-history.md)
