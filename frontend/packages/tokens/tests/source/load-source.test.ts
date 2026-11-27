import { mkdtempSync, rmSync, writeFileSync } from "node:fs";
import { tmpdir } from "node:os";
import { join } from "node:path";
import { fileURLToPath } from "node:url";

import { afterAll, beforeAll, describe, expect, it } from "vitest";

import { loadSource } from "../../src/source/load-source";
import { TokenSourceError } from "../../src/source/token-source-error";

type Json = Record<string, unknown>;

function validSource(): Json {
  return {
    colors: { primary: { light: "#4B4FCE", dark: "#8A8DF0" } },
    spacing: [4, 8, 12],
    density: { row: { comfortable: 40, compact: 32 } },
    typography: {
      families: { heading: "Inter", body: "Inter", code: "JetBrains Mono" },
      styles: {
        title: { family: "heading", sizePx: 24, lineHeightPx: 32, weight: 600 },
      },
    },
    radius: { sm: "4px" },
    elevation: { card: { light: "0 1px 2px #0003", dark: "0 1px 2px #000" } },
    fonts: [{ family: "Inter", weight: 400, file: "inter-400.woff2", package: "@fontsource/inter" }],
  };
}

function mutated(change: (source: Json) => void): Json {
  const source = validSource();
  change(source);
  return source;
}

describe("loadSource", () => {
  let folder = "";
  let counter = 0;

  beforeAll(() => {
    folder = mkdtempSync(join(tmpdir(), "tokens-source-"));
  });

  afterAll(() => {
    rmSync(folder, { recursive: true, force: true });
  });

  function fixture(content: string): string {
    counter += 1;
    const path = join(folder, `source-${counter}.json`);
    writeFileSync(path, content, "utf-8");
    return path;
  }

  it("loads the real token source with seven spacing steps and four density entries", () => {
    const path = fileURLToPath(new URL("../../src/source/tokens.json", import.meta.url));
    const source = loadSource(path);
    expect(source.spacing).toHaveLength(7);
    expect(Object.keys(source.density)).toHaveLength(4);
  });

  it("loads a minimal valid source and returns it unchanged", () => {
    const expected = validSource();
    expect(loadSource(fixture(JSON.stringify(expected)))).toEqual(expected);
  });

  it("accepts a low-contrast colour because contrast is not its concern", () => {
    const source = mutated((s) => {
      s.colors = { primary: { light: "#FFFF00", dark: "#FFFFFF" } };
    });
    expect(loadSource(fixture(JSON.stringify(source))).colors.primary.light).toBe("#FFFF00");
  });

  it.each([
    ["a colour without a dark value", (s: Json) => { s.colors = { primary: { light: "#4B4FCE" } }; }, "colors.primary.dark"],
    ["a colour with a bad hex value", (s: Json) => { s.colors = { primary: { light: "#4B4FC", dark: "#8A8DF0" } }; }, "colors.primary.light"],
    ["a spacing step that is not on the 4 px grid", (s: Json) => { s.spacing = [4, 6]; }, "spacing.1"],
    ["a spacing step of zero", (s: Json) => { s.spacing = [0]; }, "spacing.0"],
    ["a negative compact density", (s: Json) => { s.density = { row: { comfortable: 40, compact: -1 } }; }, "density.row.compact"],
    [
      "a style family that is not one of the three",
      (s: Json) => { s.typography = { families: { heading: "Inter", body: "Inter", code: "Mono" }, styles: { title: { family: "display-font", sizePx: 24, lineHeightPx: 32, weight: 600 } } }; },
      "typography.styles.title.family",
    ],
    [
      "a weight that is not a multiple of 100",
      (s: Json) => { s.typography = { families: { heading: "Inter", body: "Inter", code: "Mono" }, styles: { title: { family: "heading", sizePx: 24, lineHeightPx: 32, weight: 450 } } }; },
      "typography.styles.title.weight",
    ],
    ["a radius that is not a pixel string", (s: Json) => { s.radius = { sm: 8 }; }, "radius.sm"],
    ["a font file that is not woff2", (s: Json) => { s.fonts = [{ family: "Inter", weight: 400, file: "inter.ttf", package: "@fontsource/inter" }]; }, "fonts.0.file"],
    ["an unknown top-level key", (s: Json) => { s.shadows = {}; }, "shadows"],
    ["a missing fonts key", (s: Json) => { delete s.fonts; }, "fonts"],
  ])("refuses %s", (_name, change, field) => {
    const path = fixture(JSON.stringify(mutated(change)));
    let caught: unknown;
    try {
      loadSource(path);
    } catch (error) {
      caught = error;
    }
    expect(caught).toBeInstanceOf(TokenSourceError);
    expect((caught as TokenSourceError).field).toBe(field);
    expect((caught as TokenSourceError).message.startsWith(`Invalid ${field}:`)).toBe(true);
  });

  it("refuses a file that is not valid JSON with an empty field", () => {
    const path = fixture("{ not json");
    let caught: unknown;
    try {
      loadSource(path);
    } catch (error) {
      caught = error;
    }
    expect(caught).toBeInstanceOf(TokenSourceError);
    expect((caught as TokenSourceError).field).toBe("");
  });

  it("refuses a file that cannot be read with an empty field", () => {
    expect(() => loadSource(join(folder, "missing.json"))).toThrow(TokenSourceError);
  });
});
