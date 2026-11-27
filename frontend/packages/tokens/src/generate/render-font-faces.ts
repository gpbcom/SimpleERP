import type { TokenSource } from "../source/token-source";

/**
 * Render one `@font-face` block per font file of the source.
 *
 * @param source - The token source and its font files.
 * @param fontsUrl - The relative folder the stylesheet loads the fonts from.
 * @returns The CSS text of every font face.
 *
 * @remarks
 * Every url is relative to the stylesheet and never remote: the fonts are served by SimpleERP itself, with no call to
 * a third party (D44).
 */
export function renderFontFaces(source: TokenSource, fontsUrl = "./fonts"): string {
  return source.fonts
    .map((font) =>
      [
        "@font-face {",
        `  font-family: "${font.family}";`,
        "  font-style: normal;",
        `  font-weight: ${font.weight};`,
        "  font-display: swap;",
        `  src: url("${fontsUrl}/${font.file}") format("woff2");`,
        "}",
      ].join("\n"),
    )
    .join("\n\n");
}
