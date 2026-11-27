import { mkdirSync, rmSync, writeFileSync } from "node:fs";
import { join } from "node:path";

import { copyFonts } from "../generate/copy-fonts";
import { renderCss } from "../generate/render-css";
import { renderFontFaces } from "../generate/render-font-faces";
import { renderTypeScript } from "../generate/render-typescript";
import { loadSource } from "../source/load-source";

/** The inputs of one build. */
export interface BuildOptions {
  /** Path of the token source file. */
  sourcePath: string;
  /** Folder the build writes into. */
  outDir: string;
}

/** The result of one build. */
export interface BuildResult {
  /** Every path the build wrote. */
  files: string[];
}

/**
 * Build the tokens package: `tokens.css`, `tokens.ts` and the font files.
 *
 * The source is loaded first, so an invalid source leaves no `tokens.css`. Only `<outDir>/fonts` is removed before
 * writing, never the rest of `outDir`. The output is deterministic.
 *
 * @param options - The source path and the output folder.
 * @returns Every written path.
 */
export function buildTokens(options: BuildOptions): BuildResult {
  const source = loadSource(options.sourcePath);
  mkdirSync(options.outDir, { recursive: true });
  rmSync(join(options.outDir, "fonts"), { recursive: true, force: true });

  const cssPath = join(options.outDir, "tokens.css");
  const tsPath = join(options.outDir, "tokens.ts");
  writeFileSync(cssPath, `${renderFontFaces(source, "./fonts")}\n\n${renderCss(source)}`, "utf-8");
  writeFileSync(tsPath, renderTypeScript(source), "utf-8");
  const fonts = copyFonts(source, options.outDir);

  return { files: [cssPath, tsPath, ...fonts] };
}
