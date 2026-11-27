🏠 [Specs](../../README.md) › 🎨 [UX](../README.md) › 📐 [Design system](README.md) › 🎟️ Tokens

# 🎟️ Tokens

**Status:** ✅ specified

## Colour tokens

Values in [Colours](../visual-identity/colours.md).

| Token | Light | Dark |
|---|---|---|
| `color-primary` | `#4B4FC9` | `#A3A6FF` |
| `color-accent` | `#F2B134` | `#F2B134` |
| `color-success` | `#2E7D32` | `#7BC67E` |
| `color-error` | `#C62828` | `#FF8A80` |
| `color-warning` | `#8A5A00` | `#F2C46D` |
| `color-text` | `#1C1F24` | `#ECEDF3` |
| `color-text-muted` | `#5B6170` | `#A6AABA` |
| `color-surface` | `#FFFFFF` | `#14151C` |
| `color-surface-alt` | `#F5F5FB` | `#1E2029` |
| `color-border` | `#D9DAE6` | `#343747` |
| `color-border-strong` | `#7A7F92` | `#7C8096` |

## Spacing

A 4 px grid: 4, 8, 12, 16, 24, 32, 48. Density ([D42](../../06-decisions/ux/d42-density-per-role.md)) changes
the spacing inside tables, lists and forms:

| Token | Comfortable | Compact |
|---|---|---|
| `row-height` | 48 px | 32 px |
| `cell-padding` | 12 px | 6 px |
| `field-height` | 44 px | 32 px |
| `body-size` | 16 px | 14 px |

Phones always use comfortable values.

## Typography tokens

From the [typography scale](../visual-identity/typography.md): `font-display`, `font-h1` to `font-h3`, `font-body`,
`font-body-compact`, `font-label`, `font-caption`, `font-code`.

## Radius and elevation

Radius 8 px for cards and fields, 12 px for panels, full for badges. Two shadows: `elevation-1` for cards,
`elevation-2` for panels and modals; in dark mode, elevation is shown by lighter surfaces rather than shadows.

Values used by the mockup images since 2026-11-12:

| Token | Value |
|---|---|
| `elevation-1` | `0 1px 2px rgba(28,31,36,.06), 0 2px 6px rgba(28,31,36,.08)` |
| `elevation-2` | `0 8px 24px rgba(28,31,36,.14), 0 24px 56px rgba(28,31,36,.16)` |
| Dark raised card surface | `#1E2029` (the `surface-alt` value) |
| Dark raised panel and dialog surface | `#282A36` |

---

⬆️ [Up](README.md) · ➡️ [Layout grid](layout-grid.md)
