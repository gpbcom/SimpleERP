import { describe, expect, it } from "vitest";

import { readComponentStyles, tokenProperty } from "./component-styles";
import type { StyleDeclaration } from "./component-styles";

const COMPONENTS = ["UiButton", "UiFormField", "UiNavItem", "UiToast", "UiModal", "UiCard"];

const FOCUS_SELECTOR = /:focus-visible|:focus-within/;
const FORM_FIELD_SELECTOR = /:focus-visible|:focus-within|:focus\b/;
const WIDTH_PROPERTY = /^(outline|outline-width|border|border-width|border-[a-z]+|border-[a-z]+-width)$/;
const COLOUR_PROPERTY = /^(outline|outline-color|border|border-color|border-[a-z]+|border-[a-z]+-color)$/;

/**
 * Tells whether one rule draws a 2 px outline or border in the primary colour.
 *
 * @param declarations - The declarations of the rule.
 * @param primary - The CSS name of the primary colour token.
 * @returns Whether the rule has the width and the colour.
 */
function drawsPrimaryRing(declarations: StyleDeclaration[], primary: string): boolean {
  const wide = declarations.some((d) => WIDTH_PROPERTY.test(d.property) && /(^|[\s(])2px\b/.test(d.value));
  const coloured = declarations.some(
    (d) => COLOUR_PROPERTY.test(d.property) && d.value.includes(`var(${primary})`),
  );
  return wide && coloured;
}

describe("focus styles", () => {
  it.each(COMPONENTS)("%s shows a 2px primary ring when focused", (name) => {
    const { declarations } = readComponentStyles(name);
    const primary = tokenProperty("color-primary");
    const selector = name === "UiFormField" ? FORM_FIELD_SELECTOR : FOCUS_SELECTOR;
    const rules = new Map<number, StyleDeclaration[]>();
    for (const declaration of declarations.filter((d) => selector.test(d.selector))) {
      rules.set(declaration.rule, [...(rules.get(declaration.rule) ?? []), declaration]);
    }
    const found = [...rules.values()].some((rule) => drawsPrimaryRing(rule, primary));
    expect(found).toBe(true);
  });
});
