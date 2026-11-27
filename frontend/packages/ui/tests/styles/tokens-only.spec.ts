import { describe, expect, it } from "vitest";

import { readComponentStyles, readTokenProperties } from "./component-styles";
import type { StyleDeclaration } from "./component-styles";

const COMPONENTS = ["UiButton", "UiFormField", "UiNavItem", "UiToast", "UiModal", "UiCard", "UiIcon", "UiSpinner"];

const COLOUR_PROPERTY =
  /^(color|background|background-color|border|border-(?!radius)[a-z-]+|outline|outline-color|fill|stroke|caret-color|text-decoration-color)$/;
const SPACING_PROPERTY = /^(padding(-[a-z-]+)?|margin(-[a-z-]+)?|gap|row-gap|column-gap)$/;
const COLOUR_WORDS = new Set([
  "currentcolor",
  "transparent",
  "inherit",
  "none",
  "solid",
  "dashed",
  "color-mix",
  "in",
  "srgb",
]);
const VAR_CALL = /var\(\s*--[\w-]+\s*\)/g;

/**
 * Checks that a value is made only of `var(--...)` calls and the given words.
 *
 * @param value - The declaration value.
 * @param words - The other words allowed, in lower case.
 * @param numbers - Whether numbers, with `px` or `%`, are allowed.
 * @returns Whether the value stays inside the allowed set.
 */
function madeOf(value: string, words: Set<string>, numbers: boolean): boolean {
  let rest = value.replace(VAR_CALL, " ");
  if (numbers) {
    rest = rest.replace(/-?\d*\.?\d+(px|%)?/g, " ");
  }
  const found = rest.toLowerCase().match(/[#a-z0-9.%-]+/g) ?? [];
  return found.every((word) => words.has(word));
}

/**
 * Checks a spacing value: tokens, `0` and `auto`, or a `calc()` of tokens and plain numbers.
 *
 * @param value - The declaration value.
 * @returns Whether the value is accepted.
 */
function spacingValid(value: string): boolean {
  const rest = value.replace(VAR_CALL, " ");
  if (rest.includes("calc(")) {
    return /^[\s()+\-*/\d.]*$/.test(rest.replace(/calc\(/g, " "));
  }
  return madeOf(rest, new Set(["0", "auto"]), false);
}

/**
 * Lists the declarations of a component that break a rule.
 *
 * @param declarations - The declarations to look at.
 * @param applies - Whether the rule is about this property.
 * @param valid - Whether its value is accepted.
 * @returns One line per offender, with its selector, property and value.
 */
function offenders(
  declarations: StyleDeclaration[],
  applies: (property: string) => boolean,
  valid: (value: string) => boolean,
): string[] {
  return declarations
    .filter((d) => applies(d.property) && !valid(d.value))
    .map((d) => `${d.selector} { ${d.property}: ${d.value} }`);
}

describe("component styles", () => {
  it.each(COMPONENTS)("%s colours come from tokens, not from literals", (name) => {
    const { declarations } = readComponentStyles(name);
    const bad = offenders(
      declarations,
      (p) => COLOUR_PROPERTY.test(p),
      (v) => madeOf(v, COLOUR_WORDS, true),
    );
    expect(bad).toEqual([]);
  });

  it.each(COMPONENTS)("%s shadows and radii come from tokens", (name) => {
    const { declarations } = readComponentStyles(name);
    const shadows = offenders(
      declarations,
      (p) => p === "box-shadow",
      (v) => madeOf(v, new Set(["none"]), false),
    );
    const radii = offenders(
      declarations,
      (p) => p === "border-radius",
      (v) => madeOf(v, new Set(["0", "50%"]), false),
    );
    expect([...shadows, ...radii]).toEqual([]);
  });

  it.each(COMPONENTS)("%s spacing comes from tokens", (name) => {
    const { declarations } = readComponentStyles(name);
    expect(offenders(declarations, (p) => SPACING_PROPERTY.test(p), spacingValid)).toEqual([]);
  });

  it.each(COMPONENTS)("%s fonts come from tokens", (name) => {
    const { declarations } = readComponentStyles(name);
    const bad = offenders(
      declarations,
      (p) => p === "font-family" || p === "font-size",
      (v) => madeOf(v, new Set(["inherit"]), false),
    );
    expect(bad).toEqual([]);
  });

  it.each(COMPONENTS)("%s only uses custom properties that exist", (name) => {
    const { declarations, localProperties } = readComponentStyles(name);
    const tokens = readTokenProperties();
    const unknown = declarations.flatMap((d) =>
      [...d.value.matchAll(/var\(\s*(--[\w-]+)/g)]
        .map((match) => match[1] ?? "")
        .filter((property) => !tokens.has(property) && !localProperties[d.block]?.has(property))
        .map((property) => `${property} in ${d.selector}`),
    );
    expect(unknown).toEqual([]);
  });

  it.each(COMPONENTS)("%s has a reduced motion block when it moves", (name) => {
    const { declarations } = readComponentStyles(name);
    const moves = declarations.some((d) => /^(transition|animation)(-|$)/.test(d.property));
    const reduced = declarations.some((d) =>
      d.atRules.some((rule) => /^@media .*prefers-reduced-motion\s*:\s*reduce/.test(rule)),
    );
    expect(!moves || reduced).toBe(true);
  });
});
