import { readFileSync } from "node:fs";
import { fileURLToPath, pathToFileURL, URL } from "node:url";
import postcss from "postcss";
import type { AtRule, ChildNode, Container, Declaration, Rule } from "postcss";

/** One CSS declaration of a component, with where it sits. */
export interface StyleDeclaration {
  /** The selector of the rule that holds it, empty outside a rule. */
  selector: string;
  property: string;
  value: string;
  /** The at-rules around it, outermost first, such as `@media (prefers-reduced-motion: reduce)`. */
  atRules: string[];
  /** Which `<style>` block of the file it comes from. */
  block: number;
  /** A number shared by every declaration of the same rule, unique in the file. */
  rule: number;
}

/** What the `<style>` blocks of one component file hold. */
export interface ComponentStyles {
  declarations: StyleDeclaration[];
  /** For each `<style>` block, the custom properties it declares itself. */
  localProperties: Array<Set<string>>;
}

const COMPONENTS_URL = new URL("../../src/components/", pathToFileURL(import.meta.filename).href);
const TOKENS_URL = new URL("../../../tokens/", pathToFileURL(import.meta.filename).href);

/**
 * Finds the rule and the at-rules above a declaration.
 *
 * @param declaration - The declaration to start from.
 * @returns The selector of the closest rule, the at-rules above it (outermost first) and the parent node.
 */
function locate(declaration: Declaration): { selector: string; atRules: string[]; parent: Container | undefined } {
  const parent = declaration.parent as Container | undefined;
  const selector = parent?.type === "rule" ? (parent as Rule).selector : "";
  const atRules: string[] = [];
  let node: ChildNode | Container | undefined = parent;
  while (node) {
    if (node.type === "atrule") {
      atRules.unshift(`@${(node as AtRule).name} ${(node as AtRule).params}`.trim());
    }
    node = node.parent as Container | undefined;
  }
  return { selector, atRules, parent };
}

/**
 * Reads the declarations of every `<style>` block of a component.
 *
 * @param name - The component name, such as `UiButton`.
 * @returns The declarations and, per block, the custom properties the block declares.
 *
 * @remarks
 * The read fails when the file does not exist, so a missing component fails its own test case.
 */
export function readComponentStyles(name: string): ComponentStyles {
  const source = readFileSync(fileURLToPath(new URL(`${name}.vue`, COMPONENTS_URL)), "utf-8");
  const declarations: StyleDeclaration[] = [];
  const localProperties: Array<Set<string>> = [];
  const ruleIds = new Map<Container | undefined, number>();
  const blocks = [...source.matchAll(/<style\b[^>]*>([\s\S]*?)<\/style>/g)];
  blocks.forEach((match, block) => {
    const locals = new Set<string>();
    localProperties.push(locals);
    postcss.parse(match[1] ?? "").walkDecls((declaration) => {
      const { selector, atRules, parent } = locate(declaration);
      if (!ruleIds.has(parent)) {
        ruleIds.set(parent, ruleIds.size);
      }
      if (declaration.prop.startsWith("--")) {
        locals.add(declaration.prop);
      }
      declarations.push({
        selector,
        property: declaration.prop,
        value: declaration.value,
        atRules,
        block,
        rule: ruleIds.get(parent) ?? 0,
      });
    });
  });
  return { declarations, localProperties };
}

/**
 * Reads the CSS custom properties the tokens package defines.
 *
 * @returns Every `--name` declared in the CSS entry named by the `./tokens.css` export of its `package.json`.
 */
export function readTokenProperties(): Set<string> {
  const manifest = JSON.parse(readFileSync(fileURLToPath(new URL("package.json", TOKENS_URL)), "utf-8")) as {
    exports: Record<string, string>;
  };
  const entry = manifest.exports["./tokens.css"];
  if (entry === undefined) {
    throw new Error("The tokens package has no ./tokens.css export.");
  }
  const properties = new Set<string>();
  postcss.parse(readFileSync(fileURLToPath(new URL(entry, TOKENS_URL)), "utf-8")).walkDecls((declaration) => {
    if (declaration.prop.startsWith("--")) {
      properties.add(declaration.prop);
    }
  });
  return properties;
}

/**
 * Gives the CSS name of a token, checked against the tokens package.
 *
 * @param token - The token name without its `--`, such as `color-primary`.
 * @returns The custom property, such as `--color-primary`.
 */
export function tokenProperty(token: string): string {
  const property = `--${token}`;
  if (!readTokenProperties().has(property)) {
    throw new Error(`The tokens package does not define ${property}.`);
  }
  return property;
}
