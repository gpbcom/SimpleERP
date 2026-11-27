import { readFileSync } from "node:fs";
import { resolve } from "node:path";
import { describe, expect, it } from "vitest";

import { renderCss } from "../../src/generate/render-css";
import type { TokenSource } from "../../src/source/token-source";

const SOURCE_PATH = resolve(__dirname, "../../src/source/tokens.json");

function readSource(): TokenSource {
  return JSON.parse(readFileSync(SOURCE_PATH, "utf-8")) as TokenSource;
}

function escapeRegExp(text: string): string {
  return text.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");
}

/** Finds the body of the rule whose selector is exactly `selector`, tolerant of whitespace. */
function blockBody(css: string, selector: string): string {
  const escaped = escapeRegExp(selector).replace(/,\s+/g, ",\\s*");
  const pattern = new RegExp(`(^|[}\\s;{])${escaped}\\s*\\{`);
  const match = pattern.exec(css);
  if (match === null) {
    throw new Error(`No block for selector ${selector}`);
  }
  const start = match.index + match[0].length;
  let depth = 1;
  let index = start;
  while (index < css.length && depth > 0) {
    if (css[index] === "{") depth += 1;
    if (css[index] === "}") depth -= 1;
    index += 1;
  }
  return css.slice(start, index - 1);
}

function declares(body: string, name: string, value: string): boolean {
  const pattern = new RegExp(`(^|[\\s;{])--${escapeRegExp(name)}\\s*:\\s*${escapeRegExp(value)}\\s*;`);
  return pattern.test(body);
}

const COLOURS: Array<[string, string, string]> = [
  ["color-primary", "#4B4FC9", "#A3A6FF"],
  ["color-accent", "#F2B134", "#F2B134"],
  ["color-success", "#2E7D32", "#7BC67E"],
  ["color-error", "#C62828", "#FF8A80"],
  ["color-warning", "#8A5A00", "#F2C46D"],
  ["color-text", "#1C1F24", "#ECEDF3"],
  ["color-text-muted", "#5B6170", "#A6AABA"],
  ["color-surface", "#FFFFFF", "#14151C"],
  ["color-surface-alt", "#F5F5FB", "#1E2029"],
  ["color-border", "#D9DAE6", "#343747"],
  ["color-border-strong", "#7A7F92", "#7C8096"],
  ["color-surface-raised-1", "#FFFFFF", "#1E2029"],
  ["color-surface-raised-2", "#FFFFFF", "#282A36"],
];

const ELEVATION_1 = "0 1px 2px rgba(28,31,36,.06), 0 2px 6px rgba(28,31,36,.08)";
const ELEVATION_2 = "0 8px 24px rgba(28,31,36,.14), 0 24px 56px rgba(28,31,36,.16)";

const FONTS: Array<[string, string]> = [
  ["font-display", '800 40px/48px "Plus Jakarta Sans", sans-serif'],
  ["font-h1", '700 32px/40px "Plus Jakarta Sans", sans-serif'],
  ["font-h2", '700 24px/32px "Plus Jakarta Sans", sans-serif'],
  ["font-h3", '600 20px/28px "Plus Jakarta Sans", sans-serif'],
  ["font-body", '400 16px/24px "Inter", sans-serif'],
  ["font-body-compact", '400 14px/20px "Inter", sans-serif'],
  ["font-label", '500 14px/20px "Inter", sans-serif'],
  ["font-caption", '400 12px/16px "Inter", sans-serif'],
  ["font-code", '400 14px/20px "JetBrains Mono", monospace'],
];

describe("renderCss", () => {
  const css = renderCss(readSource());
  const light = blockBody(css, ':root, [data-theme="light"]');
  const dark = blockBody(css, '[data-theme="dark"]');
  const media = blockBody(css, "@media (prefers-color-scheme: dark)");
  const systemDark = blockBody(media, ':root:not([data-theme="light"])');
  const root = blockBody(css, ":root");
  const comfortable = blockBody(css, ':root, [data-density="comfortable"]');
  const compactMedia = blockBody(css, "@media (min-width: 768px)");
  const compact = blockBody(compactMedia, '[data-density="compact"]');

  it.each(COLOURS)("writes %s in the light block with its light value", (name, lightValue) => {
    expect(declares(light, name, lightValue)).toBe(true);
  });

  it.each(COLOURS)("writes %s in the dark block with its dark value", (name, _light, darkValue) => {
    expect(declares(dark, name, darkValue)).toBe(true);
  });

  it.each(COLOURS)("writes %s in the prefers-color-scheme block with its dark value", (name, _light, darkValue) => {
    expect(declares(systemDark, name, darkValue)).toBe(true);
  });

  it("writes the elevation shadows in light and none in dark", () => {
    expect(declares(light, "elevation-1", ELEVATION_1)).toBe(true);
    expect(declares(light, "elevation-2", ELEVATION_2)).toBe(true);
    for (const body of [dark, systemDark]) {
      expect(declares(body, "elevation-1", "none")).toBe(true);
      expect(declares(body, "elevation-2", "none")).toBe(true);
    }
  });

  it.each([4, 8, 12, 16, 24, 32, 48])("writes the spacing step %i", (step) => {
    expect(declares(root, `space-${step}`, `${step}px`)).toBe(true);
  });

  it.each([
    ["row-height", "48px", "32px"],
    ["cell-padding", "12px", "6px"],
    ["field-height", "44px", "32px"],
    ["body-size", "16px", "14px"],
  ])("writes the density token %s for comfortable and compact", (name, comfortableValue, compactValue) => {
    expect(declares(comfortable, name, comfortableValue)).toBe(true);
    expect(declares(compact, name, compactValue)).toBe(true);
  });

  it("keeps the compact density inside the media query, so phones stay comfortable", () => {
    expect(css.indexOf('[data-density="compact"]')).toBeGreaterThan(css.indexOf("@media (min-width: 768px)"));
    expect(comfortable).not.toContain("compact");
  });

  it.each(FONTS)("writes the typography token %s", (name, value) => {
    expect(declares(root, name, value)).toBe(true);
  });

  it.each([
    ["radius-card", "8px"],
    ["radius-field", "8px"],
    ["radius-panel", "12px"],
    ["radius-badge", "9999px"],
  ])("writes the radius token %s", (name, value) => {
    expect(declares(root, name, value)).toBe(true);
  });

  it("follows a changed colour in the source", () => {
    const source = readSource();
    source.colors.primary.light = "#123456";
    const changed = blockBody(renderCss(source), ':root, [data-theme="light"]');
    expect(declares(changed, "color-primary", "#123456")).toBe(true);
  });

  it("holds no url( and no http", () => {
    expect(css).not.toContain("url(");
    expect(css).not.toContain("http");
  });
});
