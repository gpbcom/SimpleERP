import { readFileSync } from "node:fs";
import { describe, expect, it } from "vitest";
import { renderFontFaces } from "../../src/generate/render-font-faces";
import type { TokenSource } from "../../src/source/token-source";

const source = JSON.parse(
  readFileSync(new URL("../../src/source/tokens.json", import.meta.url), "utf-8"),
) as TokenSource;

function weightsOf(css: string, family: string): number[] {
  const blocks = css.match(/@font-face\s*\{[^}]*\}/g) ?? [];
  return blocks
    .filter((block) => block.includes(`font-family: "${family}";`))
    .map((block) => Number(/font-weight:\s*(\d+);/.exec(block)?.[1]))
    .sort((a, b) => a - b);
}

function urlsOf(css: string): string[] {
  return [...css.matchAll(/url\(\s*["']?([^"')]+)["']?\s*\)/g)].map((match) => match[1]);
}

describe("renderFontFaces", () => {
  const css = renderFontFaces(source);

  it("writes one font face block per font of the source", () => {
    expect(css.match(/@font-face/g)).toHaveLength(7);
  });

  it.each([
    ["Plus Jakarta Sans", [600, 700, 800]],
    ["Inter", [400, 500, 600]],
    ["JetBrains Mono", [400]],
  ])("declares the weights of %s", (family, weights) => {
    expect(weightsOf(css, family)).toEqual(weights);
  });

  it("writes the style, display and format of every block", () => {
    expect(css.match(/font-style:\s*normal;/g)).toHaveLength(7);
    expect(css.match(/font-display:\s*swap;/g)).toHaveLength(7);
    expect(css.match(/format\("woff2"\)/g)).toHaveLength(7);
  });

  it("points every url at the fonts folder next to the stylesheet", () => {
    const urls = urlsOf(css);
    expect(urls).toHaveLength(7);
    for (const url of urls) {
      expect(url.startsWith("./fonts/")).toBe(true);
    }
  });

  it.each(["http:", "https:", "@import", "googleapis"])("holds no third party reference %s", (text) => {
    expect(css).not.toContain(text);
  });

  it("holds no protocol relative url", () => {
    expect(css).not.toMatch(/url\(\s*["']?\/\//);
  });

  it("uses a custom fonts url in every url", () => {
    const urls = urlsOf(renderFontFaces(source, "/assets/fonts"));
    expect(urls).toHaveLength(7);
    for (const url of urls) {
      expect(url.startsWith("/assets/fonts/")).toBe(true);
    }
  });
});
