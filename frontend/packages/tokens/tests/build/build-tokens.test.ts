import { existsSync, mkdtempSync, readFileSync, readdirSync, rmSync, writeFileSync } from "node:fs";
import { tmpdir } from "node:os";
import { join, resolve } from "node:path";
import { fileURLToPath, pathToFileURL } from "node:url";
import { afterAll, beforeAll, describe, expect, it } from "vitest";
import ts from "typescript";

import { buildTokens } from "../../src/build/build-tokens";
import { TokenSourceError } from "../../src/source/token-source-error";

const SOURCE_PATH = fileURLToPath(new URL("../../src/source/tokens.json", import.meta.url));

interface Style {
  family: string;
  sizePx: number;
  lineHeightPx: number;
  weight: number;
}

interface BuiltTokens {
  color: { light: Record<string, string>; dark: Record<string, string> };
  space: number[];
  density: { comfortable: Record<string, number>; compact: Record<string, number> };
  font: { families: Record<string, string>; styles: Record<string, Style> };
  radius: Record<string, string>;
  elevation: { light: Record<string, string>; dark: Record<string, string> };
}

interface MutableSource {
  colors: Record<string, { light: string; dark?: string }>;
  density: Record<string, { comfortable: number; compact: number }>;
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
];

const DENSITY: Array<[string, string, string]> = [
  ["row-height", "48px", "32px"],
  ["cell-padding", "12px", "6px"],
  ["field-height", "44px", "32px"],
  ["body-size", "16px", "14px"],
];

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

const RADIUS: Array<[string, string]> = [
  ["radius-card", "8px"],
  ["radius-field", "8px"],
  ["radius-panel", "12px"],
  ["radius-badge", "9999px"],
];

const ELEVATION_1 = "0 1px 2px rgba(28,31,36,.06), 0 2px 6px rgba(28,31,36,.08)";
const ELEVATION_2 = "0 8px 24px rgba(28,31,36,.14), 0 24px 56px rgba(28,31,36,.16)";

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

function readSource(): MutableSource {
  return JSON.parse(readFileSync(SOURCE_PATH, "utf-8")) as MutableSource;
}

function declaredValue(css: string, name: string): string {
  const match = new RegExp(`--${escapeRegExp(name)}\\s*:\\s*([^;]+);`).exec(css);
  if (match === null) {
    throw new Error(`No variable ${name}`);
  }
  return match[1].trim();
}

