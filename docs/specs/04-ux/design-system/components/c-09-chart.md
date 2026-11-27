🏠 [Specs](../../../README.md) › 🎨 [UX](../../README.md) › 📐 [Design system](../README.md) › 🧩 [Components](README.md) ›
🧩 C-09 Chart

# 🧩 C-09 Chart

**Status:** ✅ specified

## Purpose

Shows a trend or a comparison at a glance on dashboards and reports; its figures are always available as a table.

## Anatomy

```text
Questions per day, by feature          [This month v] [Show as table]
  |        _/\
  |   ___/    \__/\        -- Search  -- Actions
  |__/                  \
  +------------------------------
   1 Nov                    30 Nov
Source: assistant usage, updated 10:02
```

A title, the controls (period, filters, table switch), the plot, a legend, and the source with its date.

**Example images** (its variants and states, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| Variants and states | desktop | ![Variants and states, light](../images/c-09-chart-desktop-light.png) | ![Variants and states, dark](../images/c-09-chart-desktop-dark.png) |

## Variants

- **Line:** a trend over time.
- **Bar:** a comparison between items; stacked bars for parts of a whole.
- **Figure:** one figure with its change, in Plus Jakarta Sans, the face of dashboard figures
  ([Typography](../../visual-identity/typography.md)).
- **Threshold:** a line or a band marking a limit, such as a cap over 80 %, as on
  [S-F3-13 Assistant usage dashboard](../../../02-functional/f03-assistant/screens/01-ask-the-assistant/s-f03-13-assistant-usage-dashboard.md).

## States

Loading (the frame with a spinner), empty (a [C-10 Empty state](c-10-empty-state.md): "No questions yet this
period."), partial (the last figures shown with their date when a source is unavailable, as in F5's statistics), error
(the [error message pattern](../patterns/error-messages.md)), threshold crossed (highlighted with an icon and a word).

## Tokens

Series colours, in this order: `color-primary`, `color-accent` (its stated use includes charts,
[Colours](../../visual-identity/colours.md)), `color-text-muted`, `color-success`; `color-error` and `color-warning`
only for limits and alerts. Gridlines in `color-border`; axes and labels in `font-caption` with tabular figures
([Typography](../../visual-identity/typography.md)).

## Accessibility

- Each chart has its table and a one-sentence summary; colours are never the only cue, as on
  [S-F3-13 Assistant usage dashboard](../../../02-functional/f03-assistant/screens/01-ask-the-assistant/s-f03-13-assistant-usage-dashboard.md);
  series also differ by markers or line styles and are labelled.
- The accent is never used alone to carry text on white ([Colours](../../visual-identity/colours.md)).
- No drawing animation when reduced motion is asked ([Motion](../../visual-identity/motion.md)).

## Do and don't

- Do start bar charts at zero.
- Do give the period and the source with its date.
- Don't use pie charts for more than three parts: use bars.
- Don't show a chart without its table.

## Used in

[S-F1-12 Users overview dashboard](../../../02-functional/f01-administration/screens/09-administration-reports/s-f01-12-users-overview-dashboard.md),
[S-F3-01 Assistant panel](../../../02-functional/f03-assistant/screens/01-ask-the-assistant/s-f03-01-assistant-panel.md)
and
[S-F3-13 Assistant usage dashboard](../../../02-functional/f03-assistant/screens/01-ask-the-assistant/s-f03-13-assistant-usage-dashboard.md);
and the role widgets of the home screens ([Views](../../views/README.md)).

## Open questions

None.

---

⬅️ [Navigation](c-08-navigation.md) · ⬆️ [Up](README.md) · ➡️ [Empty state](c-10-empty-state.md)
