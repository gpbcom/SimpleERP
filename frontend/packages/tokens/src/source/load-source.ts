import { readFileSync } from "node:fs";

import { TokenSourceError } from "./token-source-error";
import type { TokenSource } from "./token-source";

type Json = Record<string, unknown>;

const TOP_LEVEL_KEYS = ["colors", "spacing", "density", "typography", "radius", "elevation", "fonts"];
const FONT_ROLES = ["heading", "body", "code"];
const HEX_COLOUR = /^#[0-9A-Fa-f]{6}$/;
const PIXELS = /^[0-9]+px$/;
const VALUE_MAX_LENGTH = 60;

/**
 * Build the error of one bad field.
 * @param field - The dotted path of the field.
 * @param value - The bad value, shown as JSON and cut when long.
 * @param rule - What the value must be.
 * @returns The error to throw.
 */
function invalid(field: string, value: unknown, rule: string): TokenSourceError {
  let shown = JSON.stringify(value) ?? "undefined";
  if (shown.length > VALUE_MAX_LENGTH) {
    shown = `${shown.slice(0, VALUE_MAX_LENGTH)}...`;
  }
  return new TokenSourceError(field, `Invalid ${field}: ${shown}. Must be ${rule}.`);
}

/**
 * Tell whether a value is a plain object.
 * @param value - The value to test.
 * @returns True for an object that is neither null nor an array.
 */
function isObject(value: unknown): value is Json {
  return typeof value === "object" && value !== null && !Array.isArray(value);
}

/**
 * Require an object.
 * @param field - The dotted path of the field.
 * @param value - The value to check.
 * @returns The object.
 */
function requireObject(field: string, value: unknown): Json {
  if (!isObject(value)) {
    throw invalid(field, value, "an object");
  }
  return value;
}

/**
 * Require a positive integer, booleans excluded.
 * @param field - The dotted path of the field.
 * @param value - The value to check.
 */
function requirePositiveInteger(field: string, value: unknown): void {
  if (typeof value !== "number" || !Number.isInteger(value) || value <= 0) {
    throw invalid(field, value, "a positive integer");
  }
}

/**
 * Require a non-empty string.
 * @param field - The dotted path of the field.
 * @param value - The value to check.
 */
function requireText(field: string, value: unknown): void {
  if (typeof value !== "string" || value.trim() === "") {
    throw invalid(field, value, "a non-empty string");
  }
}

/**
 * Require a font weight.
 * @param field - The dotted path of the field.
 * @param value - The value to check.
 */
function requireWeight(field: string, value: unknown): void {
  if (typeof value !== "number" || !Number.isInteger(value) || value < 100 || value > 900 || value % 100 !== 0) {
    throw invalid(field, value, "a multiple of 100 from 100 to 900");
  }
}

/**
 * Require the top-level keys to be exactly the seven sections.
 * @param source - The parsed file.
 */
function validateKeys(source: Json): void {
  for (const key of Object.keys(source)) {
    if (!TOP_LEVEL_KEYS.includes(key)) {
      throw invalid(key, source[key], `one of ${TOP_LEVEL_KEYS.join(", ")}`);
    }
  }
  for (const key of TOP_LEVEL_KEYS) {
    if (!(key in source)) {
      throw invalid(key, undefined, "present");
    }
  }
}

/**
 * Validate the colours: each one has a light and a dark hex value.
 * @param value - The `colors` section.
 */
function validateColors(value: unknown): void {
  const colors = requireObject("colors", value);
  for (const [name, colour] of Object.entries(colors)) {
    const entry = requireObject(`colors.${name}`, colour);
    for (const theme of ["light", "dark"]) {
      const hex = entry[theme];
      if (typeof hex !== "string" || !HEX_COLOUR.test(hex)) {
        throw invalid(`colors.${name}.${theme}`, hex, "a hex colour such as #4B4FCE");
      }
    }
  }
}

/**
 * Validate the spacing scale: positive multiples of 4.
 * @param value - The `spacing` section.
 */
