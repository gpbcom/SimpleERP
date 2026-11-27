import { readFileSync } from "node:fs";
import { resolve } from "node:path";

import { describe, expect, it } from "vitest";

import { contrastRatio } from "../../src/contrast/contrast-ratio";

type Theme = "light" | "dark";
type Source = { colors: Record<string, Record<Theme, string>> };
type Row = [string, string, string, number];

const source = JSON.parse(readFileSync(resolve(__dirname, "../../src/source/tokens.json"), "utf-8")) as Source;
const lightText = ["primary", "success", "error", "warning", "text-muted"];
const darkText = ["primary", "accent", "success", "error", "warning", "text", "text-muted"];

function rows(): Row[] {
  const out: Row[] = [];
  const add = (theme: Theme, foreground: string, background: string, minimum: number): void => {
    const hex = foreground === "white" ? "#FFFFFF" : source.colors[foreground][theme];
    out.push([
      `${theme}: ${foreground} on ${background} at ${minimum}`,
      hex,
      source.colors[background][theme],
      minimum,
    ]);
  };
  for (const foreground of lightText) add("light", foreground, "surface", 4.5);
  add("light", "text", "surface", 7);
  add("light", "border-strong", "surface", 3);
  add("light", "white", "primary", 4.5);
  for (const foreground of darkText) add("dark", foreground, "surface", 7);
  add("dark", "border-strong", "surface", 4.5);
  for (const foreground of [...lightText, "text"]) add("light", foreground, "surface-alt", 4.5);
  add("light", "border-strong", "surface-alt", 3);
  for (const foreground of darkText) add("dark", foreground, "surface-alt", 4.5);
  add("dark", "border-strong", "surface-alt", 3);
  return out;
}

describe("text colour pairs", () => {
  it.each(rows())("%s", (_name, foreground, background, minimum) => {
    expect(contrastRatio(foreground, background)).toBeGreaterThanOrEqual(minimum);
  });
});
