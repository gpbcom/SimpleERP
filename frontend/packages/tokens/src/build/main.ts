import { dirname, resolve } from "node:path";
import { fileURLToPath } from "node:url";

import { FontFileMissingError } from "../generate/font-file-missing-error";
import { TokenSourceError } from "../source/token-source-error";
import { buildTokens } from "./build-tokens";

/**
 * Run the build of the tokens package: `src/source/tokens.json` into `dist/`.
 *
 * Prints one line per written file. A source or font error is printed to stderr and sets the exit code to 1.
 */
function main(): void {
  const root = resolve(dirname(fileURLToPath(import.meta.url)), "..", "..");
  try {
    const { files } = buildTokens({
      sourcePath: resolve(root, "src", "source", "tokens.json"),
      outDir: resolve(root, "dist"),
    });
    for (const file of files) {
      console.log(file);
    }
  } catch (error) {
    if (error instanceof TokenSourceError || error instanceof FontFileMissingError) {
      console.error(error.message);
      process.exitCode = 1;
      return;
    }
    throw error;
  }
}

main();
