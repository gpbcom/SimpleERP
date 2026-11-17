🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🌐 [F18 Hosted websites and domains (hosted edition)](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F18-03 Domain and DNS](README.md) › 🖥️ S-F18-22 Redirects

# 🖥️ S-F18-22 Redirects

**Status:** ✅ specified

## Personas

- [U12 Marketing and communication](../../../../01-users/personas/u12-marketing.md)
- [U07 Administrator](../../../../01-users/personas/u07-administrator.md)

## Purpose

Map the old site's addresses to the new pages.

## Entry points

Site builder, Redirects; connecting an existing domain.

## Wireframe

```text
Redirects                                  [Import sitemap] [Import CSV]
-------------------------------------------------------------------------------
Old address         New page        Kind    Hits (30 d)
/nos-services       /services       moved   112
/promo-2019         -               gone    3
/equipe             ?               to map
-------------------------------------------------------------------------------
48 old addresses: 46 mapped, 1 gone, 1 to map
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F18-03 step 5, U12 | desktop | ![FL-F18-03 step 5, U12, light](../../images/03-domain-and-dns/u12-marketing/5-redirects-desktop-light.png) | ![FL-F18-03 step 5, U12, dark](../../images/03-domain-and-dns/u12-marketing/5-redirects-desktop-dark.png) |
| FL-F18-03 step 5, U12 | phone | ![FL-F18-03 step 5, U12, light](../../images/03-domain-and-dns/u12-marketing/5-redirects-phone-light.png) | ![FL-F18-03 step 5, U12, dark](../../images/03-domain-and-dns/u12-marketing/5-redirects-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f18-22-redirects-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f18-22-redirects-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f18-22-redirects-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f18-22-redirects-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f18-22-redirects-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f18-22-redirects-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f18-22-redirects-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f18-22-redirects-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Old address | E-F18-14 from | path | no | yes |
| New page | E-F18-14 to | page | yes | yes |
| Kind | E-F18-14 kind | moved, gone | yes | yes |
| Hits | E-F18-14 hits | number | no | no |

## Actions

| Action | Where | Who | Result |
|---|---|---|---|
| Import | header | marketing | old addresses listed with proposals |
| Map | row | marketing | target saved |
| Mark gone | row | marketing | answers "gone" |

## States

- Normal: old addresses with targets and hits.
- Empty: "No redirect": shown for a new site with no old one.
- Loading: the frame and titles show at once with placeholder rows for the addresses; within 1 second (D408) the data
  replaces them, and a longer load shows a progress line saying what loads.
- Error: a loop or an address without target, highlighted.
- Read-only: the owner reads.
- Offline: not available offline: redirects are set on the server. D38 keeps only today's schedule, time and
  intervention records offline. A banner says the connection is lost; what is on screen stays visible, every action is
  disabled and nothing is queued until the connection is back.

Shown entities (VD-15): [E-F18-14 Redirect](../../data/e-f18-14-redirect.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F18-14 Redirect | Active | Badge "Active"; a new record starts here; next: Removed (UC-F18-22); fields editable within the role | U07, U12 | `u07-administrator/s-f18-22-redirects-e-f18-14-redirect-active-desktop-{light,dark}.png`, `u12-marketing/s-f18-22-redirects-e-f18-14-redirect-active-{desktop,phone}-{light,dark}.png` |
| E-F18-14 Redirect | Removed | Badge "Removed"; final: read-only, no next state; the history shows how it got here | U07, U12 | `u07-administrator/s-f18-22-redirects-e-f18-14-redirect-removed-desktop-{light,dark}.png`, `u12-marketing/s-f18-22-redirects-e-f18-14-redirect-removed-{desktop,phone}-{light,dark}.png` |

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
- [C-12 File upload](../../../../04-ux/design-system/components/c-12-file-upload.md)
- [C-10 Empty state](../../../../04-ux/design-system/components/c-10-empty-state.md)

## Shown in

- [FL-F18-03 Domain and DNS](../../flows/fl-f18-03-domain-and-dns.md)

## Open questions

None.

---

⬅️ [S-F18-21 Blog](../06-content-and-search/s-f18-21-blog.md) · ⬆️ [Up](README.md) ·
➡️ [S-F18-23 Mailboxes](s-f18-23-mailboxes.md)
