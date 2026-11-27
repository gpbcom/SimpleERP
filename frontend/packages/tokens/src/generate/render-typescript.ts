import type { TokenSource } from "../source/token-source";

/** The first line of the generated module. */
const GENERATED_COMMENT = "// Generated from src/source/tokens.json by src/build/main.ts. Do not edit.";

/**
 * Pick one side of every `{a, b}` value of a token map.
 *
 * @param map - The tokens, each holding a value per variant.
 * @param variant - The variant to keep, such as `light` or `compact`.
 * @returns The same keys, in the same order, holding the value of the variant.
 */
function pick<V extends string, T>(map: Record<string, Record<V, T>>, variant: V): Record<string, T> {
  return Object.fromEntries(Object.entries(map).map(([key, value]) => [key, value[variant]]));
}

/**
 * Render the design tokens as a TypeScript module.
 *
 * The module exports the `tokens` constant, fixed with `as const`, and its type `Tokens`. Fonts are not part of it.
 *
 * @param source - The token source, as loaded from `src/source/tokens.json`.
 * @returns The text of the module.
 */
export function renderTypeScript(source: TokenSource): string {
  const tokens = {
    color: { light: pick(source.colors, "light"), dark: pick(source.colors, "dark") },
    space: source.spacing,
    density: { comfortable: pick(source.density, "comfortable"), compact: pick(source.density, "compact") },
    font: { families: source.typography.families, styles: source.typography.styles },
    radius: source.radius,
    elevation: { light: pick(source.elevation, "light"), dark: pick(source.elevation, "dark") },
  };
  return [
    GENERATED_COMMENT,
    `export const tokens = ${JSON.stringify(tokens, null, 2)} as const;`,
    "export type Tokens = typeof tokens;",
    "",
  ].join("\n");
}
