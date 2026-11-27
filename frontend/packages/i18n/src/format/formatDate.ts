/**
 * Format a date for a locale.
 *
 * @param value - A `Date`, or a string in ISO 8601 form.
 * @param locale - A BCP 47 locale tag, such as `fr-FR`.
 * @param options - Options of `Intl.DateTimeFormat`. No default is added, so the time zone is the caller's choice.
 * @returns The date written as the locale writes it.
 * @throws {RangeError} When the value is not a valid date.
 */
export function formatDate(value: Date | string, locale: string, options?: Intl.DateTimeFormatOptions): string {
  const date = typeof value === 'string' ? new Date(value) : value;
  if (Number.isNaN(date.getTime())) {
    throw new RangeError('The value is not a valid date. Give a Date or an ISO 8601 string.');
  }
  return new Intl.DateTimeFormat(locale, options).format(date);
}
