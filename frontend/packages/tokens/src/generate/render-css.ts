import type { DensityValue, ThemeName, ThemedValue, TokenSource } from "../source/token-source";

/**
 * Writes the declarations of one block, one per line.
 *
 * @param declarations - The `[name, value]` pairs, the name without its `--`.
 * @param indent - The indentation of each line.
 * @returns The lines, each ending with a line break.
 *
 * @remarks
 * Values are copied unchanged, so the generated file is exactly what the source says.
 */
function renderDeclarations(declarations: Array<[string, string]>, indent: string): string {
  return declarations.map(([name, value]) => `${indent}--${name}: ${value};\n`).join("");
}

/**
 * Lists the declarations of one theme: the colours, then the elevations.
 *
 * @param source - The token source.
 * @param theme - The theme to write.
 * @returns The `[name, value]` pairs of the theme.
 *
 * @remarks
 * Blocks 2 to 4 (light, dark by attribute, dark by device setting) all use this helper, so the three
 * cannot drift apart. Each theme is written under an attribute selector so that the manual switch of
 * D43 wins, and under a media query so that the device's setting applies when nobody has chosen.
 */
function themeDeclarations(source: TokenSource, theme: ThemeName): Array<[string, string]> {
  const colours = Object.entries(source.colors) as Array<[string, ThemedValue]>;
  const elevations = Object.entries(source.elevation) as Array<[string, ThemedValue]>;
  return [
    ...colours.map(([key, value]): [string, string] => [`color-${key}`, value[theme]]),
    ...elevations.map(([key, value]): [string, string] => [`elevation-${key}`, value[theme]]),
  ];
}

/**
 * Lists the declarations of one density.
 *
 * @param source - The token source.
 * @param density - The density to write.
 * @returns The `[name, value]` pairs of the density, in pixels.
 */
function densityDeclarations(source: TokenSource, density: keyof DensityValue): Array<[string, string]> {
  return Object.entries(source.density).map(([key, value]): [string, string] => [key, `${value[density]}px`]);
}

/**
 * Lists the declarations that do not change with the theme or the density.
 *
 * @param source - The token source.
 * @returns The spacing, radii, font families and typographic styles.
 */
function baseDeclarations(source: TokenSource): Array<[string, string]> {
  const { families, styles } = source.typography;
  return [
    ...source.spacing.map((step): [string, string] => [`space-${step}`, `${step}px`]),
    ...Object.entries(source.radius).map(([key, value]): [string, string] => [`radius-${key}`, value]),
    ...Object.entries(families).map(([role, stack]): [string, string] => [`font-family-${role}`, stack]),
    ...Object.entries(styles).map(([name, style]): [string, string] => [
      `font-${name}`,
      `${style.weight} ${style.sizePx}px/${style.lineHeightPx}px ${families[style.family]}`,
    ]),
  ];
}

/**
 * Renders the design tokens as CSS custom properties.
 *
 * @param source - The token source.
 * @returns The stylesheet, with six blocks in order: the fixed tokens on `:root`, the light theme, the
 * dark theme, the dark theme for the device's setting, the comfortable density and the compact density.
 *
 * @remarks
 * - The themes use attribute selectors (`data-theme`), because D43 gives the person a manual switch that
 *   must override the device's setting: `[data-theme="light"]` also wins over the media query through
 *   `:root:not([data-theme="light"])`.
 * - The dark values are repeated under `@media (prefers-color-scheme: dark)`, because D43 makes the app
 *   follow the device's setting until the person chooses.
 * - The densities use `[data-density]` attributes (D42), and the compact set sits inside
 *   `@media (min-width: 768px)`, so phones (up to 767 px) always stay comfortable.
 */
export function renderCss(source: TokenSource): string {
  const blocks = [
    `:root {\n${renderDeclarations(baseDeclarations(source), "  ")}}\n`,
    `:root, [data-theme="light"] {\n${renderDeclarations(themeDeclarations(source, "light"), "  ")}}\n`,
    `[data-theme="dark"] {\n${renderDeclarations(themeDeclarations(source, "dark"), "  ")}}\n`,
    `@media (prefers-color-scheme: dark) {\n  :root:not([data-theme="light"]) {\n${renderDeclarations(
      themeDeclarations(source, "dark"),
      "    ",
    )}  }\n}\n`,
    `:root, [data-density="comfortable"] {\n${renderDeclarations(densityDeclarations(source, "comfortable"), "  ")}}\n`,
    `@media (min-width: 768px) {\n  [data-density="compact"] {\n${renderDeclarations(
      densityDeclarations(source, "compact"),
      "    ",
    )}  }\n}\n`,
  ];
  return blocks.join("\n");
}
