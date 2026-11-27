/**
 * Format an exact decimal amount as money in a locale.
 *
 * The amount stays a string from end to end: converting it to a `number` would lose digits beyond 15 or 16
 * significant ones, and money is an exact decimal with its currency (REQ-T10-03). `Intl.NumberFormat.format` reads a
 * decimal string exactly.
 *
 * The result shows at least the minor digits of the currency, and every decimal the amount has beyond them. This
 * function pads and never rounds: rounding follows the country pack, which is not decided here.
 *
 * @param amount - The amount as a decimal string, such as `"-12.50"`.
 * @param currency - The ISO 4217 code, three capital letters, such as `"EUR"`.
 * @param locale - The BCP 47 tag that sets the separators and the symbol position, such as `"fr-FR"`.
 * @returns The formatted amount.
 * @throws RangeError When the amount or the currency is malformed.
 */
export function formatMoney(amount: string, currency: string, locale: string): string {
  if (!/^-?\d+(\.\d+)?$/.test(amount)) {
    throw new RangeError(`The amount "${amount}" is not a decimal number written with digits and a point.`);
  }
  if (!/^[A-Z]{3}$/.test(currency)) {
    throw new RangeError(`The currency "${currency}" is not an ISO 4217 code of three capital letters.`);
  }
  const minorDigits =
    new Intl.NumberFormat(locale, { style: "currency", currency }).resolvedOptions().minimumFractionDigits ?? 2;
  const ownDigits = amount.split(".")[1]?.length ?? 0;
  const formatter = new Intl.NumberFormat(locale, {
    style: "currency",
    currency,
    minimumFractionDigits: minorDigits,
    maximumFractionDigits: Math.max(minorDigits, ownDigits),
  });
  return formatter.format(amount as unknown as number);
}
