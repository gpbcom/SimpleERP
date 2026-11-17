🏠 [Specs](../../README.md) › 🎨 [UX](../README.md) › 🎨 [Visual identity](README.md) › 🌈 Colours

# 🌈 Colours

**Status:** ✅ specified

## Palette

Chosen with [D41](../../06-decisions/ux/d41-indigo-primary.md): primary indigo `#4B4FC9`, accent amber `#F2B134`,
success `#2E7D32`, error `#C62828`. The other colours were proposed and confirmed by the owner. Contrast ratios below
are computed with the WCAG 2.x formula.

**Light mode:**

| Token | Value | Use | Contrast on white #FFFFFF | Passes | Source |
|---|---|---|---|---|---|
| `primary` | `#4B4FC9` | Buttons, links, active navigation, focus ring | 6.44:1 | AA text | chosen with D41 |
| `accent` | `#F2B134` | Highlights, badges, charts; never text on white | 1.89:1 | decoration only | chosen with D41 |
| `success` | `#2E7D32` | Success messages and states | 5.13:1 | AA text | chosen with D41 |
| `error` | `#C62828` | Errors and destructive actions | 5.62:1 | AA text | chosen with D41 |
| `warning` | `#8A5A00` | Warnings (text) | 5.93:1 | AA text | confirmed by the owner |
| `text` | `#1C1F24` | Body text | 16.52:1 | AAA text | confirmed by the owner |
| `text-muted` | `#5B6170` | Secondary text | 6.20:1 | AA text | confirmed by the owner |
| `surface` | `#FFFFFF` | Page and cards | 1.00:1 | decoration only | confirmed by the owner |
| `surface-alt` | `#F5F5FB` | Sidebar, table stripes | 1.09:1 | decoration only | confirmed by the owner |
| `border` | `#D9DAE6` | Dividers and card edges (decoration) | 1.39:1 | decoration only | confirmed by the owner |
| `border-strong` | `#7A7F92` | Edges of form fields and controls (WCAG 1.4.11) | 3.98:1 | AA large text and UI only | confirmed by the owner |

**Dark mode:**

| Token | Value | Use | Contrast on dark surface #14151C | Passes | Source |
|---|---|---|---|---|---|
| `primary` | `#A3A6FF` | Buttons, links, active navigation, focus ring | 8.20:1 | AAA text | confirmed by the owner |
| `accent` | `#F2B134` | Highlights, badges, charts | 9.63:1 | AAA text | confirmed by the owner |
| `success` | `#7BC67E` | Success messages and states | 8.86:1 | AAA text | confirmed by the owner |
| `error` | `#FF8A80` | Errors and destructive actions | 7.97:1 | AAA text | confirmed by the owner |
| `warning` | `#F2C46D` | Warnings (text) | 11.17:1 | AAA text | confirmed by the owner |
| `text` | `#ECEDF3` | Body text | 15.58:1 | AAA text | confirmed by the owner |
| `text-muted` | `#A6AABA` | Secondary text | 7.87:1 | AAA text | confirmed by the owner |
| `surface` | `#14151C` | Page and cards | 1.00:1 | decoration only | confirmed by the owner |
| `surface-alt` | `#1E2029` | Sidebar, table stripes | 1.12:1 | decoration only | confirmed by the owner |
| `border` | `#343747` | Dividers and card edges (decoration) | 1.55:1 | decoration only | confirmed by the owner |
| `border-strong` | `#7C8096` | Edges of form fields and controls (WCAG 1.4.11) | 4.67:1 | AA text | confirmed by the owner |

## Tokens

Each colour is a design token, with a light and a dark value: see [Tokens](../design-system/tokens.md).

## Contrast

- Text and icons meet WCAG 2.2 AA ([D46](../../06-decisions/ux/d46-accessibility-standard.md)): 4.5:1 for text, 3:1 for
  large text and UI parts.
- Primary on white: 6.44:1, so indigo links and buttons pass AA.
- White text on a primary button: 6.44:1, passes AA.
- Accent on white: 1.89:1, so the accent is never used for text or as the only sign of a state; it marks highlights next
  to a text or an icon.
- Dividers use `border` (decoration); the edges of form fields and controls use `border-strong`, 3.98:1 on white and
  4.67:1 on the dark surface, above the 3:1 that WCAG 1.4.11 asks for.
- Colour is never the only way to show a state: an icon or a word goes with it.

## Light and dark modes

Both, following the device's setting, with a manual switch per user. See
[D43](../../06-decisions/ux/d43-light-and-dark.md).

---

⬅️ [Logo](logo.md) · ⬆️ [Up](README.md) · ➡️ [Typography](typography.md)
