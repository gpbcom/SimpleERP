import { copyFileSync, existsSync, mkdirSync } from "node:fs";
import { createRequire } from "node:module";
import { dirname, join } from "node:path";
import type { TokenSource } from "../source/token-source";
import { FontFileMissingError } from "./font-file-missing-error";

/**
 * Copy the font files of the source, and the licence of each package, into `<outDir>/fonts`.
 *
 * @param source - The token source and its font files.
 * @param outDir - The folder the package builds into.
 * @returns The paths written, in order.
 * @throws FontFileMissingError When a font file is not in its package.
 *
 * @remarks
 * The fonts are copied from pinned npm packages rather than linked, so that SimpleERP serves them itself and the
 * images hold them (D44). Each package's open font licence travels with its files. A second run overwrites.
 */
export function copyFonts(source: TokenSource, outDir: string): string[] {
  const require = createRequire(import.meta.url);
  const fontsDir = join(outDir, "fonts");
  mkdirSync(fontsDir, { recursive: true });
  const written: string[] = [];
  const licensed = new Set<string>();
  for (const font of source.fonts) {
    const root = dirname(require.resolve(`${font.package}/package.json`));
    const from = join(root, "files", font.file);
    if (!existsSync(from)) {
      throw new FontFileMissingError(font.file, font.package);
    }
    const to = join(fontsDir, font.file);
    copyFileSync(from, to);
    written.push(to);
    if (!licensed.has(font.package)) {
      licensed.add(font.package);
      const licence = join(fontsDir, `LICENSE-${font.package.replace(/^@[^/]+\//, "")}`);
      copyFileSync(join(root, "LICENSE"), licence);
      written.push(licence);
    }
  }
  return written;
}
