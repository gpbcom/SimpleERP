/** Raised when a font file the token source names is not in its npm package. */
export class FontFileMissingError extends Error {
  /** The file name that was not found. */
  readonly file: string;

  /**
   * Create the error.
   *
   * @param file - The file name that was not found.
   * @param packageName - The npm package that should hold the file.
   */
  constructor(file: string, packageName: string) {
    super(`Font file not found: ${file}. Install the package ${packageName} with pnpm install.`);
    this.name = "FontFileMissingError";
    this.file = file;
  }
}
