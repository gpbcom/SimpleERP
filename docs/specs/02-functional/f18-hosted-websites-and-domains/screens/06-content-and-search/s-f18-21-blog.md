🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🌐 [F18 Hosted websites and domains (hosted edition)](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F18-06 Content and search](README.md) › 🖥️ S-F18-21 Blog

# 🖥️ S-F18-21 Blog

**Status:** ✅ specified

## Personas

- [U12 Marketing and communication](../../../../01-users/personas/u12-marketing.md)

## Purpose

Manage the blog articles that come from F5 posts or are written here.

## Entry points

Site builder, Blog; the "post became an article" notification.

## Wireframe

```text
Blog                                                     [New article]
-------------------------------------------------------------------------------
Article            From        AI label   State      Date
Winter menu        F5 post     yes        preview    2026-11-12
Our new terrace    builder     no         live       2026-10-03
-------------------------------------------------------------------------------
[Article panel] title, excerpt, tags, images with alternative text
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F18-06 step 1, U12 | desktop | ![FL-F18-06 step 1, U12, light](../../images/06-content-and-search/u12-marketing/1-blog-desktop-light.png) | ![FL-F18-06 step 1, U12, dark](../../images/06-content-and-search/u12-marketing/1-blog-desktop-dark.png) |
| FL-F18-06 step 1, U12 | phone | ![FL-F18-06 step 1, U12, light](../../images/06-content-and-search/u12-marketing/1-blog-phone-light.png) | ![FL-F18-06 step 1, U12, dark](../../images/06-content-and-search/u12-marketing/1-blog-phone-dark.png) |
| Error E1, U12 | desktop | ![Error E1, U12, light](../../images/06-content-and-search/u12-marketing/e1-blog-refused-desktop-light.png) | ![Error E1, U12, dark](../../images/06-content-and-search/u12-marketing/e1-blog-refused-desktop-dark.png) |
| Error E1, U12 | phone | ![Error E1, U12, light](../../images/06-content-and-search/u12-marketing/e1-blog-refused-phone-light.png) | ![Error E1, U12, dark](../../images/06-content-and-search/u12-marketing/e1-blog-refused-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f18-21-blog-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f18-21-blog-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f18-21-blog-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f18-21-blog-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f18-21-blog-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f18-21-blog-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f18-21-blog-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f18-21-blog-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Title | E-F18-13 title | text | yes | yes |
| Excerpt, tags | E-F18-13 | text | yes | no |
| From | E-F18-13 post | F5 post or builder | no | yes |
| AI label | E-F18-13 AI label | yes, no | no | yes |
| State | E-F18-13 | preview, live, removed | no | yes |

## Actions

| Action | Where | Who | Result |
|---|---|---|---|
| New article | header | marketing | draft article |
| Edit | panel | marketing | changes on the preview |

## States

- Normal: articles with source, label and state.
- Empty: "No article yet": articles arrive from F5 posts, or write one.
- Loading: the frame and titles show at once with placeholder rows for the articles; within 1 second (D408) the data
  replaces them, and a longer load shows a progress line saying what loads.
- Error: an image without alternative text, flagged.
- Read-only: live articles are edited through the preview; others read.
- Offline: not available offline: the builder works online. D38 keeps only today's schedule, time and intervention
  records offline. A banner says the connection is lost; what is on screen stays visible, every action is disabled and
  nothing is queued until the connection is back.

Shown entities (VD-15): [E-F18-13 Blog article](../../data/e-f18-13-blog-article.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F18-13 Blog article | Preview | Badge "Preview"; a new record starts here; next: Live (UC-F18-21); fields editable within the role | U12 | `u12-marketing/s-f18-21-blog-e-f18-13-blog-article-preview-{desktop,phone}-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop; marketing reads on a phone.

## Accessibility

Keyboard order follows the reading order; every control has a visible label; amounts, states and icons are also given as
text; status changes are announced to screen readers.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)
- [C-12 File upload](../../../../04-ux/design-system/components/c-12-file-upload.md)
- [C-10 Empty state](../../../../04-ux/design-system/components/c-10-empty-state.md)

## Shown in

- [FL-F18-06 Content and search](../../flows/fl-f18-06-content-and-search.md)

## Open questions

None.

---

⬅️ [S-F18-20 Site health](../05-run-the-site/s-f18-20-site-health.md) · ⬆️ [Up](README.md) ·
➡️ [S-F18-22 Redirects](../03-domain-and-dns/s-f18-22-redirects.md)
