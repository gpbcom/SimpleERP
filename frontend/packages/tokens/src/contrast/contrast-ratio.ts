const HEX_COLOUR = /^#[0-9a-fA-F]{6}$/;

function linearise(channel: number): number {
  const c = channel / 255;
  return c <= 0.04045 ? c / 12.92 : ((c + 0.055) / 1.055) ** 2.4;
}

/**
 * Compute the WCAG 2.x relative luminance of a colour.
 *
 * @param hex - A colour written `#RRGGBB`, in either case.
 * @returns The luminance, from 0 (black) to 1 (white).
 * @throws Error naming the value when it is not `#RRGGBB`.
 */
export function relativeLuminance(hex: string): number {
  if (typeof hex !== "string" || !HEX_COLOUR.test(hex)) {
    throw new Error(`Invalid colour: ${JSON.stringify(hex)}. Must be #RRGGBB.`);
  }
  const r = linearise(parseInt(hex.slice(1, 3), 16));
  const g = linearise(parseInt(hex.slice(3, 5), 16));
  const b = linearise(parseInt(hex.slice(5, 7), 16));
  return 0.2126 * r + 0.7152 * g + 0.0722 * b;
}

/**
 * Compute the WCAG 2.x contrast ratio of two colours.
 *
 * @param foreground - A colour written `#RRGGBB`.
 * @param background - A colour written `#RRGGBB`.
 * @returns The ratio, from 1 to 21, the same whichever colour comes first.
 * @throws Error naming the value when a colour is not `#RRGGBB`.
 */
export function contrastRatio(foreground: string, background: string): number {
  const a = relativeLuminance(foreground);
  const b = relativeLuminance(background);
  return (Math.max(a, b) + 0.05) / (Math.min(a, b) + 0.05);
}
