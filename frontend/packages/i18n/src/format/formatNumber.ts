const DECIMAL_STRING = /^-?\d+(\.\d+)?$/

/**
 * Format a number for a locale.
 *
 * A decimal string is passed to `Intl.NumberFormat` as a string and never converted to a number, so it stays exact.
 *
 * @param value - A finite number, or a decimal string such as `-12.50`.
 * @param locale - A BCP 47 language tag, such as `fr-FR`.
 * @param options - Options of `Intl.NumberFormat`.
 * @returns The formatted number.
 * @throws RangeError When the string is not a decimal or the number is not finite.
 */
export function formatNumber(
  value: number | string,
  locale: string,
  options?: Intl.NumberFormatOptions,
): string {
  if (typeof value === 'string') {
    if (!DECIMAL_STRING.test(value)) {
      throw new RangeError(`The value "${value}" is not a decimal string.`)
    }
  } else if (!Number.isFinite(value)) {
    throw new RangeError(`The value ${String(value)} is not a finite number.`)
  }
  return new Intl.NumberFormat(locale, options).format(value as number)
}
