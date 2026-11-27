/** Raised when the token source cannot be read or holds an invalid value. */
export class TokenSourceError extends Error {
  /** The dotted path of the bad field, or an empty string for an unreadable or invalid JSON file. */
  readonly field: string;

  /**
   * @param field - The dotted path of the bad field, or an empty string.
   * @param message - The message, which never holds the whole content of the file.
   */
  constructor(field: string, message: string) {
    super(message);
    this.name = "TokenSourceError";
    this.field = field;
  }
}