function validateSpacing(value: unknown): void {
  if (!Array.isArray(value) || value.length === 0) {
    throw invalid("spacing", value, "a non-empty array");
  }
  value.forEach((step: unknown, index) => {
    if (typeof step !== "number" || !Number.isInteger(step) || step <= 0 || step % 4 !== 0) {
      throw invalid(`spacing.${index}`, step, "a positive multiple of 4");
    }
  });
}

/**
 * Validate the density entries.
 * @param value - The `density` section.
 */
function validateDensity(value: unknown): void {
  const density = requireObject("density", value);
  for (const [name, item] of Object.entries(density)) {
    const entry = requireObject(`density.${name}`, item);
    requirePositiveInteger(`density.${name}.comfortable`, entry.comfortable);
    requirePositiveInteger(`density.${name}.compact`, entry.compact);
  }
}

/**
 * Validate the font families and the typographic styles.
 * @param value - The `typography` section.
 */
function validateTypography(value: unknown): void {
  const typography = requireObject("typography", value);
  const families = requireObject("typography.families", typography.families);
  for (const role of FONT_ROLES) {
    requireText(`typography.families.${role}`, families[role]);
  }
  const styles = requireObject("typography.styles", typography.styles);
  for (const [name, item] of Object.entries(styles)) {
    const prefix = `typography.styles.${name}`;
    const style = requireObject(prefix, item);
    if (typeof style.family !== "string" || !FONT_ROLES.includes(style.family)) {
      throw invalid(`${prefix}.family`, style.family, `one of ${FONT_ROLES.join(", ")}`);
    }
    requirePositiveInteger(`${prefix}.sizePx`, style.sizePx);
    requirePositiveInteger(`${prefix}.lineHeightPx`, style.lineHeightPx);
    requireWeight(`${prefix}.weight`, style.weight);
  }
}

/**
 * Validate the corner radii.
 * @param value - The `radius` section.
 */
function validateRadius(value: unknown): void {
  const radius = requireObject("radius", value);
  for (const [name, item] of Object.entries(radius)) {
    if (typeof item !== "string" || !PIXELS.test(item)) {
      throw invalid(`radius.${name}`, item, "a pixel size such as 4px");
    }
  }
}

/**
 * Validate the elevations: a shadow per theme.
 * @param value - The `elevation` section.
 */
function validateElevation(value: unknown): void {
  const elevation = requireObject("elevation", value);
  for (const [name, item] of Object.entries(elevation)) {
    const entry = requireObject(`elevation.${name}`, item);
    requireText(`elevation.${name}.light`, entry.light);
    requireText(`elevation.${name}.dark`, entry.dark);
  }
}

/**
 * Validate the font files.
 * @param value - The `fonts` section.
 */
function validateFonts(value: unknown): void {
  if (!Array.isArray(value)) {
    throw invalid("fonts", value, "an array");
  }
  value.forEach((item: unknown, index) => {
    const prefix = `fonts.${index}`;
    const font = requireObject(prefix, item);
    requireText(`${prefix}.family`, font.family);
    requireText(`${prefix}.package`, font.package);
    requireWeight(`${prefix}.weight`, font.weight);
    if (typeof font.file !== "string" || !font.file.endsWith(".woff2")) {
      throw invalid(`${prefix}.file`, font.file, "a file name ending in .woff2");
    }
  });
}

/**
 * Read and validate the token source. Contrast is not checked here.
 * @param path - The path of the JSON file.
 * @returns The validated source.
 * @throws TokenSourceError When the file cannot be read, is not JSON, or holds an invalid value.
 */
export function loadSource(path: string): TokenSource {
  let parsed: unknown;
  try {
    parsed = JSON.parse(readFileSync(path, "utf-8"));
  } catch (error) {
    const reason = error instanceof Error ? error.name : "Error";
    throw new TokenSourceError("", `Invalid token source: ${reason} while reading ${path}. Must be a readable JSON file.`);
  }
  const source = requireObject("", parsed);
  validateKeys(source);
  validateColors(source.colors);
  validateSpacing(source.spacing);
  validateDensity(source.density);
  validateTypography(source.typography);
  validateRadius(source.radius);
  validateElevation(source.elevation);
  validateFonts(source.fonts);
  return source as unknown as TokenSource;
}
