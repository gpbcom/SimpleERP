import { describe, expect, it } from 'vitest';

import { formatDate } from '../../src/format/formatDate';

function plain(text: string): string {
  return text.replace(/[\u202F\u00A0]/g, ' ');
}

describe('formatDate', () => {
  it('writes a long date in French for the fr-FR locale', () => {
    const result = formatDate('2027-01-18T10:00:00Z', 'fr-FR', { dateStyle: 'long', timeZone: 'UTC' });
    expect(plain(result)).toBe('18 janvier 2027');
  });

  it('writes a long date in English for the en-GB locale', () => {
    const result = formatDate('2027-01-18T10:00:00Z', 'en-GB', { dateStyle: 'long', timeZone: 'UTC' });
    expect(plain(result)).toBe('18 January 2027');
  });

  it.each([
    ['fr-FR', '05/01/2027'],
    ['en-US', '1/5/27'],
  ])('puts the day and the month in the order of the %s locale', (locale, expected) => {
    const result = formatDate('2027-01-05T10:00:00Z', locale, { dateStyle: 'short', timeZone: 'UTC' });
    expect(plain(result)).toBe(expected);
  });

  it('gives the same output for a Date and for its ISO string', () => {
    const options: Intl.DateTimeFormatOptions = { dateStyle: 'long', timeZone: 'UTC' };
    const iso = '2027-01-18T10:00:00Z';
    expect(formatDate(new Date(iso), 'fr-FR', options)).toBe(formatDate(iso, 'fr-FR', options));
  });

  it.each([
    ['a malformed string', 'not a date'],
    ['an invalid Date', new Date('x')],
  ])('throws a RangeError for %s', (_name, value) => {
    expect(() => formatDate(value, 'fr-FR', { timeZone: 'UTC' })).toThrow(RangeError);
  });
});
