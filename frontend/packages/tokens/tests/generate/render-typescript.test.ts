import { mkdtempSync, readFileSync, rmSync, writeFileSync } from "node:fs";
import { tmpdir } from "node:os";
import { join } from "node:path";
import { pathToFileURL } from "node:url";
import { afterAll, beforeAll, describe, expect, it } from "vitest";
import ts from "typescript";

import { renderTypeScript } from "../../src/generate/render-typescript";
import type { TokenSource } from "../../src/source/token-source";

interface Style {
  family: string;
  sizePx: number;
  lineHeightPx: number;
  weight: number;
}

interface RenderedTokens {
  color: { light: Record<string, string>; dark: Record<string, string> };
  space: number[];
  density: {
    comfortable: Record<string, number>;
    compact: Record<string, number>;
  };
  font: { families: Record<string, string>; styles: Record<string, Style> };
  radius: Record<string, string>;
  elevation: { light: Record<string, string>; dark: Record<string, string> };
}

const GENERATED_COMMENT = "// Generated from src/source/tokens.json by src/build/main.ts. Do not edit.";

const source = JSON.parse(
  readFileSync(new URL("../../src/source/tokens.json", import.meta.url), "utf-8"),
) as TokenSource;

const colourKeys = Object.keys(source.colors);
const colourCases = colourKeys.flatMap((key) => [
  [key, "light"],
  [key, "dark"],
]);

describe("renderTypeScript", () => {
  let folder = "";
  let tokens: RenderedTokens;
  let output = "";
  let counter = 0;

  async function load(text: string): Promise<RenderedTokens> {
    counter += 1;
    const js = ts.transpileModule(text, {
      compilerOptions: { target: ts.ScriptTarget.ES2022, module: ts.ModuleKind.ESNext },
    }).outputText;
    const file = join(folder, `module-${counter}.mjs`);
    writeFileSync(file, js, "utf-8");
    const loaded = (await import(pathToFileURL(file).href)) as { tokens: RenderedTokens };
    return loaded.tokens;
  }

  beforeAll(async () => {
    folder = mkdtempSync(join(tmpdir(), "tokens-ts-"));
    output = renderTypeScript(source);
    tokens = await load(output);
  });

  afterAll(() => {
    rmSync(folder, { recursive: true, force: true });
  });

  it("starts with the generated-file comment", () => {
    expect(output.startsWith(GENERATED_COMMENT)).toBe(true);
  });

  it("exports the tokens constant and its type", () => {
    expect(output).toContain("export const tokens = {");
    expect(output).toContain("} as const;");
    expect(output).toContain("export type Tokens = typeof tokens;");
  });

  it("type-checks with no diagnostics under strict mode", () => {
    const file = join(folder, "tokens.ts");
    writeFileSync(file, output, "utf-8");
    const program = ts.createProgram([file], {
      strict: true,
      noEmit: true,
      target: ts.ScriptTarget.ES2022,
      module: ts.ModuleKind.ESNext,
      moduleResolution: ts.ModuleResolutionKind.Bundler,
      types: [],
    });
    const diagnostics = ts
      .getPreEmitDiagnostics(program)
      .map((diagnostic) => ts.flattenDiagnosticMessageText(diagnostic.messageText, "\n"));
    expect(diagnostics).toEqual([]);
  });

  it("gives the primary colour in the light and dark themes", () => {
    expect(tokens.color.light.primary).toBe("#4B4FC9");
    expect(tokens.color.dark.primary).toBe("#A3A6FF");
  });

  it.each(colourCases)("copies the colour %s unchanged in the %s theme", (key, theme) => {
    const name = theme as "light" | "dark";
    expect(tokens.color[name][key]).toBe(source.colors[key][name]);
  });

  it("holds the same colour keys in both themes", () => {
    expect(Object.keys(tokens.color.light)).toEqual(colourKeys);
    expect(Object.keys(tokens.color.dark)).toEqual(colourKeys);
  });

  it("gives the compact row height", () => {
    expect(tokens.density.compact["row-height"]).toBe(32);
  });

  it("gives the comfortable body size", () => {
    expect(tokens.density.comfortable["body-size"]).toBe(16);
  });

  it("gives the display text style", () => {
    expect(tokens.font.styles.display).toEqual({
      family: "heading",
      sizePx: 40,
      lineHeightPx: 48,
      weight: 800,
    });
  });

  it("gives the spacing steps in pixels", () => {
    expect(tokens.space).toEqual([4, 8, 12, 16, 24, 32, 48]);
  });

  it("gives the panel radius", () => {
    expect(tokens.radius.panel).toBe("12px");
  });

  it("gives no shadow on the first dark elevation", () => {
    expect(tokens.elevation.dark["1"]).toBe("none");
  });

  it("follows a change of the source", async () => {
    const changed = structuredClone(source);
    changed.colors.primary.light = "#123456";
    const rendered = await load(renderTypeScript(changed));
    expect(rendered.color.light.primary).toBe("#123456");
  });

  it("holds no fonts key", () => {
    expect(Object.keys(tokens)).not.toContain("fonts");
  });
});