describe("buildTokens", () => {
  const folders: string[] = [];
  let counter = 0;

  function freshFolder(): string {
    const folder = mkdtempSync(join(tmpdir(), "tokens-build-"));
    folders.push(folder);
    return folder;
  }

  async function loadTokens(outDir: string): Promise<BuiltTokens> {
    counter += 1;
    const text = readFileSync(join(outDir, "tokens.ts"), "utf-8");
    const js = ts.transpileModule(text, {
      compilerOptions: { target: ts.ScriptTarget.ES2022, module: ts.ModuleKind.ESNext },
    }).outputText;
    const file = join(outDir, `tokens-${counter}.mjs`);
    writeFileSync(file, js, "utf-8");
    const loaded = (await import(pathToFileURL(file).href)) as { tokens: BuiltTokens };
    return loaded.tokens;
  }

  function writeSource(source: MutableSource): string {
    const path = join(freshFolder(), "tokens.json");
    writeFileSync(path, JSON.stringify(source), "utf-8");
    return path;
  }

  afterAll(() => {
    for (const folder of folders) {
      rmSync(folder, { recursive: true, force: true });
    }
  });

  describe("built from the real source", () => {
    let outDir = "";
    let css = "";
    let light = "";
    let dark = "";
    let systemDark = "";
    let root = "";
    let comfortable = "";
    let compact = "";
    let tokens: BuiltTokens;
    let written: string[] = [];

    beforeAll(async () => {
      outDir = freshFolder();
      written = buildTokens({ sourcePath: SOURCE_PATH, outDir }).files;
      css = readFileSync(join(outDir, "tokens.css"), "utf-8");
      light = blockBody(css, ':root, [data-theme="light"]');
      dark = blockBody(css, '[data-theme="dark"]');
      systemDark = blockBody(blockBody(css, "@media (prefers-color-scheme: dark)"), ':root:not([data-theme="light"])');
      root = blockBody(css, ":root");
      comfortable = blockBody(css, ':root, [data-density="comfortable"]');
      compact = blockBody(blockBody(css, "@media (min-width: 768px)"), '[data-density="compact"]');
      tokens = await loadTokens(outDir);
    });

    it("returns every path it wrote", () => {
      expect(written).toContain(join(outDir, "tokens.css"));
      expect(written).toContain(join(outDir, "tokens.ts"));
      for (const path of written) {
        expect(existsSync(path)).toBe(true);
      }
    });

    it.each(COLOURS)("writes %s with its light value in the light block", (name, lightValue) => {
      expect(declares(light, name, lightValue)).toBe(true);
    });

    it.each(COLOURS)("writes %s with its dark value in the dark block", (name, _light, darkValue) => {
      expect(declares(dark, name, darkValue)).toBe(true);
    });

    it.each(DENSITY)("writes the density token %s for comfortable and compact", (name, comfortableValue, compactValue) => {
      expect(declares(comfortable, name, comfortableValue)).toBe(true);
      expect(declares(compact, name, compactValue)).toBe(true);
    });

    it.each(FONTS)("writes the typography token %s", (name, value) => {
      expect(declares(root, name, value)).toBe(true);
    });

    it.each(RADIUS)("writes the radius token %s", (name, value) => {
      expect(declares(root, name, value)).toBe(true);
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

    it.each(COLOURS)("gives %s the same light and dark values in tokens.ts", (name, lightValue, darkValue) => {
      const key = name.replace(/^color-/, "");
      expect(tokens.color.light[key]).toBe(lightValue);
      expect(tokens.color.dark[key]).toBe(darkValue);
    });

    it("gives the same density values in tokens.ts", () => {
      expect(tokens.density.comfortable).toMatchObject({
        "row-height": 48,
        "cell-padding": 12,
        "field-height": 44,
        "body-size": 16,
      });
      expect(tokens.density.compact).toMatchObject({
        "row-height": 32,
        "cell-padding": 6,
        "field-height": 32,
        "body-size": 14,
      });
    });

    it("gives the same typography values in tokens.ts", () => {
      expect(tokens.font.styles.display).toEqual({ family: "heading", sizePx: 40, lineHeightPx: 48, weight: 800 });
      expect(tokens.font.styles.body).toEqual({ family: "body", sizePx: 16, lineHeightPx: 24, weight: 400 });
      expect(tokens.font.styles.code).toEqual({ family: "code", sizePx: 14, lineHeightPx: 20, weight: 400 });
      expect(Object.keys(tokens.font.styles)).toHaveLength(9);
    });

    it("holds the seven woff2 files, each a real woff2, and three licences", () => {
      const names = readdirSync(join(outDir, "fonts"));
      const woff = names.filter((name) => name.endsWith(".woff2"));
      expect(woff).toHaveLength(7);
      expect(names.filter((name) => name.startsWith("LICENSE-"))).toHaveLength(3);
      for (const name of woff) {
        const bytes = readFileSync(join(outDir, "fonts", name));
        expect(bytes.subarray(0, 4).toString("latin1")).toBe("wOF2");
      }
    });

    it("points every url() of tokens.css to a relative file that exists", () => {
      const urls = [...css.matchAll(/url\(\s*["']?([^"')]+)["']?\s*\)/g)].map((match) => match[1]);
      expect(urls.length).toBeGreaterThanOrEqual(7);
      for (const url of urls) {
        expect(url.startsWith("./fonts/")).toBe(true);
        expect(existsSync(resolve(outDir, url))).toBe(true);
      }
    });

    it.each(["http:", "https:", "//fonts.", "googleapis", "@import"])("holds no %s in the built files", (text) => {
      expect(css).not.toContain(text);
      expect(readFileSync(join(outDir, "tokens.ts"), "utf-8")).not.toContain(text);
    });

    it.each(["font-family-heading", "font-family-body", "font-family-code"])(
      "has an @font-face for the family of %s",
      (name) => {
        const family = /["']([^"']+)["']/.exec(declaredValue(css, name));
        expect(family).not.toBeNull();
        const faces = [...css.matchAll(/@font-face\s*\{([^}]*)\}/g)].map((match) => match[1]);
        const named = faces.filter((face) =>
          new RegExp(`font-family\\s*:\\s*["']?${escapeRegExp((family as RegExpExecArray)[1])}["']?\\s*;`).test(face),
        );
        expect(named.length).toBeGreaterThanOrEqual(1);
      },
    );
  });

  describe("after a value changes in the source", () => {
    it("follows the new primary colour and compact row height in both outputs", async () => {
      const source = readSource();
      source.colors.primary.light = "#123456";
      source.density["row-height"].compact = 28;
      const outDir = freshFolder();
      buildTokens({ sourcePath: writeSource(source), outDir });
      const css = readFileSync(join(outDir, "tokens.css"), "utf-8");
      expect(declares(blockBody(css, ':root, [data-theme="light"]'), "color-primary", "#123456")).toBe(true);
      expect(css).toContain("--row-height: 28px");
      expect(css).not.toContain("--color-primary: #4B4FC9");
      const tokens = await loadTokens(outDir);
      expect(tokens.color.light.primary).toBe("#123456");
      expect(tokens.density.compact["row-height"]).toBe(28);
    });
  });

  describe("given an invalid source", () => {
    it("refuses a colour without dark and writes no tokens.css", () => {
      const source = readSource();
      delete source.colors.primary.dark;
      const outDir = freshFolder();
      expect(() => buildTokens({ sourcePath: writeSource(source), outDir })).toThrow(TokenSourceError);
      expect(existsSync(join(outDir, "tokens.css"))).toBe(false);
    });
  });

  describe("run twice", () => {
    it("gives the same tokens.css and tokens.ts into the same folder", () => {
      const outDir = freshFolder();
      buildTokens({ sourcePath: SOURCE_PATH, outDir });
      const first = [readFileSync(join(outDir, "tokens.css"), "utf-8"), readFileSync(join(outDir, "tokens.ts"), "utf-8")];
      buildTokens({ sourcePath: SOURCE_PATH, outDir });
      const second = [readFileSync(join(outDir, "tokens.css"), "utf-8"), readFileSync(join(outDir, "tokens.ts"), "utf-8")];
      expect(second).toEqual(first);
    });
  });
});
